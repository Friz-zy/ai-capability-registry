# git

## Skills
Load skill and **use it** when task matches.

### gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

File: `external/openai-skills/skills/.curated/gh-address-comments/SKILL.md`

### gh-cli
Enforces authenticated gh CLI workflows over unauthenticated curl/WebFetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

File: `external/trailofbits-skills/.codex/skills/gh-cli/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### git-cleanup
Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

File: `external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup/SKILL.md`

### openai-gh-address-comments
Help address review/issue comments on the open GitHub PR for the current branch using gh

File: `external/trailofbits-skills-curated/plugins/openai-gh-address-comments/skills/openai-gh-address-comments/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

File: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### openai-security-ownership-map
'Analyze git repositories to build a security ownership topology (people-to-file), compute

File: `external/trailofbits-skills-curated/plugins/openai-security-ownership-map/skills/openai-security-ownership-map/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### security-ownership-map
Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

File: `external/openai-skills/skills/.curated/security-ownership-map/SKILL.md`
