# Tag: like

Skills with tag `like`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## data-visualization

Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/data-visualization`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`
- **Tags**: `accessibility`, `applying`, `building`, `chart`, `charts`, `choosing`, `color`, `create`, `creating`, `data`, `data-visualization`, `dataset`, `design`, `effective`, `figures`, `like`, `matplotlib`, `plotly`, `principles`, `publication`, `publication-quality`, `python`, `quality`, `right`, `seaborn`, `theory`, `visualization`, `visualizations`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## draft-response

Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response`
- **Skill file**: `external/anthropic-knowledge-work-plugins/customer-support/skills/draft-response/SKILL.md`
- **Tags**: `answering`, `bad`, `billing`, `customer`, `customer-facing`, `customer-support`, `declining`, `delay`, `delivering`, `draft`, `draft-response`, `escalation`, `facing`, `feature`, `fix`, `issue`, `like`, `news`, `outage`, `product`, `professional`, `question`, `relationship`, `replying`, `request`, `responding`, `response`, `situation`, `support`, `t-fix`, `tailored`, `won`

## explore-data

Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/explore-data`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`
- **Tags**: `analyze`, `checking`, `column`, `data`, `dataset`, `deciding`, `dimensions`, `distributions`, `duplicates`, `encountering`, `explore`, `explore-data`, `issues`, `its`, `like`, `metrics`, `null`, `profile`, `quality`, `rates`, `shape`, `spotting`, `suspicious`, `understand`, `values`, `which`

## memory-management

Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management/SKILL.md`
- **Tags**: `acronyms`, `base`, `collaborator`, `colleague`, `decodes`, `directory`, `full`, `internal`, `knowledge`, `language`, `like`, `makes`, `management`, `memory`, `memory-management`, `nicknames`, `productivity`, `requests`, `shorthand`, `tier`, `true`, `two`, `two-tier`, `understands`, `working`, `workplace`, `would`

## pipeline-review

Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on this week, spotting stale or stuck opportunities, auditing for hygiene issues like bad close dates, or identifying single-threaded deals.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review/SKILL.md`
- **Tags**: `analyze`, `auditing`, `bad`, `close`, `dates`, `deals`, `deciding`, `flag`, `focus`, `health`, `hygiene`, `identifying`, `issues`, `like`, `opportunities`, `pipeline`, `pipeline-review`, `plan`, `prioritize`, `review`, `risks`, `running`, `sales`, `single`, `single-threaded`, `spotting`, `stale`, `stuck`, `threaded`, `week`, `weekly`, `which`

## pptx

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pptx`
- **Skill file**: `external/anthropic-skills/skills/pptx/SKILL.md`
- **Tags**: `afterward`, `both`, `combining`, `comments`, `content`, `created`, `creating`, `deck`, `decks`, `editing`, `elsewhere`, `email`, `even`, `existing`, `extracted`, `extracting`, `filename`, `includes`, `input`, `involved`, `layouts`, `like`, `mentions`, `modifying`, `needs`, `notes`, `opened`, `parsing`, `pitch`, `plan`, `pptx`, `presentation`, `presentations`, `reading`, `regardless`, `slide`, `slides`, `speaker`, `splitting`, `summary`, `text`, `they`, `time`, `touched`, `trigger`, `updating`, `used`, `way`, `whenever`, `will`, `working`

## slack-gif-creator

Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/slack-gif-creator`
- **Skill file**: `external/anthropic-skills/skills/slack-gif-creator/SKILL.md`
- **Tags**: `animated`, `animation`, `concepts`, `constraints`, `creating`, `creator`, `doing`, `gif`, `gifs`, `knowledge`, `like`, `make`, `optimized`, `provides`, `request`, `slack`, `slack-gif-creator`, `utilities`, `validation`

## vercel-deploy

Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/vercel-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`
- **Tags**: `actions`, `app`, `applications`, `create`, `curated`, `deploy`, `deployment`, `give`, `like`, `link`, `live`, `preview`, `push`, `requests`, `vercel`, `vercel-deploy`, `websites`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`
