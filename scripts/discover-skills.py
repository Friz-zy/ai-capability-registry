#!/usr/bin/env python3
"""
Generates skill maps organized by tags and roles.
All paths are relative to generated/ directory.
"""

from __future__ import annotations

import os
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

from registry_lib import GENERATED_DIR, ROOT, load_all, write_text


IGNORED_PARTS = {".git", "tests", "fixtures", "template", "node_modules", "__pycache__"}
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


def rel_from_generated(path: Path) -> str:
    """Relative path from generated/ directory to any file in repo."""
    return os.path.relpath(path, GENERATED_DIR)


def should_skip(path: Path) -> bool:
    return bool(set(path.parts) & IGNORED_PARTS)


def parse_skill_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def extract_tags(*values: Any) -> list[str]:
    text = " ".join(
        str(item) if not isinstance(item, list) else " ".join(str(i) for i in item)
        for item in values
        if item is not None
    ).lower().replace("_", "-")
    tags: set[str] = set()
    for token in re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text):
        if token.isdigit() or len(token) < 3:
            continue
        parts = [p for p in token.split("-") if p and p not in STOPWORDS and not p.isdigit()]
        if not parts:
            continue
        tags.update(p for p in parts if len(p) > 2)
        if len(parts) > 1:
            tags.add("-".join(parts))
    return sorted(tags)


def build_tag_to_categories(tag_categories: dict[str, list[str]]) -> dict[str, str]:
    tag_to_category: dict[str, str] = {}
    for category, tags in tag_categories.items():
        for tag in tags:
            tag_to_category[tag] = category
    return tag_to_category


def get_tags_for_categories(categories: list[str], tag_categories: dict[str, list[str]]) -> list[str]:
    tags: set[str] = set()
    for cat in categories:
        if cat in tag_categories:
            tags.update(tag_categories[cat])
    return sorted(tags)


class SkillRecord:
    def __init__(
        self,
        source_id: str,
        source_trust: str,
        skill_dir: Path,
        skill_file: Path,
        name: str,
        description: str,
        tags: list[str],
    ):
        self.source_id = source_id
        self.source_trust = source_trust
        self.skill_dir = skill_dir
        self.skill_file = skill_file
        self.name = name
        self.description = description
        self.tags = tags
        self.rel_file = rel_from_generated(skill_file)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "skill_file": self.rel_file,
            "source": self.source_id,
            "trust": self.source_trust,
        }


def discover_skills(registry: dict[str, Any]) -> tuple[list[SkillRecord], dict[str, list[SkillRecord]]]:
    allowed_trust = {"trusted", "reviewed"}
    skills: list[SkillRecord] = []
    skills_by_tag: dict[str, list[SkillRecord]] = defaultdict(list)

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

            skill_dir = skill_file.parent
            frontmatter = parse_skill_frontmatter(skill_file)
            name = frontmatter.get("name") or skill_dir.name
            description = frontmatter.get("description") or ""

            rel_path = skill_dir.relative_to(root).as_posix()
            tags = extract_tags(rel_path, name, description)

            if not tags:
                tags = ["uncategorized"]

            record = SkillRecord(
                source_id=source_id,
                source_trust=trust_level,
                skill_dir=skill_dir,
                skill_file=skill_file,
                name=name,
                description=description,
                tags=tags,
            )
            skills.append(record)

            for tag in tags:
                skills_by_tag[tag].append(record)

    return skills, skills_by_tag


def generate_tag_skills_md(tag: str, skills: list[SkillRecord]) -> str:
    if not skills:
        return f"# {tag}\n\nNo skills found.\n"
    
    lines = [
        f"# {tag}",
        "",
        "## Skills",
        "Load skill file when task matches.",
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
    tag_categories: dict[str, list[str]],
    skills_by_tag: dict[str, list[SkillRecord]],
) -> str:
    profile_id = profile["id"]
    role_title = profile.get("role", {}).get("title") or profile["name"]
    categories = profile.get("include", {}).get("categories", [])
    category_tags = get_tags_for_categories(categories, tag_categories)
    tags_with_skills = {tag for tag in category_tags if skills_by_tag.get(tag)}
    
    lines = [
        f"# {role_title}",
        "",
        "## Tags",
        "",
    ]

    for tag in sorted(tags_with_skills):
        count = len(skills_by_tag.get(tag, []))
        tag_path = f"tags/{tag}/skills.md"
        lines.append(f"- **{tag}**: {count} skills — `{tag_path}`")

    return "\n".join(lines)


def generate_root_skills_md(
    profiles: list[dict[str, Any]],
    tag_categories: dict[str, list[str]],
    skills_by_tag: dict[str, list[SkillRecord]],
    tag_to_category: dict[str, str],
) -> str:
    lines = [
        "# AI Capability Registry",
        "",
        "## Navigation",
        "1. Select role below",
        "2. Open role's skills.md",
        "3. Find relevant tag",
        "4. Open tag catalog",
        "5. Load skill file",
        "",
        "## Roles",
        "",
    ]

    for profile in profiles:
        profile_id = profile["id"]
        role_title = profile.get("role", {}).get("title") or profile["name"]
        role_path = f"roles/{profile_id}/skills.md"
        lines.append(f"- **{role_title}**: `{role_path}`")

    lines.extend([
        "",
        "## Policy",
        "- Use **trusted** or **reviewed** sources only",
        "- Prefer Docker/hosted MCP",
        "- Never execute untrusted scripts",
        "",
    ])

    return "\n".join(lines)


def cleanup_generated() -> None:
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    for item in GENERATED_DIR.iterdir():
        if item.name == ".gitkeep":
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def main() -> int:
    registry = load_all()
    cleanup_generated()

    tag_to_category = build_tag_to_categories(registry["tag_categories"])
    tag_categories = registry["tag_categories"]

    skills, skills_by_tag = discover_skills(registry)

    print(f"Discovered {len(skills)} skills across {len(skills_by_tag)} tags")

    # Generate tag catalogs
    tags_dir = GENERATED_DIR / "tags"
    for tag, tag_skills in skills_by_tag.items():
        tag_dir = tags_dir / tag
        content = generate_tag_skills_md(tag, tag_skills)
        write_text(tag_dir / "skills.md", content)

    # Generate role catalogs
    roles_dir = GENERATED_DIR / "roles"
    for profile in registry["profiles"]:
        profile_id = profile["id"]
        role_dir = roles_dir / profile_id
        content = generate_role_skills_md(profile, tag_categories, skills_by_tag)
        write_text(role_dir / "skills.md", content)

    # Generate root skills.md
    root_skills_content = generate_root_skills_md(
        registry["profiles"],
        tag_categories,
        skills_by_tag,
        tag_to_category,
    )
    write_text(GENERATED_DIR / "skills.md", root_skills_content)

    print("Generated skill maps:")
    print(f"  - generated/skills.md")
    print(f"  - {len(registry['profiles'])} role catalogs")
    print(f"  - {len(skills_by_tag)} tag catalogs")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
