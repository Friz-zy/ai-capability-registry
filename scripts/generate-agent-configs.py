#!/usr/bin/env python3
"""Generate CLI agent role configs from registry profiles and model tiers."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

from registry_lib import ROOT, RegistryError, load_registry, write_text


ROLE_TEMPLATES_DIR = ROOT / "templates" / "roles"
AGENT_TEMPLATES_DIR = ROOT / "templates" / "agents"
DEFAULT_TEMPLATES_PATH = "~/.ai-registry"

CLI_TARGETS: dict[str, dict[str, str]] = {
    "codex": {"template_dir": "codex", "extension": ".toml", "agent_directory": "roles", "role_catalog_path": "roles.md"},
    "claude-code": {"template_dir": "claude-code", "extension": ".md", "agent_directory": "agents", "role_catalog_path": "roles.md"},
    "kilo-code": {"template_dir": "kilo-code", "extension": ".md", "agent_directory": "agent", "role_catalog_path": "roles.md"},
    "opencode": {"template_dir": "opencode", "extension": ".md", "agent_directory": "agents", "role_catalog_path": "roles.md"},
    "amazon-kiro": {"template_dir": "amazon-kiro", "extension": ".json", "agent_directory": "agents", "role_catalog_path": "roles.md"},
}

LEGACY_AGENT_DIRECTORIES: dict[str, list[str]] = {
    "claude-code": [".claude/agents"],
    "kilo-code": [".kilo/agent"],
    "opencode": [".opencode/agents"],
    "amazon-kiro": [".kiro/agents"],
}

DEFAULT_MODEL_PREFIXES: dict[str, str] = {
    "kilo-code": "kilo",
    "opencode": "opencode-go",
}

DEFAULT_PRESETS: dict[str, str] = {
    "codex": "openai",
    "claude-code": "anthropic",
    "kilo-code": "opencode",
    "opencode": "opencode",
    "amazon-kiro": "none",
}

ROLE_LEVEL_MODES = {"tiered", "single"}
ABOVE_JUNIOR_LEVELS = {"middle", "senior", "lead"}
LOW_LEVEL_WORKER_PROFILE_IDS = {
    "bulk_reader_agent_id": "bulk-reader",
    "boilerplate_writer_agent_id": "boilerplate-writer",
}

DISABLED_MODEL_PRESETS = {"", "none"}
MODEL_REMOVAL_TOKEN = "__MODEL_FIELD_DISABLED__"
REASONING_LEVELS = {"none", "minimal", "low", "medium", "high", "xhigh", "max"}
REASONING_LEVEL_ORDER = ["none", "minimal", "low", "medium", "high", "xhigh", "max"]
GENERATOR_MARKER_VALUE = "scripts/generate-agent-configs.py"
TOML_GENERATOR_MARKER = f"# generated-by: {GENERATOR_MARKER_VALUE}"
JSONC_GENERATOR_MARKER = f"// generated-by: {GENERATOR_MARKER_VALUE}"
MARKDOWN_GENERATOR_MARKER = f"<!-- generated-by: {GENERATOR_MARKER_VALUE} -->"

CLI_ALIASES = {
    "codex": "codex",
    "codex-cli": "codex",
    "claude": "claude-code",
    "claude-code": "claude-code",
    "kilo": "kilo-code",
    "kilocode": "kilo-code",
    "kilo-code": "kilo-code",
    "opencode": "opencode",
    "kiro": "amazon-kiro",
    "amazon-kiro": "amazon-kiro",
}

MANAGED_CLI_GENERATION_OPTIONS = {
    "amazon-kiro": {"preset": "none", "model_prefix": "", "role_levels_mode": "single"},
    "claude-code": {"preset": "anthropic", "model_prefix": "", "role_levels_mode": "tiered"},
    "codex": {"preset": "openai", "model_prefix": "", "role_levels_mode": "tiered"},
    "kilo-code": {"preset": "opencode", "model_prefix": "kilo", "role_levels_mode": "tiered"},
    "opencode": {"preset": "opencode", "model_prefix": "opencode-go", "role_levels_mode": "tiered"},
}

# This exact historical Amazon Kiro tiered-role ID was tracked before the
# target changed to single-level roles. Keeping the manifest finite prevents a
# user-created legacy-looking file from acquisition.
HISTORICAL_MANAGED_LEGACY_AGENT_IDS = {
    "amazon-kiro": frozenset({"backend-engineer-senior"}),
}


def template_text(path: Path) -> str:
    """Read a template file.

    Args:
        path: Template path to read.

    Returns:
        Template content without trailing whitespace.

    Raises:
        FileNotFoundError: If the template path does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(f"Missing template: {path}")
    return path.read_text(encoding="utf-8").rstrip()


def render_text(template: str, values: dict[str, Any], source_name: str) -> str:
    """Render a simple placeholder template.

    Args:
        template: Template content with ``{{placeholder}}`` markers.
        values: Placeholder values keyed by marker name.
        source_name: Human-readable template name for error messages.

    Returns:
        Rendered text.

    Raises:
        ValueError: If any placeholder remains unresolved.
    """
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", str(value))
    unresolved_placeholders = re.findall(r"\{\{[a-zA-Z0-9_]+\}\}", rendered)
    if unresolved_placeholders:
        unique_placeholders = ", ".join(sorted(set(unresolved_placeholders)))
        raise ValueError(f"Unresolved placeholder(s) in {source_name}: {unique_placeholders}")
    return compact_blank_lines(rendered)


def compact_blank_lines(text: str) -> str:
    """Collapse excessive blank lines in generated text.

    Args:
        text: Rendered text.

    Returns:
        Text with at most one empty line between content blocks.
    """
    return re.sub(r"\n{3,}", "\n\n", text).rstrip()


def remove_model_field(rendered_text: str, file_extension: str) -> str:
    """Remove a rendered model field from generated CLI files.

    Args:
        rendered_text: Fully rendered file content.
        file_extension: Output file extension used to select the syntax.

    Returns:
        Content without a rendered model field.
    """
    if file_extension == ".toml":
        cleaned_text = re.sub(r"(?m)^[ \t]*model[ \t]*=.*\n?", "", rendered_text)
    elif file_extension == ".md":
        cleaned_text = re.sub(r"(?m)^[ \t]*model:[^\n]*\n?", "", rendered_text)
    elif file_extension == ".json":
        cleaned_text = re.sub(r"(?m)^[ \t]*\"model\"[ \t]*:[^\n]*,?\n?", "", rendered_text)
    else:
        cleaned_text = rendered_text
    return compact_blank_lines(cleaned_text)


def string_list(value: Any) -> list[str]:
    """Normalize registry scalars or lists to a list of strings.

    Args:
        value: Registry value.

    Returns:
        Non-empty string values.
    """
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    if isinstance(value, str) and value:
        return [value]
    return []


def bullet_list(values: list[str]) -> str:
    """Render Markdown bullet items.

    Args:
        values: Values to render.

    Returns:
        Markdown bullet list or a fallback item.
    """
    if not values:
        return "- Not specified."
    return "\n".join(f"- {value}" for value in values)


def markdown_section(title: str, values: list[str]) -> str:
    """Render an optional Markdown section from registry values.

    Args:
        title: Section heading without Markdown prefix.
        values: Values to render as bullets.

    Returns:
        Section text when values exist, otherwise an empty string.
    """
    if not values:
        return ""
    return f"## {title}\n\n{bullet_list(values)}\n\n"


def security_baseline_from_policy(profiles_registry: dict[str, Any]) -> list[str]:
    """Resolve the configured prompt-security baseline from the canonical policy registry.

    Args:
        profiles_registry: Loaded profiles registry containing the baseline policy reference.

    Returns:
        Baseline instructions and their policy-declared enforcement limit.

    Raises:
        ValueError: If the configured policy control or required fields are unavailable.
    """
    baseline_configuration = profiles_registry.get("security_baseline_policy")
    if not isinstance(baseline_configuration, dict):
        raise ValueError("registry/profiles.yaml must contain security_baseline_policy")
    policy_id = baseline_configuration.get("id")
    if not isinstance(policy_id, str) or not policy_id.strip():
        raise ValueError("security_baseline_policy.id must be a non-empty string")
    include_requirements = baseline_configuration.get("include_requirements")
    include_enforcement_limit = baseline_configuration.get("include_enforcement_limit")
    if not isinstance(include_requirements, bool):
        raise ValueError("security_baseline_policy.include_requirements must be a boolean")
    if not isinstance(include_enforcement_limit, bool):
        raise ValueError("security_baseline_policy.include_enforcement_limit must be a boolean")

    secure_sdd_policy = load_registry("policies").get("secure_sdd_policy")
    if not isinstance(secure_sdd_policy, dict):
        raise ValueError("registry/policies.yaml must contain secure_sdd_policy")
    controls = secure_sdd_policy.get("controls")
    if not isinstance(controls, list):
        raise ValueError("secure_sdd_policy.controls must be a list")
    matching_controls = [
        item for item in controls if isinstance(item, dict) and item.get("id") == policy_id
    ]
    if len(matching_controls) != 1:
        raise ValueError(
            f"security_baseline_policy must reference exactly one policy control '{policy_id}'"
        )
    control = matching_controls[0]

    baseline: list[str] = []
    if include_requirements:
        requirements = control.get("requirements")
        if (
            not isinstance(requirements, list)
            or not requirements
            or any(not isinstance(requirement, str) or not requirement.strip() for requirement in requirements)
        ):
            raise ValueError(f"Policy '{policy_id}' must have non-empty string requirements")
        baseline.extend(requirements)
    if include_enforcement_limit:
        enforcement_name = control.get("enforcement")
        if not isinstance(enforcement_name, str) or not enforcement_name.strip():
            raise ValueError(f"Policy '{policy_id}' has no valid enforcement classification")
        classifications = secure_sdd_policy.get("enforcement_model", {}).get("classifications", {})
        enforcement = classifications.get(enforcement_name) if isinstance(classifications, dict) else None
        enforcement_description = enforcement.get("description") if isinstance(enforcement, dict) else None
        if not isinstance(enforcement_description, str) or not enforcement_description.strip():
            raise ValueError(f"Policy '{policy_id}' has no declared enforcement-limit description")
        baseline.append(f"Enforcement limit: {enforcement_description}")
    if not baseline:
        raise ValueError(f"security_baseline_policy '{policy_id}' selected no baseline content")
    return baseline


