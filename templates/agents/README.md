# AI Agent Configuration Templates

Full configuration file templates for each CLI agent tool referenced in `ai-agents.md`.

## Conventions

- **`.example` files** (e.g. `settings.json.example`, `opencode.json.example`): Full reference with all fields commented. Since JSON doesn't support comments, these use `"//"` keys as pseudo-comments — delete all `"//"` keys before using.
- **TOML and JSONC files** (e.g. `config.toml`, `kilo.jsonc`): Already have native `#` or `//` comment support, so they serve as their own full reference.
- **Markdown files** (e.g. `agent.md`, `SKILL.md`): Use YAML frontmatter comments (`#`) and HTML comments (`<!-- -->`) for documentation.

## Directory Structure

| Tool | Directory | Format |
|------|-----------|--------|
| Codex CLI | `codex/` | TOML |
| Claude Code | `claude-code/` | JSON + Markdown (YAML frontmatter) |
| Kilo Code | `kilo-code/` | JSONC + Markdown (YAML frontmatter) |
| OpenCode | `opencode/` | JSON + Markdown (YAML frontmatter) |
| Amazon Kiro | `amazon-kiro/` | JSON + Markdown (YAML frontmatter) |

## Template Files by Tool

### Codex CLI (`codex/`)

| File | Purpose |
|------|---------|
| `config.toml` | Full project/global config: model, providers, agents, MCP, features, skills, hooks, permissions (TOML — supports `#` comments) |
| `agent-role.toml` | Agent role definition (referenced via `config_file` in `[agents.<name>]`) |
| `SKILL.md` | Skill template with TOML-compatible YAML frontmatter |
| `AGENTS.md` | Project instructions (hierarchical by directory) |

<details>
<summary>File placement details</summary>

#### `config.toml` — Main configuration

```
# Global (applies to all projects)
~/.codex/config.toml

# Project (applies only to this project)
my-project/.codex/config.toml

# Profile-specific (selected with --profile <name>)
~/.codex/code-review.config.toml
~/.codex/security.config.toml

# Managed/enterprise (system-wide, enforced)
/etc/codex/config.toml
```

Override the config directory with `CODEX_HOME` env var.

#### `agent-role.toml` — Agent role definition

```
# Place anywhere and reference from config.toml via config_file:
#   [agents.reviewer]
#   config_file = "./agents/reviewer.toml"
my-project/.codex/agents/reviewer.toml
my-project/.codex/agents/researcher.toml
```

The `config_file` path is relative to the config file that contains it.

#### `SKILL.md` — Skill definition

```
# Global (available in all projects)
~/.agents/skills/code-review/SKILL.md
~/.agents/skills/security-audit/SKILL.md

# Project (available only in this project)
my-project/.agents/skills/deploy-check/SKILL.md
my-project/.agents/skills/db-migration/SKILL.md
```

#### `AGENTS.md` — Project instructions

```
# Global (applies to all projects)
~/.codex/AGENTS.md

# Project root (applies to the entire project)
my-project/AGENTS.md

# Nested (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Nested files override parent ones. Precedence: nested > parent > global.

</details>

---

### Claude Code (`claude-code/`)

| File | Purpose |
|------|---------|
| `settings.json` | Minimal working settings: permissions + hooks |
| `settings.json.example` | Full reference of all fields with comments (JSON — delete `"//"` keys before use) |
| `settings.local.json` | Minimal local overrides example (gitignored) |
| `.mcp.json` | Minimal MCP server configuration |
| `.mcp.json.example` | Full MCP reference with all server types (JSON — delete `"//"` keys before use) |
| `agent.md` | Agent definition with all frontmatter fields (YAML fm + markdown) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `command.md` | Slash command template |
| `CLAUDE.md` | Project instructions template |
| `rule.md` | Path-scoped rule template |

<details>
<summary>File placement details</summary>

#### `settings.json` — Project settings

```
# Global (applies to all projects)
~/.claude/settings.json

# Project (applies only to this project)
my-project/.claude/settings.json

