# Tag: apps

Skills with tag `apps`:

## aspnet-core

Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web Apps, Razor Pages, MVC, Minimal APIs, controller-based Web APIs, SignalR, gRPC, middleware, dependency injection, configuration, authentication, authorization, testing, performance, deployment, or ASP.NET Core upgrades.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/aspnet-core`
- **Skill file**: `external/openai-skills/skills/.curated/aspnet-core/SKILL.md`
- **Tags**: `apis`, `applications`, `apps`, `architect`, `asp`, `aspnet`, `aspnet-core`, `authentication`, `authorization`, `blazor`, `build`, `configuration`, `controller`, `core`, `curated`, `dependency`, `deployment`, `development`, `grpc`, `guidance`, `injection`, `middleware`, `minimal`, `mvc`, `net`, `pages`, `performance`, `razor`, `refactor`, `review`, `signalr`, `testing`, `upgrades`, `web`, `working`

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

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

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## insecure-defaults

Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
- **Skill file**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- **Tags**: `allow`, `analyzing`, `apps`, `auditing`, `auth`, `config`, `defaults`, `detects`, `environment`, `fail`, `fail-open`, `handling`, `hardcoded`, `insecure`, `insecure-defaults`, `insecurely`, `management`, `open`, `permissive`, `production`, `reviewing`, `secrets`, `security`, `variable`, `weak`

## plan-zoom-product

Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`
- **Tags**: `api`, `apps`, `between`, `building`, `case`, `center`, `choose`, `clearly`, `contact`, `deciding`, `explain`, `goal`, `idea`, `integration`, `mcp`, `meeting`, `partner`, `phone`, `plan`, `plan-zoom-product`, `product`, `rest`, `right`, `sdk`, `surface`, `tradeoffs`, `video`, `webhooks`, `websockets`, `zoom`

## zoom-apps-sdk

Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`
- **Tags**: `app`, `apps`, `building`, `client`, `in-client`, `inside`, `main`, `meetings`, `partner`, `phone`, `routing`, `sdk`, `web`, `webinars`, `zoom`, `zoom-apps-sdk`

## zoom-meeting-sdk-react-native

Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md`
- **Tags**: `android`, `apps`, `auth`, `bridge`, `embedding`, `flows`, `ios`, `join`, `jwt`, `meeting`, `meeting-sdk`, `meetings`, `meetingsdk`, `meetingsdk-react-native`, `native`, `partner`, `platform`, `react`, `react-native`, `sdk`, `start`, `troubleshooting`, `zoom`, `zoom-meeting-sdk-react-native`
