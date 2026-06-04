# Infrastructure Provisioning Workflow

Workflow id: `infrastructure-provisioning`

Use this workflow to plan and provision infrastructure, environments, network, IAM, CI/CD, observability, and cost controls.

## Files

- Manifest: `workflows/platform-operations/infrastructure-provisioning/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow is for infrastructure creation or major environment setup. Use `finops-cost-optimization` when cost reduction is the primary goal.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
