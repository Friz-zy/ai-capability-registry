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

- `skills/skills.md` - Root routing index with all roles and tasks
- `skills/catalog/roles/<id>/skills.md` - Role routing catalogs
- `skills/catalog/tasks/<id>/skills.md` - Task routing catalogs
- `skills/catalog/keywords/<keyword>/skills.md` - Keyword catalogs with skill descriptions
- `skills/packs/` - Symlink packs for direct agent config inclusion

## Skill Resolution Chain

```
registry/skills.yaml → update-external.py (sync submodules) 
→ discover-skills.py (generate maps) → skills/skills.md → agents use cascades
```
