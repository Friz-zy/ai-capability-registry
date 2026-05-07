# triggers

## Navigation
Read skill files below to understand capabilities.
Load skill file when task matches.

## Skills

### account-research
Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md`

### call-prep
Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md`

### compose-outreach
Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]', or any outreach drafting request.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md`

### contact-research
Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contact-level question.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md`

### deploy-checklist
Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`

### docx
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-skills/skills/docx/SKILL.md`

### dwarf-expert
Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### instrument-data-to-allotrope
Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`

### nextflow-development
Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`

### prospect
Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`

### scvi-tools
Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`

### sharp-edges
Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`

### skill-improver
Iteratively reviews and fixes Claude Code skill quality issues until they meet standards. Runs automated fix-review cycles using the skill-reviewer agent. Use to fix skill quality issues, improve skill descriptions, run automated skill review loops, or iteratively refine a skill. Triggers on 'fix my skill', 'improve skill quality', 'skill improvement loop'. NOT for one-time reviews—use /skill-reviewer directly.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/skill-improver/skills/skill-improver/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`

### weekly-prep-brief
Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep', or any weekly planning request.

File: `/vscode/workspace/GITHUB/ai-capability-registry/external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief/SKILL.md`
