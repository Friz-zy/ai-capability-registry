# Generated Skills

This directory is generated from `registry/*.yaml` and `skill-catalog.d/*.yaml`. Do not edit generated indexes or symlinks manually.

- `skills.md` is the root routing index.
- `catalog/` contains routing-only `skills.md` indexes for selecting relevant skills.
- `catalog/tasks/<task-id>/skills.md` contains task keywords from `registry/tasks.yaml`.
- `catalog/roles/<profile-id>/skills.md` contains role keywords from `registry/profiles.yaml`.
- `catalog/keywords/<keyword>/skills.md` contains skill descriptions and source `SKILL.md` paths.
- `packs/` contains symlink packs for direct inclusion in agent configs.
- `packs/all/` contains every existing enabled skill once.

Skill paths are relative to the registry root. `external/` is a sibling of the root `skills/` directory, not a child of it.
Each `packs/` entry is a symlink to the original skill directory under `external/`, named as `<repo-name>-<skill-name>`.
To change membership, edit provider chunks under `skill-catalog.d/` or role/keyword definitions under `registry/`, then run:

```bash
python scripts/discover-skills.py
```
