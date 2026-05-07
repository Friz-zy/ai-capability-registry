# debugging

## Skills
Load skill and **use it** when task matches.

### build-zoom-rest-api-app
Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`

### debug
Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`

### playwright
Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

File: `../external/openai-skills/skills/.curated/playwright/SKILL.md`

### playwright-interactive
Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging.

File: `../external/openai-skills/skills/.curated/playwright-interactive/SKILL.md`

### security-best-practices
Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

File: `../external/openai-skills/skills/.curated/security-best-practices/SKILL.md`

### setup-zoom-oauth
Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`

### webapp-testing
Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

File: `../external/anthropic-skills/skills/webapp-testing/SKILL.md`

### zoom-oauth
Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`
