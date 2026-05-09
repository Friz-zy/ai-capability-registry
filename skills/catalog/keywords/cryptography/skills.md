# cryptography

## Skills
Select only the most relevant skills by description, then read only those `SKILL.md` files.

### constant-time-analysis
Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

File: `external/trailofbits-skills/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md`

### constant-time-testing
Constant-time testing detects timing side channels in cryptographic code. Use when auditing crypto implementations for timing vulnerabilities.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md`

### crypto-protocol-diagram
Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

File: `external/trailofbits-skills/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md`

### mermaid-to-proverif
Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

File: `external/trailofbits-skills/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`

### zeroize-audit
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

File: `external/trailofbits-skills/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md`
