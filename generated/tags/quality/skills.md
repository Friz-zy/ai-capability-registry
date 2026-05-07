# quality

## Skills
Load skill and **use it** when task matches.

### claude-md-improver
Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization".

File: `../external/anthropic-claude-plugins-official/plugins/claude-md-management/skills/claude-md-improver/SKILL.md`

### create-viz
Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation, or needing an interactive chart with hover and zoom.

File: `../external/anthropic-knowledge-work-plugins/data/skills/create-viz/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

File: `../external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### explore-data
Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

File: `../external/anthropic-knowledge-work-plugins/data/skills/explore-data/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

File: `../external/anthropic-skills/skills/frontend-design/SKILL.md`

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

File: `../external/anthropic-claude-plugins-official/plugins/frontend-design/skills/frontend-design/SKILL.md`

### guidelines-advisor
Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Provides actionable recommendations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

### mcp-builder
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

File: `../external/anthropic-skills/skills/mcp-builder/SKILL.md`

### single-cell-rna-qc
Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visualizations. Use when users request QC analysis, filtering low-quality cells, assessing data quality, or following scverse/scanpy best practices for single-cell analysis.

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/single-cell-rna-qc/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

File: `../external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### tech-debt
Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/tech-debt/SKILL.md`
