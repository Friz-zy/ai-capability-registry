#!/usr/bin/env python3
"""Shared registry helpers with a small YAML subset parser.

The registry intentionally uses a conservative YAML subset: mappings, lists,
booleans, nulls, strings, and indentation. This avoids runtime dependencies in
bootstrap and CI while keeping the registry human-editable.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "registry"
MCP_CATALOG_DIR = ROOT / "mcp-catalog.d"
SKILLS_DIR = ROOT / "skills"

RISK_ORDER = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
ENFORCEMENT_ORDER = ["prompt_guidance", "static_validation", "runtime_preflight", "human_gate"]
SEMANTIC_CONDITION_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
PROJECTED_POLICY_RENDER_FIELDS = frozenset(
    {
        "access_gate",
        "applicability",
        "applies_when",
        "apply_gate",
        "change_gate",
        "decision",
        "default_age_days",
        "deployment_gate",
        "description",
        "ecosystems",
        "enforcement",
        "escalation",
        "exception",
        "failure_behavior",
        "group",
        "id",
        "limitation",
        "match_handling",
        "non_triggers",
        "paths",
        "preflight_must_verify",
        "production_gate",
        "production_or_destructive_gate",
        "required_guarantees",
        "requirements",
        "review_requirement",
        "risk",
        "runtime_backstops",
        "runtime_requirement",
        "selection_order",
        "selectors",
        "threshold_hours",
        "time_basis",
        "title",
        "triggers",
        "trust_boundary",
        "verification",
    }
)


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
                if re.match(r"^[A-Za-z0-9_.-]+:(?:\s+|$)", rest):
                    key, value = _split_key_value(rest)
                    item: dict[str, Any] = {key: _scalar(value) if value is not None else None}
                    if value is None:
                        if index < len(lines) and lines[index][0] == indent + 4:
                            child, index = parse_block(index, indent + 4)
                            item[key] = child
                        if index < len(lines) and lines[index][0] == indent + 2:
                            continuation_line = lines[index][2]
                            child, index = parse_block(index, indent + 2)
                            if not isinstance(child, dict):
                                raise RegistryError(f"{path}:{continuation_line}: list item mapping continuation must be a mapping")
                            duplicate_keys = set(item) & set(child)
                            if duplicate_keys:
                                raise RegistryError(f"{path}:{continuation_line}: duplicate key {sorted(duplicate_keys)[0]}")
                            item.update(child)
                    elif index < len(lines) and lines[index][0] == indent + 2:
                        continuation_line = lines[index][2]
                        child, index = parse_block(index, indent + 2)
                        if isinstance(child, dict):
                            duplicate_keys = set(item) & set(child)
                            if duplicate_keys:
                                raise RegistryError(f"{path}:{continuation_line}: duplicate key {sorted(duplicate_keys)[0]}")
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
            if key in mapping:
                raise RegistryError(f"{path}:{lines[index][2]}: duplicate key {key}")
            index += 1
            if value is None:
                if index < len(lines) and lines[index][0] > indent:
                    mapping[key], index = parse_block(index, lines[index][0])
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


def _catalog_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return sorted({*path.glob("*.yaml"), *path.glob("*.yml")})


def load_mcp_catalog() -> list[dict[str, Any]]:
    if not MCP_CATALOG_DIR.exists():
        raise RegistryError(f"Missing MCP catalog directory: {MCP_CATALOG_DIR}")

    servers: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in _catalog_files(MCP_CATALOG_DIR):
        data = load_yaml(path)
        if not isinstance(data, dict):
            raise RegistryError(f"MCP catalog file must contain a mapping: {path}")
        chunk = data.get("mcp_servers", [])
        if not isinstance(chunk, list):
            raise RegistryError(f"MCP catalog file must contain mcp_servers list: {path}")
        for item in chunk:
            if not isinstance(item, dict):
                raise RegistryError(f"MCP catalog entries must be mappings: {path}")
            entry_id = item.get("id")
            if isinstance(entry_id, str) and entry_id:
                if entry_id in seen:
                    raise RegistryError(f"Duplicate MCP catalog entry {entry_id} in {path}")
                seen.add(entry_id)
            servers.append(item)
    return servers


def load_all() -> dict[str, Any]:
    return {
        "skills": load_registry("skills").get("skills", []),
        "mcp_servers": load_mcp_catalog(),
        "agents": load_registry("agents").get("agents", []),
        "workflows": load_registry("workflows").get("workflows", []),
        "profiles": load_registry("profiles").get("profiles", []),
        "tasks": load_registry("tasks").get("tasks", []),
        "keyword_categories": load_registry("keyword-categories").get("keyword_categories", {}),
        "policies": load_registry("policies"),
    }


def index_policy_nodes(policies: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Index every identified canonical policy node and reject duplicate IDs.

    Args:
        policies: Parsed canonical policy registry.

    Returns:
        Policy nodes keyed by stable policy ID.

    Raises:
        RegistryError: If an ID is empty, non-string, or duplicated.
    """
    indexed_nodes: dict[str, dict[str, Any]] = {}

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if "id" in value:
                policy_id = value["id"]
                if not isinstance(policy_id, str) or not policy_id.strip():
                    raise RegistryError("policy id must be a non-empty string")
                if policy_id in indexed_nodes:
                    raise RegistryError(f"duplicate policy id {policy_id}")
                indexed_nodes[policy_id] = value
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(policies)
    return indexed_nodes


