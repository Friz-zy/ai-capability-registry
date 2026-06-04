# Workflow Catalog

Generated human-readable view. Edit source configuration in `registry/workflows.yaml`.

Total: 34 workflows across 27 categories

## Architecture

### ADR Decision Workflow
Coordinate technical decision context, options, pros and cons, decision, consequences, migration plan, and ADR summary.

**ID:** `adr-decision`
**Categories:** `architecture`, `engineering`
**Tags:** `adr`, `decision`, `tradeoffs`, `migration`, `technical-decision`
**Task IDs:** `write-adr`, `review-architecture`, `write-documents`
**Role IDs:** `tech-lead`, `solution-architect`, `product-manager`, `backend-engineer`, `devops-platform-engineer`, `security-engineer`, `release-manager`
**Guide:** `workflows/architecture/adr-decision/workflow.md`
**Manifest:** `workflows/architecture/adr-decision/workflow.yaml`

### API Design Workflow
Coordinate OpenAPI contract, auth model, error model, pagination and filtering rules, versioning strategy, and SDK/client notes.

**ID:** `api-design`
**Categories:** `engineering`, `architecture`
**Tags:** `api`, `openapi`, `contract`, `auth`, `versioning`
**Task IDs:** `design-api`, `build-backend`, `write-documents`, `security-audit`
**Role IDs:** `product-manager`, `business-analyst`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `security-engineer`, `qa-engineer`, `sdet`, `technical-writer`
**Guide:** `workflows/engineering/api-design/workflow.md`
**Manifest:** `workflows/engineering/api-design/workflow.yaml`

### Architecture Review Workflow
Coordinate architecture review, ADR inputs, C4 notes, risk matrix, scalability notes, security notes, and cost estimate.

**ID:** `architecture-review`
**Categories:** `architecture`, `engineering`
**Tags:** `architecture-review`, `adr`, `c4`, `scalability`, `cost`
**Task IDs:** `review-architecture`, `review-code`, `manage-project`
**Role IDs:** `solution-architect`, `tech-lead`, `product-manager`, `security-engineer`, `devops-platform-engineer`, `database-engineer`, `cloud-architect`, `release-manager`
**Guide:** `workflows/architecture/architecture-review/workflow.md`
**Manifest:** `workflows/architecture/architecture-review/workflow.yaml`

### Threat Modeling Workflow
Coordinate assets, actors, trust boundaries, threat list, attack paths, mitigations, residual risks, and validation plan.

