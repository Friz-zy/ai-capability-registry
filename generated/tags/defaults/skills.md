# defaults

## Skills
Load skill file when task matches.

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

File: `../external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

File: `../external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
