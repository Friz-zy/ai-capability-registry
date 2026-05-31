#!/usr/bin/env python3
"""Query the local capability routing SQLite FTS5 cache."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any

from registry_lib import ROOT


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
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is",
    "it", "of", "on", "or", "that", "the", "this", "to", "with", "you", "your",
}
TYPE_ALIASES = {
    "task": "tasks",
    "role": "roles",
    "workflow": "workflows",
    "skill": "skills",
    "skills": "skills",
    "skill-source": "skill_sources",
    "skill-sources": "skill_sources",
    "skill-keyword": "skill_keywords",
    "skill-keywords": "skill_keywords",
    "mcp": "mcp_servers",
    "mcp-server": "mcp_servers",
    "mcp-servers": "mcp_servers",
    "mcp-keyword": "mcp_keywords",
    "mcp-keywords": "mcp_keywords",
    "agent": "agents",
    "mcp-source": "mcp_sources",
    "mcp-sources": "mcp_sources",
    "policy": "policies",
}


def fts5_available() -> tuple[bool, str]:
    try:
        con = sqlite3.connect(":memory:")
        con.execute("CREATE VIRTUAL TABLE fts5_check USING fts5(content)")
        con.close()
    except sqlite3.Error as exc:
        return False, str(exc)
    return True, "available"


def rel_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def tokenize(value: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 1 and token not in STOPWORDS
    ]


def phrase_present(text: str, phrase: str) -> bool:
    return phrase.lower() in text.lower()


def load_aliases(con: sqlite3.Connection) -> dict[str, list[str]]:
    aliases: dict[str, list[str]] = {}
    for keyword, alias in con.execute("SELECT keyword, alias FROM aliases"):
        aliases.setdefault(str(keyword), []).append(str(alias))
    return aliases


def expand_query(query: str, aliases: dict[str, list[str]]) -> list[str]:
    expanded = set(tokenize(query))
    query_lower = query.lower()
    for keyword, values in aliases.items():
        keyword_hit = phrase_present(query_lower, keyword.replace("-", " ")) or phrase_present(query_lower, keyword)
        alias_hit = any(phrase_present(query_lower, alias) for alias in values)
        if keyword_hit or alias_hit:
            expanded.update(tokenize(keyword))
            for alias in values:
                expanded.update(tokenize(alias))
    return sorted(expanded)


def fts_match_query(tokens: list[str]) -> str:
    safe = [token for token in tokens if re.fullmatch(r"[a-z0-9]+", token)]
    if not safe:
        raise ValueError("query produced no searchable tokens")
    return " OR ".join(safe)


def normalize_types(values: list[str]) -> list[str]:
    if not values:
        return list(RESOURCE_TYPES)
    result: list[str] = []
    for raw in values:
        for part in raw.split(","):
            key = part.strip().replace("_", "-").lower()
            if not key:
                continue
            normalized = TYPE_ALIASES.get(key, key.replace("-", "_"))
            if normalized not in RESOURCE_TYPES:
                raise ValueError(f"unknown resource type: {part}")
            if normalized not in result:
                result.append(normalized)
    return result


def load_negative_terms(con: sqlite3.Connection) -> dict[str, list[str]]:
    terms: dict[str, list[str]] = {}
    for resource_type, term in con.execute("SELECT resource_type, term FROM negative_matches"):
        terms.setdefault(str(resource_type), []).append(str(term))
    return terms


def query_type(
    con: sqlite3.Connection,
    resource_type: str,
    match_query: str,
    raw_query: str,
    negative_terms: dict[str, list[str]],
    limit: int,
) -> list[dict[str, Any]]:
    rows = con.execute(
        f"""
        SELECT f.id, f.title, f.path, bm25({resource_type}_fts) AS rank, r.metadata_json
        FROM {resource_type}_fts AS f
        JOIN {resource_type} AS r ON r.id = f.id
        WHERE {resource_type}_fts MATCH ?
        ORDER BY rank ASC
        LIMIT ?
        """,
        (match_query, limit),
    ).fetchall()
    output = []
    for resource_id, title, path, rank, metadata_json in rows:
        penalty_terms = [term for term in negative_terms.get(resource_type, []) if phrase_present(raw_query, term)]
        score = -float(rank) - (5.0 * len(penalty_terms))
        try:
            metadata = json.loads(metadata_json)
        except json.JSONDecodeError:
            metadata = {}
        output.append({
            "id": resource_id,
            "title": title,
            "path": path,
            "score": round(score + metadata_boost(metadata, raw_query, str(resource_id), str(title)), 6),
            "penaltyTerms": penalty_terms,
            "metadata": metadata,
        })
    output.sort(key=lambda item: item["score"], reverse=True)
    return output


def metadata_boost(metadata: dict[str, Any], raw_query: str, resource_id: str, title: str) -> float:
    boost = 0.0
    if metadata.get("enabled") is True:
        boost += 3.0
    elif metadata.get("enabled") is False:
        boost -= 3.0
    if metadata.get("exists") is False:
        boost -= 5.0
    trust = str(metadata.get("trust") or "")
    if trust == "trusted":
        boost += 1.0
    elif trust == "reviewed":
        boost += 0.5
    query_lower = raw_query.lower()
    if resource_id and resource_id.lower() in query_lower:
        boost += 4.0
    if title and title.lower() in query_lower:
        boost += 2.0
    return boost


def schema_meta(con: sqlite3.Connection) -> dict[str, str]:
    return {str(key): str(value) for key, value in con.execute("SELECT key, value FROM schema_meta")}


def main() -> int:
    parser = argparse.ArgumentParser(description="Query the local capability-router SQLite FTS5 cache.")
    parser.add_argument("query", nargs="?", help="Natural-language query from the agent or user request.")
    parser.add_argument("--query", dest="query_flag", help="Natural-language query from the agent or user request.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="Cache DB path. Defaults to .cache/capability-router.sqlite")
    parser.add_argument("--type", action="append", default=[], help="Resource type to query. Can be repeated or comma-separated.")
    parser.add_argument("--limit", type=int, default=5, help="Max results per resource type.")
    parser.add_argument("--files-only", action="store_true", help="Print only unique matched paths, one per line.")
    args = parser.parse_args()

    query = args.query_flag or args.query
    if not query:
        print("query is required", file=sys.stderr)
        return 2
    available, reason = fts5_available()
    if not available:
        print(f"SQLite FTS5 is unavailable in this Python build: {reason}", file=sys.stderr)
        return 1
    if not args.db.exists():
        print(f"Capability cache not found: {rel_path(args.db)}. Run ./scripts/build-capability-cache.py", file=sys.stderr)
        return 1

    try:
        resource_types = normalize_types(args.type)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    con = sqlite3.connect(args.db)
    try:
        aliases = load_aliases(con)
        expanded_tokens = expand_query(query, aliases)
        match_query = fts_match_query(expanded_tokens)
        negative_terms = load_negative_terms(con)
        results = {
            resource_type: query_type(con, resource_type, match_query, query, negative_terms, max(args.limit, 1))
            for resource_type in resource_types
        }
        files_to_read = []
        seen_paths = set()
        for items in results.values():
            for item in items:
                candidate_paths = [item.get("path")]
                metadata = item.get("metadata") if isinstance(item.get("metadata"), dict) else {}
                for value in metadata.values():
                    if isinstance(value, str) and value.endswith((".md", ".json")):
                        candidate_paths.append(value)
                for path in candidate_paths:
                    if path and path not in seen_paths:
                        seen_paths.add(path)
                        files_to_read.append(path)
        if args.files_only:
            print("\n".join(files_to_read))
            return 0
        print(json.dumps({
            "query": query,
            "expandedTokens": expanded_tokens,
            "matchQuery": match_query,
            "resourceTypes": resource_types,
            "results": results,
            "filesToRead": files_to_read,
            "cache": {"path": rel_path(args.db), "meta": schema_meta(con)},
        }, indent=2, ensure_ascii=False, sort_keys=True))
    except sqlite3.Error as exc:
        print(f"SQLite query failed: {exc}", file=sys.stderr)
        return 1
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
