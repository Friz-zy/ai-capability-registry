# Tag: trigger

Skills with tag `trigger`:

## accessibility-review

Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/accessibility-review/SKILL.md`
- **Tags**: `a11y`, `accessibility`, `accessibility-review`, `accessible`, `audit`, `behavior`, `color`, `contrast`, `design`, `handoff`, `keyboard`, `navigation`, `page`, `reader`, `review`, `reviewing`, `screen`, `size`, `target`, `touch`, `trigger`, `wcag`

## account-research

Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your CRM. Trigger with "research [company]", "look up [person]", "intel on [prospect]", "who is [name] at [company]", or "tell me about [company]".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/account-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/account-research/SKILL.md`
- **Tags**: `account`, `account-research`, `actionable`, `company`, `connect`, `crm`, `enrichment`, `intel`, `look`, `person`, `prospect`, `research`, `sales`, `search`, `standalone`, `supercharged`, `tell`, `trigger`, `web`, `who`

## call-prep

Prepare for a sales call with account context, attendee research, and suggested agenda. Works standalone with user input and web research, supercharged when you connect your CRM, email, chat, or transcripts. Trigger with "prep me for my call with [company]", "I'm meeting with [company] prep me", "call prep [company]", or "get me ready for [meeting]".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep/SKILL.md`
- **Tags**: `account`, `agenda`, `attendee`, `call`, `call-prep`, `chat`, `company`, `connect`, `context`, `crm`, `email`, `input`, `meeting`, `prep`, `prepare`, `ready`, `research`, `sales`, `standalone`, `suggested`, `supercharged`, `transcripts`, `trigger`, `web`

## cardputer-buddy

Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`
- **Tags**: `adv`, `already`, `app`, `buddy`, `bundle`, `cardputer`, `cardputer-adv`, `cardputer-buddy`, `changed`, `command`, `cwc`, `cwc-makers`, `device`, `flashing`, `follow`, `follow-up`, `hello`, `iterate`, `logs`, `m5-onboard`, `maker`, `makers`, `micropython`, `onboard`, `one`, `one-shot`, `provisioned`, `push`, `re-flashing`, `repl`, `serial`, `shot`, `single`, `snake`, `tail`, `trigger`, `watch`, `without`

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## code-review

Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`
- **Tags**: `cases`, `change`, `changes`, `checking`, `code`, `code-review`, `correctness`, `diff`, `edge`, `engineering`, `error`, `gaps`, `handling`, `injection`, `merge`, `missing`, `performance`, `queries`, `review`, `risks`, `safe`, `security`, `trigger`, `url`

## comp-analysis

Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`
- **Tags**: `analysis`, `analyze`, `band`, `benchmarking`, `comp`, `comp-analysis`, `compensation`, `competitive`, `data`, `equity`, `find`, `grant`, `human`, `model`, `modeling`, `offer`, `outliers`, `pay`, `placement`, `retention`, `risks`, `role`, `trigger`, `uploading`

## competitive-intelligence

