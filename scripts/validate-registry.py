#!/usr/bin/env python3
from __future__ import annotations

import sys
import re
from pathlib import Path

import registry_lib
from registry_lib import ROOT, RegistryError, load_registry


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
SECURE_SDD_STAGE_IDS = [
    "specify", "clarify", "independent_spec_review", "plan", "architecture_review",
    "checklist", "tasks", "verification_plan", "analyze", "implement",
    "adversarial_test", "deterministic_verify", "security_review",
    "final_independent_review", "converge", "policy_gate",
]
CONDITIONAL_RESULT_STATUSES = {"reviewed", "escalated", "not_applicable"}
CONDITIONAL_RESULT_FIELDS = {
    "architecture_review": {
        "reviewed": {
            "review_evidence", "findings", "decision_rationale", "infrastructure_assessment",
            "sandbox_privilege_assessment", "dependency_provenance_lock_integrity_assessment",
        },
        "escalated": {"escalation_workflow_id", "escalation_handoff", "blocking_disposition"},
        "not_applicable": {"not_applicable_basis", "condition_evidence"},
    },
    "security_review": {
        "reviewed": {"review_evidence", "findings", "residual_risks", "remediation_requirements"},
        "escalated": {"escalation_workflow_id", "escalation_handoff", "blocking_disposition"},
        "not_applicable": {"not_applicable_basis", "risk_evidence"},
    },
}
CONDITIONAL_RESULT_CONSUMERS = {
    "architecture_review": {"CHECKLIST"},
    "security_review": {"FINAL INDEPENDENT REVIEW", "CONVERGE", "POLICY GATE"},
}
RESIDUAL_RISK_EVIDENCE_FIELDS = {
    "explicit_risk_classification", "remediation_evidence", "fresh_independent_re_review_evidence",
}
RISK_LEVELS = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
INDEPENDENT_REVIEW_STAGE_IDS = {
    "independent_spec_review", "architecture_review", "analyze", "security_review", "final_independent_review",
}
PORTABLE_SDD_HEADINGS = {
    "Core Rules", "Development Workflow", "Specification", "Planning",
    "Independent Verification", "Deterministic Verification", "Dependency Security",
    "Sandbox", "Prompt Injection", "Security", "Risk", "Human Escalation", "Completion",
}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def load_policy_yaml(path: Path) -> object:
    """Parse policy YAML, including mappings nested inside list items.

    Args:
        path: Path to the policy YAML file.

    Returns:
        Parsed YAML value.

    Raises:
        RegistryError: If the restricted YAML syntax or indentation is invalid.
    """
    return registry_lib.load_yaml(path)


def load_registry_for_validation() -> dict:
    """Load registry content with the policy nested-list parser extension."""
    policies = load_policy_yaml(ROOT / "registry" / "policies.yaml")
    if not isinstance(policies, dict):
        raise RegistryError("Registry file must contain a mapping: registry/policies.yaml")
    return {
        "skills": load_registry("skills").get("skills", []),
        "mcp_servers": registry_lib.load_mcp_catalog(),
        "agents": load_registry("agents").get("agents", []),
        "workflows": load_registry("workflows").get("workflows", []),
        "profiles": load_registry("profiles").get("profiles", []),
        "tasks": load_registry("tasks").get("tasks", []),
        "keyword_categories": load_registry("keyword-categories").get("keyword_categories", {}),
        "policies": policies,
    }


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


def collect_references(value: object, key_names: set[str]) -> list[str]:
    """Collect string values stored under selected mapping keys.

    Args:
        value: Manifest value to traverse.
        key_names: Mapping keys whose scalar values are references.

    Returns:
        Referenced identifiers in deterministic traversal order.
    """
    references: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in key_names and isinstance(child, str):
                references.append(child)
            references.extend(collect_references(child, key_names))
    elif isinstance(value, list):
        for child in value:
            references.extend(collect_references(child, key_names))
    return references


def contains_template_dependency(value: object) -> bool:
    """Return whether a manifest value references a workflow template path."""
    if isinstance(value, str):
        return "workflows/templates/" in value
    if isinstance(value, dict):
        return any(contains_template_dependency(child) for child in value.values())
    if isinstance(value, list):
        return any(contains_template_dependency(child) for child in value)
    return False