def quoted_string(value: str) -> str:
    """Return a JSON-compatible quoted string usable in JSON, TOML, and YAML.

    Args:
        value: String to quote.

    Returns:
        Quoted string with escapes.
    """
    return json.dumps(value)


def profile_role(profile: dict[str, Any]) -> dict[str, Any]:
    """Return role metadata from a profile.

    Args:
        profile: Registry profile entry.

    Returns:
        Role mapping or an empty mapping.
    """
    role = profile.get("role")
    return role if isinstance(role, dict) else {}


def canonical_cli(cli_name: str) -> str:
    """Normalize a CLI name or alias to a supported target id.

    Args:
        cli_name: User-provided CLI name.

    Returns:
        Canonical CLI target id.

    Raises:
        ValueError: If the CLI name is unknown.
    """
    normalized_name = cli_name.strip().lower()
    if normalized_name not in CLI_ALIASES:
        supported_aliases = ", ".join(sorted(CLI_ALIASES))
        raise ValueError(f"Unknown CLI '{cli_name}'. Supported values: {supported_aliases}")
    return CLI_ALIASES[normalized_name]


def default_preset_for_cli(cli_id: str) -> str:
    """Return the default model preset for a CLI.

    Args:
        cli_id: Canonical CLI target id.

    Returns:
        Default preset key or ``none`` when the CLI does not use model fields.
    """
    return DEFAULT_PRESETS.get(cli_id, "none")


def normalized_role_levels_mode(role_levels_mode: str) -> str:
    """Validate and normalize the requested role-level generation mode.

    Args:
        role_levels_mode: User-provided mode string.

    Returns:
        Normalized mode name.

    Raises:
        ValueError: If the mode is unsupported.
    """
    normalized_mode = role_levels_mode.strip().lower()
    if normalized_mode not in ROLE_LEVEL_MODES:
        supported_modes = ", ".join(sorted(ROLE_LEVEL_MODES))
        raise ValueError(f"Unknown role levels mode '{role_levels_mode}'. Supported values: {supported_modes}")
    return normalized_mode


def available_presets(recommended_defaults: dict[str, Any]) -> list[str]:
    """Return model preset keys available in recommended defaults.

    Args:
        recommended_defaults: ``recommended_defaults`` mapping from model tiers.

    Returns:
        Sorted preset names.
    """
    preset_names: set[str] = set()
    for level_defaults in recommended_defaults.values():
        if isinstance(level_defaults, dict):
            preset_names.update(str(key) for key in level_defaults)
    return sorted(preset_names)


def preset_modeling_disabled(preset: str) -> bool:
    """Return whether model lookup and rendering are disabled.

    Args:
        preset: User-provided preset value.

    Returns:
        ``True`` when the preset disables model lookup and rendering.
    """
    return preset.strip().lower() in DISABLED_MODEL_PRESETS


def parse_role_preset_spec(spec: str) -> tuple[list[str], str]:
    """Parse a --role-preset CLI spec into role patterns and a preset key.

    A spec has the form ``roles=preset`` where ``roles`` is a comma-separated
    list of registry profile ids, optionally containing fnmatch globs, and
    ``preset`` is a model preset key from recommended_defaults.

    Args:
        spec: Raw spec string such as ``solution-architect=openai`` or
            ``*-architect,product-manager=openai``.

    Returns:
        Pair of role pattern list and preset key.

    Raises:
        ValueError: If the spec has no ``=``, an empty role list, or an empty preset.
    """
    if "=" not in spec:
        raise ValueError(
            f"Invalid --role-preset '{spec}'. Expected 'roles=preset' with a comma-separated role list."
        )
    roles_part, preset_part = spec.split("=", 1)
    patterns = [token.strip() for token in roles_part.split(",") if token.strip()]
    preset = preset_part.strip()
    if not patterns:
        raise ValueError(f"Invalid --role-preset '{spec}': no role patterns before '='.")
    if not preset:
        raise ValueError(f"Invalid --role-preset '{spec}': preset is empty after '='.")
    return patterns, preset


def resolve_role_preset_overrides(
    specs: list[str],
    profiles: list[dict[str, Any]],
) -> dict[str, str]:
    """Resolve --role-preset specs into a profile-id to preset mapping.

    Patterns are matched against registry profile ids using fnmatch (case
    sensitive), so ``*-architect`` matches both ``solution-architect`` and
    ``security-architect``. Specs are applied in order and later matches
    overwrite earlier ones, letting a broad pattern be refined by a later
    specific one. A pattern matching no profile prints a warning and is skipped.

    Args:
        specs: Raw --role-preset spec strings.
        profiles: Registry profile entries.

    Returns:
        Mapping from profile id to resolved preset key.
    """
    profile_ids = [str(profile.get("id") or "") for profile in profiles if isinstance(profile, dict)]
    overrides: dict[str, str] = {}
    for spec in specs:
        patterns, preset = parse_role_preset_spec(spec)
        for pattern in patterns:
            matched_ids = [
                profile_id
                for profile_id in profile_ids
                if profile_id and fnmatch.fnmatchcase(profile_id, pattern)
            ]
            if matched_ids:
                for profile_id in matched_ids:
                    overrides[profile_id] = preset
            else:
                print(
                    f"WARNING --role-preset pattern '{pattern}' matched no role; ignored.",
                    file=sys.stderr,
                )
    return overrides


def preset_configuration_for_level(
    recommended_defaults: dict[str, Any],
    level: str,
    preset: str,
    profile_id: str,
) -> dict[str, Any]:
    """Resolve the inline model and reasoning configuration for a profile level.

    Args:
        recommended_defaults: ``recommended_defaults`` mapping from model tiers.
        level: Seniority level such as ``middle`` or ``senior``.
        preset: Preset key such as ``openai`` or ``anthropic``.
        profile_id: Profile id used for precise errors.

    Returns:
        Preset mapping containing a model id and normalized reasoning level.

    Raises:
        ValueError: If the level, preset, model, or reasoning level is invalid.
    """
    level_defaults = recommended_defaults.get(level)
    if not isinstance(level_defaults, dict):
        raise ValueError(f"Missing recommended_defaults level '{level}' for profile '{profile_id}'")
    configuration = level_defaults.get(preset)
    if not isinstance(configuration, dict):
        raise ValueError(f"Missing model preset '{preset}' for profile '{profile_id}' level '{level}'")
    model_id = configuration.get("model")
    reasoning_level = configuration.get("level")
    if not isinstance(model_id, str) or not model_id:
        raise ValueError(f"Missing model for preset '{preset}' profile '{profile_id}' level '{level}'")
    if not isinstance(reasoning_level, str) or reasoning_level not in REASONING_LEVELS:
        raise ValueError(
            f"Invalid reasoning level for preset '{preset}' profile '{profile_id}' level '{level}'"
        )
    return configuration


def model_for_level(recommended_defaults: dict[str, Any], level: str, preset: str, profile_id: str) -> str:
    """Return the configured model id for a profile level and preset.

    Args:
        recommended_defaults: ``recommended_defaults`` mapping from model tiers.
        level: Seniority level such as ``middle`` or ``senior``.
        preset: Preset key such as ``openai`` or ``anthropic``.
        profile_id: Profile id used for precise errors.

    Returns:
        Bare or provider-qualified model id.
    """
    configuration = preset_configuration_for_level(recommended_defaults, level, preset, profile_id)
    return str(configuration["model"])


def normalize_model_prefix(model_prefix: str | None) -> str:
    """Normalize a model catalog prefix.

    Args:
        model_prefix: User-provided or CLI-default model prefix.

    Returns:
        Prefix without leading or trailing slashes, or an empty string when disabled.
    """
    if model_prefix is None:
        return ""
    return model_prefix.strip().strip("/")


def find_model_entry(model_tiers_registry: dict[str, Any], model_id: str) -> tuple[str | None, dict[str, Any] | None]:
    """Find a model catalog entry by model id.

    A bare id (e.g. ``gpt-5.6-terra``) matches the direct provider entry whose
    ``model_id`` equals it; a provider-qualified id (e.g. ``openai/gpt-5.6-luna-pro``)
    matches the provider/model pair that stores it verbatim. The first match wins.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id, bare or provider-qualified.

    Returns:
        Pair of native provider id and the matched model mapping, or
        ``(None, None)`` when no catalog entry matches.
    """
    providers = model_tiers_registry.get("providers", [])
    if not isinstance(providers, list):
        return None, None
    for provider in providers:
        if not isinstance(provider, dict):
            continue
        provider_id = provider.get("id")
        tiers = provider.get("tiers", {})
        if not isinstance(provider_id, str) or not isinstance(tiers, dict):
            continue
        for tier in tiers.values():
            if not isinstance(tier, dict):
                continue
            models = tier.get("models", [])
            if not isinstance(models, list):
                continue
            for model in models:
                if isinstance(model, dict) and model.get("model_id") == model_id:
                    return provider_id, model
    return None, None


def model_catalog_id_for_id(model_tiers_registry: dict[str, Any], model_id: str) -> str | None:
    """Find the provider-qualified catalog id for a registry model id.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id without provider prefix.

    Returns:
        Provider-qualified catalog id when the model is found, otherwise ``None``.
    """
    provider_id, model = find_model_entry(model_tiers_registry, model_id)
    if model is None:
        return None
    catalog_model_id = model.get("openrouter_id")
    if isinstance(catalog_model_id, str) and "/" in catalog_model_id:
        return catalog_model_id
    if isinstance(provider_id, str) and provider_id:
        return f"{provider_id}/{model_id}"
    return None


def provider_qualified_model(model_tiers_registry: dict[str, Any], model_id: str, profile_id: str) -> str:
    """Return a model id with its native model provider prefix.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id from recommended defaults.
        profile_id: Profile id used for precise errors.

    Returns:
        ``provider/model`` when a native provider can be resolved.

    Raises:
        ValueError: If an unqualified model cannot be found in the model catalog.
    """
    if "/" in model_id:
        return model_id
    catalog_model_id = model_catalog_id_for_id(model_tiers_registry, model_id)
    if not catalog_model_id:
        raise ValueError(f"Cannot resolve provider for model '{model_id}' used by profile '{profile_id}'")
    return catalog_model_id


