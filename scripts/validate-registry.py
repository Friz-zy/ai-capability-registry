#!/usr/bin/env python3
from __future__ import annotations

import re
import sys

from registry_lib import RegistryError, load_all, load_registry


REQUIRED_SKILL_FIELDS = {"id", "name", "source", "category", "trust", "compatibility", "enabled"}
REQUIRED_MCP_FIELDS = {"id", "name", "source", "security", "transport", "trust", "runtime", "default_mode", "enabled"}
DOCKER_DENY_ARGS = {"--privileged", "--network=host", "--pid=host", "--ipc=host"}
REQUIRED_AGENT_FIELDS = {"id", "name", "supports"}
REQUIRED_PROFILE_FIELDS = {"id", "name", "include"}
REQUIRED_TASK_FIELDS = {"id", "name", "description", "categories", "keywords"}
REQUIRED_WORKFLOW_FIELDS = {"id", "name", "description"}
ALLOWED_SOURCE_TYPES = {"git", "docker", "hosted_https", "hosted_https_oauth", "hosted_or_docker"}
# Normalized reasoning effort scale shared by per-model `level`, inline preset levels,
# reasoning_tier_map, and the provider reasoning tables.
ALLOWED_LEVELS = {"none", "minimal", "low", "medium", "high", "xhigh", "max"}
MODEL_TIERS = ["junior", "middle", "senior", "lead"]
FULL_GIT_COMMIT_PATTERN = re.compile(r"^[0-9a-f]{40}$")


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
        if source.get("type") == "git":
            commit = version.get("commit") if isinstance(version, dict) else None
            require(
                isinstance(version, dict) and version.get("pinned") is True,
                f"skill {skill_id}: git sources must set version.pinned: true",
                errors,
            )
            require(
                isinstance(commit, str) and FULL_GIT_COMMIT_PATTERN.fullmatch(commit) is not None,
                f"skill {skill_id}: version.commit must be a full 40-character lowercase commit hash",
                errors,
            )
        elif skill.get("enabled") and (
            not isinstance(version, dict) or version.get("pinned") is not True
        ):
            print(f"WARN skill {skill_id}: enabled but not pinned yet", file=sys.stderr)


def validate_mcp(
    servers: list[dict],
    trust_levels: set[str],
    agents: set[str],
    policy: dict,
    allowed_keywords: set[str],
    errors: list[str],
) -> None:
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
        keywords = server.get("keywords", [])
        require(isinstance(keywords, list), f"mcp {server_id}: keywords must be a list", errors)
        for keyword in keywords if isinstance(keywords, list) else []:
            require(isinstance(keyword, str) and bool(keyword), f"mcp {server_id}: invalid keyword {keyword}", errors)
            require(keyword in allowed_keywords, f"mcp {server_id}: unknown keyword {keyword}", errors)
        skill = server.get("skill")
        if skill is not None:
            require(isinstance(skill, dict), f"mcp {server_id}: skill must be a mapping", errors)
            if isinstance(skill, dict):
                for key in ("when_to_use", "instructions", "references", "docker"):
                    if key in skill:
                        require(
                            isinstance(skill[key], list) and all(isinstance(item, str) for item in skill[key]),
                            f"mcp {server_id}: skill.{key} must be a list of strings",
                            errors,
                        )
        if server.get("trust") == "candidate":
            require(server.get("enabled") is False, f"mcp {server_id}: candidate MCP should be manually enabled", errors)
        docker = server.get("source", {}).get("docker", {})
        if isinstance(docker, dict) and docker:
            command = docker.get("command")
            args = docker.get("args", [])
            require(command == "docker", f"mcp {server_id}: docker runtime must use command=docker", errors)
            require(isinstance(args, list) and len(args) >= 2 and args[:2] == ["run", "--rm"], f"mcp {server_id}: docker args must start with run --rm", errors)
            require(not (set(str(arg) for arg in args) & DOCKER_DENY_ARGS), f"mcp {server_id}: docker args include forbidden host escape flags", errors)


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


def validate_workflows(workflows: list[dict], tasks: list[dict], profiles: list[dict], errors: list[str]) -> None:
    unique_ids("workflows", workflows, errors)
    task_ids = {task.get("id") for task in tasks}
    profile_ids = {profile.get("id") for profile in profiles}
    for workflow in workflows:
        workflow_id = workflow.get("id", "<unknown>")
        missing = REQUIRED_WORKFLOW_FIELDS - set(workflow)
        require(not missing, f"workflow {workflow_id}: missing fields {sorted(missing)}", errors)
        guide = workflow.get("guide")
        if guide is not None:
            require(isinstance(guide, str) and guide.startswith("workflows/"), f"workflow {workflow_id}: guide must be a workflows/ path", errors)
        for task_id in workflow.get("match_tasks", []):
            require(task_id in task_ids, f"workflow {workflow_id}: unknown match task {task_id}", errors)
        for profile_id in workflow.get("match_roles", []):
            require(profile_id in profile_ids, f"workflow {workflow_id}: unknown match role {profile_id}", errors)


