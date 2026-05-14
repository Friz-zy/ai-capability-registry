# Development Workflow

Use this workflow for software-development work: planning, implementation, refactoring, debugging, testing, validation, review, deployment, frontend, backend, mobile, desktop, blockchain, hardware/IoT, cloud infrastructure, DevOps, SRE, QA, security engineering, data engineering, and agent automation.

This workflow adapts the Superpowers development methodology to this registry. Do not load `external/superpowers-skills/skills/using-superpowers/SKILL.md` as a normal skill; its bootstrap behavior is represented here and in `skills/skills.md`.

## Subagent Scope

If you were dispatched as a subagent to execute a specific task, do not restart top-level workflow resolution. Follow the parent task instructions and any workflow or skill choices already provided.

Resolve additional development workflows or skills only when they are directly needed for the assigned subtask.

## Selection Rule

Before acting, decide whether a process skill applies. Do this before code edits, broad file exploration, implementation planning, debugging, verification claims, or clarifying questions when a process skill could shape the question.

If a trusted or reviewed process skill plausibly matches the task after routing, use it before comparable implementation or domain skills. Do not skip it because the task looks simple, because you want to inspect files first, or because the workflow feels like overhead.

If the loaded skill does not actually match the task, stop using it and continue with the next best match.

Use only trusted or reviewed skills. Load only the skills needed for the task.

## Process Before Implementation

Prefer workflow and process skills before implementation and domain skills:

- For "build", "add", "design", "plan", or ambiguous feature requests, consider brainstorming and planning before implementation.
- For implementation from an existing plan, consider executing-plans before technology-specific skills.
- For testable behavior changes, consider test-driven-development or testing-strategy before implementation.
- For bugs, errors, failing tests, regressions, or incidents, consider systematic-debugging before domain-specific implementation.
- For larger work that can be parallelized, consider subagent-driven-development or dispatching-parallel-agents before starting execution.
- For review requests, consider requesting-code-review or receiving-code-review depending on whether the user wants a review or is responding to review feedback.
- Before claiming completion, consider verification-before-completion.
- Before finishing or preparing a development branch, consider finishing-a-development-branch.
- For feature work that needs isolation from the current workspace, consider using-git-worktrees.

## Relevant Superpowers Skills

Use agent-native skills when the current runtime exposes the same trusted skill. Otherwise resolve the skill through this registry's catalogs or direct path.

- `brainstorming`: `external/superpowers-skills/skills/brainstorming/SKILL.md`
- `writing-plans`: `external/superpowers-skills/skills/writing-plans/SKILL.md`
- `executing-plans`: `external/superpowers-skills/skills/executing-plans/SKILL.md`
- `test-driven-development`: `external/superpowers-skills/skills/test-driven-development/SKILL.md`
- `systematic-debugging`: `external/superpowers-skills/skills/systematic-debugging/SKILL.md`
- `dispatching-parallel-agents`: `external/superpowers-skills/skills/dispatching-parallel-agents/SKILL.md`
- `subagent-driven-development`: `external/superpowers-skills/skills/subagent-driven-development/SKILL.md`
- `requesting-code-review`: `external/superpowers-skills/skills/requesting-code-review/SKILL.md`
- `receiving-code-review`: `external/superpowers-skills/skills/receiving-code-review/SKILL.md`
- `verification-before-completion`: `external/superpowers-skills/skills/verification-before-completion/SKILL.md`
- `finishing-a-development-branch`: `external/superpowers-skills/skills/finishing-a-development-branch/SKILL.md`
- `using-git-worktrees`: `external/superpowers-skills/skills/using-git-worktrees/SKILL.md`

## Discipline

Treat these workflows as rigid unless user or project instructions say otherwise:

- systematic debugging
- test-driven development
- verification before completion
- code review workflows
- finishing development branches

Treat design patterns, implementation patterns, tool-specific guidance, and architecture advice as flexible. Adapt them to project conventions and the user's explicit constraints.

## Priority

When workflow guidance conflicts with other instructions, follow the priority order in `skills/skills.md`:

1. User and project instructions.
2. Selected workflow and process skills.
3. Selected implementation and domain skills.
4. Generic agent behavior.

## Anti-Rationalization Checks

Do not skip process skill selection because the task looks simple, because you want to inspect files first, because you need to ask a clarifying question, or because the workflow feels like overhead. If a process skill could change how the work should be approached, check it first.

Do not load every possible workflow and skill. Choose the smallest set of relevant process skills, then continue with ordinary task, role, and keyword routing.
