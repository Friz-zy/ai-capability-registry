# Tag: detects

Skills with tag `detects`:

## agentic-actions-auditor

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor`
- **Skill file**: `external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`
- **Tags**: `actions`, `agentic`, `agentic-actions-auditor`, `allowlists`, `attack`, `attacker`, `attacker-controlled`, `auditing`, `auditor`, `audits`, `cli`, `code`, `codex`, `coding`, `configurations`, `controlled`, `dangerous`, `detects`, `direct`, `env`, `evaluating`, `expression`, `gemini`, `github`, `including`, `inference`, `injection`, `input`, `integrations`, `intermediary`, `invoke`, `pipeline`, `pipelines`, `prompt`, `reaches`, `reviewing`, `risks`, `running`, `sandbox`, `security`, `var`, `vectors`, `vulnerabilities`, `where`, `wildcard`

## constant-time-analysis

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`
- **Tags**: `analysis`, `branches`, `channel`, `code`, `constant`, `constant-time`, `constant-time-analysis`, `crypto`, `cryptographic`, `dependent`, `detects`, `division`, `encountering`, `implementing`, `java`, `javascript`, `kotlin`, `php`, `programming`, `python`, `questions`, `reviewing`, `ruby`, `rust`, `secret`, `secret-dependent`, `secrets`, `side`, `side-channel`, `swift`, `time`, `timing`, `typescript`, `vulnerabilities`

## entry-point-analyzer

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer`
- **Skill file**: `external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`
- **Tags**: `access`, `admin`, `analyzer`, `analyzes`, `asked`, `audit`, `auditing`, `callable`, `categorizes`, `changing`, `codebases`, `contract`, `contracts`, `control`, `cosmwasm`, `detects`, `entry`, `entry-point-analyzer`, `excludes`, `externally`, `find`, `flows`, `functions`, `generates`, `identify`, `level`, `modify`, `move`, `operations`, `point`, `points`, `privileged`, `public`, `pure`, `reports`, `restricted`, `role`, `role-restricted`, `rust`, `security`, `smart`, `solana`, `solidity`, `state`, `state-changing`, `structured`, `them`, `ton`, `view`, `vyper`

## insecure-defaults

Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults`
- **Skill file**: `external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- **Tags**: `allow`, `analyzing`, `apps`, `auditing`, `auth`, `config`, `defaults`, `detects`, `environment`, `fail`, `fail-open`, `handling`, `hardcoded`, `insecure`, `insecure-defaults`, `insecurely`, `management`, `open`, `permissive`, `production`, `reviewing`, `secrets`, `security`, `variable`, `weak`

## source-management

Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages rate limiting awareness.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/source-management/SKILL.md`
- **Tags**: `awareness`, `connect`, `connected`, `detects`, `enterprise`, `enterprise-search`, `guides`, `handles`, `limiting`, `management`, `manages`, `mcp`, `ones`, `ordering`, `priority`, `rate`, `search`, `sources`

## zeroize-audit

Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit`
- **Skill file**: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
- **Tags**: `analysis`, `assembly`, `assembly-level`, `audit`, `auditing`, `code`, `compiler`, `control`, `control-flow`, `data`, `detects`, `flow`, `handling`, `identifies`, `keys`, `level`, `missing`, `optimizations`, `other`, `passwords`, `removed`, `rust`, `secrets`, `sensitive`, `verification`, `zeroization`, `zeroize`, `zeroize-audit`