**ID:** `threat-modeling`
**Categories:** `security-compliance`, `architecture`
**Tags:** `threat-modeling`, `trust-boundaries`, `attack-paths`, `mitigations`, `security-design`
**Task IDs:** `model-threats`, `security-audit`, `review-architecture`
**Role IDs:** `security-architect`, `solution-architect`, `product-manager`, `security-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `tech-lead`
**Guide:** `workflows/security-compliance/threat-modeling/workflow.md`
**Manifest:** `workflows/security-compliance/threat-modeling/workflow.yaml`

## Business

### Idea Validation Workflow
Coordinate pre-development validation of problem, audience, market signals, value proposition, pricing hypothesis, MVP scope, and go/no-go decision.

**ID:** `idea-validation`
**Categories:** `product-discovery`, `business`
**Tags:** `idea`, `validation`, `market-research`, `mvp`, `go-no-go`
**Task IDs:** `validate-idea`, `research-brief`, `manage-project`
**Role IDs:** `founder-business-owner`, `product-manager`, `market-researcher`, `business-analyst`, `finance-manager`, `ux-researcher`, `product-analyst`
**Guide:** `workflows/product-discovery/idea-validation/workflow.md`
**Manifest:** `workflows/product-discovery/idea-validation/workflow.yaml`

### Product Strategy Workflow
Coordinate product vision, positioning, north-star metric, roadmap direction, monetization model, strategic risks, and product principles.

**ID:** `product-strategy`
**Categories:** `product-discovery`, `business`
**Tags:** `strategy`, `vision`, `roadmap`, `positioning`, `north-star-metric`
**Task IDs:** `define-product-strategy`, `validate-idea`, `manage-project`
**Role IDs:** `product-strategist`, `product-manager`, `founder-business-owner`, `solution-architect`, `finance-manager`, `market-researcher`
**Guide:** `workflows/product-discovery/product-strategy/workflow.md`
**Manifest:** `workflows/product-discovery/product-strategy/workflow.yaml`

## Business Growth

### Analytics And Growth Workflow
Coordinate funnel analysis, retention report, cohort analysis, growth experiments, A/B test plan, and instrumentation gaps.

**ID:** `analytics-and-growth`
**Categories:** `business-growth`, `product-analytics`
**Tags:** `analytics`, `growth`, `funnel`, `retention`, `ab-test`
**Task IDs:** `analyze-growth`, `analyze-data`, `manage-project`
**Role IDs:** `product-manager`, `product-analyst`, `growth-marketer`, `ux-researcher`, `tech-lead`
**Guide:** `workflows/business-growth/analytics-and-growth/workflow.md`
**Manifest:** `workflows/business-growth/analytics-and-growth/workflow.yaml`

### Go To Market Workflow
Coordinate launch plan, messaging, landing page brief, sales materials, onboarding flow, support readiness, and launch checklist.

**ID:** `go-to-market`
**Categories:** `business-growth`, `product-launch`
**Tags:** `gtm`, `launch`, `messaging`, `sales-enablement`, `onboarding`
**Task IDs:** `plan-launch`, `customer-sales`, `write-documents`, `deploy-release`
**Role IDs:** `product-manager`, `product-marketing-manager`, `growth-marketer`, `sales-strategist`, `content-marketer`, `customer-success-support`, `technical-writer`, `release-manager`
**Guide:** `workflows/business-growth/go-to-market/workflow.md`
**Manifest:** `workflows/business-growth/go-to-market/workflow.yaml`

### Pricing And Monetization Workflow
Coordinate pricing tiers, unit economics, free trial or freemium rules, limits, quotas, and revenue forecast.

**ID:** `pricing-and-monetization`
**Categories:** `business-growth`, `product`
**Tags:** `pricing`, `monetization`, `unit-economics`, `freemium`, `revenue`
**Task IDs:** `design-pricing`, `finance-legal`, `manage-project`
**Role IDs:** `product-manager`, `finance-manager`, `growth-marketer`, `sales-strategist`, `compliance-officer`
**Guide:** `workflows/business-growth/pricing-and-monetization/workflow.md`
**Manifest:** `workflows/business-growth/pricing-and-monetization/workflow.yaml`

### Sales Support Workflow
Coordinate sales deck, demo script, objection handling, technical FAQ, proposal template, and risk review.

**ID:** `sales-support`
**Categories:** `business-growth`, `sales`
**Tags:** `sales`, `b2b`, `demo`, `objections`, `proposal`
**Task IDs:** `support-sales`, `customer-sales`, `write-documents`
**Role IDs:** `sales-strategist`, `product-manager`, `solution-consultant`, `technical-writer`, `compliance-officer`, `security-engineer`
**Guide:** `workflows/business-growth/sales-support/workflow.md`
**Manifest:** `workflows/business-growth/sales-support/workflow.yaml`

## Business Operations

### FinOps Cost Optimization Workflow
Coordinate cost breakdown, unused resources list, rightsizing plan, reserved or savings plan recommendation, and cost guardrails.

**ID:** `finops-cost-optimization`
**Categories:** `business-operations`, `finops`
**Tags:** `finops`, `cost-optimization`, `cloud-cost`, `rightsizing`, `savings-plan`
**Task IDs:** `optimize-costs`, `finance-legal`, `manage-cloud-infra`
**Role IDs:** `finops-analyst`, `finance-manager`, `product-manager`, `sre`, `devops-platform-engineer`, `cloud-architect`, `engineering-manager`
**Guide:** `workflows/business-operations/finops-cost-optimization/workflow.md`
**Manifest:** `workflows/business-operations/finops-cost-optimization/workflow.yaml`

### Legal Compliance Workflow
Coordinate GDPR checklist, privacy policy notes, data processing map, ToS requirements, compliance risks, and action plan.

**ID:** `legal-compliance`
**Categories:** `security-compliance`, `business-operations`
**Tags:** `legal`, `compliance`, `privacy`, `gdpr`, `terms`
**Task IDs:** `review-compliance`, `finance-legal`, `security-audit`
**Role IDs:** `compliance-officer`, `data-protection-officer`, `product-manager`, `security-engineer`, `finance-manager`, `technical-writer`, `release-manager`
**Guide:** `workflows/security-compliance/legal-compliance/workflow.md`
**Manifest:** `workflows/security-compliance/legal-compliance/workflow.yaml`

### Vendor Selection Workflow
Coordinate requirements, comparison matrix, risks, cost model, recommendation, fallback option, and approval needs.

**ID:** `vendor-selection`
**Categories:** `business-operations`, `procurement`
**Tags:** `vendor`, `procurement`, `comparison`, `cost-model`, `fallback`
**Task IDs:** `select-vendor`, `finance-legal`, `research-brief`
**Role IDs:** `procurement-manager`, `product-manager`, `tech-lead`, `finance-manager`, `security-engineer`, `compliance-officer`, `release-manager`
**Guide:** `workflows/business-operations/vendor-selection/workflow.md`
**Manifest:** `workflows/business-operations/vendor-selection/workflow.yaml`

## Customer Success

### Customer Feedback Analysis Workflow
Coordinate feedback clusters, pain points, feature requests, churn risks, roadmap inputs, and follow-up research.

**ID:** `customer-feedback-analysis`
**Categories:** `customer-success`, `product`
**Tags:** `feedback`, `customer-insights`, `churn`, `roadmap`, `feature-requests`
**Task IDs:** `analyze-feedback`, `customer-sales`, `analyze-data`
**Role IDs:** `customer-success-support`, `product-manager`, `product-analyst`, `ux-researcher`
**Guide:** `workflows/customer-success/customer-feedback-analysis/workflow.md`
**Manifest:** `workflows/customer-success/customer-feedback-analysis/workflow.yaml`

### Customer Support Workflow
Coordinate ticket classification, user impact, workaround, escalation, and bug or feature request routing.

**ID:** `customer-support`
**Categories:** `customer-success`, `operations`
**Tags:** `support`, `ticket`, `workaround`, `escalation`, `customer-impact`
**Task IDs:** `support-customer`, `customer-sales`, `triage-bug`
**Role IDs:** `customer-success-support`, `product-manager`, `qa-engineer`, `tech-lead`, `technical-writer`
**Guide:** `workflows/customer-success/customer-support/workflow.md`
**Manifest:** `workflows/customer-success/customer-support/workflow.yaml`

### User Documentation Workflow
Coordinate help center article, onboarding guide, FAQ, how-to guides, release notes, support review, and publication notes.

**ID:** `user-documentation`
**Categories:** `documentation`, `customer-success`
**Tags:** `user-docs`, `help-center`, `faq`, `onboarding`, `release-notes`
**Task IDs:** `write-user-docs`, `write-documents`, `customer-sales`
**Role IDs:** `technical-writer`, `product-manager`, `ux-designer`, `customer-success-support`, `release-manager`
**Guide:** `workflows/documentation/user-documentation/workflow.md`
**Manifest:** `workflows/documentation/user-documentation/workflow.yaml`

## Developer Experience

### Platform Engineering Workflow
Coordinate internal developer platform design, golden paths, service templates, CI/CD templates, developer portal, observability defaults, and documentation.

**ID:** `platform-engineering`
**Categories:** `platform-operations`, `developer-experience`
**Tags:** `platform`, `golden-path`, `service-template`, `developer-portal`, `observability`
**Task IDs:** `engineer-platform`, `manage-cloud-infra`, `write-documents`
**Role IDs:** `devops-platform-engineer`, `engineering-manager`, `tech-lead`, `cloud-architect`, `security-engineer`, `sre`, `technical-writer`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/platform-operations/platform-engineering/workflow.md`
**Manifest:** `workflows/platform-operations/platform-engineering/workflow.yaml`

