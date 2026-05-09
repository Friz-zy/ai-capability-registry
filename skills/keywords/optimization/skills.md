# optimization

## Skills
Load skill and **use it** when task matches.

### process-optimization
Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.

File: `external/anthropic-knowledge-work-plugins/operations/skills/process-optimization/SKILL.md`

### skill-creator
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

File: `external/anthropic-skills/skills/skill-creator/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

File: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`
