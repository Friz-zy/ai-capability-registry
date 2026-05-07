# Install Scripts

Run `<agent>.sh --profile <profile>` to populate `generated/active/` and `generated/configs/` after pin verification.

Multiple profiles are supported:

```bash
generated/install-scripts/kilo-code.sh --profile personal-assistant software-engineer
generated/install-scripts/kilo-code.sh --profile personal-assistant --profile data-analyst
generated/install-scripts/kilo-code.sh --profile personal-assistant,software-engineer
generated/install-scripts/kilo-code.sh --all-profiles
```