## Documentation

### Knowledge Base Maintenance Workflow
Coordinate knowledge articles, decision logs, runbooks, onboarding docs, deprecated docs list, governance, and maintenance cadence.

**ID:** `knowledge-base-maintenance`
**Categories:** `documentation`, `knowledge-management`
**Tags:** `knowledge-base`, `runbooks`, `decision-logs`, `onboarding-docs`, `deprecation`
**Task IDs:** `maintain-knowledge-base`, `write-documents`, `manage-project`
**Role IDs:** `knowledge-manager`, `technical-writer`, `customer-success-support`, `tech-lead`, `product-manager`, `engineering-manager`
**Guide:** `workflows/documentation/knowledge-base-maintenance/workflow.md`
**Manifest:** `workflows/documentation/knowledge-base-maintenance/workflow.yaml`

### Technical Documentation Workflow
Coordinate README, API docs, architecture docs, deployment guide, troubleshooting guide, review, and publication notes.

**ID:** `technical-documentation`
**Categories:** `documentation`, `engineering`
**Tags:** `docs`, `technical-docs`, `api-docs`, `readme`, `troubleshooting`
**Task IDs:** `write-technical-docs`, `write-documents`, `design-api`
**Role IDs:** `technical-writer`, `product-manager`, `tech-lead`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `qa-engineer`
**Guide:** `workflows/documentation/technical-documentation/workflow.md`
**Manifest:** `workflows/documentation/technical-documentation/workflow.yaml`

### User Documentation Workflow
Coordinate help center article, onboarding guide, FAQ, how-to guides, release notes, support review, and publication notes.

**ID:** `user-documentation`
**Categories:** `documentation`, `customer-success`
**Tags:** `user-docs`, `help-center`, `faq`, `onboarding`, `release-notes`
**Task IDs:** `write-user-docs`, `write-documents`, `customer-sales`
**Role IDs:** `technical-writer`, `product-manager`, `ux-designer`, `customer-success-support`, `release-manager`
**Guide:** `workflows/documentation/user-documentation/workflow.md`
**Manifest:** `workflows/documentation/user-documentation/workflow.yaml`

## Engineering

### ADR Decision Workflow
Coordinate technical decision context, options, pros and cons, decision, consequences, migration plan, and ADR summary.

**ID:** `adr-decision`
**Categories:** `architecture`, `engineering`
**Tags:** `adr`, `decision`, `tradeoffs`, `migration`, `technical-decision`
**Task IDs:** `write-adr`, `review-architecture`, `write-documents`
**Role IDs:** `tech-lead`, `solution-architect`, `product-manager`, `backend-engineer`, `devops-platform-engineer`, `security-engineer`, `release-manager`
**Guide:** `workflows/architecture/adr-decision/workflow.md`
**Manifest:** `workflows/architecture/adr-decision/workflow.yaml`

### API Design Workflow
Coordinate OpenAPI contract, auth model, error model, pagination and filtering rules, versioning strategy, and SDK/client notes.

**ID:** `api-design`
**Categories:** `engineering`, `architecture`
**Tags:** `api`, `openapi`, `contract`, `auth`, `versioning`
**Task IDs:** `design-api`, `build-backend`, `write-documents`, `security-audit`
**Role IDs:** `product-manager`, `business-analyst`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `security-engineer`, `qa-engineer`, `sdet`, `technical-writer`
**Guide:** `workflows/engineering/api-design/workflow.md`
**Manifest:** `workflows/engineering/api-design/workflow.yaml`

### Architecture Review Workflow
Coordinate architecture review, ADR inputs, C4 notes, risk matrix, scalability notes, security notes, and cost estimate.

**ID:** `architecture-review`
**Categories:** `architecture`, `engineering`
**Tags:** `architecture-review`, `adr`, `c4`, `scalability`, `cost`
**Task IDs:** `review-architecture`, `review-code`, `manage-project`
**Role IDs:** `solution-architect`, `tech-lead`, `product-manager`, `security-engineer`, `devops-platform-engineer`, `database-engineer`, `cloud-architect`, `release-manager`
**Guide:** `workflows/architecture/architecture-review/workflow.md`
**Manifest:** `workflows/architecture/architecture-review/workflow.yaml`

### Automated Testing Workflow
Coordinate unit, integration, and e2e test plans, CI test pipeline, flaky-test policy, reporting, and maintenance plan.

**ID:** `automated-testing`
**Categories:** `quality`, `engineering`
**Tags:** `automated-tests`, `unit-tests`, `integration-tests`, `e2e`, `ci`
**Task IDs:** `automate-tests`, `test-validate`, `implement-code`
**Role IDs:** `sdet`, `qa-engineer`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`
**Guide:** `workflows/quality/automated-testing/workflow.md`
**Manifest:** `workflows/quality/automated-testing/workflow.yaml`

### Bugfix Workflow
Coordinate defect triage, reproduction, root cause, fix plan, regression checklist, and hotfix or normal release decision.

**ID:** `bugfix`
**Categories:** `engineering`, `product-delivery`
**Tags:** `bugfix`, `defect`, `regression`, `root-cause`, `hotfix`
**Task IDs:** `triage-bug`, `debug-incident`, `test-validate`, `deploy-release`
**Role IDs:** `customer-success-support`, `qa-engineer`, `product-manager`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `sdet`, `release-manager`, `devops-platform-engineer`
**Guide:** `workflows/engineering/bugfix/workflow.md`
**Manifest:** `workflows/engineering/bugfix/workflow.yaml`

### Feature Development Workflow
Coordinate scoped discovery, UX fit, architecture review, implementation planning, regression testing, rollout, and iteration for an existing product feature.

**ID:** `feature-development`
**Categories:** `product-delivery`, `engineering`
**Tags:** `feature`, `existing-product`, `regression`, `feature-flags`, `architecture-review`
**Task IDs:** `plan-feature`, `implement-code`, `review-code`, `build-frontend`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`
**Role IDs:** `product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/product-delivery/feature-development/workflow.md`
**Manifest:** `workflows/product-delivery/feature-development/workflow.yaml`

