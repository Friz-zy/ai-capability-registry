# MCP Capability Registry

## MCP Resolution Protocol

1. **Extract intent** - identify the target technology, service, SaaS product, data domain, action type, and sensitivity.
2. **Route by task first** - match the request to one task listed in `mcp.md`; select a second task only for clearly mixed workflows.
3. **Use role as context** - select at most one role listed in `mcp.md` only when it disambiguates service/platform scope.
4. **Read selected indexes only** - open only the matched `mcp/catalog/tasks/<task-id>/servers.md` and optional `mcp/catalog/roles/<role-id>/servers.md`.
5. **Choose keywords** - select 1-3 exact keywords from those indexes; prefer service names over broad domains.
6. **Read keyword catalogs** - open only selected `mcp/catalog/keywords/<keyword>/servers.md` files.
7. **Read server files** - follow `mcp/servers/<server>/SKILL.md`.
8. **Select MCP only if you can work with it** - Select a hosted HTTPS MCP channel only when the current agent can connect to HTTPS through built-in MCP/web tools or approved commands such as `curl`. Select a docker MCP only when the current agent can run docker commands.
9. **Confirm authorization** - if OAuth, API keys, tokens, account access, or workspace access are required, ask the user before connecting.
10. **Connect safely** - use only allowed transport and never hardcode secrets. Use environment variables or vault integration.

## MCP Runtime Instructions

After selecting an MCP server via the resolution protocol above, read the appropriate runtime guide:

- **No prior MCP knowledge**: Only if you don't know about MCP servers, read `mcp/common.md` for general MCP concepts, tool discovery, response handling, and error diagnostics.
- **HTTPS / SSE MCP server**: Read `mcp/web.md` for HTTPS API connection, authentication methods, and health checks.
- **Docker MCP server**: Read `mcp/docker.md` for container naming, lifecycle management, connection, and cleanup.

### Roles (category groupings)

- **Personal AI Assistant**: `mcp/catalog/roles/personal-assistant/servers.md` -> `access`, `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `context7`, `deepwiki`, `directory`, `discovery`, `documentation`
- **Founder CEO Advisor**: `mcp/catalog/roles/founder-ceo/servers.md` -> `apollo`, `attio`, `audit`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `cms`, `competitive-intelligence`, `compliance`, `content`, `cost`
- **CTO and Engineering Lead**: `mcp/catalog/roles/cto-engineering-lead/servers.md` -> `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `appsignals`, `appsync`
- **Product Manager**: `mcp/catalog/roles/product-manager/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-diagram`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-nova-canvas`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`
- **Software Engineer**: `mcp/catalog/roles/software-engineer/servers.md` -> `access`, `analysis`, `appsync`, `architecture`, `astro`, `automation`, `aws-appsync`, `bindings`, `browserbase`, `communication`, `context7`, `debug`
- **Backend Engineer**: `mcp/catalog/roles/backend-engineer/servers.md` -> `actions`, `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `atlassian`, `atlassian-atlassian`, `audit`, `authentication`, `aws`, `aws-appsync`
- **Frontend Engineer**: `mcp/catalog/roles/frontend-engineer/servers.md` -> `actions`, `astro`, `atlassian`, `atlassian-atlassian`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code`, `code-examples`, `command`
- **Mobile and Desktop Engineer**: `mcp/catalog/roles/mobile-engineer/servers.md` -> `actions`, `android`, `androidmanagement`, `astro`, `atlassian`, `atlassian-atlassian`, `browserbase`, `code`, `code-examples`, `command`, `context7`, `developer-portal`
- **QA Engineer**: `mcp/catalog/roles/qa-engineer/servers.md` -> `access`, `actions`, `analysis`, `appsync`, `astro`, `atlassian`, `atlassian-atlassian`, `automation`, `aws-appsync`, `browserbase`, `code`, `code-examples`
- **Security Engineer**: `mcp/catalog/roles/security-engineer/servers.md` -> `audit`, `authentication`, `awslabs-iam`, `compliance`, `iam`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `policy`, `security`, `semgrep`
- **DevOps and Platform Engineer**: `mcp/catalog/roles/devops-platform-engineer/servers.md` -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **SRE Incident Manager**: `mcp/catalog/roles/sre-incident-manager/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsignals`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Data Analyst**: `mcp/catalog/roles/data-analyst/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `competitive-intelligence`
- **AI Engineer**: `mcp/catalog/roles/ai-engineer/servers.md` -> `agent`, `agentcore`, `ai`, `ai-assistant`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `architecture`, `audit`, `authentication`, `aws-bedrock`
- **Product Designer**: `mcp/catalog/roles/designer/servers.md` -> `amazon-kendra-index`, `astro`, `aws-diagram`, `aws-knowledge`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `code-examples`, `context7`, `deepwiki`, `design`
- **Marketing and Growth Lead**: `mcp/catalog/roles/marketing-growth/servers.md` -> `amazon-neptune`, `analytics`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `cms`, `content`, `cypher`, `dashboard`
- **Sales Account Executive**: `mcp/catalog/roles/sales-account-executive/servers.md` -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `deepwiki`, `directory`, `discovery`
- **Customer Success and Support Specialist**: `mcp/catalog/roles/customer-success-support/servers.md` -> `amazon-kendra-index`, `aws-knowledge`, `code-examples`, `competitive-intelligence`, `context7`, `customer-support`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`, `elasticsearch`
- **Finance Operations Analyst**: `mcp/catalog/roles/finance-ops/servers.md` -> `airlines`, `asana`, `asset-management`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`, `compliance`, `cost`
- **Legal Operations Assistant**: `mcp/catalog/roles/legal-ops/servers.md` -> `compliance`, `contracts`, `policy`
- **People Operations and Recruiting Partner**: `mcp/catalog/roles/people-ops-recruiting/servers.md` -> `health`, `indeed`, `recruiting`
- **Operations Manager**: `mcp/catalog/roles/operations-manager/servers.md` -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `aws-knowledge`, `aws-location`, `carbon`, `code-examples`, `context7`, `customer-support`, `deepwiki`, `directory`
- **AI Agent Builder and Pipeline Orchestrator**: `mcp/catalog/roles/ai-agent-builder/servers.md` -> `access`, `agent`, `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `architecture`
- **Creative Media Producer**: `mcp/catalog/roles/creative-media-producer/servers.md` -> `audio`, `aws-diagram`, `awslabs-nova-canvas`, `canva`, `canvas`, `carbon-voice`, `cloudinary`, `cms`, `content`, `design`, `diagram`, `document`
- **Data Engineer**: `mcp/catalog/roles/data-engineer/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Cloud Infrastructure Engineer**: `mcp/catalog/roles/cloud-infrastructure-engineer/servers.md` -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Blockchain Engineer**: `mcp/catalog/roles/blockchain-engineer/servers.md` -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `blockchain`, `cairo`, `compliance`, `context7`, `contracts`, `crypto`
- **Hardware and IoT Engineer**: `mcp/catalog/roles/hardware-iot-engineer/servers.md` -> `aks`, `amazon`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`

