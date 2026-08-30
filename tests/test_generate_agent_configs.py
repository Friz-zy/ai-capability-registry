"""Regression coverage for portable, ownership-safe CLI agent generation."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def load_generator_module():
    """Load the standalone generator module for direct behavioral tests."""
    specification = importlib.util.spec_from_file_location(
        "generate_agent_configs", ROOT / "scripts" / "generate-agent-configs.py"
    )
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


class GenerateAgentConfigsTests(unittest.TestCase):
    """Verify portable output and structurally verified ownership behavior."""

    @classmethod
    def setUpClass(cls):
        """Load the generator once for this focused suite."""
        cls.generator = load_generator_module()

    def orchestrator_entries(self):
        """Return the minimal primary-agent entry required by primary generators."""
        profile = {
            "id": "orchestrator",
            "name": "Orchestrator",
            "seniority": ["senior"],
            "role": {"title": "Orchestrator"},
        }
        return [(profile, "senior")]

    def snapshot_files(self, directory: Path) -> dict[str, bytes]:
        """Return generated file bytes keyed by their portable relative paths."""
        return {
            path.relative_to(directory).as_posix(): path.read_bytes()
            for path in sorted(directory.rglob("*"))
            if path.is_file()
        }

    def generate_primary(self, cli_id: str, output_directory: Path, prompt: str | None = None) -> int:
        """Generate one primary artifact using deterministic test inputs."""
        return self.generator.generate_primary_role_artifact(
            cli_id,
            output_directory,
            self.orchestrator_entries(),
            "refreshed-model",
            None,
            False,
            "tiered",
            prompt,
        )

    def marked_content(self, suffix: str) -> str:
        """Return minimal format-valid generated content for a file suffix."""
        marker_value = self.generator.GENERATOR_MARKER_VALUE
        if suffix == ".toml":
            return f"# generated-by: {marker_value}\nname = \"generated\"\n"
        if suffix == ".json":
            return json.dumps({"$comment": f"generated-by: {marker_value}"})
        if suffix == ".jsonc":
            return f"// generated-by: {marker_value}\n{{}}\n"
        return f"---\ngenerated_by: \"{marker_value}\"\n---\n"

    def generate_cli(self, cli_id: str, output_directory: Path) -> None:
        """Generate one supported CLI target with its standard generation mode."""
        options = self.generator.MANAGED_CLI_GENERATION_OPTIONS[cli_id]
        self.generator.generate_agent_configs(
            cli_id,
            output_directory,
            options["preset"],
            str(output_directory),
            options["model_prefix"],
            options["role_levels_mode"],
            [],
        )

    def write_legacy_catalog(self, output_directory: Path) -> None:
        """Write the exact legacy catalog signature used for migration tests."""
        (output_directory / "roles.md").write_text(
            "# Available Generated Roles\n\n"
            "Use the CLI native available agent list by default. Use this catalog only as a fallback when the CLI "
            "cannot expose available agents or when exact generated role ids are needed.\n",
            encoding="utf-8",
        )

    def legacy_role_content(self, cli_id: str, agent_id: str, managed_root: Path) -> str:
        """Return a constrained legacy role fixture matching one CLI format."""
        runtime_references = (
            f"Read `{managed_root}/security/rules.md",
            f"read `{managed_root}/skills/skills.md",
        )
        joined_runtime_references = " ".join(runtime_references)
        if cli_id == "codex":
            footer_prefix = "# Generated from registry/profiles.yaml by scripts/generate-agent-configs.py.\n"
            footer = footer_prefix + (
                "# This orchestrator role is intended to be user-facing and to delegate to exact role-level agents.\n"
                if agent_id.startswith("orchestrator")
                else "# Reference this file from config.toml [agents.<name>].config_file when needed.\n"
            )
            return (
                f'name = "{agent_id}"\ndeveloper_instructions = "{joined_runtime_references}"\n\n'
                + footer
            )
        if cli_id == "amazon-kiro":
            return json.dumps(
                {
                    "name": agent_id,
                    "description": "Legacy generated role.",
                    "prompt": f"# You are the Orchestrator\n{joined_runtime_references}",
                    "tools": ["*"],
                }
            )
        return (
            "---\ndescription: legacy\nhidden: false\n---\n\n# You are the Orchestrator\n"
            + joined_runtime_references
            + "\n"
        )

    def test_absolute_checkout_paths_generate_portable_identical_prompts(self):
        """Different build roots must not produce path-specific generated prompts."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            first_checkout_root = temporary_root / "checkout-one"
            second_checkout_root = temporary_root / "checkout-two"
            first_output_directory = first_checkout_root / "configs" / "kilo-code"
            second_output_directory = second_checkout_root / "configs" / "kilo-code"

            self.generate_cli("kilo-code", first_output_directory)
            self.generate_cli("kilo-code", second_output_directory)

            first_snapshot = self.snapshot_files(first_output_directory)
            second_snapshot = self.snapshot_files(second_output_directory)
            rendered_content = b"\n".join(first_snapshot.values()).decode("utf-8")

            self.assertEqual(first_snapshot, second_snapshot)
            self.assertNotIn(str(first_checkout_root), rendered_content)
            self.assertNotIn(str(second_checkout_root), rendered_content)
            self.assertIn("~/.ai-registry/skills/skills.md", rendered_content)

    def test_per_cli_marked_roles_refresh_after_cleanup(self):
        """Every supported CLI refreshes an exact-marker role artifact safely."""
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli(cli_id, output_directory)
                    extension = self.generator.CLI_TARGETS[cli_id]["extension"]
                    agent_directory = output_directory / self.generator.CLI_TARGETS[cli_id]["agent_directory"]
                    role_path = next(agent_directory.glob(f"orchestrator*{extension}"))
                    role_path.write_text(self.marked_content(extension), encoding="utf-8")

                    self.generate_cli(cli_id, output_directory)

                    self.assertTrue(self.generator.has_generated_marker(role_path))
                    self.assertNotEqual(self.marked_content(extension), role_path.read_text(encoding="utf-8"))

    def test_every_cli_legacy_catalog_and_role_migrates_to_exact_markers(self):
        """Verified legacy roles at managed paths regenerate with exact markers."""
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in cli_ids:
                    with self.subTest(cli_id=cli_id):
                        output_directory = managed_root / "configs" / cli_id
                        output_directory.mkdir(parents=True)
                        self.write_legacy_catalog(output_directory)
                        extension = self.generator.CLI_TARGETS[cli_id]["extension"]
                        agent_directory = output_directory / self.generator.CLI_TARGETS[cli_id]["agent_directory"]
                        agent_directory.mkdir(parents=True)
                        agent_id = "orchestrator" if cli_id == "amazon-kiro" else "orchestrator-senior"
                        role_path = agent_directory / f"{agent_id}{extension}"
                        role_path.write_text(
                            self.legacy_role_content(cli_id, agent_id, managed_root), encoding="utf-8"
                        )

                        self.generate_cli(cli_id, output_directory)

                        self.assertTrue(self.generator.has_generated_marker(output_directory / "roles.md"))
                        self.assertTrue(self.generator.has_generated_marker(role_path))
                        self.assertIn("~/.ai-registry", role_path.read_text(encoding="utf-8"))

    def test_verified_legacy_primaries_refresh_at_managed_paths(self):
        """Verified legacy primary configurations migrate to exact current markers."""
        primary_files = {"codex": "config.toml", "opencode": "opencode.json", "kilo-code": "kilo.jsonc"}
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id, primary_file_name in primary_files.items():
                    with self.subTest(cli_id=cli_id):
                        output_directory = managed_root / "configs" / cli_id
                        output_directory.mkdir(parents=True)
                        self.write_legacy_catalog(output_directory)
                        primary_path = output_directory / primary_file_name
                        if cli_id == "opencode":
                            primary_content = json.dumps({"default_agent": "orchestrator-senior"})
                        elif cli_id == "kilo-code":
                            primary_content = (
                                "// Generated by scripts/generate-agent-configs.py.\n"
                                '{"default_agent": "orchestrator-senior"}\n'
                            )
                        else:
                            primary_content = (
                                "# Generated by scripts/generate-agent-configs.py.\n"
                                'default_agent = "orchestrator-senior"\n[agents.orchestrator-senior]\n'
                            )
                        primary_path.write_text(primary_content, encoding="utf-8")

                        self.assertEqual(1, self.generate_primary(cli_id, output_directory))
                        self.assertTrue(self.generator.has_generated_marker(primary_path))

    def test_full_generation_uses_pre_catalog_legacy_primary_and_steering_snapshot(self):
        """Legacy primaries and steering migrate even after the catalog is replaced."""
        primary_files = {"codex": "config.toml", "opencode": "opencode.json", "kilo-code": "kilo.jsonc"}
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id, primary_file_name in primary_files.items():
                    with self.subTest(cli_id=cli_id):
                        output_directory = managed_root / "configs" / cli_id
                        output_directory.mkdir(parents=True)
                        self.write_legacy_catalog(output_directory)
                        primary_path = output_directory / primary_file_name
                        if cli_id == "codex":
                            primary_content = (
                                "# Generated by scripts/generate-agent-configs.py.\n"
                                'default_agent = "orchestrator-senior"\n[agents.orchestrator-senior]\n'
                            )
                        elif cli_id == "kilo-code":
                            primary_content = (
                                "// Generated by scripts/generate-agent-configs.py.\n"
                                '{"default_agent": "orchestrator-senior"}\n'
                            )
                        else:
                            primary_content = json.dumps({"default_agent": "orchestrator-senior"})
                        primary_path.write_text(primary_content, encoding="utf-8")

                        self.generate_cli(cli_id, output_directory)

                        self.assertTrue(self.generator.has_generated_marker(primary_path))

                amazon_output_directory = managed_root / "configs" / "amazon-kiro"
                amazon_output_directory.mkdir(parents=True)
                self.write_legacy_catalog(amazon_output_directory)
                steering_path = amazon_output_directory / "steering" / "orchestrator.md"
                steering_path.parent.mkdir()
                steering_path.write_text(
                    "---\ninclusion: auto\n---\n\n# You are the Orchestrator\n\n"
                    f"read {managed_root}/capability-routing.md\n",
                    encoding="utf-8",
                )

                self.generate_cli("amazon-kiro", amazon_output_directory)

                self.assertTrue(self.generator.has_generated_marker(steering_path))
                self.assertIn("~/.ai-registry", steering_path.read_text(encoding="utf-8"))

    def test_full_generation_preserves_legacy_lookalike_without_pre_catalog_eligibility(self):
        """A primary with an invalid legacy catalog remains user-owned after a full run."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                output_directory = managed_root / "configs" / "kilo-code"
                output_directory.mkdir(parents=True)
                (output_directory / "roles.md").write_text("User-owned catalog.\n", encoding="utf-8")
                primary_path = output_directory / "kilo.jsonc"
                primary_content = (
                    "// Generated by scripts/generate-agent-configs.py.\n"
                    '{"default_agent": "orchestrator-senior"}\n'
                )
                primary_path.write_text(primary_content, encoding="utf-8")

                self.generate_cli("kilo-code", output_directory)

                self.assertEqual(primary_content, primary_path.read_text(encoding="utf-8"))

    def test_verified_tracked_ordinary_role_migrates_during_full_generation(self):
        """A verified legacy ordinary role at a managed path receives the current marker."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                output_directory = managed_root / "configs" / "kilo-code"
                output_directory.mkdir(parents=True)
                self.write_legacy_catalog(output_directory)
                role_path = output_directory / "agent" / "backend-engineer-senior.md"
                role_path.parent.mkdir()
                role_path.write_text(
                    self.legacy_role_content("kilo-code", "backend-engineer-senior", managed_root),
                    encoding="utf-8",
                )

                self.generate_cli("kilo-code", output_directory)

                refreshed_content = role_path.read_text(encoding="utf-8")
                self.assertTrue(self.generator.has_generated_marker(role_path))
                self.assertIn("~/.ai-registry", refreshed_content)

    def test_full_generation_migrates_actual_affected_role_shapes_after_catalog_marker(self):
        """Current catalogs do not block migration of verified tracked legacy role shapes."""
        fixture_paths = (
            ("codex", Path("roles/backend-engineer-senior.toml")),
            ("kilo-code", Path("agent/backend-engineer-senior.md")),
            ("opencode", Path("agents/backend-engineer-senior.md")),
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in self.generator.MANAGED_CLI_GENERATION_OPTIONS:
                    self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                for cli_id, relative_role_path in fixture_paths:
                    with self.subTest(cli_id=cli_id):
                        fixture_content = (ROOT / "configs" / cli_id / relative_role_path).read_text(encoding="utf-8")
                        fixture_content = fixture_content.replace(
                            self.generator.TOML_GENERATOR_MARKER + "\n", "", 1
                        ).replace(
                            f"generated_by: \"{self.generator.GENERATOR_MARKER_VALUE}\"\n", "", 1
                        )
                        role_path = managed_root / "configs" / cli_id / relative_role_path
                        role_path.write_text(
                            fixture_content.replace(str(ROOT), str(managed_root)), encoding="utf-8"
                        )
                        self.assertTrue(
                            self.generator.has_generated_marker(
                                managed_root / "configs" / cli_id / "roles.md"
                            )
                        )
                        self.assertTrue(
                            self.generator.is_known_managed_output_directory(
                                managed_root / "configs" / cli_id, cli_id
                            )
                        )
                        self.assertTrue(
                            self.generator.has_legacy_role_signature(
                                role_path,
                                managed_root / "configs" / cli_id,
                                cli_id,
                                "backend-engineer-senior",
                                require_legacy_catalog=False,
                                expected_agent_ids=frozenset({"backend-engineer-senior"}),
                            )
                        )

                        self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                        self.assertTrue(self.generator.has_generated_marker(role_path))
                        self.assertIn("~/.ai-registry", role_path.read_text(encoding="utf-8"))

                self.assertEqual([], self.generator.verify_managed_output_drift())

    def test_full_generation_migrates_actual_amazon_role_after_catalog_marker(self):
        """A current catalog does not block verified Amazon Kiro role migration."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in self.generator.MANAGED_CLI_GENERATION_OPTIONS:
                    self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                output_directory = managed_root / "configs" / "amazon-kiro"
                role_path = output_directory / "agents" / "backend-engineer.json"
                fixture_content = (ROOT / "configs" / "amazon-kiro" / "agents" / "backend-engineer.json").read_text(
                    encoding="utf-8"
                )
                role_path.write_text(fixture_content.replace(str(ROOT), str(managed_root)), encoding="utf-8")
                self.assertTrue(self.generator.has_generated_marker(output_directory / "roles.md"))

                self.generate_cli("amazon-kiro", output_directory)

                self.assertTrue(self.generator.has_generated_marker(role_path))
                self.assertIn("~/.ai-registry", role_path.read_text(encoding="utf-8"))
                self.assertEqual([], self.generator.verify_managed_output_drift())

    def test_managed_output_verifier_uses_fresh_manifest_and_rejects_drift(self):
        """The verifier checks every expected managed artifact against fresh output bytes."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in self.generator.MANAGED_CLI_GENERATION_OPTIONS:
                    self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                self.assertEqual([], self.generator.verify_managed_output_drift())

                drifted_role_path = managed_root / "configs" / "kilo-code" / "agent" / "backend-engineer-senior.md"
                drifted_role_path.write_text(
                    drifted_role_path.read_text(encoding="utf-8") + f"\nread {managed_root}/secret.md\n",
                    encoding="utf-8",
                )
                validation_errors = self.generator.verify_managed_output_drift()

                self.assertTrue(any("Checkout-specific absolute reference" in error for error in validation_errors))
                self.assertTrue(any("Generated artifact drift" in error for error in validation_errors))

    def test_managed_output_verifier_rejects_unexpected_marked_role_and_config_artifacts(self):
        """Reverse manifest validation rejects stale owned artifacts but not user files."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in self.generator.MANAGED_CLI_GENERATION_OPTIONS:
                    self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                stale_role_path = managed_root / "configs" / "kilo-code" / "agent" / "retired-role.md"
                stale_role_path.write_text(self.marked_content(".md"), encoding="utf-8")
                stale_config_path = managed_root / "configs" / "kilo-code" / "kilo.override.jsonc"
                stale_config_path.write_text(self.marked_content(".jsonc"), encoding="utf-8")
                user_file_path = managed_root / "configs" / "kilo-code" / "agent" / "user-note.md"
                user_file_path.write_text("User-owned note.\n", encoding="utf-8")

                validation_errors = self.generator.verify_managed_output_drift()

                self.assertIn(
                    "Unexpected stale managed generated artifact: kilo-code/agent/retired-role.md",
                    validation_errors,
                )
                self.assertIn(
                    "Unexpected stale managed generated artifact: kilo-code/kilo.override.jsonc",
                    validation_errors,
                )
                self.assertFalse(any("user-note.md" in error for error in validation_errors))

    def test_reverse_manifest_rejects_historical_role_after_catalog_migration_only(self):
        """A finite historical manifest detects retired roles without acquiring lookalikes."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id in self.generator.MANAGED_CLI_GENERATION_OPTIONS:
                    self.generate_cli(cli_id, managed_root / "configs" / cli_id)

                output_directory = managed_root / "configs" / "amazon-kiro"
                roles_catalog_path = output_directory / "roles.md"
                self.assertTrue(self.generator.has_generated_marker(roles_catalog_path))
                stale_role_path = output_directory / "agents" / "backend-engineer-senior.json"
                stale_role_path.write_text(
                    self.legacy_role_content("amazon-kiro", "backend-engineer-senior", managed_root),
                    encoding="utf-8",
                )
                user_role_path = output_directory / "agents" / "user-profile.json"
                user_role_path.write_text(
                    self.legacy_role_content("amazon-kiro", "user-profile", managed_root),
                    encoding="utf-8",
                )

                validation_errors = self.generator.verify_managed_output_drift()

                self.assertIn(
                    "Unexpected stale managed generated artifact: amazon-kiro/agents/backend-engineer-senior.json",
                    validation_errors,
                )
                self.assertFalse(any("user-profile.json" in error for error in validation_errors))

    def test_reverse_verifier_recognizes_each_legacy_artifact_after_catalog_migration(self):
        """Reverse verification recognizes only exact legacy artifacts after migration."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                original_generate_agent_configs = self.generator.generate_agent_configs

                def generate_without_legacy_steering(*arguments, **keyword_arguments):
                    """Create a fresh manifest without the retired steering artifact."""
                    original_generate_agent_configs(*arguments, **keyword_arguments)
                    cli_id = arguments[0] if arguments else keyword_arguments["cli_id"]
                    output_directory = arguments[1] if len(arguments) > 1 else keyword_arguments["output_directory"]
                    if cli_id == "amazon-kiro":
                        (output_directory / "steering" / "orchestrator.md").unlink(missing_ok=True)

                artifact_cases = (
                    (
                        "primary override",
                        "kilo-code",
                        Path("kilo.override.jsonc"),
                        "Unexpected stale managed generated artifact: kilo-code/kilo.override.jsonc",
                        "// Generated by scripts/generate-agent-configs.py.\n"
                        '{"default_agent": "orchestrator-senior"}\n',
                        "// Generated by scripts/generate-agent-configs.py.\n"
                        '{"default_agent": "user-agent"}\n',
                        False,
                    ),
                    (
                        "Amazon Kiro steering",
                        "amazon-kiro",
                        Path("steering/orchestrator.md"),
                        "Unexpected stale managed generated artifact: amazon-kiro/steering/orchestrator.md",
                        "---\ninclusion: auto\n---\n\n# You are the Orchestrator\n\n"
                        f"read {managed_root}/capability-routing.md\n",
                        "---\ninclusion: auto\n---\n\nUser steering.\n",
                        True,
                    ),
                    (
                        "Claude legacy note",
                        "claude-code",
                        Path("settings.override.md"),
                        "Unexpected stale managed generated artifact: claude-code/settings.override.md",
                        "# Generated by scripts/generate-agent-configs.py.\n"
                        "# Manual merge required: legacy note.\n",
                        "User-owned note.\n",
                        False,
                    ),
                    (
                        "Amazon legacy note",
                        "amazon-kiro",
                        Path("agent.override.md"),
                        "Unexpected stale managed generated artifact: amazon-kiro/agent.override.md",
                        "# Generated by scripts/generate-agent-configs.py.\n"
                        "# Manual merge required: legacy note.\n",
                        "User-owned note.\n",
                        False,
                    ),
                )
                for case_name, cli_id, relative_path, expected_error, valid_content, invalid_content, remove_from_fresh in artifact_cases:
                    with self.subTest(case_name=case_name, signature="valid"):
                        output_directory = managed_root / "configs" / cli_id
                        self.generate_cli(cli_id, output_directory)
                        artifact_path = output_directory / relative_path
                        artifact_path.parent.mkdir(parents=True, exist_ok=True)
                        artifact_path.write_text(valid_content, encoding="utf-8")

                        verifier = (
                            patch.object(self.generator, "generate_agent_configs", generate_without_legacy_steering)
                            if remove_from_fresh
                            else patch.object(self.generator, "generate_agent_configs", original_generate_agent_configs)
                        )
                        with verifier:
                            validation_errors = self.generator.verify_managed_output_drift()
                        self.assertIn(expected_error, validation_errors)

                    with self.subTest(case_name=case_name, signature="invalid"):
                        artifact_path.write_text(invalid_content, encoding="utf-8")

                        verifier = (
                            patch.object(self.generator, "generate_agent_configs", generate_without_legacy_steering)
                            if remove_from_fresh
                            else patch.object(self.generator, "generate_agent_configs", original_generate_agent_configs)
                        )
                        with verifier:
                            validation_errors = self.generator.verify_managed_output_drift()
                        self.assertFalse(any(expected_error in error for error in validation_errors))

    def test_ci_runs_security_rule_generation_and_managed_output_verification(self):
        """The validation workflow invokes both authoritative generated-output checks."""
        workflow_content = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")

        self.assertIn("python scripts/generate-security-rules.py", workflow_content)
        self.assertIn("python scripts/generate-agent-configs.py --verify-managed-outputs", workflow_content)

    def test_codex_legacy_footer_variants_require_exact_second_comment(self):
        """Codex legacy role migration accepts both real footers and rejects a mutation."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                output_directory = managed_root / "configs" / "codex"
                output_directory.mkdir(parents=True)
                self.write_legacy_catalog(output_directory)
                role_directory = output_directory / "roles"
                role_directory.mkdir()

                for agent_id in ("orchestrator-senior", "backend-engineer-senior"):
                    with self.subTest(agent_id=agent_id):
                        role_path = role_directory / f"{agent_id}.toml"
                        role_path.write_text(
                            self.legacy_role_content("codex", agent_id, managed_root), encoding="utf-8"
                        )
                        self.assertTrue(
                            self.generator.has_legacy_role_signature(
                                role_path, output_directory, "codex", agent_id
                            )
                        )

                collision_path = role_directory / "backend-engineer-lead.toml"
                collision_content = self.legacy_role_content("codex", "backend-engineer-lead", managed_root).replace(
                    "when needed.\n", "when changed.\n"
                )
                collision_path.write_text(collision_content, encoding="utf-8")
                backend_profile = {
                    "id": "backend-engineer",
                    "seniority": ["lead"],
                    "role": {"title": "Backend Engineer"},
                }

                self.assertFalse(
                    self.generator.has_legacy_role_signature(
                        collision_path, output_directory, "codex", "backend-engineer-lead"
                    )
                )
                self.generator.cleanup_previous_generated_files(output_directory, "codex", [backend_profile])
                self.assertEqual(collision_content, collision_path.read_text(encoding="utf-8"))

    def test_ambiguous_legacy_collision_is_preserved(self):
        """A partial legacy-looking role cannot migrate without every signature check."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                output_directory = managed_root / "configs" / "kilo-code"
                output_directory.mkdir(parents=True)
                self.write_legacy_catalog(output_directory)
                role_path = output_directory / "agent" / "orchestrator-senior.md"
                role_path.parent.mkdir()
                collision_content = (
                    "---\ndescription: user role\nhidden: false\n---\n\n# You are the Orchestrator\n"
                    "read /different-root/capability-routing.md\n"
                )
                role_path.write_text(collision_content, encoding="utf-8")

                self.generate_cli("kilo-code", output_directory)

                self.assertFalse(self.generator.has_generated_marker(role_path))
                self.assertEqual(collision_content, role_path.read_text(encoding="utf-8"))

    def test_marker_collisions_do_not_grant_ownership(self):
        """Marker text outside its anchored format cannot cause destructive ownership."""
        marker_value = self.generator.GENERATOR_MARKER_VALUE
        collision_contents = {
            ".toml": f'name = "generated-by: {marker_value}"\n',
            ".json": json.dumps({"note": f"generated-by: {marker_value}"}),
            ".jsonc": f'{{"note": "generated-by: {marker_value}"}}\n',
            ".md": f"User note: generated_by: \"{marker_value}\"\n",
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for suffix, collision_content in collision_contents.items():
                with self.subTest(suffix=suffix):
                    collision_path = temporary_root / f"collision{suffix}"
                    collision_path.write_text(collision_content, encoding="utf-8")
                    self.assertFalse(self.generator.has_generated_marker(collision_path))

    def test_unmarked_generated_name_role_collision_survives_generation(self):
        """A user role matching a generated name survives a full generation pass."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            role_path = output_directory / "agent" / "orchestrator-senior.md"
            user_role_content = (
                "---\nname: user-orchestrator\ngenerated_by: \"scripts/generate-agent-configs.py\"\n---\n"
            )
            role_path.parent.mkdir(parents=True)
            role_path.write_text(user_role_content, encoding="utf-8")

            self.generate_cli("kilo-code", output_directory)

            self.assertFalse(self.generator.has_generated_marker(role_path))
            self.assertEqual(user_role_content, role_path.read_text(encoding="utf-8"))

    def test_repeated_generation_beside_user_primary_preserves_primary(self):
        """Repeated runs keep an unmarked user primary while refreshing its marker override."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            primary_config_path = output_directory / "kilo.jsonc"
            user_content = "// user-owned configuration\n{}\n"
            primary_config_path.write_text(user_content, encoding="utf-8")

            self.assertEqual(1, self.generate_primary("kilo-code", output_directory))
            override_config_path = output_directory / "kilo.override.jsonc"
            first_override_content = override_config_path.read_text(encoding="utf-8")
            self.assertEqual(1, self.generate_primary("kilo-code", output_directory))

            self.assertEqual(user_content, primary_config_path.read_text(encoding="utf-8"))
            self.assertEqual(first_override_content, override_config_path.read_text(encoding="utf-8"))
            self.assertTrue(self.generator.has_generated_marker(override_config_path))

    def test_unmarked_override_is_preserved(self):
        """An unmarked override is user-owned and cannot be replaced by generation."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            (output_directory / "config.toml").write_text("model = \"user-primary\"\n", encoding="utf-8")
            override_config_path = output_directory / "config.override.toml"
            user_override_content = "model = \"user-override\"\n"
            override_config_path.write_text(user_override_content, encoding="utf-8")

            self.assertEqual(0, self.generate_primary("codex", output_directory))
            self.assertEqual(user_override_content, override_config_path.read_text(encoding="utf-8"))

    def test_all_marked_stale_overrides_are_removed(self):
        """Marked primaries remove only marked stale overrides for every primary CLI."""
        primary_files = {"codex": "config.toml", "opencode": "opencode.json", "kilo-code": "kilo.jsonc"}
        override_files = {
            "codex": "config.override.toml",
            "opencode": "opencode.override.json",
            "kilo-code": "kilo.override.jsonc",
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id, primary_file_name in primary_files.items():
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    primary_path = output_directory / primary_file_name
                    override_path = output_directory / override_files[cli_id]
                    primary_path.parent.mkdir(parents=True)
                    primary_path.write_text(self.marked_content(primary_path.suffix), encoding="utf-8")
                    override_path.write_text(self.marked_content(override_path.suffix), encoding="utf-8")

                    self.assertEqual(1, self.generate_primary(cli_id, output_directory))
                    self.assertTrue(self.generator.has_generated_marker(primary_path))
                    self.assertFalse(override_path.exists())

    def test_marked_and_unmarked_stale_notes_are_handled_safely(self):
        """Cleanup removes marked legacy notes while preserving unmarked notes."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            marked_note_path = output_directory / "settings.override.md"
            unmarked_note_path = output_directory / "agent.override.md"
            marked_note_path.write_text(self.marked_content(".md"), encoding="utf-8")
            unmarked_note_content = "User-owned migration note.\n"
            unmarked_note_path.write_text(unmarked_note_content, encoding="utf-8")
            profile = self.orchestrator_entries()[0][0]

            self.generator.cleanup_previous_generated_files(output_directory, "claude-code", [profile])
            self.generator.cleanup_previous_generated_files(output_directory, "amazon-kiro", [profile])

            self.assertFalse(marked_note_path.exists())
            self.assertEqual(unmarked_note_content, unmarked_note_path.read_text(encoding="utf-8"))

    def test_legacy_claude_and_amazon_notes_migrate_only_at_managed_paths(self):
        """Reciprocal verified legacy notes are removed without broad note ownership."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                for cli_id, note_name in (("claude-code", "settings.override.md"), ("amazon-kiro", "agent.override.md")):
                    with self.subTest(cli_id=cli_id):
                        output_directory = managed_root / "configs" / cli_id
                        output_directory.mkdir(parents=True)
                        self.write_legacy_catalog(output_directory)
                        note_path = output_directory / note_name
                        note_path.write_text(
                            "# Generated by scripts/generate-agent-configs.py.\n# Manual merge required: legacy note.\n",
                            encoding="utf-8",
                        )

                        self.generator.cleanup_previous_generated_files(
                            output_directory, cli_id, [self.orchestrator_entries()[0][0]]
                        )

                        self.assertFalse(note_path.exists())

    def test_amazon_kiro_marked_steering_refreshes_and_user_steering_survives(self):
        """Amazon Kiro steering follows the same marker ownership rules as primaries."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            steering_path = output_directory / "steering" / "orchestrator.md"
            steering_path.parent.mkdir(parents=True)
            steering_path.write_text(self.marked_content(".md"), encoding="utf-8")

            self.assertEqual(1, self.generate_primary("amazon-kiro", output_directory, "updated prompt"))
            self.assertTrue(self.generator.has_generated_marker(steering_path))
            self.assertIn("updated prompt", steering_path.read_text(encoding="utf-8"))

            user_steering_content = "---\ninclusion: auto\n---\nUser steering.\n"
            steering_path.write_text(user_steering_content, encoding="utf-8")
            self.assertEqual(0, self.generate_primary("amazon-kiro", output_directory, "replacement prompt"))
            self.assertEqual(user_steering_content, steering_path.read_text(encoding="utf-8"))

    def test_verified_legacy_amazon_steering_refreshes(self):
        """The exact managed Amazon Kiro legacy steering signature migrates safely."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            managed_root = Path(temporary_directory)
            with patch.object(self.generator, "ROOT", managed_root):
                output_directory = managed_root / "configs" / "amazon-kiro"
                output_directory.mkdir(parents=True)
                self.write_legacy_catalog(output_directory)
                steering_path = output_directory / "steering" / "orchestrator.md"
                steering_path.parent.mkdir()
                steering_path.write_text(
                    "---\ninclusion: auto\n---\n\n# You are the Orchestrator\n\n"
                    f"read {managed_root}/capability-routing.md\n",
                    encoding="utf-8",
                )

                self.assertEqual(1, self.generate_primary("amazon-kiro", output_directory, "updated prompt"))
                self.assertTrue(self.generator.has_generated_marker(steering_path))
                self.assertIn("updated prompt", steering_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