### Integration Development Workflow
Coordinate external integration requirements, data mapping, API contract, auth and secrets model, failure handling, retry, and idempotency rules.

**ID:** `integration-development`
**Categories:** `engineering`, `integration`
**Tags:** `integration`, `external-api`, `data-mapping`, `idempotency`, `secrets`
**Task IDs:** `develop-integration`, `build-backend`, `security-audit`, `test-validate`, `deploy-release`
**Role IDs:** `business-analyst`, `product-manager`, `solution-architect`, `backend-engineer`, `security-engineer`, `qa-engineer`, `sdet`, `devops-platform-engineer`, `release-manager`, `customer-success-support`
**Guide:** `workflows/engineering/integration-development/workflow.md`
**Manifest:** `workflows/engineering/integration-development/workflow.yaml`

### Security Review Workflow
Coordinate threat/security checklist, secrets review, dependency scan report, authn/authz review, vulnerability report, and remediation plan.

**ID:** `security-review`
**Categories:** `security-compliance`, `engineering`
**Tags:** `security`, `appsec`, `secrets`, `dependencies`, `authz`
**Task IDs:** `review-security`, `security-audit`, `review-code`
**Role IDs:** `security-engineer`, `security-architect`, `solution-architect`, `product-manager`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `compliance-officer`, `tech-lead`, `release-manager`, `qa-engineer`
**Guide:** `workflows/security-compliance/security-review/workflow.md`
**Manifest:** `workflows/security-compliance/security-review/workflow.yaml`

### Technical Debt Refactoring Workflow
Coordinate debt inventory, risk analysis, behavior-preserving refactoring plan, affected modules, test strategy, and rollback plan.

