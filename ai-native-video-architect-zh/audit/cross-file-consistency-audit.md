# Cross-file Consistency Audit V4.4

## 版本

- Skill版本：4.4.0；
- 核心交付：FULL_CREATION_PACKAGE；
- 无真实媒体状态：PROMPT_PACKAGE_READY。

## 核心术语

- CF：Control Frame，只属于Shot；
- PLANNED_REFERENCE：已设计Prompt但未真实生成；
- ACTUAL_REFERENCE：用户已真实生成或上传；
- DIRECTOR_INTENT：叙事功能、情绪目标、观众位置、揭示顺序和切镜理由；
- PERFORMANCE_DIRECTION：人物目标、内外情绪、可见表演、情绪节拍和结束强度；
- NON_CHARACTER_PERFORMANCE：空镜、道具或环境镜头的观看关系与环境节奏；
- POST_ONLY：由剪辑、文字、合成或后期完成。

## 跨文件一致性要求

1. `SKILL.md`、`AGENT.md`、CREATE、ADAPT和workflow均不得把参考图确认设为完整Prompt包的阻塞门；
2. 所有Shot必须有可见描述、导演意图、摄影方向、逐镜灯光、参考绑定、图像来源和视频Prompt或POST_ONLY说明；
3. 人物Shot必须有表演方向、情绪曲线和可继承结束强度；空镜必须有NON_CHARACTER_PERFORMANCE；
4. 图片Prompt、视频Prompt、Start CF、End CF中的表演状态必须一致；
5. 所有CF必须绑定一个Shot；
6. workflow保持S00至S13，S08包含导演设计，S12为内部验证，S13为完整包交付；
7. 真实媒体验收保留为可选后续能力；
8. README和Agent默认Prompt必须说明外部平台只负责执行生成；
9. 配置、Manifest、校验脚本和版本号必须均为4.4.0。
