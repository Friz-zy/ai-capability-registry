# right

## Skills
Load skill file when task matches.

### build-mcp-server
This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

File: `../external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

### choose-zoom-approach
Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md`

### create-viz
Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or comparison, generating a plot for a report or presentation, or needing an interactive chart with hover and zoom.

File: `../external/anthropic-knowledge-work-plugins/data/skills/create-viz/SKILL.md`

### data-visualization
Create effective data visualizations with Python (matplotlib, seaborn, plotly). Use when building charts, choosing the right chart type for a dataset, creating publication-quality figures, or applying design principles like accessibility and color theory.

File: `../external/anthropic-knowledge-work-plugins/data/skills/data-visualization/SKILL.md`

### debug-zoom
Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is failing and you need a ranked hypothesis list plus verification steps.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/debug-zoom/SKILL.md`

### last30days
Researches a topic from the last 30 days on Reddit, X, and the web. Surfaces real community discussions with engagement metrics and synthesizes findings into actionable insights. Use when the user wants to know what people are saying about a topic right now.

File: `../external/trailofbits-skills-curated/plugins/last30days/skills/last30days/SKILL.md`

### plan-zoom-product
Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, or MCP for a specific product idea or integration goal.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md`

### setup-zoom-mcp
Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or defining a hybrid MCP architecture.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md`

### start
Start here for any Zoom integration or app idea. Use when you need to choose the right Zoom surface, shape the architecture, or route into the correct implementation skill without reading the whole Zoom doc set first.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/start/SKILL.md`

### system-design
Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

File: `../external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`

### validate-data
QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

File: `../external/anthropic-knowledge-work-plugins/data/skills/validate-data/SKILL.md`
