# github

## Skills
Load skill file when task matches.

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

File: `../external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

File: `../external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`

### gh-cli
Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

File: `../external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `../external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### openai-gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh

File: `../external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

File: `../external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `../external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

File: `../external/openai-skills/skills/.system/skill-installer/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

File: `../external/openai-skills/skills/.curated/yeet/SKILL.md`
