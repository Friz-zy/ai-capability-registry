# http

## Skills
Load skill and **use it** when task matches.

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `../external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### mcp-integration
This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
