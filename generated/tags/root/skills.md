# root

## Skills
Load skill and **use it** when task matches.

### hook-development
This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`

### mcp-integration
This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

File: `../external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### plugin-structure
This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
