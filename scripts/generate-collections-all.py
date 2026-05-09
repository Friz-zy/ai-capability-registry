#!/usr/bin/env python3
"""Generate skills/all directly from enabled provider catalog chunks."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from registry_lib import load_yaml  # noqa: E402

CATALOG_DIR = ROOT / "skill-catalog.d"
ALL_DIR = ROOT / "skills" / "all"


def reset_all_dir() -> None:
    if ALL_DIR.exists() or ALL_DIR.is_symlink():
        if ALL_DIR.is_dir() and not ALL_DIR.is_symlink():
            shutil.rmtree(ALL_DIR)
        else:
            ALL_DIR.unlink()
    ALL_DIR.mkdir(parents=True, exist_ok=True)


def safe_link_name(source: str, name: str, path: str) -> str:
    fallback = Path(path).name
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-") or fallback
    return f"{source}-{safe_name}"


def enabled_catalog_entries() -> list[dict[str, Any]]:
    if not CATALOG_DIR.exists():
        raise SystemExit(f"Missing catalog directory: {CATALOG_DIR}")

    entries = []
    seen_ids: set[str] = set()
    for catalog_file in sorted(CATALOG_DIR.glob("*.yaml")):
        data = load_yaml(catalog_file)
        if not isinstance(data, dict):
            raise SystemExit(f"Catalog chunk must be a mapping: {catalog_file}")
        default_source = str(data.get("source") or catalog_file.stem)
        for item in data.get("skills", []):
            if not isinstance(item, dict):
                continue
            entry_id = item.get("path") or item.get("id")
            if isinstance(entry_id, str):
                if entry_id in seen_ids:
                    raise SystemExit(f"Duplicate catalog entry {entry_id} in {catalog_file}")
                seen_ids.add(entry_id)
            if (
                not item.get("enabled", False)
                or not item.get("exists", True)
            ):
                continue
            source = item.get("source") or default_source
            name = item.get("name")
            path = item.get("path")
            if not all(isinstance(value, str) for value in (source, name, path)):
                continue
            entry = dict(item)
            entry["source"] = source
            entries.append(entry)
    return entries


def add_link(entry: dict[str, Any], used_names: dict[str, Path], used_targets: set[Path]) -> bool:
    source = str(entry["source"])
    name = str(entry["name"])
    rel_path = str(entry["path"])
    target_abs = (ROOT / rel_path).resolve(strict=False)

    if target_abs in used_targets:
        return False
    if not (target_abs / "SKILL.md").exists():
        raise SystemExit(f"Catalog entry does not point to a skill directory: {rel_path}")

    base_name = safe_link_name(source, name, rel_path)
    final_name = base_name
    suffix = 2
    while final_name in used_names and used_names[final_name] != target_abs:
        final_name = f"{base_name}-{suffix}"
        suffix += 1

    if final_name in used_names and used_names[final_name] == target_abs:
        return False

    target_rel = os.path.relpath(target_abs, ALL_DIR)
    (ALL_DIR / final_name).symlink_to(target_rel, target_is_directory=True)
    used_names[final_name] = target_abs
    used_targets.add(target_abs)
    return True


def main() -> int:
    reset_all_dir()
    used_names: dict[str, Path] = {}
    used_targets: set[Path] = set()
    created = 0

    for entry in sorted(enabled_catalog_entries(), key=lambda e: (str(e.get("source")), str(e.get("name")), str(e.get("path")))):
        if add_link(entry, used_names, used_targets):
            created += 1

    print(f"Generated {ALL_DIR.relative_to(ROOT)} with {created} symlinks from skill-catalog.d")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
