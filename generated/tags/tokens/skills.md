# tokens

## Skills
Load skill and **use it** when task matches.

### design-handoff
Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.

File: `../external/anthropic-knowledge-work-plugins/design/skills/design-handoff/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### figma-generate-library
Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

File: `../external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`

### figma-use
**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. Skipping it causes common, hard-to-debug failures. Trigger whenever the user wants to perform a write action or a unique read action that requires JavaScript execution in the Figma file context — e.g. create/edit/delete nodes, set up variables or tokens, build components and variants, modify auto-layout or fills, bind variables to properties, or inspect file structure programmatically.

File: `../external/openai-skills/skills/.curated/figma-use/SKILL.md`

### session-report
Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

File: `../external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`
