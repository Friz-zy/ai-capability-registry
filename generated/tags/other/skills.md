# Tag: other

Skills with tag `other`:

## brand-review

Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when checking a draft before it ships, when auditing copy for voice consistency and terminology, or when screening for unsubstantiated claims, missing disclaimers, and other legal flags.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/marketing/skills/brand-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/marketing/skills/brand-review/SKILL.md`
- **Tags**: `against`, `auditing`, `brand`, `brand-review`, `checking`, `claims`, `consistency`, `content`, `copy`, `deviations`, `disclaimers`, `draft`, `fixes`, `flagging`, `flags`, `legal`, `marketing`, `messaging`, `missing`, `other`, `pillars`, `review`, `screening`, `severity`, `ships`, `style`, `terminology`, `unsubstantiated`, `voice`

## canvas-design

Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/canvas-design`
- **Skill file**: `external/anthropic-skills/skills/canvas-design/SKILL.md`
- **Tags**: `art`, `artists`, `asks`, `avoid`, `beautiful`, `canvas`, `canvas-design`, `copying`, `copyright`, `create`, `design`, `designs`, `documents`, `existing`, `never`, `original`, `other`, `pdf`, `philosophy`, `piece`, `png`, `poster`, `static`, `violations`, `visual`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## let-fate-decide

Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide`
- **Skill file**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`
- **Tags**: `ambiguous`, `approaches`, `arbitrarily`, `ask`, `ask-questions-if-underspecified`, `between`, `cards`, `casual`, `casually`, `decide`, `delegated`, `draws`, `entropy`, `fate`, `idk`, `inject`, `interprets`, `let`, `let-fate-decide`, `makes`, `multiple`, `next`, `nonchalant`, `other`, `over`, `phrases`, `pick`, `planning`, `playful`, `precision`, `precision-seeking`, `prefer`, `prompts`, `questions`, `rather`, `reasonable`, `says`, `seeking`, `spread`, `tarot`, `than`, `tone`, `underspecified`, `vague`, `whatever`, `yolo`, `yu-gi-oh`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`

## zeroize-audit

Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit`
- **Skill file**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
- **Tags**: `analysis`, `assembly`, `assembly-level`, `audit`, `auditing`, `code`, `compiler`, `control`, `control-flow`, `data`, `detects`, `flow`, `handling`, `identifies`, `keys`, `level`, `missing`, `optimizations`, `other`, `passwords`, `removed`, `rust`, `secrets`, `sensitive`, `verification`, `zeroization`, `zeroize`, `zeroize-audit`
