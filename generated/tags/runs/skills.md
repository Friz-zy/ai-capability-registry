# Tag: runs

Skills with tag `runs`:

## audit-prep-assistant

Prepares codebases for security review using Trail of Bits' checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments).

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`
- **Tags**: `accessibility`, `analysis`, `audit`, `audit-prep`, `building`, `building-secure-contracts`, `checklist`, `code`, `codebases`, `comments`, `contracts`, `coverage`, `dead`, `documentation`, `ensures`, `flowcharts`, `generates`, `goals`, `helps`, `increases`, `inline`, `prep`, `prepares`, `removes`, `review`, `runs`, `secure`, `security`, `set`, `static`, `stories`, `test`

## genotoxic

Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`
- **Tags**: `analyzing`, `cairo`, `cairo-mutants`, `call`, `circomvent`, `codebases`, `coverage`, `data`, `false`, `finding`, `frameworks`, `fuzzing`, `gaps`, `genotoxic`, `graph`, `graph-informed`, `identify`, `identifying`, `including`, `informed`, `missing`, `mutants`, `mutation`, `necessist`, `parses`, `positives`, `running`, `runs`, `statements`, `survived`, `targets`, `test`, `testing`, `tests`, `then`, `trailmark`, `triage`, `triaging`, `unnecessary`, `weak`

## mutation-testing

Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing`
- **Skill file**: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`
- **Tags**: `campaign`, `campaigns`, `configure`, `configures`, `long`, `long-running`, `mentions`, `mewt`, `mutation`, `mutation-testing`, `muton`, `optimize`, `optimizes`, `running`, `runs`, `scopes`, `targets`, `testing`, `timeouts`, `tunes`

## second-opinion

Runs external LLM code reviews (OpenAI Codex or Google Gemini CLI) on uncommitted changes, branch diffs, or specific commits. Use when the user asks for a second opinion, external review, codex review, gemini review, or mentions /second-opinion.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion`
- **Skill file**: `external/trailofbits-skills/plugins/second-opinion/skills/second-opinion/SKILL.md`
- **Tags**: `asks`, `branch`, `changes`, `cli`, `code`, `codex`, `commits`, `diffs`, `gemini`, `google`, `llm`, `mentions`, `opinion`, `review`, `reviews`, `runs`, `second`, `second-opinion`, `uncommitted`

## secure-workflow-guide

Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide`
- **Skill file**: `external/trailofbits-skills/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`
- **Tags**: `areas`, `building`, `building-secure-contracts`, `checks`, `conformance`, `contracts`, `development`, `diagrams`, `document`, `erc`, `features`, `fuzzing`, `generates`, `guides`, `helps`, `integration`, `manual`, `properties`, `reviews`, `runs`, `scans`, `secure`, `security`, `slither`, `special`, `token`, `upgradeability`, `verification`, `visual`

## skill-improver

Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver`
- **Skill file**: `external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`
- **Tags**: `automated`, `code`, `cycles`, `descriptions`, `directly`, `fix`, `fix-review`, `fixes`, `improve`, `improvement`, `improver`, `issues`, `iteratively`, `loop`, `loops`, `meet`, `one`, `one-time`, `quality`, `refine`, `review`, `reviewer`, `reviews`, `runs`, `standards`, `they`, `time`, `triggers`, `until`

## trailmark-structural

Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`
- **Tags**: `analysis`, `attack`, `blast`, `boundaries`, `building`, `complexity`, `data`, `detailed`, `full`, `graph`, `hotspots`, `needs`, `preanalysis`, `privilege`, `radius`, `reporting`, `running`, `runs`, `structural`, `surface`, `taint`, `target`, `trailmark`, `trailmark-structural`, `triggers`, `vivisect`

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
