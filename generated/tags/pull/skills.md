# pull

## Skills
Load skill file when task matches.

### account-research
Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

File: `../external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md`

### gh-cli
Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

File: `../external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `../external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

File: `../external/openai-skills/skills/.curated/sentry/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

File: `../external/openai-skills/skills/.curated/yeet/SKILL.md`
