# Dialogue Check

## 职责
检查言语行为、人物声音、回应、潜台词、沉默、字幕、旁白、热梗语言和口型。

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
- 人物语言目的
- 言语行为准确性
- 人物声音区分
- 回应与答非所问
- 潜台词与沉默
- 信息权限与关键原话
- 解释负载
- 字幕/旁白/语言形式
- 口型与剪辑

## 合法设计标签
- `INTENTIONAL_INDIRECTNESS`
- `INTENTIONAL_SILENCE`
- `SUBTEXT_DRIVEN`
- `EVERYDAY_DIALOGUE`
- `POETIC_DIALOGUE`
- `LANGUAGE_BREAKDOWN`
- `INTENTIONAL_REPETITION`

## 硬失败
- 1. 人物说无来源信息
- 2. 请求/拒绝/授权被改变
- 3. 关键原话不一致
- 4. 所有人物同一声音
- 5. 沉默被无依据当同意
- 6. 潜台词只是故意模糊
- 7. 语言失效无规则
- 8. 字幕/剪辑改变含义

## 条件通过
- 1. 声音基本成立但局部趋同
- 2. 潜台词依据偏弱
- 3. 说明必要但偏密
- 4. 关键口型句过长
- 5. 方言/热梗需制作验证
