# AI Capability Registry

## Skill Resolution Protocol

When a task is received, perform these steps BEFORE starting work:

1. **Analyze request** — extract keywords from user request
2. **Choose entry point** — select a Task, Role, or Keyword below
3. **Match categories** — each task/role shows its categories and keywords
4. **Load skills** — read SKILL.md files from matched keywords
5. **Apply guidance** — follow skill instructions, adapt to project conventions

### Entry Points

Browse all tasks: `skills/tasks/`
Browse all roles: `skills/roles/`
Browse all keywords: `skills/keywords/`

### Roles (category groupings)

- **Personal AI Assistant**: `skills/roles/personal-assistant/skills.md` → `personal_assistant`, `research`, `core`
- **Founder CEO Advisor**: `skills/roles/founder-ceo/skills.md` → `founder`, `product`, `marketing`, `sales`, `finance`, `people`
- **CTO and Engineering Lead**: `skills/roles/cto-engineering-lead/skills.md` → `engineering`, `backend`, `frontend`, `devops`, `sre`, `security`, `ai`, `ml`
- **Product Manager**: `skills/roles/product-manager/skills.md` → `product`, `research`, `design`, `data`, `customer_success`
- **Software Engineer**: `skills/roles/software-engineer/skills.md` → `core`, `engineering`, `backend`, `frontend`, `qa`
- **Backend Engineer**: `skills/roles/backend-engineer/skills.md` → `backend`, `data`, `devops`, `security`
- **Frontend Engineer**: `skills/roles/frontend-engineer/skills.md` → `frontend`, `design`, `qa`
- **Mobile and Desktop Engineer**: `skills/roles/mobile-engineer/skills.md` → `mobile`, `desktop`, `frontend`, `qa`
- **QA Engineer**: `skills/roles/qa-engineer/skills.md` → `qa`, `core`, `frontend`, `backend`
- **Security Engineer**: `skills/roles/security-engineer/skills.md` → `security`
- **DevOps and Platform Engineer**: `skills/roles/devops-platform-engineer/skills.md` → `devops`, `sre`, `security`
- **SRE Incident Manager**: `skills/roles/sre-incident-manager/skills.md` → `sre`, `devops`, `data`
- **Data Analyst**: `skills/roles/data-analyst/skills.md` → `data`, `research`, `product`
- **AI Engineer**: `skills/roles/ai-engineer/skills.md` → `ai`, `ml`, `engineering`, `security`, `research`
- **Product Designer**: `skills/roles/designer/skills.md` → `design`, `frontend`, `research`
- **Marketing and Growth Lead**: `skills/roles/marketing-growth/skills.md` → `marketing`, `founder`, `data`
- **Sales Account Executive**: `skills/roles/sales-account-executive/skills.md` → `sales`, `research`, `marketing`
- **Customer Success and Support Specialist**: `skills/roles/customer-success-support/skills.md` → `customer_success`, `research`, `product`
- **Finance Operations Analyst**: `skills/roles/finance-ops/skills.md` → `finance`, `operations`
- **Legal Operations Assistant**: `skills/roles/legal-ops/skills.md` → `legal`
- **People Operations and Recruiting Partner**: `skills/roles/people-ops-recruiting/skills.md` → `people`
- **Operations Manager**: `skills/roles/operations-manager/skills.md` → `operations`, `research`, `customer_success`
- **AI Agent Builder and Pipeline Orchestrator**: `skills/roles/ai-agent-builder/skills.md` → `ai`, `ml`, `engineering`, `devops`, `security`, `core`

### Tasks (workflow entry points)

- **Plan a Feature or Spec**: `skills/tasks/plan-feature/skills.md` → `architecture`, `planning`, `requirements`, `roadmap`, `spec`, `user-research`
- **Implement or Refactor Code**: `skills/tasks/implement-code/skills.md` → `debugging`, `development`, `documentation`, `refactor`, `testing`
- **Review Code or PR**: `skills/tasks/review-code/skills.md` → `code-review`, `review`, `static-analysis`, `testing`, `threat-model`
- **Debug an Issue or Incident**: `skills/tasks/debug-incident/skills.md` → `debugging`, `incident`, `langsmith`, `runbook`, `sentry`, `status-report`
- **Test and Validate**: `skills/tasks/test-validate/skills.md` → `fuzzing`, `testing`, `validation`
- **Security Audit or Threat Model**: `skills/tasks/security-audit/skills.md` → `codeql`, `cryptography`, `sarif`, `semgrep`, `static-analysis`, `supply-chain`, `threat-model`
- **Build Frontend or UI**: `skills/tasks/build-frontend/skills.md` → `accessibility`, `angular`, `design-system`, `frontend`, `react`, `ui`, `web`
- **Build Backend or Integration**: `skills/tasks/build-backend/skills.md` → `aspnet`, `dotnet`, `rest-api`
- **Deploy or Release**: `skills/tasks/deploy-release/skills.md` → `cloudflare`, `deployment`, `netlify`, `render`, `vercel`
- **Analyze Data or Metrics**: `skills/tasks/analyze-data/skills.md` → `analytics`, `dashboard`, `data`, `forecast`, `metrics`, `sql`, `statistics`, `visualization`
- **Research and Brief**: `skills/tasks/research-brief/skills.md` → `knowledge`, `pdf`, `research`, `summarization`
- **Build Agent Automation**: `skills/tasks/automate-agent/skills.md` → `agent`, `automation`, `mcp`, `plugin`, `skill-creator`
- **Write Docs or Documents**: `skills/tasks/write-documents/skills.md` → `content`, `documentation`, `docx`, `pdf`, `pptx`, `summarization`, `writing`
- **Manage Product or Project**: `skills/tasks/manage-project/skills.md` → `planning`, `roadmap`, `spec`, `sprint`, `stakeholder`, `task-management`
- **Support Customers or Sales**: `skills/tasks/customer-sales/skills.md` → `account-research`, `call-prep`, `customer-support`, `lead-generation`, `outreach`, `pipeline`, `ticket-triage`
- **Finance, Compliance, or Legal**: `skills/tasks/finance-legal/skills.md` → `audit`, `compliance`, `contract`, `finance`, `nda`, `policy`, `risk`
- **People Operations**: `skills/tasks/people-ops/skills.md` → `compensation`, `interviewing`, `onboarding`, `org-planning`, `performance-review`, `recruiting`
- **Personal Productivity**: `skills/tasks/personal-productivity/skills.md` → `email`, `meeting`, `memory`, `productivity`, `slack`, `task-management`

## Policy
- Use **trusted** or **reviewed** sources only
- Prefer Docker/hosted MCP
- Never execute untrusted scripts
