# debugging

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` and use it before acting.

### claude-in-chrome-troubleshooting
Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

File: `external/trailofbits-skills/plugins/claude-in-chrome-troubleshooting/skills/claude-in-chrome-troubleshooting/SKILL.md`

### debug
Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

File: `external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`

### dwarf-expert
Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

File: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### openai-gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions;

File: `external/trailofbits-skills-curated/plugins/openai-gh-fix-ci/skills/openai-gh-fix-ci/SKILL.md`

### openai-sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors,

File: `external/trailofbits-skills-curated/plugins/openai-sentry/skills/openai-sentry/SKILL.md`

### systematic-debugging
Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

File: `external/superpowers-skills/skills/systematic-debugging/SKILL.md`
