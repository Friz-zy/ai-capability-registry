# fuzzing

## Skills
Select only the most relevant skills by description. If a skill matches, read its `SKILL.md` and use it before acting.

### address-sanitizer
AddressSanitizer detects memory errors during fuzzing. Use when fuzzing C/C++ code to find buffer overflows and use-after-free bugs.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md`

### aflpp
AFL++ is a fork of AFL with better fuzzing performance and advanced features. Use for multi-core fuzzing of C/C++ projects.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/aflpp/SKILL.md`

### atheris
Atheris is a coverage-guided Python fuzzer based on libFuzzer. Use for fuzzing pure Python code and Python C extensions.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/atheris/SKILL.md`

### cargo-fuzz
cargo-fuzz is the de facto fuzzing tool for Rust projects using Cargo. Use for fuzzing Rust code with libFuzzer backend.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md`

### ffuf-web-fuzzing
Expert guidance for ffuf web fuzzing during authorized penetration testing. Covers directory discovery, subdomain enumeration, parameter fuzzing, authenticated fuzzing with raw requests, auto-calibration, and result analysis. Use when running ffuf scans, analyzing ffuf output, or building fuzzing strategies for web targets.

File: `external/trailofbits-skills-curated/plugins/ffuf-web-fuzzing/skills/ffuf-web-fuzzing/SKILL.md`

### fuzzing-dictionary
Fuzzing dictionaries guide fuzzers with domain-specific tokens. Use when fuzzing parsers, protocols, or format-specific code.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md`

### fuzzing-obstacles
Techniques for patching code to overcome fuzzing obstacles. Use when checksums, global state, or other barriers block fuzzer progress.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md`

### genotoxic
Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circomvent and cairo-mutants), or using necessist.

File: `external/trailofbits-skills/plugins/trailmark/skills/genotoxic/SKILL.md`

### harness-writing
Techniques for writing effective fuzzing harnesses across languages. Use when creating new fuzz targets or improving existing harness code.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md`

### libafl
LibAFL is a modular fuzzing library for building custom fuzzers. Use for advanced fuzzing needs, custom mutators, or non-standard fuzzing targets.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/libafl/SKILL.md`

### mutation-testing
Configures mewt or muton mutation testing campaigns — scopes targets, tunes timeouts, and optimizes long-running runs. Use when the user mentions mewt, muton, mutation testing, or wants to configure or optimize a mutation testing campaign.

File: `external/trailofbits-skills/plugins/mutation-testing/skills/mutation-testing/SKILL.md`

### ossfuzz
OSS-Fuzz provides free continuous fuzzing for open source projects. Use when setting up continuous fuzzing infrastructure or enrolling projects.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md`

### ruzzy
Ruzzy is a coverage-guided Ruby fuzzer by Trail of Bits. Use for fuzzing pure Ruby code and Ruby C extensions.

File: `external/trailofbits-skills/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md`

### vector-forge
Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

File: `external/trailofbits-skills/plugins/trailmark/skills/vector-forge/SKILL.md`
