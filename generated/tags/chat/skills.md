# chat

## Skills
Load skill and **use it** when task matches.

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`

### call-prep
Prepare for a sales call with account context, attendee research, and suggested agenda. Works standalone with user input and web research, supercharged when you connect your CRM, email, chat, or transcripts. Trigger with "prep me for my call with [company]", "I'm meeting with [company] prep me", "call prep [company]", or "get me ready for [meeting]".

File: `../external/anthropic-knowledge-work-plugins/sales/skills/call-prep/SKILL.md`

### contact-center/android
Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### update
Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`

### virtual-agent/web
Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`

### zoom-rtms
Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or contact-center voice streams.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rtms/SKILL.md`
