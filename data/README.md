# 提示词内容维护源

`library.json` 保存77张适配卡的正文、变量、变体、来源及适配说明。页面由 `python scripts/build_library.py` 生成，日常先改JSON再生成，不同时手改两份正文。

字段说明：`id` 是稳定卡片编号；`group` 对应 ecommerce、templates、gallery；`source_key` 是原库条目ID或文件名；`sources` 含具体版本链接；`preview` 如有则是旧版参考；`settings_note` 用于透明输出等特殊设置。

`variants` 存放对基础正文的明确改动，生成器把基础正文和该改动组成独立可复制块。变体标题保留原来源键，以便对应；变体内容可以根据事实与任务边界改写，不能把名称存在当完成。

原始大体量JSON不重复放入本仓库。来源盘点见[来源目录](../sources/README.md)。`scripts/build_inventory.py` 是本次来源版本的重建工具，使用新版源数据时须先更新脚本中的源版本与对应说明，不能用旧版本号标新内容。