def prefixed_model_id(model_id: str, model_prefix: str) -> str:
    """Apply an outer model catalog prefix.

    Args:
        model_id: Provider-qualified model id.
        model_prefix: Normalized outer provider prefix.

    Returns:
        Model id with the outer prefix applied, or the original model id when disabled.
    """
    if not model_prefix:
        return model_id
    if model_id.startswith(f"{model_prefix}/"):
        return model_id
    return f"{model_prefix}/{model_id}"


def rendered_model_id(
    model_tiers_registry: dict[str, Any],
    model_id: str,
    model_prefix: str,
    profile_id: str,
    force_provider_qualified: bool = False,
) -> str:
    """Resolve the final model id written to generated agent configs.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id from recommended defaults.
        model_prefix: Normalized outer provider prefix.
        profile_id: Profile id used for precise errors.
        force_provider_qualified: Whether to keep the native model provider
            even when the outer prefix is disabled.

    Returns:
        Raw model id, native ``provider/model``, or outer
        ``prefix/provider/model`` according to CLI needs.
    """
    if not model_prefix:
        if force_provider_qualified:
            return provider_qualified_model(model_tiers_registry, model_id, profile_id)
        return model_id
    qualified_model_id = provider_qualified_model(model_tiers_registry, model_id, profile_id)
    return prefixed_model_id(qualified_model_id, model_prefix)


def resolve_effective_reasoning(
    preset_configuration: dict[str, Any],
) -> str:
    """Return the reasoning level declared by an inline preset configuration.

    Args:
        preset_configuration: Resolved ``recommended_defaults`` entry.

    Returns:
        Valid normalized reasoning effort.
    """
    return str(preset_configuration["level"])


def clamp_reasoning_effort(reasoning_effort: str, supported_levels: list[str]) -> str:
    """Clamp a normalized reasoning level to a provider's supported ordered values.

    Args:
        reasoning_effort: Requested normalized reasoning level.
        supported_levels: Provider-supported levels ordered from least to most effort.

    Returns:
        Supported level closest to the requested level without increasing effort.
    """
    requested_index = REASONING_LEVEL_ORDER.index(reasoning_effort)
    supported_indexes = [(REASONING_LEVEL_ORDER.index(level), level) for level in supported_levels]
    eligible_levels = [entry for entry in supported_indexes if entry[0] <= requested_index]
    return (eligible_levels[-1] if eligible_levels else supported_indexes[0])[1]


def native_reasoning_provider(model_tiers_registry: dict[str, Any], model_id: str | None) -> str | None:
    """Resolve a model's provider, including the virtual zai-coding endpoint.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Bare or provider-qualified model id.

    Returns:
        Native provider id, or ``None`` when the model is unknown.
    """
    provider_id, _ = find_model_entry(model_tiers_registry, model_id or "")
    if provider_id:
        return provider_id
    if isinstance(model_id, str) and model_id.startswith(("zai-coding-plan/", "zai-coding/")):
        return "z-ai-coding"
    return None


def provider_reasoning_yaml(provider_id: str, reasoning_effort: str) -> str:
    """Render provider-specific Kilo/OpenCode reasoning options from one level.

    Kilo Code and OpenCode forward additional agent frontmatter options to the
    selected model provider. Providers expose incompatible request schemas, so the
    generated options preserve the provider's own documented parameter names rather
    than applying the OpenAI-only ``reasoningEffort`` field universally.

    Args:
        provider_id: Native model provider id.
        reasoning_effort: Requested normalized reasoning level.

    Returns:
        YAML frontmatter suffix, or an empty string for an unknown provider.
    """
    if provider_id == "openai":
        return f'\nreasoningEffort: "{clamp_reasoning_effort(reasoning_effort, REASONING_LEVEL_ORDER)}"'
    if provider_id == "anthropic":
        effort = clamp_reasoning_effort(reasoning_effort, ["low", "medium", "high", "xhigh", "max"])
        return f'\neffort: "{effort}"'
    if provider_id == "google":
        effort = clamp_reasoning_effort(reasoning_effort, ["minimal", "low", "medium", "high"])
        return f'\nthinkingConfig:\n  thinkingLevel: "{effort}"'
    if provider_id == "xai":
        effort = clamp_reasoning_effort(reasoning_effort, ["low", "medium", "high", "xhigh"])
        return f'\nreasoning_effort: "{effort}"'
    if provider_id in {"deepseek", "z-ai", "z-ai-coding"}:
        supported_levels = ["high", "max"] if provider_id == "deepseek" else REASONING_LEVEL_ORDER
        effort = clamp_reasoning_effort(reasoning_effort, supported_levels)
        return f'\nthinking:\n  type: "enabled"\nreasoning_effort: "{effort}"'
    if provider_id == "qwen":
        return "\nenable_thinking: true"
    if provider_id == "kimi":
        return '\nthinking:\n  type: "enabled"'
    if provider_id == "minimax":
        return '\nthinking:\n  type: "adaptive"'
    if provider_id == "mimo":
        return '\nthinking:\n  type: "enabled"'
    if provider_id == "openrouter":
        return f'\nreasoning:\n  effort: "{reasoning_effort}"'
    return ""


def agent_reasoning_suffix(
    cli_id: str,
    model: str | None,
    model_id: str | None,
    reasoning_effort: str | None,
    model_tiers_registry: dict[str, Any],
) -> str:
    """Build optional reasoning frontmatter appended after the model line.

    Emission is restricted to verified CLI/provider combinations:
      * kilo-code/opencode: ``variant`` plus provider-specific model options for
        every cataloged provider with documented reasoning or thinking controls.
      * claude-code: ``effort`` only when the native resolved provider is Anthropic.
    Codex and Amazon Kiro never emit per-agent reasoning here.

    Args:
        cli_id: Canonical CLI target id.
        model: Final rendered model id (may be ``None`` when disabled).
        model_id: Bare or provider-qualified model id used for catalog/provider lookup.
        reasoning_effort: Effective normalized reasoning level from the preset.
        model_tiers_registry: Loaded ``model-tiers`` registry.

    Returns:
        Frontmatter suffix starting with a newline when emitted, else an empty string.
    """
    if not model:
        return ""
    if cli_id in ("kilo-code", "opencode"):
        provider_id = native_reasoning_provider(model_tiers_registry, model_id)
        if not provider_id or not reasoning_effort:
            return ""
        provider_options = provider_reasoning_yaml(provider_id, reasoning_effort)
        if cli_id in ("kilo-code", "opencode"):
            return f'\nvariant: "{reasoning_effort}"{provider_options}'
        return provider_options
    if cli_id == "claude-code":
        provider_id = native_reasoning_provider(model_tiers_registry, model_id)
        if provider_id != "anthropic":
            return ""
        if not reasoning_effort:
            return ""
        return f'\neffort: "{reasoning_effort}"'
    return ""


def slugify(value: str) -> str:
    """Convert registry text to a conservative file-name slug.

    Args:
        value: Text value to normalize.

    Returns:
        Lowercase hyphenated slug.
    """
    normalized_value = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower())
    return normalized_value.strip("-")


def role_slug_parts(profile: dict[str, Any]) -> tuple[str, str | None]:
    """Return domain and role-name slug parts for generated agent ids.

    Args:
        profile: Registry profile entry.

    Returns:
        Pair of domain slug and optional role-name slug. Existing profile ids are
        used as the fallback so current generated names remain stable.
    """
    profile_id = slugify(str(profile.get("id") or "unknown"))
    explicit_domain = profile.get("domain")
    explicit_role_name = profile.get("role_name")
    if explicit_domain:
        domain_slug = slugify(str(explicit_domain))
        role_name_slug = slugify(str(explicit_role_name)) if explicit_role_name else profile_id
        return domain_slug, role_name_slug
    if "-" not in profile_id:
        return profile_id, None
    domain_slug, role_name_slug = profile_id.split("-", 1)
    return domain_slug, role_name_slug


def generated_agent_id(profile: dict[str, Any], level: str, role_levels_mode: str) -> str:
    """Build the generated agent id from domain, role name, and level.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling whether level suffixes are used.

    Returns:
        Agent id following ``<domain>-<role-name>-<level>`` in tiered mode, or a
        collapsed ``<domain>-<role-name>`` / ``<domain>`` id in single mode.
    """
    domain_slug, role_name_slug = role_slug_parts(profile)
    if role_levels_mode == "single":
        if role_name_slug:
            return f"{domain_slug}-{role_name_slug}"
        return domain_slug
    level_slug = slugify(level)
    if role_name_slug:
        return f"{domain_slug}-{role_name_slug}-{level_slug}"
    return f"{domain_slug}-{level_slug}"


def low_level_worker_placeholder_values(
    profiles: list[dict[str, Any]], role_levels_mode: str
) -> dict[str, str]:
    """Resolve canonical low-level worker placeholders to generated agent ids.

    Args:
        profiles: Canonical profile entries containing the worker profiles.
        role_levels_mode: Generation mode controlling worker id shape.

    Returns:
        Placeholder values for the canonical delegation guidance.

    Raises:
        ValueError: If a required worker profile is missing or has multiple levels.
    """
    profiles_by_id = {
        str(profile.get("id") or ""): profile
        for profile in profiles
        if isinstance(profile, dict)
    }
    values: dict[str, str] = {}
    for placeholder, worker_profile_id in LOW_LEVEL_WORKER_PROFILE_IDS.items():
        worker_profile = profiles_by_id.get(worker_profile_id)
        if worker_profile is None:
            raise ValueError(f"Missing required low-level worker profile '{worker_profile_id}'")
        worker_levels = profile_generation_levels(worker_profile, role_levels_mode)
        if len(worker_levels) != 1:
            raise ValueError(
                f"Low-level worker profile '{worker_profile_id}' must resolve to exactly one generated level"
            )
        values[placeholder] = generated_agent_id(
            worker_profile,
            worker_levels[0],
            role_levels_mode,
        )
    return values


