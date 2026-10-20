# 方案：开源项目发布追踪雷达

## 任务

把多个开源项目的 Release feed 汇总成一页可核验的发布简报，帮助开发者快速看到新版本、时间和关键变更。

## Lexmount 参与

每个仓库调用：

```http
POST https://api.lexmount.cn/v1/dom/dump
```

请求目标为公开 `releases.atom` feed。最终运行使用 `engine_preference=http`。Lexmount 返回 Atom 内容、`request_id`、`dom_id`、`engine` 和 `final_url`，本地脚本解析 XML 并生成报告。

## 真实结果

- 仓库：6
- 成功：6/6
- 保留发布条目：30
- 每个仓库最新 5 条
- 输出目录：`artifacts/run-20261019T151735Z`

## 成果

- `releases.csv`：结构化发布表；
- `releases.jsonl`：便于程序处理；
- `report.md`：按项目分组的 Markdown 简报；
- `raw/*.json`：Lexmount 原始响应；
- `run_manifest.json`：调用索引；
- `SHA256SUMS.txt`：文件完整性清单。

## 核验方式

1. 打开每个 Release 链接；
2. 对照 raw JSON 中的 Atom 内容；
3. 检查 `request_id` 和 `dom_id`；
4. 校验 SHA256。

## 后续

可增加 Breaking Changes 分类、依赖影响提示、Slack/邮件订阅和两次运行 diff。
