---
description: >
  Template skill for Claude Code.
  Replace with a specific description of what the skill does.
  The model auto-invokes skills when the description matches the task.
name: my-skill-name
disable-model-invocation: false
user-invocable: true
allowed-tools:
  - Read
  - Grep
  - Glob
model: inherit
effort: high
context: inherit
---

# Skill Title

## Purpose

Describe the purpose and scope of this skill.

## Instructions

1. Step-by-step instructions for the skill.
2. Be specific about what the agent should do.
3. Include any constraints or requirements.

## Examples

Provide concrete examples of when and how this skill should be used.

## Notes

- Skill directory: `~/.claude/skills/<skill-name>/SKILL.md` (global)
  or `.claude/skills/<skill-name>/SKILL.md` (project)
- The directory name becomes the skill command: `/skill-name`
- Set `disable-model-invocation: true` for manual-only skills
- Use `${CLAUDE_SKILL_DIR}` env var to reference skill directory in the prompt