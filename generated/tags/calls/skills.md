# calls

## Skills
Load skill file when task matches.

### content-creation
Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use when writing any marketing content, when you need channel-specific formatting, SEO-optimized copy, headline options, or calls to action.

File: `external/anthropic-knowledge-work-plugins/marketing/skills/content-creation/SKILL.md`

### speech
Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

File: `external/openai-skills/skills/.curated/speech/SKILL.md`

### weekly-prep-brief
Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have this week', 'Monday prep', or any weekly planning request.

File: `external/anthropic-knowledge-work-plugins/partner-built/common-room/skills/weekly-prep-brief/SKILL.md`
