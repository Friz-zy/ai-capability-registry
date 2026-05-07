# Tag: entry

Skills with tag `entry`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## entry-point-analyzer

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
- **Tags**: `access`, `admin`, `analyzer`, `analyzes`, `asked`, `audit`, `auditing`, `callable`, `categorizes`, `changing`, `codebases`, `contract`, `contracts`, `control`, `cosmwasm`, `detects`, `entry`, `entry-point-analyzer`, `excludes`, `externally`, `find`, `flows`, `functions`, `generates`, `identify`, `level`, `modify`, `move`, `operations`, `point`, `points`, `privileged`, `public`, `pure`, `reports`, `restricted`, `role`, `role-restricted`, `rust`, `security`, `smart`, `solana`, `solidity`, `state`, `state-changing`, `structured`, `them`, `ton`, `view`, `vyper`

## journal-entry

Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation or amortization, posting revenue recognition or deferred revenue adjustments, or documenting an entry for audit review.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry`
- **Skill file**: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry/SKILL.md`
- **Tags**: `accruals`, `adjustments`, `amortization`, `audit`, `booking`, `credits`, `debits`, `deferred`, `depreciation`, `detail`, `documenting`, `end`, `entries`, `entry`, `finance`, `journal`, `journal-entry`, `month`, `month-end`, `payroll`, `posting`, `prepaid`, `prepare`, `proper`, `recognition`, `recording`, `revenue`, `review`, `supporting`

## journal-entry-prep

Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed asset depreciation, payroll entries, revenue recognition, or any manual journal entry.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/finance/skills/journal-entry-prep/SKILL.md`
- **Tags**: `accruals`, `amortization`, `asset`, `booking`, `close`, `credits`, `debits`, `depreciation`, `documentation`, `end`, `entries`, `entry`, `finance`, `fixed`, `journal`, `journal-entry-prep`, `manual`, `month`, `month-end`, `payroll`, `prep`, `prepaid`, `prepare`, `proper`, `recognition`, `revenue`, `supporting`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`

## virtual-agent/web

Zoom Virtual Agent SDK for web embeds. Use for campaign or entry ID chat launch, event-driven controls, user context updates, and CSP-safe deployment.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/web/SKILL.md`
- **Tags**: `campaign`, `chat`, `context`, `controls`, `csp`, `csp-safe`, `deployment`, `driven`, `embeds`, `entry`, `event`, `event-driven`, `launch`, `partner`, `safe`, `sdk`, `updates`, `virtual`, `web`, `zoom`
