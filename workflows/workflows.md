# Workflow Capability Registry

Read `../capability-routing.md` first. This file defines workflow-specific routing.

## Workflow Resolution Protocol

Before ordinary skill routing, decide whether a workflow applies by task first and role second:

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Read only guide files for workflows matched by the selected task or role.
3. Use workflow guidance to choose relevant process skills before implementation skills.
4. Continue capability routing through `skills/skills.md` and `mcp/mcp.md` when those entrypoints are available.

Read only workflow files that match the current task or role. Do not browse `workflows/` broadly.

### Skill Use Requirement

If a trusted or reviewed workflow or process skill plausibly matches after routing, use it before acting. If the loaded skill does not fit, stop using it and continue with the next best match.

## Workflows

### Development Workflow

Select process guidance for software development tasks before implementation or domain skills.

**ID:** `development`
**Guide:** `workflows/development.md`
**Categories:** `engineering`, `quality`, `delivery`

### Development Workflow Task IDs

`plan-feature`, `implement-code`, `review-code`, `debug-incident`, `test-validate`, `security-audit`, `build-frontend`, `build-backend`, `deploy-release`, `automate-agent`, `manage-data-systems`, `manage-cloud-infra`, `build-blockchain`, `build-hardware-iot`, `build-mobile-desktop`

### Development Workflow Role IDs

`cto-engineering-lead`, `software-engineer`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `qa-engineer`, `security-engineer`, `devops-platform-engineer`, `sre-incident-manager`, `ai-engineer`, `ai-agent-builder`, `data-engineer`, `cloud-infrastructure-engineer`, `blockchain-engineer`, `hardware-iot-engineer`

All other roles and tasks have no workflow unless another registry entry adds one.
