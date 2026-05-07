# sdk

## Skills
Load skill and **use it** when task matches.

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### build-zoom-bot
Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combining Meeting SDK, RTMS, and backend services.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md`

### build-zoom-meeting-app
Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`

### build-zoom-meeting-sdk-app
Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md`

### build-zoom-video-sdk-app
Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`

### chatgpt-apps
Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

File: `../external/openai-skills/skills/.curated/chatgpt-apps/SKILL.md`

### choose-zoom-approach
Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`

### claude-api
Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

File: `../external/anthropic-skills/skills/claude-api/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `../external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### contact-center/android
Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### debug-zoom
Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`

### debug-zoom-integration
Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate the layer before proposing a fix.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `../external/anthropic-skills/skills/mcp-builder/SKILL.md`

### meeting-sdk/linux
Zoom Meeting SDK for Linux - C++ headless meeting bots with raw audio/video access, transcription, recording, and AI integration for server-side automation

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/linux/SKILL.md`

### plan-zoom-product
Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`

### probe-sdk
Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video diagnostics, and network readiness before users join.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/probe-sdk/SKILL.md`

### rivet-sdk
Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-module composition, or Lambda receiver patterns.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md`

### ui-toolkit/web
Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Video SDK interface.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/ui-toolkit/SKILL.md`

### video-sdk/linux
Zoom Video SDK for Linux - C++ headless bots, raw audio/video capture/injection, Qt/GTK integration, Docker support

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/linux/SKILL.md`

### video-sdk/web
Zoom Video SDK for Web - JavaScript/TypeScript integration for browser-based video sessions, real-time communication, screen sharing, recording, and live transcription

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web/SKILL.md`

### video-sdk/windows
Zoom Video SDK for Windows - C++ integration for video sessions, raw audio/video capture, screen sharing, recording, and real-time communication

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows/SKILL.md`

### virtual-agent/web
Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`

### winui-app
Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

File: `../external/openai-skills/skills/.curated/winui-app/SKILL.md`

### zoom-apps-sdk
Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`

### zoom-cobrowse-sdk
Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy masking, remote assist, or PIN-based session sharing.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md`

### zoom-meeting-sdk-android
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/android/SKILL.md`

### zoom-meeting-sdk-electron
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/electron/SKILL.md`

### zoom-meeting-sdk-ios
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/ios/SKILL.md`

### zoom-meeting-sdk-macos
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/macos/SKILL.md`

### zoom-meeting-sdk-react-native
Zoom Meeting SDK for React Native. Use when embedding Zoom meetings in React Native iOS/Android apps with @zoom/meetingsdk-react-native, JWT auth, join/start flows, platform setup, and native bridge troubleshooting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/react-native/SKILL.md`

### zoom-meeting-sdk-unreal
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/unreal/SKILL.md`

### zoom-meeting-sdk-web
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/SKILL.md`

### zoom-meeting-sdk-web-client-view
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/client-view/SKILL.md`

### zoom-meeting-sdk-web-component-view
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/web/component-view/SKILL.md`

### zoom-meeting-sdk-windows
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/windows/SKILL.md`

### zoom-video-sdk-android
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/android/SKILL.md`

### zoom-video-sdk-flutter
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/flutter/SKILL.md`

### zoom-video-sdk-ios
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/ios/SKILL.md`

### zoom-video-sdk-macos
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/macos/SKILL.md`

### zoom-video-sdk-react-native
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/react-native/SKILL.md`

### zoom-video-sdk-unity
|

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/unity/SKILL.md`
