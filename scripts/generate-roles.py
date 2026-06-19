#!/usr/bin/env python3
"""Generate role runtime prompts from registry/profiles.yaml."""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_registry, write_text


ROLES_DIR = ROOT / "roles"
TEMPLATES_DIR = ROOT / "templates" / "roles"


def template(name: str) -> str:
    """Read a role template.

    Args:
        name: Template file name under templates/roles.

    Returns:
        Template content without trailing whitespace.
    """
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8").rstrip()


def render(name: str, values: dict[str, Any]) -> str:
    """Render a simple placeholder template.

    Args:
        name: Template file name.
        values: Placeholder values keyed by placeholder name.

    Returns:
        Rendered template content.

    Raises:
        ValueError: If any placeholder remains unresolved.
    """
    text = template(name)
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    unresolved_placeholders = re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", text)
    if unresolved_placeholders:
        unique_placeholders = ", ".join(sorted(set(unresolved_placeholders)))
        raise ValueError(f"Unresolved placeholder(s) in {name}: {unique_placeholders}")
    return compact_blank_lines(text)


def compact_blank_lines(text: str) -> str:
    """Collapse excessive blank lines in generated role prompts.

    Args:
        text: Rendered text.

    Returns:
        Text with at most one empty line between content blocks.
    """
    return re.sub(r"\n{3,}", "\n\n", text).rstrip()


def string_list(value: Any) -> list[str]:
    """Normalize a value to a list of strings.

    Args:
        value: Registry scalar or list value.

    Returns:
        String values with empty entries removed.
    """
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, str) and value:
        return [value]
    return []


def bullet_list(values: list[str]) -> str:
    """Render Markdown bullets.

    Args:
        values: Items to render.

    Returns:
        Markdown bullet list or a placeholder item.
    """
    if not values:
        return "- Not specified."
    return "\n".join(f"- {value}" for value in values)


def markdown_section(title: str, values: list[str]) -> str:
    """Render a Markdown section only when values exist.

    Args:
        title: Section heading text without Markdown prefix.
        values: Items to render as bullets.

    Returns:
        Markdown section content, or an empty string when no values exist.
    """
    if not values:
        return ""
    return f"## {title}\n\n{bullet_list(values)}\n\n"


def profile_role(profile: dict[str, Any]) -> dict[str, Any]:
    """Return the role metadata mapping for a profile.

    Args:
        profile: Profile registry entry.

    Returns:
        Role metadata mapping, or an empty mapping.
    """
    role = profile.get("role")
    return role if isinstance(role, dict) else {}


def generated_role_content(profile: dict[str, Any], common_instructions: list[str]) -> str:
    """Generate one role prompt from a profile.

    Args:
        profile: Profile registry entry.
        common_instructions: Instructions shared by every generated role.

    Returns:
        Rendered role prompt.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    responsibilities = bullet_list(string_list(role.get("responsibilities")))
    guardrails_section = markdown_section("Guardrails", string_list(role.get("guardrails")))
    delegation_level_rules_section = markdown_section(
        "Delegation Level Rules",
        string_list(role.get("delegation_level_rules")),
    )
    rendered_common_instructions = bullet_list(common_instructions)
    return render(
        "role.md",
        {
            "role_id": profile_id,
            "title": title,
            "purpose": purpose,
            "responsibilities": responsibilities,
            "delegation_level_rules_section": delegation_level_rules_section,
            "guardrails_section": guardrails_section,
            "common_instructions": rendered_common_instructions,
        },
    )


def role_registry_line(profile: dict[str, Any]) -> str:
    """Generate one role registry line.

    Args:
        profile: Profile registry entry.

    Returns:
        Markdown line for roles/roles.md.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    description = str(profile.get("description") or role.get("mission") or "No description.")
    categories = string_list(profile.get("include", {}).get("categories"))
    category_suffix = ""
    if categories:
        category_suffix = " Categories: " + ", ".join(f"`{category}`" for category in categories) + "."
    return f"- `{profile_id}`: {title}. {description}{category_suffix}"


def clean_roles_directory() -> None:
    """Remove generated role Markdown files before regeneration."""
    ROLES_DIR.mkdir(parents=True, exist_ok=True)
    for path in ROLES_DIR.glob("*.md"):
        path.unlink()


def write_roles(profiles: list[dict[str, Any]], common_instructions: list[str]) -> None:
    """Write generated role prompts and the role registry index.

    Args:
        profiles: Profile registry entries.
        common_instructions: Instructions shared by every generated role.
    """
    clean_roles_directory()
    sorted_profiles = sorted(profiles, key=lambda item: str(item.get("id") or ""))
    for profile in sorted_profiles:
        profile_id = str(profile.get("id") or "unknown")
        write_text(ROLES_DIR / f"{profile_id}.md", generated_role_content(profile, common_instructions))

    roles = "\n".join(role_registry_line(profile) for profile in sorted_profiles)
    write_text(ROLES_DIR / "roles.md", render("roles.md", {"roles": roles}))


def cleanup_legacy_role_directory() -> None:
    """Remove stale temporary role outputs if a failed generation created them."""
    legacy_directory = ROOT / "generated" / "roles"
    if legacy_directory.exists():
        shutil.rmtree(legacy_directory)


def main() -> int:
    """Generate role runtime files.

    Returns:
        Process exit code.
    """
    registry = load_registry("profiles")
    profiles = registry.get("profiles", [])
    common_instructions = string_list(registry.get("common_instructions"))
    cleanup_legacy_role_directory()
    write_roles(profiles, common_instructions)
    print(f"Generated role prompts: {len(profiles)} roles")
    print(f"Generated role registry: {ROLES_DIR / 'roles.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
