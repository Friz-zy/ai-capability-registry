# Idea Validation Workflow

Workflow id: `idea-validation`

Use this workflow to evaluate a product or business idea before committing to full product delivery.

## Files

- Manifest: `workflows/product-discovery/idea-validation/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow follows a distinct pre-delivery path: CAPTURE, EVIDENCE, REFINE, DESIGN, then GO, CLARIFY, or KILL. It should produce evidence, assumptions, and a decision with rationale.

A GO decision may record an explicit handoff target, but it must not automatically start any delivery workflow. CLARIFY returns the work to the appropriate earlier stage with targeted evidence gaps. KILL ends the validation path and records the rationale.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
