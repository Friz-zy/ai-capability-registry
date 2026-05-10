#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

# Sync external submodules with registry config (add/remove/update to match skills.yaml)
./scripts/update-external.py

# Validate registry
./scripts/validate-registry.py

# Sync skill catalog chunks and generate the combined skills tree
./scripts/discover-skills.py

# Generate MCP routing indexes from mcp-catalog.d/
./scripts/generate-mcp.py

echo "Bootstrap complete"
