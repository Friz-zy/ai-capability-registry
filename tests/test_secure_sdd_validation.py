"""Focused tests for Secure SDD static registry semantics."""

from __future__ import annotations

import importlib.util
import re
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "secure_sdd"
sys.path.insert(0, str(ROOT / "scripts"))

from registry_lib import RegistryError, load_all, load_yaml

def load_validator_module():
    """Load the validator script without requiring it to be a package."""
    specification = importlib.util.spec_from_file_location(
        "validate_registry", ROOT / "scripts" / "validate-registry.py"
    )
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


class SecureSddValidationTests(unittest.TestCase):
    """Check Secure SDD failure modes with repository-owned fixtures."""

    @classmethod
    def setUpClass(cls):
        """Load the validator once for the fixture suite."""
        cls.validator = load_validator_module()
        cls.baseline = cls.validator.load_policy_yaml(FIXTURES / "valid.yaml")
        for metadata_key in ("conditional_stage_results", "deterministic_verification_exception", "human_escalation"):
            if metadata_key in cls.baseline:
                cls.baseline["process_metadata"][metadata_key] = cls.baseline.pop(metadata_key)

    def validate_manifest(self, workflow: dict) -> list[str]:
        """Validate one manifest using stable reference catalogs."""
        return self.validator.validate_secure_sdd_manifest(
            workflow,
            workflow_ids={"secure-sdd", "threat-modeling", "security-review"},
            task_ids={"model-threats", "review-security"},
            role_ids={
                role_id
                for stage in self.baseline["stages"]
                for role_id in stage["roles"]
            },
            policy_ids={"secure-sdd-registry-v1"},
        )

    def test_accepts_complete_secure_sdd_baseline(self):
        """A complete Secure SDD fixture satisfies the static contract."""
        self.assertEqual([], self.validate_manifest(self.baseline))

    def test_rejects_missing_analyze_risk_evidence(self):
        """ANALYZE must retain every independent risk-topic output."""
        manifest = deepcopy(self.baseline)
        analyze = next(stage for stage in manifest["stages"] if stage["id"] == "analyze")
        analyze["outputs"].remove("prompt_injection_assessment")
        self.assertEqual(
            ["secure-sdd: ANALYZE mandatory independent risk-topic evidence is invalid"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_final_review_evidence(self):
        """FINAL INDEPENDENT REVIEW must retain all required evidence inputs."""
        manifest = deepcopy(self.baseline)
        review = next(stage for stage in manifest["stages"] if stage["id"] == "final_independent_review")
        review["inputs"].remove("regression_results")
        self.assertEqual(
            ["secure-sdd: FINAL INDEPENDENT REVIEW required evidence inputs are invalid"],
            self.validate_manifest(manifest),
        )

    def test_shared_registry_loader_accepts_nested_policy_selectors(self):
        """Generators can load canonical structured policy selectors."""
        policies = load_all()["policies"]
        selectors = policies["secure_sdd_policy"]["enforcement_model"]["applicability_matching"]["credential_bearing_config_selectors"]["selectors"]
        self.assertEqual(["pip", "pypi"], selectors[0]["ecosystems"])

    def test_shared_parser_rejects_structural_fixture_errors(self):
        """Shared parsing reports duplicate and indentation errors directly."""
        expected = {
            "duplicate-inline-key.yaml": "duplicate-inline-key.yaml:3: duplicate key id",
            "duplicate-continuation-key.yaml": "duplicate-continuation-key.yaml:3: duplicate key id",
            "duplicate-null-continuation-key.yaml": "duplicate-null-continuation-key.yaml:4: duplicate key id",
            "malformed-indentation.yaml": "malformed-indentation.yaml:3: unexpected indentation",
            "overindented-list-item-child.yaml": "overindented-list-item-child.yaml:3: unexpected indentation",
            "overindented-list-item-continuation.yaml": "overindented-list-item-continuation.yaml:3: unexpected indentation",
        }
        for fixture_name, message in expected.items():
            with self.subTest(fixture_name=fixture_name):
                with self.assertRaisesRegex(RegistryError, re.escape(message)):
                    load_yaml(FIXTURES / fixture_name)

    def test_rejects_single_stage_sequence_mutations(self):
        """Each stage-sequence mutation has a stable diagnostic."""
        mutations = {
            "missing": lambda manifest: manifest["stages"].pop(),
            "reordered": lambda manifest: manifest["stages"].__setitem__(0, manifest["stages"].pop(1)),
            "duplicate": lambda manifest: manifest["stages"].__setitem__(1, deepcopy(manifest["stages"][0])),
        }
        expected = {
            "missing": [
                "secure-sdd: stages must match the exact required stage sequence",
                "secure-sdd: POLICY GATE must consume security_review_result",
                "secure-sdd: POLICY GATE must be a human policy gate",
                "secure-sdd: POLICY GATE must reject blocker waivers and limit disposition to residual risk",
            ],
            "reordered": ["secure-sdd: stages must match the exact required stage sequence"],
            "duplicate": [
                "secure-sdd: stages must match the exact required stage sequence",
                "secure-sdd: stage ids must be unique",
            ],
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                manifest = deepcopy(self.baseline)
                mutate(manifest)
                self.assertEqual(expected[name], self.validate_manifest(manifest))

    def test_rejects_reviewer_overlap(self):
        """An implementation role cannot be an independent reviewer role."""
        manifest = deepcopy(self.baseline)
        manifest["stages"][2]["roles"] = ["backend-engineer"]
        self.assertEqual(
            ["secure-sdd: implementation and independent review roles overlap: ['backend-engineer']"],
            self.validate_manifest(manifest),
        )

    def test_rejects_architecture_and_security_reviewer_overlap(self):
        """All declared independent review stages are separated from implementers."""
        for stage_id in ("architecture_review", "security_review"):
            with self.subTest(stage_id=stage_id):
                manifest = deepcopy(self.baseline)
                stage = next(stage for stage in manifest["stages"] if stage["id"] == stage_id)
                stage["roles"] = ["backend-engineer"]
                self.assertEqual(
                    ["secure-sdd: implementation and independent review roles overlap: ['backend-engineer']"],
                    self.validate_manifest(manifest),
                )

    def test_rejects_missing_deterministic_verification(self):
        """Verification must provide reproducible evidence and failure blocking."""
        manifest = deepcopy(self.baseline)
        manifest["process_metadata"]["remediation_and_re_review"]["blocking_findings"] = []
        self.assertEqual(
            ["secure-sdd: remediation blocking-finding contract is required"],
            self.validate_manifest(manifest),
        )

    def test_rejects_each_residual_risk_schema_mutation(self):
        """Residual-risk disposition requires remediation and fresh re-review."""
        mutations = {
            "evidence": (
                "required_evidence",
                ["explicit_risk_classification"],
                "secure-sdd: residual-risk evidence contract is invalid",
            ),
            "route": (
                "rejection_route",
                "POLICY GATE",
                "secure-sdd: residual-risk rejection route must be IMPLEMENT",
            ),
        }
        for name, (field_name, value, expected_error) in mutations.items():
            with self.subTest(name=name):
                manifest = deepcopy(self.baseline)
                disposition = manifest["process_metadata"]["remediation_and_re_review"]["residual_risk_disposition"]
                disposition[field_name] = value
                self.assertEqual([expected_error], self.validate_manifest(manifest))

    def test_rejects_missing_independent_reviewer_freshness(self):
        """Every independent review depends on fresh read-only reviewers."""
        manifest = deepcopy(self.baseline)
        manifest["process_metadata"]["independent_reviewers"]["fresh"] = False
        self.assertEqual(
            ["secure-sdd: fresh read-only independent reviewer declaration is required"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_deterministic_failure_evidence(self):
        """Deterministic verification must emit both failure outputs."""
        manifest = deepcopy(self.baseline)
        deterministic_verify_stage = next(
            stage for stage in manifest["stages"] if stage["id"] == "deterministic_verify"
        )
        deterministic_verify_stage["outputs"].remove("failed_verification_evidence")
        self.assertEqual(
            ["secure-sdd: deterministic verification must emit results and failure evidence"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_deterministic_failure_output(self):
        """Deterministic failures must emit evidence for remediation."""
        manifest = deepcopy(self.baseline)
        deterministic_verify_stage = next(
            stage for stage in manifest["stages"] if stage["id"] == "deterministic_verify"
        )
        deterministic_verify_stage["outputs"].remove("failed_verification_evidence")
        self.assertEqual(
            ["secure-sdd: deterministic verification must emit results and failure evidence"],
            self.validate_manifest(manifest),
        )

    def test_rejects_waivable_blocking_finding_contract(self):
        """Neither a human nor a workflow stage may waive blocking findings."""
        manifest = deepcopy(self.baseline)
        manifest["process_metadata"]["human_escalation"]["restrictions"] = [
            "A coordinator may waive blocking findings."
        ]
        self.assertEqual(
            ["secure-sdd: human escalation must not waive blocking findings or dispose unremediated risk"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_policy_gate_blocking_and_residual_risk_semantics(self):
        """The policy gate cannot waive blockers and may disposition only residual risk."""
        mutations = {
            "blocking": "A HUMAN disposition addresses only explicitly classified residual risk.",
            "residual": "Blocking findings cannot be waived.",
        }
        for missing_semantics, criterion in mutations.items():
            with self.subTest(missing_semantics=missing_semantics):
                manifest = deepcopy(self.baseline)
                manifest["stages"][-1]["acceptance_criteria"] = [criterion]
                self.assertEqual(
                    ["secure-sdd: POLICY GATE must reject blocker waivers and limit disposition to residual risk"],
                    self.validate_manifest(manifest),
                )

    def test_rejects_stage_with_empty_role_list(self):
        """Every stage must declare at least one role."""
        manifest = deepcopy(self.baseline)
        manifest["stages"][0]["roles"] = []
        self.assertEqual(["secure-sdd: stage specify must declare a nonempty role list"], self.validate_manifest(manifest))

    def test_rejects_invalid_conditional_result(self):
        """Conditional review outcomes are limited to the declared result contract."""
        manifest = deepcopy(self.baseline)
        manifest["process_metadata"]["conditional_stage_results"]["architecture_review"]["required_status_values"] = ["reviewed"]
        self.assertEqual(
            ["secure-sdd: architecture_review conditional result statuses must be reviewed, escalated, not_applicable"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_conditional_status_required_field(self):
        """Each conditional status must retain every required field."""
        manifest = deepcopy(self.baseline)
        reviewed_fields = manifest["process_metadata"]["conditional_stage_results"]["architecture_review"][
            "status_specific_required_fields"
        ]["reviewed"]
        reviewed_fields.remove("review_evidence")
        self.assertEqual(
            ["secure-sdd: architecture_review reviewed required fields are invalid"],
            self.validate_manifest(manifest),
        )

    def test_rejects_missing_security_result_from_each_declared_consumer(self):
        """Every declared security-result consumer must receive its artifact."""
        expected_errors = {
            "final_independent_review": "secure-sdd: FINAL INDEPENDENT REVIEW must consume security_review_result",
            "converge": "secure-sdd: CONVERGE must consume security_review_result",
            "policy_gate": "secure-sdd: POLICY GATE must consume security_review_result",
        }
        for consumer_stage_id, expected_error in expected_errors.items():
            with self.subTest(consumer_stage_id=consumer_stage_id):
                manifest = deepcopy(self.baseline)
                consumer_stage = next(
                    stage for stage in manifest["stages"] if stage["id"] == consumer_stage_id
                )
                consumer_stage["inputs"].remove("security_review_result")
                self.assertEqual([expected_error], self.validate_manifest(manifest))

    def test_rejects_conditional_consumer_input_removal(self):
        """Declared conditional consumers must receive the declared artifact."""
        manifest = deepcopy(self.baseline)
        manifest["stages"][5]["inputs"].remove("architecture_review_result")
        self.assertEqual(
            ["secure-sdd: CHECKLIST must consume architecture_review_result"],
            self.validate_manifest(manifest),
        )

    def test_rejects_invalid_stage_role_value_before_set_operations(self):
        """A non-string role is rejected without raising a validator exception."""
        manifest = deepcopy(self.baseline)
        manifest["stages"][0]["roles"] = [{}]
        self.assertEqual(
            ["secure-sdd: stage specify role must be a nonempty string"],
            self.validate_manifest(manifest),
        )

    def test_rejects_exact_risk_gate_metadata(self):
        """HIGH and CRITICAL policy gate metadata accepts only canonical values."""
        policy = self.validator.load_registry_for_validation()["policies"]["secure_sdd_policy"]
        mutations = (
            ("HIGH", "levels", "minimum_review", "normal_review", "secure-sdd policy: HIGH requires independent security review"),
            ("HIGH", "review_gates", "required_reviewer", "coordinator", "secure-sdd policy: HIGH requires independent security reviewer metadata"),
            ("HIGH", "review_gates", "human_approval", "optional", "secure-sdd policy: HIGH human approval metadata is invalid"),
            ("CRITICAL", "levels", "minimum_review", "normal_review", "secure-sdd policy: CRITICAL requires security review then human gate"),
            ("CRITICAL", "review_gates", "required_reviewer", "coordinator", "secure-sdd policy: CRITICAL requires independent security reviewer metadata"),
            ("CRITICAL", "review_gates", "human_approval", "optional", "secure-sdd policy: CRITICAL requires human approval metadata"),
        )
        for risk, section, field, value, expected_error in mutations:
            with self.subTest(risk=risk, field=field):
                mutated_policy = deepcopy(policy)
                mutated_policy["risk_model"][section][risk][field] = value
                errors: list[str] = []
                self.validator.validate_secure_sdd_policy(mutated_policy, errors)
                self.assertEqual([expected_error], errors)

    def test_validates_portable_policy_tokens_and_dependencies(self):
        """Portable guidance rejects token-order and dependency mutations."""
        source = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        mutations = {
            "missing": (source.replace("→ clarify\n", "", 1), "AGENTS.md.sdd: Development Workflow must contain canonical POLICY GATE order"),
            "reordered": (source.replace("specify\n→ clarify", "clarify\n→ specify", 1), "AGENTS.md.sdd: Development Workflow must contain canonical POLICY GATE order"),
            "registry": (source + "\nregistry dependency\n", "AGENTS.md.sdd: forbidden registry dependency"),
            "provider": (source + "\nprovider selection\n", "AGENTS.md.sdd: forbidden provider dependency"),
            "model": (source + "\nmodel configuration\n", "AGENTS.md.sdd: forbidden model dependency"),
            "runtime": (source + "\nruntime requirement\n", "AGENTS.md.sdd: forbidden runtime dependency"),
            "self": (source + "\nmust use AGENTS.md.sdd\n", "AGENTS.md.sdd: forbidden self requirement"),
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            guidance_path = Path(temporary_directory) / "AGENTS.md.sdd"
            for name, (content, expected_error) in mutations.items():
                with self.subTest(name=name):
                    guidance_path.write_text(content, encoding="utf-8")
                    errors: list[str] = []
                    self.validator.validate_portable_sdd_guidance(guidance_path, errors)
                    self.assertEqual([expected_error], errors)

    def test_rejects_bidirectional_sdd_artifact_dependencies(self):
        """Portable guidance and Secure SDD remain independent in both directions."""
        portable_guidance = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        manifest = deepcopy(self.baseline)

        errors: list[str] = []
        self.validator.validate_sdd_artifact_independence(
            portable_guidance + "\nDepends on workflows/security-compliance/secure-sdd/workflow.yaml.\n",
            manifest,
            errors,
        )
        self.assertEqual(
            ["SDD independence: AGENTS.md.sdd must not depend on Secure SDD"],
            errors,
        )

        errors = []
        manifest["runtime_metadata"] = {
            "portable_guidance": {"path": "AGENTS.md.sdd"}
        }
        self.validator.validate_sdd_artifact_independence(portable_guidance, manifest, errors)
        self.assertEqual(
            ["SDD independence: Secure SDD must not depend on AGENTS.md.sdd"],
            errors,
        )

    def test_rejects_agents_reference_in_secure_sdd_workflow_artifact(self):
        """The Secure SDD workflow artifact must not reference portable guidance."""
        portable_guidance = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        manifest = deepcopy(self.baseline)
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            workflow_path = artifact_root / "workflow.md"
            workflow_path.write_text("Read AGENTS.md.sdd for additional guidance.\n", encoding="utf-8")
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence(
                portable_guidance,
                manifest,
                errors,
                artifact_root=artifact_root,
            )
            self.assertEqual(
                ["SDD independence: Secure SDD artifacts must not depend on AGENTS.md.sdd"],
                errors,
            )

    def test_rejects_agents_reference_in_local_secure_sdd_artifact(self):
        """Local artifacts under the Secure SDD directory must remain independent."""
        portable_guidance = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        manifest = deepcopy(self.baseline)
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            local_artifact_directory = artifact_root / "local"
            local_artifact_directory.mkdir()
            (artifact_root / "workflow.md").write_text("[Checklist](local/checklist.md)\n", encoding="utf-8")
            local_artifact_path = local_artifact_directory / "checklist.md"
            local_artifact_path.write_text("Use AGENTS.md.sdd as the source for this checklist.\n", encoding="utf-8")
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence(
                portable_guidance,
                manifest,
                errors,
                artifact_root=artifact_root,
            )
            self.assertEqual(
                ["SDD independence: Secure SDD artifacts must not depend on AGENTS.md.sdd"],
                errors,
            )

    def test_rejects_transitive_agents_reference_through_local_artifact_graph(self):
        """The artifact graph must not reach portable guidance through local links."""
        portable_guidance = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        manifest = deepcopy(self.baseline)
        manifest["runtime_metadata"] = {"artifact": "workflow.md"}
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            (artifact_root / "workflow.md").write_text(
                "[Local A](local-a.md)\n",
                encoding="utf-8",
            )
            (artifact_root / "local-a.md").write_text(
                "[Local B](local-b.md)\n",
                encoding="utf-8",
            )
            (artifact_root / "local-b.md").write_text(
                "[Portable guidance](AGENTS.md.sdd)\n",
                encoding="utf-8",
            )
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence(
                portable_guidance,
                manifest,
                errors,
                artifact_root=artifact_root,
            )
            self.assertEqual(
                ["SDD independence: Secure SDD artifacts must not depend on AGENTS.md.sdd"],
                errors,
            )

    def test_rejects_transitive_agents_reference_with_url_suffixes(self):
        """Artifact traversal must preserve the blocking diagnostic for URL-like links."""
        portable_guidance = (ROOT / "AGENTS.md.sdd").read_text(encoding="utf-8")
        manifest = deepcopy(self.baseline)
        manifest["runtime_metadata"] = {"artifact": "workflow.md"}
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            (artifact_root / "workflow.md").write_text(
                "[Local A](local-a.md?version=1)\n",
                encoding="utf-8",
            )
            (artifact_root / "local-a.md").write_text(
                "[Local B](local-b.md#section)\n",
                encoding="utf-8",
            )
            (artifact_root / "local-b.md").write_text(
                "[Portable guidance](AGENTS.md.sdd)\n",
                encoding="utf-8",
            )
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence(
                portable_guidance,
                manifest,
                errors,
                artifact_root=artifact_root,
            )
            self.assertEqual(
                ["SDD independence: Secure SDD artifacts must not depend on AGENTS.md.sdd"],
                errors,
            )

    def test_rejects_artifact_reference_escaping_approved_root(self):
        """Declared local references cannot traverse outside Secure SDD root."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            (artifact_root / "workflow.md").write_text("[Escape](../outside.md)\n", encoding="utf-8")
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence("portable", deepcopy(self.baseline), errors, artifact_root)
            self.assertEqual(["SDD independence: Secure SDD artifact reference escapes approved root"], errors)

    def test_rejects_traversal_only_out_of_root_reference_from_local_artifact(self):
        """Graph traversal must enforce containment beyond full-file content scanning."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            artifact_root = Path(temporary_directory)
            (artifact_root / "workflow.md").write_text("[Local A](local-a.md)\n", encoding="utf-8")
            (artifact_root / "local-a.md").write_text("[Outside](../outside.md)\n", encoding="utf-8")
            errors: list[str] = []
            self.validator.validate_sdd_artifact_independence(
                "portable",
                deepcopy(self.baseline),
                errors,
                artifact_root,
            )
            self.assertEqual(
                ["SDD independence: Secure SDD artifact reference escapes approved root"],
                errors,
            )

    def test_rejects_remote_artifact_links_as_root_escape(self):
        """Remote Markdown links cannot escape the approved Secure SDD artifact root."""
        remote_links = {
            "https": "[Remote](https://example.invalid/guidance.md)",
            "protocol_relative": "[Remote](//example.invalid/guidance.md)",
        }
        for link_type, link in remote_links.items():
            with self.subTest(link_type=link_type):
                with tempfile.TemporaryDirectory() as temporary_directory:
                    artifact_root = Path(temporary_directory)
                    (artifact_root / "workflow.md").write_text(f"{link}\n", encoding="utf-8")
                    errors: list[str] = []
                    self.validator.validate_sdd_artifact_independence(
                        "portable",
                        deepcopy(self.baseline),
                        errors,
                        artifact_root,
                    )
                    self.assertEqual(
                        ["SDD independence: Secure SDD artifact reference escapes approved root"],
                        errors,
                    )

    def test_rejects_all_artifact_root_symlinks(self):
        """Symlinks cannot bypass Secure SDD artifact-root inspection."""
        symlink_targets = {
            "portable_guidance": "AGENTS.md.sdd",
            "out_of_root_file": "outside.md",
            "in_root_file": "target.md",
            "in_root_directory": "target-directory",
        }
        for target_kind, target_name in symlink_targets.items():
            with self.subTest(target_kind=target_kind):
                with tempfile.TemporaryDirectory() as temporary_directory:
                    temporary_root = Path(temporary_directory)
                    artifact_root = temporary_root / "secure-sdd"
                    artifact_root.mkdir()
                    (artifact_root / "workflow.md").write_text("workflow\n", encoding="utf-8")
                    if target_kind == "portable_guidance":
                        target = ROOT / target_name
                    elif target_kind == "out_of_root_file":
                        target = temporary_root / target_name
                        target.write_text("outside\n", encoding="utf-8")
                    elif target_kind == "in_root_file":
                        target = artifact_root / target_name
                        target.write_text("safe\n", encoding="utf-8")
                    else:
                        target = artifact_root / target_name
                        target.mkdir()
                    link = artifact_root / "link"
                    try:
                        link.symlink_to(target, target_is_directory=target.is_dir())
                    except OSError:
                        self.skipTest("platform does not permit symlink creation")
                    errors: list[str] = []
                    self.validator.validate_sdd_artifact_independence(
                        "portable",
                        deepcopy(self.baseline),
                        errors,
                        artifact_root,
                    )
                    self.assertEqual(
                        ["SDD independence: Secure SDD artifact root must not contain symlinks"],
                        errors,
                    )

    def test_rejects_template_dependency(self):
        """Secure SDD manifests remain independent of workflow templates."""
        manifest = deepcopy(self.baseline)
        manifest["template"] = "workflows/templates/schemas/workflow.schema.yaml"
        self.assertEqual(["secure-sdd: workflow templates must not be a manifest dependency"], self.validate_manifest(manifest))

    def test_parses_nested_mapping_in_list_item(self):
        """Policy selectors retain nested mapping/list structure."""
        policy = self.validator.load_policy_yaml(FIXTURES / "nested-policy-selector.yaml")
        selector = policy["secure_sdd_policy"]["selectors"][0]
        self.assertEqual(["pip", "pypi"], selector["ecosystems"])
        self.assertEqual(["pip.conf", "**/pip.conf"], selector["path_globs"])

    def test_parses_secure_sdd_nested_result_contract(self):
        """The parser retains nested conditional-result contract mappings."""
        workflow = self.baseline
        process_metadata = workflow["process_metadata"]
        architecture_result = process_metadata["conditional_stage_results"]["architecture_review"]
        self.assertEqual("architecture_review_result", architecture_result["artifact"])
        self.assertEqual(
            ["reviewed", "escalated", "not_applicable"],
            architecture_result["required_status_values"],
        )

    def test_rejects_duplicate_mapping_keys_with_line_diagnostic(self):
        """Restricted YAML rejects duplicate inline and continuation keys."""
        expected_messages = {
            "duplicate-inline-key.yaml": "duplicate-inline-key.yaml:3: duplicate key id",
            "duplicate-continuation-key.yaml": "duplicate-continuation-key.yaml:3: duplicate key id",
        }
        for fixture_name, expected_message in expected_messages.items():
            with self.subTest(fixture_name=fixture_name):
                with self.assertRaisesRegex(Exception, re.escape(expected_message)):
                    self.validator.load_policy_yaml(FIXTURES / fixture_name)

    def test_rejects_malformed_indentation(self):
        """Restricted YAML retains indentation diagnostics."""
        with self.assertRaisesRegex(Exception, r"malformed-indentation\.yaml:\d+: unexpected indentation"):
            self.validator.load_policy_yaml(FIXTURES / "malformed-indentation.yaml")

    def test_parses_every_fixture(self):
        """Every non-error fixture remains syntactically parseable."""
        invalid_fixture_names = {
            "overindented-list-item-child.yaml",
            "overindented-list-item-continuation.yaml",
        }
        for fixture_path in FIXTURES.glob("*.yaml"):
            if fixture_path.name.startswith(("duplicate-", "malformed-")) or fixture_path.name in invalid_fixture_names:
                continue
            with self.subTest(fixture=fixture_path.name):
                self.validator.load_policy_yaml(fixture_path)


if __name__ == "__main__":
    unittest.main()