**ID:** `technical-debt-refactoring`
**Categories:** `engineering`
**Tags:** `technical-debt`, `refactoring`, `modernization`, `maintainability`, `regression`
**Task IDs:** `reduce-technical-debt`, `implement-code`, `test-validate`, `deploy-release`
**Role IDs:** `tech-lead`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `database-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `performance-engineer`, `release-manager`, `product-manager`
**Guide:** `workflows/engineering/technical-debt-refactoring/workflow.md`
**Manifest:** `workflows/engineering/technical-debt-refactoring/workflow.yaml`

### Technical Documentation Workflow
Coordinate README, API docs, architecture docs, deployment guide, troubleshooting guide, review, and publication notes.

**ID:** `technical-documentation`
**Categories:** `documentation`, `engineering`
**Tags:** `docs`, `technical-docs`, `api-docs`, `readme`, `troubleshooting`
**Task IDs:** `write-technical-docs`, `write-documents`, `design-api`
**Role IDs:** `technical-writer`, `product-manager`, `tech-lead`, `solution-architect`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `qa-engineer`
**Guide:** `workflows/documentation/technical-documentation/workflow.md`
**Manifest:** `workflows/documentation/technical-documentation/workflow.yaml`

### Test Planning Workflow
Coordinate test strategy, test cases, regression scope, automation scope, acceptance criteria, and quality gates.

**ID:** `test-planning`
**Categories:** `quality`, `engineering`
**Tags:** `qa`, `test-plan`, `acceptance-criteria`, `regression`, `quality-gates`
**Task IDs:** `plan-tests`, `test-validate`
**Role IDs:** `qa-engineer`, `product-manager`, `tech-lead`, `sdet`, `devops-platform-engineer`
**Guide:** `workflows/quality/test-planning/workflow.md`
**Manifest:** `workflows/quality/test-planning/workflow.yaml`

## Finops

### FinOps Cost Optimization Workflow
Coordinate cost breakdown, unused resources list, rightsizing plan, reserved or savings plan recommendation, and cost guardrails.

**ID:** `finops-cost-optimization`
**Categories:** `business-operations`, `finops`
**Tags:** `finops`, `cost-optimization`, `cloud-cost`, `rightsizing`, `savings-plan`
**Task IDs:** `optimize-costs`, `finance-legal`, `manage-cloud-infra`
**Role IDs:** `finops-analyst`, `finance-manager`, `product-manager`, `sre`, `devops-platform-engineer`, `cloud-architect`, `engineering-manager`
**Guide:** `workflows/business-operations/finops-cost-optimization/workflow.md`
**Manifest:** `workflows/business-operations/finops-cost-optimization/workflow.yaml`

## Infrastructure

### Infrastructure Provisioning Workflow
Coordinate Terraform/OpenTofu modules, environment plan, network plan, IAM model, CI/CD plan, observability, and cost estimate.

**ID:** `infrastructure-provisioning`
**Categories:** `platform-operations`, `infrastructure`
**Tags:** `infrastructure`, `terraform`, `opentofu`, `iam`, `ci-cd`
**Task IDs:** `provision-infrastructure`, `manage-cloud-infra`, `deploy-release`
**Role IDs:** `cloud-architect`, `devops-platform-engineer`, `sre`, `security-engineer`, `finops-analyst`, `qa-engineer`, `release-manager`
**Guide:** `workflows/platform-operations/infrastructure-provisioning/workflow.md`
**Manifest:** `workflows/platform-operations/infrastructure-provisioning/workflow.yaml`

## Integration

### Integration Development Workflow
Coordinate external integration requirements, data mapping, API contract, auth and secrets model, failure handling, retry, and idempotency rules.

**ID:** `integration-development`
**Categories:** `engineering`, `integration`
**Tags:** `integration`, `external-api`, `data-mapping`, `idempotency`, `secrets`
**Task IDs:** `develop-integration`, `build-backend`, `security-audit`, `test-validate`, `deploy-release`
**Role IDs:** `business-analyst`, `product-manager`, `solution-architect`, `backend-engineer`, `security-engineer`, `qa-engineer`, `sdet`, `devops-platform-engineer`, `release-manager`, `customer-success-support`
**Guide:** `workflows/engineering/integration-development/workflow.md`
**Manifest:** `workflows/engineering/integration-development/workflow.yaml`

## Knowledge Management

### Knowledge Base Maintenance Workflow
Coordinate knowledge articles, decision logs, runbooks, onboarding docs, deprecated docs list, governance, and maintenance cadence.

**ID:** `knowledge-base-maintenance`
**Categories:** `documentation`, `knowledge-management`
**Tags:** `knowledge-base`, `runbooks`, `decision-logs`, `onboarding-docs`, `deprecation`
**Task IDs:** `maintain-knowledge-base`, `write-documents`, `manage-project`
**Role IDs:** `knowledge-manager`, `technical-writer`, `customer-success-support`, `tech-lead`, `product-manager`, `engineering-manager`
**Guide:** `workflows/documentation/knowledge-base-maintenance/workflow.md`
**Manifest:** `workflows/documentation/knowledge-base-maintenance/workflow.yaml`

## Management

### Hiring Workflow
Coordinate role description, candidate scorecard, interview plan, test task, sourcing plan, and hiring recommendation.

**ID:** `hiring`
**Categories:** `people-operations`, `management`
**Tags:** `hiring`, `recruiting`, `interview`, `scorecard`, `test-task`
**Task IDs:** `plan-hiring`, `people-ops`
**Role IDs:** `engineering-manager`, `tech-lead`, `hr-manager`, `finance-manager`, `recruiter`
**Guide:** `workflows/people-operations/hiring/workflow.md`
**Manifest:** `workflows/people-operations/hiring/workflow.yaml`

### Team Process Improvement Workflow
Coordinate process pain points, bottlenecks, working agreements, delivery metrics, improvement plan, and review cadence.

**ID:** `team-process-improvement`
**Categories:** `people-operations`, `management`
**Tags:** `process-improvement`, `delivery`, `working-agreements`, `metrics`, `team-health`
**Task IDs:** `improve-team-process`, `people-ops`, `manage-project`
**Role IDs:** `engineering-manager`, `release-manager`, `tech-lead`, `qa-engineer`, `product-manager`
**Guide:** `workflows/people-operations/team-process-improvement/workflow.md`
**Manifest:** `workflows/people-operations/team-process-improvement/workflow.yaml`

## Mobile

### Mobile App Workflow
Coordinate product, platform UX, mobile architecture, development planning, QA, store release, and iteration for mobile apps.

**ID:** `mobile-app`
**Categories:** `product-delivery`, `mobile`
**Tags:** `mobile`, `ios`, `android`, `app-store`, `offline`, `push-notifications`
**Task IDs:** `plan-feature`, `build-mobile-desktop`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`
**Role IDs:** `product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `mobile-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/product-delivery/mobile-app/workflow.md`
**Manifest:** `workflows/product-delivery/mobile-app/workflow.yaml`

## Operations

### Customer Support Workflow
Coordinate ticket classification, user impact, workaround, escalation, and bug or feature request routing.

**ID:** `customer-support`
**Categories:** `customer-success`, `operations`
**Tags:** `support`, `ticket`, `workaround`, `escalation`, `customer-impact`
**Task IDs:** `support-customer`, `customer-sales`, `triage-bug`
**Role IDs:** `customer-success-support`, `product-manager`, `qa-engineer`, `tech-lead`, `technical-writer`
**Guide:** `workflows/customer-success/customer-support/workflow.md`
**Manifest:** `workflows/customer-success/customer-support/workflow.yaml`

### Incident Response Workflow
Coordinate incident timeline, impact analysis, mitigation actions, customer communication, recovery validation, and follow-up tasks.

**ID:** `incident-response`
**Categories:** `operations`, `reliability`
**Tags:** `incident`, `outage`, `mitigation`, `customer-communication`, `recovery`
**Task IDs:** `respond-incident`, `debug-incident`, `deploy-release`
**Role IDs:** `incident-commander`, `sre`, `customer-success-support`, `product-manager`, `devops-platform-engineer`, `backend-engineer`, `qa-engineer`, `release-manager`, `engineering-manager`
**Guide:** `workflows/operations/incident-response/workflow.md`
**Manifest:** `workflows/operations/incident-response/workflow.yaml`

### Postmortem Workflow
Coordinate what happened, why it happened, detection gap, prevention actions, owner per action, and deadline per action.

**ID:** `postmortem`
**Categories:** `operations`, `reliability`
**Tags:** `postmortem`, `incident-review`, `root-cause`, `prevention`, `follow-up`
**Task IDs:** `write-postmortem`, `debug-incident`, `write-documents`
**Role IDs:** `incident-commander`, `sre`, `customer-success-support`, `tech-lead`, `backend-engineer`, `devops-platform-engineer`, `product-manager`, `engineering-manager`
**Guide:** `workflows/operations/postmortem/workflow.md`
**Manifest:** `workflows/operations/postmortem/workflow.yaml`

## People Operations

### Hiring Workflow
Coordinate role description, candidate scorecard, interview plan, test task, sourcing plan, and hiring recommendation.

**ID:** `hiring`
**Categories:** `people-operations`, `management`
**Tags:** `hiring`, `recruiting`, `interview`, `scorecard`, `test-task`
**Task IDs:** `plan-hiring`, `people-ops`
**Role IDs:** `engineering-manager`, `tech-lead`, `hr-manager`, `finance-manager`, `recruiter`
**Guide:** `workflows/people-operations/hiring/workflow.md`
**Manifest:** `workflows/people-operations/hiring/workflow.yaml`

### Team Process Improvement Workflow
Coordinate process pain points, bottlenecks, working agreements, delivery metrics, improvement plan, and review cadence.

**ID:** `team-process-improvement`
**Categories:** `people-operations`, `management`
**Tags:** `process-improvement`, `delivery`, `working-agreements`, `metrics`, `team-health`
**Task IDs:** `improve-team-process`, `people-ops`, `manage-project`
**Role IDs:** `engineering-manager`, `release-manager`, `tech-lead`, `qa-engineer`, `product-manager`
**Guide:** `workflows/people-operations/team-process-improvement/workflow.md`
**Manifest:** `workflows/people-operations/team-process-improvement/workflow.yaml`

## Platform Operations

### Infrastructure Provisioning Workflow
Coordinate Terraform/OpenTofu modules, environment plan, network plan, IAM model, CI/CD plan, observability, and cost estimate.

**ID:** `infrastructure-provisioning`
**Categories:** `platform-operations`, `infrastructure`
**Tags:** `infrastructure`, `terraform`, `opentofu`, `iam`, `ci-cd`
**Task IDs:** `provision-infrastructure`, `manage-cloud-infra`, `deploy-release`
**Role IDs:** `cloud-architect`, `devops-platform-engineer`, `sre`, `security-engineer`, `finops-analyst`, `qa-engineer`, `release-manager`
**Guide:** `workflows/platform-operations/infrastructure-provisioning/workflow.md`
**Manifest:** `workflows/platform-operations/infrastructure-provisioning/workflow.yaml`

### Platform Engineering Workflow
Coordinate internal developer platform design, golden paths, service templates, CI/CD templates, developer portal, observability defaults, and documentation.

**ID:** `platform-engineering`
**Categories:** `platform-operations`, `developer-experience`
**Tags:** `platform`, `golden-path`, `service-template`, `developer-portal`, `observability`
**Task IDs:** `engineer-platform`, `manage-cloud-infra`, `write-documents`
**Role IDs:** `devops-platform-engineer`, `engineering-manager`, `tech-lead`, `cloud-architect`, `security-engineer`, `sre`, `technical-writer`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/platform-operations/platform-engineering/workflow.md`
**Manifest:** `workflows/platform-operations/platform-engineering/workflow.yaml`

