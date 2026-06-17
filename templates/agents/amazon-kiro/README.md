# Amazon Kiro Configuration Templates

## Where to Place Files

| File | Global | Project |
|------|--------|---------|
| `agent.json` | `~/.kiro/agents/<name>.json` | `.kiro/agents/<name>.json` |
| `mcp.json` | `~/.kiro/settings/mcp.json` | `.kiro/settings/mcp.json` |
| `SKILL.md` | `~/.kiro/skills/<name>/SKILL.md` | `.kiro/skills/<name>/SKILL.md` |
| `steering-*.md` | `~/.kiro/steering/<name>.md` | `.kiro/steering/<name>.md` |
| `AGENTS.md` | — | `<project-root>/AGENTS.md` (always active) |

Managed: MDM/Group Policy → `~/.kiro/steering/`

### File Placement Details

#### `agent.json` — Agent configuration

```
# Global (available in all projects)
~/.kiro/agents/general-assistant.json
~/.kiro/agents/code-reviewer.json
~/.kiro/agents/documentation-writer.json

# Project (available only in this project)
my-project/.kiro/agents/dev-agent.json
my-project/.kiro/agents/aws-specialist.json
```

When both global and project have an agent with the same name, the project one takes precedence (with a warning).

#### `mcp.json` — MCP server configuration

```
# Global (applies to all projects)
~/.kiro/settings/mcp.json

# Project (applies only to this project)
my-project/.kiro/settings/mcp.json
```

Agent configs can also define per-agent MCP servers via the `mcpServers` field, and control whether to merge global/project MCP config with `includeMcpJson`.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.kiro/skills/aws-patterns/SKILL.md
~/.kiro/skills/api-design/SKILL.md

# Project (available only in this project)
my-project/.kiro/skills/db-migration/SKILL.md
my-project/.kiro/skills/deploy-check/SKILL.md
```

Skills use progressive loading — metadata is loaded at startup, full content is loaded on demand. Reference from agent config:
```json
"resources": ["skill://.kiro/skills/**/SKILL.md"]
```

#### `steering-*.md` — Steering (instruction) files

```
# Global (applies to all projects)
~/.kiro/steering/coding-standards.md       # mode: always
~/.kiro/steering/security-rules.md          # mode: always
~/.kiro/steering/typescript-rules.md        # condition: "*.ts"

# Project (applies only to this project)
my-project/.kiro/steering/project-style.md  # mode: always
my-project/.kiro/steering/python-rules.md    # condition: "*.py"
my-project/.kiro/steering/deploy-check.md   # mode: manual  → activated via #deploy-check
```

Four modes available:
- **always** — Always loaded into context
- **conditional** — Loaded when files match a glob pattern (`condition: "*.ts"`)
- **manual** — Only loaded when referenced by `#name`
- **auto** — Loaded when description matches the prompt (no `mode` key)

Precedence: workspace steering > global steering.

#### `AGENTS.md` — Project instructions

```
# Project root (always active, no frontmatter needed)
my-project/AGENTS.md
```

Unlike steering files, `AGENTS.md` is always loaded into context (equivalent to `mode: always`). There is no global `AGENTS.md`.

## How to Use

### 1. Agent config (`agent.json`)

Save as `.kiro/agents/<name>.json` (project) or `~/.kiro/agents/<name>.json` (global). The **filename** (minus `.json`) becomes the agent name. When both locations have the same name, the local one takes precedence.

Key fields:
- **name** — Agent identifier (optional; derived from filename)
- **description** — Human-readable purpose
- **prompt** — System prompt. Supports inline text or `file://` URIs for external files:
  - `"prompt": "You are a specialist…"` — inline
  - `"prompt": "file://./prompts/expert.md"` — relative to agent config directory
  - `"prompt": "file:///home/user/prompts/agent.md"` — absolute path
- **model** — Model ID (must match available models from `/model` command)
- **tools** — List of available tools: `"read"`, `"write"`, `"shell"`, `"@server"`, `"@server/tool"`, `"*"`, `"@builtin"`
- **allowedTools** — Tools that skip permission prompts. Supports glob patterns:
  - `"read"` — exact match
  - `"@git/git_status"` — specific MCP tool
  - `"@server/read_*"` — wildcard prefix
  - `"@fetch"` — all tools from a server
