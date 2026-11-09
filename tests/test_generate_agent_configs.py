"""Regression coverage for portable, ownership-safe CLI agent generation."""

from __future__ import annotations

import importlib.util
import json
import re
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


def load_roles_generator_module():
    """Load the standalone role generator for direct rendering tests."""
    specification = importlib.util.spec_from_file_location(
        "generate_roles", ROOT / "scripts" / "generate-roles.py"
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
        cls.roles_generator = load_roles_generator_module()

    def registry_profiles(self) -> list[dict]:
        """Return canonical profiles used by generator behavior tests."""
        return self.generator.load_registry("profiles")["profiles"]

    def worker_profiles(self) -> dict[str, dict]:
        """Return canonical subagent-only worker profiles by id."""
        return {
            str(profile["id"]): profile
            for profile in self.registry_profiles()
            if profile.get("subagent_only") is True
        }

    def generate_cli_mode(
        self,
        cli_id: str,
        output_directory: Path,
        role_levels_mode: str,
        preset: str = "",
        model_prefix: str = "",
        role_preset_specs: list[str] | None = None,
    ) -> None:
        """Generate one CLI target with explicit mode and model settings."""
        self.generator.generate_agent_configs(
            cli_id,
            output_directory,
            preset,
            self.generator.DEFAULT_TEMPLATES_PATH,
            model_prefix,
            role_levels_mode,
            role_preset_specs or [],
        )

    def agent_content(
        self,
        cli_id: str,
        output_directory: Path,
        profile: dict,
        level: str,
        role_levels_mode: str,
    ) -> str:
        """Read one generated agent artifact using the canonical generated id."""
        options = self.generator.CLI_TARGETS[cli_id]
        agent_id = self.generator.generated_agent_id(profile, level, role_levels_mode)
        path = output_directory / options["agent_directory"] / f"{agent_id}{options['extension']}"
        return path.read_text(encoding="utf-8")

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
            self.generator.DEFAULT_TEMPLATES_PATH,
            options["model_prefix"],
            options["role_levels_mode"],
            [],
        )

    def generated_prompt_paths(self, cli_id: str, output_directory: Path) -> tuple[Path, Path]:
        """Return the generated specialist and orchestrator prompt paths for a CLI."""
        options = self.generator.MANAGED_CLI_GENERATION_OPTIONS[cli_id]
        extension = self.generator.CLI_TARGETS[cli_id]["extension"]
        agent_directory = output_directory / self.generator.CLI_TARGETS[cli_id]["agent_directory"]
        specialist_id = self.generator.generated_agent_id(
            {"id": "backend-engineer", "seniority": ["senior"]},
            "senior",
            options["role_levels_mode"],
        )
        orchestrator_id = self.generator.generated_agent_id(
            {"id": "orchestrator", "seniority": ["senior"]},
            "senior",
            options["role_levels_mode"],
        )
        return (
            agent_directory / f"{specialist_id}{extension}",
            agent_directory / f"{orchestrator_id}{extension}",
        )

    def test_every_cli_routes_skills_only_in_orchestrator_prompts(self):
        """Generated specialist prompts omit self-routing while orchestrators assign skills."""
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        orchestrator_guidance = (
            "Keep workflow and delegation proportional",
            "For simple work, do not invent stages or parallel agents",
            "Preserve mandatory gates",
            "For complex work, split only into independently testable tasks",
            "target role",
            "explicit task",
            "skills/skills.md",
            "skills/catalog/roles/<target-role>/skills.md",
            "Stop after reading the relevant keyword catalogs.",
            "canonical skill name/path/reference",
            "target subagent to read and use its assigned `SKILL.md`",
            "target subagent is responsible for reading that skill body",
            "none",
            "rationale",
            "user request",
            "workflow",
            "stage",
            "Revisit",
            "security policy",
        )
        delegated_skill_body_instruction = "Read the selected `SKILL.md` files"
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli(cli_id, output_directory)
                    specialist_path, orchestrator_path = self.generated_prompt_paths(cli_id, output_directory)
                    specialist_content = specialist_path.read_text(encoding="utf-8")
                    orchestrator_content = orchestrator_path.read_text(encoding="utf-8")

                    self.assertNotIn("## Skill Routing", specialist_content)
                    self.assertNotIn("skills/catalog/roles/", specialist_content)
                    self.assertNotIn(delegated_skill_body_instruction, orchestrator_content)
                    for guidance in orchestrator_guidance:
                        with self.subTest(guidance=guidance):
                            self.assertIn(guidance, orchestrator_content)

    def test_canonical_profiles_define_exactly_two_junior_workers(self):
        """Canonical registry data contains only the two approved junior workers."""
        profiles = self.registry_profiles()
        worker_profiles = self.worker_profiles()

        self.assertEqual({"bulk-reader", "boilerplate-writer"}, set(worker_profiles))
        self.assertEqual(2, len(worker_profiles))
        self.assertEqual(42, len(profiles))
        for worker_id, profile in worker_profiles.items():
            with self.subTest(worker_id=worker_id):
                self.assertFalse(profile["default"])
                self.assertEqual(["junior"], profile["seniority"])
                self.assertTrue(profile["subagent_only"])
                role = profile["role"]
                role_text = " ".join(
                    [
                        str(role["title"]),
                        str(profile["description"]),
                        str(role["mission"]),
                        " ".join(role["responsibilities"]),
                        " ".join(role["guardrails"]),
                    ]
                ).lower()
                self.assertIn("junior", role_text)
                self.assertIn("recur", role_text)
                self.assertIn("outside", role_text)

    def test_existing_profile_seniority_is_unchanged(self):
        """Every pre-existing profile retains its approved seniority levels."""
        expected_seniority = {
            "personal-assistant": ["middle"],
            "orchestrator": ["senior"],
            "founder-ceo": ["senior", "lead"],
            "product-manager": ["middle"],
            "software-engineer": ["junior", "middle", "senior", "lead"],
            "backend-engineer": ["junior", "middle", "senior", "lead"],
            "frontend-engineer": ["junior", "middle", "senior", "lead"],
            "mobile-engineer": ["junior", "middle", "senior", "lead"],
            "qa-engineer": ["junior", "middle", "senior", "lead"],
            "security-engineer": ["middle", "senior", "lead"],
            "devops-platform-engineer": ["junior", "middle", "senior", "lead"],
            "data-analyst": ["junior", "middle", "senior"],
            "ai-engineer": ["middle", "senior", "lead"],
            "ux-ui-designer": ["junior", "middle", "senior", "lead"],
            "business-analyst": ["middle", "senior"],
            "ux-researcher": ["middle", "senior"],
            "solution-architect": ["senior", "lead"],
            "tech-lead": ["senior", "lead"],
            "release-manager": ["senior", "lead"],
            "customer-success-support": ["junior", "middle", "senior"],
            "operations-manager": ["middle", "senior", "lead"],
            "creative-media-producer": ["junior", "middle", "senior"],
            "data-engineer": ["junior", "middle", "senior", "lead"],
            "blockchain-engineer": ["middle", "senior", "lead"],
            "hardware-iot-engineer": ["middle", "senior", "lead"],
            "product-strategist": ["senior", "lead"],
            "market-researcher": ["junior", "middle"],
            "growth-marketer": ["middle", "senior"],
            "product-marketing-manager": ["middle", "senior"],
            "sales-strategist": ["middle", "senior", "lead"],
            "security-architect": ["senior", "lead"],
            "compliance-officer": ["senior", "lead"],
            "data-protection-officer": ["senior", "lead"],
            "sre": ["junior", "middle", "senior", "lead"],
            "incident-manager": ["senior", "lead"],
            "finops-analyst": ["middle", "senior"],
            "finance-manager": ["senior", "lead"],
            "technical-writer": ["junior", "middle", "senior", "lead"],
            "hr-manager": ["senior", "lead"],
            "engineering-manager": ["senior", "lead"],
        }
        actual_seniority = {
            str(profile["id"]): profile.get("seniority")
            for profile in self.registry_profiles()
            if profile.get("subagent_only") is not True
        }
        self.assertEqual(expected_seniority, actual_seniority)

    def test_above_junior_guidance_is_rendered_for_all_profiles_and_clis(self):
        """Every effective above-junior role gets guidance on all CLI targets."""
        above_junior_levels = {"middle", "senior", "lead"}
        profiles = self.registry_profiles()
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli_mode(cli_id, output_directory, "tiered")
                    for profile in profiles:
                        profile_id = str(profile["id"])
                        generated_levels = self.generator.profile_generation_levels(profile, "tiered")
                        for level in generated_levels:
                            content = self.agent_content(
                                cli_id, output_directory, profile, level, "tiered"
                            )
                            with self.subTest(profile_id=profile_id, level=level):
                                self.assertNotIn("{{", content)
                                if level in above_junior_levels and profile.get("subagent_only") is not True:
                                    self.assertIn("## Low-Level Delegation", content)
                                    self.assertIn("only when the assigned level is above junior", content)
                                    self.assertIn("bulk-reader-junior", content)
                                    self.assertIn("boilerplate-writer-junior", content)
                                else:
                                    self.assertNotIn("## Low-Level Delegation", content)

    def test_generic_roles_use_profile_capability_without_effective_level(self):
        """Generic role files use neutral worker ids and no generated level title."""
        registry = self.generator.load_registry("profiles")
        common_instructions = self.generator.string_list(registry.get("common_instructions"))
        security_baseline = self.generator.security_baseline_from_policy(registry)
        guidance = self.generator.string_list(registry.get("low_level_delegation_instructions"))
        for profile in registry["profiles"]:
            profile_id = str(profile["id"])
            content = self.roles_generator.generated_role_content(
                profile, common_instructions, security_baseline, guidance
            )
            with self.subTest(profile_id=profile_id):
                self.assertNotIn("{{", content)
                self.assertNotRegex(content, r"^# Role: (junior|middle|senior|lead) ", re.MULTILINE)
                if set(profile.get("seniority", [])) & {"middle", "senior", "lead"}:
                    self.assertIn("## Low-Level Delegation", content)
                    self.assertIn("only when the assigned level is above junior", content)
                    self.assertIn("`bulk-reader`", content)
                    self.assertIn("`boilerplate-writer`", content)
                else:
                    self.assertNotIn("## Low-Level Delegation", content)

    def test_single_mode_selected_levels_get_collapsed_worker_guidance(self):
        """Single-mode selected middle, senior, and lead roles use collapsed ids."""
        above_junior_levels = {"middle", "senior", "lead"}
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli_mode(cli_id, output_directory, "single")
                    for profile in self.registry_profiles():
                        level = self.generator.selected_role_level(profile)
                        content = self.agent_content(
                            cli_id, output_directory, profile, level, "single"
                        )
                        with self.subTest(profile_id=profile["id"], level=level):
                            if level in above_junior_levels and profile.get("subagent_only") is not True:
                                self.assertIn("## Low-Level Delegation", content)
                                self.assertIn("`bulk-reader`", content)
                                self.assertIn("`boilerplate-writer`", content)
                            else:
                                self.assertNotIn("## Low-Level Delegation", content)

    def test_workers_have_no_guidance_and_minimal_cli_controls(self):
        """Workers remain non-recursive and receive only supported read-only controls."""
        worker_profiles = self.worker_profiles()
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli_mode(cli_id, output_directory, "tiered")
                    for worker_id, profile in worker_profiles.items():
                        content = self.agent_content(
                            cli_id, output_directory, profile, "junior", "tiered"
                        )
                        with self.subTest(worker_id=worker_id):
                            self.assertNotIn("## Low-Level Delegation", content)
                            self.assertNotIn("{{", content)
                            self.assertIn("must not recurse", content.lower())
                            if cli_id == "claude-code":
                                self.assertRegex(content, r"(?m)^tools:\n  - Read$")
                                self.assertIn("hidden: true", content)
                            elif cli_id in {"kilo-code", "opencode"}:
                                self.assertIn("mode: subagent", content)
                                self.assertIn("hidden: true", content)
                                for denied_permission in (
                                    "task: deny",
                                    "edit: deny",
                                    "bash: deny",
                                    "webfetch: deny",
                                    "websearch: deny",
                                ):
                                    self.assertIn(denied_permission, content)
                                self.assertNotIn("mcp:", content)
                                self.assertNotIn("network:", content)
                            elif cli_id == "amazon-kiro":
                                parsed_content = json.loads(content)
                                self.assertEqual(["read"], parsed_content["tools"])
                                for unsupported_field in ("hidden", "mode", "permission", "mcpServers"):
                                    self.assertNotIn(unsupported_field, parsed_content)
                            else:
                                self.assertNotRegex(
                                    content,
                                    r"(?m)^(tools|permission|hidden|mode|network|mcp)\s*[:=]",
                                )

    def test_single_mode_worker_ids_and_markers_remain_explicitly_junior(self):
        """Collapsed worker artifacts keep junior markers in identity and prompt."""
        worker_profiles = self.worker_profiles()
        cli_ids = ("amazon-kiro", "claude-code", "codex", "kilo-code", "opencode")
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            for cli_id in cli_ids:
                with self.subTest(cli_id=cli_id):
                    output_directory = temporary_root / cli_id
                    self.generate_cli_mode(cli_id, output_directory, "single")
                    for worker_id, profile in worker_profiles.items():
                        content = self.agent_content(
                            cli_id, output_directory, profile, "junior", "single"
                        )
                        with self.subTest(worker_id=worker_id):
                            self.assertIn(worker_id, content)
                            self.assertNotIn(f"{worker_id}-junior", content)
                            self.assertIn("junior", content.lower())
                            self.assertIn("As a junior", content)

    def test_workers_use_existing_junior_model_defaults(self):
        """Model resolution for workers uses each CLI preset's existing junior tier."""
        worker_profiles = self.worker_profiles()
        model_tiers_registry = self.generator.load_registry("model-tiers")
        for cli_id, options in self.generator.MANAGED_CLI_GENERATION_OPTIONS.items():
            if cli_id == "amazon-kiro":
                continue
            with tempfile.TemporaryDirectory() as temporary_directory:
                output_directory = Path(temporary_directory) / cli_id
                self.generate_cli_mode(
                    cli_id,
                    output_directory,
                    options["role_levels_mode"],
                    options["preset"],
                    options["model_prefix"],
                )
                for worker_id, profile in worker_profiles.items():
                    expected_configuration = self.generator.preset_configuration_for_level(
                        model_tiers_registry["recommended_defaults"],
                        "junior",
                        options["preset"],
                        worker_id,
                    )
                    expected_model = self.generator.rendered_model_id(
                        model_tiers_registry,
                        str(expected_configuration["model"]),
                        options["model_prefix"],
                        worker_id,
                        cli_id in self.generator.DEFAULT_MODEL_PREFIXES,
                    )
                    content = self.agent_content(
                        cli_id,
                        output_directory,
                        profile,
                        "junior",
                        options["role_levels_mode"],
                    )
                    with self.subTest(cli_id=cli_id, worker_id=worker_id):
                        self.assertIn(f'model: "{expected_model}"' if cli_id != "codex" else f'model = "{expected_model}"', content)

    def test_explicit_codex_presets_preserve_current_yaml_matrix(self):
        """Explicit Codex generation follows every model and level in the YAML matrix."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        recommended_defaults = model_tiers_registry["recommended_defaults"]
        backend_profile = next(
            profile for profile in self.registry_profiles() if profile.get("id") == "backend-engineer"
        )

        preset_names = sorted(recommended_defaults["junior"])
        for preset in preset_names:
            with self.subTest(preset=preset):
                with tempfile.TemporaryDirectory() as temporary_directory:
                    output_directory = Path(temporary_directory)
                    self.generate_cli_mode("codex", output_directory, "tiered", preset)
                    for level in ("junior", "middle", "senior", "lead"):
                        expected_configuration = recommended_defaults[level][preset]
                        content = self.agent_content(
                            "codex", output_directory, backend_profile, level, "tiered"
                        )
                        self.assertIn(f'model = "{expected_configuration["model"]}"', content)

    def test_gpt6_catalog_entries_match_published_metadata(self):
        """GPT-6 Luna and Sol keep the published IDs, prices, and capabilities."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        providers_by_id = {provider["id"]: provider for provider in model_tiers_registry["providers"]}

        def models_by_id(provider_id):
            """Index one provider's model rows by their catalog id."""
            return {
                model["model_id"]: model
                for tier in providers_by_id[provider_id]["tiers"].values()
                for model in tier["models"]
            }

        openai_models = models_by_id("openai")
        openrouter_models = models_by_id("openrouter")
        expected_capabilities = (
            "[improved_coding, improved_factuality, improved_computer_use, "
            "improved_collaboration, improved_caching, improved_alignment]"
        )
        expected_metadata = {
            "gpt-6-luna": {
                "openrouter_id": "openai/gpt-6-luna",
                "pricing_per_million_tokens": "{ input: 0.10, output: 0.50 }",
                "capabilities": expected_capabilities,
                "level": "medium",
            },
            "gpt-6-sol": {
                "openrouter_id": "openai/gpt-6-sol",
                "pricing_per_million_tokens": "{ input: 2.00, output: 10.00 }",
                "capabilities": expected_capabilities,
                "level": "medium",
            },
        }
        for model_id, expected_model_metadata in expected_metadata.items():
            with self.subTest(model_id=model_id):
                direct_model = openai_models[model_id]
                openrouter_model = openrouter_models[f"openai/{model_id}"]
                for catalog_model in (direct_model, openrouter_model):
                    self.assertEqual(
                        expected_model_metadata,
                        {
                            key: catalog_model[key]
                            for key in expected_model_metadata
                        },
                    )
                    self.assertNotIn("context", catalog_model)
                    self.assertNotIn("max_output", catalog_model)
                self.assertEqual(direct_model["openrouter_id"], openrouter_model["openrouter_id"])
        self.assertNotIn("gpt-6-luna-pro", openai_models)
        self.assertNotIn("gpt-6-sol-pro", openai_models)
        self.assertNotIn("openai/gpt-6-luna-pro", openrouter_models)
        self.assertNotIn("openai/gpt-6-sol-pro", openrouter_models)

    def test_gpt6_1_sol_catalog_entries_are_lookup_stubs(self):
        """GPT-6.1 Sol remains unverified while its provider IDs are cataloged."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        providers_by_id = {provider["id"]: provider for provider in model_tiers_registry["providers"]}

        def models_by_id(provider_id):
            """Index one provider's model rows by their catalog id."""
            return {
                model["model_id"]: model
                for tier in providers_by_id[provider_id]["tiers"].values()
                for model in tier["models"]
            }

        openai_model = models_by_id("openai")["gpt-6.1-sol"]
        openrouter_model = models_by_id("openrouter")["openai/gpt-6.1-sol"]
        for catalog_model in (openai_model, openrouter_model):
            self.assertEqual("openai/gpt-6.1-sol", catalog_model["openrouter_id"])
            self.assertIsNone(catalog_model["coding_index"])
            self.assertEqual("medium", catalog_model["level"])
            self.assertNotIn("context", catalog_model)
            self.assertNotIn("max_output", catalog_model)
            self.assertNotIn("pricing_per_million_tokens", catalog_model)
            self.assertNotIn("capabilities", catalog_model)

    def test_role_preset_selects_each_current_codex_preset(self):
        """Role-preset overrides use the source matrix for every tier and preset."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        recommended_defaults = model_tiers_registry["recommended_defaults"]
        backend_profile = next(
            profile for profile in self.registry_profiles() if profile.get("id") == "backend-engineer"
        )

        for preset in sorted(recommended_defaults["junior"]):
            with self.subTest(preset=preset), tempfile.TemporaryDirectory() as temporary_directory:
                output_directory = Path(temporary_directory)
                self.generate_cli_mode(
                    "codex",
                    output_directory,
                    "tiered",
                    "openai",
                    role_preset_specs=[f"backend-engineer={preset}"],
                )
                for level in ("junior", "middle", "senior", "lead"):
                    content = self.agent_content(
                        "codex", output_directory, backend_profile, level, "tiered"
                    )
                    self.assertIn(
                        f'model = "{recommended_defaults[level][preset]["model"]}"', content
                    )

    def test_kilo_and_opencode_provider_lookup_handles_all_presets_and_hybrids(self):
        """Kilo and OpenCode translate every source preset to native reasoning fields."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        recommended_defaults = model_tiers_registry["recommended_defaults"]
        backend_profile = next(
            profile for profile in self.registry_profiles() if profile.get("id") == "backend-engineer"
        )

        for cli_id in ("kilo-code", "opencode"):
            model_prefix = self.generator.MANAGED_CLI_GENERATION_OPTIONS[cli_id]["model_prefix"]
            for preset in sorted(recommended_defaults["junior"]):
                with self.subTest(cli_id=cli_id, preset=preset), tempfile.TemporaryDirectory() as temporary_directory:
                    output_directory = Path(temporary_directory)
                    self.generate_cli_mode(
                        cli_id,
                        output_directory,
                        "tiered",
                        preset,
                        model_prefix,
                    )
                    for level in ("junior", "middle", "senior", "lead"):
                        expected_configuration = recommended_defaults[level][preset]
                        content = self.agent_content(
                            cli_id, output_directory, backend_profile, level, "tiered"
                        )
                        expected_model = str(expected_configuration["model"])
                        rendered_model = self.generator.rendered_model_id(
                            model_tiers_registry,
                            expected_model,
                            model_prefix,
                            str(backend_profile["id"]),
                            cli_id in self.generator.DEFAULT_MODEL_PREFIXES,
                        )
                        self.assertIn(f'model: "{rendered_model}"', content)
                        provider_id = self.generator.native_reasoning_provider(
                            model_tiers_registry, expected_model
                        )
                        if provider_id:
                            expected_provider_options = self.generator.provider_reasoning_yaml(
                                provider_id, str(expected_configuration["level"])
                            )
                            self.assertIn(
                                f'variant: "{expected_configuration["level"]}"'
                                + expected_provider_options,
                                content,
                            )
                        else:
                            self.assertNotIn("variant:", content)

    def test_kilo_zai_codex_auto_free_junior_middle_emit_no_reasoning_options(self):
        """Auto Free junior and middle agents keep the bare rendered id without reasoning fields.

        The registry declares ``kilo-zai-codex`` level ``max`` for junior and middle,
        but Kilo's Auto Free entry resolves its underlying model dynamically and has
        no client-selectable reasoning variants, so the generated configs must carry
        only the ``kilo/kilo-auto/free`` model id. Emission of ``variant`` or provider
        reasoning options would send unsupported configuration to Auto Free.
        """
        model_tiers_registry = self.generator.load_registry("model-tiers")
        recommended_defaults = model_tiers_registry["recommended_defaults"]
        backend_profile = next(
            profile for profile in self.registry_profiles() if profile.get("id") == "backend-engineer"
        )

        for level in ("junior", "middle"):
            with self.subTest(level=level):
                self.assertEqual(
                    {"model": "kilo-auto/free", "level": "max"},
                    dict(recommended_defaults[level]["kilo-zai-codex"]),
                )

        model_prefix = self.generator.MANAGED_CLI_GENERATION_OPTIONS["kilo-code"]["model_prefix"]
        with tempfile.TemporaryDirectory() as temporary_directory:
            output_directory = Path(temporary_directory)
            self.generate_cli_mode(
                "kilo-code",
                output_directory,
                "tiered",
                "kilo-zai-codex",
                model_prefix,
            )
            for level in ("junior", "middle"):
                content = self.agent_content(
                    "kilo-code", output_directory, backend_profile, level, "tiered"
                )
                with self.subTest(level=level):
                    self.assertIn('model: "kilo/kilo-auto/free"', content)
                    for unsupported_reasoning_field in (
                        "variant:",
                        "effort:",
                        "thinking:",
                        "thinkingConfig:",
                        "enable_thinking:",
                        "reasoningEffort:",
                        "reasoning_effort:",
                    ):
                        self.assertNotIn(unsupported_reasoning_field, content)

    def test_codex_primary_reasoning_follows_direct_openai_models(self):
        """Codex primary settings follow the senior defaults and OpenAI translation."""
        model_tiers_registry = self.generator.load_registry("model-tiers")
        recommended_defaults = model_tiers_registry["recommended_defaults"]
        for preset in sorted(recommended_defaults["senior"]):
            expected_configuration = recommended_defaults["senior"][preset]
            provider_id = self.generator.native_reasoning_provider(
                model_tiers_registry, str(expected_configuration["model"])
            )
            expected_output_level = (
                {"max": "xhigh"}.get(str(expected_configuration["level"]), str(expected_configuration["level"]))
                if provider_id == "openai"
                else None
            )
            with self.subTest(preset=preset), tempfile.TemporaryDirectory() as temporary_directory:
                output_directory = Path(temporary_directory)
                self.generate_cli_mode("codex", output_directory, "tiered", preset)
                primary_content = (output_directory / "config.toml").read_text(encoding="utf-8")
                self.assertIn(f'model = "{expected_configuration["model"]}"', primary_content)
                if expected_output_level is None:
                    self.assertNotIn("model_reasoning_effort", primary_content)
                else:
                    self.assertIn(
                        f'model_reasoning_effort = "{expected_output_level}"',
                        primary_content,
                    )

        self.assertEqual(
            '\nreasoningEffort: "xhigh"',
            self.generator.provider_reasoning_yaml("openai", "max"),
        )

    def test_zai_coding_prefixes_resolve_virtual_provider_reasoning(self):
        """Current and legacy Z.AI coding prefixes share the virtual provider mapping."""
        model_tiers_registry = self.generator.load_registry("model-tiers")

        for model_prefix in ("zai-coding-plan/", "zai-coding/"):
            with self.subTest(model_prefix=model_prefix):
                model_id = f"{model_prefix}glm-5.3"
                self.assertEqual(
                    "z-ai-coding",
                    self.generator.native_reasoning_provider(model_tiers_registry, model_id),
                )
                reasoning_suffix = self.generator.agent_reasoning_suffix(
                    "kilo-code",
                    model_id,
                    model_id,
                    "max",
                    model_tiers_registry,
                )
                self.assertIn('variant: "max"', reasoning_suffix)
                self.assertIn('thinking:\n  type: "enabled"', reasoning_suffix)
                self.assertIn('reasoning_effort: "max"', reasoning_suffix)

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

    def test_explicit_absolute_templates_path_is_embedded_in_generated_role(self):
        """An explicitly supplied absolute templates path is preserved in role content."""
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            output_directory = temporary_root / "generated"
            explicit_templates_path = temporary_root / "explicit-registry"
            options = self.generator.MANAGED_CLI_GENERATION_OPTIONS["amazon-kiro"]

            self.generator.generate_agent_configs(
                "amazon-kiro",
                output_directory,
                options["preset"],
                f"  {explicit_templates_path}/  ",
                options["model_prefix"],
                options["role_levels_mode"],
                [],
            )

            role_path = output_directory / "agents" / "orchestrator.json"
            role_content = role_path.read_text(encoding="utf-8")
            self.assertIn(f"{explicit_templates_path}/skills/skills.md", role_content)
            self.assertNotIn("~/.ai-registry", role_content)

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
                        # Preserve the former skill reference in this migration
                        # fixture so it remains an actual pre-refactor legacy role.
                        if cli_id == "codex":
                            fixture_content = fixture_content.replace(
                                "\\n\\n## Output Format",
                                "\\n\\n- read `~/.ai-registry/skills/skills.md`\\n\\n## Output Format",
                                1,
                            )
                        else:
                            fixture_content = fixture_content.replace(
                                "\n## Output Format",
                                "\n- read `~/.ai-registry/skills/skills.md`\n\n## Output Format",
                                1,
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
