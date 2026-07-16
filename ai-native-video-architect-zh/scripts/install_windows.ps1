$ErrorActionPreference = "Stop"

$Source = Split-Path -Parent $PSScriptRoot
$SkillsRoot = Join-Path $HOME ".agents\skills"
$Target = Join-Path $SkillsRoot "ai-native-video-architect-zh"

New-Item -ItemType Directory -Path $SkillsRoot -Force | Out-Null
if (Test-Path $Target) {
    Remove-Item -Path $Target -Recurse -Force
}
Copy-Item -Path $Source -Destination $Target -Recurse -Force

Write-Host "已安装 AI 原生视频架构师（中文）到：$Target"
Write-Host "请新建 Codex 会话；如果没有识别到 Skill，请重启 Codex。"