def low_level_delegation_section(
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    low_level_delegation_instructions: list[str],
    profiles: list[dict[str, Any]],
) -> str:
    """Render delegation guidance only for eligible non-worker agents.

    Args:
        profile: Profile receiving the generated prompt.
        level: Effective seniority level for this generated agent.
        role_levels_mode: Generation mode controlling worker ids.
        low_level_delegation_instructions: Canonical delegation guidance.
        profiles: Canonical profiles used to resolve worker ids.

    Returns:
        Rendered Markdown section, or an empty string for junior and worker agents.
    """
    if level not in ABOVE_JUNIOR_LEVELS or profile.get("subagent_only") is True:
        return ""
    worker_values = low_level_worker_placeholder_values(profiles, role_levels_mode)
    rendered_instructions: list[str] = []
    for instruction in low_level_delegation_instructions:
        rendered_instruction = instruction
        for key, value in worker_values.items():
            rendered_instruction = rendered_instruction.replace(f"{{{{{key}}}}}", value)
        rendered_instructions.append(rendered_instruction)
    return markdown_section("Low-Level Delegation", rendered_instructions)


def selected_role_level(profile: dict[str, Any]) -> str:
    """Choose the internal level used when levels are collapsed.

    Args:
        profile: Registry profile entry.

    Returns:
        Preferred seniority level for single-mode generation.
    """
    levels = string_list(profile.get("seniority"))
    if "senior" in levels:
        return "senior"
    if "middle" in levels:
        return "middle"
    if levels:
        return levels[0]
    return "middle"


def profile_generation_levels(profile: dict[str, Any], role_levels_mode: str) -> list[str]:
    """Return the level list to generate for one profile.

    Args:
        profile: Registry profile entry.
        role_levels_mode: Generation mode controlling whether levels collapse.

    Returns:
        One or more seniority levels for the profile.
    """
    if role_levels_mode == "single":
        return [selected_role_level(profile)]
    return string_list(profile.get("seniority")) or ["middle"]


def role_display_title(level: str, title: str, role_levels_mode: str) -> str:
    """Build the role title shown in prompts and descriptions.

    Args:
        level: Seniority level.
        title: Role display title.
        role_levels_mode: Generation mode controlling whether the level is shown.

    Returns:
        Level-qualified title in tiered mode or the bare title in single mode.
    """
    if role_levels_mode == "single":
        return title
    if title.lower().startswith(f"{level.lower()} "):
        return title
    return f"{level} {title}"


def agent_description(title: str, level: str, role_levels_mode: str, purpose: str) -> str:
    """Build a concise CLI-facing agent description.

    Args:
        title: Role display title.
        level: Seniority level.
        role_levels_mode: Generation mode controlling whether the level is shown.
        purpose: Role mission or profile description.

    Returns:
        Human-readable agent description for CLI agent pickers.
    """
    return f"{role_display_title(level, title, role_levels_mode)}. {purpose}"


def normalized_reference_path(path: str) -> str:
    """Normalize a registry template path for generated prompts.

    Args:
        path: User-provided path to the runtime registry templates.

    Returns:
        The supplied path with surrounding whitespace and trailing slashes
        removed. Explicit absolute paths are preserved; the CLI default remains
        ``~/.ai-registry`` when no path is supplied.
    """
    normalized_path = path.strip().rstrip("/")
    if not normalized_path:
        raise ValueError("templates path must not be empty")
    return normalized_path


def role_prompt_values(
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    model: str | None,
    common_instructions: list[str],
    security_baseline: list[str],
    templates_path: str,
    low_level_delegation_section: str = "",
) -> dict[str, str]:
    """Build placeholder values for role prompt templates.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling agent ids.
        model: Resolved model id or ``None`` when model rendering is disabled.
        common_instructions: Shared profile instructions.
        security_baseline: Security and prompt-injection instructions shared by every generated agent.
        templates_path: Runtime registry template path used in generated references.
        low_level_delegation_section: Optional delegation guidance for eligible agents.

    Returns:
        Placeholder mapping for ``templates/roles`` prompt templates.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    responsibilities = bullet_list(string_list(role.get("responsibilities")))
    guardrails_section = markdown_section("You MUST follow these guardrails", string_list(role.get("guardrails")))
    security_baseline_section = markdown_section(
        "Always-On Security and Prompt-Injection Baseline",
        security_baseline,
    )
    delegation_level_rules_section = markdown_section(
        "Delegation Level Rules",
        string_list(role.get("delegation_level_rules")),
    )
    if profile_id == "orchestrator":
        if role_levels_mode == "single":
            delegation_examples = (
                "You MUST delegate each workflow stage to exact generated role-level agents, such as "
                "`backend-engineer` for implementation and `qa-engineer` for validation."
            )
        else:
            delegation_examples = (
                "You MUST delegate each workflow stage to exact generated role-level agents, such as "
                "`backend-engineer-middle` for implementation and `qa-engineer-senior` for validation."
            )
    else:
        delegation_examples = ""
    agent_id = generated_agent_id(profile, level, role_levels_mode)
    runtime_templates_path = normalized_reference_path(templates_path)
    level_prefix = (
        f"{level} "
        if role_levels_mode != "single" and not title.lower().startswith(f"{level.lower()} ")
        else ""
    )
    return {
        "agent_id": agent_id,
        "profile_id": profile_id,
        "level_prefix": level_prefix,
        "title": title,
        "responsibilities": responsibilities,
        "guardrails_section": guardrails_section,
        "security_baseline_section": security_baseline_section,
        "delegation_level_rules_section": delegation_level_rules_section,
        "low_level_delegation_section": low_level_delegation_section,
        "delegation_examples": delegation_examples,
        "common_instructions": bullet_list(common_instructions),
        "templates_path": runtime_templates_path,
    }


def render_role_prompt(
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    model: str | None,
    common_instructions: list[str],
    security_baseline: list[str],
    templates_path: str,
    single_mode_id_replacements: dict[str, str] | None,
    low_level_delegation_section: str = "",
) -> str:
    """Render the system prompt for one generated agent.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling agent ids.
        model: Resolved model id or ``None`` when model rendering is disabled.
        common_instructions: Shared profile instructions.
        security_baseline: Security and prompt-injection instructions shared by every generated agent.
        templates_path: Runtime registry template path used in generated references.
        single_mode_id_replacements: Tiered-to-single generated id replacements.
        low_level_delegation_section: Optional delegation guidance for eligible agents.

    Returns:
        Rendered system prompt.
    """
    profile_id = str(profile.get("id") or "unknown")
    prompt_template_name = "orchestrator-prompt-template.md" if profile_id == "orchestrator" else "role-prompt-template.md"
    prompt_template_path = AGENT_TEMPLATES_DIR / prompt_template_name
    values = role_prompt_values(
        profile,
        level,
        role_levels_mode,
        model,
        common_instructions,
        security_baseline,
        templates_path,
        low_level_delegation_section,
    )
    rendered_prompt = render_text(
        template_text(prompt_template_path),
        values,
        str(prompt_template_path),
    )
    if role_levels_mode == "single" and single_mode_id_replacements:
        for tiered_agent_id, single_agent_id in sorted(
            single_mode_id_replacements.items(), key=lambda item: len(item[0]), reverse=True
        ):
            rendered_prompt = rendered_prompt.replace(tiered_agent_id, single_agent_id)
    return rendered_prompt


def worker_cli_control_values(cli_id: str, profile: dict[str, Any]) -> dict[str, str]:
    """Return supported CLI controls for a canonical subagent-only worker.

    Args:
        cli_id: Canonical CLI target id.
        profile: Profile being rendered.

    Returns:
        Placeholder values for CLI-specific worker controls. Unsupported
        controls remain absent from the corresponding template.
    """
    is_worker = profile.get("subagent_only") is True
    values = {
        "agent_hidden_yaml": "true" if is_worker else "false",
        "worker_tools_yaml": "",
        "worker_permissions_yaml": "",
        "agent_tools_json": json.dumps(["read"] if is_worker and cli_id == "amazon-kiro" else ["*"]),
    }
    if not is_worker:
        return values
    if cli_id == "claude-code":
        values["worker_tools_yaml"] = "\ntools:\n  - Read"
    elif cli_id in {"kilo-code", "opencode"}:
        values["worker_permissions_yaml"] = (
            "\npermission:\n"
            "  read: allow\n"
            "  edit: deny\n"
            "  bash: deny\n"
            "  glob: allow\n"
            "  grep: allow\n"
            "  webfetch: deny\n"
            "  websearch: deny\n"
            "  task: deny"
        )
    return values


def render_cli_agent(
    cli_id: str,
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    model: str | None,
    prompt: str,
    model_disabled: bool,
    reasoning_yaml: str = "",
) -> tuple[str, str]:
    """Render one CLI-specific agent config.

    Args:
        cli_id: Canonical CLI target id.
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling agent ids.
        model: Resolved model id or ``None`` when model rendering is disabled.
        prompt: Rendered system prompt.
        model_disabled: Whether the template should omit model fields.
        reasoning_yaml: Optional reasoning frontmatter suffix appended after the
            model line (e.g. reasoningEffort or effort) for CLIs that support it;
            empty when not applicable.

    Returns:
        Pair of generated agent id and rendered file content.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    generated_agent_id_value = generated_agent_id(profile, level, role_levels_mode)
    template_kind = "orchestrator-agent-template" if profile_id == "orchestrator" else "role-agent-template"
    template_dir = CLI_TARGETS[cli_id]["template_dir"]
    extension = CLI_TARGETS[cli_id]["extension"]
    cli_template_path = AGENT_TEMPLATES_DIR / template_dir / f"{template_kind}{extension}"
    generated_description = agent_description(title, level, role_levels_mode, purpose)
    worker_controls = worker_cli_control_values(cli_id, profile)
    values = {
        "agent_id_json": quoted_string(generated_agent_id_value),
        "agent_id_toml": quoted_string(generated_agent_id_value),
        "agent_id_yaml": quoted_string(generated_agent_id_value),
        "agent_description_json": quoted_string(generated_description),
        "agent_description_toml": quoted_string(generated_description),
        "agent_description_yaml": quoted_string(generated_description),
        "model_json": quoted_string(model or MODEL_REMOVAL_TOKEN),
        "model_toml": quoted_string(model or MODEL_REMOVAL_TOKEN),
        "model_yaml": quoted_string(model or MODEL_REMOVAL_TOKEN),
        "reasoning_yaml": reasoning_yaml,
        "agent_hidden_yaml": worker_controls["agent_hidden_yaml"],
        "worker_tools_yaml": worker_controls["worker_tools_yaml"],
        "worker_permissions_yaml": worker_controls["worker_permissions_yaml"],
        "agent_tools_json": worker_controls["agent_tools_json"],
        "prompt": prompt,
        "prompt_json": quoted_string(prompt),
        "prompt_toml": quoted_string(prompt),
    }
    rendered = render_text(template_text(cli_template_path), values, str(cli_template_path))
    if model_disabled:
        rendered = remove_model_field(rendered, extension)
    return generated_agent_id_value, rendered


