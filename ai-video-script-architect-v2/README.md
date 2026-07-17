# AI视频剧本架构师 V2（中文 Skill）

这是现有 `ai-native-video-architect-zh` 的完整V2并行包，重点从“AI原生机制”扩展为完整的AI视频剧本架构系统。

## 安装

将整个 `ai-video-script-architect-v2` 目录复制到：

- Windows：`%USERPROFILE%\.agents\skills\ai-video-script-architect-v2`
- macOS/Linux：`$HOME/.agents/skills/ai-video-script-architect-v2`

也可以运行：

```powershell
.\scripts\install_windows.ps1
```

```bash
bash scripts/install_unix.sh
```

## 调用

```text
使用 $ai-video-script-architect-v2-zh，
帮我设计一个90秒现实主义AI短片。
```

```text
使用 $ai-video-script-architect-v2-zh，
只诊断下面剧本，不要重写。
```

```text
使用 $ai-video-script-architect-v2-zh，
保留人物和结尾，把剧本改成更适合竖屏传播的版本，并输出去时效版。
```

## 目录

- `SKILL.md`：Skill入口。
- `AGENT.md`：统一系统合同。
- `modes/`：Create、Transform、Diagnose、Adapt。
- `core/`：故事、连续性、对白、改写、制作。
- `controllers/`：类型、视觉、短视频与热梗控制器。
- `evals/`：九项专项评估。
- `templates/`：六个正式模板。
- `tests/`与`audit/`：压力测试和一致性审计。

## 验证

```bash
python scripts/validate_package.py
```
