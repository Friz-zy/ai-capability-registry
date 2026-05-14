# Workflow Capability Registry

## Instruction Priority

When instructions conflict, use this priority order:

1. **User and project instructions** - direct user requests, `AGENTS.md`, local repo rules, and explicit constraints have highest priority.
2. **Selected workflows and process skills** - loaded workflow guidance defines how to approach the task when it matches.
3. **Selected implementation and domain skills** - loaded technology, tool, and artifact-specific guidance shapes execution.
4. **Generic agent behavior** - use only when no more specific instruction applies.

Prefer workflows and process skills before implementation and domain skills. Process guidance determines how to approach the task; implementation guidance determines how to execute it.

## Workflow Resolution Protocol

Before ordinary skill routing, decide whether a workflow applies by task first and role second:

1. **Extract intent** - identify action, domain, stack/tool, artifact, constraints, likely task, and optional role.
2. **Match task first** - match the request to one Task below; select a second Task only for clearly mixed requests.
3. **Use role as context** - select at most one Role below only when the user asks from that role perspective or it disambiguates the process.
4. **Read selected workflow guides** - read only the guide files for workflows matched by the selected task or role.
5. **Apply workflow guidance** - use the workflow to choose relevant process skills before implementation skills.
6. **Continue capability routing** - after workflow selection, resolve concrete skills through `skills/skills.md` and MCP servers through `mcp/mcp.md` when those entrypoints are available.

Read only workflow files that match the current task or role. Do not browse `workflows/` broadly.

### Subagent Scope

If you were dispatched as a subagent to execute a specific task, do not restart top-level workflow resolution. Follow the parent task instructions and any workflow or skill choices already provided.

Resolve additional workflows or skills only when they are directly needed for the assigned subtask.

### Skill Use Requirement

If a trusted or reviewed workflow or process skill plausibly matches the task after routing, use it before acting. Do not skip it because the task looks simple, because you want to inspect files first, or because the workflow feels like overhead.

If the loaded skill does not actually fit the task, stop using it and continue with the next best match.

## Roles

- **Personal AI Assistant**: `personal-assistant` -> none
- **Founder CEO Advisor**: `founder-ceo` -> none
- **CTO and Engineering Lead**: `cto-engineering-lead` -> `development`
- **Product Manager**: `product-manager` -> none
- **Software Engineer**: `software-engineer` -> `development`
- **Backend Engineer**: `backend-engineer` -> `development`
- **Frontend Engineer**: `frontend-engineer` -> `development`
- **Mobile and Desktop Engineer**: `mobile-engineer` -> `development`
- **QA Engineer**: `qa-engineer` -> `development`
- **Security Engineer**: `security-engineer` -> `development`
- **DevOps and Platform Engineer**: `devops-platform-engineer` -> `development`
- **SRE Incident Manager**: `sre-incident-manager` -> `development`
- **Data Analyst**: `data-analyst` -> none
- **AI Engineer**: `ai-engineer` -> `development`
- **Product Designer**: `designer` -> none
- **Marketing and Growth Lead**: `marketing-growth` -> none
- **Sales Account Executive**: `sales-account-executive` -> none
- **Customer Success and Support Specialist**: `customer-success-support` -> none
- **Finance Operations Analyst**: `finance-ops` -> none
- **Legal Operations Assistant**: `legal-ops` -> none
- **People Operations and Recruiting Partner**: `people-ops-recruiting` -> none
- **Operations Manager**: `operations-manager` -> none
- **AI Agent Builder and Pipeline Orchestrator**: `ai-agent-builder` -> `development`
- **Creative Media Producer**: `creative-media-producer` -> none
- **Data Engineer**: `data-engineer` -> `development`
- **Cloud Infrastructure Engineer**: `cloud-infrastructure-engineer` -> `development`
- **Blockchain Engineer**: `blockchain-engineer` -> `development`
- **Hardware and IoT Engineer**: `hardware-iot-engineer` -> `development`

## Tasks

- **Plan a Feature or Spec**: `plan-feature` -> `development`
- **Implement or Refactor Code**: `implement-code` -> `development`
- **Review Code or PR**: `review-code` -> `development`
- **Debug an Issue or Incident**: `debug-incident` -> `development`
- **Test and Validate**: `test-validate` -> `development`
- **Security Audit or Threat Model**: `security-audit` -> `development`
- **Build Frontend or UI**: `build-frontend` -> `development`
- **Build Backend or Integration**: `build-backend` -> `development`
- **Deploy or Release**: `deploy-release` -> `development`
- **Analyze Data or Metrics**: `analyze-data` -> none
- **Research and Brief**: `research-brief` -> none
- **Build Agent Automation**: `automate-agent` -> `development`
- **Write Docs or Documents**: `write-documents` -> none
- **Manage Product or Project**: `manage-project` -> none
- **Support Customers or Sales**: `customer-sales` -> none
- **Finance, Compliance, or Legal**: `finance-legal` -> none
- **People Operations**: `people-ops` -> none
- **Personal Productivity**: `personal-productivity` -> none
- **Create or Edit Media**: `create-media` -> none
- **Manage Data Systems**: `manage-data-systems` -> `development`
- **Manage Cloud Infrastructure**: `manage-cloud-infra` -> `development`
- **Build Blockchain or Smart Contracts**: `build-blockchain` -> `development`
- **Build Hardware or IoT**: `build-hardware-iot` -> `development`
- **Build Mobile or Desktop App**: `build-mobile-desktop` -> `development`

## Workflows

### Development Workflow

Select process guidance for software development tasks before implementation or domain skills.

**ID:** `development`
**Guide:** `workflows/development.md`
**Categories:** `engineering`, `quality`, `delivery`
**Matched tasks:** `plan-feature`, `implement-code`, `review-code`, `debug-incident`, `test-validate`, `security-audit`, `build-frontend`, `build-backend`, `deploy-release`, `automate-agent`, `manage-data-systems`, `manage-cloud-infra`, `build-blockchain`, `build-hardware-iot`, `build-mobile-desktop`
**Matched roles:** `cto-engineering-lead`, `software-engineer`, `backend-engineer`, `frontend-engineer`, `mobile-engineer`, `qa-engineer`, `security-engineer`, `devops-platform-engineer`, `sre-incident-manager`, `ai-engineer`, `ai-agent-builder`, `data-engineer`, `cloud-infrastructure-engineer`, `blockchain-engineer`, `hardware-iot-engineer`
