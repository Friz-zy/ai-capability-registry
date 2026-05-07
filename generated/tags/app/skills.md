# Tag: app

Skills with tag `app`:

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

## build-zoom-contact-center-app

Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context and state handling; campaigns; callbacks; or version-drift troubleshooting.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/SKILL.md`
- **Tags**: `app`, `build`, `build-zoom-contact-center-app`, `callbacks`, `campaigns`, `center`, `contact`, `contact-center`, `context`, `drift`, `engagement`, `handling`, `implementing`, `integrations`, `native`, `partner`, `routing`, `state`, `troubleshooting`, `version`, `version-drift`, `web`, `zoom`

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

## build-zoom-rest-api-app

Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements, rate-limit awareness, or API error debugging.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rest-api/SKILL.md`
- **Tags**: `api`, `app`, `awareness`, `build`, `build-zoom-rest-api-app`, `choosing`, `debugging`, `endpoint`, `error`, `limit`, `management`, `oauth`, `partner`, `rate`, `rate-limit`, `requirements`, `resource`, `resource-management`, `rest`, `rest-api`, `selection`, `zoom`

## build-zoom-team-chat-app

Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`
- **Tags**: `app`, `build`, `build-zoom-team-chat-app`, `building`, `buttons`, `cards`, `chat`, `chatbot`, `commands`, `experiences`, `integrations`, `messaging`, `partner`, `rich`, `routing`, `scoped`, `slash`, `team`, `team-chat`, `webhooks`, `zoom`

## build-zoom-video-sdk-app

Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`
- **Tags**: `actual`, `app`, `build`, `build-zoom-video-sdk-app`, `control`, `custom`, `custom-session`, `experience`, `full`, `meeting`, `needs`, `over`, `partner`, `rather`, `routing`, `sdk`, `session`, `than`, `video`, `video-sdk`, `zoom`

## cardputer-buddy

Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`
- **Tags**: `adv`, `already`, `app`, `buddy`, `bundle`, `cardputer`, `cardputer-adv`, `cardputer-buddy`, `changed`, `command`, `cwc`, `cwc-makers`, `device`, `flashing`, `follow`, `follow-up`, `hello`, `iterate`, `logs`, `m5-onboard`, `maker`, `makers`, `micropython`, `onboard`, `one`, `one-shot`, `provisioned`, `push`, `re-flashing`, `repl`, `serial`, `shot`, `single`, `snake`, `tail`, `trigger`, `watch`, `without`

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

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

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## firebase-apk-scanner

Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner`
- **Skill file**: `external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`
- **Tags**: `analyzing`, `android`, `apk`, `apks`, `app`, `audits`, `authentication`, `authorized`, `buckets`, `cloud`, `databases`, `endpoint`, `exposed`, `firebase`, `firebase-apk-scanner`, `functions`, `including`, `issues`, `misconfigurations`, `mobile`, `open`, `performing`, `research`, `scanner`, `scans`, `security`, `storage`, `testing`, `vulnerabilities`

## m5-onboard

End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/m5-onboard`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/m5-onboard/SKILL.md`
- **Tags**: `adv`, `app`, `board`, `buddy`, `bundle`, `cardputer`, `cardputer-adv`, `core`, `cores3`, `cwc`, `cwc-makers`, `detect`, `device`, `end`, `end-to-end`, `esp32`, `firmware`, `flash`, `freshly`, `freshly-plugged-in`, `install`, `m5-onboard`, `m5stack`, `makers`, `micropython`, `onboard`, `onboarding`, `plugged`, `plugs`, `provision`, `reset`, `says`, `stick`, `uiflow`, `usb`, `whenever`

## screenshot

Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/screenshot`
- **Skill file**: `external/openai-skills/skills/.curated/screenshot/SKILL.md`
- **Tags**: `app`, `asks`, `capabilities`, `capture`, `curated`, `desktop`, `explicitly`, `full`, `level`, `needed`, `os-level`, `pixel`, `region`, `screen`, `screenshot`, `unavailable`, `window`

## setup-zoom-oauth

Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`
- **Tags**: `app`, `auth`, `authentication`, `choosing`, `correctly`, `credentials`, `debugging`, `failures`, `grant`, `handling`, `implement`, `oauth`, `partner`, `refresh`, `requesting`, `scopes`, `setting`, `token`, `zoom`, `zoom-oauth`

## start

Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`
- **Tags**: `app`, `architecture`, `choose`, `correct`, `doc`, `here`, `idea`, `implementation`, `integration`, `partner`, `reading`, `right`, `route`, `set`, `shape`, `start`, `surface`, `whole`, `without`, `zoom`

## vercel-deploy

Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/vercel-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`
- **Tags**: `actions`, `app`, `applications`, `create`, `curated`, `deploy`, `deployment`, `give`, `like`, `link`, `live`, `preview`, `push`, `requests`, `vercel`, `vercel-deploy`, `websites`

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

## zoom-general

Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`
- **Tags**: `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`, `clear`, `comparisons`, `considerations`, `context`, `cross`, `cross-product`, `general`, `guidance`, `marketplace`, `mcp`, `model`, `partner`, `platform`, `product`, `routing`, `scopes`, `shared`, `zoom`, `zoom-general`

## zoom-oauth

Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`
- **Tags**: `app`, `auth`, `authentication`, `behavior`, `choosing`, `credentials`, `debugging`, `failures`, `grant`, `oauth`, `partner`, `refresh`, `routing`, `scopes`, `token`, `types`, `zoom`, `zoom-oauth`
