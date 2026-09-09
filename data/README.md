# 提示词内容维护源

`library.json` 保存78张适配卡的正文、变量、变体、来源及适配说明。页面由 `python scripts/build_library.py` 生成，日常先改JSON再生成，不同时手改两份正文。

字段说明：`id` 是稳定卡片编号；`group` 对应 ecommerce、templates、gallery；`source_key` 是原库条目ID或文件名；`sources` 含具体版本链接；`preview_kind=user_result` 表示用户提供的生成图，其余预览为原库参考；`settings_note` 用于透明输出等特殊设置，`usage_note` 保存实际使用限制。

`variants` 存放完整独立提示词，`variants_format=complete` 时直接渲染，不再拼接基础正文与覆盖说明。变体标题保留原来源键，以便对应；合并的重复方向记在 `merged_variant_directions`，不计入变体数量。修改指令中的变量由使用者按具体问题填写，不与基础提示词变量混用。

9条原创提示词维护在 `experiments/`，5条明确来源的中文提示词维护在 `cases/`；这两组不重复放入本JSON。

原始大体量JSON不重复放入本仓库。来源盘点见[来源目录](../sources/README.md)。`scripts/build_inventory.py` 是本次来源版本的重建工具，使用新版源数据时须先更新脚本中的源版本与对应说明，不能用旧版本号标新内容。
