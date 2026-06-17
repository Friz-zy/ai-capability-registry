# Amazon Kiro Agent Configuration — Field Reference

Full field-by-field reference for Kiro agent configuration. See `agent.json.example` for a complete working example with comments.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | no | Agent name. Derived from filename if omitted. |
| `description` | string | no | Human-readable purpose. |
| `prompt` | string | no | System prompt. Inline text or `file://` URI. Relative paths resolve from agent config directory. |
| `model` | string | no | Model ID. Must match available models (`/model` command). Falls back to default if unset/unavailable. |
| `tools` | string[] | no | Available tools. Built-in: `"read"`, `"write"`, `"shell"`, `"@builtin"`. MCP: `"@server"`, `"@server/tool"`. All: `"*"`. |
| `toolAliases` | object | no | Remap tool names. Key = original (`@server/tool`), value = new name. Resolves collisions. |
| `allowedTools` | string[] | no | Tools that skip permission prompts. Supports glob: `"read"`, `"@git/git_status"`, `"@server/read_*"`, `"@fetch"`. No bare `"*"`. |
| `toolsSettings` | object | no | Per-tool config. Keys are tool names. See below. |
| `toolsSettings.<tool>.allowedPaths` | string[] | — | Glob patterns restricting file access. `["src/**", "tests/**"]` |
| `toolsSettings.shell.allowedCommands` | string[] | — | Shell commands the agent may run. |
| `toolsSettings.shell.deniedCommands` | string[] | — | Shell commands always denied (glob patterns). |
| `toolsSettings.shell.autoAllowReadonly` | boolean | — | Auto-approve read-only shell commands. |
| `resources` | (string\|object)[] | no | Files/skills/knowledge bases loaded into context. See below. |
| `mcpServers` | object | no | Per-agent MCP server definitions. See below. |
| `includeMcpJson` | boolean | no | `true` = merge global/project `mcp.json` servers with per-agent `mcpServers`. Default: `true`. |
| `hooks` | object | no | Lifecycle hooks. See below. |
| `keyboardShortcut` | string | no | Quick switch key. Format: `[ctrl+][shift+]key`. E.g. `"ctrl+a"`, `"shift+b"`. |
| `welcomeMessage` | string | no | Message shown when switching to this agent. |
| `useLegacyMcpJson` | boolean | no | Load MCP servers from legacy `.kiro/settings/mcp.json` format. |

## Resources

| Type | Example | Description |
|------|---------|-------------|
| File | `"file://README.md"` | Loaded into context at startup. Supports globs: `"file://docs/**/*.md"`. |
| Skill | `"skill://.kiro/skills/**/SKILL.md"` | Metadata loaded at startup; full content on demand. |
| Knowledge base | `{"type": "knowledgeBase", "source": "file://./docs", "name": "Docs", "indexType": "best", "autoUpdate": true}` | Searchable indexed docs. |

## MCP Servers

```json
"mcpServers": {
  "server-name": {
    "command": "command-to-run",
    "args": ["--flag"],
    "env": {"ENV_VAR": "value"},
    "timeout": 120000
  }
}
```

For HTTP servers with OAuth:
```json
"remote-api": {
  "type": "http",
  "url": "https://api.example.com/mcp",
  "oauth": {
    "clientId": "your-client-id",
    "redirectUri": "127.0.0.1:8080",
    "oauthScopes": ["read", "write"]
  }
}
```

## Hooks

| Hook | Trigger | Has `matcher`? |
|------|---------|----------------|
| `agentSpawn` | Agent activated | No |
| `userPromptSubmit` | User submits prompt | No |
| `preToolUse` | Before tool execution | Yes. Exit code 2 = block. |
| `postToolUse` | After tool execution | Yes. |
| `stop` | Agent finishes responding | No. Can return `{"decision":"block","reason":"..."}` to continue. |

Each hook entry: `{ "command": "...", "matcher": "..." (optional), "timeout_ms": 5000 (optional), "cache_ttl_seconds": 30 (optional) }`

Matcher uses canonical tool names: `fs_read`, `fs_write`, `execute_bash`, `use_aws`, or MCP format: `@git`, `@git/status`, `@builtin`, `*`.

## Precedence

1. Local: `.kiro/agents/<name>.json`
2. Global: `~/.kiro/agents/<name>.json`

Local takes precedence with a warning.