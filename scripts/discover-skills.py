#!/usr/bin/env python3
"""
Generates skill routing catalogs and symlink packs organized by keywords, roles, and tasks.
Generates absolute paths for portability across machines.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

from registry_lib import ROOT, SKILLS_DIR, load_all, load_yaml, write_text


IGNORED_PARTS = {".git", "tests", "fixtures", "template", "node_modules", "__pycache__"}
SKILL_CATALOG_DIR = ROOT / "skill-catalog.d"
SKILLS_CATALOG_DIR = SKILLS_DIR / "catalog"
SKILLS_PACKS_DIR = SKILLS_DIR / "packs"
LEGACY_OUTPUT_DIRS = (ROOT / "generated", ROOT / "collections")
STOPWORDS = {
    "about", "across", "action", "add", "after", "agent", "agents", "all", "also", "always",
    "and", "any", "are", "assistant", "available", "based", "before", "best", "built", "check",
    "common", "contents", "current", "details", "does", "each", "example", "examples", "external",
    "file", "files", "first", "for", "from", "generate", "generated", "get", "guide", "help", "how",
    "index", "into", "json", "known", "list", "name", "need", "new", "not", "official", "only",
    "output", "overview", "pattern", "patterns", "plugin", "plugins", "prerequisites", "quick", "read",
    "reference", "references", "related", "required", "resources", "results", "rules", "run", "scripts",
    "see", "setup", "should", "skill", "skills", "source", "specific", "step", "steps", "system", "table",
    "task", "tasks", "template", "templates", "that", "the", "this", "through", "tool", "tools", "type",
    "update", "usage", "use", "user", "users", "uses", "using", "via", "wants", "what", "when", "with",
    "work", "workflow", "workflows", "works", "write", "writing", "you", "your",
    "anthropic", "claude", "openai", "trailofbits", "trail", "bits", "awesome", "composio", "alirezarezvani",
}


def abs_path(path: Path) -> str:
    """Absolute path."""
    return str(path.absolute())


def rel_from_root(path: Path) -> str:
    """Relative path from registry root."""
    return path.relative_to(ROOT).as_posix()


def should_skip(path: Path) -> bool:
    return bool(set(path.parts) & IGNORED_PARTS)


def read_skill_bytes(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError:
        return b""


def normalize_skill_text(raw: bytes) -> str:
    return raw.decode("utf-8", errors="replace").replace("\r\n", "\n")


def extract_frontmatter_block(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    header = text[4:end]
    lines = [line.rstrip() for line in header.splitlines()]
    while lines and not lines[-1].strip():
        lines.pop()
    normalized = "\n".join(lines).strip()
    return normalized or None


def parse_frontmatter_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return value
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def parse_frontmatter_inline_list(value: str) -> list[str] | None:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [parse_frontmatter_scalar(item.strip()) for item in inner.split(",") if item.strip()]


def dedent_block_lines(lines: list[str]) -> list[str]:
    indents = [len(line) - len(line.lstrip(" ")) for line in lines if line.strip()]
    if not indents:
        return []
    indent = min(indents)
    return [line[indent:] if len(line) >= indent else "" for line in lines]


def parse_frontmatter_block_scalar(indicator: str, lines: list[str]) -> str:
    dedented = dedent_block_lines(lines)
    if indicator.startswith("|"):
        value = "\n".join(dedented)
    else:
        paragraphs: list[str] = []
        current: list[str] = []
        for line in dedented:
            if line.strip():
                current.append(line.strip())
            elif current:
                paragraphs.append(" ".join(current))
                current = []
        if current:
            paragraphs.append(" ".join(current))
        value = "\n\n".join(paragraphs)

    if indicator.endswith("+"):
        return value + "\n"
    return value.rstrip("\n")


def parse_skill_frontmatter_text(text: str) -> dict[str, Any]:
    header = extract_frontmatter_block(text)
    if not header:
        return {}
    values: dict[str, Any] = {}

    lines = header.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not stripped or stripped.startswith("#") or indent != 0 or ":" not in line:
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if re.fullmatch(r"[>|][+-]?", value):
            block_lines: list[str] = []
            index += 1
            while index < len(lines):
                next_line = lines[index]
                next_indent = len(next_line) - len(next_line.lstrip(" "))
                if next_line.strip() and next_indent <= indent:
                    break
                block_lines.append(next_line)
                index += 1
            values[key] = parse_frontmatter_block_scalar(value, block_lines)
            continue

        if value == "":
            child_lines: list[str] = []
            index += 1
            while index < len(lines):
                next_line = lines[index]
                next_indent = len(next_line) - len(next_line.lstrip(" "))
                if next_line.strip() and next_indent <= indent:
                    break
                child_lines.append(next_line)
                index += 1
            values[key] = parse_frontmatter_nested_block(child_lines)
            continue

        inline_list = parse_frontmatter_inline_list(value)
        values[key] = inline_list if inline_list is not None else parse_frontmatter_scalar(value)
        index += 1
    return values


def parse_frontmatter_nested_block(lines: list[str]) -> Any:
    dedented = dedent_block_lines(lines)
    if not dedented:
        return {}
    if all(not line.strip() or line.lstrip().startswith("- ") for line in dedented):
        return [parse_frontmatter_scalar(line.lstrip()[2:].strip()) for line in dedented if line.strip()]

    values: dict[str, Any] = {}
    index = 0
    while index < len(dedented):
        line = dedented[index]
        stripped = line.strip()
        indent = len(line) - len(line.lstrip(" "))
        if not stripped or stripped.startswith("#") or indent != 0 or ":" not in line:
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            child_lines: list[str] = []
            index += 1
            while index < len(dedented):
                next_line = dedented[index]
                next_indent = len(next_line) - len(next_line.lstrip(" "))
                if next_line.strip() and next_indent <= indent:
                    break
                child_lines.append(next_line)
                index += 1
            values[key] = parse_frontmatter_nested_block(child_lines)
            continue
        inline_list = parse_frontmatter_inline_list(value)
        values[key] = inline_list if inline_list is not None else parse_frontmatter_scalar(value)
        index += 1
    return values


def parse_skill_frontmatter(path: Path) -> dict[str, Any]:
    return parse_skill_frontmatter_text(normalize_skill_text(read_skill_bytes(path)))


def skill_content_hash(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def extract_keywords(*values: Any) -> list[str]:
    text = " ".join(
        str(item) if not isinstance(item, list) else " ".join(str(i) for i in item)
        for item in values
        if item is not None
    ).lower().replace("_", "-")
    keywords: set[str] = set()
    for token in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text):
        if token.isdigit() or len(token) < 3:
            continue
        parts = [p for p in token.split("-") if p and p not in STOPWORDS and not p.isdigit()]
        if not parts:
            continue
        keywords.update(p for p in parts if len(p) > 2)
        if len(parts) > 1:
            keywords.add("-".join(parts))
    return sorted(keywords)


def normalize_declared_keyword(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        keywords: list[str] = []
        for item in value:
            keywords.extend(normalize_declared_keyword(item))
        return keywords
    if isinstance(value, dict):
        return []

    text = str(value).strip()
    if not text:
        return []

    parts = [part.strip() for part in text.split(",") if part.strip()]
    if len(parts) > 1:
        keywords: list[str] = []
        for part in parts:
            keywords.extend(normalize_declared_keyword(part))
        return keywords

    keyword = re.sub(r"[^a-z0-9]+", "-", text.lower().replace("_", "-")).strip("-")
    if not keyword or keyword in STOPWORDS or len(keyword) < 3:
        return []
    return [keyword]


def frontmatter_declared_keywords(frontmatter: dict[str, Any]) -> list[str]:
    declared: set[str] = set()
    for container in (frontmatter, frontmatter.get("metadata") if isinstance(frontmatter.get("metadata"), dict) else {}):
        if not isinstance(container, dict):
            continue
        for key in ("keywords", "tags", "category", "categories"):
            values = normalize_declared_keyword(container.get(key))
            declared.update(values)
            declared.update(extract_keywords(values))
    return sorted(declared)


def build_keyword_to_categories(keyword_categories: dict[str, list[str]]) -> dict[str, str]:
    keyword_to_category: dict[str, str] = {}
    for category, keywords in keyword_categories.items():
        for keyword in keywords:
            keyword_to_category[keyword] = category
    return keyword_to_category


def registry_keywords(keyword_categories: dict[str, list[str]]) -> list[str]:
    keywords: set[str] = set()
    for values in keyword_categories.values():
        keywords.update(str(keyword) for keyword in values)
    return sorted(keyword for keyword in keywords if keyword)


def get_keywords_for_categories(categories: list[str], keyword_categories: dict[str, list[str]]) -> list[str]:
    keywords: set[str] = set()
    for cat in categories:
        if cat in keyword_categories:
            keywords.update(keyword_categories[cat])
    return sorted(keywords)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def append_yaml_list(lines: list[str], key: str, values: list[str], indent: str = "    ") -> None:
    if not values:
        lines.append(f"{indent}{key}: []")
        return
    lines.append(f"{indent}{key}:")
    lines.extend(f"{indent}  - {yaml_string(value)}" for value in values)


def build_skills_by_keyword(skills: list["SkillRecord"], allowed_keywords: set[str]) -> dict[str, list["SkillRecord"]]:
    skills_by_keyword: dict[str, list[SkillRecord]] = defaultdict(list)
    for skill in skills:
        for keyword in skill.keywords:
            if keyword not in allowed_keywords:
                continue
            skills_by_keyword[keyword].append(skill)
    return skills_by_keyword


class SkillRecord:
    def __init__(
        self,
        source_id: str,
        source_trust: str,
        skill_dir: Path,
        skill_file: Path,
        name: str,
        description: str,
        keywords: list[str],
        declared_keywords: list[str] | None = None,
    ):
        self.source_id = source_id
        self.source_trust = source_trust
        self.skill_dir = skill_dir
        self.skill_file = skill_file
        self.name = name
        self.description = description
        self.keywords = keywords
        self.declared_keywords = declared_keywords or []
        self.abs_file = abs_path(skill_file)
        self.rel_file = rel_from_root(skill_file)
        self.rel_dir = rel_from_root(skill_dir)
        self.skill_id = self.rel_dir

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "keywords": self.keywords,
            "skill_file": self.abs_file,
            "source": self.source_id,
            "trust": self.source_trust,
        }


def normalize_catalog_id(item: dict[str, Any]) -> str | None:
    path = item.get("path")
    skill_id = path if isinstance(path, str) and path else item.get("id")
    if not isinstance(skill_id, str) or not skill_id:
        return None
    if ":external/" in skill_id:
        # Backward compatibility with previous IDs formatted as `<source>:external/...`.
        skill_id = skill_id.split(":", 1)[1]
    return skill_id


def normalize_string_list(value: Any) -> list[str] | None:
    if isinstance(value, list):
        return sorted({str(item) for item in value if str(item)})
    if isinstance(value, str):
        return sorted({item.strip() for item in value.split(",") if item.strip()})
    return None


def catalog_source_slug(source: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", source.strip()).strip("-")
    return slug or "unknown"


def normalize_catalog_entry(item: dict[str, Any], default_source: str = "") -> dict[str, Any] | None:
    skill_id = normalize_catalog_id(item)
    if not skill_id:
        return None

    keywords = normalize_string_list(item.get("keywords"))
    if keywords is None:
        # Backward compatibility: old catalogs stored auto-extracted keywords in `tags`.
        keywords = normalize_string_list(item.get("tags")) or []

    source = str(item.get("source") or default_source or "")
    return {
        "id": skill_id,
        "exists": bool(item.get("exists", True)),
        "enabled": bool(item.get("enabled", False)),
        "name": str(item.get("name") or Path(skill_id).name),
        "description": str(item.get("description") or ""),
        "source": source,
        "path": str(item.get("path") or skill_id),
        "skill_file": str(item.get("skill_file") or f"{skill_id}/SKILL.md"),
        "keywords": keywords,
    }


def load_skill_catalog_entries_from_file(path: Path) -> dict[str, dict[str, Any]]:
    data = load_yaml(path)
    entries: dict[str, dict[str, Any]] = {}
    if not isinstance(data, dict):
        return entries

    default_source = str(data.get("source") or path.stem)
    for item in data.get("skills", []):
        if not isinstance(item, dict):
            continue
        entry = normalize_catalog_entry(item, default_source)
        if entry is None:
            continue
        entries[str(entry["id"])] = entry
    return entries


def load_skill_catalog_entries() -> tuple[dict[str, dict[str, Any]], bool]:
    entries: dict[str, dict[str, Any]] = {}
    if SKILL_CATALOG_DIR.exists():
        for catalog_file in sorted(SKILL_CATALOG_DIR.glob("*.yaml")):
            chunk_entries = load_skill_catalog_entries_from_file(catalog_file)
            duplicate_ids = sorted(set(entries).intersection(chunk_entries))
            if duplicate_ids:
                duplicate_list = ", ".join(duplicate_ids[:5])
                raise ValueError(f"Duplicate skill catalog entries in {catalog_file}: {duplicate_list}")
            entries.update(chunk_entries)
        return entries, True

    return entries, False


def write_skill_catalog_chunk_entries(entries: list[dict[str, Any]]) -> None:
    SKILL_CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    lines_by_source: dict[str, list[str]] = {}

    def sort_key(item: dict[str, Any]) -> tuple[bool, str, str, str]:
        return (
            not bool(item.get("exists", False)),
            str(item.get("source") or ""),
            str(item.get("name") or ""),
            str(item.get("path") or item.get("id") or ""),
        )

    for item in sorted(entries, key=sort_key):
        source = str(item.get("source") or "unknown")
        if source not in lines_by_source:
            lines_by_source[source] = [
                "# Auto-synced by scripts/discover-skills.py.",
                "# Edit `enabled` and `keywords`; other fields are refreshed from discovered skills when exists=true.",
                "# `keywords` are auto-filled only for newly discovered skills, then preserved for manual curation.",
                "# `exists=false` means the skill was previously cataloged but is absent from current external sources.",
                f"source: {yaml_string(source)}",
                "skills:",
            ]

        skill_id = str(item.get("id") or item.get("path") or "")
        lines = lines_by_source[source]
        lines.extend([
            f"  - id: {yaml_string(skill_id)}",
            f"    exists: {str(bool(item.get('exists', False))).lower()}",
            f"    enabled: {str(bool(item.get('enabled', False))).lower()}",
            f"    name: {yaml_string(str(item.get('name') or Path(skill_id).name))}",
            f"    description: {yaml_string(str(item.get('description') or 'No description.'))}",
            f"    source: {yaml_string(source)}",
            f"    path: {yaml_string(str(item.get('path') or skill_id))}",
            f"    skill_file: {yaml_string(str(item.get('skill_file') or f'{skill_id}/SKILL.md'))}",
        ])
        append_yaml_list(lines, "keywords", normalize_string_list(item.get("keywords")) or [])

    written_files: set[Path] = set()
    for source, lines in sorted(lines_by_source.items()):
        catalog_file = SKILL_CATALOG_DIR / f"{catalog_source_slug(source)}.yaml"
        write_text(catalog_file, "\n".join(lines))
        written_files.add(catalog_file)

    for stale_file in SKILL_CATALOG_DIR.glob("*.yaml"):
        if stale_file not in written_files:
            stale_file.unlink()


def registry_source_enabled_by_id(registry: dict[str, Any]) -> dict[str, bool]:
    return {
        item["id"]: bool(item.get("enabled"))
        for item in registry["skills"]
        if "id" in item
    }


def sync_skill_catalog(skills: list[SkillRecord], registry: dict[str, Any]) -> dict[str, bool]:
    previous_entries, had_catalog = load_skill_catalog_entries()
    skills_by_id = {skill.skill_id: skill for skill in skills}
    source_enabled = registry_source_enabled_by_id(registry)
    found_ids = set(skills_by_id)
    default_enabled = not had_catalog

    entries: list[dict[str, Any]] = []
    enabled_by_id: dict[str, bool] = {}

    for skill_id, skill in skills_by_id.items():
        previous = previous_entries.get(skill_id, {})
        has_previous_keywords = "keywords" in previous and isinstance(previous.get("keywords"), list)
        keywords = sorted(
            set(previous["keywords"] if has_previous_keywords else skill.keywords)
            .union(skill.declared_keywords)
        )
        enabled = bool(previous.get("enabled", default_enabled))
        entry = {
            "id": skill.skill_id,
            "exists": True,
            "enabled": enabled,
            "name": skill.name,
            "description": skill.description or "No description.",
            "source": skill.source_id,
            "path": skill.rel_dir,
            "skill_file": skill.rel_file,
            "keywords": keywords,
        }
        entries.append(entry)
        enabled_by_id[skill_id] = enabled

    for skill_id, previous in previous_entries.items():
        if skill_id in found_ids:
            continue
        entry = dict(previous)
        entry["id"] = skill_id
        entry["exists"] = False
        entry.setdefault("enabled", False)
        if source_enabled.get(str(entry.get("source") or "")) is False:
            entry["enabled"] = False
        entry.setdefault("name", Path(skill_id).name)
        entry.setdefault("description", "No description.")
        entry.setdefault("source", "")
        entry.setdefault("path", skill_id)
        entry.setdefault("skill_file", f"{skill_id}/SKILL.md")
        entry["keywords"] = normalize_string_list(entry.get("keywords")) or []
        entries.append(entry)

    added = sum(1 for skill_id in found_ids if skill_id not in previous_entries)
    removed = sum(1 for skill_id, item in previous_entries.items() if skill_id not in found_ids and item.get("exists", True))

    write_skill_catalog_chunk_entries(entries)

    if had_catalog:
        print(
            f"Synced skill-catalog.d: {len(entries)} cataloged skills "
            f"({len(found_ids)} exist, {added} added as disabled, {removed} marked exists=false, "
            f"{sum(enabled_by_id.values())} enabled and existing)"
        )
    else:
        print(
            f"Initialized skill-catalog.d: {len(skills)} existing skills "
            "enabled to preserve current behavior"
        )

    return enabled_by_id

def source_trust_by_id(registry: dict[str, Any]) -> dict[str, str]:
    return {
        item["id"]: item.get("trust", {}).get("level", "unknown")
        for item in registry["skills"]
        if "id" in item
    }


def load_skills_from_catalog(registry: dict[str, Any]) -> tuple[list[SkillRecord], dict[str, bool]]:
    catalog_entries, _ = load_skill_catalog_entries()

    trust_by_source = source_trust_by_id(registry)
    skills: list[SkillRecord] = []
    enabled_by_id: dict[str, bool] = {}

    for item in catalog_entries.values():
        if not isinstance(item, dict) or not bool(item.get("exists", True)):
            continue

        source_id = item.get("source")
        rel_path = item.get("path")
        rel_file = item.get("skill_file")
        skill_id = normalize_catalog_id(item)
        if not all(isinstance(value, str) for value in (source_id, rel_path, rel_file, skill_id)):
            continue

        skill_dir = ROOT / rel_path
        skill_file = ROOT / rel_file
        if not skill_file.exists():
            continue

        name = str(item.get("name") or skill_dir.name)
        description = str(item.get("description") or "")
        keywords = normalize_string_list(item.get("keywords"))
        if keywords is None:
            keywords = extract_keywords(rel_path, name, description) or ["uncategorized"]
        keywords = keywords or ["uncategorized"]

        record = SkillRecord(
            source_id=source_id,
            source_trust=trust_by_source.get(source_id, "unknown"),
            skill_dir=skill_dir,
            skill_file=skill_file,
            name=name,
            description=description,
            keywords=keywords,
        )
        skills.append(record)
        enabled_by_id[record.skill_id] = bool(item.get("enabled", False))

    return skills, enabled_by_id


def safe_link_name(skill: SkillRecord) -> str:
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", skill.name).strip("-") or skill.skill_dir.name
    return f"{skill.source_id}-{safe_name}"


def reset_collection_dir(path: Path) -> None:
    if path.exists() or path.is_symlink():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()
    path.mkdir(parents=True, exist_ok=True)


def add_collection_link(collection_dir: Path, skill: SkillRecord, used_names: dict[str, Path], used_targets: set[Path]) -> bool:
    target_abs = skill.skill_dir.resolve(strict=False)
    if target_abs in used_targets:
        return False

    base_name = safe_link_name(skill)
    final_name = base_name
    suffix = 2
    while final_name in used_names and used_names[final_name] != target_abs:
        final_name = f"{base_name}-{suffix}"
        suffix += 1

    if final_name in used_names and used_names[final_name] == target_abs:
        return False

    target_rel = os.path.relpath(target_abs, collection_dir)
    (collection_dir / final_name).symlink_to(target_rel, target_is_directory=True)
    used_names[final_name] = target_abs
    used_targets.add(target_abs)
    return True


def write_collection_links(collection_dir: Path, skills: list[SkillRecord]) -> int:
    collection_dir.mkdir(parents=True, exist_ok=True)
    used_names: dict[str, Path] = {}
    used_targets: set[Path] = set()
    created = 0
    for skill in sorted(skills, key=lambda s: (s.source_id, s.name, s.rel_dir)):
        if add_collection_link(collection_dir, skill, used_names, used_targets):
            created += 1
    return created


def skills_matching_keywords(skills: list[SkillRecord], keywords: list[str]) -> list[SkillRecord]:
    keyword_set = set(keywords)
    return [skill for skill in skills if keyword_set.intersection(skill.keywords)]


def write_skills_readme() -> None:
    content = """# Generated Skills

