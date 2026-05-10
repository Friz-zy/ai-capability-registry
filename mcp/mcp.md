# MCP Capability Registry

## MCP Resolution Protocol

Before connecting an MCP server, resolve it with progressive disclosure:

1. **Extract intent** - identify the target technology, service, SaaS product, data domain, action type, and sensitivity.
2. **Route by task first** - match the request to one task listed in `mcp.md`; select a second task only for clearly mixed workflows.
3. **Use role as context** - select at most one role listed in `mcp.md` only when it disambiguates service/platform scope.
4. **Read selected indexes only** - open only the matched `mcp/catalog/tasks/<task-id>/servers.md` and optional `mcp/catalog/roles/<role-id>/servers.md`.
5. **Choose keywords** - select 1-3 exact keywords from those indexes; prefer service names over broad domains.
6. **Read keyword catalogs** - open only selected `mcp/catalog/keywords/<keyword>/servers.md` files.
7. **Read server files** - follow `mcp/servers/<server>/SKILL.md`.
8. **Confirm authorization** - if OAuth, API keys, tokens, account access, or workspace access are required, ask the user before connecting.
9. **Connect safely** - use only allowed transport and never hardcode secrets. Use environment variables or vault integration.

### Roles (category groupings)

- **Personal AI Assistant**: `mcp/catalog/roles/personal-assistant/servers.md` -> `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `context7`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`
- **Founder CEO Advisor**: `mcp/catalog/roles/founder-ceo/servers.md` -> `attio`, `cms`, `competitive-intelligence`, `content`, `crm`, `dodo-payments`, `feature-flags`, `finance`, `forecast`, `hubspot`, `indeed`, `marketing`
- **CTO and Engineering Lead**: `mcp/catalog/roles/cto-engineering-lead/servers.md` -> `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `analysis`, `astro`, `authentication`, `aws`, `aws-knowledge`
- **Product Manager**: `mcp/catalog/roles/product-manager/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `bigquery`, `canva`, `code-examples`, `competitive-intelligence`, `context7`, `customer-support`, `cypher`, `dashboard`
- **Software Engineer**: `mcp/catalog/roles/software-engineer/servers.md` -> `analysis`, `astro`, `automation`, `bindings`, `communication`, `development`, `documentation`, `error-analysis`, `incident`, `management`, `oauth`, `planning`
- **Backend Engineer**: `mcp/catalog/roles/backend-engineer/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `bigquery`, `cloudflare`, `cloudflare-observability`
- **Frontend Engineer**: `mcp/catalog/roles/frontend-engineer/servers.md` -> `astro`, `canva`, `design`, `scorecard`, `scorecard-mcp`, `validation`, `web`, `web-scraping`, `webzum`
- **Mobile and Desktop Engineer**: `mcp/catalog/roles/mobile-engineer/servers.md` -> `astro`, `scorecard`, `scorecard-mcp`, `validation`, `web`, `web-scraping`, `webzum`
- **QA Engineer**: `mcp/catalog/roles/qa-engineer/servers.md` -> `analysis`, `astro`, `automation`, `communication`, `documentation`, `management`, `oauth`, `planning`, `scorecard`, `scorecard-mcp`, `validation`, `web`
- **Security Engineer**: `mcp/catalog/roles/security-engineer/servers.md` -> `authentication`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `security`, `semgrep`, `stytch`, `threat-intelligence`
- **DevOps and Platform Engineer**: `mcp/catalog/roles/devops-platform-engineer/servers.md` -> `aks`, `amazon`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `deployment`, `error-analysis`
- **SRE Incident Manager**: `mcp/catalog/roles/sre-incident-manager/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `bigquery`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`
- **Data Analyst**: `mcp/catalog/roles/data-analyst/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `bigquery`, `code-examples`, `competitive-intelligence`, `context7`, `cypher`, `dashboard`, `data`, `database`
- **AI Engineer**: `mcp/catalog/roles/ai-engineer/servers.md` -> `agentcore`, `ai`, `ai-assistant`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `analysis`, `authentication`, `aws-knowledge`, `bedrock`, `bindings`, `code-examples`, `context7`
- **Product Designer**: `mcp/catalog/roles/designer/servers.md` -> `amazon-kendra-index`, `astro`, `aws-knowledge`, `canva`, `code-examples`, `context7`, `deepwiki`, `design`, `directory`, `discovery`, `documentation`, `ean-search`
- **Marketing and Growth Lead**: `mcp/catalog/roles/marketing-growth/servers.md` -> `amazon-neptune`, `analytics`, `bigquery`, `cms`, `content`, `cypher`, `dashboard`, `data`, `database`, `databases`, `dataset`, `finance`
- **Sales Account Executive**: `mcp/catalog/roles/sales-account-executive/servers.md` -> `amazon-kendra-index`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `deepwiki`, `directory`, `discovery`, `documentation`
- **Customer Success and Support Specialist**: `mcp/catalog/roles/customer-success-support/servers.md` -> `amazon-kendra-index`, `aws-knowledge`, `code-examples`, `competitive-intelligence`, `context7`, `customer-support`, `deepwiki`, `directory`, `discovery`, `documentation`, `ean-search`, `extract`
- **Finance Operations Analyst**: `mcp/catalog/roles/finance-ops/servers.md` -> `airlines`, `asana`, `asset-management`, `carbon`, `dodo-payments`, `e-commerce`, `finance`, `management`, `mercadopago`, `metro`, `metro-mcp`, `monday`
- **Legal Operations Assistant**: `mcp/catalog/roles/legal-ops/servers.md` -> `contracts`
- **People Operations and Recruiting Partner**: `mcp/catalog/roles/people-ops-recruiting/servers.md` -> `indeed`, `recruiting`
- **Operations Manager**: `mcp/catalog/roles/operations-manager/servers.md` -> `airlines`, `amazon-kendra-index`, `asana`, `asset-management`, `aws-knowledge`, `carbon`, `code-examples`, `context7`, `customer-support`, `deepwiki`, `directory`, `discovery`
- **AI Agent Builder and Pipeline Orchestrator**: `mcp/catalog/roles/ai-agent-builder/servers.md` -> `agentcore`, `ai`, `ai-assistant`, `aks`, `amazon`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `analysis`, `authentication`, `automation`, `aws`, `aws-knowledge`
- **Creative Media Producer**: `mcp/catalog/roles/creative-media-producer/servers.md` -> `canva`, `carbon-voice`, `cloudinary`, `cms`, `content`, `design`, `document`, `documentation`, `documents`, `egnyte`, `face`, `invideo`
- **Data Engineer**: `mcp/catalog/roles/data-engineer/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `bigquery`, `cloudflare`, `cloudflare-observability`
- **Cloud Infrastructure Engineer**: `mcp/catalog/roles/cloud-infrastructure-engineer/servers.md` -> `aks`, `amazon`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `deployment`, `error-analysis`
- **Blockchain Engineer**: `mcp/catalog/roles/blockchain-engineer/servers.md` -> `analysis`, `authentication`, `bindings`, `blockchain`, `cairo`, `contracts`, `crypto`, `development`, `error-analysis`, `incident`, `malware`, `malware-patrol`
- **Hardware and IoT Engineer**: `mcp/catalog/roles/hardware-iot-engineer/servers.md` -> `aks`, `amazon`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `deployment`, `hosting`

### Tasks (workflow entry points)

- **Plan a Feature or Spec**: `mcp/catalog/tasks/plan-feature/servers.md` -> `analysis`, `automation`, `bindings`, `canva`, `communication`, `competitive-intelligence`, `design`, `development`, `documentation`, `error-analysis`, `feature-flags`, `incident`
- **Implement or Refactor Code**: `mcp/catalog/tasks/implement-code/servers.md` -> `analysis`, `astro`, `bindings`, `development`, `documentation`, `error-analysis`, `incident`, `oauth`, `scorecard`, `scorecard-mcp`, `semgrep`, `validation`
- **Review Code or PR**: `mcp/catalog/tasks/review-code/servers.md` -> `analysis`, `authentication`, `bindings`, `development`, `error-analysis`, `incident`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `scorecard`, `scorecard-mcp`
- **Debug an Issue or Incident**: `mcp/catalog/tasks/debug-incident/servers.md` -> `aks`, `amazon`, `analysis`, `automation`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `bindings`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`
- **Test and Validate**: `mcp/catalog/tasks/test-validate/servers.md` -> `analysis`, `automation`, `communication`, `documentation`, `management`, `planning`, `scorecard`, `scorecard-mcp`, `validation`, `workflow`
- **Security Audit or Threat Model**: `mcp/catalog/tasks/security-audit/servers.md` -> `analysis`, `authentication`, `bindings`, `development`, `error-analysis`, `incident`, `malware`, `malware-patrol`, `malwarepatrol`, `oauth`, `security`, `semgrep`
- **Build Frontend or UI**: `mcp/catalog/tasks/build-frontend/servers.md` -> `astro`, `canva`, `design`, `scorecard`, `scorecard-mcp`, `validation`, `web`, `web-scraping`, `webzum`
- **Build Backend or Integration**: `mcp/catalog/tasks/build-backend/servers.md` -> `actions`, `alfresco`, `anurag`, `anuragd`, `awesome`, `bgpt`, `big`, `cloudflare`, `code-examples`, `composio`, `context-awesome`, `cortex`
- **Deploy or Release**: `mcp/catalog/tasks/deploy-release/servers.md` -> `aks`, `amazon`, `analysis`, `automation`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `communication`
- **Analyze Data or Metrics**: `mcp/catalog/tasks/analyze-data/servers.md` -> `amazon-kendra-index`, `amazon-neptune`, `analytics`, `aws-knowledge`, `bigquery`, `code-examples`, `context7`, `cypher`, `dashboard`, `data`, `database`, `databases`
- **Research and Brief**: `mcp/catalog/tasks/research-brief/servers.md` -> `amazon-kendra-index`, `analysis`, `automation`, `aws-knowledge`, `code-examples`, `communication`, `content`, `context7`, `deepwiki`, `directory`, `discovery`, `document`
- **Build Agent Automation**: `mcp/catalog/tasks/automate-agent/servers.md` -> `actions`, `agentcore`, `ai`, `ai-assistant`, `alfresco`, `amazon-bedrock-agentcore`, `amazon-kendra-index`, `analysis`, `anurag`, `anuragd`, `automation`, `awesome`
- **Write Docs or Documents**: `mcp/catalog/tasks/write-documents/servers.md` -> `analysis`, `automation`, `cms`, `communication`, `content`, `document`, `documentation`, `documents`, `egnyte`, `management`, `marketing`, `mercado-libre`
- **Manage Product or Project**: `mcp/catalog/tasks/manage-project/servers.md` -> `airlines`, `analysis`, `asana`, `asset-management`, `automation`, `carbon`, `communication`, `competitive-intelligence`, `documentation`, `e-commerce`, `feature-flags`, `management`
- **Support Customers or Sales**: `mcp/catalog/tasks/customer-sales/servers.md` -> `amazon-kendra-index`, `attio`, `aws-knowledge`, `cms`, `code-examples`, `content`, `context7`, `crm`, `customer-support`, `deepwiki`, `directory`, `discovery`
- **Finance, Compliance, or Legal**: `mcp/catalog/tasks/finance-legal/servers.md` -> `airlines`, `asana`, `asset-management`, `carbon`, `contracts`, `dodo-payments`, `e-commerce`, `finance`, `management`, `mercadopago`, `metro`, `metro-mcp`
- **People Operations**: `mcp/catalog/tasks/people-ops/servers.md` -> `airlines`, `asana`, `asset-management`, `carbon`, `e-commerce`, `indeed`, `management`, `metro`, `metro-mcp`, `monday`, `project-management`, `recruiting`
- **Personal Productivity**: `mcp/catalog/tasks/personal-productivity/servers.md` -> `airlines`, `asana`, `asset-management`, `carbon`, `communication`, `dialer`, `e-commerce`, `management`, `metro`, `metro-mcp`, `monday`, `notion`
- **Create or Edit Media**: `mcp/catalog/tasks/create-media/servers.md` -> `canva`, `carbon-voice`, `cloudinary`, `design`, `face`, `invideo`, `media`, `social-media`, `video`, `voice`
- **Manage Data Systems**: `mcp/catalog/tasks/manage-data-systems/servers.md` -> `aks`, `amazon`, `amazon-neptune`, `analytics`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `bigquery`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`
- **Manage Cloud Infrastructure**: `mcp/catalog/tasks/manage-cloud-infra/servers.md` -> `aks`, `amazon`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `deployment`, `error-analysis`
- **Build Blockchain or Smart Contracts**: `mcp/catalog/tasks/build-blockchain/servers.md` -> `analysis`, `authentication`, `bindings`, `blockchain`, `cairo`, `contracts`, `crypto`, `development`, `error-analysis`, `incident`, `malware`, `malware-patrol`
- **Build Hardware or IoT**: `mcp/catalog/tasks/build-hardware-iot/servers.md` -> `aks`, `amazon`, `authentication`, `aws`, `aws-knowledge`, `awslabs`, `azure`, `cloudflare`, `cloudflare-observability`, `cloudflare-workers`, `deployment`, `hosting`
- **Build Mobile or Desktop App**: `mcp/catalog/tasks/build-mobile-desktop/servers.md` -> `astro`, `scorecard`, `scorecard-mcp`, `validation`, `web`, `web-scraping`, `webzum`

## Policy

- Use an MCP server only when the task directly involves its technology, service, SaaS product, or data domain.
- Use the MCP tools only for the user-requested service workflow and prefer read-only operations by default. Ask before write operations unless the user explicitly requested them.
- Confirm the target account, workspace, project, repository, or dataset before actions that can read private data or mutate remote state.
- If authentication, OAuth, API keys, tokens, or account access are required, ask the user before connecting or requesting credentials.
- Never expose secret values in prompts, logs, commits, or generated docs.
- Use only public HTTPS endpoints or Docker stdio commands that start with `docker run --rm`.
- Select a hosted HTTPS MCP channel only when the current agent can connect to HTTPS through built-in MCP/web tools or approved commands such as `curl`.
- Select a Docker stdio MCP channel only when the current agent can run Docker commands in the current environment.
- Do not use direct `node`, `npx`, `python`, `pip`, or `uvx` MCP runners.
- For Docker servers, launch only through the generated `docker run --rm ...` command. Confirm required environment variables before launching the container.
- For Docker stdio mode, keep stdin attached with `-i` and run the container in the foreground; do not use detached mode (`-d`) for stdio MCP servers.
- Give MCP docker containers clear names such as `mcp-<server-id>` when a named container is needed, so running containers can be identified safely.
- Before starting a Docker MCP container, check `docker ps` for an existing matching MCP container and reuse it when the server supports stdio attach/exec; otherwise start a fresh generated stdio command.
- Stop or remove Docker MCP containers you started at the end of the session unless they were already running before the session or the user explicitly asks to keep them.
- Do not use unsafe Docker options for MCP servers, including `--privileged`, host filesystem mounts such as `-v /:/host` or `--mount type=bind,source=/`, host networking with `--network host`, or mounting sensitive paths like `/var/run/docker.sock`, `~/.ssh`, or cloud credential directories.
