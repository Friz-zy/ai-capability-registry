# Tag: directly

Skills with tag `directly`:

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

## skill-improver

Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver`
- **Skill file**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`
- **Tags**: `automated`, `code`, `cycles`, `descriptions`, `directly`, `fix`, `fix-review`, `fixes`, `improve`, `improvement`, `improver`, `issues`, `iteratively`, `loop`, `loops`, `meet`, `one`, `one-time`, `quality`, `refine`, `review`, `reviewer`, `reviews`, `runs`, `standards`, `they`, `time`, `triggers`, `until`
