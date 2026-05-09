#!/usr/bin/env python3
from __future__ import annotations

import sys

from registry_lib import RegistryError, load_all


REQUIRED_SKILL_FIELDS = {"id", "name", "source", "category", "trust", "compatibility", "enabled"}
REQUIRED_MCP_FIELDS = {"id", "name", "source", "security", "transport", "compatibility", "trust", "runtime", "default_mode", "enabled"}
REQUIRED_AGENT_FIELDS = {"id", "name", "supports"}
REQUIRED_PROFILE_FIELDS = {"id", "name", "include"}
REQUIRED_TASK_FIELDS = {"id", "name", "description", "categories", "keywords"}
ALLOWED_SOURCE_TYPES = {"git", "docker", "hosted_https", "hosted_https_oauth", "hosted_or_docker"}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def unique_ids(kind: str, entries: list[dict], errors: list[str]) -> None:
    seen: set[str] = set()
    for entry in entries:
        entry_id = entry.get("id")
        require(bool(entry_id), f"{kind}: missing id", errors)
        if entry_id in seen:
            errors.append(f"{kind}: duplicate id {entry_id}")
        seen.add(entry_id)


def validate_skills(skills: list[dict], trust_levels: set[str], agents: set[str], errors: list[str]) -> None:
    unique_ids("skills", skills, errors)
    for skill in skills:
        skill_id = skill.get("id", "<unknown>")
        missing = REQUIRED_SKILL_FIELDS - set(skill)
        require(not missing, f"skill {skill_id}: missing fields {sorted(missing)}", errors)
        source = skill.get("source", {})
        trust = skill.get("trust", {})
        require(source.get("type") in ALLOWED_SOURCE_TYPES, f"skill {skill_id}: unsupported source type {source.get('type')}", errors)
        require(bool(source.get("repo")), f"skill {skill_id}: source.repo is required", errors)
        require(trust.get("level") in trust_levels, f"skill {skill_id}: unknown trust level {trust.get('level')}", errors)
        for agent in skill.get("compatibility", []):
            require(agent in agents, f"skill {skill_id}: unknown compatible agent {agent}", errors)
        if trust.get("level") == "candidate":
            require(skill.get("enabled") is False, f"skill {skill_id}: candidate skills must not be enabled", errors)
        version = skill.get("version", {})
        if skill.get("enabled") and version.get("pinned") is not True:
            print(f"WARN skill {skill_id}: enabled but not pinned yet", file=sys.stderr)


def validate_mcp(servers: list[dict], trust_levels: set[str], agents: set[str], policy: dict, errors: list[str]) -> None:
    unique_ids("mcp_servers", servers, errors)
    allowed_runtimes = set(policy.get("security_policy", {}).get("allow", [])) | {"hosted_or_docker", "docker"}
    for server in servers:
        server_id = server.get("id", "<unknown>")
        missing = REQUIRED_MCP_FIELDS - set(server)
        require(not missing, f"mcp {server_id}: missing fields {sorted(missing)}", errors)
        require(server.get("trust") in trust_levels, f"mcp {server_id}: unknown trust level {server.get('trust')}", errors)
        require(server.get("runtime") in allowed_runtimes, f"mcp {server_id}: runtime {server.get('runtime')} not allowed by policy", errors)
        require(server.get("source", {}).get("type") in ALLOWED_SOURCE_TYPES, f"mcp {server_id}: unsupported source type", errors)
        require(server.get("security", {}).get("local_code_execution") is not True, f"mcp {server_id}: unrestricted local execution is forbidden", errors)
        for agent in server.get("compatibility", []):
            require(agent in agents, f"mcp {server_id}: unknown compatible agent {agent}", errors)
        if server.get("trust") == "reviewed":
            require(server.get("enabled") is False, f"mcp {server_id}: reviewed MCP should be manually enabled", errors)


def validate_agents(agents: list[dict], errors: list[str]) -> None:
    unique_ids("agents", agents, errors)
    for agent in agents:
        agent_id = agent.get("id", "<unknown>")
        missing = REQUIRED_AGENT_FIELDS - set(agent)
        require(not missing, f"agent {agent_id}: missing fields {sorted(missing)}", errors)


def validate_profiles(profiles: list[dict], trust_levels: set[str], categories: set[str], errors: list[str]) -> None:
    unique_ids("profiles", profiles, errors)
    for profile in profiles:
        profile_id = profile.get("id", "<unknown>")
        missing = REQUIRED_PROFILE_FIELDS - set(profile)
        require(not missing, f"profile {profile_id}: missing fields {sorted(missing)}", errors)
        include = profile.get("include", {})
        for trust in include.get("trust", []):
            require(trust in trust_levels, f"profile {profile_id}: unknown trust level {trust}", errors)
        for category in include.get("categories", []):
            require(category in categories, f"profile {profile_id}: unknown category {category}", errors)


def validate_tasks(tasks: list[dict], keyword_categories: dict[str, list[str]], errors: list[str]) -> None:
    unique_ids("tasks", tasks, errors)
    categories = set(keyword_categories)
    keywords = {keyword for values in keyword_categories.values() for keyword in values}
    for task in tasks:
        task_id = task.get("id", "<unknown>")
        missing = REQUIRED_TASK_FIELDS - set(task)
        require(not missing, f"task {task_id}: missing fields {sorted(missing)}", errors)
        for category in task.get("categories", []):
            require(category in categories, f"task {task_id}: unknown category {category}", errors)
        for keyword in task.get("keywords", []):
            require(keyword in keywords, f"task {task_id}: unknown keyword {keyword}", errors)


def main() -> int:
    try:
        registry = load_all()
    except RegistryError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    policies = registry["policies"]
    trust_levels = set(policies.get("trust_levels", {}))
    categories = set(registry.get("keyword_categories", {}))
    agent_ids = {agent.get("id") for agent in registry["agents"]}

    validate_agents(registry["agents"], errors)
    validate_profiles(registry["profiles"], trust_levels, categories, errors)
    validate_tasks(registry["tasks"], registry["keyword_categories"], errors)
    validate_skills(registry["skills"], trust_levels, agent_ids, errors)
    validate_mcp(registry["mcp_servers"], trust_levels, agent_ids, policies, errors)

    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 1

    print(
        "Registry valid: "
        f"{len(registry['skills'])} skills, "
        f"{len(registry['mcp_servers'])} MCP servers, "
        f"{len(registry['agents'])} agents, "
        f"{len(registry['workflows'])} workflows, "
        f"{len(registry['profiles'])} profiles, "
        f"{len(registry['tasks'])} tasks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