### Tasks (workflow entry points)

- **Plan a Feature or Spec**: `mcp/catalog/tasks/plan-feature/servers.md` -> `access`, `analysis`, `architecture`, `automation`, `aws-diagram`, `awslabs-nova-canvas`, `bindings`, `canva`, `canvas`, `communication`, `competitive-intelligence`, `context7`
- **Implement or Refactor Code**: `mcp/catalog/tasks/implement-code/servers.md` -> `analysis`, `appsync`, `architecture`, `astro`, `aws-appsync`, `bindings`, `browserbase`, `context7`, `debug`, `development`, `documentation`, `error-analysis`
- **Review Code or PR**: `mcp/catalog/tasks/review-code/servers.md` -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `compliance`, `context7`, `debug`, `development`, `error-analysis`, `iam`
- **Debug an Issue or Incident**: `mcp/catalog/tasks/debug-incident/servers.md` -> `access`, `aks`, `amazon`, `analysis`, `appsignals`, `architecture`, `automation`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`
- **Test and Validate**: `mcp/catalog/tasks/test-validate/servers.md` -> `access`, `analysis`, `automation`, `communication`, `documentation`, `generate`, `integration`, `management`, `migration`, `optimization`, `planning`, `playwright`
- **Security Audit or Threat Model**: `mcp/catalog/tasks/security-audit/servers.md` -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `compliance`, `context7`, `debug`, `development`, `error-analysis`, `iam`
- **Build Frontend or UI**: `mcp/catalog/tasks/build-frontend/servers.md` -> `astro`, `aws-diagram`, `awslabs-nova-canvas`, `browserbase`, `canva`, `canvas`, `context7`, `design`, `diagram`, `figma`, `googleapis-design`, `html`
- **Build Backend or Integration**: `mcp/catalog/tasks/build-backend/servers.md` -> `actions`, `alfresco`, `anonymous`, `anurag`, `anuragd`, `apollo`, `appsync`, `arm`, `astra`, `atlan`, `atlassian`, `atlassian-atlassian`
- **Deploy or Release**: `mcp/catalog/tasks/deploy-release/servers.md` -> `access`, `aks`, `amazon`, `analysis`, `appsignals`, `automation`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`
- **Analyze Data or Metrics**: `mcp/catalog/tasks/analyze-data/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `awslabs-dynamodb`, `awslabs-elasticache`, `awslabs-redshift`, `awslabs-timestream-influxdb`, `bigquery`, `bigtableadmin`, `code-examples`, `context7`
- **Research and Brief**: `mcp/catalog/tasks/research-brief/servers.md` -> `access`, `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `content`, `context7`, `deepwiki`, `directory`, `discovery`
- **Build Agent Automation**: `mcp/catalog/tasks/automate-agent/servers.md` -> `access`, `actions`, `agent`, `agentcore`, `ai`, `ai-assistant`, `alfresco`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `amazon-qbusiness-anonymous`, `analysis`, `anonymous`
- **Write Docs or Documents**: `mcp/catalog/tasks/write-documents/servers.md` -> `access`, `analysis`, `automation`, `cms`, `communication`, `content`, `document`, `documentation`, `documents`, `docx`, `egnyte`, `generate`
- **Manage Product or Project**: `mcp/catalog/tasks/manage-project/servers.md` -> `access`, `airlines`, `analysis`, `asana`, `asset-management`, `automation`, `aws-location`, `carbon`, `communication`, `competitive-intelligence`, `documentation`, `e-commerce`
- **Support Customers or Sales**: `mcp/catalog/tasks/customer-sales/servers.md` -> `amazon-kendra-index`, `apollo`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `customer-support`, `deepwiki`, `directory`
- **Finance, Compliance, or Legal**: `mcp/catalog/tasks/finance-legal/servers.md` -> `airlines`, `asana`, `asset-management`, `audit`, `aws-location`, `aws-pricing`, `awslabs-billing-cost`, `awslabs-cost-explorer`, `billing`, `carbon`, `compliance`, `contracts`
- **People Operations**: `mcp/catalog/tasks/people-ops/servers.md` -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `e-commerce`, `googleapis-mapstools`, `health`, `indeed`, `location`, `management`, `maps`
- **Personal Productivity**: `mcp/catalog/tasks/personal-productivity/servers.md` -> `airlines`, `asana`, `asset-management`, `aws-location`, `carbon`, `communication`, `dialer`, `e-commerce`, `googleapis-mapstools`, `location`, `management`, `maps`
- **Create or Edit Media**: `mcp/catalog/tasks/create-media/servers.md` -> `audio`, `aws-diagram`, `awslabs-nova-canvas`, `canva`, `canvas`, `carbon-voice`, `cloudinary`, `design`, `diagram`, `face`, `figma`, `googleapis-design`
- **Manage Data Systems**: `mcp/catalog/tasks/manage-data-systems/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `appsync`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Manage Cloud Infrastructure**: `mcp/catalog/tasks/manage-cloud-infra/servers.md` -> `aks`, `amazon`, `appsignals`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`
- **Build Blockchain or Smart Contracts**: `mcp/catalog/tasks/build-blockchain/servers.md` -> `analysis`, `architecture`, `audit`, `authentication`, `awslabs-iam`, `bindings`, `blockchain`, `cairo`, `compliance`, `context7`, `contracts`, `crypto`
- **Build Hardware or IoT**: `mcp/catalog/tasks/build-hardware-iot/servers.md` -> `aks`, `amazon`, `audit`, `authentication`, `aws`, `aws-appsync`, `aws-bedrock`, `aws-cdk`, `aws-core`, `aws-dataprocessing`, `aws-diagram`, `aws-healthomics`
- **Build Mobile or Desktop App**: `mcp/catalog/tasks/build-mobile-desktop/servers.md` -> `android`, `androidmanagement`, `astro`, `browserbase`, `context7`, `googleapis-androidmanagement`, `html`, `playwright`, `scorecard`, `scorecard-mcp`, `validation`, `web`

## Policy

- Use an MCP server only when the task directly involves its technology, service, SaaS product, or data domain.
- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default. Ask before write operations unless the user explicitly requested them.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- If authentication, OAuth, API keys, tokens, or account access are required, ask the user before connecting or requesting credentials.
- Never expose secret values in prompts, logs, commits, or generated docs.
- Do not use direct `node`, `npx`, `python`, `pip`, or `uvx` MCP runners.