Research your competitors and build an interactive battlecard. Outputs an HTML artifact with clickable competitor cards and a comparison matrix. Trigger with "competitive intel", "research competitors", "how do we compare to [competitor]", "battlecard for [competitor]", or "what's new with [competitor]".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/competitive-intelligence/SKILL.md`
- **Tags**: `artifact`, `battlecard`, `build`, `cards`, `clickable`, `compare`, `comparison`, `competitive`, `competitive-intelligence`, `competitor`, `competitors`, `html`, `intel`, `intelligence`, `interactive`, `matrix`, `outputs`, `research`, `sales`, `trigger`

## compliance-tracking

Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or when the user needs help tracking, preparing for, or documenting compliance activities.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/compliance-tracking`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/compliance-tracking/SKILL.md`
- **Tags**: `activities`, `audit`, `compliance`, `compliance-tracking`, `documenting`, `gdpr`, `iso`, `needs`, `operations`, `prep`, `preparing`, `readiness`, `regulatory`, `requirement`, `requirements`, `soc`, `track`, `tracking`, `trigger`

## daily-briefing

Start your day with a prioritized sales briefing. Works standalone when you tell me your meetings and priorities, supercharged when you connect your calendar, CRM, and email. Trigger with "morning briefing", "daily brief", "what's on my plate today", "prep my day", or "start my day".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/daily-briefing`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/daily-briefing/SKILL.md`
- **Tags**: `brief`, `briefing`, `calendar`, `connect`, `crm`, `daily`, `daily-briefing`, `day`, `email`, `meetings`, `morning`, `plate`, `prep`, `priorities`, `prioritized`, `sales`, `standalone`, `start`, `supercharged`, `tell`, `today`, `trigger`

## debug

Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/debug`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`
- **Tags**: `behavior`, `broke`, `but`, `cause`, `debug`, `debugging`, `deploy`, `diagnose`, `diverges`, `engineering`, `error`, `expected`, `fix`, `isn`, `isolate`, `message`, `obvious`, `prod`, `reproduce`, `session`, `something`, `stack`, `staging`, `structured`, `trace`, `trigger`

## design-critique

Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this screen?", or when sharing a Figma link or screenshot for feedback at any stage from exploration to final polish.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/design-critique`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/design-critique/SKILL.md`
- **Tags**: `consistency`, `critique`, `design`, `design-critique`, `exploration`, `feedback`, `figma`, `final`, `hierarchy`, `link`, `mockup`, `polish`, `review`, `screen`, `screenshot`, `sharing`, `stage`, `structured`, `think`, `trigger`, `usability`

## doc-coauthoring

Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/doc-coauthoring`
- **Skill file**: `external/anthropic-skills/skills/doc-coauthoring/SKILL.md`
- **Tags**: `authoring`, `co-authoring`, `coauthoring`, `content`, `context`, `creating`, `decision`, `doc`, `doc-coauthoring`, `docs`, `documentation`, `drafting`, `efficiently`, `helps`, `iteration`, `mentions`, `proposals`, `readers`, `refine`, `similar`, `specs`, `structured`, `technical`, `transfer`, `trigger`, `verify`

## documentation

Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/documentation/SKILL.md`
- **Tags**: `api`, `architecture`, `create`, `docs`, `document`, `documentation`, `engineering`, `form`, `maintain`, `needs`, `onboarding`, `operational`, `readme`, `runbook`, `runbooks`, `technical`, `trigger`

## draft-outreach

Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with "draft outreach to [person/company]", "write cold email to [prospect]", "reach out to [name]".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/draft-outreach`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/draft-outreach/SKILL.md`
- **Tags**: `cold`, `company`, `crm`, `default`, `draft`, `draft-outreach`, `email`, `enrichment`, `out`, `outreach`, `person`, `personalized`, `prospect`, `reach`, `research`, `sales`, `supercharged`, `then`, `trigger`, `web`

## figma

Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma`
- **Skill file**: `external/openai-skills/skills/.curated/figma/SKILL.md`
- **Tags**: `assets`, `code`, `context`, `curated`, `design`, `design-to-code`, `fetch`, `figma`, `ids`, `implementation`, `involves`, `mcp`, `node`, `nodes`, `production`, `screenshots`, `server`, `translate`, `trigger`, `troubleshooting`, `urls`, `variables`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## incident-response

Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response/SKILL.md`
- **Tags**: `alert`, `assessment`, `blameless`, `communicate`, `down`, `engineering`, `have`, `incident`, `incident-response`, `mid`, `mid-incident`, `needs`, `postmortem`, `production`, `resolution`, `response`, `severity`, `status`, `triage`, `trigger`

## interview-prep

Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we interview", "scorecard for", or when the user is preparing to interview candidates.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/interview-prep/SKILL.md`
- **Tags**: `candidates`, `competency`, `create`, `human`, `interview`, `interview-prep`, `plan`, `plans`, `prep`, `preparing`, `questions`, `scorecard`, `scorecards`, `structured`, `trigger`

## org-planning

Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should we hire next", or when the user is thinking about team size, reporting structure, or organizational design.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/org-planning/SKILL.md`
- **Tags**: `design`, `headcount`, `hire`, `human`, `next`, `optimization`, `org`, `org-planning`, `organizational`, `plan`, `planning`, `reorg`, `reporting`, `size`, `structure`, `team`, `thinking`, `trigger`, `who`

## policy-lookup

Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", or any plain-language question about benefits, travel, leave, or handbook rules.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/policy-lookup`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/policy-lookup/SKILL.md`
- **Tags**: `another`, `benefits`, `can`, `company`, `country`, `expenses`, `explain`, `find`, `handbook`, `human`, `language`, `leave`, `lookup`, `our`, `plain`, `plain-language`, `policies`, `policy`, `policy-lookup`, `pto`, `question`, `remotely`, `travel`, `trigger`

