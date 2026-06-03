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
- **Founder CEO Advisor** (`founder-ceo`) -> `apollo`, `attio`, `audit`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `cms`, `competitive-intelligence`, `compliance`, `content`, `cost`
- **CTO and Engineering Lead** (`cto-engineering-lead`) -> `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `appsignals`, `appsync`
- **Product Manager** (`product-manager`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-diagram`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-nova-canvas`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`
- **Software Engineer** (`software-engineer`) -> `access`, `analysis`, `appsync`, `architecture`, `astro`, `automation`, `aws-appsync`, `bindings`, `browserbase`, `communication`, `context7`, `debug`
- **Backend Engineer** (`backend-engineer`) -> `actions`, `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `atlassian`, `atlassian-atlassian`, `audit`, `authentication`, `aws`, `aws-appsync`
- **Frontend Engineer** (`frontend-engineer`) -> `actions`, `astro`, `atlassian`, `atlassian-atlassian`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code`, `code-examples`, `command`
- **Mobile and Desktop Engineer** (`mobile-engineer`) -> `actions`, `android`, `androidmanagement`, `astro`, `atlassian`, `atlassian-atlassian`, `browserbase`, `code`, `code-examples`, `command`, `context7`, `developer-portal`
- **QA Engineer** (`qa-engineer`) -> `access`, `actions`, `analysis`, `appsync`, `astro`, `atlassian`, `atlassian-atlassian`, `automation`, `aws-appsync`, `browserbase`, `code`, `code-examples`
- **Security Engineer** (`security-engineer`) -> `audit`, `authentication`, `awslabs-iam`, `compliance`, `iam`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `policy`, `security`, `semgrep`
- **DevOps and Platform Engineer** (`devops-platform-engineer`) -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **SRE Incident Manager** (`sre-incident-manager`) -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsignals`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Data Analyst** (`data-analyst`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `competitive-intelligence`
- **AI Engineer** (`ai-engineer`) -> `agent`, `agentcore`, `ai`, `ai-assistant`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `architecture`, `audit`, `authentication`, `aws-bedrock`
- **Product Designer** (`designer`) -> `amazon-kendra-index`, `astro`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code-examples`, `context7`, `deepwiki`, `design`
- **Business Analyst** (`business-analyst`) -> `airlines`, `amazon-kendra-index`, `amazon-neptune`, `analytics`, `asana`, `asset-management`, `aws-knowledge`, `aws-location`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`
- **UX Researcher** (`ux-researcher`) -> `amazon-kendra-index`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `canva`, `canvas`, `code-examples`, `competitive-intelligence`, `context7`, `deepwiki`, `design`, `diagram`
- **UX Designer** (`ux-designer`) -> `amazon-kendra-index`, `astro`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code-examples`, `context7`, `deepwiki`, `design`
- **UI Designer** (`ui-designer`) -> `astro`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `design`, `diagram`, `figma`, `googleapis-design`, `html`, `web`
- **Solution Architect** (`solution-architect`) -> `aks`, `amazon`, `analysis`, `appsync`, `architecture`, `astro`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`
- **Tech Lead** (`tech-lead`) -> `aks`, `amazon`, `analysis`, `appsync`, `architecture`, `astro`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`
- **Software Development Engineer in Test** (`sdet`) -> `actions`, `analysis`, `appsync`, `architecture`, `astro`, `atlassian`, `atlassian-atlassian`, `aws-appsync`, `bindings`, `browserbase`, `code`, `code-examples`
- **Performance Engineer** (`performance-engineer`) -> `aks`, `amazon`, `analysis`, `appsignals`, `architecture`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Release Manager** (`release-manager`) -> `airlines`, `aks`, `amazon`, `asana`, `asset-management`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Product Analyst** (`product-analyst`) -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `competitive-intelligence`
- **Marketing and Growth Lead** (`marketing-growth`) -> `amazon-neptune`, `analytics`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `cms`, `content`, `cypher`, `dashboard`
- **Sales Account Executive** (`sales-account-executive`) -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `deepwiki`, `directory`, `discovery`
- **Customer Success and Support Specialist** (`customer-success-support`) -> `amazon-kendra-index`, `aws-knowledge`, `code-examples`, `competitive-intelligence`, `context7`, `customer-support`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`, `elasticsearch`
- **Finance Operations Analyst** (`finance-ops`) -> `airlines`, `asana`, `asset-management`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`, `compliance`, `cost`
- **Legal Operations Assistant** (`legal-ops`) -> `compliance`, `contracts`, `policy`
- **People Operations and Recruiting Partner** (`people-ops-recruiting`) -> `health`, `indeed`, `recruiting`
- **Operations Manager** (`operations-manager`) -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `aws-knowledge`, `aws-location`, `carbon`, `code-examples`, `context7`, `customer-support`, `deepwiki`, `directory`
- **AI Agent Builder and Pipeline Orchestrator** (`ai-agent-builder`) -> `access`, `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `architecture`
- **Creative Media Producer** (`creative-media-producer`) -> `audio`, `aws-diagram`, `awslabs-nova-canvas`, `canva`, `canvas`, `carbon-voice`, `cloudinary`, `cms`, `content`, `design`, `diagram`, `document`
- **Data Engineer** (`data-engineer`) -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Cloud Infrastructure Engineer** (`cloud-infrastructure-engineer`) -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Blockchain Engineer** (`blockchain-engineer`) -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `blockchain`, `cairo`, `compliance`, `context7`, `contracts`, `crypto`
- **Hardware and IoT Engineer** (`hardware-iot-engineer`) -> `aks`, `amazon`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`

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
