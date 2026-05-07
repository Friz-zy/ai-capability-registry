# trailmark

## Skills
Load skill file when task matches.

### audit-augmentation
>

File: `../external/trailofbits-skills/plugins/trailmark/skills/audit-augmentation/SKILL.md`

### crypto-protocol-diagram
Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

File: `../external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`

### diagramming-code
>

File: `../external/trailofbits-skills/plugins/trailmark/skills/diagramming-code/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `../external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### graph-evolution
>

File: `../external/trailofbits-skills/plugins/trailmark/skills/graph-evolution/SKILL.md`

### mermaid-to-proverif
Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

File: `../external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`

### trailmark
Builds and queries multi-language source code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, and entry point enumeration. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, or building a code graph for audit prioritization. Prefer `trailmark.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark/SKILL.md`

### trailmark-structural
Runs full Trailmark structural analysis on Trailmark 0.2.x by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, and attack surface. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark-structural/SKILL.md`

### trailmark-summary
Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

File: `../external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `../external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
