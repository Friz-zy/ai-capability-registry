# Tag: sdk

Skills with tag `sdk`:

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

## build-zoom-bot

Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combining Meeting SDK, RTMS, and backend services.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md`
- **Tags**: `backend`, `bot`, `build`, `build-zoom-bot`, `combining`, `joining`, `live`, `media`, `meeting`, `meetings`, `partner`, `processing`, `programmatically`, `real`, `real-time`, `recorder`, `rtms`, `sdk`, `services`, `time`, `transcripts`, `zoom`

## build-zoom-meeting-app

Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`
- **Tags**: `app`, `between`, `build`, `build-zoom-meeting-app`, `deciding`, `embed`, `embeds`, `flow`, `flows`, `implementing`, `joins`, `lifecycle`, `meeting`, `mobile`, `partner`, `sdk`, `video`, `web`, `zoom`

## build-zoom-meeting-sdk-app

Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md`
- **Tags**: `app`, `auth`, `behavior`, `bot`, `build`, `build-zoom-meeting-sdk-app`, `embed`, `flows`, `implementing`, `issues`, `join`, `joins`, `meeting`, `meeting-embed`, `meeting-sdk`, `partner`, `platform`, `real`, `room`, `routing`, `sdk`, `waiting`, `zoom`

## build-zoom-video-sdk-app

Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`
- **Tags**: `actual`, `app`, `build`, `build-zoom-video-sdk-app`, `control`, `custom`, `custom-session`, `experience`, `full`, `meeting`, `needs`, `over`, `partner`, `rather`, `routing`, `sdk`, `session`, `than`, `video`, `video-sdk`, `zoom`

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

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

## contact-center/android

Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`
- **Tags**: `android`, `callback`, `campaign`, `center`, `chat`, `contact`, `contact-center`, `handling`, `integrations`, `lifecycle`, `mode`, `native`, `partner`, `rejoin`, `scheduled`, `sdk`, `service`, `video`, `zoom`, `zva`

## contact-center/ios

Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`
- **Tags**: `app`, `bridging`, `callback`, `center`, `chat`, `contact`, `contact-center`, `flow`, `handling`, `integrations`, `ios`, `lifecycle`, `native`, `partner`, `rejoin`, `scheduled`, `sdk`, `video`, `zoom`, `zva`

## contact-center/web

Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`
- **Tags**: `app`, `app-context`, `campaign`, `center`, `chat`, `contact`, `contact-center`, `context`, `embed`, `embeds`, `engagement`, `event`, `handling`, `integrations`, `partner`, `postmessage`, `sdk`, `smart`, `video`, `web`, `zoom`

## cosmos-vulnerability-scanner

Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`
- **Tags**: `assessing`, `auditing`, `blockchain`, `building`, `building-secure-contracts`, `chain`, `consensus`, `consensus-critical`, `contracts`, `core`, `cosmos`, `cosmos-vulnerability-scanner`, `cosmwasm`, `critical`, `custom`, `divergence`, `evm`, `fund`, `halts`, `ibc`, `integrations`, `launch`, `loss`, `modules`, `pre`, `pre-launch`, `reviewing`, `scanner`, `scans`, `sdk`, `secure`, `security`, `state`, `updated`, `vulnerabilities`, `vulnerability`

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

## mcp-builder

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/mcp-builder`
- **Skill file**: `external/anthropic-skills/skills/mcp-builder/SKILL.md`
- **Tags**: `apis`, `builder`, `building`, `context`, `creating`, `designed`, `enable`, `fastmcp`, `high`, `high-quality`, `integrate`, `interact`, `llms`, `mcp`, `mcp-builder`, `model`, `node`, `protocol`, `python`, `quality`, `sdk`, `servers`, `services`, `typescript`, `well`, `well-designed`, `whether`

## meeting-sdk/linux

Zoom Meeting SDK for Linux - C++ headless meeting bots with raw audio/video access, transcription, recording, and AI integration for server-side automation

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux/SKILL.md`
- **Tags**: `access`, `audio`, `automation`, `bots`, `headless`, `integration`, `linux`, `meeting`, `meeting-sdk`, `partner`, `raw`, `recording`, `sdk`, `server`, `server-side`, `side`, `transcription`, `video`, `zoom`

