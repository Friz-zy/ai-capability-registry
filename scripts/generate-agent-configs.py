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


def rendered_model_id(model_tiers_registry: dict[str, Any], model_id: str, model_prefix: str, profile_id: str) -> str:
    """Resolve the final model id written to generated agent configs.

    Args:
        model_tiers_registry: Loaded ``model-tiers`` registry.
        model_id: Model id from recommended defaults.
        model_prefix: Normalized outer provider prefix.
        profile_id: Profile id used for precise errors.

    Returns:
        Raw model id when no prefix is configured, otherwise ``prefix/provider/model``.
    """
    if not model_prefix:
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


def generated_agent_id(profile: dict[str, Any], level: str) -> str:
    """Build the generated agent id from domain, role name, and level.

    Args:
        profile: Registry profile entry.
        level: Seniority level.

    Returns:
        Agent id following ``<domain>-<role-name>-<level>`` when role name exists,
        otherwise ``<domain>-<level>`` for single-token roles.
    """
    domain_slug, role_name_slug = role_slug_parts(profile)
    level_slug = slugify(level)
    if role_name_slug:
        return f"{domain_slug}-{role_name_slug}-{level_slug}"
    return f"{domain_slug}-{level_slug}"


def level_title(level: str, title: str) -> str:
    """Build a concise level-qualified role title.

    Args:
        level: Seniority level.
        title: Role display title.

    Returns:
        Title such as ``lead AI Engineer``.
    """
    return f"{level} {title}"


def agent_description(title: str, level: str, purpose: str) -> str:
    """Build a concise CLI-facing agent description.

    Args:
        title: Role display title.
        level: Seniority level.
        purpose: Role mission or profile description.

    Returns:
        Human-readable agent description for CLI agent pickers.
    """
    return f"{level_title(level, title)}. {purpose}"


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
    model: str,
    common_instructions: list[str],
    templates_path: str,
) -> dict[str, str]:
    """Build placeholder values for role prompt templates.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        model: Resolved model id.
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
    agent_id = generated_agent_id(profile, level)
    runtime_templates_path = normalized_reference_path(templates_path)
    return {
        "agent_id": agent_id,
        "role_id": profile_id,
        "profile_id": profile_id,
        "level": level,
        "level_label": level,
        "model": model,
        "title": title,
        "purpose": purpose,
        "responsibilities": responsibilities,
        "guardrails_section": guardrails_section,
        "delegation_level_rules_section": delegation_level_rules_section,
        "common_instructions": bullet_list(common_instructions),
        "templates_path": runtime_templates_path,
        "role_catalog_path": "roles.md",
    }


def render_role_prompt(
    profile: dict[str, Any],
    level: str,
    model: str,
    common_instructions: list[str],
    templates_path: str,
) -> str:
    """Render the system prompt for one generated agent.

    Args:
        profile: Registry profile entry.
        level: Seniority level.
        model: Resolved model id.
        common_instructions: Shared profile instructions.
        templates_path: Runtime registry template path used in generated references.

    Returns:
        Rendered system prompt.
    """
    profile_id = str(profile.get("id") or "unknown")
    prompt_template_name = "orchestrator-prompt-template.md" if profile_id == "orchestrator" else "role-prompt-template.md"
    prompt_template_path = AGENT_TEMPLATES_DIR / prompt_template_name
    values = role_prompt_values(profile, level, model, common_instructions, templates_path)
    return render_text(
        template_text(prompt_template_path),
        values,
        str(prompt_template_path),
    )


def render_cli_agent(cli_id: str, profile: dict[str, Any], level: str, model: str, prompt: str) -> tuple[str, str]:
    """Render one CLI-specific agent config.

    Args:
        cli_id: Canonical CLI target id.
        profile: Registry profile entry.
        level: Seniority level.
        model: Resolved model id.
        prompt: Rendered system prompt.

    Returns:
        Pair of generated agent id and rendered file content.
    """
    role = profile_role(profile)
    profile_id = str(profile.get("id") or "unknown")
    title = str(role.get("title") or profile.get("name") or profile_id)
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    generated_agent_id_value = generated_agent_id(profile, level)
    template_kind = "orchestrator-agent-template" if profile_id == "orchestrator" else "role-agent-template"
    template_dir = CLI_TARGETS[cli_id]["template_dir"]
    extension = CLI_TARGETS[cli_id]["extension"]
    cli_template_path = AGENT_TEMPLATES_DIR / template_dir / f"{template_kind}{extension}"
    generated_description = agent_description(title, level, purpose)
    values = {
        "agent_id_json": quoted_string(generated_agent_id_value),
        "agent_id_toml": quoted_string(generated_agent_id_value),
        "agent_id_yaml": quoted_string(generated_agent_id_value),
        "agent_description_json": quoted_string(generated_description),
        "agent_description_toml": quoted_string(generated_description),
        "agent_description_yaml": quoted_string(generated_description),
        "model_json": quoted_string(model),
        "model_toml": quoted_string(model),
        "model_yaml": quoted_string(model),
        "prompt": prompt,
        "prompt_json": quoted_string(prompt),
        "prompt_toml": quoted_string(prompt),
    }
    rendered = render_text(template_text(cli_template_path), values, str(cli_template_path))
    return generated_agent_id_value, rendered


def generated_agent_entries(profiles: list[dict[str, Any]]) -> list[tuple[dict[str, Any], str]]:
    """Return every profile and seniority pair to generate.

    Args:
        profiles: Registry profile entries.

    Returns:
        Pairs of profile mapping and seniority level.
    """
    entries: list[tuple[dict[str, Any], str]] = []
    for profile in sorted(profiles, key=lambda item: str(item.get("id") or "")):
        if not isinstance(profile, dict):
            raise ValueError("Every profile entry must be a mapping")
        for level in string_list(profile.get("seniority")) or ["middle"]:
            entries.append((profile, level))
    return entries


def role_catalog_line(profile: dict[str, Any], levels: list[str]) -> str:
    """Render one concise generated role catalog line.

    Args:
        profile: Registry profile entry.
        levels: Seniority levels available for the profile.

    Returns:
        Markdown bullet with role ids, description, tags, and usage hint.
    """
    role = profile_role(profile)
    title = str(role.get("title") or profile.get("name") or profile.get("id") or "unknown")
    purpose = str(role.get("mission") or profile.get("description") or "No purpose specified.")
    profile_description = str(profile.get("description") or purpose)
    categories = string_list(profile.get("include", {}).get("categories"))
    tags = ", ".join(f"`{category}`" for category in categories) if categories else "none"
    generated_ids = ", ".join(f"`{generated_agent_id(profile, level)}`" for level in levels)
    return (
        f"- {generated_ids}: {title}. "
        f"{purpose} Tags: {tags}. Choose when: {profile_description}"
    )


def generated_role_catalog(entries: list[tuple[dict[str, Any], str]]) -> str:
    """Render the generated role catalog.

    Args:
        entries: Profile and level pairs being generated.

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
    lines.extend(role_catalog_line(profile, levels) for profile, levels in grouped_profiles.values())
    return "\n".join(lines)


