# Tag: filename

Skills with tag `filename`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## figma-create-new-file

Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handles plan resolution via whoami if needed. Usage — /figma-create-new-file [editorType] [fileName] (e.g. /figma-create-new-file figjam My Whiteboard)

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-new-file`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-new-file/SKILL.md`
- **Tags**: `blank`, `calling`, `create`, `curated`, `design`, `editortype`, `figjam`, `figma`, `figma-create`, `filename`, `handles`, `needed`, `plan`, `resolution`, `whiteboard`, `whoami`

## pptx

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pptx`
- **Skill file**: `external/anthropic-skills/skills/pptx/SKILL.md`
- **Tags**: `afterward`, `both`, `combining`, `comments`, `content`, `created`, `creating`, `deck`, `decks`, `editing`, `elsewhere`, `email`, `even`, `existing`, `extracted`, `extracting`, `filename`, `includes`, `input`, `involved`, `layouts`, `like`, `mentions`, `modifying`, `needs`, `notes`, `opened`, `parsing`, `pitch`, `plan`, `pptx`, `presentation`, `presentations`, `reading`, `regardless`, `slide`, `slides`, `speaker`, `splitting`, `summary`, `text`, `they`, `time`, `touched`, `trigger`, `updating`, `used`, `way`, `whenever`, `will`, `working`
