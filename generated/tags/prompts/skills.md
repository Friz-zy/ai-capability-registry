# Tag: prompts

Skills with tag `prompts`:

## agent-development

This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/plugin-dev/skills/agent-development/SKILL.md`
- **Tags**: `asks`, `autonomous`, `code`, `colors`, `conditions`, `create`, `description`, `dev`, `development`, `frontmatter`, `guidance`, `needs`, `practices`, `prompts`, `structure`, `subagent`, `triggering`, `used`

## hatch-pet

Create, repair, validate, preview, and package Codex-compatible animated pets and pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user wants to hatch a Codex pet, create a custom animated pet, or build a built-in pet asset with an 8x9 atlas, transparent unused cells, row-by-row animation prompts, QA contact sheets, preview videos, and pet.json packaging. This skill composes the installed $imagegen system skill for visual generation and uses bundled scripts for deterministic spritesheet assembly.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/hatch-pet`
- **Skill file**: `external/openai-skills/skills/.curated/hatch-pet/SKILL.md`
- **Tags**: `8x9`, `animated`, `animation`, `art`, `assembly`, `asset`, `atlas`, `build`, `bundled`, `cells`, `character`, `codex`, `codex-compatible`, `compatible`, `composes`, `contact`, `create`, `curated`, `custom`, `deterministic`, `generation`, `hatch`, `hatch-pet`, `imagegen`, `images`, `installed`, `package`, `packaging`, `pet`, `pets`, `preview`, `prompts`, `repair`, `row`, `row-by-row`, `screenshots`, `sheets`, `spritesheet`, `spritesheets`, `transparent`, `unused`, `validate`, `videos`, `visual`

## let-fate-decide

Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide`
- **Skill file**: `external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`
- **Tags**: `ambiguous`, `approaches`, `arbitrarily`, `ask`, `ask-questions-if-underspecified`, `between`, `cards`, `casual`, `casually`, `decide`, `delegated`, `draws`, `entropy`, `fate`, `idk`, `inject`, `interprets`, `let`, `let-fate-decide`, `makes`, `multiple`, `next`, `nonchalant`, `other`, `over`, `phrases`, `pick`, `planning`, `playful`, `precision`, `precision-seeking`, `prefer`, `prompts`, `questions`, `rather`, `reasonable`, `says`, `seeking`, `spread`, `tarot`, `than`, `tone`, `underspecified`, `vague`, `whatever`, `yolo`, `yu-gi-oh`

## session-report

Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

- **Source**: `anthropic-claude-plugins-official` (trusted)
- **Path**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report`
- **Skill file**: `external/anthropic-claude-plugins-official/plugins/session-report/skills/session-report/SKILL.md`
- **Tags**: `cache`, `code`, `expensive`, `explorable`, `html`, `projects`, `prompts`, `report`, `session`, `session-report`, `subagents`, `tokens`, `transcripts`

## speech

Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

- **Source**: `openai-skills` (trusted)
- **Path**: `external/openai-skills/skills/.curated/speech`
- **Skill file**: `external/openai-skills/skills/.curated/speech/SKILL.md`
- **Tags**: `accessibility`, `api`, `api-key`, `asks`, `audio`, `batch`, `bundled`, `calls`, `cli`, `creation`, `curated`, `custom`, `generation`, `key`, `live`, `narration`, `out`, `prompts`, `reads`, `require`, `scope`, `speech`, `text`, `text-to-speech`, `voice`, `voiceover`, `voices`
