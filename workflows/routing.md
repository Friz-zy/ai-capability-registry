# Workflow Capability Routing

Read `../capability-routing.md`, `workflow.md`, and `../roles/orchestrator.md` before selecting a workflow.

Use this file only for primary-agent workflow selection when no workflow scope is assigned.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Match by task first, then role, category, and tags.
3. Read only the selected workflow markdown guide and YAML manifest.
4. If no workflow applies, state that and follow the no-workflow fallback in `workflow.md`.

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

`product-manager`, `business-analyst`, `ux-ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `release-manager`, `customer-success-support`

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

`product-manager`, `business-analyst`, `ux-ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `mobile-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `release-manager`, `customer-success-support`

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

`product-manager`, `business-analyst`, `ux-ui-designer`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `release-manager`, `customer-success-support`

### Idea Validation Workflow

Coordinate pre-development validation of problem, audience, market signals, value proposition, pricing hypothesis, MVP scope, and go/no-go decision.

**ID:** `idea-validation`
**Guide:** `workflows/product-discovery/idea-validation/workflow.md`
**Manifest:** `workflows/product-discovery/idea-validation/workflow.yaml`
**Categories:** `product-discovery`, `business`
**Tags:** `idea`, `validation`, `market-research`, `mvp`, `go-no-go`

### Idea Validation Workflow Task IDs

`validate-idea`, `research-brief`, `manage-project`

### Idea Validation Workflow Role IDs

`founder-ceo`, `product-manager`, `market-researcher`, `business-analyst`, `finance-manager`, `ux-researcher`

### Product Strategy Workflow

Coordinate product vision, positioning, north-star metric, roadmap direction, monetization model, strategic risks, and product principles.

**ID:** `product-strategy`
**Guide:** `workflows/product-discovery/product-strategy/workflow.md`
**Manifest:** `workflows/product-discovery/product-strategy/workflow.yaml`
**Categories:** `product-discovery`, `business`
**Tags:** `strategy`, `vision`, `roadmap`, `positioning`, `north-star-metric`

### Product Strategy Workflow Task IDs

`define-product-strategy`, `validate-idea`, `manage-project`

### Product Strategy Workflow Role IDs

`product-strategist`, `product-manager`, `founder-ceo`, `solution-architect`, `finance-manager`, `market-researcher`

### Pricing And Monetization Workflow

Coordinate pricing tiers, unit economics, free trial or freemium rules, limits, quotas, and revenue forecast.

**ID:** `pricing-and-monetization`
**Guide:** `workflows/business-growth/pricing-and-monetization/workflow.md`
**Manifest:** `workflows/business-growth/pricing-and-monetization/workflow.yaml`
**Categories:** `business-growth`, `product`
**Tags:** `pricing`, `monetization`, `unit-economics`, `freemium`, `revenue`

### Pricing And Monetization Workflow Task IDs

`design-pricing`, `finance-legal`, `manage-project`

### Pricing And Monetization Workflow Role IDs

`product-manager`, `finance-manager`, `growth-marketer`, `sales-strategist`, `compliance-officer`

### Go To Market Workflow

Coordinate launch plan, messaging, landing page brief, sales materials, onboarding flow, support readiness, and launch checklist.

**ID:** `go-to-market`
**Guide:** `workflows/business-growth/go-to-market/workflow.md`
**Manifest:** `workflows/business-growth/go-to-market/workflow.yaml`
**Categories:** `business-growth`, `product-launch`
**Tags:** `gtm`, `launch`, `messaging`, `sales-enablement`, `onboarding`

### Go To Market Workflow Task IDs

`plan-launch`, `customer-sales`, `write-documents`, `deploy-release`

### Go To Market Workflow Role IDs

`product-manager`, `product-marketing-manager`, `growth-marketer`, `sales-strategist`, `customer-success-support`, `technical-writer`, `release-manager`

### Bugfix Workflow

Coordinate defect triage, reproduction, root cause, fix plan, regression checklist, and hotfix or normal release decision.

**ID:** `bugfix`
**Guide:** `workflows/engineering/bugfix/workflow.md`
**Manifest:** `workflows/engineering/bugfix/workflow.yaml`
**Categories:** `engineering`, `product-delivery`
**Tags:** `bugfix`, `defect`, `regression`, `root-cause`, `hotfix`

### Bugfix Workflow Task IDs

`triage-bug`, `debug-incident`, `test-validate`, `deploy-release`

### Bugfix Workflow Role IDs

`customer-success-support`, `qa-engineer`, `product-manager`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `release-manager`, `devops-platform-engineer`

### Technical Debt Refactoring Workflow

Coordinate debt inventory, risk analysis, behavior-preserving refactoring plan, affected modules, test strategy, and rollback plan.

**ID:** `technical-debt-refactoring`
**Guide:** `workflows/engineering/technical-debt-refactoring/workflow.md`
**Manifest:** `workflows/engineering/technical-debt-refactoring/workflow.yaml`
**Categories:** `engineering`
**Tags:** `technical-debt`, `refactoring`, `modernization`, `maintainability`, `regression`

### Technical Debt Refactoring Workflow Task IDs

`reduce-technical-debt`, `implement-code`, `test-validate`, `deploy-release`

### Technical Debt Refactoring Workflow Role IDs

`tech-lead`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `data-engineer`, `devops-platform-engineer`, `qa-engineer`, `release-manager`, `product-manager`

### API Design Workflow

Coordinate OpenAPI contract, auth model, error model, pagination and filtering rules, versioning strategy, and SDK/client notes.

**ID:** `api-design`
**Guide:** `workflows/engineering/api-design/workflow.md`
**Manifest:** `workflows/engineering/api-design/workflow.yaml`
**Categories:** `engineering`, `architecture`
**Tags:** `api`, `openapi`, `contract`, `auth`, `versioning`

### API Design Workflow Task IDs

`design-api`, `build-backend`, `write-documents`, `security-audit`

### API Design Workflow Role IDs

`product-manager`, `business-analyst`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `security-engineer`, `qa-engineer`, `technical-writer`

### Integration Development Workflow

Coordinate external integration requirements, data mapping, API contract, auth and secrets model, failure handling, retry, and idempotency rules.

**ID:** `integration-development`
**Guide:** `workflows/engineering/integration-development/workflow.md`
**Manifest:** `workflows/engineering/integration-development/workflow.yaml`
**Categories:** `engineering`, `integration`
**Tags:** `integration`, `external-api`, `data-mapping`, `idempotency`, `secrets`

### Integration Development Workflow Task IDs

`develop-integration`, `build-backend`, `security-audit`, `test-validate`, `deploy-release`

### Integration Development Workflow Role IDs

`business-analyst`, `product-manager`, `solution-architect`, `backend-engineer`, `security-engineer`, `qa-engineer`, `devops-platform-engineer`, `release-manager`, `customer-success-support`

### Architecture Review Workflow

Coordinate architecture review, ADR inputs, C4 notes, risk matrix, scalability notes, security notes, and cost estimate.

**ID:** `architecture-review`
**Guide:** `workflows/architecture/architecture-review/workflow.md`
**Manifest:** `workflows/architecture/architecture-review/workflow.yaml`
**Categories:** `architecture`, `engineering`
**Tags:** `architecture-review`, `adr`, `c4`, `scalability`, `cost`

### Architecture Review Workflow Task IDs

`review-architecture`, `review-code`, `manage-project`

### Architecture Review Workflow Role IDs

`solution-architect`, `tech-lead`, `product-manager`, `security-engineer`, `devops-platform-engineer`, `data-engineer`, `release-manager`

### ADR Decision Workflow

Coordinate technical decision context, options, pros and cons, decision, consequences, migration plan, and ADR summary.

**ID:** `adr-decision`
**Guide:** `workflows/architecture/adr-decision/workflow.md`
**Manifest:** `workflows/architecture/adr-decision/workflow.yaml`
**Categories:** `architecture`, `engineering`
**Tags:** `adr`, `decision`, `tradeoffs`, `migration`, `technical-decision`

### ADR Decision Workflow Task IDs

`write-adr`, `review-architecture`, `write-documents`

### ADR Decision Workflow Role IDs

`tech-lead`, `solution-architect`, `product-manager`, `backend-engineer`, `devops-platform-engineer`, `security-engineer`, `release-manager`

### Infrastructure Provisioning Workflow

Coordinate Terraform/OpenTofu modules, environment plan, network plan, IAM model, CI/CD plan, observability, and cost estimate.

**ID:** `infrastructure-provisioning`
**Guide:** `workflows/platform-operations/infrastructure-provisioning/workflow.md`
**Manifest:** `workflows/platform-operations/infrastructure-provisioning/workflow.yaml`
**Categories:** `platform-operations`, `infrastructure`
**Tags:** `infrastructure`, `terraform`, `opentofu`, `iam`, `ci-cd`

### Infrastructure Provisioning Workflow Task IDs

`provision-infrastructure`, `manage-cloud-infra`, `deploy-release`

### Infrastructure Provisioning Workflow Role IDs

`devops-platform-engineer`, `sre`, `security-engineer`, `finops-analyst`, `qa-engineer`, `release-manager`

### Platform Engineering Workflow

Coordinate internal developer platform design, golden paths, service templates, CI/CD templates, developer portal, observability defaults, and documentation.

**ID:** `platform-engineering`
**Guide:** `workflows/platform-operations/platform-engineering/workflow.md`
**Manifest:** `workflows/platform-operations/platform-engineering/workflow.yaml`
**Categories:** `platform-operations`, `developer-experience`
**Tags:** `platform`, `golden-path`, `service-template`, `developer-portal`, `observability`

### Platform Engineering Workflow Task IDs

`engineer-platform`, `manage-cloud-infra`, `write-documents`

### Platform Engineering Workflow Role IDs

`devops-platform-engineer`, `engineering-manager`, `tech-lead`, `security-engineer`, `sre`, `technical-writer`, `business-analyst`, `customer-success-support`

### Security Review Workflow

Coordinate threat/security checklist, secrets review, dependency scan report, authn/authz review, vulnerability report, and remediation plan.

**ID:** `security-review`
**Guide:** `workflows/security-compliance/security-review/workflow.md`
**Manifest:** `workflows/security-compliance/security-review/workflow.yaml`
**Categories:** `security-compliance`, `engineering`
**Tags:** `security`, `appsec`, `secrets`, `dependencies`, `authz`

### Security Review Workflow Task IDs

`review-security`, `security-audit`, `review-code`

### Security Review Workflow Role IDs

`security-engineer`, `security-architect`, `solution-architect`, `product-manager`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `compliance-officer`, `tech-lead`, `release-manager`, `qa-engineer`

### Threat Modeling Workflow

Coordinate assets, actors, trust boundaries, threat list, attack paths, mitigations, residual risks, and validation plan.

**ID:** `threat-modeling`
**Guide:** `workflows/security-compliance/threat-modeling/workflow.md`
**Manifest:** `workflows/security-compliance/threat-modeling/workflow.yaml`
**Categories:** `security-compliance`, `architecture`
**Tags:** `threat-modeling`, `trust-boundaries`, `attack-paths`, `mitigations`, `security-design`

### Threat Modeling Workflow Task IDs

`model-threats`, `security-audit`, `review-architecture`

### Threat Modeling Workflow Role IDs

`security-architect`, `solution-architect`, `product-manager`, `security-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `tech-lead`