# Local overrides (gitignored, personal only)
my-project/.claude/settings.local.json

# Managed/enterprise (system-wide, enforced, overrides everything)
~/.claude/managed-settings.json
```

Precedence: managed-settings > local > project > global.

#### `.mcp.json` — MCP server configuration

```
# Global (inside ~/.claude.json, mcpServers key)
~/.claude.json

# Project (standalone file at project root)
my-project/.mcp.json
```

#### `agent.md` — Agent definition

```
# Global (available in all projects)
~/.claude/agents/code-reviewer.md
~/.claude/agents/security-auditor.md

# Project (available only in this project)
my-project/.claude/agents/backend-specialist.md
```

The filename (minus `.md`) becomes the agent name.

#### `SKILL.md` — Skill definition

```
# Global
~/.claude/skills/deploy-check/SKILL.md

# Project
my-project/.claude/skills/db-migration/SKILL.md
```

The directory name becomes the slash command: `/deploy-check`, `/db-migration`.

#### `command.md` — Slash command

```
# Global → /user:<command-name>
~/.claude/commands/deploy.md
~/.claude/commands/review.md

# Project → /project:<command-name>
my-project/.claude/commands/migrate.md
```

#### `CLAUDE.md` — Project instructions

```
# Global
~/.claude/CLAUDE.md

# Project root
my-project/CLAUDE.md

# Project .claude/ directory (takes precedence)
my-project/.claude/CLAUDE.md

# Local overrides (gitignored)
my-project/CLAUDE.local.md
```

Precedence: `.claude/CLAUDE.md` > root `CLAUDE.md` > `~/.claude/CLAUDE.md`.

#### `rule.md` — Path-scoped rules

```
# Project-level only, always active
my-project/.claude/rules/python-style.md
my-project/.claude/rules/security-standards.md
```

</details>

---

### Kilo Code (`kilo-code/`)

| File | Purpose |
|------|---------|
| `kilo.jsonc` | Full config reference: model, providers, agents, MCP, permissions, commands, references (JSONC — supports `//` comments) |
| `agent.md` | Agent definition with all frontmatter fields (YAML fm + markdown) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `AGENTS.md` | Project instructions (hierarchical) |
| `command.md` | Slash command template |

<details>
<summary>File placement details</summary>

#### `kilo.jsonc` — Main configuration (JSON with comments)

```
# Global (applies to all projects)
~/.config/kilo/kilo.jsonc

# Project — primary location (preferred)
my-project/kilo.jsonc

# Project — alternative location
my-project/.kilo/kilo.jsonc

# Managed/enterprise (system-wide, enforced)
/etc/kilo/kilo.json
```

Override config path with `KILO_CONFIG` env var, or inline with `KILO_CONFIG_CONTENT`.

#### `agent.md` — Agent definition (Markdown + YAML frontmatter)

```
# Global (available in all projects)
~/.config/kilo/agent/code-reviewer.md
~/.config/kilo/agent/security-auditor.md

# Project (available only in this project)
my-project/.kilo/agent/backend-dev.md
my-project/.kilo/agent/db-migrator.md

# Also scans compat directory:
my-project/.opencode/agents/<name>.md
```

The filename (minus `.md`) becomes the agent name. Nested directories create namespaced names: `.kilo/agent/backend/sql.md` → agent `backend/sql`.

#### `SKILL.md` — Skill definition

```
# Global
~/.config/kilo/skills/deploy-check/SKILL.md

# Project
my-project/.kilo/skills/db-migration/SKILL.md

# Compat directories also scanned:
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

#### `AGENTS.md` — Project instructions (hierarchical)

```
# Config-based global instructions:
#   In kilo.jsonc: "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md

# Per-directory (overrides parent for this subtree)
my-project/src/AGENTS.md
my-project/tests/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md (nested > parent).

#### `command.md` — Slash command

```
# Global
~/.config/kilo/command/deploy.md
~/.config/kilo/command/review.md

# Project
my-project/.kilo/command/migrate.md
```

