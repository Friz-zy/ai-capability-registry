# Tag: layout

Skills with tag `layout`:

## design-handoff

Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff/SKILL.md`
- **Tags**: `animation`, `breakpoints`, `cases`, `component`, `covering`, `design`, `design-handoff`, `developer`, `edge`, `engineering`, `handoff`, `interaction`, `layout`, `needs`, `props`, `ready`, `responsive`, `sheet`, `spec`, `specs`, `states`, `tokens`

## example-command

An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-command`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-command/SKILL.md`
- **Tags**: `command`, `demonstrates`, `frontmatter`, `invoked`, `layout`, `options`

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## openai-pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-pdf/skills/openai-pdf/SKILL.md`
- **Tags**: `creating`, `involve`, `layout`, `pdf`, `reading`, `rendering`, `reviewing`, `where`

## pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/pdf`
- **Skill file**: `external/openai-skills/skills/.curated/pdf/SKILL.md`
- **Tags**: `checks`, `creating`, `curated`, `extraction`, `generation`, `involve`, `layout`, `matter`, `pages`, `pdf`, `pdfplumber`, `poppler`, `prefer`, `pypdf`, `python`, `reading`, `rendering`, `reportlab`, `reviewing`, `such`, `visual`, `where`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`
