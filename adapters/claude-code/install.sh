#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TARGET_DIR="${HOME}/.claude/skills"

mkdir -p "${TARGET_DIR}"
ln -sfn "${ROOT_DIR}/generated/skills.md" "${TARGET_DIR}/global-skills.md"
ln -sfn "${ROOT_DIR}/generated/mcp-catalog.md" "${TARGET_DIR}/mcp-catalog.md"

echo "Linked Claude Code registry artifacts into ${TARGET_DIR}"
