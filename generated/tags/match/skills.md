# match

## Skills
Load skill file when task matches.

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### prospect
Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

File: `../external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`
