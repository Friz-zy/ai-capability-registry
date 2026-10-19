# Secure SDD Workflow

Workflow id: `secure-sdd`

Use this full workflow when explicitly requested or when an actual material trust-boundary or security-enforcement change needs independent specification and policy disposition. Ordinary reversible implementation and unchanged-scope verification use a shorter assess, implement, test, and review path.

## Files

- Manifest: `workflows/security-compliance/secure-sdd/workflow.yaml`
- Common schemas: `workflows/templates/schemas/`
- Common artifact templates: `workflows/templates/artifacts/`

## Coordinator Notes

This is a standalone workflow with no portable-guidance, provider, or model dependency.

The canonical sequence is strict: SPECIFY, CLARIFY, INDEPENDENT SPEC REVIEW, PLAN, conditional ARCHITECTURE REVIEW, CHECKLIST, TASKS, VERIFICATION PLAN, ANALYZE, IMPLEMENT, ADVERSARIAL TEST, DETERMINISTIC VERIFY, risk-based SECURITY REVIEW, FINAL INDEPENDENT REVIEW, CONVERGE, and POLICY GATE.

Use `threat-modeling` as an explicit escalation when the change introduces or changes assets, trust boundaries, attacker capabilities, or attack paths. Use `security-review` as an explicit escalation when risk-based implementation security review is required. Neither escalation replaces the required Secure SDD policy gate.

Before PLAN and again in ANALYZE before IMPLEMENT, fresh read-only reviewers must independently gate untrusted-content and prompt-injection exposure, dependency provenance, quarantine, and integrity, and sandbox or privilege boundaries. ANALYZE reviewers must be disjoint from IMPLEMENT roles and must record those assessments, a risk classification, and unresolved findings. Uncertainty about any of those topics is an escalation, not an implicit pass. Each conditional ARCHITECTURE REVIEW and SECURITY REVIEW emits exactly one mandatory result artifact with status `reviewed`, `escalated`, or `not_applicable` and the fields required for that status. FINAL INDEPENDENT REVIEW consumes the implementation change summary, adversarial and regression evidence, deterministic verification, risk assessment, and conditional review results.

ARCHITECTURE REVIEW assigns only non-implementer reviewers. Its result must assess architecture, infrastructure, sandbox and privilege boundaries, and dependency provenance and lock integrity, or explicitly escalate the uncertainty.

On deterministic verification failure, DETERMINISTIC VERIFY emits failed verification evidence and an exception request, not an exception decision. The failure is blocking and returns work to remediation and re-verification; it cannot be waived by a HUMAN authority, CONVERGE, or POLICY GATE. A HUMAN disposition is permitted only for an explicitly classified residual risk that remains after remediation and fresh independent re-review. A rejection returns the work to remediation.

Follow the manifest for stage order, role separation, reviewer independence, human escalation, gates, and acceptance criteria.
