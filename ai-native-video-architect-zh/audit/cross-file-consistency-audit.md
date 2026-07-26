# Cross-File Consistency Audit V4.1

## 静态审计结论

- `SKILL.md`与`AGENT.md`均将Skill定义为“剧本创作 + 剧本后Prompt生产”的统一能力：PASS。
- 用户可从想法、大纲、完整剧本、参考图、分镜图或单个Prompt任务直接进入：PASS。
- 已有剧本时不强制重走创作阶段：PASS。
- Skill完成剧本后可继续生成核心参考图、分镜帧和视频Prompt：PASS。
- 普通短片默认采用最少必要参考图，不建立完整影视资产库：PASS。
- `LEAN`为默认，`CONTROLLED`仅按失败升级，`STUDIO`仅由用户明确要求：PASS。
- 角色默认采用综合角色板或标准三视图，场景默认采用一张无人物空镜：PASS。
- 后续分镜优先继承上一张满意分镜，不默认预制多机位空镜：PASS。
- 尾帧、手部板、面部板、技术测试和多机位参考均为按需能力：PASS。
- 用户提供Prompt资料时，原模板、主体提示和负面约束优先，自行补充必须区分：PASS。
- 图片Prompt与视频Prompt分工明确：PASS。
- 进度导航默认关闭，仅在用户要求、长任务或回退时启用：PASS。
- “下一步”表示下一个相关交付物，而不是下一张图或下一个资产：PASS。
- 用户默认自行在外部工具中生成和筛选，辅助审核仅在明确请求时启用：PASS。
- V4.1版本已同步至Manifest、配置、调用描述和验证脚本：PASS。

## 兼容性说明

- S00至S13仍作为内部兼容定位保留，不作为强制用户界面。
- 旧版完整资产、评分器和生产模板仍可用于系列项目、长片或用户明确要求的STUDIO模式。
- `CREATE`、`TRANSFORM`、`DIAGNOSE`、`ADAPT`四种操作模式继续保留。
- `STORY_DIRECTOR`、`VISUAL_DIRECTOR`、`BLOCKBUSTER_DIRECTOR`、`EXPERIMENTAL_DIRECTOR`、`PRODUCTION_DIRECTOR`继续保留。

## 非阻塞说明

- 当前执行环境无法直接连接GitHub运行完整仓库验证，因此本轮完成了文件级静态审计和验证脚本同步。
- 正式安装后应运行：`python scripts/validate_package.py`。
- 平台能力、模型版本、价格、额度和规则仍需在真实任务中实时核实。
