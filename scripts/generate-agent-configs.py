#!/usr/bin/env python3
"""Generate CLI agent role configs from registry profiles and model tiers."""

from __future__ import annotations

import argparse
import json
import re
import sys
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

DISABLED_MODEL_PRESETS = {"", "none"}
MODEL_REMOVAL_TOKEN = "__MODEL_FIELD_DISABLED__"

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


def model_for_level(recommended_defaults: dict[str, Any], level: str, preset: str, profile_id: str) -> str:
    """Resolve the model id for a profile level and preset.

    Args:
        recommended_defaults: ``recommended_defaults`` mapping from model tiers.
        level: Seniority level such as ``middle`` or ``senior``.
        preset: Preset key such as ``openai`` or ``anthropic``.
        profile_id: Profile id used for precise errors.

    Returns:
        Model id.

    Raises:
        ValueError: If the level or preset is missing.
    """
    level_defaults = recommended_defaults.get(level)
    if not isinstance(level_defaults, dict):
        raise ValueError(f"Missing recommended_defaults level '{level}' for profile '{profile_id}'")
    model_id = level_defaults.get(preset)
    if not model_id:
        raise ValueError(f"Missing model preset '{preset}' for profile '{profile_id}' level '{level}'")
    return str(model_id)


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


def model_catalog_id_for_id(model_tiers_registry: dict[str, Any], model_id: str) -> str | None:
    """Find the provider-qualified catalog id for a registry model id.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id without provider prefix.

    Returns:
        Provider-qualified catalog id when the model is found, otherwise ``None``.
    """
    providers = model_tiers_registry.get("providers", [])
    if not isinstance(providers, list):
        return None
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
                if not isinstance(model, dict) or model.get("model_id") != model_id:
                    continue
                catalog_model_id = model.get("openrouter_id")
                if isinstance(catalog_model_id, str) and "/" in catalog_model_id:
                    return catalog_model_id
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
    """Normalize a registry template path for generated prompt references.

    Args:
        path: User-provided path to the runtime registry templates.

    Returns:
        Path without trailing slashes, preserving ``~`` when provided.
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
    templates_path: str,
) -> dict[str, str]:
    """Build placeholder values for role prompt templates.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling agent ids.
        model: Resolved model id or ``None`` when model rendering is disabled.
        common_instructions: Shared profile instructions.
        templates_path: Runtime registry template path used in generated references.

    Returns:
        Placeholder mapping for ``templates/roles`` prompt templates.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    responsibilities = bullet_list(string_list(role.get("responsibilities")))
    guardrails_section = markdown_section("You must follow this guardrails", string_list(role.get("guardrails")))
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
    level_prefix = f"{level} " if role_levels_mode != "single" else ""
    return {
        "agent_id": agent_id,
        "role_id": profile_id,
        "profile_id": profile_id,
        "level": level,
        "level_label": level,
        "level_prefix": level_prefix,
        "model": model or "",
        "title": title,
        "purpose": purpose,
        "responsibilities": responsibilities,
        "guardrails_section": guardrails_section,
        "delegation_level_rules_section": delegation_level_rules_section,
        "delegation_examples": delegation_examples,
        "common_instructions": bullet_list(common_instructions),
        "templates_path": runtime_templates_path,
        "role_catalog_path": "roles.md",
    }


def render_role_prompt(
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    model: str | None,
    common_instructions: list[str],
    templates_path: str,
    single_mode_id_replacements: dict[str, str] | None,
) -> str:
    """Render the system prompt for one generated agent.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        role_levels_mode: Generation mode controlling agent ids.
        model: Resolved model id or ``None`` when model rendering is disabled.
        common_instructions: Shared profile instructions.
        templates_path: Runtime registry template path used in generated references.
        single_mode_id_replacements: Tiered-to-single generated id replacements.

    Returns:
        Rendered system prompt.
    """
    profile_id = str(profile.get("id") or "unknown")
    prompt_template_name = "orchestrator-prompt-template.md" if profile_id == "orchestrator" else "role-prompt-template.md"
    prompt_template_path = AGENT_TEMPLATES_DIR / prompt_template_name
    values = role_prompt_values(profile, level, role_levels_mode, model, common_instructions, templates_path)
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


