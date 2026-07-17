param(
  [string]$Destination = "$HOME\.agents\skills\ai-native-video-architect-zh"
)
$Source = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Parent = Split-Path $Destination -Parent
New-Item -ItemType Directory -Path $Parent -Force | Out-Null
if (Test-Path $Destination) { Remove-Item $Destination -Recurse -Force }
Copy-Item $Source $Destination -Recurse -Force
python (Join-Path $Destination "scripts\validate_package.py")
Write-Host "Installed to $Destination"
