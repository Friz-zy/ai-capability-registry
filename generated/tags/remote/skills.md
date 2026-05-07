# remote

## Skills
Load skill and **use it** when task matches.

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### zoom-cobrowse-sdk
Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy masking, remote assist, or PIN-based session sharing.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md`
