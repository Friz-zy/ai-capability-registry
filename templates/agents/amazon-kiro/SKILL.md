---
name: my-skill-name
description: >
  Template skill for Amazon Kiro.
  Replace with a specific description of what the skill does.
  Skills are progressively loaded — metadata is loaded at startup,
  full content is loaded on demand when the agent determines it's needed.
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

- Skill directory: `~/.kiro/skills/<skill-name>/SKILL.md` (global)
  or `.kiro/skills/<skill-name>/SKILL.md` (project)
- YAML frontmatter must include `name` and `description`
- Skills are referenced from agent config: `"skill://.kiro/skills/**/SKILL.md"`
- Manual activation only (no auto-invoke in Kiro)