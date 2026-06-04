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
- **Founder Business Owner** (`founder-business-owner`) -> `founder`, `product`, `finance`, `operations`
- **Product Strategist** (`product-strategist`) -> `product`, `research`, `founder`, `finance`
- **Market Researcher** (`market-researcher`) -> `research`, `product`, `marketing`, `sales`
- **Growth Marketer** (`growth-marketer`) -> `marketing`, `data`, `product`, `sales`
- **Product Marketing Manager** (`product-marketing-manager`) -> `marketing`, `product`, `sales`, `customer_success`
- **Sales Strategist** (`sales-strategist`) -> `sales`, `marketing`, `research`, `product`
- **Solution Consultant** (`solution-consultant`) -> `sales`, `engineering`, `backend`, `product`
- **Security Architect** (`security-architect`) -> `security`, `engineering`, `devops`
- **Compliance Officer** (`compliance-officer`) -> `legal`, `security`, `finance`, `operations`
- **Data Protection Officer** (`data-protection-officer`) -> `legal`, `security`, `data`, `product`
- **Database Engineer** (`database-engineer`) -> `data`, `backend`, `devops`, `engineering`
- **Cloud Architect** (`cloud-architect`) -> `devops`, `sre`, `security`, `finance`
- **SRE** (`sre`) -> `sre`, `devops`, `data`, `security`
- **Incident Commander** (`incident-commander`) -> `sre`, `operations`, `devops`, `customer_success`
- **FinOps Analyst** (`finops-analyst`) -> `finance`, `devops`, `sre`, `operations`
- **Finance Manager** (`finance-manager`) -> `finance`, `operations`, `founder`
- **Procurement Manager** (`procurement-manager`) -> `operations`, `finance`, `legal`, `research`
- **Technical Writer** (`technical-writer`) -> `documents`, `research`, `product`, `customer_success`
- **Knowledge Manager** (`knowledge-manager`) -> `documents`, `operations`, `customer_success`, `research`
- **Content Marketer** (`content-marketer`) -> `marketing`, `documents`, `product`, `research`
- **Recruiter** (`recruiter`) -> `people`, `operations`
- **HR Manager** (`hr-manager`) -> `people`, `operations`
- **Engineering Manager** (`engineering-manager`) -> `people`, `operations`, `engineering`, `product`

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
- **Validate an Idea** (`validate-idea`) -> `competitive-intelligence`, `forecast`, `product`, `research`, `roadmap`
- **Define Product Strategy** (`define-product-strategy`) -> `competitive-intelligence`, `finance`, `metrics`, `planning`, `product`, `roadmap`
- **Design Pricing and Monetization** (`design-pricing`) -> `compliance`, `finance`, `forecast`, `sales`
- **Plan Go To Market Launch** (`plan-launch`) -> `campaign`, `content`, `customer-support`, `marketing`, `planning`, `sales`
- **Triage and Fix a Bug** (`triage-bug`) -> `debugging`, `deployment`, `error-analysis`, `incident`, `status-report`, `testing`
- **Reduce Technical Debt** (`reduce-technical-debt`) -> `architecture`, `migration`, `optimization`, `refactoring`, `tech-debt`, `testing`
- **Design an API** (`design-api`) -> `documentation`, `rest-api`, `testing`
- **Develop an Integration** (`develop-integration`) -> `data`, `incident`, `integration`, `rest-api`
- **Review Architecture** (`review-architecture`) -> `architecture`, `review`, `risk`, `security`, `system-design`
- **Write an ADR** (`write-adr`) -> `architecture`, `documentation`, `migration`, `planning`, `review`
- **Provision Infrastructure** (`provision-infrastructure`) -> `ci`, `deployment`
- **Engineer Internal Platform** (`engineer-platform`) -> `ci`, `deployment`, `documentation`, `process`
- **Review Security** (`review-security`) -> `audit`, `authentication`, `compliance`, `security`, `supply-chain`, `threat-model`
- **Model Threats** (`model-threats`) -> `architecture`, `authentication`, `risk`, `security`, `threat-model`, `validation`
- **Plan Tests** (`plan-tests`) -> `planning`, `requirements`, `testing`, `testing-strategy`, `validation`
- **Automate Tests** (`automate-tests`) -> `automation`, `ci`, `playwright`, `testing`, `validation`
- **Test Performance** (`test-performance`) -> `capacity`, `metrics`, `optimization`, `testing`
- **Respond to Incident** (`respond-incident`) -> `customer-support`, `deployment`, `incident`, `runbook`, `status-report`
- **Write Postmortem** (`write-postmortem`) -> `documentation`, `incident`, `process`, `reporting`, `risk`, `runbook`
- **Support Customer** (`support-customer`) -> `customer-support`, `debugging`, `documentation`, `product`, `ticket-triage`
- **Analyze Customer Feedback** (`analyze-feedback`) -> `analytics`, `customer-support`, `product`, `roadmap`, `user-research`
- **Analyze Growth** (`analyze-growth`) -> `analytics`, `dashboard`, `metrics`, `statistics`, `visualization`
- **Support Sales** (`support-sales`) -> `call-prep`, `content`, `contract`, `crm`, `documentation`, `sales`
- **Review Legal Compliance** (`review-compliance`) -> `compliance`, `contract`, `legal`, `policy`, `risk`, `security`
- **Write Technical Documentation** (`write-technical-docs`) -> `architecture`, `debugging`, `deployment`, `documentation`, `rest-api`, `writing`
- **Write User Documentation** (`write-user-docs`) -> `changelog`, `content`, `customer-support`, `documentation`, `onboarding`, `writing`
- **Maintain Knowledge Base** (`maintain-knowledge-base`) -> `documentation`, `knowledge`, `onboarding`, `organization`, `process`, `runbook`
- **Optimize Costs** (`optimize-costs`) -> `finance`, `metrics`, `optimization`
- **Select Vendor** (`select-vendor`) -> `competitive-intelligence`, `contract`, `risk`, `vendor`
- **Plan Hiring** (`plan-hiring`) -> `compensation`, `interviewing`, `onboarding`, `people`, `recruiting`
- **Improve Team Process** (`improve-team-process`) -> `management`, `metrics`, `planning`, `process`, `reporting`
