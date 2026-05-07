# risks

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### agentic-actions-auditor
Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

### code-maturity-assessor
Systematic code maturity assessment using Trail of Bits' 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing. Produces professional scorecard with evidence-based ratings and actionable recommendations.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

### code-review
Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`

### comp-analysis
Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`

### legal-risk-assessment
Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, classifying issues by severity, or determining whether a matter needs senior counsel or outside legal review.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`

### pipeline-review
Analyze pipeline health — prioritize deals, flag risks, get a weekly action plan. Use when running a weekly pipeline review, deciding which deals to focus on this week, spotting stale or stuck opportunities, auditing for hygiene issues like bad close dates, or identifying single-threaded deals.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/sales/skills/pipeline-review/SKILL.md`

### risk-assessment
Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user is evaluating risks associated with a project, vendor, process, or decision.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/operations/skills/risk-assessment/SKILL.md`

### scientific-problem-selection
This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`

### status-report
Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/operations/skills/status-report/SKILL.md`
