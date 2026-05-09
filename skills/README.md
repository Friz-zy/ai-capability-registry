# Generated Skills

This directory is generated from `registry/*.yaml` and `skill-catalog.d/*.yaml`. Do not edit generated indexes or symlinks manually.

- `skills.md` is the root routing index.
- `keywords/<keyword>/` contains a keyword catalog and symlinks for enabled skills matching a keyword from `registry/keyword-categories.yaml`.
- `roles/<profile-id>/` contains a role catalog and symlinks for enabled skills matching a role from `registry/profiles.yaml`.
- `tasks/<task-id>/` contains a task catalog and symlinks for enabled skills matching task keywords from `registry/tasks.yaml`.
- `all/` contains every existing enabled skill once.

Each entry is a symlink to the original skill directory under `external/`, named as `<repo-name>-<skill-name>`.
To change membership, edit `enabled` or `keywords` in provider chunks under `skill-catalog.d/`, or role/keyword definitions under `registry/`, then run:

```bash
python scripts/discover-skills.py
```
