# Lexmount Release Radar

用 Lexmount Web Fetch 抓取多个开源项目的 Releases Atom feed，抽取版本号、发布时间、链接和摘要，生成跨项目发布简报。

## 目标项目

- Playwright Python
- Browser Use
- Crawl4AI
- FastAPI
- Vite
- Next.js

每个项目保留最新 5 条发布记录，共 30 条。

## 运行

```powershell
# 本地校验
python .\release_radar.py --dry-run --env ..\lexmount-status-watch\.env

# 真实运行
python .\release_radar.py --engine http --env ..\lexmount-status-watch\.env
```

## 最终运行

- 运行时间：2026-10-19 23:17 左右，北京时间
- 仓库：6
- 成功：6
- 保留发布条目：30
- 输出目录：`artifacts/run-20261019T151735Z`

输出包括：

- `report.md`
- `releases.csv`
- `releases.jsonl`
- `summary.json`
- `run_manifest.json`
- `raw/*.json`
- `SHA256SUMS.txt`

## 说明

脚本会处理 Lexmount 渲染层把 XML 包进 HTML 后的特殊情况，并优先使用 `http` 引擎抓取 Atom feed。项目后续如果需要抓取动态文档，可切换浏览器引擎。

## 局限

- 只处理公开 Releases feed；
- Release 摘要来自 Atom content/summary，复杂 Markdown 可能有缺失；
- 不预测未发布版本，不抓取私有仓库。
