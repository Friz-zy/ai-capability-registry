# Workflow Capability Routing

Read `../capability-routing.md`, `workflow.md`, and `../roles/orchestrator.md` before selecting a workflow.

Use this file only for primary-agent workflow selection when no workflow scope is assigned.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Match by task first, then role, category, and tags.
3. Read only the selected workflow markdown guide and YAML manifest.
4. If no workflow applies, state that and continue with ordinary task handling.

Do not browse workflow directories broadly. Use the smallest matching index, then read only the selected workflow guide and manifest.

Generated narrow indexes may exist under these paths:

- `workflows/catalog/tasks/<task-id>/workflows.md`
- `workflows/catalog/roles/<role-id>/workflows.md`
- `workflows/catalog/categories/<category>/workflows.md`
- `workflows/catalog/tags/<tag>/workflows.md`

Use a catalog index when it gives a narrower view than this dispatcher. The manifest remains the source for stage order, roles, outputs, gates, and acceptance criteria.

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
