# command

## Skills
Load skill file when task matches.

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `../external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### cardputer-buddy
Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

File: `../external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`

### cli-creator
Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

File: `../external/openai-skills/skills/.curated/cli-creator/SKILL.md`

### command-development
This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

File: `../external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`

### example-command
An example user-invoked skill that demonstrates frontmatter options and the skills/<name>/SKILL.md layout

File: `../external/anthropic-claude-plugins-official/plugins/example-plugin/skills/example-command/SKILL.md`

### sentry
Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

File: `../external/openai-skills/skills/.curated/sentry/SKILL.md`
