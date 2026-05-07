# scope

## Skills
Load skill file when task matches.

### gh-fix-ci
Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL.

File: `../external/openai-skills/skills/.curated/gh-fix-ci/SKILL.md`

### speech
Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

File: `../external/openai-skills/skills/.curated/speech/SKILL.md`

### sprint-planning
Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounting for PTO and meetings), deciding what's P0 vs. stretch, or handling carryover from the last sprint.

File: `../external/anthropic-knowledge-work-plugins/product-management/skills/sprint-planning/SKILL.md`
