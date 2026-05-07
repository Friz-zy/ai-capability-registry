# Tag: prompt

Skills with tag `prompt`:

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## gh-address-comments

Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-address-comments`
- **Skill file**: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`
- **Tags**: `address`, `auth`, `authenticate`, `branch`, `cli`, `comments`, `curated`, `gh-address-comments`, `github`, `issue`, `logged`, `open`, `prompt`, `review`, `verify`

## hook-development

This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`
- **Tags**: `advanced`, `api`, `asks`, `automation`, `block`, `code`, `commands`, `comprehensive`, `create`, `creating`, `dangerous`, `dev`, `development`, `driven`, `event`, `event-driven`, `events`, `focus`, `guidance`, `hook`, `hook-development`, `hooks`, `implement`, `implementing`, `mentions`, `notification`, `posttooluse`, `precompact`, `pretooluse`, `prompt`, `provides`, `root`, `sessionend`, `sessionstart`, `set`, `stop`, `subagentstop`, `used`, `userpromptsubmit`, `validate`

## openai-docs

Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/openai-docs`
- **Skill file**: `external/openai-skills/skills/.curated/openai-docs/SKILL.md`
- **Tags**: `apis`, `asks`, `browsing`, `build`, `bundled`, `case`, `choosing`, `citations`, `context`, `curated`, `date`, `docs`, `documentation`, `domains`, `fallback`, `guidance`, `helper`, `latest`, `mcp`, `model`, `needs`, `prioritize`, `products`, `prompt`, `prompt-upgrade`, `restrict`, `up-to-date`, `upgrade`

## openai-docs

Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/openai-docs`
- **Skill file**: `external/openai-skills/skills/.system/openai-docs/SKILL.md`
- **Tags**: `apis`, `asks`, `browsing`, `build`, `bundled`, `case`, `choosing`, `citations`, `context`, `date`, `docs`, `documentation`, `domains`, `fallback`, `guidance`, `helper`, `latest`, `mcp`, `model`, `needs`, `prioritize`, `products`, `prompt`, `prompt-upgrade`, `restrict`, `up-to-date`, `upgrade`

## playground

Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`
- **Tags**: `asks`, `configure`, `contained`, `controls`, `copy`, `creates`, `explorer`, `explorers`, `html`, `interactive`, `let`, `live`, `make`, `out`, `playground`, `playgrounds`, `preview`, `prompt`, `self`, `self-contained`, `single`, `something`, `topic`, `visually`
