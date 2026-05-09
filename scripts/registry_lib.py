#!/usr/bin/env python3
"""Shared registry helpers with a small YAML subset parser.

The registry intentionally uses a conservative YAML subset: mappings, lists,
booleans, nulls, strings, and indentation. This avoids runtime dependencies in
bootstrap and CI while keeping the registry human-editable.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registry"
SKILLS_DIR = ROOT / "skills"


class RegistryError(Exception):
    pass


def _strip_comment(line: str) -> str:
    in_single = False
    in_double = False
    for idx, char in enumerate(line):
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            return line[:idx]
    return line


def _scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value in {"true", "True", "TRUE"}:
        return True
    if value in {"false", "False", "FALSE"}:
        return False
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value.startswith('"') and value.endswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def _split_key_value(text: str) -> tuple[str, str | None]:
    if ":" not in text:
        raise RegistryError(f"Expected key/value pair, got: {text}")
    key, value = text.split(":", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        raise RegistryError(f"Empty key in line: {text}")
    return key, value if value else None


def _prepare_lines(path: Path) -> list[tuple[int, str, int]]:
    prepared: list[tuple[int, str, int]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "\t" in raw:
            raise RegistryError(f"{path}:{line_no}: tabs are not allowed")
        stripped = _strip_comment(raw).rstrip()
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        prepared.append((indent, stripped.strip(), line_no))
    return prepared


def load_yaml(path: Path) -> Any:
    lines = _prepare_lines(path)

    def parse_block(index: int, indent: int) -> tuple[Any, int]:
        if index >= len(lines):
            return {}, index
        current_indent, text, _ = lines[index]
        if current_indent < indent:
            return {}, index
        if current_indent != indent:
            raise RegistryError(f"{path}:{lines[index][2]}: unexpected indentation")

        if text.startswith("- "):
            items: list[Any] = []
            while index < len(lines):
                line_indent, line_text, line_no = lines[index]
                if line_indent < indent:
                    break
                if line_indent != indent or not line_text.startswith("- "):
                    break
                rest = line_text[2:].strip()
                index += 1
                if not rest:
                    child, index = parse_block(index, indent + 2)
                    items.append(child)
                    continue
                if ":" in rest:
                    key, value = _split_key_value(rest)
                    item: dict[str, Any] = {key: _scalar(value) if value is not None else None}
                    if value is None:
                        child, index = parse_block(index, indent + 2)
                        item[key] = child
                    elif index < len(lines) and lines[index][0] > indent:
                        child, index = parse_block(index, indent + 2)
                        if isinstance(child, dict):
                            item.update(child)
                        else:
                            raise RegistryError(
                                f"{path}:{line_no}: list item mapping continuation must be a mapping"
                            )
                    items.append(item)
                else:
                    items.append(_scalar(rest))
            return items, index

        mapping: dict[str, Any] = {}
        while index < len(lines):
            line_indent, line_text, _ = lines[index]
            if line_indent < indent:
                break
            if line_indent != indent:
                raise RegistryError(f"{path}:{lines[index][2]}: unexpected indentation")
            if line_text.startswith("- "):
                break
            key, value = _split_key_value(line_text)
            index += 1
            if value is None:
                if index < len(lines) and lines[index][0] > indent:
                    mapping[key], index = parse_block(index, indent + 2)
                else:
                    mapping[key] = None
            else:
                mapping[key] = _scalar(value)
        return mapping, index

    result, next_index = parse_block(0, lines[0][0] if lines else 0)
    if next_index != len(lines):
        raise RegistryError(f"{path}: parser stopped before EOF")
    return result


def load_registry(name: str) -> dict[str, Any]:
    path = REGISTRY_DIR / f"{name}.yaml"
    if not path.exists():
        raise RegistryError(f"Missing registry file: {path}")
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise RegistryError(f"Registry file must contain a mapping: {path}")
    return data


def load_all() -> dict[str, Any]:
    return {
        "skills": load_registry("skills").get("skills", []),
        "mcp_servers": load_registry("mcp").get("mcp_servers", []),
        "agents": load_registry("agents").get("agents", []),
        "workflows": load_registry("workflows").get("workflows", []),
        "profiles": load_registry("profiles").get("profiles", []),
        "tasks": load_registry("tasks").get("tasks", []),
        "keyword_categories": load_registry("keyword-categories").get("keyword_categories", {}),
        "policies": load_registry("policies"),
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def bullet_list(values: list[str] | None) -> str:
    if not values:
        return "- none"
    return "\n".join(f"- {value}" for value in values)
