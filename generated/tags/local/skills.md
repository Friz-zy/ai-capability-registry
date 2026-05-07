# Tag: local

Skills with tag `local`:

## build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`
- **Tags**: `api`, `app`, `asks`, `build`, `build-mcp-server`, `building`, `case`, `context`, `create`, `deployment`, `design`, `determines`, `dev`, `development`, `discusses`, `entry`, `expose`, `hands`, `http`, `integration`, `interrogates`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `model`, `off`, `picks`, `point`, `protocol`, `remote`, `right`, `server`, `something`, `specialized`, `stdio`, `their`, `used`, `wrap`

## build-mcpb

This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`
- **Tags**: `apps`, `build`, `build-mcpb`, `bundle`, `bundling`, `desktop`, `dev`, `discusses`, `distribute`, `filesystem`, `having`, `installable`, `interacts`, `local`, `make`, `mcp`, `mcp-server-dev`, `mcpb`, `mentions`, `must`, `needs`, `node`, `package`, `python`, `runtime`, `server`, `set`, `ship`, `their`, `used`, `without`

## cli-creator

Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/cli-creator`
- **Skill file**: `external/openai-skills/skills/.curated/cli-creator/SKILL.md`
- **Tags**: `admin`, `api`, `app`, `auth`, `build`, `can`, `cli`, `cli-creator`, `codex`, `command`, `command-line`, `commands`, `companion`, `composable`, `create`, `creator`, `curated`, `curl`, `docs`, `existing`, `expose`, `line`, `local`, `manage`, `openapi`, `pair`, `repo`, `return`, `script`, `sdk`, `spec`, `stable`, `web`

## git-cleanup

Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup`
- **Skill file**: `external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup/SKILL.md`
- **Tags**: `active`, `analyzes`, `branches`, `categorizing`, `cleans`, `cleanup`, `git`, `git-cleanup`, `local`, `merged`, `safely`, `squash`, `squash-merged`, `superseded`, `them`, `worktrees`

## nextflow-development

Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`
- **Tags**: `accessions`, `analysis`, `analyzing`, `atac`, `atac-seq`, `atacseq`, `bio`, `bio-research`, `bioinformatics`, `calling`, `core`, `creation`, `data`, `datasets`, `development`, `differential`, `either`, `expression`, `fastq`, `fastqs`, `gene`, `geo`, `gse`, `gsm`, `local`, `nextflow`, `nextflow-development`, `nf-core`, `pipelines`, `public`, `reanalysis`, `research`, `rna`, `rna-seq`, `rnaseq`, `samplesheet`, `sarek`, `seq`, `sequencing`, `sra`, `srr`, `triggers`, `variant`, `wes`, `wgs`

## plugin-creator

Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can edit before publishing or testing. Use when Codex needs to create a new local plugin, add optional plugin structure, or generate or update repo-root `.agents/plugins/marketplace.json` entries for plugin ordering and availability metadata.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.system/plugin-creator`
- **Skill file**: `external/openai-skills/skills/.system/plugin-creator/SKILL.md`
- **Tags**: `availability`, `baseline`, `can`, `codex`, `create`, `creator`, `directories`, `edit`, `entries`, `folders`, `local`, `marketplace`, `metadata`, `needs`, `optional`, `ordering`, `placeholders`, `publishing`, `repo`, `repo-root`, `root`, `scaffold`, `structure`, `testing`

## plugin-settings

This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/plugin-settings/SKILL.md`
- **Tags**: `asks`, `behavior`, `configurable`, `configuration`, `content`, `dev`, `documents`, `frontmatter`, `local`, `make`, `markdown`, `per`, `per-project`, `project`, `settings`, `state`, `store`, `storing`, `used`, `yaml`

## webapp-testing

Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/webapp-testing`
- **Skill file**: `external/anthropic-skills/skills/webapp-testing/SKILL.md`
- **Tags**: `applications`, `behavior`, `browser`, `capturing`, `debugging`, `frontend`, `functionality`, `interacting`, `local`, `logs`, `playwright`, `screenshots`, `supports`, `testing`, `toolkit`, `verifying`, `viewing`, `web`, `webapp`, `webapp-testing`
