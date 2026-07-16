$ErrorActionPreference = "Stop"

$Source = Split-Path -Parent $PSScriptRoot
$SkillsRoot = Join-Path $HOME ".agents\skills"
$Target = Join-Path $SkillsRoot "ai-native-video-architect"

New-Item -ItemType Directory -Path $SkillsRoot -Force | Out-Null
if (Test-Path $Target) {
    Remove-Item -Path $Target -Recurse -Force
}
Copy-Item -Path $Source -Destination $Target -Recurse -Force

Write-Host "Installed AI Native Video Architect to: $Target"
Write-Host "Start a new Codex conversation. Restart Codex if the skill is not detected."
