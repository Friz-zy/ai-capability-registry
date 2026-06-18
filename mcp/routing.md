# MCP Capability Routing

Read `../capability-routing.md` and `mcp/mcp.md` first.

Use this file only when no registry role, task, or catalog path is assigned and an MCP server route must be selected.

## Routing Protocol

1. Follow the shared routing pattern in `../capability-routing.md`, including service, product, and data-domain sensitivity.
2. Match by task first, then use role only as context or when it disambiguates the request.
3. Read the selected task or role server index before keyword catalogs.
4. Select 1-3 exact keywords from matched indexes, preferring service names over broad domains.
5. Continue selection and safety checks through `mcp/mcp.md`.

For an unassigned subagent, this route selects MCP catalogs only; it does not change assigned role, workflow, parent instructions, expected outputs, or handoff scope.

### Path Templates

- Role index: `mcp/catalog/roles/<role-id>/servers.md`
- Task index: `mcp/catalog/tasks/<task-id>/servers.md`
- Keyword catalog: `mcp/catalog/keywords/<keyword>/servers.md`
- Server guide: `mcp/servers/<server>/SKILL.md`

### Runtime Indexes

- **Hosted HTTPS** (public HTTPS endpoints using Streamable HTTP or SSE): `mcp/catalog/runtime/hosted/servers.md` — 110 server(s)
- **Docker stdio** (OCI images launched via `docker run --rm -i`): `mcp/catalog/runtime/docker/servers.md` — 59 server(s)
- **Other** (non-standard runtimes requiring manual review): `mcp/catalog/runtime/other/servers.md` — no enabled servers

### Roles (category groupings)

