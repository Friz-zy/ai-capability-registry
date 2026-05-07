# them

## Skills
Load skill file when task matches.

### entry-point-analyzer
Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

File: `../external/trailofbits-skills/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

### figma-generate-design
Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma', 'create in Figma from code', 'push page to Figma', 'take this app/page and build it in Figma', 'create a screen', 'build a landing page in Figma', 'update the Figma screen to match code'. This is the preferred workflow skill whenever the user wants to build or update a full page, screen, or view in Figma from code or a description. Discovers design system components, variables, and styles via search_design_system, imports them, and assembles screens incrementally section-by-section using design system tokens instead of hardcoded values.

File: `../external/openai-skills/skills/.curated/figma-generate-design/SKILL.md`

### git-cleanup
Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

File: `../external/trailofbits-skills/plugins/git-cleanup/skills/git-cleanup/SKILL.md`

### notion-spec-to-implementation
Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

File: `../external/openai-skills/skills/.curated/notion-spec-to-implementation/SKILL.md`

### pdf
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

File: `../external/anthropic-skills/skills/pdf/SKILL.md`

### sequence-load
Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.

File: `../external/anthropic-knowledge-work-plugins/partner-built/apollo/skills/sequence-load/SKILL.md`
