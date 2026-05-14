# skill-creator

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### add-remote-skill
This skill should be used when the user wants to add one or more skills from GitHub repositories to the kilo-marketplace. It handles parsing GitHub URLs, cloning skill directories, and updating SKILL.md frontmatter with source metadata.

File: `external/kilo-marketplace-skills/.kilocode/skills/add-remote-skill/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

File: `external/anthropic-skills/skills/skill-creator/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

File: `external/openai-skills/skills/.system/skill-creator/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

File: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### skill-installer
Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

File: `external/openai-skills/skills/.system/skill-installer/SKILL.md`

### skill-share
A skill that creates new agent skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.

File: `external/kilo-marketplace-skills/skills/skill-share/SKILL.md`

### writing-skills
Use when creating new skills, editing existing skills, or verifying skills work before deployment

File: `external/superpowers-skills/skills/writing-skills/SKILL.md`
