# Contributing

This registry is security-first. New capabilities are indexed before they are enabled.

## Contribution Flow

1. Add or update entries in `registry/skills.yaml` (trusted/reviewed sources only)
2. Pin upstream sources with a specific commit hash (required for trusted status)
3. Set `enabled: true` only for reviewed sources; use `enabled: false` for candidate
4. Run `./scripts/bootstrap.sh` to sync submodules and regenerate skill maps
5. CI will auto-commit the generated changes if `registry/skills.yaml` is modified
6. Review the generated `skills/skills.md` and `skills/catalog/` catalogs

## Adding New Sources

```yaml
# In registry/skills.yaml
- id: my-source
  name: My Source
  trust:
    level: candidate  # Start as candidate, promote after review
    reviewed: false
  enabled: false  # Disabled by default
  version:
    commit: <specific-sha>  # Required
    pinned: true
```

## Trust Levels

- `trusted`: Official vendor or security-reviewed. Used by default.
- `reviewed`: Manually reviewed by maintainer. Available on request.
- `candidate`: Discovery-only. Not installed by default.

## Capability Rules

- Do not add `curl | sh`, random `npx`, or arbitrary local execution paths
- Prefer hosted HTTPS/OAuth or Docker-isolated runtimes
- Do not enable community sources by default without manual review
- Keep generated files generated; edit registry YAML instead

## Generated Artifacts

The following are auto-generated and should NOT be edited manually:

- `skill-catalog.md` — Human-readable view of `skill-catalog.d/`
- `skills/skills.md` — Skill runtime instructions and scoped selection protocol
- `skills/routing.md` — Root skill routing index with all roles and tasks
- `skills/catalog/roles/<id>/skills.md` — Role routing catalogs
- `skills/catalog/tasks/<id>/skills.md` — Task routing catalogs
- `skills/catalog/keywords/<keyword>/skills.md` — Keyword catalogs with skill descriptions
- `skills/packs/` — Symlink packs for direct agent config inclusion
- `mcp-catalog.md` — Human-readable view of `mcp-catalog.d/`
- `mcp/mcp.md` — MCP runtime instructions, transport guidance, and safety rules
- `mcp/routing.md` — Root MCP routing index with roles and tasks
- `mcp/web.md` — HTTPS/SSE MCP connector guide
- `mcp/docker.md` — Docker MCP connector guide
- `mcp/common.md` — General MCP concepts and diagnostics
- `mcp/catalog/roles/<id>/servers.md` — Role MCP routing catalogs
- `mcp/catalog/tasks/<id>/servers.md` — Task MCP routing catalogs
- `mcp/catalog/runtime/<runtime>/servers.md` — Runtime MCP routing catalogs
- `mcp/catalog/keywords/<keyword>/servers.md` — Keyword MCP routing catalogs
- `mcp/servers/<server>/SKILL.md` — Generated MCP usage wrapper
- `mcp/servers/<server>/connection.json` — Generated MCP connection config
- `workflows/workflow.md` — Workflow runtime instructions and coordination protocol
- `workflows/routing.md` — Root workflow routing index with all workflows
- `workflows/catalog/**/workflows.md` — Route-specific workflow routing catalogs

## Resolution Chains

### Skills

```
registry/skills.yaml → update-external.py (sync submodules) 
→ discover-skills.py (generate maps) → skills/skills.md + skills/routing.md → agents use cascades
```

### MCP

```
mcp-catalog.d/*.yml → generate-mcp.py (generate indexes)
→ mcp/mcp.md + mcp/routing.md → mcp/web.md | mcp/docker.md → mcp/servers/<server>/SKILL.md
```

### Workflows

```
registry/workflows.yaml → generate-workflows.py
→ workflows/workflow.md + workflows/routing.md → workflows/<category>/<workflow>/workflow.md
```