## Procurement

### Vendor Selection Workflow
Coordinate requirements, comparison matrix, risks, cost model, recommendation, fallback option, and approval needs.

**ID:** `vendor-selection`
**Categories:** `business-operations`, `procurement`
**Tags:** `vendor`, `procurement`, `comparison`, `cost-model`, `fallback`
**Task IDs:** `select-vendor`, `finance-legal`, `research-brief`
**Role IDs:** `procurement-manager`, `product-manager`, `tech-lead`, `finance-manager`, `security-engineer`, `compliance-officer`, `release-manager`
**Guide:** `workflows/business-operations/vendor-selection/workflow.md`
**Manifest:** `workflows/business-operations/vendor-selection/workflow.yaml`

## Product

### Customer Feedback Analysis Workflow
Coordinate feedback clusters, pain points, feature requests, churn risks, roadmap inputs, and follow-up research.

**ID:** `customer-feedback-analysis`
**Categories:** `customer-success`, `product`
**Tags:** `feedback`, `customer-insights`, `churn`, `roadmap`, `feature-requests`
**Task IDs:** `analyze-feedback`, `customer-sales`, `analyze-data`
**Role IDs:** `customer-success-support`, `product-manager`, `product-analyst`, `ux-researcher`
**Guide:** `workflows/customer-success/customer-feedback-analysis/workflow.md`
**Manifest:** `workflows/customer-success/customer-feedback-analysis/workflow.yaml`

### Pricing And Monetization Workflow
Coordinate pricing tiers, unit economics, free trial or freemium rules, limits, quotas, and revenue forecast.

**ID:** `pricing-and-monetization`
**Categories:** `business-growth`, `product`
**Tags:** `pricing`, `monetization`, `unit-economics`, `freemium`, `revenue`
**Task IDs:** `design-pricing`, `finance-legal`, `manage-project`
**Role IDs:** `product-manager`, `finance-manager`, `growth-marketer`, `sales-strategist`, `compliance-officer`
**Guide:** `workflows/business-growth/pricing-and-monetization/workflow.md`
**Manifest:** `workflows/business-growth/pricing-and-monetization/workflow.yaml`

## Product Analytics

### Analytics And Growth Workflow
Coordinate funnel analysis, retention report, cohort analysis, growth experiments, A/B test plan, and instrumentation gaps.

**ID:** `analytics-and-growth`
**Categories:** `business-growth`, `product-analytics`
**Tags:** `analytics`, `growth`, `funnel`, `retention`, `ab-test`
**Task IDs:** `analyze-growth`, `analyze-data`, `manage-project`
**Role IDs:** `product-manager`, `product-analyst`, `growth-marketer`, `ux-researcher`, `tech-lead`
**Guide:** `workflows/business-growth/analytics-and-growth/workflow.md`
**Manifest:** `workflows/business-growth/analytics-and-growth/workflow.yaml`

## Product Delivery

### Bugfix Workflow
Coordinate defect triage, reproduction, root cause, fix plan, regression checklist, and hotfix or normal release decision.

