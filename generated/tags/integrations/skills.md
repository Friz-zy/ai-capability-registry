# integrations

## Skills
Load skill and **use it** when task matches.

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

File: `../external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### build-zoom-contact-center-app
Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context and state handling; campaigns; callbacks; or version-drift troubleshooting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/SKILL.md`

### build-zoom-team-chat-app
Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, buttons, slash commands, or chat webhooks.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/team-chat/SKILL.md`

### build-zoom-virtual-agent
Reference skill for Zoom Virtual Agent. Use after routing to a virtual-agent workflow when implementing web embeds, Android or iOS wrapper integrations, knowledge-base sync, lifecycle handling, or troubleshooting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/virtual-agent/SKILL.md`

### contact-center/android
Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/android/SKILL.md`

### contact-center/ios
Zoom Contact Center SDK for iOS. Use for native iOS chat/video/ZVA/scheduled callback integrations, app lifecycle bridging, rejoin flow, and callback handling.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/ios/SKILL.md`

### contact-center/web
Zoom Contact Center SDK for Web. Use for web chat/video/campaign embeds, engagement event handling, app-context integrations, and Smart Embed postMessage workflows.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/contact-center/web/SKILL.md`

### cosmos-vulnerability-scanner
Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

### skill-creator
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations.

File: `../external/openai-skills/skills/.system/skill-creator/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`