def cleanup_previous_generated_files(output_directory: Path, cli_id: str, entries: list[tuple[dict[str, Any], str]]) -> None:
    """Remove previously generated files for the current CLI target.

    This only deletes files matching generated agent ids in the current flat output
    directory and in the current CLI agent directory. It avoids deleting unrelated
    user files from the output tree.

    Args:
        output_directory: Root output directory selected by the user.
        cli_id: Canonical CLI target id.
        entries: Profile and level pairs being regenerated.
    """
    extension = CLI_TARGETS[cli_id]["extension"]
    agent_directories = [output_directory / CLI_TARGETS[cli_id]["agent_directory"]]
    agent_directories.extend(output_directory / legacy_path for legacy_path in LEGACY_AGENT_DIRECTORIES.get(cli_id, []))
    for profile, level in entries:
        file_name = f"{generated_agent_id(profile, level)}{extension}"
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


def generate_agent_configs(
    cli_id: str,
    output_directory: Path,
    preset: str,
    templates_path: str,
    model_prefix: str,
) -> int:
    """Generate all role-level agent configs for a CLI target.

    Args:
        cli_id: Canonical CLI target id.
        output_directory: Directory where generated files are written.
        preset: Model preset key from recommended defaults.
        templates_path: Runtime registry template path used in generated references.
        model_prefix: Outer provider prefix for generated model ids.

    Returns:
        Number of generated files.

    Raises:
        ValueError: If registry data or preset resolution is invalid.
    """
    profiles_registry = load_registry("profiles")
    model_tiers_registry = load_registry("model-tiers")
    profiles = profiles_registry.get("profiles", [])
    if not isinstance(profiles, list):
        raise ValueError("registry/profiles.yaml must contain a profiles list")
    recommended_defaults = model_tiers_registry.get("recommended_defaults", {})
    if not isinstance(recommended_defaults, dict):
        raise ValueError("registry/model-tiers.yaml must contain recommended_defaults")
    if preset not in available_presets(recommended_defaults):
        presets = ", ".join(available_presets(recommended_defaults))
        raise ValueError(f"Unknown preset '{preset}'. Available presets: {presets}")

    common_instructions = string_list(profiles_registry.get("common_instructions"))
    extension = CLI_TARGETS[cli_id]["extension"]
    agent_directory = output_directory / CLI_TARGETS[cli_id]["agent_directory"]
    entries = generated_agent_entries(profiles)
    cleanup_previous_generated_files(output_directory, cli_id, entries)
    write_text(output_directory / CLI_TARGETS[cli_id]["role_catalog_path"], generated_role_catalog(entries))
    generated_count = 0
    for profile, level in entries:
        profile_id = str(profile.get("id") or "unknown")
        model = rendered_model_id(
            model_tiers_registry,
            model_for_level(recommended_defaults, level, preset, profile_id),
            model_prefix,
            profile_id,
        )
        prompt = render_role_prompt(profile, level, model, common_instructions, templates_path)
        generated_agent_id_value, rendered_agent = render_cli_agent(cli_id, profile, level, model, prompt)
        write_text(agent_directory / f"{generated_agent_id_value}{extension}", rendered_agent)
        generated_count += 1
    return generated_count


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed argparse namespace.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", required=True, help="Target CLI name, such as codex, claude, kilo, opencode, or kiro.")
    parser.add_argument("--output", required=True, help="Directory where generated agent configs will be written.")
    parser.add_argument("--preset", required=True, help="Model preset key from registry/model-tiers.yaml recommended_defaults.")
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
        default_model_prefix = (
            DEFAULT_MODEL_PREFIXES.get(cli_id, "") if args.model_prefix is None else args.model_prefix
        )
        model_prefix = normalize_model_prefix(default_model_prefix)
        generated_count = generate_agent_configs(
            cli_id,
            output_directory,
            args.preset,
            args.templates_path,
            model_prefix,
        )
    except (FileNotFoundError, RegistryError, ValueError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 1
    print(f"Generated {generated_count} {cli_id} agent config files in {output_directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