def validate_secure_sdd_manifest(
    workflow: dict,
    workflow_ids: set[str],
    task_ids: set[str],
    role_ids: set[str],
    policy_ids: set[str],
) -> list[str]:
    """Validate deterministic static semantics for a Secure SDD manifest.

    Args:
        workflow: Parsed Secure SDD workflow manifest.
        workflow_ids: Registered workflow identifiers.
        task_ids: Registered task identifiers.
        role_ids: Registered role identifiers.
        policy_ids: Registered policy/control identifiers.

    Returns:
        Validation errors, ordered by the deterministic validation sequence.
    """
    errors: list[str] = []
    stages = workflow.get("stages", [])
    if not isinstance(stages, list):
        return ["secure-sdd: stages must be a list"]

    stage_ids = [stage.get("id") for stage in stages if isinstance(stage, dict)]
    if stage_ids != SECURE_SDD_STAGE_IDS:
        errors.append("secure-sdd: stages must match the exact required stage sequence")
    if len(stage_ids) != len(set(stage_ids)):
        errors.append("secure-sdd: stage ids must be unique")
    stages_by_id = {stage.get("id"): stage for stage in stages if isinstance(stage, dict)}
    analyze_stage = stages_by_id.get("analyze", {})
    required_analyze_outputs = {
        "pre_implementation_independent_risk_review", "prompt_injection_assessment",
        "dependency_provenance_quarantine_integrity_assessment", "sandbox_privilege_assessment",
        "risk_classification", "unresolved_risk_findings", "pre_implementation_risk_review_disposition",
        "pre_implementation_risk_review_escalation",
    }
    if not required_analyze_outputs <= set(analyze_stage.get("outputs", [])) or analyze_stage.get("gate", {}).get("type") != "independent_risk_review":
        errors.append("secure-sdd: ANALYZE mandatory independent risk-topic evidence is invalid")
    final_review_stage = stages_by_id.get("final_independent_review", {})
    required_final_inputs = {
        "clarified_specification", "checklist_status", "implementation_change_summary", "adversarial_test_results",
        "adversarial_test_disposition", "regression_results", "deterministic_verification_results", "risk_assessment",
        "architecture_review_result", "security_review_result",
    }
    # The conditional-result contract below emits the precise missing security
    # review diagnostic, avoiding two errors for the same absent artifact.
    foundational_final_inputs = required_final_inputs - {"security_review_result"}
    if not foundational_final_inputs <= set(final_review_stage.get("inputs", [])):
        errors.append("secure-sdd: FINAL INDEPENDENT REVIEW required evidence inputs are invalid")

    process_metadata = workflow.get("process_metadata", {})
    independent_reviewers = process_metadata.get("independent_reviewers", {}) if isinstance(process_metadata, dict) else {}
    role_separation = process_metadata.get("role_separation", []) if isinstance(process_metadata, dict) else []
    if not isinstance(role_separation, list) or not role_separation:
        errors.append("secure-sdd: process_metadata.role_separation declaration is required")
    if not isinstance(independent_reviewers, dict) or independent_reviewers.get("fresh") is not True or independent_reviewers.get("read_only") is not True:
        errors.append("secure-sdd: fresh read-only independent reviewer declaration is required")

    implementation_stage = stages_by_id.get("implement", {})
    implementation_role_values = implementation_stage.get("roles", []) if isinstance(implementation_stage, dict) else []
    implementation_roles = {
        role_id for role_id in implementation_role_values if isinstance(role_id, str) and role_id
    }
    review_roles = set()
    for stage in stages:
        if not isinstance(stage, dict):
            errors.append("secure-sdd: each stage must be a mapping")
            continue
        stage_id = stage.get("id", "<unknown>")
        stage_roles = stage.get("roles")
        if not isinstance(stage_roles, list) or not stage_roles:
            errors.append(f"secure-sdd: stage {stage_id} must declare a nonempty role list")
            stage_roles = []
        for role_id in stage_roles:
            if not isinstance(role_id, str) or not role_id:
                errors.append(f"secure-sdd: stage {stage_id} role must be a nonempty string")
            elif role_id not in role_ids:
                errors.append(f"secure-sdd: unknown stage role {role_id}")
        gate_type = stage.get("gate", {}).get("type") if isinstance(stage.get("gate"), dict) else None
        if stage_id in INDEPENDENT_REVIEW_STAGE_IDS or (isinstance(gate_type, str) and "independent_review" in gate_type):
            if not isinstance(stage_roles, list) or not stage_roles:
                errors.append(f"secure-sdd: independent review stage {stage_id} requires reviewers")
            else:
                review_roles.update(role_id for role_id in stage_roles if isinstance(role_id, str) and role_id)
    overlap = sorted(implementation_roles & review_roles)
    if overlap:
        errors.append(f"secure-sdd: implementation and independent review roles overlap: {overlap}")

    conditional_results = workflow.get("conditional_stage_results") or process_metadata.get("conditional_stage_results", {})
    if not isinstance(conditional_results, dict):
        errors.append("secure-sdd: conditional_stage_results must be a mapping")
        conditional_results = {}
    for stage_id, artifact_name in (("architecture_review", "architecture_review_result"), ("security_review", "security_review_result")):
        result_contract = conditional_results.get(stage_id, {})
        statuses = result_contract.get("required_status_values", []) if isinstance(result_contract, dict) else []
        if not isinstance(result_contract, dict) or result_contract.get("artifact") != artifact_name:
            errors.append(f"secure-sdd: {stage_id} conditional result artifact must be {artifact_name}")
        if set(statuses) != CONDITIONAL_RESULT_STATUSES or len(statuses) != len(CONDITIONAL_RESULT_STATUSES):
            errors.append(f"secure-sdd: {stage_id} conditional result statuses must be reviewed, escalated, not_applicable")
        required_fields = result_contract.get("status_specific_required_fields", {}) if isinstance(result_contract, dict) else {}
        for status, expected_fields in CONDITIONAL_RESULT_FIELDS[stage_id].items():
            actual_fields = required_fields.get(status, []) if isinstance(required_fields, dict) else []
            if set(actual_fields) != expected_fields or len(actual_fields) != len(expected_fields):
                errors.append(f"secure-sdd: {stage_id} {status} required fields are invalid")
        consumers = result_contract.get("consumed_by", []) if isinstance(result_contract, dict) else []
        if set(consumers) != CONDITIONAL_RESULT_CONSUMERS[stage_id]:
            errors.append(f"secure-sdd: {stage_id} conditional result consumers are invalid")
        for consumer_name in consumers if isinstance(consumers, list) else []:
            consumer_id = consumer_name.lower().replace(" ", "_")
            consumer_stage = stages_by_id.get(consumer_id, {})
            consumer_inputs = consumer_stage.get("inputs", []) if isinstance(consumer_stage, dict) else []
            if artifact_name not in consumer_inputs:
                errors.append(f"secure-sdd: {consumer_name} must consume {artifact_name}")
        stage = stages_by_id.get(stage_id, {})
        if stage.get("conditional") is not True or stage.get("outputs") != [artifact_name]:
            errors.append(f"secure-sdd: {stage_id} must be conditional and emit only {artifact_name}")

    verification = stages_by_id.get("deterministic_verify", {})
    verification_outputs = verification.get("outputs", []) if isinstance(verification, dict) else []
    expected_failure_outputs = {"failed_verification_evidence", "verification_exception_request"}
    if not expected_failure_outputs <= set(verification_outputs) or "deterministic_verification_results" not in verification_outputs:
        errors.append("secure-sdd: deterministic verification must emit results and failure evidence")
    if verification.get("gate", {}).get("type") != "deterministic_verification":
        errors.append("secure-sdd: deterministic verification gate is required")
    remediation_contract = process_metadata.get("remediation_and_re_review", {})
    blocking_findings = (
        remediation_contract.get("blocking_findings", [])
        if isinstance(remediation_contract, dict)
        else []
    )
    if not isinstance(blocking_findings, list) or not blocking_findings:
        errors.append("secure-sdd: remediation blocking-finding contract is required")
    residual_risk_disposition = (
        remediation_contract.get("residual_risk_disposition", {})
        if isinstance(remediation_contract, dict)
        else {}
    )
    residual_evidence = (
        residual_risk_disposition.get("required_evidence", [])
        if isinstance(residual_risk_disposition, dict)
        else []
    )
    if set(residual_evidence) != RESIDUAL_RISK_EVIDENCE_FIELDS or len(residual_evidence) != len(RESIDUAL_RISK_EVIDENCE_FIELDS):
        errors.append("secure-sdd: residual-risk evidence contract is invalid")
    if not isinstance(residual_risk_disposition, dict) or residual_risk_disposition.get("rejection_route") != "IMPLEMENT":
        errors.append("secure-sdd: residual-risk rejection route must be IMPLEMENT")

    risk_metadata = workflow.get("risk_metadata", {})
    risk = risk_metadata.get("risk") if isinstance(risk_metadata, dict) else None
    human_escalation = workflow.get("human_escalation") or process_metadata.get("human_escalation", {})
    policy_gate = stages_by_id.get("policy_gate", {})
    if risk in {"HIGH", "CRITICAL"} and (
        risk_metadata.get("required_reviewer") != "independent_security_reviewer"
        or risk_metadata.get("human_approval") != "required"
        or
        not isinstance(human_escalation, dict)
        or not human_escalation.get("required_when")
        or policy_gate.get("gate", {}).get("type") != "human_policy_gate"
    ):
        errors.append("secure-sdd: HIGH/CRITICAL risk requires human and security gate metadata")
    if risk is not None and risk not in RISK_LEVELS:
        errors.append("secure-sdd: risk metadata must use an allowed risk level")
    if workflow.get("id") == "secure-sdd" and policy_gate.get("gate", {}).get("type") != "human_policy_gate":
        errors.append("secure-sdd: POLICY GATE must be a human policy gate")
    restrictions = human_escalation.get("restrictions", []) if isinstance(human_escalation, dict) else []
    normalized_restrictions = " ".join(
        restriction.lower() for restriction in restrictions if isinstance(restriction, str)
    )
    if "cannot be waived" not in normalized_restrictions or "residual risk" not in normalized_restrictions:
        errors.append(
            "secure-sdd: human escalation must not waive blocking findings or dispose unremediated risk"
        )
    policy_gate_criteria = policy_gate.get("acceptance_criteria", []) if isinstance(policy_gate, dict) else []
    normalized_policy_gate_criteria = " ".join(
        criterion.lower() for criterion in policy_gate_criteria if isinstance(criterion, str)
    )
    if "cannot be waived" not in normalized_policy_gate_criteria or "residual risk" not in normalized_policy_gate_criteria:
        errors.append(
            "secure-sdd: POLICY GATE must reject blocker waivers and limit disposition to residual risk"
        )

    for role_id in collect_references(workflow, {"role_id"}):
        if role_id not in role_ids:
            errors.append(f"secure-sdd: unknown role reference {role_id}")
    for workflow_id in collect_references(workflow, {"workflow_id"}):
        if workflow_id not in workflow_ids:
            errors.append(f"secure-sdd: unknown workflow reference {workflow_id}")
    for task_id in collect_references(workflow, {"task_id"}):
        if task_id not in task_ids:
            errors.append(f"secure-sdd: unknown task reference {task_id}")
    for policy_id in collect_references(workflow, {"policy_id", "policy_reference"}):
        if policy_id not in policy_ids:
            errors.append(f"secure-sdd: unknown policy reference {policy_id}")
    if contains_template_dependency(workflow):
        errors.append("secure-sdd: workflow templates must not be a manifest dependency")
    return errors


