# Tag: queries

Skills with tag `queries`:

## code-review

Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/code-review/SKILL.md`
- **Tags**: `cases`, `change`, `changes`, `checking`, `code`, `code-review`, `correctness`, `diff`, `edge`, `engineering`, `error`, `gaps`, `handling`, `injection`, `merge`, `missing`, `performance`, `queries`, `review`, `risks`, `safe`, `security`, `trigger`, `url`

## search-strategy

Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-specific syntax, ranks results by relevance, and handles ambiguity and fallback strategies.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy`
- **Skill file**: `external/anthropic-knowledge-work-plugins/enterprise-search/skills/search-strategy/SKILL.md`
- **Tags**: `ambiguity`, `breaks`, `decomposition`, `enterprise`, `enterprise-search`, `fallback`, `handles`, `language`, `multi`, `natural`, `orchestration`, `per`, `queries`, `query`, `questions`, `ranks`, `relevance`, `search`, `search-strategy`, `searches`, `strategies`, `strategy`, `syntax`, `targeted`, `translates`

## sentry

Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform read-only queries using the `sentry` command.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/sentry`
- **Skill file**: `external/openai-skills/skills/.curated/sentry/SKILL.md`
- **Tags**: `asks`, `basic`, `cli`, `command`, `curated`, `data`, `errors`, `events`, `health`, `inspect`, `issues`, `perform`, `production`, `pull`, `queries`, `recent`, `sentry`, `summarize`

## sql-queries

Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries`
- **Skill file**: `external/anthropic-knowledge-work-plugins/data/skills/sql-queries/SKILL.md`
- **Tags**: `aggregations`, `analytical`, `between`, `bigquery`, `building`, `complex`, `correct`, `ctes`, `data`, `databricks`, `dialects`, `etc`, `functions`, `major`, `optimizing`, `performant`, `postgresql`, `queries`, `slow`, `snowflake`, `sql`, `sql-queries`, `translating`, `warehouse`, `window`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## variant-analysis

Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `audits`, `bug`, `bugs`, `building`, `code`, `codebases`, `codeql`, `find`, `finding`, `hunting`, `initial`, `issue`, `performing`, `queries`, `security`, `semgrep`, `similar`, `systematic`, `variant`, `variant-analysis`, `variants`, `vulnerabilities`
