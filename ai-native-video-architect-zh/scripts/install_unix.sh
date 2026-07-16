#!/usr/bin/env bash
set -euo pipefail

SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_ROOT="${HOME}/.agents/skills"
TARGET="${SKILLS_ROOT}/ai-native-video-architect-zh"

mkdir -p "${SKILLS_ROOT}"
rm -rf "${TARGET}"
cp -R "${SOURCE}" "${TARGET}"

echo "已安装 AI 原生视频架构师（中文）到：${TARGET}"
echo "请新建 Codex 会话；如果没有识别到 Skill，请重启 Codex。"