def resolve_policy_ids(
    policies: dict[str, Any],
    policy_ids: list[str],
) -> dict[str, dict[str, Any]]:
    """Resolve stable policy IDs to canonical policy nodes.

    Args:
        policies: Parsed canonical policy registry.
        policy_ids: Policy IDs to resolve.

    Returns:
        Resolved nodes in requested order, keyed by policy ID.

    Raises:
        RegistryError: If a reference is malformed, duplicated, or unresolved.
    """
    indexed_nodes = index_policy_nodes(policies)
    resolved_nodes: dict[str, dict[str, Any]] = {}
    for policy_id in policy_ids:
        if not isinstance(policy_id, str) or not policy_id.strip():
            raise RegistryError("policy reference must be a non-empty string")
        if policy_id in resolved_nodes:
            raise RegistryError(f"duplicate policy reference {policy_id}")
        if policy_id not in indexed_nodes:
            raise RegistryError(f"unknown policy reference {policy_id}")
        resolved_nodes[policy_id] = indexed_nodes[policy_id]
    return resolved_nodes


def normalized_node_digest(node: dict[str, Any]) -> str:
    """Return a deterministic SHA-256 digest for a parsed policy node.

    Args:
        node: Canonical parsed policy node.

    Returns:
        Hexadecimal SHA-256 digest of normalized JSON.
    """
    normalized_node = json.dumps(
        node,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(normalized_node).hexdigest()


@dataclass(frozen=True, slots=True)
class DependencyManifestObservation:
    """Raw dependency facts consumed by the internal semantic predicate.

    This type carries observations only; it has no condition-ID field and cannot
    mint semantic evidence. Callers remain responsible for the authenticity of
    supplied facts because in-process Python objects are not a sandbox boundary.

    Attributes:
        repository_relative_path: Manifest path relative to the repository root.
        dependency_sources: Immutable dependency source strings observed in the manifest.
    """

    repository_relative_path: str
    dependency_sources: tuple[str, ...]


def validate_repository_relative_path(path: str, description: str) -> str:
    """Reject absolute paths and parent traversal in repository selectors.

    Args:
        path: Repository path or glob to validate.
        description: Diagnostic label for the path source.

    Raises:
        RegistryError: If the path is empty, absolute, or traverses a parent.
    """
    if not isinstance(path, str) or not path or "\x00" in path:
        raise RegistryError(f"{description} must be a non-empty repository-relative path")
    normalized_path = path.replace("\\", "/")
    is_absolute = normalized_path.startswith("/") or bool(
        re.match(r"^[A-Za-z]:/", normalized_path)
    )
    has_parent_traversal = ".." in normalized_path.split("/")
    if is_absolute or has_parent_traversal:
        raise RegistryError(
            f"{description} must be repository-relative without parent traversal: {path}"
        )
    normalized_segments = [segment for segment in normalized_path.split("/") if segment not in {"", "."}]
    if not normalized_segments:
        raise RegistryError(f"{description} must be a non-empty repository-relative path")
    return "/".join(normalized_segments)


def validate_semantic_condition_id(condition_id: str) -> None:
    """Validate a stable semantic condition identifier.

    Args:
        condition_id: Semantic condition identifier to validate.

    Raises:
        RegistryError: If the identifier is malformed.
    """
    if not isinstance(condition_id, str) or not SEMANTIC_CONDITION_ID_PATTERN.fullmatch(condition_id):
        raise RegistryError(f"semantic condition ID {condition_id} is invalid")


def validate_projected_policy_node(policy_id: str, policy_node: dict[str, Any]) -> None:
    """Fail closed when a projected policy node cannot be safely rendered.

    Args:
        policy_id: Expected stable policy ID.
        policy_node: Canonical projected policy node.

    Raises:
        RegistryError: If fields or routing selectors are unsupported or unsafe.
    """
    unsupported_fields = sorted(set(policy_node) - PROJECTED_POLICY_RENDER_FIELDS)
    if unsupported_fields:
        raise RegistryError(f"policy {policy_id} has unsupported fields {unsupported_fields}")
    if policy_node.get("id") != policy_id:
        raise RegistryError(f"policy {policy_id} has a mismatched canonical id")

    def validate_classifications(value: Any) -> None:
        if isinstance(value, dict):
            risk = value.get("risk")
            if risk is not None and risk not in RISK_ORDER:
                raise RegistryError(f"policy {policy_id} has unknown risk classification {risk}")
            enforcement = value.get("enforcement")
            if enforcement is not None and enforcement not in ENFORCEMENT_ORDER:
                raise RegistryError(
                    f"policy {policy_id} has unknown enforcement classification {enforcement}"
                )
            for child in value.values():
                validate_classifications(child)
        elif isinstance(value, list):
            for child in value:
                validate_classifications(child)

    validate_classifications(policy_node)

    paths = policy_node.get("paths", [])
    if paths is not None:
        if not isinstance(paths, list):
            raise RegistryError(f"policy {policy_id} paths must be a list")
        for path in paths:
            validate_repository_relative_path(path, f"policy {policy_id} protected path")

    applicability = policy_node.get("applicability")
    if applicability is not None:
        if not isinstance(applicability, dict):
            raise RegistryError(f"policy {policy_id} applicability must be a mapping")
        path_globs = applicability.get("path_globs", {})
        if not isinstance(path_globs, dict):
            raise RegistryError(f"policy {policy_id} applicability.path_globs must be a mapping")
        for selector_kind, selector_values in path_globs.items():
            if not isinstance(selector_values, list):
                raise RegistryError(f"policy {policy_id} path_globs.{selector_kind} must be a list")
            for path_glob in selector_values:
                validate_repository_relative_path(
                    path_glob,
                    f"policy {policy_id} path_globs.{selector_kind}",
                )
        semantic_conditions = applicability.get("semantic_conditions", [])
        if not isinstance(semantic_conditions, list):
            raise RegistryError(f"policy {policy_id} semantic_conditions must be a list")
        for condition_id in semantic_conditions:
            validate_semantic_condition_id(condition_id)

    selectors = policy_node.get("selectors")
    if selectors is not None:
        if not isinstance(selectors, list):
            raise RegistryError(f"policy {policy_id} selectors must be a list")
        for selector_index, selector in enumerate(selectors):
            if not isinstance(selector, dict):
                raise RegistryError(f"policy {policy_id} selector {selector_index} must be a mapping")
            selector_path_globs = selector.get("path_globs", [])
            if not isinstance(selector_path_globs, list):
                raise RegistryError(
                    f"policy {policy_id} selector {selector_index}.path_globs must be a list"
                )
            for path_glob in selector_path_globs:
                validate_repository_relative_path(
                    path_glob,
                    f"policy {policy_id} selector {selector_index}.path_globs",
                )


def agent_rule_set_policy_ids(projection: dict[str, Any]) -> list[str]:
    """Collect policy IDs from the agent rule-set projection.

    Args:
        projection: ``agent_rule_sets`` projection metadata.

    Returns:
        Policy IDs in deterministic projection order.

    Raises:
        RegistryError: If projection sections have an invalid shape.
    """
    allowed_projection_fields = {"universal", "languages", "tools", "unknown_tool_fallback"}
    if set(projection) != allowed_projection_fields:
        raise RegistryError(
            "agent_rule_sets may contain only universal, languages, tools, and "
            "unknown_tool_fallback references"
        )
    universal_policy_ids = projection.get("universal")
    languages = projection.get("languages")
    tools = projection.get("tools")
    if not isinstance(universal_policy_ids, list):
        raise RegistryError("agent_rule_sets.universal must be a list")
    if not isinstance(languages, dict):
        raise RegistryError("agent_rule_sets.languages must be a mapping")
    if not isinstance(tools, dict):
        raise RegistryError("agent_rule_sets.tools must be a mapping")

    references = list(universal_policy_ids)
    for section_name, groups in (("languages", languages), ("tools", tools)):
        for group_name in sorted(groups):
            if not SEMANTIC_CONDITION_ID_PATTERN.fullmatch(group_name):
                raise RegistryError(
                    f"agent_rule_sets.{section_name} group {group_name} is not a safe identifier"
                )
            policy_ids = groups[group_name]
            if not isinstance(policy_ids, list):
                raise RegistryError(
                    f"agent_rule_sets.{section_name}.{group_name} must be a list"
                )
            references.extend(policy_ids)
    fallback_rule_set = projection.get("unknown_tool_fallback")
    known_rule_sets = {
        f"{section_name}/{group_name}"
        for section_name, groups in (("languages", languages), ("tools", tools))
        for group_name in groups
    }
    if not isinstance(fallback_rule_set, str) or fallback_rule_set not in known_rule_sets:
        raise RegistryError(
            "agent_rule_sets.unknown_tool_fallback must reference a focused rule set"
        )
    return references


def _policy_selector_values(policy_node: dict[str, Any]) -> tuple[list[str], list[str], list[str]]:
    """Extract path, ecosystem, and semantic selectors from one policy node.

    Args:
        policy_node: Canonical focused policy node.

    Returns:
        Tuple of path globs, ecosystems, and semantic conditions.
    """
    applicability = policy_node.get("applicability", {})
    path_globs = applicability.get("path_globs", {}) if isinstance(applicability, dict) else {}
    flattened_path_globs: list[str] = []
    if isinstance(path_globs, dict):
        for selector_kind in sorted(path_globs):
            values = path_globs[selector_kind]
            if isinstance(values, list):
                flattened_path_globs.extend(value for value in values if isinstance(value, str))
    ecosystems = policy_node.get("ecosystems", [])
    semantic_conditions = applicability.get("semantic_conditions", []) if isinstance(applicability, dict) else []
    return (
        flattened_path_globs,
        [value for value in ecosystems if isinstance(value, str)] if isinstance(ecosystems, list) else [],
        [value for value in semantic_conditions if isinstance(value, str)]
        if isinstance(semantic_conditions, list)
        else [],
    )


def _policy_route_metadata(policy_nodes: list[dict[str, Any]]) -> tuple[str, list[str]]:
    """Resolve maximum risk and the union of enforcement classifications.

    Args:
        policy_nodes: Matching focused policy nodes.

    Returns:
        Highest risk and ordered enforcement classification union.
    """
    risks: list[str] = []
    enforcements: list[str] = []

    def collect_enforcement(value: Any) -> None:
        if isinstance(value, dict):
            enforcement = value.get("enforcement")
            if isinstance(enforcement, str):
                if enforcement not in ENFORCEMENT_ORDER:
                    raise RegistryError(f"unknown enforcement classification {enforcement}")
                enforcements.append(enforcement)
            for child in value.values():
                collect_enforcement(child)
        elif isinstance(value, list):
            for child in value:
                collect_enforcement(child)

    for policy_node in policy_nodes:
        risk = policy_node.get("risk")
        if isinstance(risk, str):
            if risk not in RISK_ORDER:
                raise RegistryError(f"unknown risk classification {risk}")
            risks.append(risk)
        collect_enforcement(policy_node)
    highest_risk = max(risks, key=RISK_ORDER.index) if risks else "LOW"
    enforcement_union = [
        enforcement for enforcement in ENFORCEMENT_ORDER if enforcement in set(enforcements)
    ]
    return highest_risk, enforcement_union


def _build_security_rule_resolver():
    """Build the resolver around a closure-private evidence capability."""
    evidence_capability = object()

    class _ValidatedSemanticCondition:
        """Immutable predicate result gated by the closure-private capability."""

        __slots__ = ("_condition_id",)

        def __init__(self, condition_id: str, presented_capability: object) -> None:
            if presented_capability is not evidence_capability:
                raise RegistryError(
                    "validated semantic conditions require the private predicate capability"
                )
            object.__setattr__(self, "_condition_id", condition_id)

        def __setattr__(self, name: str, value: object) -> None:
            """Prevent mutation after predicate validation."""
            raise AttributeError("validated semantic conditions are immutable")

    def derive_semantic_conditions(
        semantic_observations: list[DependencyManifestObservation],
        declared_condition_ids: set[str],
    ) -> tuple[_ValidatedSemanticCondition, ...]:
        """Derive condition results from fixed predicates over typed facts."""
        derived_conditions: list[_ValidatedSemanticCondition] = []
        for observation in semantic_observations:
            if not isinstance(observation, DependencyManifestObservation):
                raise RegistryError(
                    "semantic observations must use a supported typed observation"
                )
            validate_repository_relative_path(
                observation.repository_relative_path,
                "dependency manifest observation path",
            )
            if not isinstance(observation.dependency_sources, tuple) or not all(
                isinstance(source, str) and source
                for source in observation.dependency_sources
            ):
                raise RegistryError("dependency manifest observation sources are invalid")

            git_sources = tuple(
                source
                for source in observation.dependency_sources
                if source.lower().startswith(("git+", "git://", "ssh://", "git@"))
                or source.lower().endswith(".git")
                or ".git@" in source.lower()
            )
            if not git_sources:
                continue
            condition_id = "dependency_manifest_contains_git_source"
            if condition_id not in declared_condition_ids:
                raise RegistryError(
                    f"predicate derived undeclared semantic condition {condition_id}"
                )
            derived_conditions.append(
                _ValidatedSemanticCondition(condition_id, evidence_capability)
            )
        return tuple(derived_conditions)

    def resolve_security_rule_route(
        policies: dict[str, Any],
        affected_paths: list[str],
        observed_ecosystems: list[str],
        semantic_observations: list[DependencyManifestObservation],
    ) -> dict[str, Any]:
        """Resolve focused rules from paths, ecosystems, and derived observations.

        The source API exposes no condition-ID or evidence-minting parameter.
        Semantic conditions are immutable results of fixed predicates over typed
        observations. This capability pattern prevents ordinary accidental or
        self-attested condition minting; Python reflection and forged input facts
        are not sandbox-grade security boundaries and require process isolation
        when hostile in-process callers are in scope.

        Args:
            policies: Parsed canonical policy registry.
            affected_paths: Repository-relative paths affected by the task.
            observed_ecosystems: Tool or language ecosystems observed by trusted analysis.
            semantic_observations: Typed raw facts evaluated by internal predicates.

        Returns:
            Selected focused sets, maximum risk, and enforcement union.

        Raises:
            RegistryError: If observations, projection references, or selectors are invalid.
        """
        secure_policy = policies.get("secure_sdd_policy", {})
        projection = secure_policy.get("agent_rule_sets", {}) if isinstance(secure_policy, dict) else {}
        if not isinstance(projection, dict):
            raise RegistryError("secure_sdd_policy.agent_rule_sets must be a mapping")
        resolved_nodes = resolve_policy_ids(policies, agent_rule_set_policy_ids(projection))
        for policy_id, policy_node in resolved_nodes.items():
            validate_projected_policy_node(policy_id, policy_node)
        normalized_affected_paths = [
            validate_repository_relative_path(affected_path, "affected path")
            for affected_path in affected_paths
        ]
        matching_rule_sets: set[str] = set()
        known_ecosystems: set[str] = set()
        declared_condition_ids: set[str] = set()
        for policy_node in resolved_nodes.values():
            _, _, conditions = _policy_selector_values(policy_node)
            declared_condition_ids.update(conditions)
        validated_conditions = derive_semantic_conditions(
            semantic_observations,
            declared_condition_ids,
        )
        derived_condition_ids = {
            condition._condition_id for condition in validated_conditions
        }

        for section_name in ("languages", "tools"):
            groups = projection[section_name]
            for group_name, policy_ids in groups.items():
                group_matches = False
                for policy_id in policy_ids:
                    policy_node = resolved_nodes[policy_id]
                    path_globs, ecosystems, conditions = _policy_selector_values(policy_node)
                    known_ecosystems.update(ecosystems)
                    path_matches = any(
                        fnmatch.fnmatchcase(path, path_glob)
                        for path in normalized_affected_paths
                        for path_glob in path_globs
                    )
                    ecosystem_matches = bool(set(observed_ecosystems) & set(ecosystems))
                    semantic_matches = bool(derived_condition_ids & set(conditions))
                    group_matches = (
                        group_matches
                        or path_matches
                        or ecosystem_matches
                        or semantic_matches
                    )
                if group_matches:
                    matching_rule_sets.add(f"{section_name}/{group_name}")

        unknown_ecosystems = set(observed_ecosystems) - known_ecosystems
        fallback_rule_set = projection.get("unknown_tool_fallback")
        if not isinstance(fallback_rule_set, str) or not fallback_rule_set.strip():
            raise RegistryError(
                "agent_rule_sets.unknown_tool_fallback must be a rule-set reference"
            )
        if unknown_ecosystems:
            matching_rule_sets.add(fallback_rule_set)

        matching_nodes: list[dict[str, Any]] = []
        for rule_set in sorted(matching_rule_sets):
            section_name, group_name = rule_set.split("/", 1)
            groups = projection.get(section_name, {})
            if not isinstance(groups, dict) or group_name not in groups:
                raise RegistryError(f"unknown focused rule-set reference {rule_set}")
            matching_nodes.extend(
                resolved_nodes[policy_id] for policy_id in groups[group_name]
            )
        risk, enforcements = _policy_route_metadata(matching_nodes)
        return {
            "universal_rule_set": "universal.md",
            "focused_rule_sets": sorted(matching_rule_sets),
            "risk": risk,
            "enforcements": enforcements,
        }

    return resolve_security_rule_route


resolve_security_rule_route = _build_security_rule_resolver()
del _build_security_rule_resolver


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