def render_cli_agent(
    cli_id: str,
    profile: dict[str, Any],
    level: str,
    role_levels_mode: str,
    model: str | None,
    prompt: str,
    model_disabled: bool,
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
    model_disabled: bool,
    is_override: bool,
    role_levels_mode: str,
) -> str:
    """Render the Codex main config or override file.

    Args:
        entries: Profile and seniority pairs being generated.
        primary_model: Resolved orchestrator model id when available.
        model_disabled: Whether model fields were disabled by the preset.
        is_override: Whether the file is a manual-merge override.
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
    lines = ["# Generated by scripts/generate-agent-configs.py."]
    if is_override:
        lines.append("# Manual merge required: apply this file to an existing Codex config.toml.")
    lines.append(f"default_agent = {quoted_string(primary_agent_id)}")
    if primary_model and not model_disabled:
        lines.append(f"model = {quoted_string(primary_model)}")
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
    return "{\n" + f"  \"default_agent\": {quoted_string(agent_name)}\n" + "}\n"


def kilo_default_config_text(agent_name: str, is_override: bool) -> str:
    """Render the Kilo Code main config or override file.

    Args:
        agent_name: Primary agent name to activate.
        is_override: Whether the generated file is a manual-merge override.

    Returns:
        JSONC content selecting the default agent.
    """
    lines = ["// Generated by scripts/generate-agent-configs.py."]
    if is_override:
        lines.append("// Manual merge required: apply this override to an existing kilo.jsonc file.")
    lines.append("{")
    lines.append(f"  \"default_agent\": {quoted_string(agent_name)}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def generate_primary_role_artifact(
    cli_id: str,
    output_directory: Path,
    entries: list[tuple[dict[str, Any], str]],
    primary_model: str | None,
    model_disabled: bool,
    role_levels_mode: str,
) -> int:
    """Write the primary-role config or override artifact for the selected CLI.

    Args:
        cli_id: Canonical CLI target id.
        output_directory: Directory where generated files are written.
        entries: Profile and seniority pairs being generated.
        primary_model: Resolved orchestrator model id when available.
        model_disabled: Whether model fields were disabled by the preset.
        role_levels_mode: Generation mode controlling agent ids.

    Returns:
        Number of generated primary-role artifacts.
    """
    primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
    primary_agent_id = generated_agent_id(primary_profile, primary_level, role_levels_mode)
    if cli_id == "codex":
        main_config_path = output_directory / "config.toml"
        target_path = output_directory / ("config.override.toml" if main_config_path.exists() else "config.toml")
        write_text(
            target_path,
            codex_config_text(
                entries,
                primary_model,
                model_disabled,
                target_path.name.endswith(".override.toml"),
                role_levels_mode,
            ),
        )
        return 1
    if cli_id == "opencode":
        main_config_path = output_directory / "opencode.json"
        target_path = output_directory / ("opencode.override.json" if main_config_path.exists() else "opencode.json")
        write_text(target_path, default_agent_json_text(primary_agent_id))
        return 1
    if cli_id == "kilo-code":
        main_config_path = output_directory / "kilo.jsonc"
        target_path = output_directory / ("kilo.override.jsonc" if main_config_path.exists() else "kilo.jsonc")
        write_text(target_path, kilo_default_config_text(primary_agent_id, target_path.name.endswith(".override.jsonc")))
        return 1
    if cli_id == "claude-code":
        return 0
    if cli_id == "amazon-kiro":
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


def cleanup_previous_generated_files(output_directory: Path, cli_id: str, profiles: list[dict[str, Any]]) -> None:
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
                if generated_path.is_file():
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
        if stale_note_path.is_file():
            stale_note_path.unlink()


def generate_agent_configs(
    cli_id: str,
    output_directory: Path,
    preset: str | None,
    templates_path: str,
    model_prefix: str,
    role_levels_mode: str,
) -> int:
    """Generate all role-level agent configs for a CLI target.

    Args:
        cli_id: Canonical CLI target id.
        output_directory: Directory where generated files are written.
        preset: Model preset key from recommended defaults, or ``""``/``none`` to omit models.
        templates_path: Runtime registry template path used in generated references.
        model_prefix: Outer provider prefix for generated model ids.
        role_levels_mode: ``tiered`` for current behavior or ``single`` for collapsed roles.

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

    common_instructions = string_list(profiles_registry.get("common_instructions"))
    extension = CLI_TARGETS[cli_id]["extension"]
    agent_directory = output_directory / CLI_TARGETS[cli_id]["agent_directory"]
    entries = generated_agent_entries(profiles, role_levels_mode)
    single_mode_id_replacements = single_mode_agent_id_replacements(profiles) if role_levels_mode == "single" else None
    cleanup_previous_generated_files(output_directory, cli_id, profiles)
    write_text(
        output_directory / CLI_TARGETS[cli_id]["role_catalog_path"],
        generated_role_catalog(entries, role_levels_mode),
    )
    generated_count = 0
    for profile, level in entries:
        profile_id = str(profile.get("id") or "unknown")
        model: str | None = None
        if not model_disabled:
            model = rendered_model_id(
                model_tiers_registry,
                model_for_level(recommended_defaults, level, selected_preset, profile_id),
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
            templates_path,
            single_mode_id_replacements,
        )
        generated_agent_id_value, rendered_agent = render_cli_agent(
            cli_id,
            profile,
            level,
            role_levels_mode,
            model,
            prompt,
            model_disabled,
        )
        write_text(agent_directory / f"{generated_agent_id_value}{extension}", rendered_agent)
        generated_count += 1
    primary_model = None
    if not model_disabled:
        primary_profile, primary_level = orchestrator_primary_entry(entries, role_levels_mode)
        primary_model = rendered_model_id(
            model_tiers_registry,
            model_for_level(
                recommended_defaults,
                primary_level,
                selected_preset,
                str(primary_profile.get("id") or "unknown"),
            ),
            model_prefix,
            str(primary_profile.get("id") or "unknown"),
            cli_id in DEFAULT_MODEL_PREFIXES,
        )
    generated_count += generate_primary_role_artifact(
        cli_id,
        output_directory,
        entries,
        primary_model,
        model_disabled,
        role_levels_mode,
    )
    return generated_count


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed argparse namespace.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", required=True, help="Target CLI name, such as codex, claude, kilo, opencode, or kiro.")
    parser.add_argument("--output", required=True, help="Directory where generated agent configs will be written.")
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
        "--templates-path",
        default=DEFAULT_TEMPLATES_PATH,
        help="Runtime registry template path embedded in generated prompts. Defaults to ~/.ai-registry.",
    )
    parser.add_argument(
        "--model-prefix",
        default=None,
        help=(
            "Outer provider prefix for generated model ids. Defaults to kilo for kilo-code, "
            "opencode-go for opencode, and no prefix for other CLIs. Use an empty value to disable."
        ),
    )
    return parser.parse_args()


def main() -> int:
    """Run the generator command.

    Returns:
        Process exit code.
    """
    args = parse_args()
    try:
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
        )
    except (FileNotFoundError, RegistryError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Generated {generated_count} {cli_id} agent config files in {output_directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
