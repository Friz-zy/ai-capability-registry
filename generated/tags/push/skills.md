# push

## Skills
Load skill and **use it** when task matches.

### campaign-plan
Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a product launch, lead-gen push, or awareness campaign, when you need a week-by-week content calendar with dependencies, or when translating a marketing goal into a structured, executable plan.

File: `../external/anthropic-knowledge-work-plugins/marketing/skills/campaign-plan/SKILL.md`

### cardputer-buddy
Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

File: `../external/anthropic-claude-plugins-official/plugins/cwc-makers/skills/cardputer-buddy/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### openai-yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request

File: `../external/trailofbits-skills-curated/plugins/openai-yeet/skills/openai-yeet/SKILL.md`

### vercel-deploy
Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

File: `../external/openai-skills/skills/.curated/vercel-deploy/SKILL.md`

### yeet
Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).

File: `../external/openai-skills/skills/.curated/yeet/SKILL.md`
