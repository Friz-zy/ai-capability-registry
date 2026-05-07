# url

## Skills
Load skill file when task matches.

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### enrich-lead
Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions.

File: `../external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/enrich-lead/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `../external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### virtual-agent/android
Zoom Virtual Agent Android integration via WebView. Use for Java/Kotlin bridge callbacks, native URL handling, support_handoff relay, and lifecycle-safe embedding.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/android/SKILL.md`

### virtual-agent/ios
Zoom Virtual Agent iOS integration via WKWebView. Use for Swift/Objective-C script injection, message handlers, support_handoff relay, and URL routing policies.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/ios/SKILL.md`
