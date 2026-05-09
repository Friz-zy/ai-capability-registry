# AI Capability Registry

## Skill Resolution Protocol

Before starting work, resolve skills with progressive disclosure:

1. **Extract intent** — identify action, domain, stack/tool, artifact, and constraints from the user request.
2. **Route by task first** — match the request to one Task below; select a second Task only for clearly mixed workflows.
3. **Use role as context** — select at most one Role only when the user asks from that role perspective or it disambiguates the task.
4. **Read selected indexes only** — open only the matched `skills/catalog/tasks/<task-id>/skills.md` and optional `skills/catalog/roles/<role-id>/skills.md`.
5. **Choose keywords** — select 1-3 most specific keywords from those indexes; prefer exact stack/tool keywords over broad category keywords.
6. **Read keyword catalogs** — open only selected `skills/catalog/keywords/<keyword>/skills.md` files.
7. **Load skills** — choose 1-3 best matching skill descriptions per keyword, then read only those `SKILL.md` files.
8. **Apply guidance** — follow loaded skill instructions and adapt them to project conventions.

### Routing Scope

Use `skills/catalog/` only for skill selection.
Use `skills/packs/` only when configuring agents with preselected skill directories.
Do not browse `skills/catalog/` or `skills/packs/` broadly during task execution.

### Roles (category groupings)

- **Personal AI Assistant**: `skills/catalog/roles/personal-assistant/skills.md` -> `personal_assistant`, `research`, `core`
- **Founder CEO Advisor**: `skills/catalog/roles/founder-ceo/skills.md` -> `founder`, `product`, `marketing`, `sales`, `finance`, `people`
- **CTO and Engineering Lead**: `skills/catalog/roles/cto-engineering-lead/skills.md` -> `engineering`, `backend`, `frontend`, `devops`, `sre`, `security`, `ai`, `ml`
- **Product Manager**: `skills/catalog/roles/product-manager/skills.md` -> `product`, `research`, `design`, `data`, `customer_success`
- **Software Engineer**: `skills/catalog/roles/software-engineer/skills.md` -> `core`, `engineering`, `backend`, `frontend`, `qa`
- **Backend Engineer**: `skills/catalog/roles/backend-engineer/skills.md` -> `backend`, `data`, `devops`, `security`
- **Frontend Engineer**: `skills/catalog/roles/frontend-engineer/skills.md` -> `frontend`, `design`, `qa`
- **Mobile and Desktop Engineer**: `skills/catalog/roles/mobile-engineer/skills.md` -> `mobile`, `desktop`, `frontend`, `qa`
- **QA Engineer**: `skills/catalog/roles/qa-engineer/skills.md` -> `qa`, `core`, `frontend`, `backend`
- **Security Engineer**: `skills/catalog/roles/security-engineer/skills.md` -> `security`
- **DevOps and Platform Engineer**: `skills/catalog/roles/devops-platform-engineer/skills.md` -> `devops`, `sre`, `security`
- **SRE Incident Manager**: `skills/catalog/roles/sre-incident-manager/skills.md` -> `sre`, `devops`, `data`
- **Data Analyst**: `skills/catalog/roles/data-analyst/skills.md` -> `data`, `research`, `product`
- **AI Engineer**: `skills/catalog/roles/ai-engineer/skills.md` -> `ai`, `ml`, `engineering`, `security`, `research`
- **Product Designer**: `skills/catalog/roles/designer/skills.md` -> `design`, `frontend`, `research`
- **Marketing and Growth Lead**: `skills/catalog/roles/marketing-growth/skills.md` -> `marketing`, `founder`, `data`
- **Sales Account Executive**: `skills/catalog/roles/sales-account-executive/skills.md` -> `sales`, `research`, `marketing`
- **Customer Success and Support Specialist**: `skills/catalog/roles/customer-success-support/skills.md` -> `customer_success`, `research`, `product`
- **Finance Operations Analyst**: `skills/catalog/roles/finance-ops/skills.md` -> `finance`, `operations`
- **Legal Operations Assistant**: `skills/catalog/roles/legal-ops/skills.md` -> `legal`
- **People Operations and Recruiting Partner**: `skills/catalog/roles/people-ops-recruiting/skills.md` -> `people`
- **Operations Manager**: `skills/catalog/roles/operations-manager/skills.md` -> `operations`, `research`, `customer_success`
- **AI Agent Builder and Pipeline Orchestrator**: `skills/catalog/roles/ai-agent-builder/skills.md` -> `ai`, `ml`, `engineering`, `devops`, `security`, `core`

