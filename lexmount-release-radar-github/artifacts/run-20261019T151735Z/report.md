# 开源项目发布雷达

- 生成时间：`2026-10-19T15:17:35.238661Z`
- 抓取服务：Lexmount Web Fetch `https://api.lexmount.cn/v1/dom/dump`
- 仓库数量：6
- 成功返回：6/6
- 保留发布条目：30
- 数据来源：各仓库公开 Releases Atom feed；本报告不猜测未发布内容。

## 最新版本

| 项目 | 最新版本 | 发布/更新时间 | Feed 状态 | 最新条目链接 |
|---|---|---|---|---|
| Playwright Python | v1.64.0 | 2026-10-13T23:32:18Z | `ok` | [打开](https://github.com/microsoft/playwright-python/releases/tag/v1.64.0) |
| Browser Use | 0.13.13 | 2026-10-15T23:50:45Z | `ok` | [打开](https://github.com/browser-use/browser-use/releases/tag/0.13.13) |
| Crawl4AI | v0.9.5 | 2026-10-14T10:25:39Z | `ok` | [打开](https://github.com/unclecode/crawl4ai/releases/tag/v0.9.5) |
| FastAPI | 0.148.0 | 2026-10-19T12:25:19Z | `ok` | [打开](https://github.com/fastapi/fastapi/releases/tag/0.148.0) |
| Vite | create-vite%409.3.0 | 2026-10-19T08:05:45Z | `ok` | [打开](https://github.com/vitejs/vite/releases/tag/create-vite%409.3.0) |
| Next.js | v16.5.0-canary.17 | 2026-10-17T23:46:40Z | `ok` | [打开](https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.17) |

## 项目详情

### Playwright Python

- Feed URL：<https://github.com/microsoft/playwright-python/releases.atom>
- 最终 URL：https://github.com/microsoft/playwright-python/releases.atom
- Lexmount request_id：`ebdd1110-b009-451a-9583-9591d4b52579`
- Lexmount dom_id：`846861`
- Raw 文件：`raw/playwright-python.json`

#### v1.64.0 — 2026-10-13T23:32:18Z
- 链接：<https://github.com/microsoft/playwright-python/releases/tag/v1.64.0>
- 摘要：🧰 WebMCP New page.webmcp and frame.webmcp give access to the tools that a page registers through the experimental WebMCP browser API, so you can test them like any other part of your app: browser = chromium . launch ( args = [ "--enable-features=WebMCP" ]) page = browser . new_page () page . goto ( "https://example.com" ) for tool in page . webmcp . tools (): print ( tool [ "name" ], tool [ "description" ]) result = page . webmcp . call_tool ( "add" , { "a" : 2 , "b" : 40 }) print ( result [ "c…

#### v1.63.0 — 2026-09-15T19:21:56Z
- 链接：<https://github.com/microsoft/playwright-python/releases/tag/v1.63.0>
- 摘要：🪟 Locate across frames page.frame_locator() and frame.frame_locator() called without a selector search in any frame of the subtree, so you no longer need to locate the iframe first: # Finds the button in any frame on the page. page . frame_locator (). get_by_role ( "button" ). click () The rest of the locator resolves inside a single frame, just like a regular locator, and an error is thrown when it matches elements in several frames. 👁️ Visible-only locators New locator.visible returns a locat…

#### v1.62.0 — 2026-07-31T16:32:36Z
- 链接：<https://github.com/microsoft/playwright-python/releases/tag/v1.62.0>
- 摘要：🖼️ WebP screenshots page.screenshot() and locator.screenshot() can now capture screenshots in the WebP format. Playwright infers the format from a .webp file extension, or you can set the type explicitly. Quality 100 (the default) is lossless, while lower values use lossy compression: page . screenshot ( path = "homepage.webp" , quality = 50 ) New APIs New scroll option ( "auto" | "none" ) on actions to opt out of Playwright's automatic scrolling into view. New locator.wait_for_function() waits…

#### v1.61.0 — 2026-06-29T09:50:08Z
- 链接：<https://github.com/microsoft/playwright-python/releases/tag/v1.61.0>
- 摘要：🔑 WebAuthn passkeys New Credentials virtual authenticator, available via browserContext.credentials , lets tests register passkeys and answer navigator.credentials.create() / navigator.credentials.get() ceremonies in the page — no real hardware key required, works in all browsers: context = browser . new_context () # Seed a passkey your backend provisioned for a test user. context . credentials . create ( "example.com" , id = credential_id , user_handle = user_handle , private_key = private_key…

#### v1.60.0 — 2026-05-18T11:25:27Z
- 链接：<https://github.com/microsoft/playwright-python/releases/tag/v1.60.0>
- 摘要：🐍 Python improvements New FormData class for building multipart/form-data request bodies — pass to api_request_context.post(form=…) etc. expect.soft(...) soft assertions collect multiple failures in a test instead of stopping at the first one. Requires up-to-date pytest integration to work. All timeout parameters now accept datetime.timedelta — applies wherever a timeout is taken, e.g. page.goto() , locator.click() , expect(...).to_be_visible() . Async context manager support across more APIs —…

### Browser Use

- Feed URL：<https://github.com/browser-use/browser-use/releases.atom>
- 最终 URL：https://github.com/browser-use/browser-use/releases.atom
- Lexmount request_id：`98582cea-219f-4558-8dd6-ce5c67b1c2d3`
- Lexmount dom_id：`846862`
- Raw 文件：`raw/browser-use.json`

#### 0.13.13 — 2026-10-15T23:50:45Z
- 标题：0.13.13: OpenAI browser tools and Cloud fixes
- 链接：<https://github.com/browser-use/browser-use/releases/tag/0.13.13>
- 摘要：This release includes the OpenAI browser-tool driver and fixes two integration issues. Handle temporary empty Cloud tab URLs during navigation. Keep screenshots, crops, and pointer coordinates aligned on scaled displays. Provide 18 default browser tools and six optional actions through Browser Use Actor. Support local browsers, Browser Use Cloud, and borrowed browser sessions. Install the openai-tools extra with OpenAI Python 3.31+. OpenAI 3.x uses httpx2; use its DefaultAsyncHttpxClient for cu…

#### 0.13.12 — 2026-10-15T23:37:58Z
- 标题：0.13.12: OpenAI browser tools
- 链接：<https://github.com/browser-use/browser-use/releases/tag/0.13.12>
- 摘要：Add OpenAI browser tools backed by Browser Use Actor. Import BrowserUse from browser_use.integrations.openai . Install browser-use[openai-tools] to enable OpenAI Python 3.31+. Use local browsers, Browser Use Cloud, or an existing connected BrowserSession. Support the 18 default browser tools and six optional actions. Preserve borrowed browser ownership and check Cloud browser cleanup. Preserve URL and timeout settings across OpenAI 2.x and 3.x model wrappers. OpenAI 3.x uses httpx2. For custom…

#### 0.13.11 — 2026-10-07T04:23:18Z
- 链接：<https://github.com/browser-use/browser-use/releases/tag/0.13.11>
- 摘要：This release includes Browser Use toolsets for Claude, available at browser_use.integrations.toolsets_for_claude . The integration requires an Anthropic SDK release containing anthropic.tools.browser ; the current public Anthropic SDK does not yet include it. Documentation: https://docs.browser-use.com/open-source/customize/integrations/toolsets-for-claude PyPI publication runs through the protected release workflow and requires a separate reviewer approval. What's Changed chore: pin publish wo…

#### 0.13.10 — 2026-09-04T03:28:53Z
- 链接：<https://github.com/browser-use/browser-use/releases/tag/0.13.10>
- 摘要：Browser Use 0.13.10 Upgrade Browser Harness to 0.1.13. Exact-pin all declared runtime, optional, development, and build dependencies. Upgrade and migrate to MCP Python SDK 2.1.1. Add pydantic-settings 2.15.0 as an explicit runtime dependency. Pin Pydantic 2.13.5 and Hatchling 1.32.0. Upgrade pypdf to 6.16.2, resolving the three current pypdf Dependabot advisories. Report unknown MCP tool calls as application errors instead of successful results. Validation includes the full GitHub test matrix,…

#### 0.13.9 — 2026-09-04T01:29:32Z
- 链接：<https://github.com/browser-use/browser-use/releases/tag/0.13.9>
- 摘要：What's Changed fix(llm): make bu-2-0 the ChatBrowserUse default again, keep mini opt-in by @sauravpanda in #5488 ci: remove the dead cloud_evals image-build trigger by @sauravpanda in #5491 fix(filesystem): report missing target text in replace_file by @uczltw6 in #5498 fix(filesystem): escape plain text in generated PDFs by @primorLee in #5502 docs: highlight rerunnable Cloud scripts by @MagMueller in #5551 docs(cloud): update tools guide for CLI 3.0 by @MagMueller in #5553 fix(deps): bump dep…

### Crawl4AI

- Feed URL：<https://github.com/unclecode/crawl4ai/releases.atom>
- 最终 URL：https://github.com/unclecode/crawl4ai/releases.atom
- Lexmount request_id：`0b0f8533-00ce-49ab-a6a6-3f8207b3d616`
- Lexmount dom_id：`846863`
- Raw 文件：`raw/crawl4ai.json`

#### v0.9.5 — 2026-10-14T10:25:39Z
- 标题：Release v0.9.5
- 链接：<https://github.com/unclecode/crawl4ai/releases/tag/v0.9.5>
- 摘要：🎉 Crawl4AI v0.9.5 Released! 📦 Installation PyPI: pip install crawl4ai==0.9.5 Docker: docker pull unclecode/crawl4ai:0.9.5 docker pull unclecode/crawl4ai:latest Note: Docker images are being built and will be available shortly. Check the Docker Release workflow for build status. 📝 What's Changed See CHANGELOG.md for details.

#### docker-rebuild-v0.9.5 — 2026-10-14T10:23:58Z
- 链接：<https://github.com/unclecode/crawl4ai/releases/tag/docker-rebuild-v0.9.5>
- 摘要：Merge main into develop: cloud launch wording

#### v0.9.4 — 2026-09-23T12:14:55Z
- 标题：Release v0.9.4
- 链接：<https://github.com/unclecode/crawl4ai/releases/tag/v0.9.4>
- 摘要：🎉 Crawl4AI v0.9.4 Released! 📦 Installation PyPI: pip install crawl4ai==0.9.4 Docker: docker pull unclecode/crawl4ai:0.9.4 docker pull unclecode/crawl4ai:latest Note: Docker images are being built and will be available shortly. Check the Docker Release workflow for build status. 📝 What's Changed See CHANGELOG.md for details.

#### docker-rebuild-v0.9.4 — 2026-09-23T12:09:09Z
- 标题：docker-rebuild-v0.9.4: docs: release notes, changelog, README, and security credits for v0.9.4
- 链接：<https://github.com/unclecode/crawl4ai/releases/tag/docker-rebuild-v0.9.4>
- 摘要：Bump the version to 0.9.4 and add the v0.9.4 fixes to SECURITY.md.

#### v0.9.3 — 2026-08-31T11:34:14Z
- 标题：Release v0.9.3
- 链接：<https://github.com/unclecode/crawl4ai/releases/tag/v0.9.3>
- 摘要：🎉 Crawl4AI v0.9.3 Released! 📦 Installation PyPI: pip install crawl4ai==0.9.3 Docker: docker pull unclecode/crawl4ai:0.9.3 docker pull unclecode/crawl4ai:latest Note: Docker images are being built and will be available shortly. Check the Docker Release workflow for build status. 📝 What's Changed See CHANGELOG.md for details.

### FastAPI

- Feed URL：<https://github.com/fastapi/fastapi/releases.atom>
- 最终 URL：https://github.com/fastapi/fastapi/releases.atom
- Lexmount request_id：`4bf8bacf-dee3-41b0-b516-87d8f9462e35`
- Lexmount dom_id：`846864`
- Raw 文件：`raw/fastapi.json`

#### 0.148.0 — 2026-10-19T12:25:19Z
- 链接：<https://github.com/fastapi/fastapi/releases/tag/0.148.0>
- 摘要：Defaults for omitted Query , Header , Cookie , and Form parameters and model fields are no longer treated as user input. Defaults are not validated unless validate_default=True is enabled. If you rely on validators running for omitted values, enable default validation with Field(validate_default=True) for model fields or, for example, Query(validate_default=True) for individual parameters. Body(validate_default=True) is now honored too. For parameter models, applying a default no longer marks a…

#### 0.147.0 — 2026-10-19T09:48:41Z
- 链接：<https://github.com/fastapi/fastapi/releases/tag/0.147.0>
- 摘要：Omitted bool and bool | None form fields are now interpreted as False , matching unchecked HTML checkboxes. This applies to individual Form parameters and form models, including required fields and fields with defaults of True or None . The inferred value is considered explicitly set, including in model_dump(exclude_unset=True) . JSON requests and direct Pydantic validation are unchanged. See Boolean Form Fields . Breaking Changes 🐛 Treat omitted boolean form fields as False. PR #16523 by @tian…

#### 0.146.0 — 2026-10-18T15:18:08Z
- 链接：<https://github.com/fastapi/fastapi/releases/tag/0.146.0>
- 摘要：The root_path parameter in FastAPI() is deprecated. Configure the server with fastapi run --root-path /api/v1 instead. Breaking Changes 🗑️ Deprecate the root_path parameter in FastAPI . PR #16520 by @tiangolo .

#### 0.145.0 — 2026-10-18T14:40:20Z
- 链接：<https://github.com/fastapi/fastapi/releases/tag/0.145.0>
- 摘要：Breaking Changes 🔥 Remove deprecated openapi_prefix and unused **extra from FastAPI . PR #16518 by @tiangolo . Docs 📝 Document URL paths in templates. PR #16517 by @tiangolo .

#### 0.144.0 — 2026-10-18T12:42:34Z
- 链接：<https://github.com/fastapi/fastapi/releases/tag/0.144.0>
- 摘要：Features ✨ Add WebSocket support to security dependencies. PR #10147 by @mnixry .

### Vite

- Feed URL：<https://github.com/vitejs/vite/releases.atom>
- 最终 URL：https://github.com/vitejs/vite/releases.atom
- Lexmount request_id：`6d74c5cc-5a71-4e1c-86ca-44e0c1a30855`
- Lexmount dom_id：`846865`
- Raw 文件：`raw/vite.json`

#### create-vite%409.3.0 — 2026-10-19T08:05:45Z
- 标题：create-vite@9.3.0
- 链接：<https://github.com/vitejs/vite/releases/tag/create-vite%409.3.0>
- 摘要：Features create-vite: print version before scaffolding ( #23806 ) ( a3001c5 ) create-vite: use typescript v7 where possible ( #23794 ) ( 9df8bbc ) Bug Fixes create-vite: add router only options for tanstack router/start ( #23543 ) ( f155b62 ) deps: update all non-major dependencies ( #23482 ) ( 3c752c8 ) deps: update all non-major dependencies ( #23537 ) ( e8990c4 ) deps: update all non-major dependencies ( #23601 ) ( 9944fa6 ) deps: update all non-major dependencies ( #23648 ) ( 8a4c19c ) deps…

#### v8.3.4 — 2026-10-08T12:03:54Z
- 链接：<https://github.com/vitejs/vite/releases/tag/v8.3.4>
- 摘要：Features bundled-dev: support import.meta.hot.acceptExports ( #23463 ) ( bc0f21c ) Bug Fixes avoid mutating hmr defaults (fix #23575 ) ( #23576 ) ( 574d5e3 ) build: correct preloads when chunkImportMap is enabled with non-root base ( #23698 ) ( 2a8c0f0 ) build: wait for in-flight stylesheets in preload helper (fix #23652 ) ( #23662 ) ( 036b745 ) bundled-dev: serve /@vite/client and stub @vite/env ( #23664 ) ( 5afc5a8 ) client: skip rewriting unchanged adopted styles ( #23697 ) ( fa71469 ) css:…

#### v8.3.3 — 2026-10-06T08:23:01Z
- 链接：<https://github.com/vitejs/vite/releases/tag/v8.3.3>
- 摘要：Bug Fixes deps: update launch-editor to v2.14.2 ( #23654 ) ( 22fd1d5 ) html: filename passed to transformIndexHtml should not include queries ( #23653 ) ( 7dafd8e ) server: check fs.serve for ?vite-wasm-instance ( #23655 ) ( ba8b7ab ) server: store ids to safeModulePaths rather than URLs ( #23656 ) ( c3e06f9 )

#### v8.2.4 — 2026-10-06T04:42:58Z
- 链接：<https://github.com/vitejs/vite/releases/tag/v8.2.4>
- 摘要：Please refer to CHANGELOG.md for details.

#### v8.1.6 — 2026-10-06T04:48:45Z
- 链接：<https://github.com/vitejs/vite/releases/tag/v8.1.6>
- 摘要：Please refer to CHANGELOG.md for details.

### Next.js

- Feed URL：<https://github.com/vercel/next.js/releases.atom>
- 最终 URL：https://github.com/vercel/next.js/releases.atom
- Lexmount request_id：`4e58e836-054b-4ac6-a41a-e859511fc60e`
- Lexmount dom_id：`846866`
- Raw 文件：`raw/nextjs.json`

#### v16.5.0-canary.17 — 2026-10-17T23:46:40Z
- 链接：<https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.17>
- 摘要：Misc Changes turbo-persistence: prefetch multi-page SST blocks with MADV_WILLNEED: #100283 Credits Huge thanks to @lukesandberg for helping!

#### v16.5.0-canary.16 — 2026-10-16T23:47:57Z
- 链接：<https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.16>
- 摘要：Core Changes Refactor fetchStrategy -> stage and completeness: #99706 Remove dead NextNodeServer.renderHTML: #100284 Pass Server Action request metadata into App rendering: #100274 Revert "Keep requests through middleware in a single OpenTelemetry trace": #100302 Respect release age when pinning the upgrade CLI: #100256 Misc Changes test: remove stale deploy gate on cold RSC navigation param caching test: #100285 Fix upgrade eval worktree dependency links: #100257 Credits Huge thanks to @lukesa…

#### v16.5.0-canary.15 — 2026-10-15T23:44:24Z
- 链接：<https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.15>
- 摘要：Core Changes Hoist app page request URL into render context: #99269 Hide overlay editor button labels on smaller screens: #100266 Prefer non-partial entries regardless of FetchStrategy: #99705 [Partial Prefetching] Don't report vary params in responses that include dynamic data: #99700 [Partial Prefetching] Small optimizations and fixes: #99695 [Cached Navs] Extract the shell from a fully cached response: #99619 Refactor the navigation fetch and decode layering: #99618 [Cached Navs] Don't extra…

#### v16.5.0-canary.14 — 2026-10-15T13:52:48Z
- 链接：<https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.14>
- 摘要：Core Changes Upgrade React from 07dde64d-20261013 to 99c106c4-20261014 : #100215 Example Changes docs: type error.js error prop as unknown: #100232 Misc Changes chore: fix turborepo cache for miri unit test job: #100241 Fix binary trace self-time on same-span re-entry: #100205 docs: add instant navigation testing to Playwright guide: #100003 Credits Huge thanks to @mischnic , @yousefdawood7 , and @icyJoseph for helping!

#### v16.5.0-canary.13 — 2026-10-15T10:00:06Z
- 链接：<https://github.com/vercel/next.js/releases/tag/v16.5.0-canary.13>
- 摘要：Core Changes Fix extensionless Google font URLs in both bundlers: #100158 Emit the Turbopack shared-runtime bootstrap in the PPR resume so it gets the CSP nonce: #100102 Keep requests through middleware in a single OpenTelemetry trace: #100136 Write webpack dev manifests atomically: #100112 Misc Changes next-api: isolate dropped entrypoint collectibles in an inner operation: #100187 turbo-tasks-backend: optimize aggregated updates outside of the lock: #100165 docs: Add turborepo agents rules: #…

## 核验步骤

1. 打开各仓库 Releases 页面核对最新版本。
2. 打开 `raw/*.json`，检查 Lexmount 抓取到的 Atom feed 内容。
3. 对照 `run_manifest.json` 的 request_id 和 dom_id。
4. 使用 `SHA256SUMS.txt` 核对文件完整性。
