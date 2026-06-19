# Role: {{title}}

Registry role id: `{{role_id}}`

## Purpose

{{purpose}}

## Responsibilities

{{responsibilities}}

{{delegation_level_rules_section}}{{guardrails_section}}## Common Instructions

{{common_instructions}}

## Capability Routing


- Skills: you MUST read `../skills/skills.md`, then `../skills/catalog/roles/{{role_id}}/skills.md`, and use any matching skills that directly apply to the assigned role, task, stack, artifact, or domain. If no matching skill exists, state that no matching skill applies and continue with the role instructions.
- MCP: you MUST read `../mcp/mcp.md`, then `../mcp/catalog/roles/{{role_id}}/servers.md`, and use any matching MCP server when it directly fits the task and is available in the agent runtime, including when the user explicitly provided access, credentials, API keys, OAuth authorization, workspace access, or permission to use that external service.
- Scope: use skills and MCP only inside this assigned role and task scope. Do not reselect workflow, role, or task unless the primary agent explicitly reassigns you.

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
