# Tag: model

Skills with tag `model`:

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

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## comp-analysis

Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`
- **Tags**: `analysis`, `analyze`, `band`, `benchmarking`, `comp`, `comp-analysis`, `compensation`, `competitive`, `data`, `equity`, `find`, `grant`, `human`, `model`, `modeling`, `offer`, `outliers`, `pay`, `placement`, `retention`, `risks`, `role`, `trigger`, `uploading`

## crypto-protocol-diagram

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`
- **Tags**: `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`, `cryptographic`, `diagram`, `diagramming`, `diagrams`, `double`, `drawing`, `ecdh`, `exchange`, `extracting`, `extracts`, `flow`, `frost`, `generates`, `handshake`, `informal`, `key`, `mermaid`, `message`, `model`, `models`, `noise`, `papers`, `prose`, `protocol`, `protocols`, `proverif`, `pseudocode`, `ratchet`, `rfc`, `rfcs`, `sequence`, `sequencediagrams`, `signal`, `spec`, `spthy`, `tamarin`, `tls`, `trailmark`, `visualizing`, `x3dh`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

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

## mermaid-to-proverif

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`
- **Tags**: `attacks`, `authentication`, `checking`, `converting`, `cryptographic`, `describing`, `diagram`, `formal`, `formally`, `forward`, `generating`, `mermaid`, `mermaid-to-proverif`, `model`, `models`, `producing`, `properties`, `protocol`, `protocols`, `proverif`, `replay`, `secrecy`, `security`, `sequence`, `sequencediagrams`, `trailmark`, `translates`, `verification`, `verifying`

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

## openai-security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`
- **Tags**: `assets`, `attacker`, `boundaries`, `capabilities`, `enumerates`, `grounded`, `model`, `modeling`, `repository`, `repository-grounded`, `security`, `security-threat-model`, `threat`, `trust`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## zoom-general

Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`
- **Tags**: `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`, `clear`, `comparisons`, `considerations`, `context`, `cross`, `cross-product`, `general`, `guidance`, `marketplace`, `mcp`, `model`, `partner`, `platform`, `product`, `routing`, `scopes`, `shared`, `zoom`, `zoom-general`