This directory is generated from `registry/*.yaml` and `skill-catalog.d/*.yaml`. Do not edit generated indexes or symlinks manually.

- `skills.md` is the root routing index.
- `catalog/` contains routing-only `skills.md` indexes for selecting relevant skills.
- `catalog/tasks/<task-id>/skills.md` contains task keywords from `registry/tasks.yaml`.
- `catalog/roles/<profile-id>/skills.md` contains role keywords from `registry/profiles.yaml`.
- `catalog/keywords/<keyword>/skills.md` contains skill descriptions and source `SKILL.md` paths.
- `packs/` contains symlink packs for direct inclusion in agent configs.
- `packs/all/` contains every existing enabled skill once.

Skill paths are relative to the registry root. The `external/` directory is a sibling of the root `skills/` directory, not a child of it.
Each `packs/` entry is a symlink to the original skill directory under `external/`, named as `<repo-name>-<skill-name>`.
To change membership, edit `enabled` or `keywords` in provider chunks under `skill-catalog.d/`, or role/keyword definitions under `registry/`, then run:

```bash
python scripts/discover-skills.py
```
"""
    write_text(SKILLS_DIR / "README.md", content)


def generate_collections(
    skills: list[SkillRecord],
    keyword_categories: dict[str, list[str]],
    profiles: list[dict[str, Any]],
    tasks: list[dict[str, Any]],
) -> None:
    packs_keywords_dir = SKILLS_PACKS_DIR / "keywords"
    packs_roles_dir = SKILLS_PACKS_DIR / "roles"
    packs_tasks_dir = SKILLS_PACKS_DIR / "tasks"
    packs_all_dir = SKILLS_PACKS_DIR / "all"

    packs_keywords_dir.mkdir(parents=True, exist_ok=True)
    packs_roles_dir.mkdir(parents=True, exist_ok=True)
    packs_tasks_dir.mkdir(parents=True, exist_ok=True)
    packs_all_dir.mkdir(parents=True, exist_ok=True)

    keyword_count = 0
    role_count = 0
    task_count = 0
    skills_by_keyword = build_skills_by_keyword(skills, set(registry_keywords(keyword_categories)))

    for keyword, keyword_skills in sorted(skills_by_keyword.items()):
        keyword_count += write_collection_links(
            packs_keywords_dir / keyword,
            keyword_skills,
        )

    for profile in sorted(profiles, key=lambda p: p["id"]):
        categories = profile.get("include", {}).get("categories", [])
        role_keywords = get_keywords_for_categories(categories, keyword_categories)
        role_count += write_collection_links(
            packs_roles_dir / profile["id"],
            skills_matching_keywords(skills, role_keywords),
        )

    for task in sorted(tasks, key=lambda t: t["id"]):
        task_count += write_collection_links(
            packs_tasks_dir / task["id"],
            skills_matching_keywords(skills, task_keywords(task, keyword_categories)),
        )

    all_count = write_collection_links(packs_all_dir, skills)
    write_skills_readme()

    print(
        "Generated skill packs: "
        f"{len(skills_by_keyword)} keyword dirs / {keyword_count} links, "
        f"{len(profiles)} role dirs / {role_count} links, "
        f"{len(tasks)} task dirs / {task_count} links, "
        f"all / {all_count} links"
    )


def discover_skills(registry: dict[str, Any]) -> tuple[list[SkillRecord], dict[str, list[SkillRecord]]]:
    allowed_trust = {"trusted", "reviewed"}
    skills: list[SkillRecord] = []
    skills_by_keyword: dict[str, list[SkillRecord]] = defaultdict(list)
    seen_content_hashes: set[str] = set()
    seen_frontmatter_headers: set[str] = set()
    deduped_by_hash = 0
    deduped_by_header = 0

    for item in registry["skills"]:
        trust_level = item.get("trust", {}).get("level", "unknown")
        if trust_level not in allowed_trust:
            continue
        if not item.get("enabled"):
            continue

        source_id = item["id"]
        external_path = item.get("source", {}).get("external_path")
        if not external_path:
            continue

        root = ROOT / external_path
        if not root.exists():
            continue

        for skill_file in sorted(root.rglob("SKILL.md")):
            if should_skip(skill_file.relative_to(root)):
                continue

            raw = read_skill_bytes(skill_file)
            file_hash = skill_content_hash(raw)
            if file_hash in seen_content_hashes:
                deduped_by_hash += 1
                continue

            text = normalize_skill_text(raw)
            frontmatter_header = extract_frontmatter_block(text)
            if frontmatter_header and frontmatter_header in seen_frontmatter_headers:
                deduped_by_header += 1
                continue

            skill_dir = skill_file.parent
            frontmatter = parse_skill_frontmatter_text(text)
            name = str(frontmatter.get("name") or skill_dir.name)
            description = str(frontmatter.get("description") or "")
            declared_keywords = frontmatter_declared_keywords(frontmatter)

            rel_path = skill_dir.relative_to(root).as_posix()
            keywords = sorted(set(extract_keywords(rel_path, name, description)).union(declared_keywords))

            if not keywords:
                keywords = ["uncategorized"]

            record = SkillRecord(
                source_id=source_id,
                source_trust=trust_level,
                skill_dir=skill_dir,
                skill_file=skill_file,
                name=name,
                description=description,
                keywords=keywords,
                declared_keywords=declared_keywords,
            )
            skills.append(record)
            seen_content_hashes.add(file_hash)
            if frontmatter_header:
                seen_frontmatter_headers.add(frontmatter_header)

            for keyword in keywords:
                skills_by_keyword[keyword].append(record)

    if deduped_by_hash or deduped_by_header:
        print(
            "Deduplicated "
            f"{deduped_by_hash + deduped_by_header} skills "
            f"({deduped_by_hash} by identical SKILL.md hash, "
            f"{deduped_by_header} by identical YAML header)"
        )

    return skills, skills_by_keyword


def generate_keyword_skills_md(keyword: str, skills: list[SkillRecord]) -> str:
    lines = [
        f"# {keyword}",
        "",
        "## Skills",
        "Select only the most relevant skills by description, then read only those `SKILL.md` files.",
        "",
    ]

    for skill in sorted(skills, key=lambda s: s.name):
        lines.extend([
            f"### {skill.name}",
            f"{skill.description or 'No description.'}",
            "",
            f"File: `{skill.rel_file}`",
            "",
        ])

    return "\n".join(lines)


def generate_role_skills_md(
    profile: dict[str, Any],
    keyword_categories: dict[str, list[str]],
    skills_by_keyword: dict[str, list[SkillRecord]],
) -> str:
    profile_id = profile["id"]
    role_title = profile.get("role", {}).get("title") or profile["name"]
    categories = profile.get("include", {}).get("categories", [])
    category_keywords = get_keywords_for_categories(categories, keyword_categories)
    keywords_with_skills = {keyword for keyword in category_keywords if skills_by_keyword.get(keyword)}
    
    lines = [
        f"# {role_title}",
        "",
        "## Keywords",
        "Select only keywords that directly match the current request. Prefer exact stack/tool keywords over broad categories.",
        "",
    ]

    for keyword in sorted(keywords_with_skills):
        count = len(skills_by_keyword.get(keyword, []))
        keyword_path = f"skills/catalog/keywords/{keyword}/skills.md"
        lines.append(f"- **{keyword}**: {count} skills — `{keyword_path}`")

    return "\n".join(lines)


def task_keywords(task: dict[str, Any], keyword_categories: dict[str, list[str]]) -> list[str]:
    keywords = task.get("keywords", [])
    if keywords:
        return sorted(set(keywords))
    return get_keywords_for_categories(task.get("categories", []), keyword_categories)


def generate_task_skills_md(
    task: dict[str, Any],
    keyword_categories: dict[str, list[str]],
    skills_by_keyword: dict[str, list[SkillRecord]],
) -> str:
    keywords = [keyword for keyword in task_keywords(task, keyword_categories) if skills_by_keyword.get(keyword)]
    categories = task.get("categories", [])
    lines = [
        f"# {task['name']}",
        "",
        task.get("description", ""),
        "",
        "## Categories",
        "",
    ]
    lines.extend(f"- `{category}`" for category in categories)
    lines.extend([
        "",
        "## Keywords",
        "Select 1-3 keywords that directly match the current request. Prefer exact stack/tool keywords over broad categories.",
        "",
    ])

    for keyword in keywords:
        count = len(skills_by_keyword.get(keyword, []))
        lines.append(f"- **{keyword}**: {count} skills — `skills/catalog/keywords/{keyword}/skills.md`")

    return "\n".join(lines)


def build_role_to_categories(profiles: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Build role-to-categories mapping from profiles registry."""
    result = {}
    for profile in profiles:
        role_title = profile.get("role", {}).get("title") or profile["name"]
        categories = profile.get("include", {}).get("categories", [])
        if categories:
            result[role_title] = categories
    return result


