# AI Capability Registry

Read `../capability-routing.md` first. This file defines skill-specific routing.

## Skill Sources

Skills may be agent-native or registry-indexed. Treat both as one capability pool. Prefer an already-available trusted native skill when equivalent; otherwise use this registry's catalogs and read the referenced `SKILL.md`. Do not assume both sources mirror each other.

## Skill Resolution Protocol

Before starting work, resolve skills from both agent-native skills and this registry with progressive disclosure:

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Read only the matched task index and optional role index.
3. Select 1-3 specific keywords, preferring exact stack/tool keywords over broad category keywords.
4. Read only selected keyword catalogs.
5. Choose 1-3 best matching skill descriptions per keyword.
6. Read only those `SKILL.md` files and adapt their guidance to project conventions.

### Routing Scope

Paths in keyword catalogs are relative to this registry root.
`external/` is a sibling of the root `skills/` directory at `<registry-root>/external/`; do not look for it under `skills/external/`.

Use `skills/catalog/` only for skill selection.
Use `skills/packs/` only when configuring agents with preselected skill directories.
Do not browse `skills/catalog/` or `skills/packs/` broadly during task execution.

### Path Templates

- Role index: `skills/catalog/roles/<role-id>/skills.md`
- Task index: `skills/catalog/tasks/<task-id>/skills.md`
- Keyword catalog: `skills/catalog/keywords/<keyword>/skills.md`

### Roles (category groupings)

- **Personal AI Assistant** (`personal-assistant`) -> `personal_assistant`, `research`, `core`
- **Founder CEO Advisor** (`founder-ceo`) -> `founder`, `product`, `marketing`, `sales`, `finance`, `people`
- **CTO and Engineering Lead** (`cto-engineering-lead`) -> `engineering`, `backend`, `frontend`, `devops`, `sre`, `security`, `ai`, `ml`
- **Product Manager** (`product-manager`) -> `product`, `research`, `design`, `data`, `customer_success`
- **Software Engineer** (`software-engineer`) -> `core`, `engineering`, `backend`, `frontend`, `qa`
- **Backend Engineer** (`backend-engineer`) -> `backend`, `data`, `devops`, `security`, `developer_tools`
- **Frontend Engineer** (`frontend-engineer`) -> `frontend`, `design`, `qa`, `developer_tools`
- **Mobile and Desktop Engineer** (`mobile-engineer`) -> `mobile`, `desktop`, `frontend`, `qa`, `developer_tools`
- **QA Engineer** (`qa-engineer`) -> `qa`, `core`, `frontend`, `backend`, `developer_tools`
- **Security Engineer** (`security-engineer`) -> `security`
- **DevOps and Platform Engineer** (`devops-platform-engineer`) -> `devops`, `sre`, `security`
- **SRE Incident Manager** (`sre-incident-manager`) -> `sre`, `devops`, `data`
- **Data Analyst** (`data-analyst`) -> `data`, `research`, `product`
- **AI Engineer** (`ai-engineer`) -> `ai`, `ml`, `engineering`, `security`, `research`
- **Product Designer** (`designer`) -> `design`, `frontend`, `research`
- **Marketing and Growth Lead** (`marketing-growth`) -> `marketing`, `founder`, `data`
- **Sales Account Executive** (`sales-account-executive`) -> `sales`, `research`, `marketing`
- **Customer Success and Support Specialist** (`customer-success-support`) -> `customer_success`, `research`, `product`
- **Finance Operations Analyst** (`finance-ops`) -> `finance`, `operations`
- **Legal Operations Assistant** (`legal-ops`) -> `legal`
- **People Operations and Recruiting Partner** (`people-ops-recruiting`) -> `people`
- **Operations Manager** (`operations-manager`) -> `operations`, `research`, `customer_success`
- **AI Agent Builder and Pipeline Orchestrator** (`ai-agent-builder`) -> `ai`, `ml`, `engineering`, `devops`, `security`, `core`
- **Creative Media Producer** (`creative-media-producer`) -> `creative_media`, `design`, `documents`, `marketing`
- **Data Engineer** (`data-engineer`) -> `data`, `backend`, `devops`, `security`
- **Cloud Infrastructure Engineer** (`cloud-infrastructure-engineer`) -> `devops`, `sre`, `security`
- **Blockchain Engineer** (`blockchain-engineer`) -> `blockchain`, `security`, `engineering`
- **Hardware and IoT Engineer** (`hardware-iot-engineer`) -> `hardware`, `devops`, `security`

