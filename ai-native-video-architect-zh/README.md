# AI 原生视频架构师（中文版 Skill）

这是本仓库可直接安装的中文 Codex Skill，显式调用名称为：

```text
$ai-native-video-architect-zh
```

它用于：

- 从零设计 AI 原生叙事短片；
- 将已有故事或剧本进行 AI 原生化改造；
- 诊断创意是否只是 AI 特效拼贴；
- 建立世界规则、人物因果和场景图谱；
- 将方案拆成可制作镜头与生成任务；
- 对现实主义、恐怖、喜剧加载不同控制器；
- 运行 AI 原生性、类型、反套路和生产可行性检查。

完整项目说明请阅读仓库根目录的 [`README.md`](../README.md)。

---

## 快速安装

### Windows

复制整个目录到：

```text
%USERPROFILE%\.agents\skills\ai-native-video-architect-zh
```

或在当前目录运行：

```powershell
.\scripts\install_windows.ps1
```

### macOS / Linux

复制到：

```text
$HOME/.agents/skills/ai-native-video-architect-zh
```

或运行：

```bash
bash scripts/install_unix.sh
```

### 项目级安装

```text
<项目根目录>/.agents/skills/ai-native-video-architect-zh
```

安装后重新打开 Codex 会话，首次建议显式调用：

```text
使用 $ai-native-video-architect-zh，
帮我设计一个90秒关于职场隐形劳动的现实主义AI原生短片。
```

---

## 四种工作模式

| 模式 | 用途 | 常见请求 |
|---|---|---|
| Create | 从零创作 | 帮我想一个 AI 短片 |
| Transform | 原生化改造 | 把这个剧本改成 AI 原生版本 |
| Diagnose | 诊断与评分 | 这个创意算 AI 原生吗 |
| Adapt | 制作适配 | 拆成可生成镜头和任务 |

混合请求按照：

```text
Diagnose → Transform → Adapt
```

执行。

---

## 默认输出

用户没有指定时，默认：

- 时长 60—120 秒；
- 人物 1—3 名；
- 5—8 个场景节点；
- 一个主机制；
- 最多一个辅助机制；
- 对白低到中；
- 输出 Level 2 标准方案。

默认不会把全部理论、候选机制和评分表都展示出来。需要时可明确要求：

```text
给我完整创作包。
```

```text
做深度诊断并显示评分。
```

```text
进入生产适配，拆成镜头和生成任务。
```

---

## 关键设计原则

1. 先找人物处境中的不可见矛盾，再想 AI 画面；
2. 默认一个主机制，不堆叠无关效果；
3. 机制必须具有触发、响应、升级、人物影响和结尾兑现；
4. 删除机制后故事核心不应完全不受影响；
5. 现实主义必须保留现实责任；
6. 恐怖的未知不能来自规则随意改变；
7. 喜剧规则应快速理解，并控制伤害阈值；
8. 制作降级优先改变镜头实现，不改变核心意义；
9. AI 原生不等于纯 AI 制作；
10. 高频意象可以使用，但必须证明不可替代性。

---

## 目录说明

```text
SKILL.md          入口、路由和硬规则
modes/            Create、Transform、Diagnose、Adapt
controllers/      现实主义、恐怖、喜剧和通用叙事控制器
references/       核心工作流、机制库、世界规则、场景图谱、生产适配
templates/        概念、标准方案、完整创作包、诊断、剧本和生产包模板
evals/            AI原生评分、反套路、类型、生产和回归测试
examples/         现实主义、恐怖、喜剧和制作适配案例
scripts/          安装、校验和评分辅助工具
```

主入口会按任务渐进读取文件，不会一次加载全部参考内容。

---

## 校验

```bash
python scripts/validate_package.py
```

评分辅助：

```bash
python scripts/score_concept.py
```

触发测试：

```text
evals/trigger-tests.csv
```

回归案例：

```text
evals/regression-cases.md
```

---

## 调用示例

### 从零创作

```text
使用 $ai-native-video-architect-zh，
设计一个90秒恐怖短片：一段旧家庭语音每次播放都会多一句话。
不要鬼脸，不要死亡预言，使用软规则或观察污染结构。
```

### 改造剧本

```text
使用 $ai-native-video-architect-zh，
保留下面剧本的人物和结局，进行中度AI原生化改造。
不要使用透明人物、镜子、时间循环和粒子消散。
```

### 只诊断

```text
使用 $ai-native-video-architect-zh，
只诊断这个创意，不要改写。
运行去AI测试、机制替换测试、因果参与测试和类型漂移测试。
```

### 制作适配

```text
使用 $ai-native-video-architect-zh，
不改变核心机制和结尾，拆成场景、镜头和生成任务。
给出理想实现、稳定实现和最低成本实现。
```

---

## 版本

当前版本：`0.8.0`

详细更新记录见 [`CHANGELOG.md`](CHANGELOG.md)。