The filename (minus `.md`) becomes the command name.

</details>

---

### OpenCode (`opencode/`)

| File | Purpose |
|------|---------|
| `opencode.json` | Working config with all sections populated |
| `opencode.json.example` | Full reference of all fields with comments (JSON — delete `"//"` keys before use) |
| `agent.md` | Agent definition with all frontmatter fields (YAML fm + markdown) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `AGENTS.md` | Project instructions |

<details>
<summary>File placement details</summary>

#### `opencode.json` — Main configuration

```
# Global (applies to all projects)
~/.config/opencode/opencode.json

# Project (applies only to this project)
my-project/opencode.json

# Managed/enterprise (MDM)
<managed>.mobileconfig
```

Override config path with `OPENCODE_CONFIG`, inline with `OPENCODE_CONFIG_CONTENT`, or directory with `OPENCODE_CONFIG_DIR`.

#### `agent.md` — Agent definition (Markdown + YAML frontmatter)

```
# Global
~/.config/opencode/agents/code-reviewer.md
~/.config/opencode/agents/security-auditor.md

# Project
my-project/.opencode/agents/backend-dev.md
my-project/.opencode/agents/db-migrator.md
```

Agents can also be defined inline in `opencode.json` under the `agent` key. Use `"prompt": "{file:./prompts/my-prompt.txt}"` to reference external prompt files.

#### `SKILL.md` — Skill definition

```
# Global
~/.config/opencode/skills/deploy-check/SKILL.md

# Project
my-project/.opencode/skills/db-migration/SKILL.md

# Compat directories also scanned:
my-project/.claude/skills/<name>/SKILL.md
my-project/.agents/skills/<name>/SKILL.md
```

#### `AGENTS.md` — Project instructions

```
# Config-based global instructions:
#   In opencode.json: "instructions": ["AGENTS.md", "docs/style.md"]

# Project root
my-project/AGENTS.md
```

Precedence: agent.prompt > config `instructions` > AGENTS.md.

</details>

---

### Amazon Kiro (`amazon-kiro/`)

| File | Purpose |
|------|---------|
| `agent.json.example` | Full agent config with all fields documented (JSON — delete `"//"` keys before use) |
| `mcp.json.example` | Full MCP server config with all fields documented (JSON — delete `"//"` keys before use) |
| `SKILL.md` | Skill template with YAML frontmatter |
| `steering-always.md` | Steering file: always active (`mode: always`) |
| `steering-conditional.md` | Steering file: activated by glob pattern (`condition: "*.ts"`) |
| `steering-manual.md` | Steering file: activated by `#name` reference (`mode: manual`) |
| `AGENTS.md` | Project instructions (always active) |
| `REFERENCE.md` | Field-by-field reference for `agent.json` fields |

<details>
<summary>File placement details</summary>

#### `agent.json.example` — Agent configuration

```
# Global (available in all projects)
~/.kiro/agents/general-assistant.json
~/.kiro/agents/code-reviewer.json

# Project (available only in this project)
my-project/.kiro/agents/dev-agent.json
my-project/.kiro/agents/aws-specialist.json
```

When both locations have an agent with the same name, the project one takes precedence (with a warning).

#### `mcp.json` — MCP server configuration

```
# Global (applies to all projects)
~/.kiro/settings/mcp.json

# Project (applies only to this project)
my-project/.kiro/settings/mcp.json
```

Agent configs can also define per-agent MCP servers via the `mcpServers` field, and control merging with `includeMcpJson`.

#### `SKILL.md` — Skill definition

```
# Global
~/.kiro/skills/aws-patterns/SKILL.md
~/.kiro/skills/api-design/SKILL.md

# Project
my-project/.kiro/skills/db-migration/SKILL.md
my-project/.kiro/skills/deploy-check/SKILL.md
```

Skills use progressive loading — metadata loaded at startup, full content loaded on demand. Reference from agent config:

```json
"resources": ["skill://.kiro/skills/**/SKILL.md"]
```

#### `steering-*.md` — Steering files (instruction modes)

