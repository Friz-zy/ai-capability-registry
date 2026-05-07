# screen

## Skills
Load skill file when task matches.

### accessibility-review
Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

File: `../external/anthropic-knowledge-work-plugins/design/skills/accessibility-review/SKILL.md`

### design-critique
Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this screen?", or when sharing a Figma link or screenshot for feedback at any stage from exploration to final polish.

File: `../external/anthropic-knowledge-work-plugins/design/skills/design-critique/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### openai-screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific

File: `../external/trailofbits-skills-curated/plugins/openai-screenshot/skills/openai-screenshot/SKILL.md`

### screenshot
Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed.

File: `../external/openai-skills/skills/.curated/screenshot/SKILL.md`

### video-sdk/web
Zoom Video SDK for Web - JavaScript/TypeScript integration for browser-based video sessions, real-time communication, screen sharing, recording, and live transcription

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/web/SKILL.md`

### video-sdk/windows
Zoom Video SDK for Windows - C++ integration for video sessions, raw audio/video capture, screen sharing, recording, and real-time communication

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/windows/SKILL.md`

### zoom-rtms
Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or contact-center voice streams.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/rtms/SKILL.md`
