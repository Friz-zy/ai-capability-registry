# Feature Development Workflow

Use this workflow when the user wants to add, change, or improve functionality in an existing product.

## Files

- Manifest: `workflows/product-delivery/feature-development/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow is shorter than new-product workflows, but regression risk is higher because existing users, systems, data, APIs, and design patterns may already exist. Preserve existing product and codebase constraints unless the user explicitly asks to change them.

Use staged parallel delegation inside each stage, then validate outputs against the manifest acceptance criteria before continuing.