### Tasks (workflow entry points)

- **Plan a Feature or Spec**: `skills/catalog/tasks/plan-feature/skills.md` -> `architecture`, `planning`, `requirements`, `roadmap`, `spec`, `user-research`
- **Implement or Refactor Code**: `skills/catalog/tasks/implement-code/skills.md` -> `debugging`, `development`, `documentation`, `refactor`, `testing`
- **Review Code or PR**: `skills/catalog/tasks/review-code/skills.md` -> `code-review`, `review`, `static-analysis`, `testing`, `threat-model`
- **Debug an Issue or Incident**: `skills/catalog/tasks/debug-incident/skills.md` -> `debugging`, `incident`, `langsmith`, `runbook`, `sentry`, `status-report`
- **Test and Validate**: `skills/catalog/tasks/test-validate/skills.md` -> `fuzzing`, `testing`, `validation`
- **Security Audit or Threat Model**: `skills/catalog/tasks/security-audit/skills.md` -> `codeql`, `cryptography`, `sarif`, `semgrep`, `static-analysis`, `supply-chain`, `threat-model`
- **Build Frontend or UI**: `skills/catalog/tasks/build-frontend/skills.md` -> `accessibility`, `angular`, `design-system`, `frontend`, `react`, `ui`, `web`
- **Build Backend or Integration**: `skills/catalog/tasks/build-backend/skills.md` -> `aspnet`, `dotnet`, `rest-api`
- **Deploy or Release**: `skills/catalog/tasks/deploy-release/skills.md` -> `cloudflare`, `deployment`, `netlify`, `render`, `vercel`
- **Analyze Data or Metrics**: `skills/catalog/tasks/analyze-data/skills.md` -> `analytics`, `dashboard`, `data`, `forecast`, `metrics`, `sql`, `statistics`, `visualization`
- **Research and Brief**: `skills/catalog/tasks/research-brief/skills.md` -> `knowledge`, `pdf`, `research`, `summarization`
- **Build Agent Automation**: `skills/catalog/tasks/automate-agent/skills.md` -> `agent`, `automation`, `mcp`, `plugin`, `skill-creator`
- **Write Docs or Documents**: `skills/catalog/tasks/write-documents/skills.md` -> `content`, `documentation`, `docx`, `pdf`, `pptx`, `summarization`, `writing`
- **Manage Product or Project**: `skills/catalog/tasks/manage-project/skills.md` -> `planning`, `roadmap`, `spec`, `sprint`, `stakeholder`, `task-management`
- **Support Customers or Sales**: `skills/catalog/tasks/customer-sales/skills.md` -> `account-research`, `call-prep`, `customer-support`, `lead-generation`, `outreach`, `pipeline`, `ticket-triage`
- **Finance, Compliance, or Legal**: `skills/catalog/tasks/finance-legal/skills.md` -> `audit`, `compliance`, `contract`, `finance`, `nda`, `policy`, `risk`
- **People Operations**: `skills/catalog/tasks/people-ops/skills.md` -> `compensation`, `interviewing`, `onboarding`, `org-planning`, `performance-review`, `recruiting`
- **Personal Productivity**: `skills/catalog/tasks/personal-productivity/skills.md` -> `email`, `meeting`, `memory`, `productivity`, `slack`, `task-management`

## Policy
- Use **trusted** or **reviewed** sources only
- Prefer Docker/hosted MCP
- Never execute untrusted scripts
