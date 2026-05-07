# token

## Skills
Load skill file when task matches.

### configure
Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`

### configure
Set up the Telegram channel — save the bot token and review access policy. Use when the user pastes a Telegram bot token, asks to configure Telegram, asks "how do I set this up" or "who can reach me," or wants to check channel status.

File: `../external/anthropic-claude-plugins-official/external_plugins/telegram/skills/configure/SKILL.md`

### secure-workflow-guide
Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

### setup-zoom-oauth
Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging auth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md`

### token-integration-analyzer
Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Context-aware for both token implementations and token integrations.

File: `../external/trailofbits-skills/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

### zoom-oauth
Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or debugging Zoom OAuth failures.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/oauth/SKILL.md`
