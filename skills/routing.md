# Skill Capability Routing

Read `../capability-routing.md` and `skills/skills.md` first.

Use this file only when no registry role, task, or catalog path is assigned and a skill route must be selected.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`.
2. Match by task first, then use role only as context or when it disambiguates the request.
3. Read the selected task or role index before keyword catalogs.
4. Select 1-3 specific keywords from matched indexes, preferring exact stack or tool keywords over broad category keywords.
5. Continue selection through `skills/skills.md`.

For an unassigned subagent, this route selects skill catalogs only; it does not change assigned role, workflow, parent instructions, expected outputs, or handoff scope.

### Path Templates

- Role index: `skills/catalog/roles/<role-id>/skills.md`
- Task index: `skills/catalog/tasks/<task-id>/skills.md`
- Keyword catalog: `skills/catalog/keywords/<keyword>/skills.md`

### Roles (category groupings)

- **Personal AI Assistant** (`personal-assistant`) -> `personal_assistant`, `research`, `core`
- **Orchestrator** (`orchestrator`) -> `orchestration`
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
- **Business Analyst** (`business-analyst`) -> `product`, `operations`, `research`, `data`
- **UX Researcher** (`ux-researcher`) -> `research`, `design`, `product`
- **UX Designer** (`ux-designer`) -> `design`, `research`, `frontend`
- **UI Designer** (`ui-designer`) -> `design`, `frontend`
- **Solution Architect** (`solution-architect`) -> `engineering`, `backend`, `frontend`, `devops`, `security`
- **Tech Lead** (`tech-lead`) -> `engineering`, `backend`, `frontend`, `devops`, `qa`, `security`
- **Software Development Engineer in Test** (`sdet`) -> `qa`, `engineering`, `frontend`, `backend`, `developer_tools`
- **Performance Engineer** (`performance-engineer`) -> `qa`, `engineering`, `sre`, `devops`
- **Release Manager** (`release-manager`) -> `devops`, `operations`, `product`, `customer_success`
- **Product Analyst** (`product-analyst`) -> `data`, `product`, `research`
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
