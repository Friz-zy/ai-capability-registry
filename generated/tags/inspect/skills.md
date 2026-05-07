# inspect

## Skills
Load skill file when task matches.

### figma-use
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

File: `../external/openai-skills/skills/.curated/figma-use/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `../external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### openai-sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

File: `../external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

File: `../external/openai-skills/skills/.curated/sentry/SKILL.md`
