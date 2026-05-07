# Tag: variants

Skills with tag `variants`:

## design-system

Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/design-system`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/design-system/SKILL.md`
- **Tags**: `accessibility`, `audit`, `checking`, `component`, `components`, `design`, `designing`, `document`, `documentation`, `existing`, `extend`, `fits`, `hardcoded`, `inconsistencies`, `naming`, `notes`, `states`, `values`, `variants`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## imagegen

Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/imagegen`
- **Skill file**: `external/openai-skills/skills/.system/imagegen/SKILL.md`
- **Tags**: `ai-created`, `asset`, `assets`, `background`, `benefits`, `better`, `bitmap`, `brand`, `building`, `canvas`, `code`, `code-native`, `codex`, `create`, `created`, `css`, `cutouts`, `derive`, `directly`, `edit`, `editing`, `established`, `existing`, `extending`, `handled`, `html`, `icon`, `illustrations`, `image`, `imagegen`, `images`, `logo`, `mockups`, `native`, `photos`, `raster`, `rather`, `repo`, `repo-native`, `sprites`, `such`, `svg`, `textures`, `than`, `transform`, `transparent`, `transparent-background`, `variants`, `vector`, `visual`, `visuals`

## semgrep-rule-variant-creator

Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator`
- **Skill file**: `external/trailofbits-skills/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`
- **Tags**: `creates`, `creator`, `directories`, `existing`, `independent`, `input`, `language`, `languages`, `porting`, `produces`, `rule`, `semgrep`, `semgrep-rule-variant-creator`, `specified`, `takes`, `target`, `test`, `variant`, `variants`

## variant-analysis

Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `audits`, `bug`, `bugs`, `building`, `code`, `codebases`, `codeql`, `find`, `finding`, `hunting`, `initial`, `issue`, `performing`, `queries`, `security`, `semgrep`, `similar`, `systematic`, `variant`, `variant-analysis`, `variants`, `vulnerabilities`
