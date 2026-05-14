#!/usr/bin/env python3
"""Generate workflow routing indexes from registry/workflows.yaml."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_all, write_text


WORKFLOWS_DIR = ROOT / "workflows"
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


def matched_workflows(workflows: list[dict[str, Any]], field: str, entry_id: str) -> list[dict[str, Any]]:
    return [workflow for workflow in workflows if entry_id in string_list(workflow.get(field))]


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
    categories = string_list(workflow.get("category"))
    policies = string_list(workflow.get("required_policies"))
    steps = string_list(workflow.get("steps"))
    lines = [f"### {name}", "", description, "", f"**ID:** `{workflow_id}`"]
    if guide:
        lines.append(f"**Guide:** `{guide}`")
    if categories:
        lines.append("**Categories:** " + ", ".join(f"`{category}`" for category in categories))
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


def main() -> int:
    registry = load_all()
    workflows = registry["workflows"]
    content = render(
        "workflows.md",
        {
            "workflows": workflow_lines(workflows),
        },
    )
    write_text(WORKFLOWS_DIR / "workflows.md", content)
    print(f"Generated workflow routing index: {WORKFLOWS_DIR / 'workflows.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