def build_keyword_category_display(keyword_categories: dict[str, list[str]]) -> dict[str, str]:
    """Build human-readable keyword category descriptions from registry."""
    # Use category name as description
    return {cat: cat.replace("_", " ").title() for cat in keyword_categories.keys()}


def generate_root_skills_md(
    profiles: list[dict[str, Any]],
    tasks: list[dict[str, Any]],
    keyword_categories: dict[str, list[str]],
    skills_by_keyword: dict[str, list[SkillRecord]],
    keyword_to_category: dict[str, str],
) -> str:
    lines = [
        "# AI Capability Registry",
        "",
        "## Skill Resolution Protocol",
        "",
        "Before starting work, resolve skills with progressive disclosure:",
        "",
        "1. **Extract intent** — identify action, domain, stack/tool, artifact, and constraints from the user request.",
        "2. **Route by task first** — match the request to one Task below; select a second Task only for clearly mixed workflows.",
        "3. **Use role as context** — select at most one Role only when the user asks from that role perspective or it disambiguates the task.",
        "4. **Read selected indexes only** — open only the matched `skills/catalog/tasks/<task-id>/skills.md` and optional `skills/catalog/roles/<role-id>/skills.md`.",
        "5. **Choose keywords** — select 1-3 most specific keywords from those indexes; prefer exact stack/tool keywords over broad category keywords.",
        "6. **Read keyword catalogs** — open only selected `skills/catalog/keywords/<keyword>/skills.md` files.",
        "7. **Load skills** — choose 1-3 best matching skill descriptions per keyword, then read only those `SKILL.md` files.",
        "8. **Apply guidance** — follow loaded skill instructions and adapt them to project conventions.",
        "",
        "### Routing Scope",
        "",
        "Paths in keyword catalogs are relative to this registry root.",
        "`external/` is a sibling of the root `skills/` directory at `<registry-root>/external/`; do not look for it under `skills/external/`.",
        "",
        "Use `skills/catalog/` only for skill selection.",
        "Use `skills/packs/` only when configuring agents with preselected skill directories.",
        "Do not browse `skills/catalog/` or `skills/packs/` broadly during task execution.",
        "",
        "### Roles (category groupings)",
        "",
    ]

    for profile in profiles:
        role = profile.get("role", {}).get("title") or profile["name"]
        cats = profile.get("include", {}).get("categories", [])
        keyword_list = ", ".join(f"`{c}`" for c in cats if c in keyword_categories)
        lines.append(f"- **{role}**: `skills/catalog/roles/{profile['id']}/skills.md` -> {keyword_list}")

    lines.extend([
        "",
        "### Tasks (workflow entry points)",
        "",
    ])

    for task in tasks:
        available = [keyword for keyword in task_keywords(task, keyword_categories) if keyword in skills_by_keyword]
        if available:
            keyword_links = ", ".join(f"`{keyword}`" for keyword in available)
            lines.append(f"- **{task['name']}**: `skills/catalog/tasks/{task['id']}/skills.md` -> {keyword_links}")

    lines.extend([
        "",
        "## Policy",
        "- Use **trusted** or **reviewed** sources only",
        "- Prefer Docker/hosted MCP",
        "- Never execute untrusted scripts",
        "",
    ])

    return "\n".join(lines)


