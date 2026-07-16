#!/usr/bin/env bash
set -euo pipefail

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="${HOME}/.agents/skills"
TARGET="${SKILLS_ROOT}/ai-native-video-architect"

mkdir -p "${SKILLS_ROOT}"
rm -rf "${TARGET}"
cp -R "${SOURCE}" "${TARGET}"

echo "Installed AI Native Video Architect to: ${TARGET}"
echo "Start a new Codex conversation. Restart Codex if the skill is not detected."
