# Tag: mcp

Skills with tag `mcp`:

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

## chatgpt-apps

Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/chatgpt-apps`
- **Skill file**: `external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`
- **Tags**: `aligned`, `apis`, `applications`, `apply`, `apps`, `bridge`, `build`, `chatgpt`, `chatgpt-apps`, `code`, `codex`, `combine`, `compatibility`, `csp`, `curated`, `design`, `developer`, `docs`, `docs-aligned`, `domain`, `generating`, `invoking`, `mcp`, `metadata`, `needs`, `prefer`, `produce`, `project`, `refactor`, `register`, `scaffold`, `sdk`, `server`, `settings`, `troubleshoot`, `widget`, `wire`

## choose-zoom-approach

Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`
- **Tags**: `api`, `approach`, `apps`, `architecture`, `between`, `case`, `center`, `choose`, `choose-zoom-approach`, `contact`, `deciding`, `hybrid`, `mcp`, `meeting`, `partner`, `phone`, `rest`, `right`, `sdk`, `video`, `webhooks`, `websockets`, `zoom`

## claude-automation-recommender

Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- **Tags**: `analyze`, `asks`, `automation`, `automation-recommender`, `automations`, `code`, `codebase`, `features`, `hooks`, `improving`, `know`, `mcp`, `mentions`, `optimize`, `project`, `recommend`, `recommendations`, `recommender`, `servers`, `set`, `subagents`, `their`, `they`

## claude-in-chrome-troubleshooting

Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting`
- **Skill file**: `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting/SKILL.md`
- **Tags**: `behave`, `browser`, `chrome`, `connected`, `connectivity`, `diagnose`, `erratically`, `extension`, `fail`, `fix`, `in-chrome`, `in-chrome-troubleshooting`, `issues`, `mcp`, `return`, `troubleshooting`

## debug-zoom

Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`
- **Tags**: `api`, `auth`, `behavior`, `broken`, `debug`, `debug-zoom`, `failing`, `failure`, `hypothesis`, `integration`, `isolating`, `mcp`, `partner`, `plus`, `point`, `ranked`, `right`, `routing`, `sdk`, `verification`, `webhook`, `zoom`

## debug-zoom-integration

Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate the layer before proposing a fix.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`
- **Tags**: `auth`, `broken`, `debug`, `debug-zoom-integration`, `failing`, `fix`, `implementations`, `integration`, `isolate`, `joins`, `layer`, `mcp`, `media`, `partner`, `proposing`, `quickly`, `real`, `real-time`, `sdk`, `time`, `transport`, `webhooks`, `zoom`

## design-mcp-workflow

Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsibilities from REST API responsibilities.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md`
- **Tags**: `api`, `deciding`, `design`, `design-mcp`, `fits`, `mcp`, `partner`, `planning`, `responsibilities`, `rest`, `separating`, `whether`, `zoom`

## figma

Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma`
- **Skill file**: `external/openai-skills/skills/.curated/figma/SKILL.md`
- **Tags**: `assets`, `code`, `context`, `curated`, `design`, `design-to-code`, `fetch`, `figma`, `ids`, `implementation`, `involves`, `mcp`, `node`, `nodes`, `production`, `screenshots`, `server`, `translate`, `trigger`, `troubleshooting`, `urls`, `variables`

## figma-create-design-system-rules

Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-design-system-rules`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`
- **Tags**: `code`, `codebase`, `connection`, `conventions`, `create`, `curated`, `custom`, `customize`, `design`, `establish`, `figma`, `figma-create-design`, `figma-to-code`, `generates`, `guidelines`, `mcp`, `project`, `requires`, `says`, `server`, `set`

## mcp-builder

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/mcp-builder`
- **Skill file**: `external/anthropic-skills/skills/mcp-builder/SKILL.md`
- **Tags**: `apis`, `builder`, `building`, `context`, `creating`, `designed`, `enable`, `fastmcp`, `high`, `high-quality`, `integrate`, `interact`, `llms`, `mcp`, `mcp-builder`, `model`, `node`, `protocol`, `python`, `quality`, `sdk`, `servers`, `services`, `typescript`, `well`, `well-designed`, `whether`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## migrate-to-codex

Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/migrate-to-codex`
- **Skill file**: `external/openai-skills/skills/.curated/migrate-to-codex/SKILL.md`
- **Tags**: `codex`, `config`, `curated`, `global`, `instruction`, `mcp`, `migrate`, `migrate-to-codex`, `project`, `supported`

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

## plan-zoom-product

Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`
- **Tags**: `api`, `apps`, `between`, `building`, `case`, `center`, `choose`, `clearly`, `contact`, `deciding`, `explain`, `goal`, `idea`, `integration`, `mcp`, `meeting`, `partner`, `phone`, `plan`, `plan-zoom-product`, `product`, `rest`, `right`, `sdk`, `surface`, `tradeoffs`, `video`, `webhooks`, `websockets`, `zoom`

## setup-zoom-mcp

Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or defining a hybrid MCP architecture.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md`
- **Tags**: `architecture`, `between`, `data`, `decide`, `deciding`, `defining`, `fit`, `hybrid`, `mcp`, `over`, `partner`, `plan`, `planning`, `produce`, `rest`, `right`, `safe`, `zoom`, `zoom-mcp`

## source-management

Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`
- **Tags**: `awareness`, `connect`, `connected`, `detects`, `enterprise`, `enterprise-search`, `guides`, `handles`, `limiting`, `management`, `manages`, `mcp`, `ones`, `ordering`, `priority`, `rate`, `search`, `sources`

## start

Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/start`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/start/SKILL.md`
- **Tags**: `analysis`, `bio`, `bio-research`, `checking`, `connected`, `discovery`, `drug`, `drug-discovery`, `environment`, `explore`, `getting`, `literature`, `mcp`, `oriented`, `project`, `research`, `servers`, `set`, `start`, `starting`, `surveying`, `visualization`, `which`

## zoom-general

Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`
- **Tags**: `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`, `clear`, `comparisons`, `considerations`, `context`, `cross`, `cross-product`, `general`, `guidance`, `marketplace`, `mcp`, `model`, `partner`, `platform`, `product`, `routing`, `scopes`, `shared`, `zoom`, `zoom-general`

## zoom-mcp

Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, recordings, meeting assets, or transcripts. Route Zoom Docs requests to the dedicated Docs MCP server and Whiteboard-specific requests to `zoom-mcp/whiteboard`.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/SKILL.md`
- **Tags**: `access`, `assets`, `bundled`, `connectors`, `dedicated`, `docs`, `guidance`, `mcp`, `meeting`, `meetings`, `partner`, `planning`, `recordings`, `requests`, `route`, `routing`, `server`, `transcripts`, `troubleshooting`, `whiteboard`, `zoom`, `zoom-mcp`

## zoom-mcp/whiteboard

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/whiteboard`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-mcp/whiteboard/SKILL.md`
- **Tags**: `mcp`, `partner`, `whiteboard`, `zoom`, `zoom-mcp`