def cleanup_output_dir(path: Path) -> None:
    if path.exists() or path.is_symlink():
        if path.is_dir() and not path.is_symlink():
            shutil.rmtree(path)
        else:
            path.unlink()


def cleanup_skills() -> None:
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    for item in SKILLS_DIR.iterdir():
        if item.name == ".gitkeep":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    for legacy_dir in LEGACY_OUTPUT_DIRS:
        cleanup_output_dir(legacy_dir)


def generate_skill_catalog_md(
    skills: list[SkillRecord],
    keyword_categories: dict[str, list[str]],
    enabled_by_id: dict[str, bool],
) -> str:
    """Generate human-readable skill catalog grouped by category."""
    by_category: dict[str, list[SkillRecord]] = defaultdict(list)
    uncategorized: list[SkillRecord] = []

    for skill in skills:
        matched = False
        for cat, keywords in keyword_categories.items():
            if any(keyword in skill.keywords for keyword in keywords):
                by_category[cat].append(skill)
                matched = True
                break
        if not matched:
            uncategorized.append(skill)

    enabled_count = sum(1 for skill in skills if enabled_by_id.get(skill.skill_id, False))
    disabled_count = len(skills) - enabled_count

    lines = [
        "# Skill Catalog",
        "",
        "This is a generated human-readable view. Edit `enabled` and `keywords` in `skill-catalog.d/*.yaml`.",
        "",
        f"Total: {len(skills)} skills across {len(keyword_categories)} categories",
        f"Enabled: {enabled_count}; Disabled: {disabled_count}",
        "",
    ]

    for category in sorted(by_category.keys()):
        cat_skills = sorted(by_category[category], key=lambda s: s.name)
        lines.extend([
            f"## {category.replace('_', ' ').title()}",
            "",
        ])
        for skill in cat_skills:
            keywords_str = ", ".join(f"`{keyword}`" for keyword in skill.keywords[:10])
            lines.extend([
                f"### {skill.name}",
                f"{skill.description or 'No description.'}",
                "",
                f"**Enabled:** `{str(enabled_by_id.get(skill.skill_id, False)).lower()}`",
                f"**ID:** `{skill.skill_id}`",
                f"**Keywords:** {keywords_str}",
                f"**Source:** {skill.source_id}",
                "",
                f"File: `{skill.rel_file}`",
                "",
            ])

    if uncategorized:
        lines.extend([
            "## Other",
            "",
        ])
        for skill in sorted(uncategorized, key=lambda s: s.name):
            lines.extend([
                f"### {skill.name}",
                f"{skill.description or 'No description.'}",
                "",
                f"**Enabled:** `{str(enabled_by_id.get(skill.skill_id, False)).lower()}`",
                f"**ID:** `{skill.skill_id}`",
                f"**Keywords:** {', '.join(skill.keywords[:10])}",
                f"**Source:** {skill.source_id}",
                "",
            ])

    return "\n".join(lines)


