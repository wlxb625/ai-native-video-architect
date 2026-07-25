# AI Native Film Studio V3.2

一套中文AI电影导演、资产设计与制作Skill。

显式调用：

```text
$ai-native-video-architect-zh
```

## 完整链路

```text
创作访谈
→ 概念与剧本
→ 视觉叙事与镜头语言
→ Visual Bible
→ 角色、服装、场景和道具资产
→ Asset Readiness Gate
→ 首帧、尾帧和详细分镜
→ 视频动作Prompt、续拍和硬切
→ 制片、声音、调色、传播与导演审查
```

## V3.2：资产先行

V3.2不再从剧本直接跳到批量视频Prompt。

正式制作前按需建立：

- 角色生产三视图、面部身份、发型和姿态；
- 服装结构与状态版本；
- 场景主布局、无人物空镜和多机位；
- 道具尺寸、三视图、交互和状态链；
- 资产ID、版本和镜头依赖；
- 分镜首帧与尾帧；
- Core Sample与不同机位一致性测试。

图片Prompt负责静态身份、状态、构图、光线和材质；视频Prompt负责从指定首帧完成一个明确动作并抵达指定结束状态。

## 创作前访谈

宽泛请求会先通过选择或填空确认类型、情绪、形式、场景、主角、关系、对白、结尾、时长画幅、工具阶段和禁忌，再提供差异化创作方向。

## 输出层级

- `CONCEPT_DIRECTION`
- `DEVELOPMENT_PACKAGE`
- `ASSET_PACK`
- `DIRECTOR_PACKAGE`
- `DETAILED_STORYBOARD`
- `PRODUCTION_PACK`

## 核心新增文件

- `controllers/asset-first-production.md`
- `evals/asset-readiness-score.md`
- `templates/asset-registry.md`
- `templates/character-asset-pack.md`
- `templates/environment-asset-pack.md`
- `templates/prop-asset-pack.md`
- `templates/frame-generation-pack.md`

## 安装

```bash
git clone https://github.com/wlxb625/ai-native-video-architect.git
cd ai-native-video-architect/ai-native-video-architect-zh
```

复制到：

```text
Windows: %USERPROFILE%\.agents\skills\ai-native-video-architect-zh
macOS/Linux: $HOME/.agents/skills/ai-native-video-architect-zh
```

## 验证

```bash
python scripts/validate_package.py
```

详细说明见 `ai-native-video-architect-zh/README.md`。