```
# Global
~/.kiro/steering/coding-standards.md       # mode: always
~/.kiro/steering/security-rules.md          # mode: always
~/.kiro/steering/typescript-rules.md        # condition: "*.ts"

# Project
my-project/.kiro/steering/project-style.md  # mode: always
my-project/.kiro/steering/python-rules.md    # condition: "*.py"
my-project/.kiro/steering/deploy-check.md   # mode: manual → #deploy-check
```

Four modes: `always` (always loaded), `conditional` (glob match), `manual` (`#name` reference), `auto` (description match).

Precedence: workspace steering > global steering.

#### `AGENTS.md` — Project instructions

```
# Project root only (always active, no frontmatter needed)
my-project/AGENTS.md
```

Unlike steering files, `AGENTS.md` is always loaded into context (equivalent to `mode: always`).

</details>

---

## Key Differences

| Feature | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|---------|-----------|-------------|-----------|----------|-------------|
| Config format | TOML | JSON / YAML fm | JSONC / YAML fm | JSON / YAML fm | JSON / YAML fm |
| Multi-provider | No (OpenAI) | No (Anthropic) | Yes (75+) | Yes (75+) | No (AWS Bedrock) |
| Agent definition | TOML `[agents.<name>]` + role file | `.claude/agents/<name>.md` | `.kilo/agent/<name>.md` or config | `.opencode/agents/<name>.md` or config | `.kiro/agents/<name>.json` |
| MCP transport | stdio + HTTP | stdio + HTTP + SSE + WS | stdio (local) + HTTP (remote) | stdio (local) + HTTP (remote) | stdio + streamable HTTP |
| Spec-driven dev | No | No | No | No | Yes (steering) |
| Hooks | Yes | Yes (pre/post tool) | No | Yes (via plugins) | Yes (lifecycle hooks) |
| Plugins | Early stage | Mature | No | TS/JS | No |
| Profiles | Yes (`--profile`) | No | No | No | No |

## Global vs Project Config Precedence

