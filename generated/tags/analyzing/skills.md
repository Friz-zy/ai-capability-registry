# analyzing

## Skills
Load skill and **use it** when task matches.

### burpsuite-project-parser
Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

File: `../external/trailofbits-skills/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

### dwarf-expert
Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

File: `../external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`

### firebase-apk-scanner
Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

File: `../external/trailofbits-skills/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `../external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### insecure-defaults
Detects fail-open insecure defaults (hardcoded secrets, weak auth, permissive security) that allow apps to run insecurely in production. Use when auditing security, reviewing config management, or analyzing environment variable handling.

File: `../external/trailofbits-skills/plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`

### nextflow-development
Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

File: `../external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`

### openai-spreadsheet
Use when tasks involve creating, editing, analyzing, or formatting spreadsheets (`.xlsx`,

File: `../external/trailofbits-skills-curated/plugins/openai-spreadsheet/skills/openai-spreadsheet/SKILL.md`

### people-report
Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by team, preparing diversity representation metrics, or assessing span of control and flight risk across the org.

File: `../external/anthropic-knowledge-work-plugins/human-resources/skills/people-report/SKILL.md`

### render-deploy
Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform.

File: `../external/openai-skills/skills/.curated/render-deploy/SKILL.md`

### statistical-analysis
Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for significance, detecting anomalies, computing correlations, or interpreting statistical results.

File: `../external/anthropic-knowledge-work-plugins/data/skills/statistical-analysis/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### variance-analysis
Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes, revenue or expense variances, or preparing variance commentary for leadership.

File: `../external/anthropic-knowledge-work-plugins/finance/skills/variance-analysis/SKILL.md`

### variant-analysis
Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.

File: `../external/trailofbits-skills/plugins/variant-analysis/skills/variant-analysis/SKILL.md`
