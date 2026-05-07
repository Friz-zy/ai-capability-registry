# Tag: components

Skills with tag `components`:

## build-mcp-app

This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`
- **Tags**: `already`, `app`, `apps`, `build`, `build-mcp-app`, `build-mcp-server`, `chat`, `components`, `confirmation`, `context`, `conversation`, `dashboard`, `deployment`, `dev`, `dialog`, `form`, `has`, `inline`, `interactive`, `knows`, `make`, `mcp`, `mcp-server-dev`, `mentions`, `model`, `picker`, `render`, `sdk`, `server`, `settled`, `shows`, `they`, `used`, `want`, `widgets`

## design-system

Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/design-system`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/design-system/SKILL.md`
- **Tags**: `accessibility`, `audit`, `checking`, `component`, `components`, `design`, `designing`, `document`, `documentation`, `existing`, `extend`, `fits`, `hardcoded`, `inconsistencies`, `naming`, `notes`, `states`, `values`, `variants`

## figma-code-connect-components

Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map this component", "link component to code", "create code connect mapping", or wants to establish mappings between Figma designs and code implementations. For canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-code-connect-components`
- **Skill file**: `external/openai-skills/skills/.curated/figma-code-connect-components/SKILL.md`
- **Tags**: `between`, `canvas`, `code`, `component`, `components`, `connect`, `connects`, `create`, `curated`, `design`, `designs`, `establish`, `figma`, `figma-code-connect-components`, `implementations`, `link`, `map`, `mapping`, `mappings`, `says`, `writes`

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## figma-implement-design

Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-implement-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`
- **Tags**: `application`, `asks`, `build`, `canvas`, `code`, `component`, `components`, `curated`, `design`, `designs`, `fidelity`, `figma`, `figma-implement-design`, `implement`, `implementing`, `matching`, `mentions`, `production`, `production-ready`, `provides`, `ready`, `specs`, `translates`, `urls`, `visual`, `writes`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/frontend-design`
- **Skill file**: `external/anthropic-skills/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `artifacts`, `asks`, `avoids`, `beautifying`, `build`, `code`, `components`, `create`, `creative`, `css`, `dashboards`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `html`, `include`, `interfaces`, `landing`, `layouts`, `pages`, `polished`, `posters`, `production`, `production-grade`, `quality`, `react`, `styling`, `web`, `websites`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `asks`, `avoids`, `build`, `code`, `components`, `create`, `creative`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `interfaces`, `pages`, `polished`, `production`, `production-grade`, `quality`, `web`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## web-artifacts-builder

Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/web-artifacts-builder`
- **Skill file**: `external/anthropic-skills/skills/web-artifacts-builder/SKILL.md`
- **Tags**: `artifacts`, `builder`, `complex`, `component`, `components`, `creating`, `css`, `elaborate`, `frontend`, `html`, `jsx`, `management`, `modern`, `multi`, `multi-component`, `react`, `requiring`, `routing`, `shadcn`, `simple`, `single`, `state`, `suite`, `tailwind`, `technologies`, `web`, `web-artifacts-builder`

## winui-app

Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Windows App SDK samples, and CommunityToolkit components. Use when creating a brand new app, preparing a machine for WinUI, reviewing, refactoring, planning, troubleshooting, environment-checking, or setting up WinUI 3 XAML, controls, navigation, windowing, theming, accessibility, responsiveness, performance, deployment, or related Windows app design and development work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/winui-app`
- **Skill file**: `external/openai-skills/skills/.curated/winui-app/SKILL.md`
- **Tags**: `accessibility`, `app`, `applications`, `bootstrap`, `brand`, `checking`, `communitytoolkit`, `components`, `controls`, `creating`, `curated`, `deployment`, `design`, `desktop`, `develop`, `development`, `environment`, `environment-checking`, `gallery`, `guidance`, `machine`, `microsoft`, `modern`, `navigation`, `performance`, `planning`, `preparing`, `refactoring`, `responsiveness`, `reviewing`, `samples`, `sdk`, `setting`, `theming`, `troubleshooting`, `windowing`, `windows`, `winui`, `winui-app`, `xaml`
