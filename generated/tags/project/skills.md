# Tag: project

Skills with tag `project`:

## burpsuite-project-parser

Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser`
- **Skill file**: `external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`
- **Tags**: `analyzing`, `audit`, `bodies`, `burp`, `burpsuite`, `burpsuite-project-parser`, `captured`, `command`, `data`, `dumping`, `explores`, `extracting`, `findings`, `headers`, `history`, `http`, `line`, `map`, `parser`, `project`, `proxy`, `regex`, `response`, `searches`, `searching`, `security`, `site`, `suite`, `traffic`

## chatgpt-apps

Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/chatgpt-apps`
- **Skill file**: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`
- **Tags**: `aligned`, `apis`, `applications`, `apply`, `apps`, `bridge`, `build`, `chatgpt`, `chatgpt-apps`, `code`, `codex`, `combine`, `compatibility`, `csp`, `curated`, `design`, `developer`, `docs`, `docs-aligned`, `domain`, `generating`, `invoking`, `mcp`, `metadata`, `needs`, `prefer`, `produce`, `project`, `refactor`, `register`, `scaffold`, `sdk`, `server`, `settings`, `troubleshoot`, `widget`, `wire`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## claude-automation-recommender

Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- **Tags**: `analyze`, `asks`, `automation`, `automation-recommender`, `automations`, `code`, `codebase`, `features`, `hooks`, `improving`, `know`, `mcp`, `mentions`, `optimize`, `project`, `recommend`, `recommendations`, `recommender`, `servers`, `set`, `subagents`, `their`, `they`

## claude-md-improver

Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`
- **Tags**: `against`, `asks`, `audit`, `evaluates`, `fix`, `improve`, `improver`, `maintenance`, `makes`, `management`, `md-improver`, `md-management`, `memory`, `mentions`, `optimization`, `outputs`, `project`, `quality`, `report`, `repositories`, `scans`, `targeted`, `then`, `updates`

## cloudflare-deploy

Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cloudflare-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`
- **Tags**: `applications`, `asks`, `cloudflare`, `cloudflare-deploy`, `curated`, `deploy`, `host`, `infrastructure`, `pages`, `platform`, `project`, `publish`, `services`, `set`, `workers`

## devcontainer-setup

Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup`
- **Skill file**: `external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`
- **Tags**: `adding`, `code`, `configuring`, `creates`, `devcontainer`, `devcontainers`, `development`, `environments`, `isolated`, `language`, `node`, `persistent`, `project`, `python`, `rust`, `sandboxed`, `setting`, `support`, `tooling`, `volumes`, `workspaces`

## digest

Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`
- **Tags**: `activity`, `away`, `catching`, `connected`, `daily`, `day`, `decisions`, `digest`, `document`, `enterprise`, `enterprise-search`, `grouped`, `items`, `mentions`, `project`, `reviewing`, `search`, `sources`, `starting`, `summary`, `time`, `updates`, `wanting`, `week`, `weekly`

## figma-create-design-system-rules

Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-design-system-rules`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`
- **Tags**: `code`, `codebase`, `connection`, `conventions`, `create`, `curated`, `custom`, `customize`, `design`, `establish`, `figma`, `figma-create-design`, `figma-to-code`, `generates`, `guidelines`, `mcp`, `project`, `requires`, `says`, `server`, `set`

## internal-comms

A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/internal-comms`
- **Skill file**: `external/anthropic-skills/skills/internal-comms/SKILL.md`
- **Tags**: `asked`, `comms`, `communications`, `company`, `etc`, `faqs`, `formats`, `incident`, `internal`, `internal-comms`, `kinds`, `leadership`, `likes`, `newsletters`, `project`, `reports`, `set`, `some`, `sort`, `status`, `updates`, `whenever`

## migrate-to-codex

Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/migrate-to-codex`
- **Skill file**: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`
- **Tags**: `codex`, `config`, `curated`, `global`, `instruction`, `mcp`, `migrate`, `migrate-to-codex`, `project`, `supported`

## plugin-settings

This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- **Tags**: `asks`, `behavior`, `configurable`, `configuration`, `content`, `dev`, `documents`, `frontmatter`, `local`, `make`, `markdown`, `per`, `per-project`, `project`, `settings`, `state`, `store`, `storing`, `used`, `yaml`

## risk-assessment

Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`
- **Tags**: `assess`, `assessment`, `associated`, `could`, `decision`, `evaluating`, `identify`, `mitigate`, `operational`, `operations`, `process`, `project`, `register`, `risk`, `risk-assessment`, `risks`, `trigger`, `vendor`, `wrong`

## scientific-problem-selection

This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`
- **Tags**: `advice`, `ask`, `bio`, `bio-research`, `choosing`, `decision`, `decisions`, `evaluate`, `have`, `idea`, `ideation`, `include`, `navigate`, `pitch`, `plan`, `problem`, `project`, `projects`, `requests`, `research`, `risks`, `scientific`, `scientific-problem-selection`, `scientists`, `selection`, `strategic`, `strategy`, `stuck`, `trees`, `troubleshooting`, `typical`, `used`

## search

Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`
- **Tags**: `chat`, `cloud`, `connected`, `conversation`, `could`, `decide`, `decision`, `did`, `discussion`, `doc`, `document`, `email`, `enterprise`, `enterprise-search`, `find`, `live`, `looking`, `one`, `project`, `query`, `search`, `sources`, `storage`, `tracker`, `trigger`, `was`, `where`

## start

Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/start`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`
- **Tags**: `analysis`, `bio`, `bio-research`, `checking`, `connected`, `discovery`, `drug`, `drug-discovery`, `environment`, `explore`, `getting`, `literature`, `mcp`, `oriented`, `project`, `research`, `servers`, `set`, `start`, `starting`, `surveying`, `visualization`, `which`

## start

Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/start`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`
- **Tags**: `acronyms`, `bootstrapping`, `codenames`, `dashboard`, `decoding`, `existing`, `initialize`, `memory`, `nicknames`, `open`, `productivity`, `project`, `setting`, `shorthand`, `start`, `time`, `todos`, `working`

## status-report

Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/status-report`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/status-report/SKILL.md`
- **Tags**: `activity`, `attention`, `decisions`, `green`, `health`, `items`, `kpis`, `leadership`, `monthly`, `narrative`, `operations`, `pile`, `project`, `readable`, `red`, `report`, `risks`, `stakeholder`, `status`, `status-report`, `summarizing`, `surfacing`, `tracker`, `turning`, `weekly`, `yellow`

## update

Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/update`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`
- **Tags**: `activity`, `assignments`, `buried`, `catch`, `chat`, `comprehensive`, `email`, `filling`, `gaps`, `memory`, `overdue`, `people`, `productivity`, `project`, `projects`, `pulling`, `refresh`, `running`, `scan`, `stale`, `sync`, `todos`, `tracker`, `triaging`, `unknown`
