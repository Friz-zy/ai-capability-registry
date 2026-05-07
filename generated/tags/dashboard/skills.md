# dashboard

## Skills
Load skill and **use it** when task matches.

### build-dashboard
Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

File: `../external/anthropic-knowledge-work-plugins/data/skills/build-dashboard/SKILL.md`

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

File: `../external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`
