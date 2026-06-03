# Workflow Capability Dispatcher

Read `../capability-routing.md` first. This file defines workflow-specific routing.

## Workflow Resolution Protocol

Workflow routing is the primary practice for all new user tasks and requests. A primary agent must attempt to match the request to a workflow whenever any listed workflow plausibly applies, then follow that workflow as the facilitator and coordinator instead of improvising a parallel process.

When coordinating a selected workflow, the primary agent also takes the Product Manager role by default: clarify the user's goal, ask necessary product and scope questions, maintain the workflow state, assign subagents to stage roles, validate their outputs, and consolidate the result for the user.

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Extract the user's task, likely workflow type, domain, constraints, and requested output.
3. Match the request against the workflow entries below by task first, then role, category, and tags.
4. If one or more workflows plausibly match, select the best fit, read only its guide and manifest, and proceed as that workflow's coordinator.
5. If no workflow plausibly matches, state that no workflow applies and continue with ordinary task handling.
6. Load role prompts from `../roles/<role-id>.md` only when the selected workflow stage needs those roles.
7. Let selected roles route to skills through `../skills/skills.md` and `../skills/catalog/roles/<role-id>/skills.md`.
8. Let selected roles or workflow stages route to MCP through `../mcp/mcp.md` only when the task directly needs an external service, data source, or tool integration.

Do not browse workflow directories broadly. Read the smallest matching workflow guide, role files, and capability indexes needed for the current request.

## Subagent Boundary

Subagents must not select their own workflow or role. A subagent must follow the workflow id, stage id, role id, task, expected outputs, acceptance criteria, and handoff instructions assigned by the primary agent.

A subagent may route to skills and MCP only inside its assigned role and task scope. It may not restart top-level routing, replace the selected workflow, promote itself to coordinator, or choose a different role unless the primary agent explicitly reassigns it.

## Generated Catalogs

Generated narrow indexes may exist under these paths:

- `workflows/catalog/tasks/<task-id>/workflows.md`
- `workflows/catalog/roles/<role-id>/workflows.md`
- `workflows/catalog/categories/<category>/workflows.md`
- `workflows/catalog/tags/<tag>/workflows.md`

Use a catalog index when it gives a smaller route-specific view than this dispatcher. The workflow manifest remains the source for stage order, roles, outputs, gates, and acceptance criteria.

## Coordination Rules

When a workflow is selected:

1. Summarize the user's request in concise bullets.
2. Assume the Product Manager coordinator posture unless the selected workflow says otherwise.
3. Ask only clarification questions required to select, scope, or start the workflow.
4. Read the selected workflow manifest.
5. Execute stages in manifest order unless the manifest explicitly allows skipping.
6. Run roles inside the same stage in parallel when inputs are ready.
7. Give each subagent the user request, workflow id, stage id, assigned role id, relevant previous outputs, expected outputs, acceptance criteria, and required output format.
8. Validate outputs against the stage acceptance criteria before moving to the next stage.
9. Request targeted revisions when outputs are incomplete, contradictory, or based on hidden assumptions.
10. Resolve role conflicts through the manifest's conflict resolution mapping.
11. Produce a consolidated final result for the user without exposing internal agent chatter unless requested.

## Quality Gates

Do not proceed to the next stage when required outputs are missing, critical assumptions are hidden, user-facing requirements are unclear, technical plans contradict product requirements, QA cannot derive test cases from the spec, or release planning lacks rollback guidance when release is in scope.

## Workflows

### SaaS From Scratch Workflow

Coordinate discovery, design, architecture, development planning, QA, release, and iteration for a new SaaS product.

**ID:** `saas-from-scratch`
**Guide:** `workflows/product-delivery/saas-from-scratch/workflow.md`
**Manifest:** `workflows/product-delivery/saas-from-scratch/workflow.yaml`
**Categories:** `product-delivery`
**Tags:** `saas`, `new-product`, `product-discovery`, `architecture`, `release`

### SaaS From Scratch Workflow Task IDs

`plan-feature`, `build-frontend`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`

### SaaS From Scratch Workflow Role IDs

`product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`

### Mobile App Workflow

Coordinate product, platform UX, mobile architecture, development planning, QA, store release, and iteration for mobile apps.

**ID:** `mobile-app`
**Guide:** `workflows/product-delivery/mobile-app/workflow.md`
**Manifest:** `workflows/product-delivery/mobile-app/workflow.yaml`
**Categories:** `product-delivery`, `mobile`
**Tags:** `mobile`, `ios`, `android`, `app-store`, `offline`, `push-notifications`

### Mobile App Workflow Task IDs

`plan-feature`, `build-mobile-desktop`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`

### Mobile App Workflow Role IDs

`product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `mobile-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`

### Feature Development Workflow

Coordinate scoped discovery, UX fit, architecture review, implementation planning, regression testing, rollout, and iteration for an existing product feature.

**ID:** `feature-development`
**Guide:** `workflows/product-delivery/feature-development/workflow.md`
**Manifest:** `workflows/product-delivery/feature-development/workflow.yaml`
**Categories:** `product-delivery`, `engineering`
**Tags:** `feature`, `existing-product`, `regression`, `feature-flags`, `architecture-review`

### Feature Development Workflow Task IDs

`plan-feature`, `implement-code`, `review-code`, `build-frontend`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`

### Feature Development Workflow Role IDs

`product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`

All other roles and tasks have no workflow unless another registry entry adds one.
