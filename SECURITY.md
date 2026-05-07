# Security Policy

This project curates AI skills, MCP servers, workflows, and agent integrations for secure multi-agent development.

## Security Model

- Registry entries are declarative metadata in `registry/skills.yaml`
- External sources are pinned git submodules with verified commit hashes
- Generated skill maps are derived from trusted/reviewed sources only
- MCP servers must use hosted HTTPS/OAuth or Docker isolation
- Local arbitrary execution is denied by default
- Read-only and ask-before-write modes are preferred

## Trust Levels

| Level | Description | Auto-indexed | Auto-enabled |
|-------|-------------|--------------|--------------|
| `trusted` | Official vendor or reputable security-reviewed | Yes | Yes |
| `reviewed` | Manually reviewed source | Yes | No (manual) |
| `candidate` | Discovery-only, not reviewed | No | No |

## Source Synchronization

External submodules are synchronized with `registry/skills.yaml` via:

```bash
./scripts/update-external.py  # Sync submodules to pinned commits
./scripts/bootstrap.sh         # Full sync + generate skill maps
```

CI automatically syncs when `registry/skills.yaml` is modified.

## Denied Patterns

- `curl | sh` installation
- Global random package execution (e.g., `npm install -g random-mcp`)
- Unknown `python server.py` MCP runtimes
- Unrestricted shell MCP servers
- Unrestricted filesystem access
- Browser automation without sandboxing

## Capability Discovery

Agents discover capabilities via cascading skill maps:

```
generated/agents.md.template → generated/skills.md (root)
→ generated/roles/<role>/skills.md (delegates to tags)
→ generated/tags/<tag>/skills.md (skill listings)
→ external/<source>/<path>/SKILL.md (actual skill)
```

## Reporting Issues

Open a private security advisory or contact the repository owner before publishing exploit details.
