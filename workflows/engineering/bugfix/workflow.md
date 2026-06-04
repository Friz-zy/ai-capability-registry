# Bugfix Workflow

Workflow id: `bugfix`

Use this workflow to triage, reproduce, diagnose, fix, validate, and release a defect in an existing product.

## Files

- Manifest: `workflows/engineering/bugfix/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow is narrower than `feature-development`: preserve existing behavior, minimize change scope, and validate regression risk. Use `incident-response` when the issue is an active production incident.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
