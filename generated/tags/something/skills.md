# Tag: something

Skills with tag `something`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## compliance-check

Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk areas. Use when launching a feature that touches personal data, when marketing or product proposes something with regulatory implications, or when you need to know which approvals and jurisdictional requirements apply before proceeding.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/legal/skills/compliance-check`
- **Skill file**: `external/anthropic-knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`
- **Tags**: `applicable`, `apply`, `approvals`, `areas`, `business`, `compliance`, `data`, `feature`, `implications`, `initiative`, `jurisdictional`, `know`, `launching`, `legal`, `marketing`, `personal`, `proceeding`, `product`, `proposed`, `proposes`, `regulations`, `regulatory`, `requirements`, `risk`, `something`, `surfacing`, `touches`, `which`

## customer-research

Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a bug has been reported before, checking what was previously told to a specific account, or gathering background before drafting a response.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/customer-support/skills/customer-research/SKILL.md`
- **Tags**: `account`, `asks`, `attribution`, `background`, `been`, `bug`, `checking`, `customer`, `customer-research`, `customer-support`, `drafting`, `gathering`, `has`, `investigating`, `look`, `multi`, `previously`, `question`, `reported`, `research`, `response`, `something`, `support`, `told`, `topic`, `was`, `whether`

## debug

Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "something broke after the deploy", or when behavior diverges from expected and the cause isn't obvious.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/debug`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/debug/SKILL.md`
- **Tags**: `behavior`, `broke`, `but`, `cause`, `debug`, `debugging`, `deploy`, `diagnose`, `diverges`, `engineering`, `error`, `expected`, `fix`, `isn`, `isolate`, `message`, `obvious`, `prod`, `reproduce`, `session`, `something`, `stack`, `staging`, `structured`, `trace`, `trigger`

## playground

Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/playground/skills/playground/SKILL.md`
- **Tags**: `asks`, `configure`, `contained`, `controls`, `copy`, `creates`, `explorer`, `explorers`, `html`, `interactive`, `let`, `live`, `make`, `out`, `playground`, `playgrounds`, `preview`, `prompt`, `self`, `self-contained`, `single`, `something`, `topic`, `visually`

## xlsx

Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like \"the xlsx in my downloads\") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/xlsx`
- **Skill file**: `external/anthropic-skills/skills/xlsx/SKILL.md`
- **Tags**: `adding`, `api`, `between`, `casually`, `charting`, `cleaning`, `columns`, `computing`, `convert`, `create`, `csv`, `data`, `database`, `deliverable`, `document`, `done`, `downloads`, `edit`, `especially`, `even`, `existing`, `fix`, `formats`, `formatting`, `formulas`, `google`, `headers`, `html`, `input`, `integration`, `involved`, `junk`, `like`, `malformed`, `means`, `messy`, `misplaced`, `must`, `open`, `other`, `path`, `pipeline`, `primary`, `produced`, `proper`, `python`, `report`, `restructuring`, `rows`, `scratch`, `script`, `sheets`, `something`, `sources`, `spreadsheet`, `spreadsheets`, `standalone`, `tabular`, `time`, `trigger`, `tsv`, `where`, `word`, `xlsm`, `xlsx`