def validate_model_tiers(errors: list[str]) -> None:
    """Validate registry/model-tiers.yaml additively.

    Keeps the existing registry validations intact and adds checks for the
    per-model ``level`` field and inline recommended-default preset configuration.
    Per-model ``level`` is an explicit catalog value and is intentionally NOT
    required to match ``reasoning_tier_map``.

    Args:
        errors: List accumulating validation error messages.
    """
    try:
        model_tiers = load_registry("model-tiers")
    except RegistryError as exc:
        errors.append(f"model-tiers: {exc}")
        return

    providers = model_tiers.get("providers", [])
    if not isinstance(providers, list):
        errors.append("model-tiers: providers must be a list")
        return

    # Every catalog model entry carries a normalized reasoning level.
    for provider in providers:
        if not isinstance(provider, dict):
            continue
        provider_id = provider.get("id", "<unknown>")
        tiers = provider.get("tiers", {})
        if not isinstance(tiers, dict):
            continue
        for tier_id, tier in tiers.items():
            if not isinstance(tier, dict):
                continue
            models = tier.get("models", [])
            if not isinstance(models, list):
                continue
            for model in models:
                if not isinstance(model, dict):
                    continue
                model_id = model.get("model_id", "<unknown>")
                level = model.get("level")
                require(
                    isinstance(level, str) and level in ALLOWED_LEVELS,
                    f"model-tiers provider {provider_id} tier {tier_id} model {model_id}: "
                    f"level must be one of {sorted(ALLOWED_LEVELS)}",
                    errors,
                )

    # recommended_defaults: every preset key must be present in all four tiers as an
    # inline mapping with a scalar model id and an explicit reasoning level.
    recommended_defaults = model_tiers.get("recommended_defaults", {})
    require(isinstance(recommended_defaults, dict), "model-tiers: recommended_defaults must be a mapping", errors)
    preset_keys: set[str] = set()
    if isinstance(recommended_defaults, dict):
        for level_id in MODEL_TIERS:
            level_defaults = recommended_defaults.get(level_id)
            require(isinstance(level_defaults, dict), f"model-tiers: recommended_defaults.{level_id} must be a mapping", errors)
            if isinstance(level_defaults, dict):
                preset_keys.update(str(key) for key in level_defaults)
        for preset in sorted(preset_keys):
            for level_id in MODEL_TIERS:
                level_defaults = recommended_defaults.get(level_id, {})
                require(
                    isinstance(level_defaults, dict) and preset in level_defaults,
                    f"model-tiers: preset '{preset}' missing from recommended_defaults.{level_id}",
                    errors,
                )
        for level_id in MODEL_TIERS:
            level_defaults = recommended_defaults.get(level_id, {})
            if not isinstance(level_defaults, dict):
                continue
            for preset, value in level_defaults.items():
                require(
                    isinstance(value, dict),
                    f"model-tiers: recommended_defaults.{level_id}.{preset} must be a mapping",
                    errors,
                )
                if not isinstance(value, dict):
                    continue
                model_id = value.get("model")
                reasoning_level = value.get("level")
                require(
                    isinstance(model_id, str) and bool(model_id.strip()),
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.model must be a non-empty string",
                    errors,
                )
                require(
                    reasoning_level in ALLOWED_LEVELS,
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.level must be one of {sorted(ALLOWED_LEVELS)}",
                    errors,
                )
        for preset, expected_levels in {
            "openai": {level_id: "medium" for level_id in MODEL_TIERS},
            "openai-pro-medium": {level_id: "medium" for level_id in MODEL_TIERS},
            "openai-pro-high": {level_id: "high" for level_id in MODEL_TIERS},
        }.items():
            for level_id in MODEL_TIERS:
                level_defaults = recommended_defaults.get(level_id, {})
                value = level_defaults.get(preset) if isinstance(level_defaults, dict) else None
                require(
                    isinstance(value, dict) and isinstance(value.get("model"), str) and bool(value["model"].strip()),
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.model must be a non-empty string",
                    errors,
                )
                require(
                    isinstance(value, dict) and value.get("level") == expected_levels[level_id],
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.level must be {expected_levels[level_id]}",
                    errors,
                )
        expected_openai_models = {
            "openai": {
                "junior": "gpt-5.4-nano",
                "middle": "gpt-5.6-luna",
                "senior": "gpt-5.6-terra",
                "lead": "gpt-5.6-sol",
            },
            "openai-pro-medium": {
                "junior": "gpt-5.4-nano",
                "middle": "gpt-5.6-luna-pro",
                "senior": "gpt-5.6-terra-pro",
                "lead": "gpt-5.6-sol-pro",
            },
            "openai-pro-high": {
                "junior": "gpt-5.4-nano",
                "middle": "gpt-5.6-luna-pro",
                "senior": "gpt-5.6-terra-pro",
                "lead": "gpt-5.6-sol-pro",
            },
        }
        for preset, expected_models in expected_openai_models.items():
            for level_id, expected_model in expected_models.items():
                level_defaults = recommended_defaults.get(level_id, {})
                value = level_defaults.get(preset) if isinstance(level_defaults, dict) else None
                require(
                    isinstance(value, dict) and value.get("model") == expected_model,
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.model must be {expected_model}",
                    errors,
                )


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
    allowed_keywords = {keyword for values in registry["keyword_categories"].values() for keyword in values}
    agent_ids = {agent.get("id") for agent in registry["agents"]}

    validate_agents(registry["agents"], errors)
    validate_profiles(registry["profiles"], trust_levels, categories, errors)
    validate_tasks(registry["tasks"], registry["keyword_categories"], errors)
    validate_workflows(registry["workflows"], registry["tasks"], registry["profiles"], errors)
    validate_skills(registry["skills"], trust_levels, agent_ids, errors)
    validate_mcp(registry["mcp_servers"], trust_levels, agent_ids, policies, allowed_keywords, errors)
    validate_model_tiers(errors)

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
