#!/usr/bin/env python3
"""Fetch public GitHub release feeds through Lexmount and build a release radar."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

from lexapi import checksum_dir, compact, credentials, retry_call, run_stamp, utc_now, write_json

ROOT = Path(__file__).resolve().parent
ATOM = "{http://www.w3.org/2005/Atom}"


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data.strip())


def strip_html(value: str) -> str:
    parser = TextExtractor()
    parser.feed(value)
    return compact(" ".join(parser.parts), 1200)


def read_repos(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))["repos"]
    seen: set[str] = set()
    repos = []
    for item in data:
        repo_id = compact(item.get("id"), 80)
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", repo_id) or repo_id in seen:
            raise ValueError(f"invalid or duplicate repo id: {repo_id}")
        seen.add(repo_id)
        repos.append({"id": repo_id, "name": compact(item.get("name"), 120), "feed": compact(item.get("feed"), 1000)})
    if not repos:
        raise ValueError("no repositories configured")
    return repos


def parse_atom(xml_text: str) -> list[dict[str, str]]:
    # Some rendering engines wrap XML inside an HTML shell and turn void elements
    # such as <link/> into HTML-style <link>. Recover the Atom fragment first.
    feed_start = xml_text.find("<feed")
    feed_end = xml_text.rfind("</feed>")
    if feed_start >= 0 and feed_end > feed_start:
        xml_text = xml_text[feed_start:feed_end + len("</feed>")]
    xml_text = re.sub(r"<link\b([^>]*?)\s*/?>", r"<link\1/>", xml_text, flags=re.I)
    xml_text = re.sub(r"<media:thumbnail\b([^>]*?)\s*/?>\s*</media:thumbnail>", r"<media:thumbnail\1/>", xml_text, flags=re.I)
    root = ET.fromstring(xml_text.lstrip("\ufeff \t\r\n"))
    entries = []
    for entry in root.findall(f"{ATOM}entry"):
        entry_id = compact(entry.findtext(f"{ATOM}id"), 500)
        title = compact(entry.findtext(f"{ATOM}title"), 200)
        updated = compact(entry.findtext(f"{ATOM}updated"), 40)
        link = ""
        link_node = entry.find(f"{ATOM}link")
        if link_node is not None:
            link = compact(link_node.attrib.get("href"), 1000)
        content_node = entry.find(f"{ATOM}content")
        summary_node = entry.find(f"{ATOM}summary")
        content = strip_html((content_node.text if content_node is not None and content_node.text else "") or (summary_node.text if summary_node is not None and summary_node.text else ""))
        version_match = re.search(r"/releases/tag/([^/?#]+)", entry_id + "/" + link)
        version = unescape(version_match.group(1)) if version_match else title
        entries.append({
            "version": compact(version, 120),
            "title": title,
            "updated": updated,
            "link": link or entry_id,
            "highlights": content,
        })
    return entries


def render_report(generated_at: str, rows: list[dict], endpoint: str) -> str:
    success = sum(bool(r["ok"]) for r in rows)
    total_releases = sum(len(r["releases"]) for r in rows)
    lines = [
        "# 开源项目发布雷达",
        "",
        f"- 生成时间：`{generated_at}`",
        f"- 抓取服务：Lexmount Web Fetch `{endpoint}`",
        f"- 仓库数量：{len(rows)}",
        f"- 成功返回：{success}/{len(rows)}",
        f"- 保留发布条目：{total_releases}",
        "- 数据来源：各仓库公开 Releases Atom feed；本报告不猜测未发布内容。",
        "",
        "## 最新版本",
        "",
        "| 项目 | 最新版本 | 发布/更新时间 | Feed 状态 | 最新条目链接 |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        latest = row["releases"][0] if row["releases"] else {}
        lines.append(
            f"| {row['name']} | {latest.get('version') or '-'} | {latest.get('updated') or '-'} | `{row['status']}` | "
            f"{('[打开](' + latest['link'] + ')') if latest.get('link') else '-'} |"
        )

    lines.extend(["", "## 项目详情", ""])
    for row in rows:
        lines.extend([
            f"### {row['name']}",
            "",
            f"- Feed URL：<{row['feed']}>",
            f"- 最终 URL：{row.get('final_url') or '-'}",
            f"- Lexmount request_id：`{row.get('request_id') or '-'}`",
            f"- Lexmount dom_id：`{row.get('dom_id') or '-'}`",
            f"- Raw 文件：`{row.get('raw_relative') or '-'}`",
            "",
        ])
        if not row["releases"]:
            lines.extend(["- 未解析到 release 条目；请查看 raw JSON。", ""])
            continue
        for release in row["releases"]:
            lines.append(f"#### {release['version']} — {release['updated']}")
            if release["title"] and release["title"] != release["version"]:
                lines.append(f"- 标题：{release['title']}")
            lines.append(f"- 链接：<{release['link']}>")
            if release["highlights"]:
                lines.append(f"- 摘要：{compact(release['highlights'], 500)}")
            lines.append("")
    lines.extend([
        "## 核验步骤",
        "",
        "1. 打开各仓库 Releases 页面核对最新版本。",
        "2. 打开 `raw/*.json`，检查 Lexmount 抓取到的 Atom feed 内容。",
        "3. 对照 `run_manifest.json` 的 request_id 和 dom_id。",
        "4. 使用 `SHA256SUMS.txt` 核对文件完整性。",
        "",
    ])
    return "\n".join(lines)


def run(args: argparse.Namespace) -> int:
    env_path = args.env if args.env.is_absolute() else Path.cwd() / args.env
    repos_path = args.repos if args.repos.is_absolute() else Path.cwd() / args.repos
    repos = read_repos(repos_path)
    api_key, project_id, base_url = credentials(env_path)
    if args.dry_run:
        print("DRY-RUN OK")
        print(f"repos={len(repos)}")
        print(f"base_url={base_url}")
        print(f"api_key_present={bool(api_key)}")
        print(f"project_id_present={bool(project_id)}")
        return 0
    if not api_key or not project_id:
        print("Missing LEXMOUNT_API_KEY or LEXMOUNT_PROJECT_ID", file=sys.stderr)
        return 2

    generated_at = utc_now()
    out_dir = ROOT / "artifacts" / f"run-{run_stamp()}"
    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    endpoint = base_url + "/v1/dom/dump"
    rows = []
    calls = []

    for index, repo in enumerate(repos, 1):
        print(f"[{index}/{len(repos)}] {repo['name']}: {repo['feed']}")
        payload = {"url": repo["feed"], "options": {"engine_preference": args.engine, "timeout_ms": 30000}}
        response, http_status, attempts = retry_call(endpoint, payload, api_key, project_id, args.attempts, args.timeout)
        raw_path = raw_dir / f"{repo['id']}.json"
        write_json(raw_path, response)
        dom_id = compact(response.get("dom_id"), 100)
        request_id = compact(response.get("request_id"), 100) or compact(attempts[-1].get("request_id"), 100)
        html = response.get("html") if isinstance(response.get("html"), str) else ""
        releases = []
        parse_error = ""
        if html:
            try:
                releases = parse_atom(html)[:args.limit]
            except Exception as exc:
                parse_error = f"{type(exc).__name__}: {exc}"
        raw_relative = raw_path.relative_to(out_dir).as_posix()
        status = "ok" if releases else ("target_error" if response.get("status_code") not in (200, None) else "parse_error")
        row = {
            "id": repo["id"], "name": repo["name"], "feed": repo["feed"], "ok": bool(releases),
            "status": status, "parse_error": parse_error,
            "final_url": compact(response.get("final_url"), 1000),
            "target_status_code": response.get("status_code"), "engine": compact(response.get("engine"), 40),
            "request_id": request_id, "dom_id": dom_id, "releases": releases,
            "raw_relative": raw_relative, "attempts": attempts, "generated_at": generated_at,
        }
        rows.append(row)
        calls.append({
            "repo_id": repo["id"], "endpoint": endpoint, "feed_url": repo["feed"], "http_status": http_status,
            "target_status_code": response.get("status_code"), "lexmount_ok": bool(releases),
            "request_id": request_id, "dom_id": dom_id, "engine": row["engine"],
            "raw_file": raw_relative, "release_count": len(releases), "attempts": attempts,
        })

    report_path = out_dir / "report.md"
    summary_path = out_dir / "summary.json"
    csv_path = out_dir / "releases.csv"
    jsonl_path = out_dir / "releases.jsonl"
    manifest_path = out_dir / "run_manifest.json"
    report_path.write_text(render_report(generated_at, rows, endpoint), encoding="utf-8")
    write_json(summary_path, {"generated_at": generated_at, "endpoint": endpoint, "repos": len(rows), "success": sum(r["ok"] for r in rows), "results": rows})

    fields = ["repo", "version", "title", "updated", "link", "highlights", "feed_url", "request_id", "dom_id", "engine", "raw_file"]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            for release in row["releases"]:
                writer.writerow({
                    "repo": row["name"], **release, "feed_url": row["feed"], "request_id": row["request_id"],
                    "dom_id": row["dom_id"], "engine": row["engine"], "raw_file": row["raw_relative"],
                })

    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            for release in row["releases"]:
                handle.write(json.dumps({
                    "generated_at": generated_at, "repo": row["name"], "feed_url": row["feed"], **release,
                    "request_id": row["request_id"], "dom_id": row["dom_id"], "engine": row["engine"],
                    "raw_file": row["raw_relative"],
                }, ensure_ascii=False, separators=(",", ":")) + "\n")

    write_json(manifest_path, {"generated_at": generated_at, "endpoint": endpoint, "security_note": "No API key or project id is stored.", "calls": calls})
    files = [report_path, summary_path, csv_path, jsonl_path, manifest_path, *(raw_dir / f"{r['id']}.json" for r in rows)]
    checksum_dir(out_dir, files)
    print(f"Artifact directory: {out_dir}")
    print(f"Success: {sum(r['ok'] for r in rows)}/{len(rows)}; releases kept: {sum(len(r['releases']) for r in rows)}")
    print(f"Report: {report_path}")
    return 0 if all(r["ok"] for r in rows) else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env", type=Path, default=ROOT / ".env")
    parser.add_argument("--repos", type=Path, default=ROOT / "repos.json")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--engine", default="lightmount_dcl", choices=["http","chrome","chrome_cdp","lightmount_lite","lightmount_dcl","lightmount_domstable"])
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    try:
        raise SystemExit(run(parse_args()))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)



