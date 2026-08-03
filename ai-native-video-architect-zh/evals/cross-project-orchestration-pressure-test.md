# Cross-Project Temporal Visual Orchestration Pressure Test V4.5

## 目的

验证`temporal-visual-orchestration.md`是否允许不同项目得出不同导演答案，而不是把某个参考视频中的主体先动、环境响应、摄影机跟随和移动高光固化为默认。

本测试覆盖五种明显不同的项目条件。以下内容是规则压力测试，不是项目默认模板。

---

## Case A｜现实主义人物关系

### 场景

清晨火车站，父亲与女儿刚完成物品交接。情绪依靠未完成手势和时间压力。

### 选择

```yaml
directing_form: NARRATIVE_DRIVEN
dominant_agency: CHARACTER
coupling_mode: COUNTERPOINT
camera_role: HOLD
environment_role: REMAIN_NEUTRAL
light_role: STABILIZE
sound_role: LEAD
```

### 原因

- 人物关系和动作残留是主要信息；
- 环境不应神奇回应人物情绪；
- 固定摄影机让观众观察克制表演；
- 站台广播或关门提示音先出现，形成时间压力；
- 冷暖光保持稳定，不随情绪闪烁。

### 证明

该项目不采用“人物动作带动环境、摄影机随后跟随”。通用控制器仍能成立。

---

## Case B｜悬疑走廊

### 场景

夜间办公楼，人物尚未察觉走廊尽头的门正在缓慢开启。

### 选择

```yaml
directing_form: NARRATIVE_DRIVEN
dominant_agency: ENVIRONMENT
coupling_mode: ANTICIPATORY
camera_role: REVEAL
environment_role: INITIATE
light_role: ANTICIPATE
sound_role: LEAD
```

### 原因

- 环境先发生异常；
- 摄影机先于人物发现门缝变化，使观众成为先知；
- 门内光线先扩大一线，但不完全揭示内部；
- 声音先出现，人物稍后反应；
- 人物在前半镜保持不动。

### 证明

摄影机可以先动，灯光可以先于人物变化，环境可以拥有主导权。

---

## Case C｜办公室冷幽默

### 场景

员工郑重宣布辞职，办公室打印机在沉默两秒后突然吐出大量无关纸张。

### 选择

```yaml
directing_form: HYBRID
dominant_agency: CHARACTER
coupling_mode: DELAYED
camera_role: HOLD
environment_role: DELAY
light_role: IGNORE
sound_role: COUNTERPOINT
```

### 原因

- 人物先完成严肃动作；
- 环境不立即响应，延迟两秒形成喜剧节拍；
- 摄影机保持严肃固定构图；
- 灯光完全忽视事件，维持平淡办公照明；
- 打印机机械声打断沉默，形成声音对位。

### 证明

环境延迟、摄影机不跟随、灯光不响应同样可以形成高度统一的镜头。

---

## Case D｜动作释放高潮

### 场景

主角冲破封锁门进入开阔空间，追兵仍从后方逼近。

### 选择

```yaml
directing_form: HYBRID
dominant_agency: GROUP
coupling_mode: RESISTANT
camera_role: RESIST
environment_role: OPPOSE
light_role: REVEAL
sound_role: SYNCHRONIZE
```

### 原因

- 主角向前冲，摄影机短暂反向后撤维持压迫距离；
- 门和空间结构形成真实阻力，而不是顺从人物；
- 光线在门被撞开后揭示开阔区域，变化由物理事件触发；
- 追兵与主角形成相反运动方向；
- 声音在撞击点同步，但随后节奏分离。

### 证明

摄影机与主体可以对抗，环境可以作为阻力，而非响应或托举人物。

---

## Case E｜抽象视觉序列

### 场景

无明确现实空间，人物记忆被分成互相错位的房间、声音和影子。

### 选择

```yaml
directing_form: VISUAL_SEQUENCE_DRIVEN
dominant_agency: NONE
coupling_mode: PARTIALLY_DECOUPLED
camera_role: DESTABILIZE
environment_role: MISLEAD
light_role: CONTRADICT
sound_role: BRIDGE
```

### 原因

- 没有单一主导者；多个系统服从“记忆时间不同步”的形式规则；
- 人物动作与影子存在固定延迟；
- 摄影机在空间接缝处产生有意失稳；
- 灯光方向与人物朝向不一致，表达记忆错位；
- 声音跨越空间连接本不相邻的房间；
- 部分连续、部分断裂，不追求自然物理融合。

### 证明

统一不等于同步或自然因果。有意脱节只要拥有稳定形式规则，也可以是高质量导演选择。

---

## 横向结论

### 可迁移机制

1. 多系统变化需要明确主导权或共享规则；
2. 摄影机、灯光、环境和声音需要定义相对时序角色；
3. 统一可以来自因果、同步、延迟、对位、抵抗或有意脱节；
4. 镜头必须有可验证的初始关系、发展和结束关系；
5. 相邻镜头需要选择感知连续通道，或说明有意断裂；
6. 同一序列不能机械重复一种关系。

### 不可固化的具体手法

- 人物必须先动；
- 环境必须响应人物；
- 摄影机必须随后跟随；
- 高光必须依附运动材质；
- 所有镜头必须形状和方向连续；
- 所有动作必须跟音乐重拍；
- 所有视觉高潮都依靠材质变形。

### 压力测试结果

```yaml
status: PASS
allows_multiple_directing_answers: true
case_specific_aesthetic_leakage: false
supports_camera_lead_follow_hold_resist: true
supports_light_follow_anticipate_ignore_contradict: true
supports_environment_initiate_respond_ignore_oppose_delay: true
supports_causal_and_intentional_decoupling: true
supports_continuity_and_intentional_discontinuity: true
narrative_lock_conflicts: []
fixed_default_conflicts: []
```

## 进入核心Skill的建议

允许进入：

- 测试学习抽象协议；
- 主导权、耦合方式和时序角色；
- 感知连续通道；
- 序列关系变化与冲突检查；
- 项目专属选择与理由。

仅进入案例库：

- 当前用户参考视频中的具体红日、金液、绸带、人物先动、摄影机后跟和移动高光策略；
- 本测试五个场景的具体内容和参数。

本测试证明：新控制器适合作为现有导演系统的通用决策层，但不应成为固定视觉序列模板。