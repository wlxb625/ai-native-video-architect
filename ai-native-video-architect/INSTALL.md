# Installation

## User-scoped installation

Install the entire `ai-native-video-architect` folder under your personal Codex skills directory:

- Windows: `%USERPROFILE%\.agents\skills\ai-native-video-architect`
- macOS/Linux: `$HOME/.agents/skills/ai-native-video-architect`

You can use the included helper scripts from the extracted skill folder:

### Windows PowerShell

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\install_windows.ps1
```

### macOS/Linux

```bash
chmod +x scripts/install_unix.sh
./scripts/install_unix.sh
```

## Repository-scoped installation

Place the folder at:

```text
<repository>/.agents/skills/ai-native-video-architect
```

Use repository scope when the skill should travel with one project or team.

## Verify

Run:

```bash
python scripts/validate_package.py
```

Then start a new Codex conversation and invoke it explicitly:

```text
$ai-native-video-architect 给我设计一个90秒AI原生短片。
```

Codex normally detects changes automatically. Restart Codex when the skill does not appear after installation or modification.
