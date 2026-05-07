# app

## Skills
Load skill and **use it** when task matches.

### build-mcp-app
This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### build-zoom-contact-center-app
Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context and state handling; campaigns; callbacks; or version-drift troubleshooting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/SKILL.md`

### build-zoom-meeting-app
Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Meeting SDK and Video SDK.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md`

### build-zoom-meeting-sdk-app
Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, auth and join flows, waiting room issues, or meeting bot patterns.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md`

### build-zoom-rest-api-app
Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`

### build-zoom-video-sdk-app
Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`

### cardputer-buddy
Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

File: `../external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `../external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

File: `../external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

### m5-onboard
End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

File: `../external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/m5-onboard/SKILL.md`

### screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

File: `../external/openai-skills/skills/.curated/screenshot/SKILL.md`

### setup-zoom-oauth
Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`

### start
Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

File: `../external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`

### winui-app
Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

File: `../external/openai-skills/skills/.curated/winui-app/SKILL.md`

### zoom-apps-sdk
Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main client, or Zoom Phone.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md`

### zoom-general
Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`

### zoom-oauth
Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`
