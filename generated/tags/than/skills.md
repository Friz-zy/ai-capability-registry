# than

## Skills
Load skill and **use it** when task matches.

### algorithmic-art
Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

File: `../external/anthropic-skills/skills/algorithmic-art/SKILL.md`

### build-zoom-video-sdk-app
Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an actual Zoom meeting.

File: `../external/anthropic-knowledge-work-plugins/partner-built/zoom-plugin/skills/video-sdk/SKILL.md`

### imagegen
Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-background cutouts. Use when Codex should create a brand-new image, transform an existing image, or derive visual variants from references, and the output should be a bitmap asset rather than repo-native code or vector. Do not use when the task is better handled by editing existing SVG/vector/code-native assets, extending an established icon or logo system, or building the visual directly in HTML/CSS/canvas.

File: `../external/openai-skills/skills/.system/imagegen/SKILL.md`

### let-fate-decide
Draws 4 Tarot cards to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over ask-questions-if-underspecified when the user's tone is casual or playful rather than precision-seeking.

File: `../external/trailofbits-skills/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md`

### property-based-testing
Provides guidance for property-based testing across multiple languages and smart contracts. Use when writing tests, reviewing code with serialization/validation/parsing patterns, designing features, or when property-based testing would provide stronger coverage than example-based tests.

File: `../external/trailofbits-skills/plugins/property-based-testing/skills/property-based-testing/SKILL.md`
