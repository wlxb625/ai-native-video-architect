# Contract Skill 强执行协议

## 激活义务

调用本包时，第一项动作不是创作，而是激活契约：

```bash
python scripts/contract_runner.py start --request-file <用户任务文件>
```

若宿主支持脚本执行，未生成`ACTIVATION_RECEIPT`前禁止输出领域成品。

若宿主不支持脚本执行，只能进入`SOFT_CONTRACT`：必须明确说明无法提供强制执行凭证，并仍按阶段顺序工作；不得声称已经通过强门禁。

## 单阶段暴露

每次只运行：

```bash
python scripts/contract_runner.py prepare --task-id <TASK_ID>
```

该命令生成当前阶段Prompt Packet。模型只应依据当前Packet工作，不得提前撰写未来阶段产物。

## 提交与门禁

阶段产物写入JSON文件后提交：

```bash
python scripts/contract_runner.py submit --task-id <TASK_ID> --artifact <FILE>
```

若阶段需要评估，Runner会进入`AWAITING_EVALUATION`。评估结果必须独立生成并提交：

```bash
python scripts/contract_runner.py evaluate --task-id <TASK_ID> --evaluation <FILE>
```

Runner依据固定阈值决定PASS、CONDITIONAL或FAIL。模型无权修改状态。

## 返修

- `CONDITIONAL`：回到当前阶段，只修`must_fix`。
- `FAIL`：按契约退回当前或上一阶段。
- 每个门禁最多两轮。
- `must_protect`必须在返修中保留。

## 完成

只有Runner进入`READY_TO_FINALIZE`后才允许：

```bash
python scripts/contract_runner.py finalize --task-id <TASK_ID> --artifact <FINAL_FILE>
```

成功后产生`CONTRACT_COMPLETE`凭证。没有凭证的内容只能称为草稿、候选或未验证产物。

固定生命周期：`prepare → submit → evaluate → finalize`。

## 高潮强制检查

S02与S03必须调用`evals/climax-force-check.md`。默认高潮档位为`STRONG_DRAMATIC_PEAK`。

以下内容不能单独充当强戏剧高潮：覆盖旧物、烧毁纪念品、剪断连接物、关灯、离开、清理痕迹、沉默告别。只有在它们同时承接至少两次压力升级、两个真实价值、不可拖延触发点、非预定结果、现场代价和高潮后状态翻转时，才可通过。

评估必须携带与当前产物哈希绑定的`evaluation_context`，生成上下文ID与评估上下文ID必须不同。


## 0.3 门禁强化
- 第一层执行下限不可由自适应层修改。
- 适用性声明决定NOT_APPLICABLE是否合法。
- 评估必须匹配当次nonce与评估规则哈希。
- S04-S12必须提交非空内容和完整coverage。
- S13最终文件哈希必须与交付声明一致。
