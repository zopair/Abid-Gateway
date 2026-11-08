#!/usr/bin/env bash
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
mkdir -p evidence
find apps services docs scripts .github -type f -print0 2>/dev/null | sort -z | xargs -0 sha256sum > evidence/SHA256SUMS
sha256sum README.md package.json index.html >> evidence/SHA256SUMS
echo "Created evidence/SHA256SUMS"
