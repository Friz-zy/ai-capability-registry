# AI Agent Configuration Reference

A comparative table of AI agent configuration mechanisms via config files (global ~/, project ./, env vars).

> Current as of: May 2026. Sources: official documentation, Context7, GitHub repositories.

| Tool | Templates | Docs |
|------|-----------|------|
| Codex CLI | [README](templates/agents/codex/README.md) · [config.toml](templates/agents/codex/config.toml) · [agent-role.toml](templates/agents/codex/agent-role.toml) · [SKILL.md](templates/agents/codex/SKILL.md) · [AGENTS.md](templates/agents/codex/AGENTS.md) | [GitHub](https://github.com/openai/codex) |
| Claude Code | [README](templates/agents/claude-code/README.md) · [settings.json](templates/agents/claude-code/settings.json) · [settings.local.json](templates/agents/claude-code/settings.local.json) · [.mcp.json](templates/agents/claude-code/.mcp.json) · [agent.md](templates/agents/claude-code/agent.md) · [SKILL.md](templates/agents/claude-code/SKILL.md) · [command.md](templates/agents/claude-code/command.md) · [CLAUDE.md](templates/agents/claude-code/CLAUDE.md) · [rule.md](templates/agents/claude-code/rule.md) | [Docs](https://docs.anthropic.com/en/docs/claude-code) |
| Kilo Code | [README](templates/agents/kilo-code/README.md) · [kilo.jsonc](templates/agents/kilo-code/kilo.jsonc) · [agent.md](templates/agents/kilo-code/agent.md) · [SKILL.md](templates/agents/kilo-code/SKILL.md) · [AGENTS.md](templates/agents/kilo-code/AGENTS.md) · [command.md](templates/agents/kilo-code/command.md) | [Docs](https://kilo.ai/docs/customize) |
| OpenCode | [README](templates/agents/opencode/README.md) · [opencode.json](templates/agents/opencode/opencode.json) · [agent.md](templates/agents/opencode/agent.md) · [SKILL.md](templates/agents/opencode/SKILL.md) · [AGENTS.md](templates/agents/opencode/AGENTS.md) | [GitHub](https://github.com/anomalyco/opencode) |
| Amazon Kiro | [README](templates/agents/amazon-kiro/README.md) · [agent.json](templates/agents/amazon-kiro/agent.json) · [mcp.json](templates/agents/amazon-kiro/mcp.json) · [SKILL.md](templates/agents/amazon-kiro/SKILL.md) · [AGENTS.md](templates/agents/amazon-kiro/AGENTS.md) · [steering-*.md](templates/agents/amazon-kiro/steering-always.md) | [Docs](https://kiro.dev/docs) |

---

## Summary: Capabilities by Configuration Type

| Capability | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|-------------|-----------|-------------|-----------|----------|-------------|
| Roles/agents via config | ✅ TOML | ✅ MD + YAML fm | ✅ JSONC + MD | ✅ JSON + MD | ✅ JSON |
| Skills with auto-discovery | ✅ | ✅ | ✅ | ✅ | ✅ |
| MCP multi-scope | ✅ user/project | ✅ user/project/local/managed/plugin | ✅ global/project | ✅ global/project/agent | ✅ global/project/agent |
| Instructions (AGENTS/CLAUDE) | ✅ hierarchical | ✅ (+ rules) | ✅ (+ per-dir) | ✅ | ✅ steering (4 modes) |
| Plugins | ⚠️ early | ✅ mature | ❌ | ✅ TS/JS | ❌ |
| Hooks | ✅ | ✅ | ❌ | ✅ (via plugins) | ✅ |
| Multi-provider | ❌ | ❌ | ✅ | ✅ (75+) | ❌ |
| Managed/enterprise | ✅ system config | ✅ managed-settings | ✅ managed config | ✅ managed MDM | ✅ MDM/GPO |
| Permissions per agent | ✅ (via role) | ✅ | ✅ | ✅ | ✅ |
| Profiles | ✅ | ❌ | ❌ | ❌ | ❌ |
| LSP | ❌ | ✅ (via plugins) | ❌ | ✅ (native) | ❌ |
| Spec-driven dev | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Configuration Files

| Aspect | Codex CLI (OpenAI) | Claude Code (Anthropic) | Kilo Code | OpenCode | Amazon Kiro (AWS) |
|--------|--------------------|-------------------------|-----------|----------|--------------------|
| **Format** | TOML | JSON / Markdown (YAML fm) | JSONC / Markdown (YAML fm) | JSON / Markdown (YAML fm) | JSON / Markdown (YAML fm) |
| **Template** | [config.toml](templates/agents/codex/config.toml) | [settings.json](templates/agents/claude-code/settings.json) / [.mcp.json](templates/agents/claude-code/.mcp.json) | [kilo.jsonc](templates/agents/kilo-code/kilo.jsonc) | [opencode.json](templates/agents/opencode/opencode.json) | [agent.json](templates/agents/amazon-kiro/agent.json) / [mcp.json](templates/agents/amazon-kiro/mcp.json) |
| **Global config** | `~/.codex/config.toml` | `~/.claude.json` `~/.claude/settings.json` | `~/.config/kilo/kilo.jsonc` | `~/.config/opencode/opencode.json` | `~/.kiro/` |
| **Project config** | `.codex/config.toml` | `.claude/settings.json` `.mcp.json` | `kilo.jsonc` `.kilo/kilo.jsonc` | `opencode.json` | `.kiro/` |
| **Local/private config** | — | `.claude/settings.local.json` `CLAUDE.local.md` | — | — | — |
| **Profiles** | `~/.codex/<name>.config.toml` (`--profile`) | — | — | — | — |
| **Managed/enterprise** | `/etc/codex/config.toml` | `managed-settings.json` | `/etc/kilo/kilo.json` | Managed MDM `.mobileconfig` | MDM/Group Policy → `~/.kiro/steering/` |
| **Config via env var** | `CODEX_HOME` | — | `KILO_CONFIG` `KILO_CONFIG_CONTENT` | `OPENCODE_CONFIG` `OPENCODE_CONFIG_CONTENT` `OPENCODE_CONFIG_DIR` | — |
| **Remote config** | — | — | — | `.well-known/opencode` | — |
| **Schema validation** | JSON Schema (`just write-config-schema`) | JSON (schema enforced) | JSON Schema (`$schema`) | JSON Schema (`https://opencode.ai/config.json`) | — |

---

## Roles and Agents (Subagents)

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Template** | [agent-role.toml](templates/agents/codex/agent-role.toml) | [agent.md](templates/agents/claude-code/agent.md) | [agent.md](templates/agents/kilo-code/agent.md) | [agent.md](templates/agents/opencode/agent.md) | [agent.json](templates/agents/amazon-kiro/agent.json) |
| **Global agents** | `~/.codex/config.toml` → `[agents.<name>]` | `~/.claude/agents/<name>.md` | `~/.config/kilo/agent/<name>.md` | `~/.config/opencode/agents/<name>.md` | `~/.kiro/agents/<name>.json` |
| **Project agents** | `.codex/config.toml` → `[agents.<name>]` | `.claude/agents/<name>.md` | `.kilo/agent/<name>.md` | `.opencode/agents/<name>.md` | `.kiro/agents/<name>.json` |
| **Inline (config)** | `[agents.<name>]` TOML | — | `agent.<name>` in kilo.jsonc | `agent.<name>` in opencode.json | — |
| **Agent file format** | TOML → `AgentRoleToml` (+ `config_file`) | Markdown YAML frontmatter | Markdown YAML frontmatter | Markdown YAML frontmatter | JSON |
| **Agent fields: mode** | implicit (subagent) | `mode:` not needed (always subagent) | `mode: primary / subagent / all` | `mode: primary / subagent / all` | — (always primary) |
| **Agent fields: model** | from config_file | in frontmatter (undocumented) | `model: provider/model` | `model: provider/model` | `model: "model-id"` |
| **Agent fields: prompt** | `description` in TOML | `prompt` in Markdown frontmatter | `prompt: "..."` in config | `prompt: "..."` / `{file:./path}` | `prompt: "..."` |
| **Agent fields: tools** | — (via permissions) | `tools:` list in frontmatter | `permission:` in frontmatter | `permission:` + `tools:` (deprecated) | `tools: [...]`, `toolAliases`, `toolsSettings`, `allowedTools` |
| **Agent fields: hidden** | — | `hidden: true` | `hidden: true` | `hidden: true` | — |
| **Agent fields: max steps** | — | — | `steps: 25` | — | — |
| **Agent fields: resources** | — | — | — | — | `resources: ["file://...", "skill://..."]` + knowledge bases |
| **Agent fields: hooks** | — | — | — | — | `hooks: {...}` |
| **Agent fields: keyboard shortcut** | — | — | — | — | `keyboardShortcut: "..."` |
| **Agent nickname** | `nickname_candidates: [...]` | — | — | — | — |
| **Agent role file** | `config_file` → separate TOML | — | — | — | — |
| **Task subagent delegation** | — | — | `permission.task` with globs | `permission.task` with globs | — |

---

## Skills

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Template** | [SKILL.md](templates/agents/codex/SKILL.md) | [SKILL.md](templates/agents/claude-code/SKILL.md) | [SKILL.md](templates/agents/kilo-code/SKILL.md) | [SKILL.md](templates/agents/opencode/SKILL.md) | [SKILL.md](templates/agents/amazon-kiro/SKILL.md) |
| **Format** | `SKILL.md` with metadata | `SKILL.md` YAML frontmatter + Markdown | `SKILL.md` YAML frontmatter (name, description) | `SKILL.md` YAML frontmatter (name, description) | `SKILL.md` YAML frontmatter (name, description) |
| **Global skills** | `~/.agents/skills/<name>/SKILL.md` | `~/.claude/skills/<name>/SKILL.md` | `~/.config/kilo/skills/<name>/SKILL.md` `.kilo/skills/<name>/SKILL.md` | `~/.config/opencode/skills/<name>/SKILL.md` | `~/.kiro/skills/<name>/SKILL.md` |
| **Project skills** | `.agents/skills/<name>/SKILL.md` | `.claude/skills/<name>/SKILL.md` | `.kilo/skills/<name>/SKILL.md` | `.opencode/skills/<name>/SKILL.md` | `.kiro/skills/<name>/SKILL.md` |
| **Compat skills** | — | — | `.claude/skills/` `.agents/skills/` | `.claude/skills/` `.agents/skills/` | — |
| **Config paths** | `skills.config.[].path` `skills.config.[].enabled` | — (auto-discovery) | `skills.paths: [...]` `skills.urls: [...]` | — (auto-discovery) | `resources: ["skill://..."]` in agent |
| **YAML frontmatter fields** | description (standard) | `description`, `name`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `shell` | `name`, `description` | `name`, `description`, `license`, `compatibility`, `metadata` | `name`, `description` |
| **Skill command name** | — | directory name = `/skill-name` | directory name | directory name | — |
| **Auto-invoke** | ✅ (model decides) | ✅ (if `description` matches) | ✅ | ✅ | — (manual activation) |
| **Manual only** | — | `disable-model-invocation: true` | — | — | — |
| **Model override** | — | `model:` in frontmatter | — | — | — |
| **Fork/context** | — | `context: fork` + `agent:` | — | — | — |
| **Permissions per skill** | — | `allowed-tools` | — | `permission.skill` with pattern matching | — |
| **Dependencies** | `SkillDependencies {tools: [...]}` | — | — | — | — |
| **Shell exec in skill** | — | `!command` / ````!` blocks | — | — | — |
| **Skill env var** | — | `${CLAUDE_SKILL_DIR}` | — | — | — |
| **Commands (flat skills)** | — | `.claude/commands/<name>.md` (merged) | `.kilo/command/<name>.md` | — | — |

---

## MCP Servers

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Format** | TOML `[mcp_servers]` | JSON `mcpServers` | JSONC `mcp` | JSON `mcp` | JSON `mcpServers` |
| **Global MCP** | `~/.codex/config.toml` | `~/.claude.json` | `~/.config/kilo/kilo.jsonc` | `~/.config/opencode/opencode.json` | `~/.kiro/settings/mcp.json` |
| **Project MCP** | `.codex/config.toml` | `.mcp.json` (project root) | `.kilo/kilo.jsonc` `kilo.jsonc` | `opencode.json` | `.kiro/settings/mcp.json` |
| **Multiple files** | — | user/local/project/plugin/managed | global + project merge | global + project merge | global + project + per-agent + `includeMcpJson` |
| **Transports** | stdio + streamable HTTP | stdio + streamable HTTP + SSE + WebSocket | local (stdio) + remote (HTTP) | local (stdio) + remote (HTTP) | stdio + streamable HTTP |
| **Stdio example** | `command = "..."` `args = [...]` `env = {...}` | `"command": "..."` `"args": [...]` `"env": {...}` | `"command": [...]` `"environment": {...}` | `"command": [...]` `"env": {...}` | `"command": "..."` `"args": [...]` `"env": {...}` |
| **HTTP example** | type=sse/streamable_http + url | type=http + url + headers | type=remote + url + headers | type=remote + url + headers | url + type |
| **OAuth** | ✅ (streamable HTTP) | ✅ (OAuth flow) | ✅ (`oauth.clientId`, `.scope`) | ✅ (`opencode mcp auth`) | — |
| **CLI management** | `codex mcp add/list/remove` | `claude mcp add/list/remove` | — (via UI/Settings) | `opencode mcp add/list` | — (via config) |
| **Scope (MCP)** | — (project config trusted only) | local / project / user | global / project (merge) | global / project (merge) + per-agent | per-agent + global/project (`includeMcpJson`) |
| **Enable/disable** | `enabled = true/false` | `disabledMcpjsonServers` `enabledMcpjsonServers` | `"enabled": true/false` | `"enabled": true/false` | `"disabled": false` |
| **Tool allowlist** | — | `allowedMcpServers` `deniedMcpServers` (managed) | `permission` with wildcards `{server}_{tool}` | `permission` with wildcards | `allowedTools: [...]` `autoApprove: [...]` |
| **Env var expansion** | ✅ (TOML env) | ✅ (`${VAR}`) | ✅ (`{env:VAR}`) | ✅ (`env:VAR`) | ✅ (`${key_name}`) |
| **Plugin MCP** | — | `.mcp.json` in plugin root / inline `plugin.json` | — | — | — |
| **Managed MCP** | — | `managed-mcp.json` | — | — | — |
| **Authentication discovery** | — | `authServerMetadataUrl` + `oauth.scopes` | — | — | — |
| **Timeout** | — | — | `timeout` (ms) | — | — |

---

## Instructions and Context

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Template** | [AGENTS.md](templates/agents/codex/AGENTS.md) | [CLAUDE.md](templates/agents/claude-code/CLAUDE.md) / [rule.md](templates/agents/claude-code/rule.md) | [AGENTS.md](templates/agents/kilo-code/AGENTS.md) | [AGENTS.md](templates/agents/opencode/AGENTS.md) | [AGENTS.md](templates/agents/amazon-kiro/AGENTS.md) / [steering-*.md](templates/agents/amazon-kiro/steering-always.md) |
| **Standard** | `AGENTS.md` | `CLAUDE.md` | `AGENTS.md` | `AGENTS.md` | `AGENTS.md` + steering |
| **Global instructions** | `~/.codex/AGENTS.md` | `~/.claude/CLAUDE.md` | config `instructions` key | — | `~/.kiro/steering/<name>.md` |
| **Project instructions** | `AGENTS.md` (root + nested, hierarchical) | `CLAUDE.md` / `.claude/CLAUDE.md` | `AGENTS.md` (root + per-dir) | `AGENTS.md` | `.kiro/steering/<name>.md` `AGENTS.md` |
| **Local overrides** | — | `CLAUDE.local.md` | — | — | — |
| **Config-based** | `model_instructions_file` | — | `instructions` key in config | `instructions` key in config | — |
| **Scoped rules** | AGENTS.md hierarchy by directory | `.claude/rules/<name>.md` (path-scoped) | — | — | steering `condition: "*.ts"` glob patterns |
| **Steering modes** | — | — | — | — | `always` / `conditional` (glob) / `manual` (#name) / `auto` (description) |
| **Managed instructions** | — | `claudeMd` in managed-settings | — | — | MDM/Group Policy push |
| **Precedence** | nested AGENTS.md > parent AGENTS.md | `.claude/CLAUDE.md` > root `CLAUDE.md` | agent.prompt > config instructions > AGENTS.md | agent.prompt > config instructions > AGENTS.md | workspace > global; AGENTS.md = always |

---

## Models and Providers

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Model config** | `model` key (TOML) | `/model` command (runtime) | `model` key (config) or `/models` menu | `model.default` + `model.fast` | `model` per agent |
| **Provider config** | `model_provider` `model_providers` | built-in (Anthropic) + Vertex AI | `provider` key + `api_key` with `env:` | `provider.<name>` with `api_key` + `api_url` | built-in (AWS Bedrock) |
| **API key** | `OPENAI_API_KEY` env, keychain, file | `ANTHROPIC_API_KEY` env | in config `api_key: "env:VAR"` | in config `api_key: "env:VAR"` | IAM / AWS profile |
| **Base URL** | `openai_base_url` `chatgpt_base_url` | `ANTHROPIC_BASE_URL` env | — | `api_url` | — |
| **Model per agent** | via role config_file | via `/model` (session) | ✅ via agent config | ✅ via agent config | ✅ |
| **Review model** | `review_model` | — | — | — | — |
| **Context window** | `model_context_window` | — | — | — | — |
| **Auto-compact** | `model_auto_compact_token_limit` `model_auto_compact_token_limit_scope` | — | — | — | — |
| **Reasoning effort** | — | — | — | — | — |
| **Provider-agnostic** | ❌ (OpenAI-first) | ❌ (Anthropic/Vert.AI) | ✅ (multi-provider) | ✅ (75+ providers) | ❌ (AWS-focused) |

---

## Permissions and Security

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Global** | approval policies in config | `permissions` in settings.json | `permission` key in config | `permission` key in config | — |
| **Per-agent** | — | ✅ `.claude/agents/` | ✅ agent frontmatter / config | ✅ agent frontmatter / config | ✅ `allowedTools` `toolsSettings` |
| **Tool-level** | sandbox settings | `allow` / `deny` / `ask` | `allow` / `ask` / `deny` | `allow` / `ask` / `deny` | `allowedTools` + `autoApprove` |
| **Path restrict** | — | — | glob patterns (`*.md: allow`) | glob patterns | `toolsSettings.allowedPaths` |
| **MCP tool restrict** | — | wildcards (`mcp_server_tool`) | wildcards (`{server}_{tool}`) | wildcards (`mymcp_*: deny`) | per-tool `autoApprove` |
| **Skill restrict** | `skills.config.[].enabled` | `skillOverrides` (on/off/name-only) | — | `permission.skill` patterns | — |
| **Shell restrict** | approval policies | `disableSkillShellExecution` (managed) | bash permission per agent | bash permission per agent | write tools opt-in |
| **External dir restrict** | — | — | — | ✅ `external_directory` key | — |
| **Task delegation restrict** | — | — | ✅ `permission.task` with globs | ✅ `permission.task` with globs | — |
| **Project trust** | project `.codex/` ignored if untrusted | trust dialog per project | — | — | — |
| **Managed policy** | managed prefs | `strictPluginOnlyCustomization` `allowManagedHooksOnly` `allowManagedMcpServersOnly` `deniedMcpServers` | — | managed config | — |

---

## Plugins and Extensions

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Plugins** | `.agents/plugins/` (early stage) | `.claude-plugin/plugin.json` with `skills/` `agents/` `hooks/` `.mcp.json` `monitors/` `settings.json` `bin/` | — | `.opencode/plugins/<name>.ts` / npm packages in `plugin` array | — |
| **Marketplace** | — | `claude-plugins-official` + custom | — | — | — |
| **Plugin lifecycle** | — | `/plugin install`, `/reload-plugins` | — | — | — |
| **Plugin MCP** | — | `.mcp.json` / inline `plugin.json` | — | — | — |
| **Plugin hooks** | — | `hooks/hooks.json` | — | 25+ lifecycle hooks | `.kiro/hooks/` |
| **Plugin commands** | — | `/plugin-name:command-name` | — | — | — |
| **Plugin agent override** | — | `agent` in plugin `settings.json` | — | — | — |
| **Plugin LSP** | — | `.lsp.json` | — | LSP built-in (native) | — |
| **Custom tools** | — | — | — | `.opencode/tool/<name>.ts` | — |
| **Hooks standalone** | `hooks.json` + `[hooks]` inline | `settings.json` → `hooks` | — | — | agent JSON `hooks` |

---

## Feature Flags and Experimental Capabilities

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Declarative** | `[features]` table in config.toml | settings.json feature keys | — | — | — |
| **CLI** | `codex --enable <name>`, `codex features enable/disable` | — | — | — | — |
| **Requirements** | `requirements.toml` for per-project pinning | — | — | — | — |
| **Key flags** | `multi_agent`, `hooks`, `shell_tool`, `memories`, `personality`, `web_search`, `undo`, `apps`, `codex_git_commit` | `channelsEnabled`, `enableAllProjectMcpServers`, `toolSearch` | — | — | — |

---

## State Management and Memory

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Memories** | ✅ `memories` feature flag | ✅ auto memory (v2.1.59+) → `~/.claude/projects/*/memory/MEMORY.md` | — | — | — |
| **Persistent history** | `~/.codex/history.jsonl` | session projects | — | — | — |
| **Git commit** | `codex_git_commit` feature flag | — | — | — | — |
| **Shell snapshot** | `shell_snapshot` feature | — | — | — | — |
| **Undo** | `undo` feature (git ghost snapshots) | — | — | — | — |

---

## Key Environment Variables

| Aspect | Codex CLI | Claude Code | Kilo Code | OpenCode | Amazon Kiro |
|--------|-----------|-------------|-----------|----------|-------------|
| **Config path** | `CODEX_HOME` | — | `KILO_CONFIG`, `KILO_CONFIG_CONTENT` | `OPENCODE_CONFIG`, `OPENCODE_CONFIG_CONTENT`, `OPENCODE_CONFIG_DIR` | — |
| **API key** | `OPENAI_API_KEY` | `ANTHROPIC_API_KEY` | — (in config) | — (in config) | `AWS_PROFILE`, `AWS_REGION` |
| **Base URL** | — | `ANTHROPIC_BASE_URL` | — | — | — |
| **Disable skills** | — | — | `KILO_DISABLE_EXTERNAL_SKILLS` | — | — |
| **CLAUDE.md from extra dirs** | — | `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | — | — | — |
| **MCP from claude.ai** | — | `ENABLE_CLAUDEAI_MCP_SERVERS` | — | — | — |
| **Tool search** | — | `ENABLE_TOOL_SEARCH` | — | — | — |
| **PowerShell** | — | `CLAUDE_CODE_USE_POWERSHELL_TOOL` | — | — | — |
| **Project dir (MCP)** | — | `CLAUDE_PROJECT_DIR` | — | — | — |
