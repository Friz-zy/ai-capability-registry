#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "${ROOT_DIR}"

git submodule update --init --recursive
./scripts/validate-registry.py
./scripts/discover-capabilities.py
./scripts/generate-readme.py

echo "Bootstrap complete"
