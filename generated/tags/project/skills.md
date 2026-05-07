# project

## Skills
Load skill and **use it** when task matches.

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `../external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

File: `../external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `../external/anthropic-skills/skills/claude-api/SKILL.md`

### claude-automation-recommender
Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

File: `../external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

### claude-md-improver
Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

File: `../external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

### cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

File: `../external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`

### devcontainer-setup
Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

File: `../external/trailofbits-skills/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

### digest
Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of mentions and action items, or reviewing a week's decisions and document updates grouped by project.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/digest/SKILL.md`

### figma-create-design-system-rules
Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

File: `../external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

File: `../external/anthropic-skills/skills/internal-comms/SKILL.md`

### migrate-to-codex
Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

File: `../external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`

### plugin-settings
This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`

### risk-assessment
Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`

### scientific-problem-selection
This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`

### search
Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

File: `../external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`

### start
Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`

### start
Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`

### status-report
Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

File: `../external/anthropic-knowledge-work-plugins/operations/skills/status-report/SKILL.md`

### update
Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

File: `../external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`
