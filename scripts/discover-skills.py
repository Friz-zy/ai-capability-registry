#!/usr/bin/env python3
"""
Generates skill maps organized by tags and roles.
Generates absolute paths for portability across machines.
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


def abs_path(path: Path) -> str:
    """Absolute path."""
    return str(path.absolute())


def rel_from_root(path: Path) -> str:
    """Relative path from registry root."""
    return path.relative_to(ROOT).as_posix()


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
        self.abs_file = abs_path(skill_file)
        self.rel_file = rel_from_root(skill_file)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "tags": self.tags,
            "skill_file": self.abs_file,
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
        "Load skill and **use it** when task matches.",
        "",
    ]

    for skill in sorted(skills, key=lambda s: s.name):
        lines.extend([
            f"### {skill.name}",
            f"{skill.description or 'No description.'}",
            "",
            f"File: `{skill.abs_file}`",
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
        tag_abs = abs_path(GENERATED_DIR / "tags" / tag / "skills.md")
        lines.append(f"- **{tag}**: {count} skills — `{tag_abs}`")

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


def build_tag_category_display(tag_categories: dict[str, list[str]]) -> dict[str, str]:
    """Build human-readable tag category descriptions from registry."""
    # Use category name as description
    return {cat: cat.replace("_", " ").title() for cat in tag_categories.keys()}


def build_quick_reference_tags(tag_categories: dict[str, list[str]]) -> list[tuple[str, list[str]]]:
    """Build quick reference from first 10 categories as task->tags mapping."""
    items = list(tag_categories.items())[:10]
    return [(name.title().replace("_", " "), tags) for name, tags in items]


def generate_root_skills_md(
    profiles: list[dict[str, Any]],
    tag_categories: dict[str, list[str]],
    skills_by_tag: dict[str, list[SkillRecord]],
    tag_to_category: dict[str, str],
) -> str:
    root_abs = abs_path(GENERATED_DIR / "skills.md")
    tags_abs = abs_path(GENERATED_DIR / "tags")
    roles_abs = abs_path(GENERATED_DIR / "roles")

    # Build dynamic data from registry
    role_to_categories = build_role_to_categories(profiles)
    tag_category_display = build_tag_category_display(tag_categories)
    quick_reference_tags = build_quick_reference_tags(tag_categories)

    lines = [
        "# AI Capability Registry",
        "",
        "## Skill Resolution Protocol",
        "",
        "When a task is received, perform these steps BEFORE starting work:",
        "",
        "1. **Analyze request** — extract keywords from user request",
        "2. **Choose entry point** — select a Role below OR browse Tags directly",
        "3. **Match categories** — each role shows its categories",
        "4. **Load skills** — read SKILL.md files from matched tags",
        "5. **Apply guidance** — follow skill instructions, adapt to project conventions",
        "",
        "### Roles (category groupings)",
        "",
        f"Browse all roles: `{roles_abs}/`\nBrowse all tags: `{tags_abs}/`",
        "",
    ]

    for role, cats in sorted(role_to_categories.items()):
        tag_list = ", ".join(f"`{c}`" for c in cats if c in tag_categories)
        lines.append(f"- **{role}** → {tag_list}")

    lines.extend([
        "",
        "### Quick Reference (task → tags)",
        "",
        "| Task | Tags to Check |",
        "|------|---------------|",
    ])

    for task, tags in quick_reference_tags:
        available = [t for t in tags if t in skills_by_tag]
        if available:
            tag_links = ", ".join(f"`{t}`" for t in available)
            lines.append(f"| {task} | {tag_links} |")

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


def generate_skill_catalog_md(
    skills: list[SkillRecord],
    tag_categories: dict[str, list[str]],
) -> str:
    """Generate human-readable skill catalog grouped by category."""
    by_category: dict[str, list[SkillRecord]] = defaultdict(list)
    uncategorized: list[SkillRecord] = []

    for skill in skills:
        matched = False
        for cat, tags in tag_categories.items():
            if any(t in skill.tags for t in tags):
                by_category[cat].append(skill)
                matched = True
                break
        if not matched:
            uncategorized.append(skill)

    lines = [
        "# Skill Catalog",
        "",
        f"Total: {len(skills)} skills across {len(tag_categories)} categories",
        "",
    ]

    for category in sorted(by_category.keys()):
        cat_skills = sorted(by_category[category], key=lambda s: s.name)
        lines.extend([
            f"## {category.replace('_', ' ').title()}",
            "",
        ])
        for skill in cat_skills:
            tags_str = ", ".join(f"`{t}`" for t in skill.tags[:5])
            lines.extend([
                f"### {skill.name}",
                f"{skill.description or 'No description.'}",
                "",
                f"**Tags:** {tags_str}",
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
                f"**Tags:** {', '.join(skill.tags[:5])}",
                f"**Source:** {skill.source_id}",
                "",
            ])

    return "\n".join(lines)


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

    # Generate human-readable skill catalog at root level
    catalog_path = ROOT / "skill-catalog.md"
    catalog_content = generate_skill_catalog_md(skills, tag_categories)
    write_text(catalog_path, catalog_content)
    print(f"Generated skill catalog: {catalog_path}")

    print("Generated skill maps:")
    print(f"  - {GENERATED_DIR / 'skills.md'}")
    print(f"  - {len(registry['profiles'])} role catalogs")
    print(f"  - {len(skills_by_tag)} tag catalogs")
    print(f"\nAdd this to your agent config:")
    print(f"  {abs_path(GENERATED_DIR / 'skills.md')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
