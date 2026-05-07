# Tag: general

Skills with tag `general`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-best-practices`
- **Skill file**: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`
- **Tags**: `code`, `coding`, `curated`, `debugging`, `default`, `explicitly`, `framework`, `general`, `guidance`, `improvements`, `javascript`, `language`, `languages`, `non`, `non-security`, `perform`, `practice`, `practices`, `python`, `report`, `requests`, `review`, `reviews`, `secure`, `secure-by-default`, `security`, `security-practices`, `suggest`, `supported`, `trigger`, `typescript`

## security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-ownership-map`
- **Skill file**: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
- **Tags**: `analysis`, `analyze`, `build`, `bus`, `bus-factor`, `checks`, `clusters`, `code`, `codeowners`, `compute`, `csv`, `curated`, `databases`, `explicitly`, `export`, `factor`, `general`, `git`, `graph`, `grounded`, `history`, `hotspots`, `lists`, `maintainer`, `maintainers`, `map`, `non`, `non-security`, `oriented`, `orphaned`, `ownership`, `people`, `people-to`, `questions`, `reality`, `repositories`, `risk`, `security`, `security-oriented`, `security-ownership-map`, `sensitive`, `sensitive-code`, `topology`, `trigger`, `visualization`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## zoom-general

Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scopes, marketplace considerations, or API-vs-MCP routing.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/general/SKILL.md`
- **Tags**: `api`, `api-vs-mcp`, `app`, `app-model`, `authentication`, `clear`, `comparisons`, `considerations`, `context`, `cross`, `cross-product`, `general`, `guidance`, `marketplace`, `mcp`, `model`, `partner`, `platform`, `product`, `routing`, `scopes`, `shared`, `zoom`, `zoom-general`
