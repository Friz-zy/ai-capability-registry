---
description: >
  Template skill for Codex CLI.
  Replace this description with a specific description
  of what the skill does. The model uses this to decide
  when to auto-invoke the skill.
---

# Codex CLI Skill Template

## Purpose

Describe the purpose and scope of this skill.

## Instructions

1. Step-by-step instructions for the skill.
2. Be specific about what the agent should do.
3. Include any constraints or requirements.

## Examples

Provide concrete examples of when and how this skill should be used.

## Notes

- Skill directory: `~/.agents/skills/<skill-name>/SKILL.md` (global)
  or `.agents/skills/<skill-name>/SKILL.md` (project)
- Enable/disable in config: `[[skills.config]]` with `path` and `enabled`
- Dependencies can be declared: `SkillDependencies { tools: [...] }`