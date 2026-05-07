# ask

## Skills
Load skill file when task matches.

### ask-questions-if-underspecified
Clarify requirements before implementing. Use when serious doubts arise.

File: `../external/trailofbits-skills/plugins/ask-questions-if-underspecified/skills/ask-questions-if-underspecified/SKILL.md`

### let-fate-decide
Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

File: `../external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`

### scientific-problem-selection
This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`

### write-spec
Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a feature with goals and non-goals, defining success metrics and acceptance criteria, or breaking a big ask into a phased spec.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/write-spec/SKILL.md`