def validate_portable_sdd_guidance(path: Path, errors: list[str]) -> None:
    """Validate that portable SDD guidance has no registry or model dependency."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"AGENTS.md.sdd: unable to read portable guidance: {exc}")
        return
    headings = set(re.findall(r"^##\s+(.+?)\s*$", content, flags=re.MULTILINE))
    missing_headings = sorted(PORTABLE_SDD_HEADINGS - headings)
    require(not missing_headings, f"AGENTS.md.sdd: missing required headings {missing_headings}", errors)
    workflow_tokens = [
        "specify", "clarify", "independent spec review", "plan", "architecture review when required",
        "checklist", "tasks", "verification plan", "analyze", "implement", "adversarial test",
        "deterministic verify", "security review when required", "independent final review", "converge",
        "POLICY GATE",
    ]
    development_workflow_match = re.search(
        r"^##\s+Development Workflow\s*$([\s\S]*?)(?=^##\s+|\Z)",
        content,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    development_workflow_content = (
        development_workflow_match.group(1) if development_workflow_match else ""
    )
    next_token_start = 0
    workflow_order_is_valid = True
    for workflow_token in workflow_tokens:
        token_pattern = r"\s+".join(
            re.escape(token_word) for token_word in workflow_token.split()
        )
        token_match = re.search(
            rf"(?<!\w){token_pattern}(?!\w)",
            development_workflow_content[next_token_start:],
            flags=re.IGNORECASE,
        )
        if token_match is None:
            workflow_order_is_valid = False
            break
        next_token_start += token_match.end()
    require(
        workflow_order_is_valid,
        "AGENTS.md.sdd: Development Workflow must contain canonical POLICY GATE order",
        errors,
    )
    forbidden_patterns = {
        "registry dependency": r"(?i)\bregistry(?:/|\s+(?:dependency|requirement|configuration|reference))",
        "provider dependency": r"(?i)\bprovider\s+(?:selection|configuration|requirement|model|id|name|version)\b",
        "model dependency": r"(?i)\b(?:ai\s+)?model\s+(?:selection|configuration|requirement|id|name|version)\b",
        "runtime dependency": r"(?i)\bruntime\s+(?:dependency|requirement|configuration|selection|id|name|version)\b",
        "self requirement": r"(?i)(?:require|must use|depends on).*AGENTS\.md\.sdd",
    }
    for description, pattern in forbidden_patterns.items():
        require(re.search(pattern, content) is None, f"AGENTS.md.sdd: forbidden {description}", errors)


def validate_sdd_artifact_independence(
    portable_guidance: str,
    secure_sdd_manifest: dict,
    errors: list[str],
    artifact_root: Path | None = None,
) -> None:
    """Validate independence in both directions between portable and workflow SDD.

    Args:
        portable_guidance: AGENTS.md.sdd content.
        secure_sdd_manifest: Parsed Secure SDD workflow manifest.
        errors: List accumulating validation errors.
    """
    portable_dependency_pattern = re.compile(
        r"(?i)(?:secure[-_ ]sdd|workflows/security-compliance/secure-sdd)"
    )
    if portable_dependency_pattern.search(portable_guidance):
        errors.append("SDD independence: AGENTS.md.sdd must not depend on Secure SDD")

    serialized_manifest = repr(secure_sdd_manifest)
    if re.search(r"(?i)AGENTS\.md\.sdd", serialized_manifest):
        errors.append("SDD independence: Secure SDD must not depend on AGENTS.md.sdd")
    if artifact_root is not None and artifact_root.is_dir():
        root_path = artifact_root.resolve()
        for artifact_path in sorted(artifact_root.rglob("*")):
            if artifact_path.is_symlink():
                errors.append("SDD independence: Secure SDD artifact root must not contain symlinks")
                break
        if errors:
            return
        for artifact_path in sorted(artifact_root.rglob("*")):
            if not artifact_path.is_file():
                continue
            try:
                artifact_content = artifact_path.read_text(encoding="utf-8")
            except OSError:
                errors.append(f"SDD independence: unable to read artifact {artifact_path.relative_to(artifact_root)}")
                continue
            if re.search(r"(?i)AGENTS\.md\.sdd", artifact_content):
                errors.append("SDD independence: Secure SDD artifacts must not depend on AGENTS.md.sdd")
                break
        if errors:
            return
        pending_artifacts = [path for path in (artifact_root / "workflow.md", artifact_root / "workflow.yaml") if path.is_file()]
        visited_artifacts: set[Path] = set()
        while pending_artifacts:
            artifact_path = pending_artifacts.pop()
            resolved_artifact = artifact_path.resolve()
            if resolved_artifact in visited_artifacts:
                continue
            visited_artifacts.add(resolved_artifact)
            artifact_content = artifact_path.read_text(encoding="utf-8")
            for reference in re.findall(r"(?:\]\(|\bpath:\s*[\"']?)([^\s)\"']+)", artifact_content):
                if re.match(r"(?i)[a-z][a-z0-9+.-]*:", reference) or reference.startswith("//"):
                    errors.append("SDD independence: Secure SDD artifact reference escapes approved root")
                    break
                local_reference = re.split(r"[?#]", reference, maxsplit=1)[0]
                candidate = (artifact_path.parent / local_reference).resolve()
                if root_path not in candidate.parents and candidate != root_path:
                    errors.append("SDD independence: Secure SDD artifact reference escapes approved root")
                    break
                if candidate.is_file():
                    pending_artifacts.append(candidate)


def validate_secure_sdd_policy(policy: dict, errors: list[str]) -> None:
    """Validate required security and human gate metadata in the policy.

    Args:
        policy: Parsed secure_sdd_policy mapping.
        errors: List accumulating validation errors.
    """
    risk_model = policy.get("risk_model", {}) if isinstance(policy, dict) else {}
    levels = risk_model.get("levels", {}) if isinstance(risk_model, dict) else {}
    review_gates = risk_model.get("review_gates", {}) if isinstance(risk_model, dict) else {}
    high_level = levels.get("HIGH", {}) if isinstance(levels, dict) else {}
    critical_level = levels.get("CRITICAL", {}) if isinstance(levels, dict) else {}
    high_gate = review_gates.get("HIGH", {}) if isinstance(review_gates, dict) else {}
    critical_gate = review_gates.get("CRITICAL", {}) if isinstance(review_gates, dict) else {}
    require(high_level.get("minimum_review") == "independent_security_review", "secure-sdd policy: HIGH requires independent security review", errors)
    require(high_gate.get("required_reviewer") == "independent_security_reviewer", "secure-sdd policy: HIGH requires independent security reviewer metadata", errors)
    require(
        high_gate.get("human_approval") == "required_only_when_an_applicable_control_defines_a_human_gate",
        "secure-sdd policy: HIGH human approval metadata is invalid",
        errors,
    )
    require(critical_level.get("minimum_review") == "independent_security_review_then_human_gate", "secure-sdd policy: CRITICAL requires security review then human gate", errors)
    require(critical_gate.get("required_reviewer") == "independent_security_reviewer", "secure-sdd policy: CRITICAL requires independent security reviewer metadata", errors)
    require(critical_gate.get("human_approval") == "required", "secure-sdd policy: CRITICAL requires human approval metadata", errors)
    required_categories = {
        "package_quarantine": "dependency quarantine",
        "protected_files": "trusted-file protections",
    }
    contracts = policy.get("contracts", {}) if isinstance(policy, dict) else {}
    for contract_name, description in {"dependency": "dependency review", "sandbox": "sandbox contract"}.items():
        require(isinstance(contracts, dict) and isinstance(contracts.get(contract_name), dict), f"secure-sdd policy: missing {description} contract", errors)
    for category, description in required_categories.items():
        require(isinstance(policy.get(category), dict), f"secure-sdd policy: missing {description}", errors)
    require(isinstance(policy.get("ecosystem_security_defaults"), dict), "secure-sdd policy: missing ecosystem defaults", errors)
    controls = policy.get("controls", []) if isinstance(policy, dict) else []
    control_ids = {control.get("id") for control in controls if isinstance(control, dict)}
    for control_id, description in {
        "SDD-PROMPT-INJECTION-001": "prompt injection control",
        "SDD-HUMAN-ESCALATION-001": "HUMAN gate control",
    }.items():
        require(control_id in control_ids, f"secure-sdd policy: missing {description}", errors)
    protected_files = policy.get("protected_files", {}) if isinstance(policy, dict) else {}
    protected_paths = protected_files.get("paths", []) if isinstance(protected_files, dict) else []
    require(".github/**" in protected_paths and "registry/policies.yaml" in protected_paths, "secure-sdd policy: trusted-file protections are incomplete", errors)


def validate_agent_rule_sets(policy: dict, errors: list[str]) -> None:
    """Validate policy projection references, coverage, and focused selectors.

    Args:
        policy: Parsed ``secure_sdd_policy`` mapping.
        errors: List accumulating validation errors.
    """
    projection = policy.get("agent_rule_sets") if isinstance(policy, dict) else None
    if not isinstance(projection, dict):
        errors.append("security rules: agent_rule_sets must be a mapping")
        return
    allowed_projection_fields = {"universal", "languages", "tools", "unknown_tool_fallback"}
    require(
        set(projection) == allowed_projection_fields,
        "security rules: agent_rule_sets may contain only universal, languages, tools, and unknown_tool_fallback references",
        errors,
    )

    policies_wrapper = {"secure_sdd_policy": policy}
    try:
        policy_nodes = registry_lib.index_policy_nodes(policies_wrapper)
        projected_policy_ids = registry_lib.agent_rule_set_policy_ids(projection)
        projected_policy_nodes = registry_lib.resolve_policy_ids(
            policies_wrapper,
            projected_policy_ids,
        )
    except RegistryError as exc:
        errors.append(f"security rules: {exc}")
        return
    for policy_id, policy_node in projected_policy_nodes.items():
        unsupported_fields = sorted(
            set(policy_node) - registry_lib.PROJECTED_POLICY_RENDER_FIELDS
        )
        if unsupported_fields:
            errors.append(
                f"security rules: policy {policy_id} has unsupported fields {unsupported_fields}"
            )
            continue
        try:
            registry_lib.validate_projected_policy_node(policy_id, policy_node)
        except RegistryError as exc:
            errors.append(f"security rules: {exc}")

    universal_policy_ids = projection.get("universal", [])
    require(bool(universal_policy_ids), "security rules: universal projection must not be empty", errors)
    require(
        "SDD-PROMPT-INJECTION-001" in universal_policy_ids,
        "security rules: universal projection must include SDD-PROMPT-INJECTION-001",
        errors,
    )
    require(
        "SDD-CREDENTIAL-SELECTORS-001" in universal_policy_ids,
        "security rules: universal projection must include SDD-CREDENTIAL-SELECTORS-001",
        errors,
    )
    credential_selector_policy = policy_nodes.get("SDD-CREDENTIAL-SELECTORS-001", {})
    credential_selectors = credential_selector_policy.get("selectors")
    if not isinstance(credential_selectors, list) or not credential_selectors:
        errors.append("security rules: credential-bearing selectors must be a nonempty list")
    else:
        for selector_index, selector in enumerate(credential_selectors):
            if not isinstance(selector, dict):
                errors.append(
                    f"security rules: credential-bearing selector {selector_index} must be a mapping"
                )
                continue
            for selector_field in ("ecosystems", "path_globs"):
                selector_values = selector.get(selector_field)
                require(
                    isinstance(selector_values, list)
                    and bool(selector_values)
                    and all(isinstance(value, str) and bool(value) for value in selector_values),
                    f"security rules: credential-bearing selector {selector_index}.{selector_field} must be a nonempty string list",
                    errors,
                )
            selector_path_globs = selector.get("path_globs")
            if isinstance(selector_path_globs, list):
                for path_glob in selector_path_globs:
                    try:
                        registry_lib.validate_repository_relative_path(
                            path_glob,
                            f"credential-bearing selector {selector_index}.path_globs",
                        )
                    except RegistryError as exc:
                        errors.append(f"security rules: {exc}")
    match_handling = credential_selector_policy.get("match_handling", {})
    require(
        isinstance(match_handling, dict)
        and match_handling.get("read_values_by_default") is False
        and match_handling.get("log_or_persist_values") is False,
        "security rules: credential-bearing selector handling must prohibit default reads and value disclosure",
        errors,
    )

    ecosystem_defaults = policy.get("ecosystem_security_defaults", {})
    focused_categories = {
        "languages": ecosystem_defaults.get("languages", []) if isinstance(ecosystem_defaults, dict) else [],
        "tools": ecosystem_defaults.get("tools", []) if isinstance(ecosystem_defaults, dict) else [],
    }
    focused_policy_sections = {
        str(policy_node.get("id")): section_name
        for section_name, focused_nodes in focused_categories.items()
        if isinstance(focused_nodes, list)
        for policy_node in focused_nodes
        if isinstance(policy_node, dict)
    }
    projected_reference_counts: dict[str, int] = {}
    for section_name in ("languages", "tools"):
        groups = projection.get(section_name, {})
        if not isinstance(groups, dict):
            continue
        for group_name, policy_ids in groups.items():
            if not isinstance(group_name, str) or not group_name:
                errors.append(f"security rules: {section_name} group names must be non-empty strings")
                continue
            if not isinstance(policy_ids, list) or not policy_ids:
                errors.append(f"security rules: {section_name}.{group_name} must reference at least one policy ID")
                continue
            for policy_id in policy_ids:
                if isinstance(policy_id, str):
                    projected_reference_counts[policy_id] = projected_reference_counts.get(policy_id, 0) + 1
                    policy_node = policy_nodes.get(policy_id, {})
                    require(
                        policy_node.get("group") == group_name,
                        f"security rules: projection {section_name}.{group_name} does not match policy group {policy_id}",
                        errors,
                    )
                    require(
                        focused_policy_sections.get(policy_id) == section_name,
                        f"security rules: focused policy {policy_id} is projected under the wrong category",
                        errors,
                    )

    for section_name, focused_nodes in focused_categories.items():
        if not isinstance(focused_nodes, list):
            errors.append(f"security rules: ecosystem_security_defaults.{section_name} must be a list")
            continue
        for policy_node in focused_nodes:
            if not isinstance(policy_node, dict):
                errors.append(f"security rules: {section_name} policies must be mappings")
                continue
            policy_id = policy_node.get("id", "<unknown>")
            require(
                projected_reference_counts.get(str(policy_id), 0) == 1,
                f"security rules: focused policy {policy_id} must have exactly one projection reference",
                errors,
            )
            ecosystems = policy_node.get("ecosystems")
            require(
                isinstance(ecosystems, list)
                and bool(ecosystems)
                and all(isinstance(value, str) and bool(value) for value in ecosystems),
                f"security rules: policy {policy_id} ecosystems must be a nonempty string list",
                errors,
            )
            applicability = policy_node.get("applicability")
            if not isinstance(applicability, dict):
                errors.append(f"security rules: policy {policy_id} applicability must be a mapping")
                continue
            path_globs = applicability.get("path_globs")
            if not isinstance(path_globs, dict):
                errors.append(
                    f"security rules: policy {policy_id} applicability.path_globs must be a mapping"
                )
            else:
                for selector_kind in ("manifests", "lockfiles", "config_files"):
                    selector_values = path_globs.get(selector_kind)
                    require(
                        isinstance(selector_values, list)
                        and all(isinstance(value, str) and bool(value) for value in selector_values),
                        f"security rules: policy {policy_id} path_globs.{selector_kind} must be a string list",
                        errors,
                    )
                    if isinstance(selector_values, list):
                        for selector_value in selector_values:
                            try:
                                registry_lib.validate_repository_relative_path(
                                    selector_value,
                                    f"policy {policy_id} path_globs.{selector_kind}",
                                )
                            except RegistryError:
                                errors.append(
                                    f"security rules: policy {policy_id} path_globs.{selector_kind} "
                                    f"contains unsafe repository path {selector_value}"
                                )
            semantic_conditions = applicability.get("semantic_conditions")
            require(
                isinstance(semantic_conditions, list)
                and all(isinstance(value, str) and bool(value) for value in semantic_conditions),
                f"security rules: policy {policy_id} semantic_conditions must be a string list",
                errors,
            )
            if isinstance(semantic_conditions, list):
                for condition_id in semantic_conditions:
                    try:
                        registry_lib.validate_semantic_condition_id(condition_id)
                    except RegistryError:
                        errors.append(
                            f"security rules: policy {policy_id} semantic condition ID "
                            f"{condition_id} is invalid"
                        )

    fallback_rule_set = projection.get("unknown_tool_fallback")
    require(
        isinstance(fallback_rule_set, str)
        and fallback_rule_set in {
            f"{section_name}/{group_name}"
            for section_name in ("languages", "tools")
            for group_name in projection.get(section_name, {})
        },
        "security rules: unknown_tool_fallback must reference a focused rule set",
        errors,
    )


def validate_route_manifest(manifest: dict, workflow_id: str, errors: list[str]) -> None:
    """Validate static invariants unique to non-Secure-SDD routes."""
    stages = manifest.get("stages", [])
    stage_ids = [stage.get("id") for stage in stages if isinstance(stage, dict)] if isinstance(stages, list) else []
    if workflow_id == "bugfix":
        require(stage_ids == ["assess", "fix", "test", "verify", "independent_review"], "bugfix: stage route semantics are invalid", errors)
        metadata = manifest.get("process_metadata", {})
        escalation = metadata.get("escalation", {}) if isinstance(metadata, dict) else {}
        require(escalation.get("workflow_id") == "secure-sdd" and escalation.get("terminal_outcome") == "escalated_to_secure_sdd", "bugfix: Secure SDD escalation handoff is invalid", errors)
    if workflow_id == "idea-validation":
        require(stage_ids == ["capture", "evidence", "refine", "design", "decision"], "idea-validation: stage route semantics are invalid", errors)
        decision = manifest.get("decision_metadata", {})
        require(isinstance(decision, dict) and decision.get("outcomes") == ["GO", "CLARIFY", "KILL"], "idea-validation: decision outcomes are invalid", errors)
        handoff = decision.get("go_handoff", {}) if isinstance(decision, dict) else {}
        require(isinstance(handoff, dict) and handoff.get("automatic") is False, "idea-validation: GO handoff must be non-automatic", errors)


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
            "openai": {
                "junior": "low",
                "middle": "high",
                "senior": "max",
                "lead": "low",
            },
            "openai-critical": {
                "junior": "max",
                "middle": "max",
                "senior": "low",
                "lead": "medium",
            },
            "codex": {
                "junior": "low",
                "middle": "high",
                "senior": "max",
                "lead": "low",
            },
            "codex-critical": {
                "junior": "max",
                "middle": "max",
                "senior": "low",
                "lead": "medium",
            },
            "zai-codex": {
                "junior": "low",
                "middle": "high",
                "senior": "max",
                "lead": "high",
            },
            "zai-codex-critical": {
                "junior": "max",
                "middle": "high",
                "senior": "low",
                "lead": "medium",
            },
            "z-ai-coding": {
                "junior": "low",
                "middle": "medium",
                "senior": "high",
                "lead": "max",
            },
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
        expected_models = {
            "openai": {
                "junior": "gpt-5.6-luna",
                "middle": "gpt-5.6-luna",
                "senior": "gpt-5.6-luna",
                "lead": "gpt-6-astra",
            },
            "openai-critical": {
                "junior": "gpt-5.6-luna",
                "middle": "gpt-5.6-terra",
                "senior": "gpt-6-astra",
                "lead": "gpt-6-astra",
            },
            "codex": {
                "junior": "gpt-5.3-codex-spark",
                "middle": "gpt-5.6-luna",
                "senior": "gpt-5.6-luna",
                "lead": "gpt-6-astra",
            },
            "codex-critical": {
                "junior": "gpt-5.3-codex-spark",
                "middle": "gpt-5.6-terra",
                "senior": "gpt-6-astra",
                "lead": "gpt-6-astra",
            },
            "zai-codex": {
                "junior": "gpt-5.3-codex-spark",
                "middle": "zai-coding-plan/glm-5.3-flash",
                "senior": "zai-coding-plan/glm-5.3",
                "lead": "openai/gpt-5.6-sol",
            },
            "zai-codex-critical": {
                "junior": "gpt-5.3-codex-spark",
                "middle": "zai-coding-plan/glm-5.3-flash",
                "senior": "gpt-6-astra",
                "lead": "gpt-6-astra",
            },
            "z-ai-coding": {
                "junior": "zai-coding-plan/glm-4.5-air",
                "middle": "zai-coding-plan/glm-4.7",
                "senior": "zai-coding-plan/glm-5.3",
                "lead": "zai-coding-plan/glm-5.3",
            },
        }
        for preset, expected_models_by_level in expected_models.items():
            for level_id, expected_model in expected_models_by_level.items():
                level_defaults = recommended_defaults.get(level_id, {})
                value = level_defaults.get(preset) if isinstance(level_defaults, dict) else None
                require(
                    isinstance(value, dict) and value.get("model") == expected_model,
                    f"model-tiers: recommended_defaults.{level_id}.{preset}.model must be {expected_model}",
                    errors,
                )


def main() -> int:
    try:
        registry = load_registry_for_validation()
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

    workflow_ids = {workflow.get("id") for workflow in registry["workflows"]}
    task_ids = {task.get("id") for task in registry["tasks"]}
    role_ids = {profile.get("id") for profile in registry["profiles"]}
    policy_ids = set(collect_references(policies, {"id"}))
    secure_policy = policies.get("secure_sdd_policy", {})
    validate_secure_sdd_policy(secure_policy, errors)
    try:
        registry_lib.index_policy_nodes(policies)
    except RegistryError as exc:
        errors.append(f"policies: {exc}")
    validate_agent_rule_sets(secure_policy, errors)
    for route_id in ("bugfix", "idea-validation"):
        route = next((workflow for workflow in registry["workflows"] if workflow.get("id") == route_id), {})
        route_path = route.get("manifest") if isinstance(route, dict) else None
        if isinstance(route_path, str):
            try:
                route_manifest = load_policy_yaml(ROOT / route_path)
            except RegistryError as exc:
                errors.append(f"{route_id}: unable to load workflow manifest: {exc}")
            else:
                if isinstance(route_manifest, dict):
                    validate_route_manifest(route_manifest, route_id, errors)
                else:
                    errors.append(f"{route_id}: workflow manifest must be a mapping")
    secure_workflow = next((workflow for workflow in registry["workflows"] if workflow.get("id") == "secure-sdd"), {})
    manifest_path = secure_workflow.get("manifest") if isinstance(secure_workflow, dict) else None
    secure_sdd_manifest: dict | None = None
    if not isinstance(manifest_path, str):
        errors.append("secure-sdd: registry workflow manifest path is required")
    else:
        try:
            manifest = load_policy_yaml(ROOT / manifest_path)
        except RegistryError as exc:
            errors.append(f"secure-sdd: unable to load workflow manifest: {exc}")
        else:
            if not isinstance(manifest, dict):
                errors.append("secure-sdd: workflow manifest must be a mapping")
            else:
                secure_sdd_manifest = manifest
                errors.extend(validate_secure_sdd_manifest(manifest, workflow_ids, task_ids, role_ids, policy_ids))
    portable_guidance_path = ROOT / "AGENTS.md.sdd"
    validate_portable_sdd_guidance(portable_guidance_path, errors)
    if secure_sdd_manifest is not None:
        try:
            portable_guidance = portable_guidance_path.read_text(encoding="utf-8")
        except OSError:
            pass
        else:
            validate_sdd_artifact_independence(
                portable_guidance,
                secure_sdd_manifest,
                errors,
                ROOT / "workflows" / "security-compliance" / "secure-sdd",
            )

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
