# Tag: discusses

Skills with tag `discusses`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## build-mcpb

This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`
- **Tags**: `apps`, `build`, `build-mcpb`, `bundle`, `bundling`, `desktop`, `dev`, `discusses`, `distribute`, `filesystem`, `having`, `installable`, `interacts`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `mentions`, `must`, `needs`, `node`, `package`, `python`, `runtime`, `server`, `set`, `ship`, `their`, `used`, `without`

## example-skill

This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-skill/SKILL.md`
- **Tags**: `asks`, `code`, `create`, `creating`, `demonstrate`, `development`, `discusses`, `format`, `provides`, `show`, `used`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## recruiting-pipeline

Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user discusses sourcing, screening, interviewing, or extending offers.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline/SKILL.md`
- **Tags**: `candidate`, `candidates`, `discusses`, `extending`, `hiring`, `human`, `interviewing`, `manage`, `many`, `offers`, `pipeline`, `recruiting`, `recruiting-pipeline`, `screening`, `sourcing`, `stages`, `status`, `track`, `trigger`
