# Bugfix Workflow

Workflow id: `bugfix`

Use this workflow to triage, reproduce, diagnose, fix, validate, and release a defect in an existing product.

## Files

- Manifest: `workflows/engineering/bugfix/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This workflow follows a distinct corrective path: ASSESS, FIX, TEST, VERIFY, and INDEPENDENT REVIEW. It is narrower than `feature-development`: preserve intended behavior, minimize change scope, and validate regression risk. Use `incident-response` when the issue is an active production incident.

ASSESS is a terminal routing gate. Escalate to `secure-sdd` before FIX when the fix requires changing intended behavior, architecture, dependencies or build tooling, sandbox or privilege boundaries, untrusted inputs or prompt handling, secrets, authentication or authorization, or infrastructure. Only an ASSESS result of `secure_sdd_escalation_decision: not_required` permits FIX.

Every bugfix requires reproducible deterministic verification evidence. On failure, VERIFY emits failed verification evidence and an exception request, not an exception decision. The failure remains blocking and returns work to remediation and re-verification; it cannot be waived by a HUMAN authority. INDEPENDENT REVIEW and release remain blocked until deterministic verification passes.

Follow the manifest for stage order, role delegation, gates, and acceptance criteria.
