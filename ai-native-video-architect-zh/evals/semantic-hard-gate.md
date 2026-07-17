# Semantic Hard Gate

## 职责
检查事实、信息、知识、原话、文件、道具、时间、空间、视角、现实层级和制作语义回归。

## 统一输出
```yaml
status: PASS | CONDITIONAL | FAIL
design_tags: []
applicability: HIGH | MEDIUM | LOW | NOT_APPLICABLE
evidence: []
risks: []
must_fix: []
should_strengthen: []
must_protect: []
```

## 评估维度
- 确认事实与人物说法分离
- 人物知识来源与确定程度
- 文件/消息/系统状态
- 道具持有人与状态
- 时间空间连续性
- 主观视角与不可靠叙述
- 开放事实与故意矛盾
- 粗剪后的语义顺序

## 合法设计标签
- `INTENTIONAL_AMBIGUITY`
- `UNRELIABLE_NARRATION`
- `MULTIPLE_REALITIES`
- `INTENTIONAL_DISCONTINUITY`

## 硬失败
- 1. 确认事实无意矛盾
- 2. 人物使用无来源信息
- 3. 关键原话改变行为含义
- 4. 文件/消息状态错误
- 5. 道具无来源转移
- 6. 时间空间不可能且无规则
- 7. 客观镜头虚构事实
- 8. 制作改变事实或知识顺序

## 条件通过
- 1. 开放内容边界略弱
- 2. 现实层级标记不足
- 3. 制作可能制造误读
- 4. 人物确定程度略过强
