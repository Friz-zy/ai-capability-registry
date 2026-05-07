# Tag: cli

Skills with tag `cli`:

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

## gh-address-comments

Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-address-comments`
- **Skill file**: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`
- **Tags**: `address`, `auth`, `authenticate`, `branch`, `cli`, `comments`, `curated`, `gh-address-comments`, `github`, `issue`, `logged`, `open`, `prompt`, `review`, `verify`

## gh-cli

Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/.codex/skills/gh-cli`
- **Skill file**: `external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`
- **Tags**: `access`, `api`, `authenticated`, `cli`, `codex`, `curl`, `enforces`, `gh-cli`, `github`, `issues`, `over`, `pull`, `requests`, `unauthenticated`, `urls`, `webfetch`, `working`

## netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/netlify-deploy`
- **Skill file**: `external/openai-skills/skills/.curated/netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `curated`, `deploy`, `deploys`, `host`, `including`, `link`, `netlify`, `netlify-deploy`, `npx`, `preview`, `production`, `projects`, `publish`, `repo`, `site`, `web`

## openai-netlify-deploy

Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-netlify-deploy/skills/openai-netlify-deploy/SKILL.md`
- **Tags**: `asks`, `cli`, `deploy`, `netlify`, `netlify-deploy`, `npx`, `projects`, `web`

## playwright

Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/playwright`
- **Skill file**: `external/openai-skills/skills/.curated/playwright/SKILL.md`
- **Tags**: `automating`, `browser`, `bundled`, `cli`, `curated`, `data`, `debugging`, `extraction`, `filling`, `flow`, `form`, `navigation`, `playwright`, `playwright-cli`, `real`, `requires`, `screenshots`, `script`, `snapshots`, `terminal`, `ui-flow`, `wrapper`

## second-opinion

Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
- **Skill file**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`
- **Tags**: `asks`, `branch`, `changes`, `cli`, `code`, `codex`, `commits`, `diffs`, `gemini`, `google`, `llm`, `mentions`, `opinion`, `review`, `reviews`, `runs`, `second`, `second-opinion`, `uncommitted`

## sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/sentry`
- **Skill file**: `external/openai-skills/skills/.curated/sentry/SKILL.md`
- **Tags**: `asks`, `basic`, `cli`, `command`, `curated`, `data`, `errors`, `events`, `health`, `inspect`, `issues`, `perform`, `production`, `pull`, `queries`, `recent`, `sentry`, `summarize`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`

## yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/yeet`
- **Skill file**: `external/openai-skills/skills/.curated/yeet/SKILL.md`
- **Tags**: `asks`, `cli`, `commit`, `curated`, `explicitly`, `flow`, `github`, `one`, `open`, `pull`, `push`, `request`, `stage`, `yeet`
