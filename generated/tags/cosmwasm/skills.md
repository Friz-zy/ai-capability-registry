# cosmwasm

## Skills
Load skill and **use it** when task matches.

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `../external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
