# Tag: questions

Skills with tag `questions`:

## analyze

Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segments over time, or preparing a formal data report for stakeholders.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/analyze`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/analyze/SKILL.md`
- **Tags**: `analyses`, `analyze`, `answer`, `comparing`, `data`, `driving`, `drop`, `formal`, `full`, `investigating`, `looking`, `lookups`, `metric`, `over`, `preparing`, `questions`, `report`, `segments`, `single`, `stakeholders`, `time`, `trend`

## ask-questions-if-underspecified

Clarify requirements before implementing. Use when serious doubts arise.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified`
- **Skill file**: `external/trailofbits-skills/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified/SKILL.md`
- **Tags**: `arise`, `ask`, `ask-questions-if-underspecified`, `clarify`, `doubts`, `implementing`, `questions`, `requirements`, `serious`, `underspecified`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## constant-time-analysis

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`
- **Tags**: `analysis`, `branches`, `channel`, `code`, `constant`, `constant-time`, `constant-time-analysis`, `crypto`, `cryptographic`, `dependent`, `detects`, `division`, `encountering`, `implementing`, `java`, `javascript`, `kotlin`, `php`, `programming`, `python`, `questions`, `reviewing`, `ruby`, `rust`, `secret`, `secret-dependent`, `secrets`, `side`, `side-channel`, `swift`, `time`, `timing`, `typescript`, `vulnerabilities`

## dwarf-expert

Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert`
- **Skill file**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`
- **Tags**: `analyzing`, `answering`, `code`, `data`, `debug`, `dwarf`, `dwarf-expert`, `expert`, `expertise`, `format`, `information`, `interacting`, `parses`, `provides`, `questions`, `standard`, `triggers`, `understanding`, `v3-v5`, `working`

## interview-prep

Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we interview", "scorecard for", or when the user is preparing to interview candidates.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep/SKILL.md`
- **Tags**: `candidates`, `competency`, `create`, `human`, `interview`, `interview-prep`, `plan`, `plans`, `prep`, `preparing`, `questions`, `scorecard`, `scorecards`, `structured`, `trigger`

## legal-response

Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. Use when responding to data subject requests, litigation hold notices, vendor legal questions, NDA requests from business teams, or subpoenas.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/legal-response/SKILL.md`
- **Tags**: `business`, `checks`, `configured`, `data`, `escalation`, `hold`, `inquiry`, `legal`, `legal-response`, `litigation`, `nda`, `notices`, `questions`, `reply`, `requests`, `responding`, `response`, `shouldn`, `situations`, `subject`, `subpoenas`, `teams`, `templated`, `vendor`

## let-fate-decide

Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide`
- **Skill file**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`
- **Tags**: `ambiguous`, `approaches`, `arbitrarily`, `ask`, `ask-questions-if-underspecified`, `between`, `cards`, `casual`, `casually`, `decide`, `delegated`, `draws`, `entropy`, `fate`, `idk`, `inject`, `interprets`, `let`, `let-fate-decide`, `makes`, `multiple`, `next`, `nonchalant`, `other`, `over`, `phrases`, `pick`, `planning`, `playful`, `precision`, `precision-seeking`, `prefer`, `prompts`, `questions`, `rather`, `reasonable`, `says`, `seeking`, `spread`, `tarot`, `than`, `tone`, `underspecified`, `vague`, `whatever`, `yolo`, `yu-gi-oh`

## search-strategy

Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`
- **Tags**: `ambiguity`, `breaks`, `decomposition`, `enterprise`, `enterprise-search`, `fallback`, `handles`, `language`, `multi`, `natural`, `orchestration`, `per`, `queries`, `query`, `questions`, `ranks`, `relevance`, `search`, `search-strategy`, `searches`, `strategies`, `strategy`, `syntax`, `targeted`, `translates`

## security-ownership-map

Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-ownership-map`
- **Skill file**: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
- **Tags**: `analysis`, `analyze`, `build`, `bus`, `bus-factor`, `checks`, `clusters`, `code`, `codeowners`, `compute`, `csv`, `curated`, `databases`, `explicitly`, `export`, `factor`, `general`, `git`, `graph`, `grounded`, `history`, `hotspots`, `lists`, `maintainer`, `maintainers`, `map`, `non`, `non-security`, `oriented`, `orphaned`, `ownership`, `people`, `people-to`, `questions`, `reality`, `repositories`, `risk`, `security`, `security-oriented`, `security-ownership-map`, `sensitive`, `sensitive-code`, `topology`, `trigger`, `visualization`

## user-research

Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or when the user needs help with any aspect of understanding their users through research.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/user-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/user-research/SKILL.md`
- **Tags**: `aspect`, `conduct`, `design`, `interview`, `needs`, `plan`, `questions`, `research`, `survey`, `synthesize`, `test`, `their`, `trigger`, `understanding`, `usability`