def main() -> int:
    registry = load_all()
    cleanup_skills()

    keyword_to_category = build_keyword_to_categories(registry["keyword_categories"])
    keyword_categories = registry["keyword_categories"]
    allowed_keywords = set(registry_keywords(keyword_categories))

    discovered_skills, _ = discover_skills(registry)
    sync_skill_catalog(discovered_skills, registry)
    catalog_skills, enabled_by_id = load_skills_from_catalog(registry)
    skills = [skill for skill in catalog_skills if enabled_by_id.get(skill.skill_id, False)]
    skills_by_keyword = build_skills_by_keyword(skills, allowed_keywords)

    print(
        f"Catalog has {len(catalog_skills)} skills; "
        f"enabled {len(skills)} skills across {len(skills_by_keyword)} keywords"
    )

    # Generate keyword routing catalogs
    keywords_dir = SKILLS_CATALOG_DIR / "keywords"
    for keyword, keyword_skills in sorted(skills_by_keyword.items()):
        keyword_dir = keywords_dir / keyword
        content = generate_keyword_skills_md(keyword, keyword_skills)
        write_text(keyword_dir / "skills.md", content)

    # Generate role routing catalogs
    roles_dir = SKILLS_CATALOG_DIR / "roles"
    for profile in registry["profiles"]:
        profile_id = profile["id"]
        role_dir = roles_dir / profile_id
        content = generate_role_skills_md(profile, keyword_categories, skills_by_keyword)
        write_text(role_dir / "skills.md", content)

    # Generate task routing catalogs
    tasks_dir = SKILLS_CATALOG_DIR / "tasks"
    for task in registry["tasks"]:
        task_dir = tasks_dir / task["id"]
        content = generate_task_skills_md(task, keyword_categories, skills_by_keyword)
        write_text(task_dir / "skills.md", content)

    # Generate symlink packs for direct inclusion in agent configs.
    generate_collections(skills, keyword_categories, registry["profiles"], registry["tasks"])

    # Generate root skills.md
    root_skills_content = generate_root_skills_md(
        registry["profiles"],
        registry["tasks"],
        keyword_categories,
        skills_by_keyword,
        keyword_to_category,
    )
    write_text(SKILLS_DIR / "skills.md", root_skills_content)

    # Generate human-readable skill catalog at root level
    catalog_path = ROOT / "skill-catalog.md"
    catalog_content = generate_skill_catalog_md(catalog_skills, keyword_categories, enabled_by_id)
    write_text(catalog_path, catalog_content)
    print(f"Generated skill catalog: {catalog_path}")

    print("Generated skill maps:")
    print(f"  - {SKILLS_DIR / 'skills.md'}")
    print(f"  - {len(registry['profiles'])} role catalogs")
    print(f"  - {len(registry['tasks'])} task catalogs")
    print(f"  - {len(skills_by_keyword)} keyword catalogs")
    print(f"\nAdd this to your agent config:")
    print(f"  {abs_path(SKILLS_DIR / 'skills.md')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
