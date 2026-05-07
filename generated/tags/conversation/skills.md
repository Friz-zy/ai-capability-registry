# conversation

## Skills
Load skill and **use it** when task matches.

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`
