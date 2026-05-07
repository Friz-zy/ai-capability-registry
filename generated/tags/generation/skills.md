# Tag: generation

Skills with tag `generation`:

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## guideline-generation

>

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/guideline-generation`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/brand-voice/skills/guideline-generation/SKILL.md`
- **Tags**: `brand`, `brand-voice`, `generation`, `guideline`, `guideline-generation`, `partner`, `voice`

## hatch-pet

Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/hatch-pet`
- **Skill file**: `external/openai-skills/skills/.curated/hatch-pet/SKILL.md`
- **Tags**: `8x9`, `animated`, `animation`, `art`, `assembly`, `asset`, `atlas`, `build`, `bundled`, `cells`, `character`, `codex`, `codex-compatible`, `compatible`, `composes`, `contact`, `create`, `curated`, `custom`, `deterministic`, `generation`, `hatch`, `hatch-pet`, `imagegen`, `images`, `installed`, `package`, `packaging`, `pet`, `pets`, `preview`, `prompts`, `repair`, `row`, `row-by-row`, `screenshots`, `sheets`, `spritesheet`, `spritesheets`, `transparent`, `unused`, `validate`, `videos`, `visual`

## pdf

Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/pdf`
- **Skill file**: `external/openai-skills/skills/.curated/pdf/SKILL.md`
- **Tags**: `checks`, `creating`, `curated`, `extraction`, `generation`, `involve`, `layout`, `matter`, `pages`, `pdf`, `pdfplumber`, `poppler`, `prefer`, `pypdf`, `python`, `reading`, `rendering`, `reportlab`, `reviewing`, `such`, `visual`, `where`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
