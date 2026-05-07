# Tag: include

Skills with tag `include`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## docx

Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/docx`
- **Skill file**: `external/anthropic-skills/skills/docx/SKILL.md`
- **Tags**: `asks`, `changes`, `coding`, `comments`, `content`, `converting`, `create`, `deliverable`, `doc`, `docs`, `document`, `documents`, `docx`, `edit`, `extracting`, `find`, `find-replace`, `formatting`, `general`, `generation`, `google`, `headings`, `images`, `include`, `inserting`, `letter`, `letterheads`, `like`, `manipulate`, `memo`, `mention`, `numbers`, `page`, `pdfs`, `performing`, `polished`, `produce`, `professional`, `reorganizing`, `replace`, `replacing`, `report`, `requests`, `similar`, `spreadsheets`, `tables`, `tracked`, `triggers`, `unrelated`, `whenever`, `word`, `working`

## frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/frontend-design`
- **Skill file**: `external/anthropic-skills/skills/frontend-design/SKILL.md`
- **Tags**: `aesthetics`, `applications`, `artifacts`, `asks`, `avoids`, `beautifying`, `build`, `code`, `components`, `create`, `creative`, `css`, `dashboards`, `design`, `distinctive`, `frontend`, `frontend-design`, `generates`, `generic`, `grade`, `high`, `html`, `include`, `interfaces`, `landing`, `layouts`, `pages`, `polished`, `posters`, `production`, `production-grade`, `quality`, `react`, `styling`, `web`, `websites`

## instrument-data-to-allotrope

Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md`
- **Tags**: `allotrope`, `analysis`, `asm`, `auto`, `auto-detection`, `bio`, `bio-research`, `code`, `convert`, `converting`, `csv`, `data`, `detection`, `downstream`, `easy`, `eln`, `engineers`, `excel`, `exportable`, `flattened`, `format`, `full`, `generating`, `import`, `include`, `instrument`, `instrument-data-to-allotrope`, `lab`, `laboratory`, `lakes`, `lims`, `model`, `outputs`, `parser`, `pdf`, `pipelines`, `preparing`, `production`, `python`, `research`, `scientists`, `simple`, `standardize`, `standardizing`, `supports`, `systems`, `triggers`, `txt`, `types`, `upload`

## scientific-problem-selection

This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scientific-problem-selection/SKILL.md`
- **Tags**: `advice`, `ask`, `bio`, `bio-research`, `choosing`, `decision`, `decisions`, `evaluate`, `have`, `idea`, `ideation`, `include`, `navigate`, `pitch`, `plan`, `problem`, `project`, `projects`, `requests`, `research`, `risks`, `scientific`, `scientific-problem-selection`, `scientists`, `selection`, `strategic`, `strategy`, `stuck`, `trees`, `troubleshooting`, `typical`, `used`

## scvi-tools

Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`
- **Tags**: `analysis`, `atac`, `atac-seq`, `autoencoder`, `batch`, `bio`, `bio-research`, `cell`, `cite`, `cite-seq`, `correction`, `data`, `deconvolution`, `deep`, `destvi`, `include`, `integration`, `label`, `latent`, `learning`, `mapping`, `mentions`, `method`, `modal`, `multi`, `multi-modal`, `multiome`, `multivi`, `peakvi`, `research`, `rna`, `scanvi`, `scarches`, `scvi`, `seq`, `single`, `single-cell`, `space`, `spatial`, `sysvi`, `totalvi`, `transcriptomics`, `transfer`, `triggers`, `used`, `vae`, `variational`, `velocity`, `velovi`
