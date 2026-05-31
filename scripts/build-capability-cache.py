#!/usr/bin/env python3
"""Build a local SQLite FTS5 cache for capability routing.

The cache is a derived artifact and is intentionally written under .cache/.
It is safe for bootstrap to skip this step on Python builds where SQLite lacks
FTS5 support.
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_all, load_mcp_catalog, load_registry, load_yaml


SCHEMA_VERSION = "1"
DEFAULT_DB = ROOT / ".cache" / "capability-router.sqlite"
RESOURCE_TYPES = (
    "tasks",
    "roles",
    "workflows",
    "skills",
    "skill_sources",
    "skill_keywords",
    "mcp_servers",
    "mcp_keywords",
    "agents",
    "mcp_sources",
    "policies",
)


@dataclass(frozen=True)
class Document:
    resource_type: str
    resource_id: str
    title: str
    path: str
    text: str
    metadata: dict[str, Any]


def fts5_available() -> tuple[bool, str]:
    try:
        con = sqlite3.connect(":memory:")
        con.execute("CREATE VIRTUAL TABLE fts5_check USING fts5(content)")
        con.close()
    except sqlite3.Error as exc:
        return False, str(exc)
    return True, "available"


def slug(value: Any) -> str:
    return re.sub(r"[^a-z0-9._-]+", "-", str(value).lower()).strip("-") or "unknown"


def string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, str) and value:
        return [value]
    return []


def flatten_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, dict):
        return " ".join(f"{key} {flatten_text(val)}" for key, val in value.items())
    if isinstance(value, list):
        return " ".join(flatten_text(item) for item in value)
    return str(value)


def rel_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def existing_path(*parts: str) -> str:
    path = ROOT.joinpath(*parts)
    return rel_path(path) if path.exists() else "/".join(parts)


def read_optional_text(relative_path: str, max_chars: int = 20000) -> str:
    path = ROOT / relative_path
    if not path.exists() or not path.is_file():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")[:max_chars]


def alias_config() -> tuple[dict[str, list[str]], dict[str, dict[str, list[str]]]]:
    data = load_registry("keyword-categories")
    raw_aliases = data.get("routing_aliases", {})
    aliases: dict[str, list[str]] = {}
    if isinstance(raw_aliases, dict):
        for key, values in raw_aliases.items():
            aliases[str(key)] = string_list(values)

    raw_negative = data.get("routing_negative_matches", {})
    negative: dict[str, dict[str, list[str]]] = {}
    if isinstance(raw_negative, dict):
        for resource_type, groups in raw_negative.items():
            if not isinstance(groups, dict):
                continue
            negative[str(resource_type)] = {
                str(group): string_list(values)
                for group, values in groups.items()
            }
    return aliases, negative


def aliases_for(keyword: str, aliases: dict[str, list[str]]) -> list[str]:
    return aliases.get(keyword, [])


def build_task_documents(registry: dict[str, Any], aliases: dict[str, list[str]]) -> list[Document]:
    docs: list[Document] = []
    for task in registry["tasks"]:
        task_id = str(task["id"])
        keywords = string_list(task.get("keywords"))
        text = " ".join([
            task_id,
            str(task.get("name") or ""),
            str(task.get("description") or ""),
            flatten_text(task.get("categories")),
            flatten_text(keywords),
            flatten_text([aliases_for(keyword, aliases) for keyword in keywords]),
        ])
        docs.append(Document(
            "tasks",
            task_id,
            str(task.get("name") or task_id),
            "registry/tasks.yaml",
            text,
            {
                "categories": string_list(task.get("categories")),
                "keywords": keywords,
                "skill_task_index": existing_path("skills", "catalog", "tasks", task_id, "skills.md"),
                "mcp_task_index": existing_path("mcp", "catalog", "tasks", task_id, "servers.md"),
            },
        ))
    return docs


def build_role_documents(registry: dict[str, Any], aliases: dict[str, list[str]]) -> list[Document]:
    docs: list[Document] = []
    for profile in registry["profiles"]:
        role_id = str(profile["id"])
        role = profile.get("role", {}) if isinstance(profile.get("role"), dict) else {}
        categories = string_list(profile.get("include", {}).get("categories") if isinstance(profile.get("include"), dict) else [])
        category_keywords: list[str] = []
        for category in categories:
            category_keywords.extend(string_list(registry["keyword_categories"].get(category)))
        title = str(role.get("title") or profile.get("name") or role_id)
        text = " ".join([
            role_id,
            title,
            str(profile.get("description") or ""),
            flatten_text(role),
            flatten_text(categories),
            flatten_text(category_keywords),
            flatten_text([aliases_for(keyword, aliases) for keyword in category_keywords]),
        ])
        docs.append(Document(
            "roles",
            role_id,
            title,
            "registry/profiles.yaml",
            text,
            {
                "categories": categories,
                "skill_role_index": existing_path("skills", "catalog", "roles", role_id, "skills.md"),
                "mcp_role_index": existing_path("mcp", "catalog", "roles", role_id, "servers.md"),
            },
        ))
    return docs


def build_workflow_documents(registry: dict[str, Any]) -> list[Document]:
    docs: list[Document] = []
    for workflow in registry["workflows"]:
        workflow_id = str(workflow["id"])
        guide = str(workflow.get("guide") or "workflows/workflows.md")
        text = " ".join([
            workflow_id,
            str(workflow.get("name") or ""),
            str(workflow.get("description") or ""),
            flatten_text(workflow.get("category")),
            flatten_text(workflow.get("match_tasks")),
            flatten_text(workflow.get("match_roles")),
            read_optional_text(guide, 12000),
        ])
        docs.append(Document(
            "workflows",
            workflow_id,
            str(workflow.get("name") or workflow_id),
            guide,
            text,
            {
                "categories": string_list(workflow.get("category")),
                "match_tasks": string_list(workflow.get("match_tasks")),
                "match_roles": string_list(workflow.get("match_roles")),
            },
        ))
    return docs


def load_skill_catalog_entries() -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    catalog_dir = ROOT / "skill-catalog.d"
    if not catalog_dir.exists():
        return entries
    for path in sorted(catalog_dir.glob("*.yaml")):
        data = load_yaml(path)
        if not isinstance(data, dict):
            continue
        source = str(data.get("source") or path.stem)
        for item in data.get("skills", []):
            if not isinstance(item, dict):
                continue
            item = dict(item)
            item.setdefault("source", source)
            entries.append(item)
    return entries


def build_skill_documents(aliases: dict[str, list[str]]) -> list[Document]:
    docs: list[Document] = []
    for item in load_skill_catalog_entries():
        skill_id = str(item.get("id") or item.get("path") or "")
        if not skill_id:
            continue
        skill_file = str(item.get("skill_file") or f"{skill_id}/SKILL.md")
        keywords = string_list(item.get("keywords"))
        text = " ".join([
            skill_id,
            str(item.get("name") or Path(skill_id).name),
            str(item.get("description") or ""),
            str(item.get("source") or ""),
            flatten_text(keywords),
            flatten_text([aliases_for(keyword, aliases) for keyword in keywords]),
            read_optional_text(skill_file, 16000),
        ])
        docs.append(Document(
            "skills",
            skill_id,
            str(item.get("name") or Path(skill_id).name),
            skill_file,
            text,
            {
                "enabled": bool(item.get("enabled", False)),
                "exists": bool(item.get("exists", True)),
                "source": str(item.get("source") or ""),
                "keywords": keywords,
                "path": str(item.get("path") or skill_id),
            },
        ))
    return docs


def build_skill_source_documents(registry: dict[str, Any]) -> list[Document]:
    docs: list[Document] = []
    for item in registry["skills"]:
        source_id = str(item.get("id") or "")
        if not source_id:
            continue
        text = " ".join([
            source_id,
            str(item.get("name") or ""),
            str(item.get("description") or ""),
            flatten_text(item.get("category")),
            flatten_text(item.get("activation")),
            flatten_text(item.get("compatibility")),
            flatten_text(item.get("trust")),
        ])
        docs.append(Document(
            "skill_sources",
            source_id,
            str(item.get("name") or source_id),
            "registry/skills.yaml",
            text,
            {
                "enabled": bool(item.get("enabled", False)),
                "category": string_list(item.get("category")),
                "trust": item.get("trust", {}),
                "source": item.get("source", {}),
            },
        ))
    return docs


def build_keyword_documents(resource_type: str, registry: dict[str, Any], aliases: dict[str, list[str]]) -> list[Document]:
    docs: list[Document] = []
    prefix = "skills/catalog/keywords" if resource_type == "skill_keywords" else "mcp/catalog/keywords"
    filename = "skills.md" if resource_type == "skill_keywords" else "servers.md"
    categories_by_keyword: dict[str, list[str]] = {}
    for category, keywords in registry["keyword_categories"].items():
        for keyword in string_list(keywords):
            categories_by_keyword.setdefault(keyword, []).append(str(category))
    for keyword, categories in sorted(categories_by_keyword.items()):
        path = existing_path(prefix, keyword, filename)
        text = " ".join([
            keyword,
            flatten_text(categories),
            flatten_text(aliases_for(keyword, aliases)),
            read_optional_text(path, 12000),
        ])
        docs.append(Document(
            resource_type,
            keyword,
            keyword,
            path,
            text,
            {"categories": sorted(set(categories)), "aliases": aliases_for(keyword, aliases)},
        ))
    return docs


def mcp_keywords(server: dict[str, Any]) -> list[str]:
    return [slug(item) for item in string_list(server.get("keywords"))]


def build_mcp_documents(aliases: dict[str, list[str]]) -> list[Document]:
    docs: list[Document] = []
    for server in load_mcp_catalog():
        server_id = slug(server.get("id") or "unknown")
        keywords = mcp_keywords(server)
        guide = existing_path("mcp", "servers", server_id, "SKILL.md")
        text = " ".join([
            server_id,
            str(server.get("name") or ""),
            str(server.get("description") or ""),
            str(server.get("runtime") or ""),
            str(server.get("trust") or ""),
            flatten_text(keywords),
            flatten_text([aliases_for(keyword, aliases) for keyword in keywords]),
            flatten_text(server.get("skill")),
            read_optional_text(guide, 12000),
        ])
        docs.append(Document(
            "mcp_servers",
            server_id,
            str(server.get("name") or server_id),
            guide,
            text,
            {
                "enabled": bool(server.get("enabled", False)),
                "exists": bool(server.get("exists", True)),
                "runtime": str(server.get("runtime") or ""),
                "trust": str(server.get("trust") or ""),
                "keywords": keywords,
                "default_mode": str(server.get("default_mode") or ""),
            },
        ))
    return docs


def build_agent_documents(registry: dict[str, Any]) -> list[Document]:
    docs: list[Document] = []
    for agent in registry["agents"]:
        agent_id = str(agent.get("id") or "")
        if not agent_id:
            continue
        docs.append(Document(
            "agents",
            agent_id,
            str(agent.get("name") or agent_id),
            "registry/agents.yaml",
            flatten_text(agent),
            {"supports": string_list(agent.get("supports")), "config_paths": agent.get("config_paths", {})},
        ))
    return docs


def build_mcp_source_documents() -> list[Document]:
    data = load_registry("mcp-sources")
    docs: list[Document] = []
    for source in data.get("mcp_sources", []):
        if not isinstance(source, dict):
            continue
        source_id = str(source.get("id") or "")
        if not source_id:
            continue
        docs.append(Document(
            "mcp_sources",
            source_id,
            str(source.get("name") or source_id),
            "registry/mcp-sources.yaml",
            flatten_text(source),
            {"enabled": bool(source.get("enabled", False)), "trust": str(source.get("trust") or "")},
        ))
    return docs


def build_policy_documents(registry: dict[str, Any]) -> list[Document]:
    docs: list[Document] = []
    for key, value in registry["policies"].items():
        docs.append(Document(
            "policies",
            str(key),
            str(key).replace("_", " ").title(),
            "registry/policies.yaml",
            f"{key} {flatten_text(value)}",
            {"value": value},
        ))
    return docs


def collect_documents() -> tuple[list[Document], dict[str, list[str]], dict[str, dict[str, list[str]]]]:
    registry = load_all()
    aliases, negative = alias_config()
    docs: list[Document] = []
    docs.extend(build_task_documents(registry, aliases))
    docs.extend(build_role_documents(registry, aliases))
    docs.extend(build_workflow_documents(registry))
    docs.extend(build_skill_documents(aliases))
    docs.extend(build_skill_source_documents(registry))
    docs.extend(build_keyword_documents("skill_keywords", registry, aliases))
    docs.extend(build_mcp_documents(aliases))
    docs.extend(build_keyword_documents("mcp_keywords", registry, aliases))
    docs.extend(build_agent_documents(registry))
    docs.extend(build_mcp_source_documents())
    docs.extend(build_policy_documents(registry))
    return docs, aliases, negative


def create_resource_tables(con: sqlite3.Connection) -> None:
    for resource_type in RESOURCE_TYPES:
        con.execute(f"""
            CREATE TABLE {resource_type} (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                path TEXT NOT NULL,
                text TEXT NOT NULL,
                metadata_json TEXT NOT NULL
            )
        """)
        con.execute(f"""
            CREATE VIRTUAL TABLE {resource_type}_fts USING fts5(
                id UNINDEXED,
                title,
                path UNINDEXED,
                text,
                tokenize = 'unicode61 remove_diacritics 2'
            )
        """)


def create_db(db_path: Path, docs: list[Document], aliases: dict[str, list[str]], negative: dict[str, dict[str, list[str]]]) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    con = sqlite3.connect(db_path)
    try:
        con.execute("PRAGMA journal_mode = WAL")
        con.execute("CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)")
        con.execute("CREATE TABLE aliases (keyword TEXT NOT NULL, alias TEXT NOT NULL, PRIMARY KEY (keyword, alias))")
        con.execute("CREATE TABLE negative_matches (resource_type TEXT NOT NULL, group_id TEXT NOT NULL, term TEXT NOT NULL)")
        create_resource_tables(con)

        con.executemany(
            "INSERT INTO schema_meta (key, value) VALUES (?, ?)",
            [
                ("schema_version", SCHEMA_VERSION),
                ("created_at_unix", str(int(time.time()))),
                ("root", str(ROOT)),
                ("python_sqlite_version", sqlite3.sqlite_version),
            ],
        )
        alias_rows = [(keyword, alias) for keyword, values in aliases.items() for alias in values]
        con.executemany("INSERT INTO aliases (keyword, alias) VALUES (?, ?)", alias_rows)
        negative_rows = [
            (resource_type, group_id, term)
            for resource_type, groups in negative.items()
            for group_id, terms in groups.items()
            for term in terms
        ]
        con.executemany("INSERT INTO negative_matches (resource_type, group_id, term) VALUES (?, ?, ?)", negative_rows)

        for doc in docs:
            con.execute(
                f"INSERT INTO {doc.resource_type} (id, title, path, text, metadata_json) VALUES (?, ?, ?, ?, ?)",
                (doc.resource_id, doc.title, doc.path, doc.text, json.dumps(doc.metadata, ensure_ascii=False, sort_keys=True)),
            )
            con.execute(
                f"INSERT INTO {doc.resource_type}_fts (id, title, path, text) VALUES (?, ?, ?, ?)",
                (doc.resource_id, doc.title, doc.path, doc.text),
            )
        con.commit()
    finally:
        con.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the local capability-router SQLite FTS5 cache.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Cache DB path. Defaults to .cache/capability-router.sqlite")
    parser.add_argument("--check", action="store_true", help="Only check Python SQLite FTS5 availability.")
    parser.add_argument("--require-fts5", action="store_true", help="Exit non-zero instead of skipping when FTS5 is unavailable.")
    args = parser.parse_args()

    available, reason = fts5_available()
    if args.check:
        print(json.dumps({"fts5": available, "reason": reason, "sqlite_version": sqlite3.sqlite_version}, sort_keys=True))
        return 0 if available else 1
    if not available:
        message = f"SQLite FTS5 is unavailable in this Python build: {reason}; skipped capability cache generation"
        if args.require_fts5:
            print(message, file=sys.stderr)
            return 1
        print(message)
        return 0

    docs, aliases, negative = collect_documents()
    create_db(args.db, docs, aliases, negative)
    counts: dict[str, int] = {resource_type: 0 for resource_type in RESOURCE_TYPES}
    for doc in docs:
        counts[doc.resource_type] += 1
    print(json.dumps({"cache": rel_path(args.db), "documents": counts, "fts5": True}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
