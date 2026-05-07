# Contributing

This registry is security-first. New capabilities are indexed before they are enabled.

## Contribution Flow

1. Add or update entries in `registry/*.yaml`.
2. Pin upstream sources with a tag and commit when possible.
3. Set conservative defaults: read-only, disabled, or manual enablement.
4. Run `./scripts/validate-registry.py`.
5. Run `./scripts/generate-index.py` and `./scripts/generate-readme.py`.
6. Review generated files before submitting changes.

## Capability Rules

- Do not add `curl | sh`, random `npx`, or arbitrary local Python/Node execution paths.
- Prefer hosted HTTPS/OAuth or Docker-isolated runtimes.
- Do not enable community sources by default without manual review.
- Keep generated files generated; edit registry YAML instead.
