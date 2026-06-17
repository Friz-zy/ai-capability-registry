---
name: my-skill-name
description: >
  Template skill for Kilo Code.
  Replace with a specific description of what the skill does.
  The agent auto-invokes skills when the description matches the task.
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

- Skill directory: `~/.config/kilo/skills/<skill-name>/SKILL.md` (global)
  or `.kilo/skills/<skill-name>/SKILL.md` (project)
- Compat skill directories also scanned:
  `.claude/skills/<skill-name>/SKILL.md`
  `.agents/skills/<skill-name>/SKILL.md`
- For commands (non-skill prompts):
  `.kilo/command/<command-name>.md`