- **Personal AI Assistant** (`personal-assistant`) -> `access`, `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `context7`, `deepwiki`, `directory`, `discovery`, `documentation`
- **Orchestrator** (`orchestrator`) -> `context7`, `task-management`
- **Founder CEO Advisor** (`founder-ceo`) -> `airlines`, `apollo`, `asana`, `asset-management`, `attio`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`
- **Product Manager** (`product-manager`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-diagram`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-nova-canvas`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`
- **Software Engineer** (`software-engineer`) -> `access`, `analysis`, `appsync`, `architecture`, `astro`, `automation`, `aws-appsync`, `bindings`, `browserbase`, `communication`, `context7`, `debug`
- **Backend Engineer** (`backend-engineer`) -> `actions`, `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `atlassian`, `atlassian-atlassian`, `audit`, `authentication`, `aws`, `aws-appsync`
- **Frontend Engineer** (`frontend-engineer`) -> `actions`, `astro`, `atlassian`, `atlassian-atlassian`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code`, `code-examples`, `command`
- **Mobile and Desktop Engineer** (`mobile-engineer`) -> `actions`, `android`, `androidmanagement`, `astro`, `atlassian`, `atlassian-atlassian`, `browserbase`, `code`, `code-examples`, `command`, `context7`, `developer-portal`
- **QA Engineer** (`qa-engineer`) -> `access`, `actions`, `aks`, `amazon`, `analysis`, `appsignals`, `appsync`, `architecture`, `astro`, `atlassian`, `atlassian-atlassian`, `automation`
- **Security Engineer** (`security-engineer`) -> `audit`, `authentication`, `awslabs-iam`, `compliance`, `iam`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `policy`, `security`, `semgrep`
- **DevOps and Platform Engineer** (`devops-platform-engineer`) -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Data Analyst** (`data-analyst`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `competitive-intelligence`
- **AI Engineer** (`ai-engineer`) -> `access`, `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `architecture`
- **UX UI Designer** (`ux-ui-designer`) -> `amazon-kendra-index`, `astro`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code-examples`, `context7`, `deepwiki`, `design`
- **Business and Product Analyst** (`business-analyst`) -> `airlines`, `amazon-kendra-index`, `amazon-neptune`, `analytics`, `asana`, `asset-management`, `aws-knowledge`, `aws-location`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`
- **UX Researcher** (`ux-researcher`) -> `amazon-kendra-index`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `canva`, `canvas`, `code-examples`, `competitive-intelligence`, `context7`, `deepwiki`, `design`, `diagram`
- **Solution Architect** (`solution-architect`) -> `aks`, `amazon`, `analysis`, `appsignals`, `appsync`, `architecture`, `astro`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`
- **Tech Lead** (`tech-lead`) -> `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `appsignals`, `appsync`
- **Release Manager** (`release-manager`) -> `airlines`, `aks`, `amazon`, `asana`, `asset-management`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Customer Success and Support Specialist** (`customer-success-support`) -> `amazon-kendra-index`, `aws-knowledge`, `code-examples`, `competitive-intelligence`, `context7`, `customer-support`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`, `elasticsearch`
- **Operations Manager** (`operations-manager`) -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `audit`, `aws-knowledge`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`
- **Creative Media Producer** (`creative-media-producer`) -> `audio`, `aws-diagram`, `awslabs-nova-canvas`, `canva`, `canvas`, `carbon-voice`, `cloudinary`, `cms`, `content`, `design`, `diagram`, `document`
- **Data Engineer** (`data-engineer`) -> `aks`, `amazon`, `amazon-neptune`, `analysis`, `analytics`, `appsync`, `architecture`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`
- **Blockchain Engineer** (`blockchain-engineer`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `blockchain`, `cairo`, `compliance`, `context7`, `contracts`, `crypto`
- **Hardware and IoT Engineer** (`hardware-iot-engineer`) -> `aks`, `amazon`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`
- **Product Strategist** (`product-strategist`) -> `amazon-kendra-index`, `audit`, `aws-knowledge`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `code-examples`, `competitive-intelligence`, `compliance`, `context7`, `cost`
- **Market Researcher** (`market-researcher`) -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `competitive-intelligence`, `content`, `context7`, `crm`, `deepwiki`, `directory`
- **Growth Marketer** (`growth-marketer`) -> `amazon-neptune`, `analytics`, `apollo`, `attio`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `cms`, `competitive-intelligence`
- **Product Marketing Manager** (`product-marketing-manager`) -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `competitive-intelligence`, `content`, `context7`, `crm`, `customer-support`, `deepwiki`
- **Sales Strategist** (`sales-strategist`) -> `amazon-kendra-index`, `analysis`, `apollo`, `appsync`, `architecture`, `attio`, `aws-appsync`, `aws-knowledge`, `bindings`, `cms`, `code-examples`, `competitive-intelligence`
- **Security Architect** (`security-architect`) -> `aks`, `amazon`, `analysis`, `architecture`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Compliance Officer** (`compliance-officer`) -> `airlines`, `asana`, `asset-management`, `audit`, `authentication`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `awslabs-iam`, `billing`, `carbon`
- **Data Protection Officer** (`data-protection-officer`) -> `amazon-neptune`, `analytics`, `audit`, `authentication`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-iam`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `competitive-intelligence`
- **SRE** (`sre`) -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Incident Manager** (`incident-manager`) -> `airlines`, `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsignals`, `asana`, `asset-management`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`
- **FinOps Analyst** (`finops-analyst`) -> `airlines`, `aks`, `amazon`, `appsignals`, `asana`, `asset-management`, `audit`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Finance Manager** (`finance-manager`) -> `airlines`, `asana`, `asset-management`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`, `compliance`, `cost`
- **Technical Writer** (`technical-writer`) -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `aws-knowledge`, `aws-location`, `carbon`, `code-examples`, `competitive-intelligence`, `content`, `context7`, `customer-support`
- **HR Manager** (`hr-manager`) -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `e-commerce`, `googleapis-mapstools`, `health`, `indeed`, `location`, `management`, `maps`
- **Engineering Manager** (`engineering-manager`) -> `airlines`, `analysis`, `architecture`, `asana`, `asset-management`, `aws-location`, `bindings`, `carbon`, `competitive-intelligence`, `context7`, `debug`, `development`

### Tasks (workflow entry points)

- **Plan a Feature or Spec** (`plan-feature`) -> `access`, `analysis`, `architecture`, `automation`, `aws-diagram`, `awslabs-nova-canvas`, `bindings`, `canva`, `canvas`, `communication`, `competitive-intelligence`, `context7`
- **Implement or Refactor Code** (`implement-code`) -> `analysis`, `appsync`, `architecture`, `astro`, `aws-appsync`, `bindings`, `browserbase`, `context7`, `debug`, `development`, `documentation`, `error-analysis`
- **Review Code or PR** (`review-code`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `compliance`, `context7`, `debug`, `development`, `error-analysis`, `iam`
- **Debug an Issue or Incident** (`debug-incident`) -> `access`, `aks`, `amazon`, `analysis`, `appsignals`, `architecture`, `automation`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Test and Validate** (`test-validate`) -> `access`, `analysis`, `automation`, `communication`, `documentation`, `generate`, `integration`, `management`, `migration`, `optimization`, `planning`, `playwright`
- **Security Audit or Threat Model** (`security-audit`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `compliance`, `context7`, `debug`, `development`, `error-analysis`, `iam`
- **Build Frontend or UI** (`build-frontend`) -> `astro`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `context7`, `design`, `diagram`, `figma`, `googleapis-design`, `html`
- **Build Backend or Integration** (`build-backend`) -> `actions`, `alfresco`, `anonymous`, `anurag`, `anuragd`, `apollo`, `appsync`, `arm`, `astra`, `atlan`, `atlassian`, `atlassian-atlassian`
- **Deploy or Release** (`deploy-release`) -> `access`, `aks`, `amazon`, `analysis`, `appsignals`, `automation`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Analyze Data or Metrics** (`analyze-data`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `context7`
- **Research and Brief** (`research-brief`) -> `access`, `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `content`, `context7`, `deepwiki`, `directory`, `discovery`
- **Build Agent Automation** (`automate-agent`) -> `access`, `actions`, `agent`, `agentcore`, `ai`, `ai-assistant`, `alfresco`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `anonymous`
- **Write Docs or Documents** (`write-documents`) -> `access`, `analysis`, `automation`, `cms`, `communication`, `content`, `document`, `documentation`, `documents`, `docx`, `egnyte`, `generate`
- **Manage Product or Project** (`manage-project`) -> `access`, `airlines`, `analysis`, `asana`, `asset-management`, `automation`, `aws-location`, `carbon`, `communication`, `competitive-intelligence`, `documentation`, `e-commerce`
- **Support Customers or Sales** (`customer-sales`) -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `customer-support`, `deepwiki`, `directory`
- **Finance, Compliance, or Legal** (`finance-legal`) -> `airlines`, `asana`, `asset-management`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`, `compliance`, `contracts`
- **People Operations** (`people-ops`) -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `e-commerce`, `googleapis-mapstools`, `health`, `indeed`, `location`, `management`, `maps`
- **Personal Productivity** (`personal-productivity`) -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `communication`, `dialer`, `e-commerce`, `googleapis-mapstools`, `location`, `management`, `maps`
- **Create or Edit Media** (`create-media`) -> `audio`, `aws-diagram`, `awslabs-nova-canvas`, `canva`, `canvas`, `carbon-voice`, `cloudinary`, `design`, `diagram`, `face`, `figma`, `googleapis-design`
- **Manage Data Systems** (`manage-data-systems`) -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Manage Cloud Infrastructure** (`manage-cloud-infra`) -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Build Blockchain or Smart Contracts** (`build-blockchain`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `blockchain`, `cairo`, `compliance`, `context7`, `contracts`, `crypto`
- **Build Hardware or IoT** (`build-hardware-iot`) -> `aks`, `amazon`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`
- **Build Mobile or Desktop App** (`build-mobile-desktop`) -> `android`, `androidmanagement`, `astro`, `browserbase`, `context7`, `googleapis-androidmanagement`, `html`, `playwright`, `scorecard`, `scorecard-mcp`, `validation`, `web`
- **Validate an Idea** (`validate-idea`) -> `amazon-kendra-index`, `audit`, `aws-knowledge`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `code-examples`, `competitive-intelligence`, `compliance`, `context7`, `cost`
- **Define Product Strategy** (`define-product-strategy`) -> `amazon-kendra-index`, `aws-knowledge`, `code-examples`, `competitive-intelligence`, `context7`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`, `elasticsearch`, `extract`
- **Design Pricing and Monetization** (`design-pricing`) -> `apollo`, `attio`, `audit`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `cms`, `competitive-intelligence`, `compliance`, `content`, `cost`
- **Plan Go To Market Launch** (`plan-launch`) -> `apollo`, `attio`, `cms`, `competitive-intelligence`, `content`, `crm`, `customer-support`, `feature-flags`, `hubspot`, `insights`, `intercom`, `marketing`
- **Triage and Fix a Bug** (`triage-bug`) -> `analysis`, `architecture`, `bindings`, `context7`, `customer-support`, `debug`, `deployment`, `development`, `error-analysis`, `incident`, `intercom`, `playwright`
- **Reduce Technical Debt** (`reduce-technical-debt`) -> `aks`, `amazon`, `analysis`, `architecture`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`
- **Design an API** (`design-api`) -> `analysis`, `appsync`, `architecture`, `audit`, `authentication`, `aws-appsync`, `awslabs-iam`, `bindings`, `compliance`, `content`, `context7`, `debug`
- **Develop an Integration** (`develop-integration`) -> `aks`, `alfresco`, `amazon`, `anonymous`, `anurag`, `anuragd`, `apollo`, `appsync`, `arm`, `astra`, `atlan`, `audit`
- **Review Architecture** (`review-architecture`) -> `aks`, `amazon`, `analysis`, `architecture`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Write an ADR** (`write-adr`) -> `analysis`, `architecture`, `bindings`, `content`, `context7`, `debug`, `development`, `document`, `documentation`, `documents`, `docx`, `egnyte`
- **Provision Infrastructure** (`provision-infrastructure`) -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Engineer Internal Platform** (`engineer-platform`) -> `airlines`, `aks`, `amazon`, `analysis`, `appsignals`, `architecture`, `asana`, `asset-management`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`
- **Review Security** (`review-security`) -> `aks`, `amazon`, `analysis`, `architecture`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Model Threats** (`model-threats`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `compliance`, `context7`, `debug`, `development`, `error-analysis`, `iam`
- **Plan Tests** (`plan-tests`) -> `analysis`, `architecture`, `bindings`, `competitive-intelligence`, `context7`, `debug`, `development`, `error-analysis`, `feature-flags`, `incident`, `insights`, `metrics`
- **Automate Tests** (`automate-tests`) -> `aks`, `amazon`, `analysis`, `architecture`, `automation`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Test Performance** (`test-performance`) -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsignals`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Respond to Incident** (`respond-incident`) -> `airlines`, `aks`, `amazon`, `appsignals`, `asana`, `asset-management`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Write Postmortem** (`write-postmortem`) -> `airlines`, `appsignals`, `asana`, `asset-management`, `aws-location`, `awslabs-cloudwatch`, `awslabs-cloudwatch-appsignals`, `carbon`, `cloudflare-observability`, `cloudwatch`, `content`, `document`
- **Support Customer** (`support-customer`) -> `competitive-intelligence`, `customer-support`, `documentation`, `feature-flags`, `insights`, `intercom`, `metrics`, `planning`, `playwright`, `posthog`, `product`, `product-insights`
- **Analyze Customer Feedback** (`analyze-feedback`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `competitive-intelligence`
- **Analyze Growth** (`analyze-growth`) -> `amazon-neptune`, `analytics`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `cms`, `competitive-intelligence`, `content`, `cypher`
- **Support Sales** (`support-sales`) -> `apollo`, `attio`, `cms`, `competitive-intelligence`, `content`, `crm`, `document`, `documentation`, `documents`, `docx`, `egnyte`, `feature-flags`
- **Review Legal Compliance** (`review-compliance`) -> `audit`, `authentication`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `awslabs-iam`, `billing`, `competitive-intelligence`, `compliance`, `contracts`, `cost`, `dodo-payments`
- **Write Technical Documentation** (`write-technical-docs`) -> `aks`, `amazon`, `analysis`, `appsync`, `architecture`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Write User Documentation** (`write-user-docs`) -> `competitive-intelligence`, `content`, `customer-support`, `document`, `documentation`, `documents`, `docx`, `egnyte`, `feature-flags`, `insights`, `intercom`, `metrics`
- **Maintain Knowledge Base** (`maintain-knowledge-base`) -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `content`, `customer-support`, `document`, `documentation`, `documents`, `docx`, `e-commerce`
- **Optimize Costs** (`optimize-costs`) -> `aks`, `amazon`, `appsignals`, `audit`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`
- **Select Vendor** (`select-vendor`) -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `audit`, `aws-knowledge`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`
- **Plan Hiring** (`plan-hiring`) -> `airlines`, `analysis`, `architecture`, `asana`, `asset-management`, `aws-location`, `bindings`, `carbon`, `context7`, `debug`, `development`, `e-commerce`
- **Improve Team Process** (`improve-team-process`) -> `airlines`, `analysis`, `architecture`, `asana`, `asset-management`, `aws-location`, `bindings`, `carbon`, `competitive-intelligence`, `context7`, `debug`, `development`