### Legal Compliance Workflow

Coordinate GDPR checklist, privacy policy notes, data processing map, ToS requirements, compliance risks, and action plan.

**ID:** `legal-compliance`
**Guide:** `workflows/security-compliance/legal-compliance/workflow.md`
**Manifest:** `workflows/security-compliance/legal-compliance/workflow.yaml`
**Categories:** `security-compliance`, `business-operations`
**Tags:** `legal`, `compliance`, `privacy`, `gdpr`, `terms`

### Legal Compliance Workflow Task IDs

`review-compliance`, `finance-legal`, `security-audit`

### Legal Compliance Workflow Role IDs

`compliance-officer`, `data-protection-officer`, `product-manager`, `security-engineer`, `finance-manager`, `technical-writer`, `release-manager`

### Test Planning Workflow

Coordinate test strategy, test cases, regression scope, automation scope, acceptance criteria, and quality gates.

**ID:** `test-planning`
**Guide:** `workflows/quality/test-planning/workflow.md`
**Manifest:** `workflows/quality/test-planning/workflow.yaml`
**Categories:** `quality`, `engineering`
**Tags:** `qa`, `test-plan`, `acceptance-criteria`, `regression`, `quality-gates`

### Test Planning Workflow Task IDs

`plan-tests`, `test-validate`

