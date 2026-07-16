# 安装说明

## 用户级安装

将整个 `ai-native-video-architect-zh` 文件夹复制到：

### Windows

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

### macOS / Linux

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

也可以运行：

### Windows PowerShell

```powershell
.\scripts\install_windows.ps1
```

### macOS / Linux

```bash
bash scripts/install_unix.sh
```

安装后新建一个 Codex 会话。未识别时重启 Codex。

## 项目级安装

也可以放到项目目录：

```text
<项目根目录>/.agents/skills/ai-native-video-architect-zh
```

## 测试

显式调用：

```text
使用 $ai-native-video-architect-zh，帮我设计一个90秒关于职场隐形劳动的现实主义AI原生短片。
```

## 校验

```bash
python scripts/validate_package.py
```

评分辅助：

```bash
python scripts/score_concept.py
```
