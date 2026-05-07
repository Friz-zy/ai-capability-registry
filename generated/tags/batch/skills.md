# Tag: batch

Skills with tag `batch`:

## claude-api

Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements). TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project. SKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.

- **Source**: `anthropic-skills` (trusted)
- **Path**: `external/anthropic-skills/skills/claude-api`
- **Skill file**: `external/anthropic-skills/skills/claude-api/SKILL.md`
- **Tags**: `adds`, `api`, `apps`, `asks`, `batch`, `between`, `build`, `cache`, `caching`, `citations`, `code`, `compaction`, `debug`, `existing`, `feature`, `filename`, `general`, `generic`, `haiku`, `handles`, `hit`, `imports`, `include`, `like`, `managed`, `memory`, `migrating`, `model`, `modifies`, `neutral`, `optimize`, `opus`, `other`, `other-provider`, `programming`, `project`, `prompt`, `provider`, `provider-neutral`, `questions`, `rate`, `replacements`, `retired`, `retired-model`, `sdk`, `skip`, `sonnet`, `thinking`, `trigger`, `tunes`, `versions`

## scribe

Reference skill for Zoom AI Services Scribe. Use after routing to a transcription workflow when handling uploaded or stored media, Build-platform JWT auth, fast mode transcription, batch jobs, or transcript pipeline design.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/scribe`
- **Skill file**: `external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/scribe/SKILL.md`
- **Tags**: `auth`, `batch`, `build`, `build-platform`, `design`, `fast`, `handling`, `jobs`, `jwt`, `media`, `mode`, `partner`, `pipeline`, `platform`, `routing`, `scribe`, `services`, `stored`, `transcript`, `transcription`, `uploaded`, `zoom`

## scvi-tools

Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (2) ATAC-seq analysis with PeakVI, (3) CITE-seq multi-modal analysis with totalVI, (4) multiome RNA+ATAC analysis with MultiVI, (5) spatial transcriptomics deconvolution with DestVI, (6) label transfer and reference mapping with scANVI/scArches, (7) RNA velocity with veloVI, or (8) any deep learning-based single-cell method. Triggers include mentions of scVI, scANVI, totalVI, PeakVI, MultiVI, DestVI, veloVI, sysVI, scArches, variational autoencoder, VAE, batch correction, data integration, multi-modal, CITE-seq, multiome, reference mapping, latent space.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools`
- **Skill file**: `external/anthropic-knowledge-work-plugins/bio-research/skills/scvi-tools/SKILL.md`
- **Tags**: `analysis`, `atac`, `atac-seq`, `autoencoder`, `batch`, `bio`, `bio-research`, `cell`, `cite`, `cite-seq`, `correction`, `data`, `deconvolution`, `deep`, `destvi`, `include`, `integration`, `label`, `latent`, `learning`, `mapping`, `mentions`, `method`, `modal`, `multi`, `multi-modal`, `multiome`, `multivi`, `peakvi`, `research`, `rna`, `scanvi`, `scarches`, `scvi`, `seq`, `single`, `single-cell`, `space`, `spatial`, `sysvi`, `totalvi`, `transcriptomics`, `transfer`, `triggers`, `used`, `vae`, `variational`, `velocity`, `velovi`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`
