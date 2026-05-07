# Tag: triggers

Skills with tag `triggers`:

## account-research

Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on with [company]', or any account-level question.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/account-research/SKILL.md`
- **Tags**: `account`, `account-level`, `account-research`, `company`, `data`, `domain`, `going`, `level`, `partner`, `pull`, `question`, `research`, `room`, `signals`, `tell`, `triggers`

## call-prep

Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with [company]', 'what should I know before talking to [company]', or any call preparation request.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/call-prep/SKILL.md`
- **Tags**: `call`, `call-prep`, `company`, `customer`, `know`, `meeting`, `partner`, `prep`, `preparation`, `prepare`, `prospect`, `request`, `room`, `signals`, `talking`, `triggers`

## compose-outreach

Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for [contact]', or any outreach drafting request.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/compose-outreach/SKILL.md`
- **Tags**: `compose`, `compose-outreach`, `contact`, `draft`, `drafting`, `email`, `message`, `messages`, `outreach`, `partner`, `person`, `personalized`, `request`, `room`, `signals`, `triggers`

## contact-research

Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contact-level question.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/contact-research/SKILL.md`
- **Tags**: `contact`, `contact-level`, `contact-research`, `data`, `email`, `lead`, `level`, `look`, `partner`, `person`, `question`, `research`, `room`, `triggers`, `warm`, `who`

## deploy-checklist

Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/deploy-checklist/SKILL.md`
- **Tags**: `ahead`, `approvals`, `change`, `checklist`, `database`, `deploy`, `deploy-checklist`, `deploying`, `deployment`, `documenting`, `engineering`, `feature`, `flags`, `going`, `migrations`, `pre`, `pre-deployment`, `production`, `release`, `rollback`, `ship`, `status`, `time`, `triggers`, `verification`, `verifying`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## dwarf-expert

Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding DWARF information, interacting with DWARF files, answering DWARF-related questions, or working with code that parses DWARF data.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert`
- **Skill file**: `external/trailofbits-skills/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md`
- **Tags**: `analyzing`, `answering`, `code`, `data`, `debug`, `dwarf`, `dwarf-expert`, `expert`, `expertise`, `format`, `information`, `interacting`, `parses`, `provides`, `questions`, `standard`, `triggers`, `understanding`, `v3-v5`, `working`

## figma-generate-design

Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/figma-generate-design`
- **Skill file**: `external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`
- **Tags**: `alongside`, `app`, `application`, `assembles`, `build`, `code`, `components`, `create`, `curated`, `description`, `design`, `discovers`, `figma`, `figma-design`, `full`, `hardcoded`, `imports`, `incrementally`, `instead`, `involves`, `landing`, `layout`, `match`, `multi`, `multi-section`, `page`, `preferred`, `push`, `screen`, `screens`, `search`, `search-design`, `section`, `section-by-section`, `styles`, `take`, `them`, `tokens`, `translating`, `triggers`, `values`, `variables`, `view`, `whenever`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

## nextflow-development

Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or public datasets from GEO/SRA. Triggers on nf-core, Nextflow, FASTQ analysis, variant calling, gene expression, differential expression, GEO reanalysis, GSE/GSM/SRR accessions, or samplesheet creation.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md`
- **Tags**: `accessions`, `analysis`, `analyzing`, `atac`, `atac-seq`, `atacseq`, `bio`, `bio-research`, `bioinformatics`, `calling`, `core`, `creation`, `data`, `datasets`, `development`, `differential`, `either`, `expression`, `fastq`, `fastqs`, `gene`, `geo`, `gse`, `gsm`, `local`, `nextflow`, `nextflow-development`, `nf-core`, `pipelines`, `public`, `reanalysis`, `research`, `rna`, `rna-seq`, `rnaseq`, `samplesheet`, `sarek`, `seq`, `sequencing`, `sra`, `srr`, `triggers`, `variant`, `wes`, `wgs`

## prospect

Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect list', 'find contacts at [type of company]', 'show me companies hiring [role]', or any list-building request.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/prospect/SKILL.md`
- **Tags**: `account`, `build`, `building`, `companies`, `company`, `contact`, `contacts`, `criteria`, `find`, `hiring`, `lists`, `match`, `partner`, `prospect`, `prospector`, `request`, `role`, `room`, `show`, `targeted`, `triggers`

## scvi-tools

Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`
- **Tags**: `analysis`, `atac`, `atac-seq`, `autoencoder`, `batch`, `bio`, `bio-research`, `cell`, `cite`, `cite-seq`, `correction`, `data`, `deconvolution`, `deep`, `destvi`, `include`, `integration`, `label`, `latent`, `learning`, `mapping`, `mentions`, `method`, `modal`, `multi`, `multi-modal`, `multiome`, `multivi`, `peakvi`, `research`, `rna`, `scanvi`, `scarches`, `scvi`, `seq`, `single`, `single-cell`, `space`, `spatial`, `sysvi`, `totalvi`, `transcriptomics`, `transfer`, `triggers`, `used`, `vae`, `variational`, `velocity`, `velovi`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

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

## weekly-prep-brief

Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep', or any weekly planning request.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief/SKILL.md`
- **Tags**: `brief`, `briefing`, `calls`, `comprehensive`, `days`, `have`, `monday`, `next`, `partner`, `planning`, `prep`, `prepare`, `request`, `room`, `triggers`, `week`, `weekly`, `weekly-prep-brief`
