# their

## Skills
Load skill and **use it** when task matches.

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### build-mcpb
This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

### claude-automation-recommender
Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

File: `../external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

File: `../external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### task-management
Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/task-management/SKILL.md`

### user-research
Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or when the user needs help with any aspect of understanding their users through research.

File: `../external/anthropic-knowledge-work-plugins/design/skills/user-research/SKILL.md`
