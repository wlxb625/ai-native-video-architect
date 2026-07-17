#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$HOME/.agents/skills/ai-video-script-architect-v2}"
mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
python3 "$DEST/scripts/validate_package.py"
echo "Installed to $DEST"