### Test Planning Workflow Role IDs

`qa-engineer`, `product-manager`, `tech-lead`, `devops-platform-engineer`

### Automated Testing Workflow

Coordinate unit, integration, and e2e test plans, CI test pipeline, flaky-test policy, reporting, and maintenance plan.

**ID:** `automated-testing`
**Guide:** `workflows/quality/automated-testing/workflow.md`
**Manifest:** `workflows/quality/automated-testing/workflow.yaml`
**Categories:** `quality`, `engineering`
**Tags:** `automated-tests`, `unit-tests`, `integration-tests`, `e2e`, `ci`

### Automated Testing Workflow Task IDs

`automate-tests`, `test-validate`, `implement-code`

### Automated Testing Workflow Role IDs

`qa-engineer`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`

### Performance Testing Workflow

Coordinate load profile, performance scenarios, bottleneck report, capacity estimate, optimization plan, and rollout safeguards.

**ID:** `performance-testing`
**Guide:** `workflows/quality/performance-testing/workflow.md`
**Manifest:** `workflows/quality/performance-testing/workflow.yaml`
**Categories:** `quality`, `reliability`
**Tags:** `performance`, `load-test`, `capacity`, `bottleneck`, `optimization`

### Performance Testing Workflow Task IDs

`test-performance`, `test-validate`, `analyze-data`

### Performance Testing Workflow Role IDs

`sre`, `product-manager`, `backend-engineer`, `data-engineer`, `devops-platform-engineer`, `tech-lead`, `qa-engineer`

### Incident Response Workflow

Coordinate incident timeline, impact analysis, mitigation actions, customer communication, recovery validation, and follow-up tasks.

**ID:** `incident-response`
**Guide:** `workflows/operations/incident-response/workflow.md`
**Manifest:** `workflows/operations/incident-response/workflow.yaml`
**Categories:** `operations`, `reliability`
**Tags:** `incident`, `outage`, `mitigation`, `customer-communication`, `recovery`

### Incident Response Workflow Task IDs

`respond-incident`, `debug-incident`, `deploy-release`

### Incident Response Workflow Role IDs

`incident-manager`, `sre`, `customer-success-support`, `product-manager`, `devops-platform-engineer`, `backend-engineer`, `qa-engineer`, `release-manager`, `engineering-manager`

### Postmortem Workflow

Coordinate what happened, why it happened, detection gap, prevention actions, owner per action, and deadline per action.

**ID:** `postmortem`
**Guide:** `workflows/operations/postmortem/workflow.md`
**Manifest:** `workflows/operations/postmortem/workflow.yaml`
**Categories:** `operations`, `reliability`
**Tags:** `postmortem`, `incident-review`, `root-cause`, `prevention`, `follow-up`

### Postmortem Workflow Task IDs

`write-postmortem`, `debug-incident`, `write-documents`

### Postmortem Workflow Role IDs

`incident-manager`, `sre`, `customer-success-support`, `tech-lead`, `backend-engineer`, `devops-platform-engineer`, `product-manager`, `engineering-manager`

### Customer Support Workflow

Coordinate ticket classification, user impact, workaround, escalation, and bug or feature request routing.

**ID:** `customer-support`
**Guide:** `workflows/customer-success/customer-support/workflow.md`
**Manifest:** `workflows/customer-success/customer-support/workflow.yaml`
**Categories:** `customer-success`, `operations`
**Tags:** `support`, `ticket`, `workaround`, `escalation`, `customer-impact`

### Customer Support Workflow Task IDs

`support-customer`, `customer-sales`, `triage-bug`

### Customer Support Workflow Role IDs

`customer-success-support`, `product-manager`, `qa-engineer`, `tech-lead`, `technical-writer`

### Customer Feedback Analysis Workflow

Coordinate feedback clusters, pain points, feature requests, churn risks, roadmap inputs, and follow-up research.

**ID:** `customer-feedback-analysis`
**Guide:** `workflows/customer-success/customer-feedback-analysis/workflow.md`
**Manifest:** `workflows/customer-success/customer-feedback-analysis/workflow.yaml`
**Categories:** `customer-success`, `product`
**Tags:** `feedback`, `customer-insights`, `churn`, `roadmap`, `feature-requests`

### Customer Feedback Analysis Workflow Task IDs

`analyze-feedback`, `customer-sales`, `analyze-data`

### Customer Feedback Analysis Workflow Role IDs

`customer-success-support`, `product-manager`, `business-analyst`, `ux-researcher`

### Analytics And Growth Workflow

Coordinate funnel analysis, retention report, cohort analysis, growth experiments, A/B test plan, and instrumentation gaps.

**ID:** `analytics-and-growth`
**Guide:** `workflows/business-growth/analytics-and-growth/workflow.md`
**Manifest:** `workflows/business-growth/analytics-and-growth/workflow.yaml`
**Categories:** `business-growth`, `product-analytics`
**Tags:** `analytics`, `growth`, `funnel`, `retention`, `ab-test`

### Analytics And Growth Workflow Task IDs

`analyze-growth`, `analyze-data`, `manage-project`

### Analytics And Growth Workflow Role IDs

`product-manager`, `business-analyst`, `growth-marketer`, `ux-researcher`, `tech-lead`

### Sales Support Workflow

Coordinate sales deck, demo script, objection handling, technical FAQ, proposal template, and risk review.

**ID:** `sales-support`
**Guide:** `workflows/business-growth/sales-support/workflow.md`
**Manifest:** `workflows/business-growth/sales-support/workflow.yaml`
**Categories:** `business-growth`, `sales`
**Tags:** `sales`, `b2b`, `demo`, `objections`, `proposal`

### Sales Support Workflow Task IDs

`support-sales`, `customer-sales`, `write-documents`

### Sales Support Workflow Role IDs

`sales-strategist`, `product-manager`, `technical-writer`, `compliance-officer`, `security-engineer`

### Technical Documentation Workflow

Coordinate README, API docs, architecture docs, deployment guide, troubleshooting guide, review, and publication notes.

**ID:** `technical-documentation`
**Guide:** `workflows/documentation/technical-documentation/workflow.md`
**Manifest:** `workflows/documentation/technical-documentation/workflow.yaml`
**Categories:** `documentation`, `engineering`
**Tags:** `docs`, `technical-docs`, `api-docs`, `readme`, `troubleshooting`

### Technical Documentation Workflow Task IDs

`write-technical-docs`, `write-documents`, `design-api`

### Technical Documentation Workflow Role IDs

`technical-writer`, `product-manager`, `tech-lead`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `qa-engineer`

### User Documentation Workflow

Coordinate help center article, onboarding guide, FAQ, how-to guides, release notes, support review, and publication notes.

**ID:** `user-documentation`
**Guide:** `workflows/documentation/user-documentation/workflow.md`
**Manifest:** `workflows/documentation/user-documentation/workflow.yaml`
**Categories:** `documentation`, `customer-success`
**Tags:** `user-docs`, `help-center`, `faq`, `onboarding`, `release-notes`

### User Documentation Workflow Task IDs

`write-user-docs`, `write-documents`, `customer-sales`

### User Documentation Workflow Role IDs

`technical-writer`, `product-manager`, `ux-ui-designer`, `customer-success-support`, `release-manager`

### Knowledge Base Maintenance Workflow

Coordinate knowledge articles, decision logs, runbooks, onboarding docs, deprecated docs list, governance, and maintenance cadence.

**ID:** `knowledge-base-maintenance`
**Guide:** `workflows/documentation/knowledge-base-maintenance/workflow.md`
**Manifest:** `workflows/documentation/knowledge-base-maintenance/workflow.yaml`
**Categories:** `documentation`, `knowledge-management`
**Tags:** `knowledge-base`, `runbooks`, `decision-logs`, `onboarding-docs`, `deprecation`

### Knowledge Base Maintenance Workflow Task IDs

`maintain-knowledge-base`, `write-documents`, `manage-project`

### Knowledge Base Maintenance Workflow Role IDs

`technical-writer`, `customer-success-support`, `tech-lead`, `product-manager`, `engineering-manager`

### FinOps Cost Optimization Workflow

Coordinate cost breakdown, unused resources list, rightsizing plan, reserved or savings plan recommendation, and cost guardrails.

**ID:** `finops-cost-optimization`
**Guide:** `workflows/business-operations/finops-cost-optimization/workflow.md`
**Manifest:** `workflows/business-operations/finops-cost-optimization/workflow.yaml`
**Categories:** `business-operations`, `finops`
**Tags:** `finops`, `cost-optimization`, `cloud-cost`, `rightsizing`, `savings-plan`

### FinOps Cost Optimization Workflow Task IDs

`optimize-costs`, `finance-legal`, `manage-cloud-infra`

### FinOps Cost Optimization Workflow Role IDs

`finops-analyst`, `finance-manager`, `product-manager`, `sre`, `devops-platform-engineer`, `solution-architect`, `engineering-manager`

### Vendor Selection Workflow

Coordinate requirements, comparison matrix, risks, cost model, recommendation, fallback option, and approval needs.

**ID:** `vendor-selection`
**Guide:** `workflows/business-operations/vendor-selection/workflow.md`
**Manifest:** `workflows/business-operations/vendor-selection/workflow.yaml`
**Categories:** `business-operations`, `procurement`
**Tags:** `vendor`, `procurement`, `comparison`, `cost-model`, `fallback`

### Vendor Selection Workflow Task IDs

`select-vendor`, `finance-legal`, `research-brief`

### Vendor Selection Workflow Role IDs

`operations-manager`, `product-manager`, `tech-lead`, `finance-manager`, `security-engineer`, `compliance-officer`, `release-manager`

### Hiring Workflow

Coordinate role description, candidate scorecard, interview plan, test task, sourcing plan, and hiring recommendation.

**ID:** `hiring`
**Guide:** `workflows/people-operations/hiring/workflow.md`
**Manifest:** `workflows/people-operations/hiring/workflow.yaml`
**Categories:** `people-operations`, `management`
**Tags:** `hiring`, `recruiting`, `interview`, `scorecard`, `test-task`

### Hiring Workflow Task IDs

`plan-hiring`, `people-ops`

### Hiring Workflow Role IDs

`engineering-manager`, `tech-lead`, `hr-manager`, `finance-manager`

### Team Process Improvement Workflow

Coordinate process pain points, bottlenecks, working agreements, delivery metrics, improvement plan, and review cadence.

**ID:** `team-process-improvement`
**Guide:** `workflows/people-operations/team-process-improvement/workflow.md`
**Manifest:** `workflows/people-operations/team-process-improvement/workflow.yaml`
**Categories:** `people-operations`, `management`
**Tags:** `process-improvement`, `delivery`, `working-agreements`, `metrics`, `team-health`

### Team Process Improvement Workflow Task IDs

`improve-team-process`, `people-ops`, `manage-project`

### Team Process Improvement Workflow Role IDs

`engineering-manager`, `release-manager`, `tech-lead`, `qa-engineer`, `product-manager`

All other roles and tasks have no workflow unless another registry entry adds one.
