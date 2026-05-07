# Workflow Catalog

Generated from `registry/workflows.yaml`.

## Agent Bootstrap

Generate agent-specific config references from registry metadata.

Steps:
- `validate_registry`
- `generate_indexes`
- `generate_agent_configs`
- `link_artifacts`

## MCP Risk Review

Review MCP server permissions, transport, runtime, and data exposure before enablement.

Steps:
- `verify_hosted_or_docker_runtime`
- `verify_no_unrestricted_local_execution`
- `classify_data_risk`
- `require_read_only_or_ask_before_write`
- `document_required_secrets`

## Secure Capability Onboarding

Review, pin, index, generate, and manually promote a new skill or MCP server.

Steps:
- `identify_source_owner`
- `verify_execution_model`
- `check_license`
- `review_scripts_and_hooks`
- `pin_tag_and_commit`
- `add_registry_entry`
- `run_validation`
- `generate_artifacts`
- `enable_manually_if_reviewed`
