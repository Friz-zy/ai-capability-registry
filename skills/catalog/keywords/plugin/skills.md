# plugin

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### cowork-plugin-customizer
Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, adjust plugin settings, customize plugin connectors, customize plugin skill, tweak plugin, modify plugin configuration.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md`

### create-cowork-plugin
Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.

File: `external/anthropic-knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md`

### plugin-creator
Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

File: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`

### using-superpowers
Use when starting any conversation - establishes how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions

File: `external/superpowers-skills/skills/using-superpowers/SKILL.md`

### writing-skills
Use when creating new skills, editing existing skills, or verifying skills work before deployment

File: `external/superpowers-skills/skills/writing-skills/SKILL.md`
