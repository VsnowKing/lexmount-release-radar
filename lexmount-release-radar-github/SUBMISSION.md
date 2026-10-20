# 提交草稿：开源项目发布追踪雷达

## 作品名称

```text
Lexmount Release Radar
```

## 想解决什么问题

```text
开源项目更新很快，Release 信息分散在多个仓库。开发者需要反复打开不同 Releases 页面才能知道哪些工具有新版本、哪些变更会影响自己的项目。
```

## 怎么做的，云平台参与了什么

```text
脚本读取 repos.json 中的六个公开 Releases Atom feed，逐个调用 Lexmount Web Fetch POST /v1/dom/dump。最终运行使用 http 引擎。云平台负责抓取 feed，本地脚本解析 Atom XML，抽取版本、更新时间、链接和摘要，生成 CSV、JSONL、Markdown 报告、调用索引和 SHA256 清单。
```

## 结果与发现

```text
运行时间：2026-10-19 23:17 左右，北京时间。
6 个仓库全部成功，共保留 30 条最新发布记录。

覆盖项目：
- Playwright Python
- Browser Use
- Crawl4AI
- FastAPI
- Vite
- Next.js

发现：Releases Atom 是稳定且结构化的公开入口，适合用 Web Fetch 做跨项目追踪；但某些抓取路径会把 XML 包装进 HTML，需要先恢复 Atom 片段再解析。
```

## 作品演示或运行材料链接

```text
[待填：GitHub / 网盘链接]
```

## 材料访问说明　选填

```text
材料包含 release_radar.py、repos.json、最终运行目录 artifacts/run-20261019T151735Z、report.md、releases.csv、releases.jsonl、raw/*.json、run_manifest.json 和 SHA256SUMS.txt。不包含 .env、API Key 或 Project ID。
```

## 是否基于已有项目或教程

```text
是。参考 Lexmount Web Fetch 官方文档中的 Dump DOM 接口；目标仓库、Atom 恢复解析、输出结构、真实运行和提交材料均为本次活动新增。
```

## 作者与联系信息

```text
实际作者：[待填]
分工：独立完成选题、feed 选择、脚本开发、真实运行、结果核验和文档，贡献 100%。
联系邮箱：[待填]
```
