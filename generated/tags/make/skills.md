# Tag: make

Skills with tag `make`:

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

## pdf

Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pdf`
- **Skill file**: `external/anthropic-skills/skills/pdf/SKILL.md`
- **Tags**: `adding`, `anything`, `apart`, `asks`, `combining`, `creating`, `decrypting`, `encrypting`, `extracting`, `filling`, `forms`, `images`, `includes`, `make`, `mentions`, `merging`, `multiple`, `ocr`, `one`, `pages`, `pdf`, `pdfs`, `produce`, `reading`, `rotating`, `scanned`, `searchable`, `splitting`, `tables`, `text`, `them`, `watermarks`, `whenever`

## playground

Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`
- **Tags**: `asks`, `configure`, `contained`, `controls`, `copy`, `creates`, `explorer`, `explorers`, `html`, `interactive`, `let`, `live`, `make`, `out`, `playground`, `playgrounds`, `preview`, `prompt`, `self`, `self-contained`, `single`, `something`, `topic`, `visually`

## plugin-settings

This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- **Tags**: `asks`, `behavior`, `configurable`, `configuration`, `content`, `dev`, `documents`, `frontmatter`, `local`, `make`, `markdown`, `per`, `per-project`, `project`, `settings`, `state`, `store`, `storing`, `used`, `yaml`

## roadmap-update

Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new information comes in, moving timelines due to a dependency slip, or building a Now/Next/Later view from scratch.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update`
- **Skill file**: `external/anthropic-knowledge-work-plugins/product-management/skills/roadmap-update/SKILL.md`
- **Tags**: `adding`, `building`, `comes`, `create`, `deciding`, `dependency`, `due`, `information`, `initiative`, `later`, `make`, `management`, `moves`, `moving`, `next`, `now`, `priorities`, `product`, `product-management`, `reprioritize`, `roadmap`, `room`, `scratch`, `shifting`, `slip`, `timelines`, `view`

## setup-zoom-websockets

Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constraints make WebSockets preferable to webhooks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/websockets/SKILL.md`
- **Tags**: `connections`, `constraints`, `delivery`, `event`, `faster`, `latency`, `low`, `low-latency`, `make`, `partner`, `persistent`, `preferable`, `routing`, `security`, `webhooks`, `websockets`, `zoom`, `zoom-websockets`

## slack-gif-creator

Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/slack-gif-creator`
- **Skill file**: `external/anthropic-skills/skills/slack-gif-creator/SKILL.md`
- **Tags**: `animated`, `animation`, `concepts`, `constraints`, `creating`, `creator`, `doing`, `gif`, `gifs`, `knowledge`, `like`, `make`, `optimized`, `provides`, `request`, `slack`, `slack-gif-creator`, `utilities`, `validation`

## synthesize-research

Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey responses, or support tickets to make sense of, need to extract themes and rank findings by frequency and impact, or want to turn raw feedback into roadmap recommendations.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/product-management/skills/synthesize-research/SKILL.md`
- **Tags**: `extract`, `feedback`, `findings`, `frequency`, `have`, `impact`, `insights`, `interview`, `interviews`, `make`, `management`, `notes`, `pile`, `product`, `product-management`, `rank`, `raw`, `recommendations`, `research`, `responses`, `roadmap`, `sense`, `structured`, `support`, `survey`, `surveys`, `synthesize`, `synthesize-research`, `themes`, `tickets`, `turn`, `want`
