# Tag: dev

Skills with tag `dev`:

## agent-development

This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`
- **Tags**: `asks`, `autonomous`, `code`, `colors`, `conditions`, `create`, `description`, `dev`, `development`, `frontmatter`, `guidance`, `needs`, `practices`, `prompts`, `structure`, `subagent`, `triggering`, `used`

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

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

## command-development

This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`
- **Tags**: `arguments`, `asks`, `askuserquestion`, `bash`, `code`, `command`, `command-development`, `commands`, `create`, `custom`, `define`, `dev`, `development`, `dynamic`, `execution`, `fields`, `frontmatter`, `guidance`, `interaction`, `interactive`, `needs`, `organize`, `practices`, `slash`, `structure`, `used`, `yaml`

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## plugin-settings

This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- **Tags**: `asks`, `behavior`, `configurable`, `configuration`, `content`, `dev`, `documents`, `frontmatter`, `local`, `make`, `markdown`, `per`, `per-project`, `project`, `settings`, `state`, `store`, `storing`, `used`, `yaml`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## skill-development

This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/skill-development/SKILL.md`
- **Tags**: `code`, `content`, `create`, `description`, `dev`, `development`, `disclosure`, `guidance`, `improve`, `needs`, `organize`, `practices`, `progressive`, `structure`, `used`