**ID:** `bugfix`
**Categories:** `engineering`, `product-delivery`
**Tags:** `bugfix`, `defect`, `regression`, `root-cause`, `hotfix`
**Task IDs:** `triage-bug`, `debug-incident`, `test-validate`, `deploy-release`
**Role IDs:** `customer-success-support`, `qa-engineer`, `product-manager`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `sdet`, `release-manager`, `devops-platform-engineer`
**Guide:** `workflows/engineering/bugfix/workflow.md`
**Manifest:** `workflows/engineering/bugfix/workflow.yaml`

### Feature Development Workflow
Coordinate scoped discovery, UX fit, architecture review, implementation planning, regression testing, rollout, and iteration for an existing product feature.

**ID:** `feature-development`
**Categories:** `product-delivery`, `engineering`
**Tags:** `feature`, `existing-product`, `regression`, `feature-flags`, `architecture-review`
**Task IDs:** `plan-feature`, `implement-code`, `review-code`, `build-frontend`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`
**Role IDs:** `product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/product-delivery/feature-development/workflow.md`
**Manifest:** `workflows/product-delivery/feature-development/workflow.yaml`

### Mobile App Workflow
Coordinate product, platform UX, mobile architecture, development planning, QA, store release, and iteration for mobile apps.

**ID:** `mobile-app`
**Categories:** `product-delivery`, `mobile`
**Tags:** `mobile`, `ios`, `android`, `app-store`, `offline`, `push-notifications`
**Task IDs:** `plan-feature`, `build-mobile-desktop`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`
**Role IDs:** `product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `mobile-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/product-delivery/mobile-app/workflow.md`
**Manifest:** `workflows/product-delivery/mobile-app/workflow.yaml`

### SaaS From Scratch Workflow
Coordinate discovery, design, architecture, development planning, QA, release, and iteration for a new SaaS product.

**ID:** `saas-from-scratch`
**Categories:** `product-delivery`
**Tags:** `saas`, `new-product`, `product-discovery`, `architecture`, `release`
**Task IDs:** `plan-feature`, `build-frontend`, `build-backend`, `test-validate`, `deploy-release`, `manage-project`
**Role IDs:** `product-manager`, `business-analyst`, `ux-designer`, `ui-designer`, `ux-researcher`, `solution-architect`, `tech-lead`, `frontend-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `sdet`, `release-manager`, `product-analyst`, `customer-success-support`
**Guide:** `workflows/product-delivery/saas-from-scratch/workflow.md`
**Manifest:** `workflows/product-delivery/saas-from-scratch/workflow.yaml`

## Product Discovery

### Idea Validation Workflow
Coordinate pre-development validation of problem, audience, market signals, value proposition, pricing hypothesis, MVP scope, and go/no-go decision.

**ID:** `idea-validation`
**Categories:** `product-discovery`, `business`
**Tags:** `idea`, `validation`, `market-research`, `mvp`, `go-no-go`
**Task IDs:** `validate-idea`, `research-brief`, `manage-project`
**Role IDs:** `founder-business-owner`, `product-manager`, `market-researcher`, `business-analyst`, `finance-manager`, `ux-researcher`, `product-analyst`
**Guide:** `workflows/product-discovery/idea-validation/workflow.md`
**Manifest:** `workflows/product-discovery/idea-validation/workflow.yaml`

### Product Strategy Workflow
Coordinate product vision, positioning, north-star metric, roadmap direction, monetization model, strategic risks, and product principles.

**ID:** `product-strategy`
**Categories:** `product-discovery`, `business`
**Tags:** `strategy`, `vision`, `roadmap`, `positioning`, `north-star-metric`
**Task IDs:** `define-product-strategy`, `validate-idea`, `manage-project`
**Role IDs:** `product-strategist`, `product-manager`, `founder-business-owner`, `solution-architect`, `finance-manager`, `market-researcher`
**Guide:** `workflows/product-discovery/product-strategy/workflow.md`
**Manifest:** `workflows/product-discovery/product-strategy/workflow.yaml`

## Product Launch

### Go To Market Workflow
Coordinate launch plan, messaging, landing page brief, sales materials, onboarding flow, support readiness, and launch checklist.

**ID:** `go-to-market`
**Categories:** `business-growth`, `product-launch`
**Tags:** `gtm`, `launch`, `messaging`, `sales-enablement`, `onboarding`
**Task IDs:** `plan-launch`, `customer-sales`, `write-documents`, `deploy-release`
**Role IDs:** `product-manager`, `product-marketing-manager`, `growth-marketer`, `sales-strategist`, `content-marketer`, `customer-success-support`, `technical-writer`, `release-manager`
**Guide:** `workflows/business-growth/go-to-market/workflow.md`
**Manifest:** `workflows/business-growth/go-to-market/workflow.yaml`

## Quality

### Automated Testing Workflow
Coordinate unit, integration, and e2e test plans, CI test pipeline, flaky-test policy, reporting, and maintenance plan.

