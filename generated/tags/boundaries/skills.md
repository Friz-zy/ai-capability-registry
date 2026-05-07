# Tag: boundaries

Skills with tag `boundaries`:

## openai-security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities,

- **Source**: `trailofbits-skills-curated` (trusted)
- **Path**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model`
- **Skill file**: `external/trailofbits-skills-curated/plugins/openai-security-threat-model/skills/openai-security-threat-model/SKILL.md`
- **Tags**: `assets`, `attacker`, `boundaries`, `capabilities`, `enumerates`, `grounded`, `model`, `modeling`, `repository`, `repository-grounded`, `security`, `security-threat-model`, `threat`, `trust`

## security-threat-model

Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/security-threat-model`
- **Skill file**: `external/openai-skills/skills/.curated/security-threat-model/SKILL.md`
- **Tags**: `abuse`, `appsec`, `architecture`, `asks`, `assets`, `attacker`, `boundaries`, `capabilities`, `code`, `codebase`, `concise`, `curated`, `design`, `enumerate`, `enumerates`, `explicitly`, `general`, `grounded`, `markdown`, `mitigations`, `model`, `modeling`, `non`, `non-security`, `path`, `paths`, `perform`, `repository`, `repository-grounded`, `review`, `security`, `security-threat-model`, `summaries`, `threat`, `threats`, `trigger`, `trust`, `writes`

## system-design

Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.

- **Source**: `anthropic-knowledge-work-plugins` (trusted)
- **Path**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design`
- **Skill file**: `external/anthropic-knowledge-work-plugins/engineering/skills/system-design/SKILL.md`
- **Tags**: `api`, `architect`, `architecture`, `architectures`, `boundaries`, `data`, `design`, `engineering`, `modeling`, `needs`, `right`, `service`, `services`, `systems`, `trigger`

## trailmark

Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`
- **Tags**: `analysis`, `analyzing`, `attack`, `audit`, `auto`, `blast`, `boundaries`, `building`, `builds`, `call`, `code`, `complexity`, `detect`, `detect-languages`, `entry`, `enumerating`, `enumeration`, `finding`, `graph`, `graphs`, `hotspots`, `includes`, `language`, `languages`, `mapping`, `measuring`, `multi`, `multi-language`, `parse`, `passes`, `paths`, `point`, `points`, `polyglot`, `pre`, `pre-analysis`, `prefer`, `prioritization`, `privilege`, `propagation`, `queries`, `radius`, `security`, `surface`, `taint`, `target`, `tracing`, `trailmark`, `unknown`

## trailmark-structural

Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`
- **Tags**: `analysis`, `attack`, `blast`, `boundaries`, `building`, `complexity`, `data`, `detailed`, `full`, `graph`, `hotspots`, `needs`, `preanalysis`, `privilege`, `radius`, `reporting`, `running`, `runs`, `structural`, `surface`, `taint`, `target`, `trailmark`, `trailmark-structural`, `triggers`, `vivisect`