| Tool | Global | Project | Local/Private | Managed |
|------|--------|---------|---------------|---------|
| Codex CLI | `~/.codex/config.toml` | `.codex/config.toml` | — | `/etc/codex/config.toml` |
| Claude Code | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` (gitignored) | `managed-settings.json` |
| Kilo Code | `~/.config/kilo/kilo.jsonc` | `kilo.jsonc` / `.kilo/kilo.jsonc` | — | `/etc/kilo/kilo.json` |
| OpenCode | `~/.config/opencode/opencode.json` | `opencode.json` | — | MDM `.mobileconfig` |
| Amazon Kiro | `~/.kiro/agents/`, `~/.kiro/settings/`, `~/.kiro/steering/` | `.kiro/agents/`, `.kiro/settings/`, `.kiro/steering/` | — | MDM/Group Policy → `~/.kiro/steering/` |

---

## Permissions Cross-Reference

Permission models across the 5 CLI tools, analyzed for a unified `profiles.yaml` permissions schema.

### Permission Model Comparison

| Aspect | Codex CLI | Claude Code | OpenCode | Kilo Code | Amazon Kiro |
|--------|-----------|-------------|----------|-----------|-------------|
| **Primary model** | 3 presets: `workspace` / `sandbox` / `full-auto` | `allow` / `deny` / `ask` per-tool patterns | `allow` / `ask` / `deny` per-tool + glob maps | `allow` / `ask` / `deny` per-tool + glob maps | tools whitelist + allowedTools auto-approve + toolsSettings |
| **Bash command restrictions** | Via sandbox mode only | `Bash(git log *)` glob patterns in allow/deny | Glob pattern map, last match wins | Glob pattern map, last match wins | `allowedCommands[]` + `deniedCommands[]` + `autoAllowReadonly` |
| **File path edit restrictions** | No | No | `permission.edit` glob patterns (`"*.md": "allow"`) | `permission.edit` glob patterns (`"*.md": "allow"`) | `toolsSettings.write.allowedPaths[]` glob patterns |
| **MCP tool restrictions** | `enabled: true/false` per server | `allowedMcpServers` / `deniedMcpServers` (managed) | `enabled: true/false` per server | `enabled: true/false` per server | `tools: ["@server"]` + `allowedTools: ["@server/read_*"]` |
| **Skill restrictions** | `skills.config.[].enabled` boolean | `allowed-tools` in SKILL.md + `skillOverrides` in agent | `permission.skill` glob patterns | Not in templates | Not in templates (manual only) |
| **Subagent delegation** | No | `Agent(name)` in allow/deny | `permission.task` glob patterns | `permission.task` glob patterns | No (subset via `tools: ["@server"]`) |
| **Network restrictions** | Full: domain allow/deny, proxy, SOCKS5, MITM hooks | `sandbox.network.allowedDomains`, `allowLocalBinding` | No | No | No |
| **Shell sandbox** | Built-in (`sandbox` mode) | `sandbox` config with network controls | No | No | `autoAllowReadonly` for read-only shell commands |
| **Per-agent permissions** | Via role `config_file` (inherits base config) | `tools:` whitelist + `allowed-tools` in frontmatter | `permission:` in frontmatter or inline config | `permission:` in frontmatter or inline config | `tools`, `allowedTools`, `toolsSettings` in agent.json |
| **Managed/enterprise** | `/etc/codex/config.toml` | `managed-settings.json` with lock-down flags | MDM `.mobileconfig` | `/etc/kilo/kilo.json` | MDM/Group Policy → `~/.kiro/steering/` |
| **Config scopes** | Global, project, profile, managed, per-role | Global, project, local, managed, per-agent, per-skill, per-command | Global, project, managed, per-agent | Global, project, managed, per-agent | Per-agent (project + global), MCP (project + global), steering (project + global + MDM) |
| **Step/iteration limit** | `job_max_runtime_seconds`, `max_threads` | No | No | `steps: 25` per agent | No |
| **Provider restrict** | No (OpenAI-first) | No (Anthropic-first) | `enabled_providers` / `disabled_providers` | `enabled_providers` / `disabled_providers` | No (AWS Bedrock) |
| **AWS service restrict** | No | No | No | No | `toolsSettings.aws.allowedServices[]` |
| **Hook system** | `pre_tool_use`, `post_tool_use`, `on_agent_start` (shell scripts) | `PreToolUse`, `PostToolUse`, `Notification`, `Stop` (regex matcher) | Via plugins only | Not in templates | `agentSpawn`, `userPromptSubmit`, `preToolUse`, `postToolUse`, `stop` (canonical names) |
| **Project trust** | Yes — `.codex/` ignored if untrusted | Yes — trust dialog per project | No | No | No |

### Bash Command Restriction Syntax Comparison

| Tool | Syntax | Example |
|------|--------|---------|
| Codex CLI | Preset mode only | `default_permissions = "sandbox"` |
| Claude Code | `Tool(pattern)` glob in allow/deny lists | `"Bash(git log *)"`, `"Bash(rm -rf *)"` |
| OpenCode | Glob pattern map in `permission.bash`, last match wins | `{"*": "ask", "git *": "allow", "rm *": "deny"}` |
| Kilo Code | Glob pattern map in `permission.bash`, last match wins | `{"*": "ask", "git *": "allow", "rm *": "deny"}` |
| Amazon Kiro | Explicit allow/deny lists in `toolsSettings.shell` | `"allowedCommands": ["git status", "npm test"]`, `"deniedCommands": ["rm *"]` |

### File Path Edit Restriction Syntax Comparison

| Tool | Syntax | Example |
|------|--------|---------|
| Codex CLI | No path-level edit restrictions | — |
| Claude Code | No path-level edit restrictions (only tool-level allow/deny) | — |
| OpenCode | Glob pattern map in `permission.edit`, last match wins | `{"*.md": "allow", "*": "deny"}` |
| Kilo Code | Glob pattern map in `permission.edit`, last match wins | `{"*.md": "allow", "*": "deny"}` |
| Amazon Kiro | Glob patterns in `toolsSettings.write.allowedPaths` | `["src/**", "tests/**", "*.md"]` |

### Subagent Delegation Syntax Comparison

| Tool | Syntax | Example |
|------|--------|---------|
| Codex CLI | No subagent delegation control | — |
| Claude Code | `Agent(name)` pattern in allow/deny | `"allow": ["Agent(code-reviewer)"]` |
| OpenCode | `permission.task` glob pattern map | `{"*": "deny", "code-reviewer": "allow"}` |
| Kilo Code | `permission.task` glob pattern map | `{"*": "deny", "code-reviewer": "allow"}` |
| Amazon Kiro | No delegation control (subset via `tools: ["@server"]`) | — |

### MCP Server Control Syntax Comparison

| Tool | Enable/disable per server | Tool-level allow/deny | Server-level allow/deny |
|------|--------------------------|----------------------|-------------------------|
| Codex CLI | `enabled = true/false` | No | No |
| Claude Code | `disabled: true` in .mcp.json | `allowedMcpServers`, `deniedMcpServers` (managed only) | No |
| OpenCode | `"enabled": true/false` | No | No |
| Kilo Code | `"enabled": true/false` | No | No |
| Amazon Kiro | No enable/disable (included or not) | `tools: ["@server"]`, `allowedTools: ["@server/tool"]` | `@server` namespace in tools |

### Network Restriction Syntax Comparison (Codex CLI only)

| Field | Codex CLI Syntax |
|-------|-----------------|
| Enable networking | `network = { enabled = false }` |
| Proxy URL | `proxy_url = "http://127.0.0.1:3128"` |
| SOCKS5 | `enable_socks5 = true`, `socks_url = "http://127.0.0.1:8081"` |
| Domain allow/deny | `[permissions.workspace.network.domains]` → `"*.openai.com" = "allow"`, `"evil.example" = "deny"` |
| Local binding | `allow_local_binding = false` |
| MITM hooks | `[permissions.workspace.network.mitm]` with host, methods, path_prefixes, actions |

### Canonical Tool Name Mapping

Different CLIs use different canonical tool names for the same concepts:

| Concept | Codex CLI | Claude Code | OpenCode | Kilo Code | Amazon Kiro |
|---------|-----------|-------------|----------|-----------|-------------|
| File read | — | `Read` | `read` | `read` | `read` |
| File write/edit | — | `Edit`, `Write` | `edit` | `edit` | `write` |
| Shell execution | — | `Bash` | `bash` | `bash` | `shell` |
| File glob search | — | `Glob` | `glob` | `glob` | — |
| Content search | — | `Grep` | `grep` | `grep` | — |
| Web search | — | `WebSearch` | `websearch` | `websearch` | — |
| Web fetch | — | `WebFetch` | `webfetch` | `webfetch` | — |
| Subagent/task | — | `Agent(name)` | `task` | `task` | — |
| MCP tool | — | `mcp_server_tool` | — | `{server}_{tool}` | `@server/tool` |
| All built-in | — | — | — | — | `@builtin` |
| All tools | — | `*` | — | — | `*` |

### Hooks Comparison

| Aspect | Codex CLI | Claude Code | OpenCode | Kilo Code | Amazon Kiro |
|--------|-----------|-------------|----------|-----------|-------------|
| Hook events | `pre_tool_use`, `post_tool_use`, `on_agent_start` | `PreToolUse`, `PostToolUse`, `Notification`, `Stop` | Via plugins only | Not in templates | `agentSpawn`, `userPromptSubmit`, `preToolUse`, `postToolUse`, `stop` |
| Matcher support | No | Yes — regex on tool names | — | — | Yes — canonical names: `fs_read`, `fs_write`, `execute_bash`, `use_aws`, `@git`, `@builtin`, `*` |
| Block capability | No | Yes — exit code 2 for `PreToolUse` | — | — | Yes — exit code 2 for `preToolUse` |
| Stop hook can continue | No | No | — | — | Yes — `{"decision":"block","reason":"..."}` in `stop` |
| Hook entry format | Array of command paths | `{matcher, hooks: [{type, command}]}` | — | — | `{command, matcher?, timeout_ms?, cache_ttl_seconds?}` |

### Feasibility Assessment: Unified `profiles.yaml` Permissions → CLI Config Generation

**Verdict: Possible with a two-tier approach.**

#### Core Tier — maps cleanly to 3+ CLIs without loss

| Profile field | Maps to |
|---------------|---------|
| `tools.<name>: allow/ask/deny` | Claude `permissions.allow/deny`, OpenCode/Kilo `permission.<tool>`, Kiro `tools`+`allowedTools` (with semantic transform) |
| `bash_commands.allow[]` | Claude `Bash(pattern)` in allow, OpenCode/Kilo `permission.bash` patterns, Kiro `toolsSettings.shell.allowedCommands[]` |
| `bash_commands.deny[]` | Claude `Bash(pattern)` in deny, OpenCode/Kilo `permission.bash` patterns, Kiro `toolsSettings.shell.deniedCommands[]` |
| `edit_paths.allow[]` | OpenCode/Kilo `permission.edit` patterns, Kiro `toolsSettings.write.allowedPaths[]` |
| `edit_paths.deny[]` | OpenCode/Kilo `permission.edit` patterns (via `"*": "deny"`) |
| `subagent_delegation.default + allow[]` | Claude `Agent(name)`, OpenCode/Kilo `permission.task` patterns |
| `mcp.allow_servers[]` / `mcp.deny_servers[]` | Claude `allowedMcpServers`/`deniedMcpServers` (managed), OpenCode/Kilo `enabled`, Kiro `tools: ["@server"]` |

#### CLI-Specific Tier — only generated when targeting that CLI

| Profile field | CLI | Maps to |
|---------------|-----|---------|
| `network.mode` + `network.allowed_domains[]` + `network.denied_domains[]` | Codex | `[permissions.workspace.network]` TOML |
| `auto_approve_readonly: true` | Kiro | `toolsSettings.shell.autoAllowReadonly: true` |
| `aws_services.allowed[]` | Kiro | `toolsSettings.aws.allowedServices[]` |
| `managed_policy.disable_bypass` | Claude | `disableBypassPermissionsMode: "disable"` |
| `managed_policy.lock_mcp` | Claude | `allowManagedMcpServersOnly: true` |
| `steps_limit: 25` | Kilo | `steps: 25` in agent config |

#### Losses on generation

| From | Loss when generating for | What's lost |
|------|-------------------------|-------------|
| Core `tools: ask` | Codex | Cannot express `ask` — only `workspace`/`sandbox`/`full-auto` presets |
| `bash_commands.allow/deny` | Codex | No bash-command granularity — only sandbox mode |
| `edit_paths` | Claude, Codex | No path-level edit restrictions in these CLIs |
| `subagent_delegation` | Codex, Kiro | No per-subagent allow/deny control |
| `network.*` | Claude, OpenCode, Kilo, Kiro | Only Codex has this level of network granularity |
| `toolsSettings.write.allowedPaths` | Claude, OpenCode | Kiro's write-path restrictions don't map cleanly |
| `toolsSettings.shell.autoAllowReadonly` | All except Kiro | Unique to Kiro |
| `toolsSettings.aws.allowedServices` | All except Kiro | Unique to Kiro |
| Kiro `toolAliases`, `resources`, `hooks`, `keyboardShortcut` | Core tier | No equivalent in other CLIs |
| Claude `skillOverrides`, `disable-model-invocation` | Core tier | Unique to Claude |
| Codex `nickname_candidates`, `features.*` | Core tier | Unique to Codex |

### Proposed `profiles.yaml` Permissions Schema

```yaml
permissions:
  # ── Tool access (core tier — maps to all 5 CLIs) ──
  tools:
    read: allow           # allow | ask | deny
    edit: ask
    bash: ask
    glob: allow
    grep: allow
    webfetch: ask
    websearch: ask

  # ── Bash command patterns (core tier — maps to 4 CLIs, Codex uses presets only) ──
  bash_commands:
    allow:
      - "git status"
      - "git diff"
      - "git log"
      - "npm test"
      - "npm run *"
      - "grep"
    deny:
      - "rm -rf *"
      - "git push *"

  # ── File path edit restrictions (core tier — maps to OpenCode, Kilo, Kiro) ──
  edit_paths:
    allow:
      - "src/**"
      - "tests/**"
      - "*.md"
    deny:
      - "*.env"
      - "*.secret"

  # ── Subagent delegation (core tier — maps to Claude, OpenCode, Kilo) ──
  subagent_delegation:
    default: deny
    allow:
      - code-reviewer
      - docs-writer
      - security-auditor

  # ── MCP server access (core tier — maps to all 5 CLIs with different syntax) ──
  mcp:
    allow_servers: []      # empty = all allowed
    deny_servers: []       # blacklisted servers

  # ── CLI-specific tier ──
  # Only generated when targeting the specific CLI.

  auto_approve_readonly: false           # Kiro: toolsSettings.shell.autoAllowReadonly

  network:                                # Codex only
    mode: limited                         # limited | full | sandbox
    allowed_domains: []
    denied_domains: []

  aws_services:                           # Kiro only
    allowed: []

  steps_limit: null                       # Kilo: steps per agent (null = no limit)

  managed_policy:                         # Claude managed-settings only
    disable_bypass: false
    lock_permissions: false
    lock_hooks: false
    lock_mcp: false
