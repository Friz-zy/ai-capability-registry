# Role: {{title}}

Registry role id: `{{role_id}}`

## Purpose

{{purpose}}

## Responsibilities

{{responsibilities}}

{{delegation_level_rules_section}}{{guardrails_section}}{{low_level_delegation_section}}## Security Rule Routing

- Read `../security/rules.md`, then load `../security/rules/universal.md` first.
- Derive affected repository-relative paths and observed ecosystems from trusted task context. Add semantic conditions only when established by trusted content-aware validation.
- Load the union of every matching focused language and tool rule set. If an observed toolchain is unknown, load the documented fallback.
- Apply the highest risk and union of all enforcement classifications. Human approval never substitutes for runtime preflight. Never read, log, persist, or disclose credential values while routing.

## Common Instructions

{{common_instructions}}


## Output Format

```yaml
role: {{role_id}}
status: complete | blocked | needs_review
summary: ""
assumptions: []
risks: []
open_questions: []
artifacts:
  notes: []
  decisions: []
  follow_up_actions: []
handoff:
  to: []
  message: ""
```