### Tasks (entry points)

- **Plan a Feature or Spec** (`plan-feature`) -> `architecture`, `planning`, `requirements`, `roadmap`, `spec`, `user-research`
- **Implement or Refactor Code** (`implement-code`) -> `debugging`, `development`, `documentation`, `refactor`, `testing`
- **Review Code or PR** (`review-code`) -> `code-review`, `review`, `static-analysis`, `testing`, `threat-model`
- **Debug an Issue or Incident** (`debug-incident`) -> `debugging`, `incident`, `langsmith`, `runbook`, `sentry`, `status-report`
- **Test and Validate** (`test-validate`) -> `fuzzing`, `testing`, `testing-strategy`, `validation`
- **Security Audit or Threat Model** (`security-audit`) -> `codeql`, `cryptography`, `sarif`, `semgrep`, `static-analysis`, `supply-chain`, `threat-model`
- **Build Frontend or UI** (`build-frontend`) -> `accessibility`, `angular`, `design-system`, `frontend`, `react`, `ui`, `web`
- **Build Backend or Integration** (`build-backend`) -> `aspnet`, `dotnet`, `rest-api`
- **Deploy or Release** (`deploy-release`) -> `changelog`, `ci`, `cloudflare`, `deployment`, `netlify`, `render`, `vercel`
- **Analyze Data or Metrics** (`analyze-data`) -> `analytics`, `dashboard`, `data`, `forecast`, `metrics`, `sql`, `statistics`, `visualization`
- **Research and Brief** (`research-brief`) -> `knowledge`, `pdf`, `research`, `summarization`
- **Build Agent Automation** (`automate-agent`) -> `agent`, `automation`, `mcp`, `plugin`, `skill-creator`
- **Write Docs or Documents** (`write-documents`) -> `changelog`, `content`, `documentation`, `docx`, `pdf`, `pptx`, `summarization`, `writing`
- **Manage Product or Project** (`manage-project`) -> `planning`, `roadmap`, `spec`, `sprint`, `stakeholder`, `task-management`
- **Support Customers or Sales** (`customer-sales`) -> `account-research`, `call-prep`, `customer-support`, `lead-generation`, `outreach`, `pipeline`, `ticket-triage`
- **Finance, Compliance, or Legal** (`finance-legal`) -> `audit`, `compliance`, `contract`, `finance`, `nda`, `policy`, `risk`
- **People Operations** (`people-ops`) -> `compensation`, `interviewing`, `onboarding`, `org-planning`, `performance-review`, `recruiting`
- **Personal Productivity** (`personal-productivity`) -> `email`, `meeting`, `memory`, `productivity`, `slack`, `task-management`
- **Create or Edit Media** (`create-media`) -> `creative-media`, `imagegen`, `media`, `screenshot`, `speech`, `transcribe`, `youtube`
- **Manage Data Systems** (`manage-data-systems`) -> `analytics`, `dashboard`, `data`, `dbt`, `sql`
- **Manage Cloud Infrastructure** (`manage-cloud-infra`) -> `ci`, `cloudflare`, `deployment`, `incident`, `netlify`, `render`, `vercel`
- **Build Blockchain or Smart Contracts** (`build-blockchain`) -> `blockchain`, `cairo`, `smart-contracts`, `solana`, `solidity`, `threat-model`
- **Build Hardware or IoT** (`build-hardware-iot`) -> `integration`
- **Build Mobile or Desktop App** (`build-mobile-desktop`) -> `android`, `ios`, `react-native`, `testing`, `windows`

## Policy

- Use trusted or reviewed skill sources only.
- Never execute untrusted scripts.
- For MCP-backed capabilities, follow `mcp/mcp.md`.