## plan-zoom-product

Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`
- **Tags**: `api`, `apps`, `between`, `building`, `case`, `center`, `choose`, `clearly`, `contact`, `deciding`, `explain`, `goal`, `idea`, `integration`, `mcp`, `meeting`, `partner`, `phone`, `plan`, `plan-zoom-product`, `product`, `rest`, `right`, `sdk`, `surface`, `tradeoffs`, `video`, `webhooks`, `websockets`, `zoom`

## probe-sdk

Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video diagnostics, and network readiness before users join.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk/SKILL.md`
- **Tags**: `audio`, `browser`, `compatibility`, `diagnostics`, `join`, `media`, `network`, `partner`, `permissions`, `preflight`, `probe`, `probe-sdk`, `readiness`, `routing`, `sdk`, `testing`, `video`, `zoom`

## rivet-sdk

Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-module composition, or Lambda receiver patterns.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md`
- **Tags**: `api`, `auth`, `composition`, `consumers`, `handling`, `implementing`, `lambda`, `module`, `multi`, `multi-module`, `partner`, `receiver`, `rivet`, `rivet-sdk`, `routing`, `sdk`, `server`, `webhook`, `wrappers`, `zoom`

## ui-toolkit/web

Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Video SDK interface.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit/SKILL.md`
- **Tags**: `building`, `custom`, `fully`, `instead`, `interface`, `partner`, `prebuilt`, `react`, `routing`, `sdk`, `toolkit`, `ui-toolkit`, `video`, `want`, `web`, `zoom`

## video-sdk/linux

Zoom Video SDK for Linux - C++ headless bots, raw audio/video capture/injection, Qt/GTK integration, Docker support

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux/SKILL.md`
- **Tags**: `audio`, `bots`, `capture`, `docker`, `gtk`, `headless`, `injection`, `integration`, `linux`, `partner`, `raw`, `sdk`, `support`, `video`, `video-sdk`, `zoom`

## video-sdk/web

Zoom Video SDK for Web - JavaScript/TypeScript integration for browser-based video sessions, real-time communication, screen sharing, recording, and live transcription

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web/SKILL.md`
- **Tags**: `browser`, `communication`, `integration`, `javascript`, `live`, `partner`, `real`, `real-time`, `recording`, `screen`, `sdk`, `sessions`, `sharing`, `time`, `transcription`, `typescript`, `video`, `video-sdk`, `web`, `zoom`

## video-sdk/windows

Zoom Video SDK for Windows - C++ integration for video sessions, raw audio/video capture, screen sharing, recording, and real-time communication

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows/SKILL.md`
- **Tags**: `audio`, `capture`, `communication`, `integration`, `partner`, `raw`, `real`, `real-time`, `recording`, `screen`, `sdk`, `sessions`, `sharing`, `time`, `video`, `video-sdk`, `windows`, `zoom`

## virtual-agent/web

Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`
- **Tags**: `campaign`, `chat`, `context`, `controls`, `csp`, `csp-safe`, `deployment`, `driven`, `embeds`, `entry`, `event`, `event-driven`, `launch`, `partner`, `safe`, `sdk`, `updates`, `virtual`, `web`, `zoom`

## winui-app

Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/winui-app`
- **Skill file**: `external/openai-skills/skills/.curated/winui-app/SKILL.md`
- **Tags**: `accessibility`, `app`, `applications`, `bootstrap`, `brand`, `checking`, `communitytoolkit`, `components`, `controls`, `creating`, `curated`, `deployment`, `design`, `desktop`, `develop`, `development`, `environment`, `environment-checking`, `gallery`, `guidance`, `machine`, `microsoft`, `modern`, `navigation`, `performance`, `planning`, `preparing`, `refactoring`, `responsiveness`, `reviewing`, `samples`, `sdk`, `setting`, `theming`, `troubleshooting`, `windowing`, `windows`, `winui`, `winui-app`, `xaml`

## zoom-apps-sdk

Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`
- **Tags**: `app`, `apps`, `building`, `client`, `in-client`, `inside`, `main`, `meetings`, `partner`, `phone`, `routing`, `sdk`, `web`, `webinars`, `zoom`, `zoom-apps-sdk`

