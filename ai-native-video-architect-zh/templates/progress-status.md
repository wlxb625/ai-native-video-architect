# Project Progress Status Template

用于Skill首次调用、阶段切换、评估回退、用户询问进度或中途进入项目时。

## 紧凑版

```text
【项目进度｜{stage_id}/13 {stage_name}】
已完成：{completed_stages}
正在进行：{current_goal}
本轮交付：{current_deliverable}
需要你确认：{user_decision_or_none}
下一步：{next_stage}
```

## 带门槛版

```text
【项目进度｜{stage_id}/13 {stage_name}】
进入依据：{entry_reason}
已完成：{completed_stages}
正在进行：{current_goal}
本轮交付：{current_deliverable}
阶段门槛：{gate_status}
需要你确认：{user_decision}
下一步：{next_stage}
```

## 修复回退版

```text
【项目进度｜△ {stage_name}未通过】
已经保留：{protected_passed_outputs}
当前问题：{failed_evidence}
正在修复：{repair_target}
完成后返回：{return_stage}
```

## 中途进入版

```text
【项目进度｜从{stage_name}进入】
已有材料：{provided_materials}
跳过阶段：{skipped_stages}
跳过依据：{skip_reason}
当前先做：{current_goal}
下一步：{next_stage}
```

## DIAGNOSE版

```text
【项目进度｜诊断模式】
正在诊断：{artifact_type}
所属阶段：{source_stage}
本轮只做：问题定位、证据、最小修复建议
不会自动：重写、生成资产或推进生产
```

## TRANSFORM版

```text
【项目进度｜修改模式】
原成果阶段：{source_stage}
允许修改：{allowed_changes}
必须保护：{must_preserve}
当前修改：{current_target}
完成后返回：{return_stage}
```

## 显示规则

- 进度提示位于本轮主要内容之前；
- 最多显示6行，除非用户主动要求完整流程图；
- 已完成必须有实际输出、用户提供材料或明确确认作为证据；
- `需要你确认`没有内容时写“无，本轮可直接继续”，不能制造等待；
- 用户已经提供成熟剧本、资产或分镜时，从对应阶段进入；
- 跳过不等于通过，未经审核的资产必须进入S08；
- 阶段回退时说明只修哪一层，避免让用户误以为全部推翻；
- 用户明确说“不要显示进度”后，本项目后续可隐藏，直到用户再次询问。

## 阶段短名称

```text
S00 创作需求
S01 创意方向
S02 故事方案
S03 剧本或视觉脚本
S04 剧本拆解
S05 视觉圣经
S06 资产计划
S07 资产制作
S08 资产审核
S09 分镜设计
S10 分镜帧与提示词
S11 核心样片
S12 批量制作与后期
S13 导演审查与交付
```
