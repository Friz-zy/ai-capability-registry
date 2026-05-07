# Tag: auto

Skills with tag `auto`:

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

## plugin-structure

This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`
- **Tags**: `architecture`, `asks`, `auto`, `auto-discovery`, `code`, `commands`, `component`, `components`, `configuration`, `configure`, `conventions`, `create`, `dev`, `directory`, `discovery`, `guidance`, `hooks`, `layout`, `manifest`, `naming`, `needs`, `organization`, `organize`, `practices`, `root`, `scaffold`, `set`, `structure`, `understand`, `used`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`
