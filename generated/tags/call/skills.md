# Tag: call

Skills with tag `call`:

## build-zoom-phone-integration

Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CTI dialers, or call handling automation.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/phone`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/phone/SKILL.md`
- **Tags**: `apis`, `automation`, `build`, `build-zoom-phone-integration`, `call`, `crm`, `cti`, `dialers`, `embed`, `events`, `handling`, `implementing`, `integration`, `oauth`, `partner`, `phone`, `routing`, `schemes`, `smart`, `uri`, `webhooks`, `zoom`

## call-prep

Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md`
- **Tags**: `call`, `call-prep`, `company`, `customer`, `know`, `meeting`, `partner`, `prep`, `preparation`, `prepare`, `prospect`, `request`, `room`, `signals`, `talking`, `triggers`

## call-prep

Prepare for a sales call with account context, attendee research, and suggested agenda. Works standalone with user input and web research, supercharged when you connect your CRM, email, chat, or transcripts. Trigger with "prep me for my call with [company]", "I'm meeting with [company] prep me", "call prep [company]", or "get me ready for [meeting]".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/call-prep/SKILL.md`
- **Tags**: `account`, `agenda`, `attendee`, `call`, `call-prep`, `chat`, `company`, `connect`, `context`, `crm`, `email`, `input`, `meeting`, `prep`, `prepare`, `ready`, `research`, `sales`, `standalone`, `suggested`, `supercharged`, `transcripts`, `trigger`, `web`

## call-summary

Process call notes or a transcript — extract action items, draft follow-up email, generate internal summary. Use when pasting rough notes or a transcript after a discovery, demo, or negotiation call, drafting a customer follow-up, logging the activity for your CRM, or capturing objections and next steps for your team.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/call-summary`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/call-summary/SKILL.md`
- **Tags**: `activity`, `call`, `call-summary`, `capturing`, `crm`, `customer`, `demo`, `discovery`, `draft`, `drafting`, `email`, `extract`, `follow`, `follow-up`, `internal`, `items`, `logging`, `negotiation`, `next`, `notes`, `objections`, `pasting`, `process`, `rough`, `sales`, `summary`, `team`, `transcript`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## forecast

Generate a weighted sales forecast with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis. Use when preparing a quarterly forecast call, assessing gap-to-quota from a pipeline CSV, deciding which deals to commit vs. call upside, or checking pipeline coverage against your number.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/sales/skills/forecast`
- **Skill file**: `external/anthropic-knowledge-work-plugins/sales/skills/forecast/SKILL.md`
- **Tags**: `against`, `analysis`, `assessing`, `breakdown`, `call`, `checking`, `commit`, `coverage`, `csv`, `deals`, `deciding`, `forecast`, `gap`, `gap-to-quota`, `likely`, `number`, `pipeline`, `preparing`, `quarterly`, `quota`, `sales`, `scenarios`, `upside`, `weighted`, `which`, `worst`

## genotoxic

Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`
- **Tags**: `analyzing`, `cairo`, `cairo-mutants`, `call`, `circomvent`, `codebases`, `coverage`, `data`, `false`, `finding`, `frameworks`, `fuzzing`, `gaps`, `genotoxic`, `graph`, `graph-informed`, `identify`, `identifying`, `including`, `informed`, `missing`, `mutants`, `mutation`, `necessist`, `parses`, `positives`, `running`, `runs`, `statements`, `survived`, `targets`, `test`, `testing`, `tests`, `then`, `trailmark`, `triage`, `triaging`, `unnecessary`, `weak`

## runbook

Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/operations/skills/runbook`
- **Skill file**: `external/anthropic-knowledge-work-plugins/operations/skills/runbook/SKILL.md`
- **Tags**: `adding`, `call`, `commands`, `create`, `documenting`, `escalation`, `exact`, `existing`, `knowledge`, `needs`, `on-call`, `operational`, `operations`, `ops`, `paths`, `procedure`, `recurring`, `repeatably`, `rollback`, `runbook`, `things`, `tribal`, `troubleshooting`, `turning`, `wrong`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`
