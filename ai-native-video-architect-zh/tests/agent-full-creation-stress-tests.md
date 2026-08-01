# Agent Full Creation Stress Tests V4.4

## FULL_PACKAGE_NO_ASSET_GATE

用户只有想法并要求全套制作包。

PASS：Agent完成剧本、规划资产Prompt、Shot、CF、生图Prompt和视频Prompt；参考图未真实生成不阻塞。

FAIL：输出资产Prompt后要求用户先生成图片再继续。

## SHOT_WITHOUT_PROMPT

镜头表有12个Shot，其中2个被模型视为过渡镜头。

PASS：12个Shot都有制作卡；过渡镜头也有可见描述、参考继承和视频Prompt或POST_ONLY说明。

FAIL：只给10条Prompt或空白参考字段。

## CF_ORPHAN

生成CF但没有Shot归属。

PASS：内部修复ID与shot_id绑定。

FAIL：最终包出现孤立CF。

## INHERITED_FRAME_NOT_BLANK

Shot使用上一镜尾帧。

PASS：写明上一镜CF、基础资产、允许变化和备用首帧Prompt。

FAIL：图片Prompt写“沿用上一镜”或留空。

## NO_NEW_REFERENCE

某空镜没有角色参考。

PASS：明确只使用场景资产，并说明无需角色参考。

FAIL：参考图字段为空。

## POST_ONLY_COVERAGE

精确手机文字由后期完成。

PASS：Shot标记POST_ONLY并给素材、合成、时长和剪辑说明。

FAIL：因为无视频Prompt而直接遗漏该Shot。

## PAIRWISE_CONTINUITY

上一镜右手拿钥匙，下一镜改成左手。

PASS：内部检查发现并统一，或设计可见换手动作。

FAIL：直接交付冲突Prompt。

## FIRST_LAST_FRAME_DECISION

下一镜依赖准确门把手状态。

PASS：使用首尾帧或明确抽尾帧续拍。

FAIL：单首帧自由结束。

## ID_COVERAGE

Shot总表、CF表、图片Prompt和视频Prompt编号不一致。

PASS：交付前修复到完全一致。

FAIL：存在缺号、重复号或未定义引用。

## FULL_PACKAGE_STATUS

没有真实生成媒体。

PASS：状态为PROMPT_PACKAGE_READY。

FAIL：声称SAMPLE_VALIDATED或DELIVERY_READY。
