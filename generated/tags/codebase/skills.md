# Tag: codebase

Skills with tag `codebase`:

## claude-automation-recommender

Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`
- **Tags**: `analyze`, `asks`, `automation`, `automation-recommender`, `automations`, `code`, `codebase`, `features`, `hooks`, `improving`, `know`, `mcp`, `mentions`, `optimize`, `project`, `recommend`, `recommendations`, `recommender`, `servers`, `set`, `subagents`, `their`, `they`

## code-maturity-assessor

Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`
- **Tags**: `access`, `actionable`, `analyzes`, `arithmetic`, `assessment`, `assessor`, `auditing`, `building`, `building-secure-contracts`, `category`, `code`, `code-maturity-assessor`, `codebase`, `complexity`, `contracts`, `controls`, `decentralization`, `documentation`, `evidence`, `framework`, `level`, `low`, `low-level`, `maturity`, `mev`, `practices`, `produces`, `professional`, `ratings`, `recommendations`, `risks`, `safety`, `scorecard`, `secure`, `systematic`, `testing`

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## figma-create-design-system-rules

Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-create-design-system-rules`
- **Skill file**: `external/openai-skills/skills/.curated/figma-create-design-system-rules/SKILL.md`
- **Tags**: `code`, `codebase`, `connection`, `conventions`, `create`, `curated`, `custom`, `customize`, `design`, `establish`, `figma`, `figma-create-design`, `figma-to-code`, `generates`, `guidelines`, `mcp`, `project`, `requires`, `says`, `server`, `set`

## figma-generate-library

Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set up theming (light/dark modes), document foundations, or reconcile gaps between code and Figma. This skill teaches WHAT to build and in WHAT ORDER — it complements the `figma-use` skill which teaches HOW to call the Plugin API. Both skills should be loaded together.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-library`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-library/SKILL.md`
- **Tags**: `api`, `between`, `both`, `build`, `call`, `code`, `codebase`, `complements`, `component`, `create`, `curated`, `dark`, `design`, `document`, `figma`, `figma-library`, `foundations`, `gaps`, `grade`, `libraries`, `library`, `light`, `loaded`, `modes`, `order`, `professional`, `professional-grade`, `reconcile`, `set`, `teaches`, `theming`, `together`, `tokens`, `variables`, `which`

## guidelines-advisor

Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`
- **Tags**: `actionable`, `advisor`, `analyzes`, `architecture`, `assess`, `building`, `building-secure-contracts`, `codebase`, `contract`, `contracts`, `dependencies`, `development`, `documentation`, `evaluate`, `guidelines`, `guidelines-advisor`, `identify`, `implementation`, `pitfalls`, `practices`, `provides`, `quality`, `recommendations`, `review`, `secure`, `smart`, `specifications`, `testing`, `upgradeability`

## scv-scan

Audits Solidity codebases for smart contract vulnerabilities using a four-phase workflow (cheatsheet loading, codebase sweep, deep validation, reporting) covering 36 vulnerability classes. Use when auditing Solidity contracts for security issues, performing smart contract vulnerability scans, or reviewing Solidity code for common exploit patterns.

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan`
- **Skill file**: `external/trailofbits-skills-curated/plugins/scv-scan/skills/scv-scan/SKILL.md`
- **Tags**: `auditing`, `audits`, `cheatsheet`, `classes`, `code`, `codebase`, `codebases`, `contract`, `contracts`, `covering`, `deep`, `exploit`, `four`, `four-phase`, `issues`, `loading`, `performing`, `phase`, `reporting`, `reviewing`, `scan`, `scans`, `scv`, `scv-scan`, `security`, `smart`, `solidity`, `sweep`, `validation`, `vulnerabilities`, `vulnerability`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`
