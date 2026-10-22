# Bugfix Workflow

Workflow id: `bugfix`

Use this workflow to triage, reproduce, diagnose, fix, validate, and release a defect in an existing product.

## Files

- Manifest: `workflows/engineering/bugfix/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow follows a distinct corrective path: ASSESS, FIX, TEST, VERIFY, and INDEPENDENT REVIEW. It is narrower than `feature-development`: preserve intended behavior, minimize change scope, and validate regression risk. Use `incident-response` when the issue is an active production incident.

ASSESS routes the affected fix to `secure-sdd` before FIX only when the user requests the full process or the action materially changes a trust boundary, security enforcement, production authority, or an irreversible operation. A path, domain label, normal dependency update, or routine configuration fix alone is not escalation. Handoff is not abandonment: continue independent diagnosis and safe remediation while the dependent action waits.

Every bugfix needs applicable deterministic verification evidence. A failed required check returns the affected change to remediation; it cannot be declared passing by HUMAN approval. Distinguish a failing check from an unavailable environment check, pursue alternative diagnostics or verification, and report remaining limits honestly. Diagnostic review and independent work can proceed while verified completion or release remains blocked.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
