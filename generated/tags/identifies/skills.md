# identifies

## Skills
Load skill file when task matches.

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

File: `../external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`

### supply-chain-risk-auditor
Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements.

File: `../external/trailofbits-skills/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`

### zeroize-audit
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

File: `../external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
