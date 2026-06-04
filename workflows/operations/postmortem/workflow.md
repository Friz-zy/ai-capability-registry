# Postmortem Workflow

Workflow id: `postmortem`

Use this workflow to analyze an incident after stabilization, identify causes and detection gaps, and assign prevention actions.

## Files

- Manifest: `workflows/operations/postmortem/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow is for learning after an incident, not real-time response. Use `incident-response` while mitigation or recovery is still active.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
