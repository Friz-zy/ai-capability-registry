#!/usr/bin/env python3
"""Generate workflow routing indexes from registry/workflows.yaml.

This generator intentionally preserves authored workflow guide and manifest files
under workflows/<category>/<workflow-id>/. The registry stores routing metadata;
the detailed stage and gate manifests remain authored runtime files until the
registry schema is expanded to store those details without making
registry/workflows.yaml unwieldy.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_all, write_text


WORKFLOWS_DIR = ROOT / "workflows"
WORKFLOWS_CATALOG_MD = ROOT / "workflows-catalog.md"
TEMPLATES_DIR = ROOT / "templates" / "workflows"


def template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8").rstrip()


def render(name: str, values: dict[str, Any]) -> str:
    text = template(name)
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", str(value))
    unresolved = re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", text)
    if unresolved:
        raise ValueError(f"Unresolved placeholder(s) in {name}: {', '.join(sorted(set(unresolved)))}")
    return text


def string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, str) and value:
        return [value]
    return []


def workflow_refs(workflows: list[dict[str, Any]]) -> str:
    if not workflows:
        return "none"
    return ", ".join(f"`{workflow['id']}`" for workflow in sorted(workflows, key=lambda item: str(item.get("id"))))


def validate_authored_workflow_files(workflows: list[dict[str, Any]]) -> None:
    """Validate workflow guide and manifest references without generating them.

    Args:
        workflows: Workflow registry entries.

    Raises:
        FileNotFoundError: If a referenced guide or manifest is missing.
    """
    missing_paths: list[str] = []
    for workflow in workflows:
        workflow_id = str(workflow.get("id") or "unknown")
        for field in ("guide", "manifest"):
            value = workflow.get(field)
            if not isinstance(value, str) or not value:
                continue
            path = ROOT / value
            if not path.exists():
                missing_paths.append(f"{workflow_id}: {field} {value}")

    if missing_paths:
        missing_summary = "\n".join(f"- {path}" for path in missing_paths)
        raise FileNotFoundError(f"Missing authored workflow file(s):\n{missing_summary}")


def matched_workflows(workflows: list[dict[str, Any]], field: str, entry_id: str) -> list[dict[str, Any]]:
    return [workflow for workflow in workflows if entry_id in string_list(workflow.get(field))]


def catalog_workflow_lines(workflows: list[dict[str, Any]]) -> str:
    if not workflows:
        return "No workflows match this route."
    lines = []
    for workflow in sorted(workflows, key=lambda item: str(item.get("id"))):
        workflow_id = str(workflow.get("id") or "unknown")
        name = str(workflow.get("name") or workflow_id)
        description = str(workflow.get("description") or "No description.")
        guide = workflow.get("guide")
        manifest = workflow.get("manifest")
        line = f"- **{name}** (`{workflow_id}`): {description}"
        if guide:
            line += f" Guide: `{guide}`."
        if manifest:
            line += f" Manifest: `{manifest}`."
        lines.append(line)
    return "\n".join(lines)


def role_lines(profiles: list[dict[str, Any]], workflows: list[dict[str, Any]]) -> str:
    lines = []
    for profile in profiles:
        role = profile.get("role", {}).get("title") or profile.get("name") or profile.get("id")
        matches = matched_workflows(workflows, "match_roles", str(profile.get("id")))
        lines.append(f"- **{role}**: `{profile['id']}` -> {workflow_refs(matches)}")
    return "\n".join(lines)


def task_lines(tasks: list[dict[str, Any]], workflows: list[dict[str, Any]]) -> str:
    lines = []
    for task in tasks:
        matches = matched_workflows(workflows, "match_tasks", str(task.get("id")))
        lines.append(f"- **{task['name']}**: `{task['id']}` -> {workflow_refs(matches)}")
    return "\n".join(lines)


def workflow_block(workflow: dict[str, Any], tasks_by_workflow: dict[str, list[str]], roles_by_workflow: dict[str, list[str]]) -> str:
    workflow_id = str(workflow.get("id") or "unknown")
    name = str(workflow.get("name") or workflow_id)
    description = str(workflow.get("description") or "No description.")
    guide = workflow.get("guide")
    manifest = workflow.get("manifest")
    categories = string_list(workflow.get("category"))
    tags = string_list(workflow.get("tags"))
    policies = string_list(workflow.get("required_policies"))
    steps = string_list(workflow.get("steps"))
    lines = [f"### {name}", "", description, "", f"**ID:** `{workflow_id}`"]
    if guide:
        lines.append(f"**Guide:** `{guide}`")
    if manifest:
        lines.append(f"**Manifest:** `{manifest}`")
    if categories:
        lines.append("**Categories:** " + ", ".join(f"`{category}`" for category in categories))
    if tags:
        lines.append("**Tags:** " + ", ".join(f"`{tag}`" for tag in tags))
    matched_tasks = tasks_by_workflow.get(workflow_id, [])
    matched_roles = roles_by_workflow.get(workflow_id, [])
    if matched_tasks:
        lines.extend(["", f"### {name} Task IDs", "", ", ".join(f"`{task_id}`" for task_id in matched_tasks)])
    if matched_roles:
        lines.extend(["", f"### {name} Role IDs", "", ", ".join(f"`{role_id}`" for role_id in matched_roles)])
    if policies:
        lines.append("**Required policies:** " + ", ".join(f"`{policy}`" for policy in policies))
    if steps:
        lines.extend(["", "Steps:", ""])
        lines.extend(f"- `{step}`" for step in steps)
    return "\n".join(lines)


def workflow_lines(workflows: list[dict[str, Any]]) -> str:
    tasks_by_workflow: dict[str, list[str]] = defaultdict(list)
    roles_by_workflow: dict[str, list[str]] = defaultdict(list)
    for workflow in workflows:
        workflow_id = str(workflow.get("id") or "unknown")
        tasks_by_workflow[workflow_id] = string_list(workflow.get("match_tasks"))
        roles_by_workflow[workflow_id] = string_list(workflow.get("match_roles"))
    return "\n\n".join(workflow_block(workflow, tasks_by_workflow, roles_by_workflow) for workflow in workflows)


def inline_code_list(values: list[str]) -> str:
    """Render values as a comma-separated inline code list.

    Args:
        values: Values to render.

    Returns:
        A human-readable inline code list, or `none` when no values exist.
    """
    if not values:
        return "none"
    return ", ".join(f"`{value}`" for value in values)


def workflow_catalog_block(workflow: dict[str, Any]) -> str:
    """Generate one human-readable workflow catalog block.

    Args:
        workflow: Workflow registry entry.

    Returns:
        Markdown describing the workflow and its routing metadata.
    """
    workflow_id = str(workflow.get("id") or "unknown")
    name = str(workflow.get("name") or workflow_id)
    description = str(workflow.get("description") or "No description.")
    categories = string_list(workflow.get("category"))
    tags = string_list(workflow.get("tags"))
    tasks = string_list(workflow.get("match_tasks"))
    roles = string_list(workflow.get("match_roles"))
    guide = str(workflow.get("guide") or "")
    manifest = str(workflow.get("manifest") or "")

    lines = [
        f"### {name}",
        description,
        "",
        f"**ID:** `{workflow_id}`",
        f"**Categories:** {inline_code_list(categories)}",
        f"**Tags:** {inline_code_list(tags)}",
        f"**Task IDs:** {inline_code_list(tasks)}",
        f"**Role IDs:** {inline_code_list(roles)}",
    ]
    if guide:
        lines.append(f"**Guide:** `{guide}`")
    if manifest:
        lines.append(f"**Manifest:** `{manifest}`")
    return "\n".join(lines)


def generate_workflows_catalog_md(workflows: list[dict[str, Any]]) -> str:
    """Generate the root human-readable workflow catalog.

    Args:
        workflows: Workflow registry entries.

    Returns:
        Rendered Markdown catalog content.
    """
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    uncategorized = []
    for workflow in workflows:
        categories = string_list(workflow.get("category"))
        if categories:
            for category in categories:
                by_category[category].append(workflow)
        else:
            uncategorized.append(workflow)

    sections = []
    for category in sorted(by_category):
        sections.extend([
            f"## {category.replace('-', ' ').replace('_', ' ').title()}",
            "",
            "\n\n".join(workflow_catalog_block(workflow) for workflow in sorted(by_category[category], key=lambda item: str(item.get("name") or item.get("id")))),
            "",
        ])
    if uncategorized:
        sections.extend([
            "## Other",
            "",
            "\n\n".join(workflow_catalog_block(workflow) for workflow in sorted(uncategorized, key=lambda item: str(item.get("name") or item.get("id")))),
            "",
        ])

    return render(
        "workflows-catalog.md",
        {
            "total": len(workflows),
            "category_count": len(by_category),
            "sections": "\n".join(sections).rstrip(),
        },
    )


def clean_generated_catalog() -> None:
    """Clean only generated workflow catalog indexes.

    Authored workflow guide and manifest files are deliberately preserved.
    """
    catalog_dir = WORKFLOWS_DIR / "catalog"
    if not catalog_dir.exists():
        return
    for path in sorted(catalog_dir.rglob("*"), reverse=True):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def write_catalog_indexes(workflows: list[dict[str, Any]], tasks: list[dict[str, Any]], profiles: list[dict[str, Any]]) -> None:
    clean_generated_catalog()

    for task in tasks:
        entry_id = str(task.get("id"))
        matches = matched_workflows(workflows, "match_tasks", entry_id)
        if matches:
            content = render(
                "catalog.md",
                {
                    "title": str(task.get("name") or entry_id),
                    "route_type": "task",
                    "route_id": entry_id,
                    "workflows": catalog_workflow_lines(matches),
                },
            )
            write_text(WORKFLOWS_DIR / "catalog" / "tasks" / entry_id / "workflows.md", content)

    for profile in profiles:
        entry_id = str(profile.get("id"))
        matches = matched_workflows(workflows, "match_roles", entry_id)
        if matches:
            title = profile.get("role", {}).get("title") or profile.get("name") or entry_id
            content = render(
                "catalog.md",
                {
                    "title": str(title),
                    "route_type": "role",
                    "route_id": entry_id,
                    "workflows": catalog_workflow_lines(matches),
                },
            )
            write_text(WORKFLOWS_DIR / "catalog" / "roles" / entry_id / "workflows.md", content)

    categories = sorted({category for workflow in workflows for category in string_list(workflow.get("category"))})
    for category in categories:
        matches = [workflow for workflow in workflows if category in string_list(workflow.get("category"))]
        content = render(
            "catalog.md",
            {
                "title": category,
                "route_type": "category",
                "route_id": category,
                "workflows": catalog_workflow_lines(matches),
            },
        )
        write_text(WORKFLOWS_DIR / "catalog" / "categories" / category / "workflows.md", content)

    tags = sorted({tag for workflow in workflows for tag in string_list(workflow.get("tags"))})
    for tag in tags:
        matches = [workflow for workflow in workflows if tag in string_list(workflow.get("tags"))]
        content = render(
            "catalog.md",
            {
                "title": tag,
                "route_type": "tag",
                "route_id": tag,
                "workflows": catalog_workflow_lines(matches),
            },
        )
        write_text(WORKFLOWS_DIR / "catalog" / "tags" / tag / "workflows.md", content)


def main() -> int:
    registry = load_all()
    workflows = registry["workflows"]
    validate_authored_workflow_files(workflows)
    write_text(WORKFLOWS_DIR / "workflow.md", render("workflow.md", {}))
    routing_content = render(
        "routing.md",
        {
            "workflows": workflow_lines(workflows),
        },
    )
    write_text(WORKFLOWS_DIR / "routing.md", routing_content)
    write_catalog_indexes(workflows, registry["tasks"], registry["profiles"])
    write_text(WORKFLOWS_CATALOG_MD, generate_workflows_catalog_md(workflows))
    print(f"Generated workflow runtime instructions: {WORKFLOWS_DIR / 'workflow.md'}")
    print(f"Generated workflow routing dispatcher: {WORKFLOWS_DIR / 'routing.md'}")
    print(f"Generated workflow catalog: {WORKFLOWS_CATALOG_MD}")
    print("Preserved authored workflow guide and manifest files referenced by registry/workflows.yaml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
