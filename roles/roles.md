# Runtime Role Registry

Use these role prompts when a selected workflow stage delegates work to subagents. These files are runtime instructions, not generated skill catalogs.

## Role Loading Protocol

1. Load only the role files listed by the selected workflow stage.
2. Give each role the user request, workflow id, stage id, previous stage outputs, expected outputs, acceptance criteria, and required output format.
3. Instruct the role to route to skills through `skills/catalog/roles/<role-id>/skills.md` when specialized skills are needed.
4. Instruct the role to route to MCP through `mcp/catalog/roles/<role-id>/servers.md` only when the task directly needs an external service, data source, or tool integration.
5. Require structured outputs so the coordinator can validate gates and pass handoff packets between stages.

## Roles

- `product-manager`: Product scope, goals, metrics, PRD, roadmap, and user value.
- `business-analyst`: Requirements, use cases, processes, business rules, and integrations.
- `ux-researcher`: Research planning, usability testing, evidence synthesis, and journey insights.
- `ux-designer`: User flows, interaction design, wireframes, states, and edge cases.
- `ui-designer`: Visual design, component states, design-system fit, and handoff notes.
- `solution-architect`: System boundaries, architecture, data flows, APIs, and technical tradeoffs.
- `tech-lead`: Engineering sequencing, implementation planning, review boundaries, and delivery risk.
- `frontend-engineer`: Web UI implementation planning, accessibility, state handling, and frontend risks.
- `backend-engineer`: APIs, services, data models, integrations, migrations, and backend risks.
- `mobile-engineer`: Native and cross-platform mobile implementation, platform constraints, and app releases.
- `devops-platform-engineer`: CI/CD, infrastructure, environments, observability, deployment, and rollback.
- `qa-engineer`: Risk-based test planning, manual coverage, regression scope, and defect clarity.
- `sdet`: Automated test strategy, CI checks, test reliability, and automation candidates.
- `performance-engineer`: Performance budgets, load scenarios, bottlenecks, and scalability validation.
- `release-manager`: Release readiness, rollout, rollback, release notes, and launch coordination.
- `product-analyst`: Metrics, funnels, dashboards, instrumentation, and post-release analysis.
- `customer-success-support`: Support readiness, customer communication, feedback channels, and knowledge-base notes.
