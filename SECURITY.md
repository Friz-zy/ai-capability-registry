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

Agents discover capabilities via routing catalogs with progressive disclosure:

### Skills

```
skills/skills.md (root)
-> skills/catalog/tasks/<task>/skills.md (task routing catalog)
-> skills/catalog/roles/<role>/skills.md (optional role routing catalog)
-> skills/catalog/keywords/<keyword>/skills.md (keyword catalog with skill descriptions)
-> external/<source>/<path>/SKILL.md (actual skill)
```

### MCP

```
mcp/mcp.md (root with resolution protocol)
-> mcp/web.md | mcp/docker.md | mcp/common.md (runtime connector guides)
-> mcp/catalog/tasks/<task>/servers.md (task routing catalog)
-> mcp/catalog/roles/<role>/servers.md (optional role routing catalog)
-> mcp/catalog/runtime/<runtime>/servers.md (runtime routing catalog)
-> mcp/catalog/keywords/<keyword>/servers.md (keyword routing catalog)
-> mcp/servers/<server>/SKILL.md (generated MCP usage wrapper)
```

`skills/packs/` contains symlink packs for direct inclusion in agent configs and is not used for runtime skill selection.

MCP connectors (`mcp/web.md`, `mcp/docker.md`, `mcp/common.md`) describe transport modes and diagnostics. They are generated alongside routing catalogs from `templates/mcp/` and should not be edited directly.

## Reporting Issues

Open a private security advisory or contact the repository owner before publishing exploit details.
