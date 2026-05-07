# Tag: protocol

Skills with tag `protocol`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## crypto-protocol-diagram

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`
- **Tags**: `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`, `cryptographic`, `diagram`, `diagramming`, `diagrams`, `double`, `drawing`, `ecdh`, `exchange`, `extracting`, `extracts`, `flow`, `frost`, `generates`, `handshake`, `informal`, `key`, `mermaid`, `message`, `model`, `models`, `noise`, `papers`, `prose`, `protocol`, `protocols`, `proverif`, `pseudocode`, `ratchet`, `rfc`, `rfcs`, `sequence`, `sequencediagrams`, `signal`, `spec`, `spthy`, `tamarin`, `tls`, `trailmark`, `visualizing`, `x3dh`

## dimensional-analysis

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md`
- **Tags**: `analysis`, `annotate`, `annotates`, `arithmetic`, `asks`, `blockchain`, `bugs`, `catches`, `code`, `codebase`, `codebases`, `comments`, `decimal`, `defi`, `dimensional`, `dimensional-analysis`, `dimensions`, `documenting`, `early`, `find`, `formula`, `mismatches`, `offchain`, `other`, `perform`, `prevents`, `protocol`, `scaling`, `someone`, `units`, `vulnerabilities`

## mcp-builder

Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/mcp-builder`
- **Skill file**: `external/anthropic-skills/skills/mcp-builder/SKILL.md`
- **Tags**: `apis`, `builder`, `building`, `context`, `creating`, `designed`, `enable`, `fastmcp`, `high`, `high-quality`, `integrate`, `interact`, `llms`, `mcp`, `mcp-builder`, `model`, `node`, `protocol`, `python`, `quality`, `sdk`, `servers`, `services`, `typescript`, `well`, `well-designed`, `whether`

## mcp-integration

This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/mcp-integration/SKILL.md`
- **Tags**: `asks`, `code`, `comprehensive`, `configure`, `connect`, `context`, `dev`, `discusses`, `guidance`, `http`, `integrate`, `integrating`, `integration`, `mcp`, `mcp-integration`, `mentions`, `model`, `protocol`, `provides`, `root`, `server`, `servers`, `service`, `set`, `sse`, `stdio`, `types`, `used`, `websocket`

## mermaid-to-proverif

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`
- **Tags**: `attacks`, `authentication`, `checking`, `converting`, `cryptographic`, `describing`, `diagram`, `formal`, `formally`, `forward`, `generating`, `mermaid`, `mermaid-to-proverif`, `model`, `models`, `producing`, `properties`, `protocol`, `protocols`, `proverif`, `replay`, `secrecy`, `security`, `sequence`, `sequencediagrams`, `trailmark`, `translates`, `verification`, `verifying`

## spec-to-code-compliance

Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding gaps between specs and implementation, or performing compliance checks for protocol implementations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance`
- **Skill file**: `external/trailofbits-skills/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`
- **Tags**: `against`, `audits`, `between`, `blockchain`, `checks`, `code`, `comparing`, `compliance`, `documentation`, `exactly`, `finding`, `gaps`, `implementation`, `implementations`, `implements`, `performing`, `protocol`, `spec`, `spec-to-code-compliance`, `specifies`, `specs`, `verifies`, `whitepapers`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
