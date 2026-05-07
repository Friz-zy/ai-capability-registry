# Tag: perform

Skills with tag `perform`:

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## figma-use

**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-use`
- **Skill file**: `external/openai-skills/skills/.curated/figma-use/SKILL.md`
- **Tags**: `auto`, `auto-layout`, `bind`, `build`, `call`, `causes`, `components`, `context`, `create`, `curated`, `debug`, `delete`, `directly`, `edit`, `every`, `execution`, `failures`, `figma`, `fills`, `hard`, `hard-to-debug`, `inspect`, `invoke`, `javascript`, `layout`, `loading`, `mandatory`, `modify`, `must`, `never`, `nodes`, `perform`, `prerequisite`, `programmatically`, `properties`, `requires`, `set`, `skipping`, `structure`, `tokens`, `trigger`, `unique`, `variables`, `variants`, `whenever`, `without`

## openai-security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-best-practices/skills/openai-security-best-practices/SKILL.md`
- **Tags**: `framework`, `improvements`, `language`, `perform`, `practice`, `practices`, `reviews`, `security`, `security-practices`, `suggest`

## security-best-practices

Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-best-practices`
- **Skill file**: `external/openai-skills/skills/.curated/security-best-practices/SKILL.md`
- **Tags**: `code`, `coding`, `curated`, `debugging`, `default`, `explicitly`, `framework`, `general`, `guidance`, `improvements`, `javascript`, `language`, `languages`, `non`, `non-security`, `perform`, `practice`, `practices`, `python`, `report`, `requests`, `review`, `reviews`, `secure`, `secure-by-default`, `security`, `security-practices`, `suggest`, `supported`, `trigger`, `typescript`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/sentry`
- **Skill file**: `external/openai-skills/skills/.curated/sentry/SKILL.md`
- **Tags**: `asks`, `basic`, `cli`, `command`, `curated`, `data`, `errors`, `events`, `health`, `inspect`, `issues`, `perform`, `production`, `pull`, `queries`, `recent`, `sentry`, `summarize`
