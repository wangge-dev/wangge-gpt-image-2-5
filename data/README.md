# 提示词内容维护源

`library.json` 保存530张提示词卡的正文、变量、变体、来源及适配说明。页面由 `python scripts/build_library.py` 生成，日常先改JSON再生成，不同时手改两份正文。

字段说明：`id` 是稳定卡片编号；`group` 对应 ecommerce、templates、gallery；`source_key` 是原库条目ID或文件名；`sources` 含具体版本链接；`preview_kind=user_result` 表示用户提供的生成图，`preview_kind=layout_diagram` 表示本库原创构图示意（不是实测成图），`preview_kind=licensed_reference`表示有逐图作者／许可／职责的真实输入参考，`licensed_references`保存原文件路径、作者、文件页、许可URL、职责、改动和核查日期，不计生成结果；旧来源预览仍标为原库参考；`settings_note` 用于透明输出等特殊设置，`usage_note` 保存实际使用限制。示意许可与职责见[说明](../assets/layouts/README.md)。

`variants` 存放完整独立提示词，`variants_format=complete` 时直接渲染，不再拼接基础正文与覆盖说明。变体标题保留原来源键，以便对应；合并的重复方向记在 `merged_variant_directions`，不计入变体数量。修改指令中的变量由使用者按具体问题填写，不与基础提示词变量混用。2026-10-22人工对标补强后为149个完整变体，其中电商100个；新增EC56单图无配料、EC57双款选款、EC58单图腕表三个完整分支。EC06三个来源键保留且分开版式。每段只填自身引用变量，单图默认值不得残留多图号。后续独立成片批新增EC62／EC63，基础词550、149变体，当前64条预览含24张原创构图示意及三张真实输入参考预览，28张常用精选全部有预览；三张历史用户结果不变，示意不计生成结果。

9条原创提示词维护在 `experiments/`，11条明确来源的中文提示词维护在 `cases/`；这两组不重复放入本JSON。

原始大体量JSON不重复放入本仓库。来源盘点见[来源目录](../sources/README.md)。`scripts/build_inventory.py` 是本次来源版本的重建工具，使用新版源数据时须先更新脚本中的源版本与对应说明，不能用旧版本号标新内容。

## 可筛选画廊

`library.json` 的 `example` 与 `example_inputs` 保存具体示例；模板仍保存在 `prompt`。`gallery-metadata.json` 维护人工核对的筛选标签与官方图来源。`scripts/build_gallery.py` 同时读取来源卡与原创卡，生成 `browse/index.html`，不需要构建依赖或登录。

`entry` 按实际交付区分主图、场景、详情、活动、编辑与一致性、商业创意、结构与资料核对及其他任务；`featured` 仅表示常用入口精选，不代表已实测。2026-10-01旧548条导航已补齐；2026-10-22后续新增两卡后为550条导航元数据，其中530张为JSON卡。`product_category` 按可复用任务对象归类，不用填写示例中的商品限定通用卡；材质模板或跨品类工作流保留“通用品类”。商品类缺省标签也不得回落为“非商品专项”。
