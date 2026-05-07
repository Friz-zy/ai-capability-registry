# Tag: trailmark

Skills with tag `trailmark`:

## audit-augmentation

>

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/audit-augmentation`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/audit-augmentation/SKILL.md`
- **Tags**: `audit`, `audit-augmentation`, `augmentation`, `trailmark`

## crypto-protocol-diagram

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`
- **Tags**: `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`, `cryptographic`, `diagram`, `diagramming`, `diagrams`, `double`, `drawing`, `ecdh`, `exchange`, `extracting`, `extracts`, `flow`, `frost`, `generates`, `handshake`, `informal`, `key`, `mermaid`, `message`, `model`, `models`, `noise`, `papers`, `prose`, `protocol`, `protocols`, `proverif`, `pseudocode`, `ratchet`, `rfc`, `rfcs`, `sequence`, `sequencediagrams`, `signal`, `spec`, `spthy`, `tamarin`, `tls`, `trailmark`, `visualizing`, `x3dh`

## diagramming-code

>

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/diagramming-code/SKILL.md`
- **Tags**: `code`, `diagramming`, `diagramming-code`, `trailmark`

## genotoxic

Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`
- **Tags**: `analyzing`, `cairo`, `cairo-mutants`, `call`, `circomvent`, `codebases`, `coverage`, `data`, `false`, `finding`, `frameworks`, `fuzzing`, `gaps`, `genotoxic`, `graph`, `graph-informed`, `identify`, `identifying`, `including`, `informed`, `missing`, `mutants`, `mutation`, `necessist`, `parses`, `positives`, `running`, `runs`, `statements`, `survived`, `targets`, `test`, `testing`, `tests`, `then`, `trailmark`, `triage`, `triaging`, `unnecessary`, `weak`

## graph-evolution

>

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/graph-evolution`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/graph-evolution/SKILL.md`
- **Tags**: `evolution`, `graph`, `graph-evolution`, `trailmark`

## mermaid-to-proverif

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`
- **Tags**: `attacks`, `authentication`, `checking`, `converting`, `cryptographic`, `describing`, `diagram`, `formal`, `formally`, `forward`, `generating`, `mermaid`, `mermaid-to-proverif`, `model`, `models`, `producing`, `properties`, `protocol`, `protocols`, `proverif`, `replay`, `secrecy`, `security`, `sequence`, `sequencediagrams`, `trailmark`, `translates`, `verification`, `verifying`

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

## trailmark-summary

Runs a Trailmark summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: trailmark summary, code summary, structural overview.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/trailmark-summary/SKILL.md`
- **Tags**: `analysis`, `auto`, `auto-detected`, `code`, `codebase`, `count`, `dependency`, `detected`, `entry`, `galvanize`, `languages`, `needs`, `point`, `returns`, `runs`, `structural`, `summary`, `trailmark`, `trailmark-summary`, `triggers`, `vivisect`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