**ID:** `automated-testing`
**Categories:** `quality`, `engineering`
**Tags:** `automated-tests`, `unit-tests`, `integration-tests`, `e2e`, `ci`
**Task IDs:** `automate-tests`, `test-validate`, `implement-code`
**Role IDs:** `sdet`, `qa-engineer`, `tech-lead`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`
**Guide:** `workflows/quality/automated-testing/workflow.md`
**Manifest:** `workflows/quality/automated-testing/workflow.yaml`

### Performance Testing Workflow
Coordinate load profile, performance scenarios, bottleneck report, capacity estimate, optimization plan, and rollout safeguards.

**ID:** `performance-testing`
**Categories:** `quality`, `reliability`
**Tags:** `performance`, `load-test`, `capacity`, `bottleneck`, `optimization`
**Task IDs:** `test-performance`, `test-validate`, `analyze-data`
**Role IDs:** `performance-engineer`, `sre`, `product-manager`, `backend-engineer`, `database-engineer`, `devops-platform-engineer`, `tech-lead`, `qa-engineer`
**Guide:** `workflows/quality/performance-testing/workflow.md`
**Manifest:** `workflows/quality/performance-testing/workflow.yaml`

### Test Planning Workflow
Coordinate test strategy, test cases, regression scope, automation scope, acceptance criteria, and quality gates.

**ID:** `test-planning`
**Categories:** `quality`, `engineering`
**Tags:** `qa`, `test-plan`, `acceptance-criteria`, `regression`, `quality-gates`
**Task IDs:** `plan-tests`, `test-validate`
**Role IDs:** `qa-engineer`, `product-manager`, `tech-lead`, `sdet`, `devops-platform-engineer`
**Guide:** `workflows/quality/test-planning/workflow.md`
**Manifest:** `workflows/quality/test-planning/workflow.yaml`

## Reliability

### Incident Response Workflow
Coordinate incident timeline, impact analysis, mitigation actions, customer communication, recovery validation, and follow-up tasks.

**ID:** `incident-response`
**Categories:** `operations`, `reliability`
**Tags:** `incident`, `outage`, `mitigation`, `customer-communication`, `recovery`
**Task IDs:** `respond-incident`, `debug-incident`, `deploy-release`
**Role IDs:** `incident-commander`, `sre`, `customer-success-support`, `product-manager`, `devops-platform-engineer`, `backend-engineer`, `qa-engineer`, `release-manager`, `engineering-manager`
**Guide:** `workflows/operations/incident-response/workflow.md`
**Manifest:** `workflows/operations/incident-response/workflow.yaml`

### Performance Testing Workflow
Coordinate load profile, performance scenarios, bottleneck report, capacity estimate, optimization plan, and rollout safeguards.

**ID:** `performance-testing`
**Categories:** `quality`, `reliability`
**Tags:** `performance`, `load-test`, `capacity`, `bottleneck`, `optimization`
**Task IDs:** `test-performance`, `test-validate`, `analyze-data`
**Role IDs:** `performance-engineer`, `sre`, `product-manager`, `backend-engineer`, `database-engineer`, `devops-platform-engineer`, `tech-lead`, `qa-engineer`
**Guide:** `workflows/quality/performance-testing/workflow.md`
**Manifest:** `workflows/quality/performance-testing/workflow.yaml`

### Postmortem Workflow
Coordinate what happened, why it happened, detection gap, prevention actions, owner per action, and deadline per action.

**ID:** `postmortem`
**Categories:** `operations`, `reliability`
**Tags:** `postmortem`, `incident-review`, `root-cause`, `prevention`, `follow-up`
**Task IDs:** `write-postmortem`, `debug-incident`, `write-documents`
**Role IDs:** `incident-commander`, `sre`, `customer-success-support`, `tech-lead`, `backend-engineer`, `devops-platform-engineer`, `product-manager`, `engineering-manager`
**Guide:** `workflows/operations/postmortem/workflow.md`
**Manifest:** `workflows/operations/postmortem/workflow.yaml`

## Sales

### Sales Support Workflow
Coordinate sales deck, demo script, objection handling, technical FAQ, proposal template, and risk review.

**ID:** `sales-support`
**Categories:** `business-growth`, `sales`
**Tags:** `sales`, `b2b`, `demo`, `objections`, `proposal`
**Task IDs:** `support-sales`, `customer-sales`, `write-documents`
**Role IDs:** `sales-strategist`, `product-manager`, `solution-consultant`, `technical-writer`, `compliance-officer`, `security-engineer`
**Guide:** `workflows/business-growth/sales-support/workflow.md`
**Manifest:** `workflows/business-growth/sales-support/workflow.yaml`

## Security Compliance

### Legal Compliance Workflow
Coordinate GDPR checklist, privacy policy notes, data processing map, ToS requirements, compliance risks, and action plan.

**ID:** `legal-compliance`
**Categories:** `security-compliance`, `business-operations`
**Tags:** `legal`, `compliance`, `privacy`, `gdpr`, `terms`
**Task IDs:** `review-compliance`, `finance-legal`, `security-audit`
**Role IDs:** `compliance-officer`, `data-protection-officer`, `product-manager`, `security-engineer`, `finance-manager`, `technical-writer`, `release-manager`
**Guide:** `workflows/security-compliance/legal-compliance/workflow.md`
**Manifest:** `workflows/security-compliance/legal-compliance/workflow.yaml`

### Security Review Workflow
Coordinate threat/security checklist, secrets review, dependency scan report, authn/authz review, vulnerability report, and remediation plan.

**ID:** `security-review`
**Categories:** `security-compliance`, `engineering`
**Tags:** `security`, `appsec`, `secrets`, `dependencies`, `authz`
**Task IDs:** `review-security`, `security-audit`, `review-code`
**Role IDs:** `security-engineer`, `security-architect`, `solution-architect`, `product-manager`, `backend-engineer`, `frontend-engineer`, `devops-platform-engineer`, `compliance-officer`, `tech-lead`, `release-manager`, `qa-engineer`
**Guide:** `workflows/security-compliance/security-review/workflow.md`
**Manifest:** `workflows/security-compliance/security-review/workflow.yaml`

### Threat Modeling Workflow
Coordinate assets, actors, trust boundaries, threat list, attack paths, mitigations, residual risks, and validation plan.

**ID:** `threat-modeling`
**Categories:** `security-compliance`, `architecture`
**Tags:** `threat-modeling`, `trust-boundaries`, `attack-paths`, `mitigations`, `security-design`
**Task IDs:** `model-threats`, `security-audit`, `review-architecture`
**Role IDs:** `security-architect`, `solution-architect`, `product-manager`, `security-engineer`, `backend-engineer`, `devops-platform-engineer`, `qa-engineer`, `tech-lead`
**Guide:** `workflows/security-compliance/threat-modeling/workflow.md`
**Manifest:** `workflows/security-compliance/threat-modeling/workflow.yaml`
