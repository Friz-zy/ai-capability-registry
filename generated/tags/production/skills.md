# Tag: production

Skills with tag `production`:

## deploy-checklist

Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`
- **Tags**: `ahead`, `approvals`, `change`, `checklist`, `database`, `deploy`, `deploy-checklist`, `deploying`, `deployment`, `documenting`, `engineering`, `feature`, `flags`, `going`, `migrations`, `pre`, `pre-deployment`, `production`, `release`, `rollback`, `ship`, `status`, `time`, `triggers`, `verification`, `verifying`

## figma

Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when a task involves Figma URLs, node IDs, design-to-code implementation, or Figma MCP setup and troubleshooting.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma`
- **Skill file**: `external/openai-skills/skills/.curated/figma/SKILL.md`
- **Tags**: `assets`, `code`, `context`, `curated`, `design`, `design-to-code`, `fetch`, `figma`, `ids`, `implementation`, `involves`, `mcp`, `node`, `nodes`, `production`, `screenshots`, `server`, `translate`, `trigger`, `troubleshooting`, `urls`, `variables`

## figma-implement-design

Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "implement design", "generate code", "implement component", provides Figma URLs, or asks to build components matching Figma specs. For Figma canvas writes via `use_figma`, use `figma-use`.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-implement-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-implement-design/SKILL.md`
- **Tags**: `application`, `asks`, `build`, `canvas`, `code`, `component`, `components`, `curated`, `design`, `designs`, `fidelity`, `figma`, `figma-implement-design`, `implement`, `implementing`, `matching`, `mentions`, `production`, `production-ready`, `provides`, `ready`, `specs`, `translates`, `urls`, `visual`, `writes`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/frontend-design`
- **Skill file**: `external/anthropic-skills/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `artifacts`, `asks`, `avoids`, `beautifying`, `build`, `code`, `components`, `create`, `creative`, `css`, `dashboards`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `html`, `include`, `interfaces`, `landing`, `layouts`, `pages`, `polished`, `posters`, `production`, `production-grade`, `quality`, `react`, `styling`, `web`, `websites`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `asks`, `avoids`, `build`, `code`, `components`, `create`, `creative`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `interfaces`, `pages`, `polished`, `production`, `production-grade`, `quality`, `web`

## incident-response

Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs severity assessment, a status update mid-incident, or when writing a blameless postmortem after resolution.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/incident-response/SKILL.md`
- **Tags**: `alert`, `assessment`, `blameless`, `communicate`, `down`, `engineering`, `have`, `incident`, `incident-response`, `mid`, `mid-incident`, `needs`, `postmortem`, `production`, `resolution`, `response`, `severity`, `status`, `triage`, `trigger`

## insecure-defaults

Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
- **Skill file**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- **Tags**: `allow`, `analyzing`, `apps`, `auditing`, `auth`, `config`, `defaults`, `detects`, `environment`, `fail`, `fail-open`, `handling`, `hardcoded`, `insecure`, `insecure-defaults`, `insecurely`, `management`, `open`, `permissive`, `production`, `reviewing`, `secrets`, `security`, `variable`, `weak`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

## netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/netlify-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `curated`, `deploy`, `deploys`, `host`, `including`, `link`, `netlify`, `netlify-deploy`, `npx`, `preview`, `production`, `projects`, `publish`, `repo`, `site`, `web`

## openai-sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`
- **Tags**: `asks`, `errors`, `events`, `inspect`, `issues`, `production`, `recent`, `sentry`, `summarize`

## sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/sentry`
- **Skill file**: `external/openai-skills/skills/.curated/sentry/SKILL.md`
- **Tags**: `asks`, `basic`, `cli`, `command`, `curated`, `data`, `errors`, `events`, `health`, `inspect`, `issues`, `perform`, `production`, `pull`, `queries`, `recent`, `sentry`, `summarize`