## pptx

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/pptx`
- **Skill file**: `external/anthropic-skills/skills/pptx/SKILL.md`
- **Tags**: `afterward`, `both`, `combining`, `comments`, `content`, `created`, `creating`, `deck`, `decks`, `editing`, `elsewhere`, `email`, `even`, `existing`, `extracted`, `extracting`, `filename`, `includes`, `input`, `involved`, `layouts`, `like`, `mentions`, `modifying`, `needs`, `notes`, `opened`, `parsing`, `pitch`, `plan`, `pptx`, `presentation`, `presentations`, `reading`, `regardless`, `slide`, `slides`, `speaker`, `splitting`, `summary`, `text`, `they`, `time`, `touched`, `trigger`, `updating`, `used`, `way`, `whenever`, `will`, `working`

## process-optimization

Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`
- **Tags**: `analyze`, `bottleneck`, `business`, `can`, `describes`, `fix`, `improve`, `inefficient`, `many`, `operations`, `optimization`, `process`, `process-optimization`, `processes`, `slow`, `streamline`, `they`, `too`, `trigger`, `want`

## recruiting-pipeline

Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user discusses sourcing, screening, interviewing, or extending offers.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline`
- **Skill file**: `external/anthropic-knowledge-work-plugins/human-resources/skills/recruiting-pipeline/SKILL.md`
- **Tags**: `candidate`, `candidates`, `discusses`, `extending`, `hiring`, `human`, `interviewing`, `manage`, `many`, `offers`, `pipeline`, `recruiting`, `recruiting-pipeline`, `screening`, `sourcing`, `stages`, `status`, `track`, `trigger`

## risk-assessment

Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`
- **Tags**: `assess`, `assessment`, `associated`, `could`, `decision`, `evaluating`, `identify`, `mitigate`, `operational`, `operations`, `process`, `project`, `register`, `risk`, `risk-assessment`, `risks`, `trigger`, `vendor`, `wrong`

## search

Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or when looking for a decision, document, or discussion that could live in chat, email, cloud storage, or a project tracker.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search/SKILL.md`
- **Tags**: `chat`, `cloud`, `connected`, `conversation`, `could`, `decide`, `decision`, `did`, `discussion`, `doc`, `document`, `email`, `enterprise`, `enterprise-search`, `find`, `live`, `looking`, `one`, `project`, `query`, `search`, `sources`, `storage`, `tracker`, `trigger`, `was`, `where`

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

## system-design

Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`
- **Tags**: `api`, `architect`, `architecture`, `architectures`, `boundaries`, `data`, `design`, `engineering`, `modeling`, `needs`, `right`, `service`, `services`, `systems`, `trigger`

## tech-debt

Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`
- **Tags**: `asks`, `audit`, `backlog`, `categorize`, `code`, `debt`, `engineering`, `health`, `identify`, `maintenance`, `priorities`, `prioritize`, `quality`, `refactor`, `refactoring`, `tech`, `tech-debt`, `technical`, `trigger`

## testing-strategy

Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/testing-strategy`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/testing-strategy/SKILL.md`
- **Tags**: `approaches`, `architecture`, `coverage`, `design`, `engineering`, `needs`, `plan`, `plans`, `strategies`, `strategy`, `test`, `testing`, `testing-strategy`, `tests`, `trigger`

## user-research

Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or when the user needs help with any aspect of understanding their users through research.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/user-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/user-research/SKILL.md`
- **Tags**: `aspect`, `conduct`, `design`, `interview`, `needs`, `plan`, `questions`, `research`, `survey`, `synthesize`, `test`, `their`, `trigger`, `understanding`, `usability`

## ux-copy

Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error message", or when naming a CTA, wording a confirmation dialog, filling an empty state, or writing onboarding text.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/design/skills/ux-copy`
- **Skill file**: `external/anthropic-knowledge-work-plugins/design/skills/ux-copy/SKILL.md`
- **Tags**: `button`, `confirmation`, `copy`, `cta`, `ctas`, `design`, `dialog`, `empty`, `error`, `filling`, `message`, `messages`, `microcopy`, `naming`, `onboarding`, `review`, `say`, `state`, `states`, `text`, `trigger`, `ux-copy`, `wording`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`