def orchestrator_primary_entry(
    entries: list[tuple[dict[str, Any], str]],
    role_levels_mode: str,
) -> tuple[dict[str, Any], str]:
    """Return the orchestrator senior entry used as the primary agent.

    Args:
        entries: Profile and seniority pairs being generated.
        role_levels_mode: Generation mode controlling agent ids.

    Returns:
        The orchestrator profile pair using the selected generation mode.

    Raises:
        ValueError: If the orchestrator entry does not exist.
    """
    for profile, level in entries:
        if str(profile.get("id") or "") != "orchestrator":
            continue
        if role_levels_mode == "tiered" and level != "senior":
            continue
        if role_levels_mode == "single" or level == "senior":
            return profile, level
    raise ValueError("Missing orchestrator profile required for primary CLI config generation")


def codex_config_text(
    entries: list[tuple[dict[str, Any], str]],
    primary_model: str | None,
    primary_reasoning_effort: str | None,
    model_disabled: bool,
    role_levels_mode: str,
) -> str:
    """Render the Codex primary config.

    Args:
        entries: Profile and seniority pairs being generated.
        primary_model: Resolved orchestrator model id when available.
        primary_reasoning_effort: Effective reasoning effort for the orchestrator when
            its primary model is a direct OpenAI model, otherwise ``None``. Effort is a
            global/profile setting only; it is never written into per-role ``.toml`` files.
        model_disabled: Whether model fields were disabled by the preset.
        role_levels_mode: Generation mode controlling agent ids.

    Returns:
        Rendered Codex config content.
    """
    primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
    primary_agent_id = generated_agent_id(primary_profile, primary_level, role_levels_mode)
    ordered_entries = [
        (primary_profile, primary_level),
        *[
            (profile, level)
            for profile, level in entries
            if generated_agent_id(profile, level, role_levels_mode) != primary_agent_id
        ],
    ]
    lines = [TOML_GENERATOR_MARKER]
    lines.append(f"default_agent = {quoted_string(primary_agent_id)}")
    if primary_model and not model_disabled:
        lines.append(f"model = {quoted_string(primary_model)}")
    if primary_reasoning_effort and not model_disabled:
        lines.append(f"model_reasoning_effort = {quoted_string(primary_reasoning_effort)}")
    lines.append("")
    for profile, level in ordered_entries:
        agent_id = generated_agent_id(profile, level, role_levels_mode)
        lines.append(f"[agents.{agent_id}]")
        lines.append(f"config_file = {quoted_string(f'./roles/{agent_id}.toml')}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def default_agent_json_text(agent_name: str) -> str:
    """Render a minimal JSON object that selects the primary agent.

    Args:
        agent_name: Primary agent name to activate.

    Returns:
        JSON object text with a single default-agent setting.
    """
    return (
        "{\n"
        + f"  \"$comment\": {quoted_string(f'generated-by: {GENERATOR_MARKER_VALUE}')},\n"
        + f"  \"default_agent\": {quoted_string(agent_name)}\n"
        + "}\n"
    )


def kilo_default_config_text(agent_name: str) -> str:
    """Render the Kilo Code primary config.

    Args:
        agent_name: Primary agent name to activate.
    Returns:
        JSONC content selecting the default agent.
    """
    lines = [JSONC_GENERATOR_MARKER]
    lines.append("{")
    lines.append(f"  \"default_agent\": {quoted_string(agent_name)}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def has_generated_marker(path: Path) -> bool:
    """Return whether a file has an anchored, format-valid ownership marker.

    Args:
        path: File to inspect.

    Returns:
        ``True`` only when the format-specific marker exactly identifies this
        generator without relying on a substring match.
    """
    if not path.is_file():
        return False
    content = path.read_text(encoding="utf-8")
    if path.suffix == ".toml":
        return content.startswith(TOML_GENERATOR_MARKER + "\n")
    if path.suffix == ".jsonc":
        return content.startswith(JSONC_GENERATOR_MARKER + "\n")
    if path.suffix == ".json":
        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError:
            return False
        return isinstance(parsed_content, dict) and parsed_content.get("$comment") == (
            f"generated-by: {GENERATOR_MARKER_VALUE}"
        )
    if path.suffix == ".md":
        if content.startswith(MARKDOWN_GENERATOR_MARKER + "\n"):
            return True
        front_matter_match = re.match(r"\A---\ngenerated_by: ([^\n]+)\n", content)
        return front_matter_match is not None and front_matter_match.group(1) == quoted_string(GENERATOR_MARKER_VALUE)
    return False


def is_known_managed_output_directory(output_directory: Path, cli_id: str) -> bool:
    """Return whether an output path is the repository's tracked CLI output.

    Args:
        output_directory: Output directory being evaluated.
        cli_id: Canonical CLI target id.

    Returns:
        ``True`` only for the repository-managed output path of the CLI target.
    """
    return output_directory.resolve() == (ROOT / "configs" / cli_id).resolve()


def has_legacy_role_catalog_signature(output_directory: Path, cli_id: str) -> bool:
    """Verify the exact legacy catalog signature at a managed output path.

    Args:
        output_directory: Output directory being evaluated.
        cli_id: Canonical CLI target id.

    Returns:
        ``True`` when the legacy catalog header and explanatory line match.
    """
    if not is_known_managed_output_directory(output_directory, cli_id):
        return False
    catalog_path = output_directory / CLI_TARGETS[cli_id]["role_catalog_path"]
    if not catalog_path.is_file():
        return False
    catalog_lines = catalog_path.read_text(encoding="utf-8").splitlines()
    return len(catalog_lines) >= 3 and catalog_lines[0] == "# Available Generated Roles" and catalog_lines[2] == (
        "Use the CLI native available agent list by default. Use this catalog only as a fallback when the CLI "
        "cannot expose available agents or when exact generated role ids are needed."
    )


def has_legacy_primary_signature(
    path: Path,
    output_directory: Path,
    cli_id: str,
    primary_agent_id: str,
    require_legacy_catalog: bool = True,
) -> bool:
    """Verify a legacy primary or override artifact without broad marker matching.

    Args:
        path: Candidate primary or override artifact.
        output_directory: Output directory being evaluated.
        cli_id: Canonical CLI target id.
        primary_agent_id: Expected generated default agent id.
        require_legacy_catalog: Whether the legacy catalog must still be present.

    Returns:
        ``True`` only when the known managed path and CLI-specific legacy
        signature both match.
    """
    primary_file_names = {
        "codex": {"config.toml", "config.override.toml"},
        "opencode": {"opencode.json", "opencode.override.json"},
        "kilo-code": {"kilo.jsonc", "kilo.override.jsonc"},
    }
    expected_primary_paths = {output_directory / file_name for file_name in primary_file_names.get(cli_id, set())}
    if (
        not is_known_managed_output_directory(output_directory, cli_id)
        or path not in expected_primary_paths
        or not path.is_file()
        or (require_legacy_catalog and not has_legacy_role_catalog_signature(output_directory, cli_id))
    ):
        return False
    content = path.read_text(encoding="utf-8")
    if cli_id == "codex":
        return content.startswith("# Generated by scripts/generate-agent-configs.py.\n") and (
            f'default_agent = "{primary_agent_id}"' in content
        ) and f"[agents.{primary_agent_id}]" in content
    if cli_id == "kilo-code":
        return content.startswith("// Generated by scripts/generate-agent-configs.py.\n") and (
            f'"default_agent": "{primary_agent_id}"' in content
        )
    if cli_id == "opencode":
        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError:
            return False
        return parsed_content == {"default_agent": primary_agent_id}
    return False


def has_legacy_role_signature(
    path: Path,
    output_directory: Path,
    cli_id: str,
    agent_id: str,
    require_legacy_catalog: bool = True,
    expected_agent_ids: frozenset[str] = frozenset(),
) -> bool:
    """Verify a legacy generated role artifact at an expected managed path.

    Args:
        path: Candidate role artifact.
        output_directory: Output directory being evaluated.
        cli_id: Canonical CLI target id.
        agent_id: Expected generated agent id from the role file name.
        require_legacy_catalog: Whether the legacy catalog must still be present.
        expected_agent_ids: Current managed agent IDs eligible for a one-time
            migration when the catalog already has a current marker.

    Returns:
        ``True`` only for a known managed legacy role signature.
    """
    if (
        not is_known_managed_output_directory(output_directory, cli_id)
        or not path.is_file()
        or (require_legacy_catalog and not has_legacy_role_catalog_signature(output_directory, cli_id))
        or (
            not require_legacy_catalog
            and agent_id not in HISTORICAL_MANAGED_LEGACY_AGENT_IDS.get(cli_id, frozenset())
            and agent_id not in expected_agent_ids
        )
    ):
        return False
    expected_path = output_directory / CLI_TARGETS[cli_id]["agent_directory"] / f"{agent_id}{CLI_TARGETS[cli_id]['extension']}"
    if path != expected_path:
        return False
    content = path.read_text(encoding="utf-8")
    legacy_runtime_reference_sets = (
        (f"Read `{ROOT}/security/rules.md", f"read `{ROOT}/skills/skills.md"),
        ("Read `~/.ai-registry/security/rules.md", "read `~/.ai-registry/skills/skills.md"),
    )
    if cli_id == "codex":
        legacy_footer_prefix = "# Generated from registry/profiles.yaml by scripts/generate-agent-configs.py.\n"
        legacy_role_footer = legacy_footer_prefix + (
            "# Reference this file from config.toml [agents.<name>].config_file when needed.\n"
        )
        legacy_orchestrator_footer = legacy_footer_prefix + (
            "# This orchestrator role is intended to be user-facing and to delegate to exact role-level agents.\n"
        )
        expected_footer = legacy_orchestrator_footer if agent_id.startswith("orchestrator") else legacy_role_footer
        return (
            content.startswith(f'name = "{agent_id}"\n')
            and any(all(reference in content for reference in references) for references in legacy_runtime_reference_sets)
            and content.endswith(expected_footer)
        )
    if cli_id == "amazon-kiro":
        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError:
            return False
        return (
            parsed_content.get("name") == agent_id
            and isinstance(parsed_content.get("description"), str)
            and isinstance(parsed_content.get("prompt"), str)
            and any(
                all(reference in parsed_content["prompt"] for reference in references)
                for references in legacy_runtime_reference_sets
            )
            and parsed_content.get("tools") == ["*"]
        )
    return (
        content.startswith("---\n")
        and any(all(reference in content for reference in references) for references in legacy_runtime_reference_sets)
        and "\nhidden: false\n---\n\n# You are " in content
    )


def has_legacy_steering_signature(
    path: Path, output_directory: Path, require_legacy_catalog: bool = True
) -> bool:
    """Verify the legacy Amazon Kiro steering artifact at its managed path.

    Args:
        path: Candidate steering artifact.
        output_directory: Output directory being evaluated.
        require_legacy_catalog: Whether the legacy catalog must still be present.

    Returns:
        ``True`` only for the known legacy steering header and prompt signature.
    """
    expected_path = output_directory / "steering" / "orchestrator.md"
    return (
        is_known_managed_output_directory(output_directory, "amazon-kiro")
        and path == expected_path
        and path.is_file()
        and (not require_legacy_catalog or has_legacy_role_catalog_signature(output_directory, "amazon-kiro"))
        and path.read_text(encoding="utf-8").startswith(
            f"---\ninclusion: auto\n---\n\n# You are the Orchestrator\n\n"
        )
        and f"read {ROOT}/capability-routing.md" in path.read_text(encoding="utf-8")
    )


def has_legacy_note_signature(
    path: Path, output_directory: Path, cli_id: str, require_legacy_catalog: bool = True
) -> bool:
    """Verify a legacy manual-merge note at its sole managed output path.

    Args:
        path: Candidate note path.
        output_directory: Output directory being evaluated.
        cli_id: Canonical CLI target id.
        require_legacy_catalog: Whether the legacy catalog must still be present.

    Returns:
        ``True`` only for the expected legacy generated note format.
    """
    note_names = {"claude-code": "settings.override.md", "amazon-kiro": "agent.override.md"}
    expected_name = note_names.get(cli_id)
    if (
        not expected_name
        or not is_known_managed_output_directory(output_directory, cli_id)
        or (require_legacy_catalog and not has_legacy_role_catalog_signature(output_directory, cli_id))
    ):
        return False
    return path == output_directory / expected_name and path.is_file() and path.read_text(encoding="utf-8").startswith(
        "# Generated by scripts/generate-agent-configs.py.\n# Manual merge required:"
    )


def generate_primary_role_artifact(
    cli_id: str,
    output_directory: Path,
    entries: list[tuple[dict[str, Any], str]],
    primary_model: str | None,
    primary_reasoning_effort: str | None,
    model_disabled: bool,
    role_levels_mode: str,
    orchestrator_prompt: str | None = None,
    legacy_primary_eligible: bool | None = None,
    legacy_override_eligible: bool | None = None,
    legacy_steering_eligible: bool | None = None,
) -> int:
    """Write the primary config for managed output or an override for user output.

    Args:
        cli_id: Canonical CLI target id.
        output_directory: Directory where generated files are written.
        entries: Profile and seniority pairs being generated.
        primary_model: Resolved orchestrator model id when available.
        primary_reasoning_effort: Effective reasoning effort for the orchestrator when
            its primary model is a direct OpenAI model (Codex only); otherwise ``None``.
        model_disabled: Whether model fields were disabled by the preset.
        role_levels_mode: Generation mode controlling agent ids.
        orchestrator_prompt: Rendered orchestrator prompt body for Amazon Kiro steering.
        legacy_primary_eligible: Prevalidated legacy ownership of the primary
            config, or ``None`` to validate immediately.
        legacy_override_eligible: Prevalidated legacy ownership of the override
            config, or ``None`` to validate immediately.
        legacy_steering_eligible: Prevalidated legacy ownership of Amazon Kiro
            steering, or ``None`` to validate immediately.

    Returns:
        Number of generated primary-role artifacts.
    """
    primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
    primary_agent_id = generated_agent_id(primary_profile, primary_level, role_levels_mode)
    if cli_id == "codex":
        main_config_path = output_directory / "config.toml"
        override_path = output_directory / "config.override.toml"
        if legacy_primary_eligible is None:
            legacy_primary_eligible = has_legacy_primary_signature(
                main_config_path, output_directory, cli_id, primary_agent_id
            )
        if legacy_override_eligible is None:
            legacy_override_eligible = has_legacy_primary_signature(
                override_path, output_directory, cli_id, primary_agent_id
            )
        if not main_config_path.exists() or has_generated_marker(main_config_path) or legacy_primary_eligible:
            target_path = main_config_path
        elif not override_path.exists() or has_generated_marker(override_path) or legacy_override_eligible:
            target_path = override_path
        else:
            return 0
        if target_path == main_config_path and (
            has_generated_marker(override_path)
            or legacy_override_eligible
        ):
            override_path.unlink()
        write_text(
            target_path,
            codex_config_text(
                entries,
                primary_model,
                primary_reasoning_effort,
                model_disabled,
                role_levels_mode,
            ),
        )
        return 1
    if cli_id == "opencode":
        main_config_path = output_directory / "opencode.json"
        override_path = output_directory / "opencode.override.json"
        if legacy_primary_eligible is None:
            legacy_primary_eligible = has_legacy_primary_signature(
                main_config_path, output_directory, cli_id, primary_agent_id
            )
        if legacy_override_eligible is None:
            legacy_override_eligible = has_legacy_primary_signature(
                override_path, output_directory, cli_id, primary_agent_id
            )
        if not main_config_path.exists() or has_generated_marker(main_config_path) or legacy_primary_eligible:
            target_path = main_config_path
        elif not override_path.exists() or has_generated_marker(override_path) or legacy_override_eligible:
            target_path = override_path
        else:
            return 0
        if target_path == main_config_path and (
            has_generated_marker(override_path)
            or legacy_override_eligible
        ):
            override_path.unlink()
        write_text(target_path, default_agent_json_text(primary_agent_id))
        return 1
    if cli_id == "kilo-code":
        main_config_path = output_directory / "kilo.jsonc"
        override_path = output_directory / "kilo.override.jsonc"
        if legacy_primary_eligible is None:
            legacy_primary_eligible = has_legacy_primary_signature(
                main_config_path, output_directory, cli_id, primary_agent_id
            )
        if legacy_override_eligible is None:
            legacy_override_eligible = has_legacy_primary_signature(
                override_path, output_directory, cli_id, primary_agent_id
            )
        if not main_config_path.exists() or has_generated_marker(main_config_path) or legacy_primary_eligible:
            target_path = main_config_path
        elif not override_path.exists() or has_generated_marker(override_path) or legacy_override_eligible:
            target_path = override_path
        else:
            return 0
        if target_path == main_config_path and (
            has_generated_marker(override_path)
            or legacy_override_eligible
        ):
            override_path.unlink()
        write_text(target_path, kilo_default_config_text(primary_agent_id))
        return 1
    if cli_id == "claude-code":
        return 0
    if cli_id == "amazon-kiro":
        # Write steering/orchestrator.md with inclusion: auto frontmatter
        if orchestrator_prompt is not None:
            steering_dir = output_directory / "steering"
            steering_dir.mkdir(parents=True, exist_ok=True)
            steering_path = steering_dir / "orchestrator.md"
            steering_content = f"---\ngenerated_by: {quoted_string(GENERATOR_MARKER_VALUE)}\ninclusion: auto\n---\n\n" + orchestrator_prompt
            if legacy_steering_eligible is None:
                legacy_steering_eligible = has_legacy_steering_signature(steering_path, output_directory)
            if not steering_path.exists() or has_generated_marker(steering_path) or legacy_steering_eligible:
                write_text(steering_path, steering_content)
                return 1
        return 0
    raise ValueError(f"Unsupported CLI '{cli_id}'")


def generated_agent_entries(
    profiles: list[dict[str, Any]],
    role_levels_mode: str,
) -> list[tuple[dict[str, Any], str]]:
    """Return every profile and seniority pair to generate.

    Args:
        profiles: Registry profile entries.
        role_levels_mode: Generation mode controlling whether levels collapse.

    Returns:
        Pairs of profile mapping and seniority level.
    """
    entries: list[tuple[dict[str, Any], str]] = []
    for profile in sorted(profiles, key=lambda item: str(item.get("id") or "")):
        if not isinstance(profile, dict):
            raise ValueError("Every profile entry must be a mapping")
        for level in profile_generation_levels(profile, role_levels_mode):
            entries.append((profile, level))
    return entries


def single_mode_agent_id_replacements(profiles: list[dict[str, Any]]) -> dict[str, str]:
    """Build prompt replacements that remove tiered role ids in single mode.

    Args:
        profiles: Registry profile entries.

    Returns:
        Mapping from tiered generated ids to their collapsed single-mode ids.
    """
    replacements: dict[str, str] = {}
    for profile in profiles:
        if not isinstance(profile, dict):
            raise ValueError("Every profile entry must be a mapping")
        single_mode_agent_id = generated_agent_id(profile, selected_role_level(profile), "single")
        for level in profile_generation_levels(profile, "tiered"):
            tiered_agent_id = generated_agent_id(profile, level, "tiered")
            replacements[tiered_agent_id] = single_mode_agent_id
    return replacements


def role_catalog_line(profile: dict[str, Any], levels: list[str], role_levels_mode: str) -> str:
    """Render one concise generated role catalog line.

    Args:
        profile: Registry profile entry.
        levels: Seniority levels available for the profile.
        role_levels_mode: Generation mode controlling agent ids.

    Returns:
        Markdown bullet with role ids, description, tags, and usage hint.
    """
    role = profile_role(profile)
    title = str(role.get("title") or profile.get("name") or profile.get("id") or "unknown")
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    profile_description = str(profile.get("description") or purpose)
    categories = string_list(profile.get("include", {}).get("categories"))
    tags = ", ".join(f"`{category}`" for category in categories) if categories else "none"
    generated_ids = ", ".join(f"`{generated_agent_id(profile, level, role_levels_mode)}`" for level in levels)
    return (
        f"- {generated_ids}: {title}. "
        f"{purpose} Tags: {tags}. Choose when: {profile_description}"
    )


def generated_role_catalog(entries: list[tuple[dict[str, Any], str]], role_levels_mode: str) -> str:
    """Render the generated role catalog.

    Args:
        entries: Profile and level pairs being generated.
        role_levels_mode: Generation mode controlling agent ids.

    Returns:
        Markdown catalog content.
    """
    lines = [
        MARKDOWN_GENERATOR_MARKER,
        "# Available Generated Roles",
        "",
        "Use the CLI native available agent list by default. Use this catalog only as a fallback when the CLI cannot expose available agents or when exact generated role ids are needed.",
        "",
    ]
    grouped_profiles: dict[str, tuple[dict[str, Any], list[str]]] = {}
    for profile, level in entries:
        profile_id = str(profile.get("id") or "unknown")
        if profile_id not in grouped_profiles:
            grouped_profiles[profile_id] = (profile, [])
        grouped_profiles[profile_id][1].append(level)
    lines.extend(role_catalog_line(profile, levels, role_levels_mode) for profile, levels in grouped_profiles.values())
    return "\n".join(lines)


def cleanup_previous_generated_files(
    output_directory: Path,
    cli_id: str,
    profiles: list[dict[str, Any]],
    verified_legacy_role_paths: set[Path] | None = None,
) -> None:
    """Remove previously generated files for the current CLI target.

    This removes files matching generated agent ids in the current flat output
    directory and in the current CLI agent directory. It also removes stale files
    from the alternate role-level mode so switching between tiered and single
    generation does not leave behind orphaned generated files. It avoids deleting
    unrelated user files from the output tree.

    Args:
        output_directory: Root output directory selected by the user.
        cli_id: Canonical CLI target id.
        profiles: Registry profile entries being regenerated.
    """
    extension = CLI_TARGETS[cli_id]["extension"]
    agent_directories = [output_directory / CLI_TARGETS[cli_id]["agent_directory"]]
    agent_directories.extend(output_directory / legacy_path for legacy_path in LEGACY_AGENT_DIRECTORIES.get(cli_id, []))
    for profile in profiles:
        all_generated_ids = {
            generated_agent_id(profile, level, "tiered") for level in profile_generation_levels(profile, "tiered")
        }
        all_generated_ids.add(generated_agent_id(profile, selected_role_level(profile), "single"))
        for generated_id in all_generated_ids:
            file_name = f"{generated_id}{extension}"
            generated_paths = [output_directory / file_name]
            generated_paths.extend(agent_directory / file_name for agent_directory in agent_directories)
            for generated_path in generated_paths:
                if (
                    has_generated_marker(generated_path)
                    or (verified_legacy_role_paths is not None and generated_path in verified_legacy_role_paths)
                    or has_legacy_role_signature(
                    generated_path, output_directory, cli_id, generated_id
                    )
                ):
                    generated_path.unlink()

    for legacy_path in LEGACY_AGENT_DIRECTORIES.get(cli_id, []):
        legacy_directory = output_directory / legacy_path
        while legacy_directory != output_directory and legacy_directory.exists():
            try:
                legacy_directory.rmdir()
            except OSError:
                break
            legacy_directory = legacy_directory.parent

    for stale_note_path in {
        "claude-code": [output_directory / "settings.override.md"],
        "amazon-kiro": [output_directory / "agent.override.md"],
    }.get(cli_id, []):
        if has_generated_marker(stale_note_path) or has_legacy_note_signature(
            stale_note_path, output_directory, cli_id
        ):
            stale_note_path.unlink()


def generate_agent_configs(
    cli_id: str,
    output_directory: Path,
    preset: str | None,
    templates_path: str,
    model_prefix: str,
    role_levels_mode: str,
    role_preset_specs: list[str] | None,
) -> int:
    """Generate all role-level agent configs for a CLI target.

    Args:
        cli_id: Canonical CLI target id.
        output_directory: Directory where generated files are written.
        preset: Model preset key from recommended defaults, or ``""``/``none`` to omit models.
        templates_path: Runtime registry template path used in generated references.
        model_prefix: Outer provider prefix for generated model ids.
        role_levels_mode: ``tiered`` for current behavior or ``single`` for collapsed roles.
        role_preset_specs: Optional repeatable ``roles=preset`` specs that override the model
            preset for matching roles; ignored when model lookup is disabled.

    Returns:
        Number of generated files.

    Raises:
        ValueError: If registry data or preset resolution is invalid.
    """
    profiles_registry = load_registry("profiles")
    selected_preset = (preset or "").strip()
    model_disabled = preset_modeling_disabled(selected_preset)
    if role_levels_mode == "single" and not model_disabled:
        raise ValueError("--role-levels single requires --preset none or --preset \"\" so model fields are disabled")
    profiles = profiles_registry.get("profiles", [])
    if not isinstance(profiles, list):
        raise ValueError("registry/profiles.yaml must contain a profiles list")
    role_preset_overrides: dict[str, str] = {}
    model_tiers_registry: dict[str, Any] = {}
    recommended_defaults: dict[str, Any] = {}
    if not model_disabled:
        model_tiers_registry = load_registry("model-tiers")
        recommended_defaults = model_tiers_registry.get("recommended_defaults", {})
        if not isinstance(recommended_defaults, dict):
            raise ValueError("registry/model-tiers.yaml must contain recommended_defaults")
        if selected_preset not in available_presets(recommended_defaults):
            presets = ", ".join(available_presets(recommended_defaults))
            raise ValueError(f"Unknown preset '{selected_preset}'. Available presets: {presets}")
        if role_preset_specs:
            role_preset_overrides = resolve_role_preset_overrides(role_preset_specs, profiles)
            available_preset_names = available_presets(recommended_defaults)
            for override_profile_id, override_preset in role_preset_overrides.items():
                if override_preset not in available_preset_names:
                    presets = ", ".join(available_preset_names)
                    raise ValueError(
                        f"Unknown preset '{override_preset}' for role '{override_profile_id}'. "
                        f"Available presets: {presets}"
                    )
    elif role_preset_specs:
        print(
            "WARNING --role-preset overrides ignored because --preset disables model fields.",
            file=sys.stderr,
        )

    common_instructions = string_list(profiles_registry.get("common_instructions"))
    security_baseline = security_baseline_from_policy(profiles_registry)
    low_level_delegation_instructions = string_list(
        profiles_registry.get("low_level_delegation_instructions")
    )
    extension = CLI_TARGETS[cli_id]["extension"]
    agent_directory = output_directory / CLI_TARGETS[cli_id]["agent_directory"]
    entries = generated_agent_entries(profiles, role_levels_mode)
    single_mode_id_replacements = single_mode_agent_id_replacements(profiles) if role_levels_mode == "single" else None
    expected_agent_ids = frozenset(
        generated_agent_id(profile, level, role_levels_mode) for profile, level in entries
    )
    verified_legacy_role_paths = {
        output_directory / CLI_TARGETS[cli_id]["agent_directory"] / f"{agent_id}{extension}"
        for agent_id in expected_agent_ids
        if has_legacy_role_signature(
            output_directory / CLI_TARGETS[cli_id]["agent_directory"] / f"{agent_id}{extension}",
            output_directory,
            cli_id,
            agent_id,
            require_legacy_catalog=False,
            expected_agent_ids=expected_agent_ids,
        )
    }
    legacy_primary_eligible = False
    legacy_override_eligible = False
    legacy_steering_eligible = False
    if cli_id in {"codex", "opencode", "kilo-code"}:
        primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
        primary_agent_id = generated_agent_id(primary_profile, primary_level, role_levels_mode)
        primary_file_names = {
            "codex": ("config.toml", "config.override.toml"),
            "opencode": ("opencode.json", "opencode.override.json"),
            "kilo-code": ("kilo.jsonc", "kilo.override.jsonc"),
        }
        primary_file_name, override_file_name = primary_file_names[cli_id]
        legacy_primary_eligible = has_legacy_primary_signature(
            output_directory / primary_file_name, output_directory, cli_id, primary_agent_id
        )
        legacy_override_eligible = has_legacy_primary_signature(
            output_directory / override_file_name, output_directory, cli_id, primary_agent_id
        )
    elif cli_id == "amazon-kiro":
        legacy_steering_eligible = has_legacy_steering_signature(
            output_directory / "steering" / "orchestrator.md", output_directory
        )
    cleanup_previous_generated_files(output_directory, cli_id, profiles, verified_legacy_role_paths)
    role_catalog_path = output_directory / CLI_TARGETS[cli_id]["role_catalog_path"]
    if not role_catalog_path.exists() or has_generated_marker(role_catalog_path) or has_legacy_role_catalog_signature(
        output_directory, cli_id
    ):
        write_text(role_catalog_path, generated_role_catalog(entries, role_levels_mode))
    generated_count = 0
    orchestrator_prompt: str | None = None
    for profile, level in entries:
        profile_id = str(profile.get("id") or "unknown")
        effective_preset = role_preset_overrides.get(profile_id, selected_preset)
        effective_model_disabled = preset_modeling_disabled(effective_preset)
        model: str | None = None
        bare_model_id: str | None = None
        reasoning_effort: str | None = None
        if not effective_model_disabled:
            preset_configuration = preset_configuration_for_level(
                recommended_defaults, level, effective_preset, profile_id
            )
            bare_model_id = str(preset_configuration["model"])
            reasoning_effort = resolve_effective_reasoning(preset_configuration)
            model = rendered_model_id(
                model_tiers_registry,
                bare_model_id,
                model_prefix,
                profile_id,
                cli_id in DEFAULT_MODEL_PREFIXES,
            )
        prompt = render_role_prompt(
            profile,
            level,
            role_levels_mode,
            model,
            common_instructions,
            security_baseline,
            templates_path,
            single_mode_id_replacements,
            low_level_delegation_section(
                profile,
                level,
                role_levels_mode,
                low_level_delegation_instructions,
                profiles,
            ),
        )
        # Capture orchestrator prompt for Amazon Kiro steering artifact
        if profile_id == "orchestrator" and cli_id == "amazon-kiro":
            orchestrator_prompt = prompt
        reasoning_yaml = agent_reasoning_suffix(cli_id, model, bare_model_id, reasoning_effort, model_tiers_registry)
        generated_agent_id_value, rendered_agent = render_cli_agent(
            cli_id,
            profile,
            level,
            role_levels_mode,
            model,
            prompt,
            effective_model_disabled,
            reasoning_yaml,
        )
        agent_path = agent_directory / f"{generated_agent_id_value}{extension}"
        if not agent_path.exists() or has_generated_marker(agent_path) or has_legacy_role_signature(
            agent_path, output_directory, cli_id, generated_agent_id_value
        ):
            write_text(agent_path, rendered_agent)
            generated_count += 1
    primary_model = None
    primary_reasoning_effort: str | None = None
    if not model_disabled:
        primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
        primary_profile_id = str(primary_profile.get("id") or "unknown")
        primary_preset = role_preset_overrides.get(primary_profile_id, selected_preset)
        primary_preset_configuration = preset_configuration_for_level(
            recommended_defaults, primary_level, primary_preset, primary_profile_id
        )
        primary_bare_model_id = str(primary_preset_configuration["model"])
        primary_model = rendered_model_id(
            model_tiers_registry,
            primary_bare_model_id,
            model_prefix,
            primary_profile_id,
            cli_id in DEFAULT_MODEL_PREFIXES,
        )
        # Codex exposes reasoning as a global/profile setting only. Emit it for the
        # primary config when the primary model is a direct OpenAI model (native openai
        # provider, no gateway outer prefix) and an effective effort is available.
        primary_provider, _ = find_model_entry(model_tiers_registry, primary_bare_model_id)
        if primary_provider == "openai" and not model_prefix:
            primary_reasoning_effort = resolve_effective_reasoning(primary_preset_configuration)
    generated_count += generate_primary_role_artifact(
        cli_id,
        output_directory,
        entries,
        primary_model,
        primary_reasoning_effort,
        model_disabled,
        role_levels_mode,
        orchestrator_prompt,
        legacy_primary_eligible,
        legacy_override_eligible,
        legacy_steering_eligible,
    )
    return generated_count


def verify_managed_output_drift() -> list[str]:
    """Compare every managed CLI artifact against a freshly generated manifest.

    Returns:
        Deterministic validation errors for missing, unmarked, non-portable, or
        byte-drifted managed artifacts.
    """
    validation_errors: list[str] = []
    for cli_id, options in MANAGED_CLI_GENERATION_OPTIONS.items():
        managed_output_directory = ROOT / "configs" / cli_id
        with tempfile.TemporaryDirectory() as temporary_directory:
            fresh_output_directory = Path(temporary_directory) / cli_id
            generate_agent_configs(
                cli_id,
                fresh_output_directory,
                options["preset"],
                DEFAULT_TEMPLATES_PATH,
                options["model_prefix"],
                options["role_levels_mode"],
                [],
            )
            expected_paths = sorted(path for path in fresh_output_directory.rglob("*") if path.is_file())
            expected_relative_paths = {
                expected_path.relative_to(fresh_output_directory) for expected_path in expected_paths
            }
            for expected_path in expected_paths:
                relative_path = expected_path.relative_to(fresh_output_directory)
                managed_path = managed_output_directory / relative_path
                artifact_label = f"{cli_id}/{relative_path.as_posix()}"
                if not managed_path.is_file():
                    validation_errors.append(f"Missing managed generated artifact: {artifact_label}")
                    continue
                if not has_generated_marker(managed_path):
                    validation_errors.append(f"Missing structural generator marker: {artifact_label}")
                managed_content = managed_path.read_text(encoding="utf-8")
                if str(ROOT) in managed_content:
                    validation_errors.append(f"Checkout-specific absolute reference: {artifact_label}")
                if managed_path.read_bytes() != expected_path.read_bytes():
                    validation_errors.append(f"Generated artifact drift: {artifact_label}")
            if not managed_output_directory.exists():
                continue
            primary_agent_id = "orchestrator" if cli_id == "amazon-kiro" else "orchestrator-senior"
            primary_file_names = {
                "codex": {"config.toml", "config.override.toml"},
                "opencode": {"opencode.json", "opencode.override.json"},
                "kilo-code": {"kilo.jsonc", "kilo.override.jsonc"},
            }
            legacy_note_names = {"claude-code": "settings.override.md", "amazon-kiro": "agent.override.md"}
            for managed_path in sorted(path for path in managed_output_directory.rglob("*") if path.is_file()):
                relative_path = managed_path.relative_to(managed_output_directory)
                if relative_path in expected_relative_paths:
                    continue
                is_owned_generated_artifact = has_generated_marker(managed_path)
                if not is_owned_generated_artifact and relative_path == Path(CLI_TARGETS[cli_id]["role_catalog_path"]):
                    is_owned_generated_artifact = has_legacy_role_catalog_signature(managed_output_directory, cli_id)
                if not is_owned_generated_artifact and managed_path.name in primary_file_names.get(cli_id, set()):
                    is_owned_generated_artifact = has_legacy_primary_signature(
                        managed_path, managed_output_directory, cli_id, primary_agent_id, require_legacy_catalog=False
                    )
                if not is_owned_generated_artifact and managed_path.parent == (
                    managed_output_directory / CLI_TARGETS[cli_id]["agent_directory"]
                ):
                    is_owned_generated_artifact = has_legacy_role_signature(
                        managed_path, managed_output_directory, cli_id, managed_path.stem, require_legacy_catalog=False
                    )
                if not is_owned_generated_artifact and cli_id == "amazon-kiro" and relative_path == Path(
                    "steering/orchestrator.md"
                ):
                    is_owned_generated_artifact = has_legacy_steering_signature(
                        managed_path, managed_output_directory, require_legacy_catalog=False
                    )
                if not is_owned_generated_artifact and managed_path.name == legacy_note_names.get(cli_id):
                    is_owned_generated_artifact = has_legacy_note_signature(
                        managed_path, managed_output_directory, cli_id, require_legacy_catalog=False
                    )
                if is_owned_generated_artifact:
                    validation_errors.append(
                        f"Unexpected stale managed generated artifact: {cli_id}/{relative_path.as_posix()}"
                    )
    return validation_errors


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed argparse namespace.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", help="Target CLI name, such as codex, claude, kilo, opencode, or kiro.")
    parser.add_argument("--output", help="Directory where generated agent configs will be written.")
    parser.add_argument(
        "--preset",
        default=None,
        help=(
            "Model preset key from registry/model-tiers.yaml recommended_defaults. "
            "Defaults to the CLI-specific preset when omitted. Use '' or none to omit model fields. "
            "Use this explicitly with --role-levels single unless the CLI default preset is already none."
        ),
    )
    parser.add_argument(
        "--role-levels",
        default=None,
        choices=sorted(ROLE_LEVEL_MODES),
        help=(
            "Generate tiered role ids with seniority suffixes or collapse each profile to a single role id. "
            "Defaults to single for Amazon Kiro and tiered for other CLIs."
        ),
    )
    parser.add_argument(
        "--role-preset",
        action="append",
        default=[],
        metavar="ROLES=PRESET",
        help=(
            "Override the model preset for specific roles. ROLES is a comma-separated "
            "list of registry profile ids and supports fnmatch globs (e.g. '*-architect'). "
            "Example: --role-preset \"*-architect,product-manager=openai\". Repeatable; "
            "later rules override earlier ones for the same role. Only applies when "
            "--preset selects a real model preset."
        ),
    )
    parser.add_argument(
        "--templates-path",
        default=DEFAULT_TEMPLATES_PATH,
        help=(
            "Runtime registry path embedded in generated prompts. Explicit paths "
            "are embedded as provided after trimming whitespace and trailing slashes; "
            "defaults to ~/.ai-registry."
        ),
    )
    parser.add_argument(
        "--model-prefix",
        default=None,
        help=(
            "Outer provider prefix for generated model ids. Defaults to kilo for kilo-code, "
            "opencode-go for opencode, and no prefix for other CLIs. Use an empty value to disable."
        ),
    )
    parser.add_argument(
        "--verify-managed-outputs",
        action="store_true",
        help="Fail when tracked managed CLI artifacts differ from fresh generation.",
    )
    return parser.parse_args()


def main() -> int:
    """Run the generator command.

    Returns:
        Process exit code.
    """
    args = parse_args()
    try:
        if args.verify_managed_outputs:
            validation_errors = verify_managed_output_drift()
            if validation_errors:
                print("ERROR managed CLI output verification failed:", file=sys.stderr)
                for validation_error in validation_errors:
                    print(f"- {validation_error}", file=sys.stderr)
                return 1
            print("Managed CLI outputs match fresh generation")
            return 0
        if not args.cli:
            raise ValueError("--cli is required unless --verify-managed-outputs is used")
        if not args.output:
            raise ValueError("--output is required unless --verify-managed-outputs is used")
        cli_id = canonical_cli(args.cli)
        output_directory = Path(args.output)
        default_role_levels_mode = "single" if cli_id == "amazon-kiro" else "tiered"
        selected_role_levels_mode = args.role_levels or default_role_levels_mode
        role_levels_mode = normalized_role_levels_mode(selected_role_levels_mode)
        preset = default_preset_for_cli(cli_id) if args.preset is None else args.preset
        default_model_prefix = (
            DEFAULT_MODEL_PREFIXES.get(cli_id, "") if args.model_prefix is None else args.model_prefix
        )
        model_prefix = normalize_model_prefix(default_model_prefix)
        generated_count = generate_agent_configs(
            cli_id,
            output_directory,
            preset,
            args.templates_path,
            model_prefix,
            role_levels_mode,
            args.role_preset,
        )
    except (FileNotFoundError, RegistryError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Generated {generated_count} {cli_id} agent config files in {output_directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