```

### Generation Mapping Table

| Profile field | Claude Code | OpenCode / Kilo | Amazon Kiro | Codex CLI |
|---------------|-------------|-----------------|-------------|-----------|
| `tools.*` | `permissions.allow/deny` with `Tool(name)` patterns | `permission.<tool>: "action"` or glob map | `tools[]` whitelist + `allowedTools[]` auto-approve | `default_permissions` preset (all-allow→`full-auto`, ask-default→`workspace`) |
| `bash_commands.allow` | `Bash(pattern)` in `allow` | `permission.bash` glob map → `"allow"` | `toolsSettings.shell.allowedCommands[]` | Ignored (preset only) |
| `bash_commands.deny` | `Bash(pattern)` in `deny` | `permission.bash` glob map → `"deny"` | `toolsSettings.shell.deniedCommands[]` | Ignored (preset only) |
| `edit_paths.allow` | No mapping | `permission.edit` glob map → `"allow"` | `toolsSettings.write.allowedPaths[]` | No mapping |
| `edit_paths.deny` | No mapping | `permission.edit` glob map → `"deny"` + `"*": "deny"` catchall | No mapping (Kiro uses `allowedPaths` allowlist only) | No mapping |
| `subagent_delegation.allow` | `Agent(name)` in `allow` | `permission.task` glob map → `"allow"` | No mapping | No mapping |
| `mcp.allow_servers` | `allowedMcpServers` (managed) | `mcp.<name>.enabled: true` | `tools: ["@server"]` + `allowedTools: ["@server"]` | `enabled = true` |
| `mcp.deny_servers` | `deniedMcpServers` (managed) | `mcp.<name>.enabled: false` | Omit from `tools[]` and `allowedTools[]` | `enabled = false` |
| `auto_approve_readonly` | `autoAllowBashIfSandboxed` (partial) | No mapping | `toolsSettings.shell.autoAllowReadonly` | No mapping |
| `network.*` | `sandbox.network.*` (partial) | No mapping | No mapping | `[permissions.workspace.network]` |
| `aws_services.allowed` | No mapping | No mapping | `toolsSettings.aws.allowedServices[]` | No mapping |
| `steps_limit` | No mapping | No mapping | No mapping | No mapping (Codex uses `job_max_runtime_seconds`) |
| `managed_policy.*` | `managed-settings.json` fields | No mapping | No mapping | No mapping |