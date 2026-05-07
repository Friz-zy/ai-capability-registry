# make

## Skills
Load skill file when task matches.

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### build-mcpb
This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

File: `../external/anthropic-skills/skills/pdf/SKILL.md`

### playground
Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

File: `../external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`

### plugin-settings
This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`

### roadmap-update
Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update/SKILL.md`

### setup-zoom-websockets
Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constraints make WebSockets preferable to webhooks.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets/SKILL.md`

### slack-gif-creator
Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

File: `../external/anthropic-skills/skills/slack-gif-creator/SKILL.md`

### synthesize-research
Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey responses, or support tickets to make sense of, need to extract themes and rank findings by frequency and impact, or want to turn raw feedback into roadmap recommendations.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research/SKILL.md`
