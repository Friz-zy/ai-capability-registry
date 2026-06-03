# SaaS From Scratch Workflow

Use this workflow when the user wants to create a new web product, SaaS, marketplace, dashboard, platform, or service from zero.

## Files

- Manifest: `workflows/product-delivery/saas-from-scratch/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow has the deepest discovery and architecture phases because there is no existing product context, no established design system, and usually no validated customer base. Do not rush into implementation planning until the business problem, target users, and MVP boundary are explicit.

Use staged parallel delegation inside each stage, then validate outputs against the manifest acceptance criteria before continuing.
