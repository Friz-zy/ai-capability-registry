# Tag: tokens

Skills with tag `tokens`:

## design-handoff

Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/design-handoff/SKILL.md`
- **Tags**: `animation`, `breakpoints`, `cases`, `component`, `covering`, `design`, `design-handoff`, `developer`, `edge`, `engineering`, `handoff`, `interaction`, `layout`, `needs`, `props`, `ready`, `responsive`, `sheet`, `spec`, `specs`, `states`, `tokens`

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## session-report

Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`
- **Tags**: `cache`, `code`, `expensive`, `explorable`, `html`, `projects`, `prompts`, `report`, `session`, `session-report`, `subagents`, `tokens`, `transcripts`

## token-integration-analyzer

Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`
- **Tags**: `analysis`, `analyzer`, `analyzes`, `assesses`, `aware`, `both`, `building`, `building-secure-contracts`, `chain`, `checklist`, `checks`, `composition`, `conformity`, `context`, `context-aware`, `contract`, `contracts`, `erc20`, `erc721`, `evaluates`, `handle`, `implementation`, `implementations`, `integration`, `integrations`, `non`, `non-standard`, `on-chain`, `owner`, `performs`, `privileges`, `protocols`, `scarcity`, `secure`, `standard`, `token`, `token-integration-analyzer`, `tokens`, `weird`
