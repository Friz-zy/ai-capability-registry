#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path

from registry_lib import GENERATED_DIR, ROOT, load_all, write_text


def main() -> int:
    registry = load_all()
    links_dir = GENERATED_DIR / "links"
    links_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[str] = ["# Artifact Links", "", "Symlinks are created only when external sources are present locally.", ""]

    created = 0
    skipped = 0
    for skill in registry["skills"]:
        source = skill.get("source", {})
        external_path = source.get("external_path")
        if not external_path:
            continue
        target = ROOT / external_path
        link = links_dir / skill["id"]
        if target.exists():
            if link.exists() or link.is_symlink():
                link.unlink()
            os.symlink(os.path.relpath(target, link.parent), link)
            created += 1
            manifest.append(f"- `{skill['id']}` -> `{external_path}`")
        else:
            skipped += 1
            manifest.append(f"- `{skill['id']}` skipped; missing `{external_path}`")

    write_text(links_dir / "README.md", "\n".join(manifest))
    print(f"Artifact links complete: {created} created, {skipped} skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
