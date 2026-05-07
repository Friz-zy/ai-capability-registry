# Tag: memory

Skills with tag `memory`:

## c-review

Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/c-review/skills/c-review`
- **Skill file**: `external/trailofbits-skills/plugins/c-review/skills/c-review/SKILL.md`
- **Tags**: `applications`, `auditing`, `c-review`, `code`, `comprehensive`, `conditions`, `corruption`, `daemons`, `free`, `hunting`, `integer`, `memory`, `native`, `overflow`, `overflows`, `performs`, `platform`, `race`, `review`, `reviewing`, `safety`, `security`, `services`, `userspace`, `vulnerabilities`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## claude-md-improver

Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`
- **Tags**: `against`, `asks`, `audit`, `evaluates`, `fix`, `improve`, `improver`, `maintenance`, `makes`, `management`, `md-improver`, `md-management`, `memory`, `mentions`, `optimization`, `outputs`, `project`, `quality`, `report`, `repositories`, `scans`, `targeted`, `then`, `updates`

## memory-management

Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/memory-management/SKILL.md`
- **Tags**: `acronyms`, `base`, `collaborator`, `colleague`, `decodes`, `directory`, `full`, `internal`, `knowledge`, `language`, `like`, `makes`, `management`, `memory`, `memory-management`, `nicknames`, `productivity`, `requests`, `shorthand`, `tier`, `true`, `two`, `two-tier`, `understands`, `working`, `workplace`, `would`

## start

Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing task list, or decoding the shorthand (nicknames, acronyms, project codenames) you use in your todos.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/start`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/start/SKILL.md`
- **Tags**: `acronyms`, `bootstrapping`, `codenames`, `dashboard`, `decoding`, `existing`, `initialize`, `memory`, `nicknames`, `open`, `productivity`, `project`, `setting`, `shorthand`, `start`, `time`, `todos`, `working`

## update

Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue tasks, filling memory gaps for unknown people or projects, or running a comprehensive scan to catch todos buried in chat and email.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/productivity/skills/update`
- **Skill file**: `external/anthropic-knowledge-work-plugins/productivity/skills/update/SKILL.md`
- **Tags**: `activity`, `assignments`, `buried`, `catch`, `chat`, `comprehensive`, `email`, `filling`, `gaps`, `memory`, `overdue`, `people`, `productivity`, `project`, `projects`, `pulling`, `refresh`, `running`, `scan`, `stale`, `sync`, `todos`, `tracker`, `triaging`, `unknown`
