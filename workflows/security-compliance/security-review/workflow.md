# Security Review Workflow

Workflow id: `security-review`

Use this workflow to review application, infrastructure, dependency, secrets, authentication, authorization, and vulnerability risks.

## Files

- Manifest: `workflows/security-compliance/security-review/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow covers security findings and remediation planning. Use `threat-modeling` when the primary work is modeling assets, trust boundaries, and attack paths before or during design.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
