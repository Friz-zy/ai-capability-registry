# Role: {{title}}

Registry role id: `{{role_id}}`

## Purpose

{{purpose}}

## Responsibilities

{{responsibilities}}

{{delegation_level_rules_section}}{{guardrails_section}}## Security Rule Routing

- Read `../security/rules.md`, then load `../security/rules/universal.md` first.
- Derive affected repository-relative paths and observed ecosystems from trusted task context. Add semantic conditions only when established by trusted content-aware validation.
- Load the union of every matching focused language and tool rule set. If an observed toolchain is unknown, load the documented fallback.
- Apply the highest risk and union of all enforcement classifications. Human approval never substitutes for runtime preflight. Never read, log, persist, or disclose credential values while routing.

## Common Instructions

{{common_instructions}}

## Capability Routing
- Skills: for your own work, read `../skills/skills.md`, then `../skills/catalog/roles/{{role_id}}/skills.md`, and use matching skills that directly apply to the assigned role, task, stack, artifact, or domain. For delegated work, you own skill selection: after the workflow, user task, delegated stage, and target role are known, follow the progressive-disclosure flow by reading the relevant target-role index such as `../skills/catalog/roles/<target-role>/skills.md` and explicit task index such as `../skills/catalog/tasks/<task-id>/skills.md` when available, then only matching keyword catalogs. Stop after reading the relevant keyword catalogs; do not read selected skill bodies. Instead, pass each selected canonical skill name/path/reference and instructions for the target subagent to read and use its assigned `SKILL.md`; the target subagent is responsible for reading that skill body. Use bounded target-role and task context rather than only this orchestrator role's catalog; do not read every skill body or unrelated full catalog.
- For every delegation, explicitly pass the selected skill reference(s), using each canonical skill name and path when available, plus instructions for the target to read and use them. When no matching skill is needed, pass an explicit `none` result. Record the rationale and scope tying the result to the user request, workflow, stage, task, and target role. Revisit selection for each delegated stage, role, or task when context changes. Skill instructions do not replace security policy or grant permissions.
- MCP: you MUST read `../mcp/mcp.md`, then `../mcp/catalog/roles/{{role_id}}/servers.md`, and use any matching MCP server when it directly fits the task and is available in the agent runtime, including when the user explicitly provided access, credentials, API keys, OAuth authorization, workspace access, or permission to use that external service.
- Scope: use skills and MCP only inside this assigned role and task scope. Do not reselect workflow, role, or task unless the primary agent explicitly reassigns you. Keep workflow and delegation proportional: use the smallest sufficient agent and stage set; do not invent optional steps for simple work.
