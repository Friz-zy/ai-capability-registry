# Tag: github

Skills with tag `github`:

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

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

## gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/gh-fix-ci`
- **Skill file**: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `approval`, `asks`, `buildkite`, `checks`, `context`, `curated`, `debug`, `draft`, `explicit`, `failing`, `failure`, `fix`, `gh-fix-ci`, `github`, `implement`, `inspect`, `logs`, `out`, `plan`, `providers`, `report`, `scope`, `summarize`, `treat`, `url`

## openai-gh-address-comments

Help address review/issue comments on the open GitHub PR for the current branch using gh

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`
- **Tags**: `address`, `branch`, `comments`, `gh-address-comments`, `github`, `issue`, `open`, `review`

## openai-gh-fix-ci

Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`
- **Tags**: `actions`, `asks`, `checks`, `debug`, `failing`, `fix`, `gh-fix-ci`, `github`

## openai-yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`
- **Tags**: `asks`, `commit`, `explicitly`, `github`, `open`, `pull`, `push`, `request`, `stage`, `yeet`

## skill-installer

Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/skill-installer`
- **Skill file**: `external/openai-skills/skills/.system/skill-installer/SKILL.md`
- **Tags**: `another`, `asks`, `codex`, `codex-home`, `curated`, `github`, `home`, `including`, `install`, `installable`, `installer`, `path`, `private`, `repo`, `repos`

## yeet

Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/yeet`
- **Skill file**: `external/openai-skills/skills/.curated/yeet/SKILL.md`
- **Tags**: `asks`, `cli`, `commit`, `curated`, `explicitly`, `flow`, `github`, `one`, `open`, `pull`, `push`, `request`, `stage`, `yeet`
