# set

## Skills
Load skill file when task matches.

### access
Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel.

File: `../external/anthropic-claude-plugins-official/external_plugins/discord/skills/access/SKILL.md`

### access
Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel.

File: `../external/anthropic-claude-plugins-official/external_plugins/imessage/skills/access/SKILL.md`

### access
Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel.

File: `../external/anthropic-claude-plugins-official/external_plugins/telegram/skills/access/SKILL.md`

### audit-prep-assistant
Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

### build-mcpb
This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

### claude-automation-recommender
Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

File: `../external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

### cloudflare-deploy
Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.

File: `../external/openai-skills/skills/.curated/cloudflare-deploy/SKILL.md`

### configure
Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`

### configure
Check iMessage channel setup and review access policy. Use when the user asks to configure iMessage, asks "how do I set this up" or "who can reach me," or wants to know why texts aren't reaching the assistant.

File: `../external/anthropic-claude-plugins-official/external_plugins/imessage/skills/configure/SKILL.md`

### configure
Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure/SKILL.md`

### figma-create-design-system-rules
Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

File: `../external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`

### figma-generate-library
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

File: `../external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`

### figma-use
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

File: `../external/openai-skills/skills/.curated/figma-use/SKILL.md`

### hook-development
This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on advanced prompt-based hooks API.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/hook-development/SKILL.md`

### internal-comms
A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

File: `../external/anthropic-skills/skills/internal-comms/SKILL.md`

### mcp-integration
This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`

### plugin-structure
This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

File: `../external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### sprint-planning
Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounting for PTO and meetings), deciding what's P0 vs. stretch, or handling carryover from the last sprint.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/sprint-planning/SKILL.md`

### start
Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`

### start
Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`

### theme-factory
Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.

File: `../external/anthropic-skills/skills/theme-factory/SKILL.md`
