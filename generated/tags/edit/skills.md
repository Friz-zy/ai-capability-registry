# Tag: edit

Skills with tag `edit`:

## access

Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Discord channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/discord/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `discord`, `edit`, `group`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `who`

## access

Manage iMessage channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the iMessage channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/imessage/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `edit`, `group`, `imessage`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `who`

## access

Manage Telegram channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or change policy for the Telegram channel.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/access`
- **Skill file**: `external/anthropic-claude-plugins-official/external_plugins/telegram/skills/access/SKILL.md`
- **Tags**: `access`, `allowed`, `allowlists`, `approve`, `asks`, `change`, `channel`, `edit`, `group`, `manage`, `pair`, `pairings`, `policy`, `set`, `someone`, `telegram`, `who`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

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

## jupyter-notebook

Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/jupyter-notebook`
- **Skill file**: `external/openai-skills/skills/.curated/jupyter-notebook/SKILL.md`
- **Tags**: `asks`, `bundled`, `clean`, `create`, `curated`, `edit`, `experiments`, `explorations`, `helper`, `ipynb`, `jupyter`, `jupyter-notebook`, `notebook`, `notebooks`, `prefer`, `scaffold`, `script`, `starting`, `tutorials`

## openai-jupyter-notebook

Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-jupyter-notebook/skills/openai-jupyter-notebook/SKILL.md`
- **Tags**: `asks`, `create`, `edit`, `experiments`, `ipynb`, `jupyter`, `jupyter-notebook`, `notebook`, `notebooks`, `scaffold`

## plugin-creator

Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/plugin-creator`
- **Skill file**: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`
- **Tags**: `availability`, `baseline`, `can`, `codex`, `create`, `creator`, `directories`, `edit`, `entries`, `folders`, `local`, `marketplace`, `metadata`, `needs`, `optional`, `ordering`, `placeholders`, `publishing`, `repo`, `repo-root`, `root`, `scaffold`, `structure`, `testing`

## skill-creator

Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/skill-creator`
- **Skill file**: `external/anthropic-skills/skills/skill-creator/SKILL.md`
- **Tags**: `accuracy`, `analysis`, `benchmark`, `better`, `create`, `creator`, `description`, `edit`, `evals`, `existing`, `improve`, `measure`, `modify`, `optimize`, `performance`, `scratch`, `test`, `triggering`, `variance`, `want`

## skill-creator

Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/skill-creator/skills/skill-creator`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/skill-creator/skills/skill-creator/SKILL.md`
- **Tags**: `accuracy`, `analysis`, `benchmark`, `better`, `create`, `creator`, `description`, `edit`, `evals`, `existing`, `improve`, `measure`, `modify`, `optimize`, `performance`, `scratch`, `test`, `triggering`, `variance`, `want`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`