## zoom-cobrowse-sdk

Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy masking, remote assist, or PIN-based session sharing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md`
- **Tags**: `annotation`, `assist`, `browser`, `browsing`, `co-browsing`, `cobrowse`, `cobrowse-sdk`, `collaborative`, `collaborative-support`, `implementing`, `masking`, `partner`, `pin`, `privacy`, `remote`, `routing`, `sdk`, `session`, `sharing`, `support`, `zoom`, `zoom-cobrowse-sdk`

## zoom-meeting-sdk-android

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android/SKILL.md`
- **Tags**: `android`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `zoom`, `zoom-meeting-sdk-android`

## zoom-meeting-sdk-electron

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/electron`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/electron/SKILL.md`
- **Tags**: `electron`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `zoom`, `zoom-meeting-sdk-electron`

## zoom-meeting-sdk-ios

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios/SKILL.md`
- **Tags**: `ios`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `zoom`, `zoom-meeting-sdk-ios`

## zoom-meeting-sdk-macos

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/macos`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/macos/SKILL.md`
- **Tags**: `macos`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `zoom`, `zoom-meeting-sdk-macos`

## zoom-meeting-sdk-react-native

Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md`
- **Tags**: `android`, `apps`, `auth`, `bridge`, `embedding`, `flows`, `ios`, `join`, `jwt`, `meeting`, `meeting-sdk`, `meetings`, `meetingsdk`, `meetingsdk-react-native`, `native`, `partner`, `platform`, `react`, `react-native`, `sdk`, `start`, `troubleshooting`, `zoom`, `zoom-meeting-sdk-react-native`

## zoom-meeting-sdk-unreal

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/unreal`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/unreal/SKILL.md`
- **Tags**: `meeting`, `meeting-sdk`, `partner`, `sdk`, `unreal`, `zoom`, `zoom-meeting-sdk-unreal`

## zoom-meeting-sdk-web

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/SKILL.md`
- **Tags**: `meeting`, `meeting-sdk`, `partner`, `sdk`, `web`, `zoom`, `zoom-meeting-sdk-web`

## zoom-meeting-sdk-web-client-view

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view/SKILL.md`
- **Tags**: `client`, `client-view`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `view`, `web`, `zoom`, `zoom-meeting-sdk-web-client-view`

## zoom-meeting-sdk-web-component-view

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view/SKILL.md`
- **Tags**: `component`, `component-view`, `meeting`, `meeting-sdk`, `partner`, `sdk`, `view`, `web`, `zoom`, `zoom-meeting-sdk-web-component-view`

## zoom-meeting-sdk-windows

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/windows`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/windows/SKILL.md`
- **Tags**: `meeting`, `meeting-sdk`, `partner`, `sdk`, `windows`, `zoom`, `zoom-meeting-sdk-windows`

## zoom-video-sdk-android

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android/SKILL.md`
- **Tags**: `android`, `partner`, `sdk`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-android`

## zoom-video-sdk-flutter

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/flutter`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/flutter/SKILL.md`
- **Tags**: `flutter`, `partner`, `sdk`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-flutter`

## zoom-video-sdk-ios

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios/SKILL.md`
- **Tags**: `ios`, `partner`, `sdk`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-ios`

## zoom-video-sdk-macos

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/macos`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/macos/SKILL.md`
- **Tags**: `macos`, `partner`, `sdk`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-macos`

## zoom-video-sdk-react-native

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native/SKILL.md`
- **Tags**: `native`, `partner`, `react`, `react-native`, `sdk`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-react-native`

## zoom-video-sdk-unity

|

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/unity`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/unity/SKILL.md`
- **Tags**: `partner`, `sdk`, `unity`, `video`, `video-sdk`, `zoom`, `zoom-video-sdk-unity`
