# AI Native Video Architect — 中英双版本

本仓库包含两个可独立安装的 Codex Skill：

- `ai-native-video-architect`：英文版，显式调用 `$ai-native-video-architect`
- `ai-native-video-architect-zh`：中文版，显式调用 `$ai-native-video-architect-zh`

## 推荐安装方式

中文创作为主时，只安装 `ai-native-video-architect-zh`。

英文创作为主时，只安装 `ai-native-video-architect`。

如果同时安装两个版本，建议使用显式调用，避免两个高度相似的 Skill 在隐式路由时产生竞争。

## 用户级安装目录

### Windows

```text
%USERPROFILE%\.agents\skills\
```

### macOS / Linux

```text
$HOME/.agents/skills/
```

将选择的整个 Skill 文件夹复制到该目录即可。
