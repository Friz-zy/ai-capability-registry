# Tag: cryptographic

Skills with tag `cryptographic`:

## constant-time-analysis

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis`
- **Skill file**: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`
- **Tags**: `analysis`, `branches`, `channel`, `code`, `constant`, `constant-time`, `constant-time-analysis`, `crypto`, `cryptographic`, `dependent`, `detects`, `division`, `encountering`, `implementing`, `java`, `javascript`, `kotlin`, `php`, `programming`, `python`, `questions`, `reviewing`, `ruby`, `rust`, `secret`, `secret-dependent`, `secrets`, `side`, `side-channel`, `swift`, `time`, `timing`, `typescript`, `vulnerabilities`

## crypto-protocol-diagram

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`
- **Tags**: `academic`, `annotations`, `code`, `crypto`, `crypto-protocol-diagram`, `cryptographic`, `diagram`, `diagramming`, `diagrams`, `double`, `drawing`, `ecdh`, `exchange`, `extracting`, `extracts`, `flow`, `frost`, `generates`, `handshake`, `informal`, `key`, `mermaid`, `message`, `model`, `models`, `noise`, `papers`, `prose`, `protocol`, `protocols`, `proverif`, `pseudocode`, `ratchet`, `rfc`, `rfcs`, `sequence`, `sequencediagrams`, `signal`, `spec`, `spthy`, `tamarin`, `tls`, `trailmark`, `visualizing`, `x3dh`

## mermaid-to-proverif

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`
- **Tags**: `attacks`, `authentication`, `checking`, `converting`, `cryptographic`, `describing`, `diagram`, `formal`, `formally`, `forward`, `generating`, `mermaid`, `mermaid-to-proverif`, `model`, `models`, `producing`, `properties`, `protocol`, `protocols`, `proverif`, `replay`, `secrecy`, `security`, `sequence`, `sequencediagrams`, `trailmark`, `translates`, `verification`, `verifying`

## sharp-edges

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges`
- **Skill file**: `external/trailofbits-skills/plugins/sharp-edges/skills/sharp-edges/SKILL.md`
- **Tags**: `api`, `apis`, `code`, `configuration`, `configurations`, `cryptographic`, `dangerous`, `default`, `defaults`, `designs`, `edges`, `enable`, `ergonomics`, `error`, `error-prone`, `evaluating`, `follows`, `footgun`, `identifies`, `library`, `mistakes`, `misuse`, `misuse-resistant`, `pit`, `principles`, `prone`, `resistant`, `reviewing`, `schemas`, `secure`, `security`, `sharp`, `sharp-edges`, `success`, `triggers`, `usability`, `whether`

## vector-forge

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

- **Source**: `trailofbits-skills` (trusted)
- **Path**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge`
- **Skill file**: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
- **Tags**: `algorithm`, `code`, `compares`, `coverage`, `creating`, `cross`, `cross-implementation`, `crypto`, `cryptographic`, `deliberately`, `driven`, `effectiveness`, `escaped`, `exercise`, `finding`, `finds`, `forge`, `gaps`, `generates`, `generating`, `generation`, `identify`, `implementation`, `implementations`, `improving`, `kill`, `measuring`, `mutants`, `mutation`, `mutation-driven`, `paths`, `primitives`, `protocol`, `prove`, `rates`, `runs`, `suites`, `test`, `testing`, `then`, `trailmark`, `uncovered`, `vector`, `vector-forge`, `vectors`, `wycheproof`