- **toolAliases** — Remap tool names to resolve collisions:
  ```json
  "@github-mcp/get_issues": "github_issues"
  ```
- **toolsSettings** — Per-tool configuration:
  - `write.allowedPaths` — Restrict write access to glob patterns
  - `shell.allowedCommands` / `shell.deniedCommands` / `shell.autoAllowReadonly`
- **resources** — Load context at startup or on-demand:
  - `"file://README.md"` — load file into context
  - `"skill://.kiro/skills/**/SKILL.md"` — progressive skill loading
  - `{"type": "knowledgeBase", "source": "file://./docs", "name": "Docs"}` — searchable index
- **mcpServers** — Per-agent MCP servers (overrides/extends global config)
- **includeMcpJson** — `true` = include servers from `~/.kiro/settings/mcp.json` and project `.kiro/settings/mcp.json`
- **hooks** — Lifecycle hooks (see below)
- **keyboardShortcut** — Quick switch: `"ctrl+a"`, `"shift+b"`, etc.
- **welcomeMessage** — Shown when switching to this agent

### 2. MCP servers (`mcp.json`)

Place at `.kiro/settings/mcp.json` (project) or `~/.kiro/settings/mcp.json` (global).

Server types:
- **stdio** — `command` + `args` + optional `env` + `timeout`
- **HTTP** — `type: "http"` + `url` + optional `oauth` (with `clientId`, `redirectUri`, `oauthScopes`)

### 3. Skills (`SKILL.md`)

Place in `.kiro/skills/<skill-name>/SKILL.md`. Skills use **progressive loading** — metadata is loaded at startup, full content is loaded on demand.

YAML frontmatter must include `name` and `description`. Reference skills from agent config:
```json
"resources": ["skill://.kiro/skills/**/SKILL.md"]
```

### 4. Steering files (`steering-*.md`)

Steering files are the Kiro equivalent of instruction files. They have four modes:

| Mode | Frontmatter | Behavior |
|------|-------------|----------|
| **always** | `---\nmode: always\n---` | Always loaded into context |
| **conditional** | `---\ncondition: "*.ts"\n---` | Loaded when files match the glob pattern |
| **manual** | `---\nmode: manual\n---` | Only loaded when referenced by `#name` |
| **auto** | `---\ndescription: "..."` (no mode) | Loaded when description matches the prompt |

The top 3 steering file templates in this directory demonstrate each mode.

### 5. Instructions (`AGENTS.md`)

Place at project root. Always active regardless of steering mode. Precedence: workspace steering > global steering; AGENTS.md is always loaded.

### 6. Hooks

Hooks run shell commands at agent lifecycle points. Define them in the agent `hooks` field:

| Hook | Trigger |
|------|---------|
| `agentSpawn` | When agent is activated |
| `userPromptSubmit` | When user submits a prompt |
| `preToolUse` | Before tool execution (matcher required; exit code 2 = block) |
| `postToolUse` | After tool execution (matcher required) |
| `stop` | When agent finishes responding |

Each hook entry:
```json
{ "command": "git status", "timeout_ms": 5000, "cache_ttl_seconds": 30 }
```
`preToolUse` and `postToolUse` also accept a `matcher` field for tool name filtering.

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `AWS_PROFILE` | AWS profile for Bedrock authentication |
| `AWS_REGION` | AWS region |

## Useful Commands

```bash
kiro-cli agent list              # List available agents
kiro-cli agent create <name>     # Create agent interactively
kiro-cli agent create <name> --manual   # Create in editor
kiro-cli --agent my-agent        # Start session with specific agent
/agent swap                      # Switch agent in session
/agent schema                    # Show agent config JSON schema
/mcp                              # List loaded MCP servers
```

## Agent Precedence

When Kiro CLI looks for an agent:
1. **Local first**: `.kiro/agents/` in current directory
2. **Global fallback**: `~/.kiro/agents/` in HOME directory

If both locations have an agent with the same name, the local one takes precedence (with a warning).