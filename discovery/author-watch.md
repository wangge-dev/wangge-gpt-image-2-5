# 按作者持续跟进

每轮先检查已确认来源的后续文章和原帖，再扩展作者。来源案例和旧创意分别记录；同一原帖被转载多次只保留一个条目。

| 作者／渠道 | 原始入口 | 版本证据 | 当前可用内容 | 下轮动作 |
| --- | --- | --- | --- | --- |
| OpenAI | [提示词指南](https://developers.openai.com/api/docs/guides/image-prompting) | 具体输出标注 Flare / Sunburst | C001–C004、C006–C007 | 比对新增章节、输入图与型号标签 |
| Simon Willison | [2.5文章](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) · [作者首页](https://simonwillison.net/) | 公开调用指定Sunburst | C005 | 查看后续图像编辑文章与更新 |
| withmagi / 12ui | [UI对比原帖](https://www.reddit.com/r/codex/comments/1wb8p1g/gpt_image_25_comparison_for_ui_generation/) | 作者明确称对比2、Flare与Sunburst；属于作者自述 | 候选；本次可读正文未提供完整提示词 | 跟进原帖和公开演示，取得具体正文再整理 |
| BrushGlow Editorial Team | [GPT Image 2.5提示词指南](https://gptimage2-5.art/blog/gpt-image-2-5-prompt-guide) | 页面标注按OpenAI文档整理，并自述2026-09-11五组工作流测试；属于二次整理与作者自述 | 可复用三参考职责、Keep清单和单变量编辑原则；不把其测试当本库实测 | 继续核对页面版本；有新完整正文时与现有卡去重 |

最近成功核查：2026-09-09。作者关于速度、费用或质量的感受不转写为本库实测结论。

## 每轮记录

在维护记录中写下：作者、原帖URL、原帖日期、核查日期、版本依据、完整正文是否可获取、输入和结果出处、落地卡片或未收录原因。访问失败不更新该来源的成功核查日期。

对没有新增内容的已确认作者继续保留追踪；对只有“2.5”标题的聚合页面先追原作者。旧库创意仍进入原有来源盘点，不能归到新版作者案例。

### 2026-10-01定向核查

OpenAI指南、Simon的9月8日原文及首页、BrushGlow原指南本轮可读；只核对参考职责、保留项与单变量编辑，不新增作者实测结论。未完整回扫所有作者文章，不把本轮日期当作全体来源成功核查日期；Reddit候选继续待追。EC01、EC02、EC11补官方方法链接，同时保留旧Image 2原模板固定提交出处，仍是面向2.5适配而非本库实测。

### 2026-10-01成片补强批核查

2026-10-01成片补强批再次读取官方2.5章节、Simon的9月8日原文及BrushGlow指南；只使用参考职责、单变量与保留项的提示方法，不新增作者测试或质量结论。四个已跟踪GitHub仓库HEAD与本日上批记录一致；没有完整回扫作者全部文章，Reddit等候选状态不变。具体版本及修订卡见[本批记录](../maintenance/reviews/2026-10-01-production-expansion-batch-01.md)。

### 2026-10-01编辑与一致性批核查

2026-10-01编辑与一致性批再次读取OpenAI的2.5编辑段、Simon的9月8日原文和BrushGlow原指南；本轮只核对编辑范围、参考职责与保留边界，未全量回扫作者文章，未新增作者案例或测试结论。见[本批记录](../maintenance/reviews/2026-10-01-editing-consistency-batch-01.md)。

## 2026-09-10新增作者

- [Practical_Low29原帖](https://www.reddit.com/r/aigamedev/comments/1wbmvnm/gpt_image_25_nailed_a_16_frame_combat_sprite_sheet/)：有完整一行提示词，作者自述Atlas Cloud上的2.5，具体子型号未知；已整理[C008](../cases/C008-combat-sprite-sheet.md)，后续追动作连贯、切图与实际型号记录。

### 2026-10-02成片批定向核查

公开搜索覆盖Simon的2.5文章线索和BrushGlow编辑／一致性指南，并读取Simon当前主页及BrushGlow原指南相关段落。没有本批值得新增的完整独立案例；未全面回扫全部文章或Reddit，候选不变。官方2.5参考职责与文字原则用于EC05、EC14、EC31修订，不把第三方质量或测试结论计入本库结果。见[本批记录](../maintenance/reviews/2026-10-02-production-expansion-batch-02.md)。

## EvoLink持续跟进

### 2026-10-03缺图分支批定向核查

读取官方2.5参考职责与局部编辑段、BrushGlow指南以及Simon的[9月9日.blend查看器文章](https://simonwillison.net/2026/Sep/9/blender-viewer/)。Simon文章有单行图像提示词但主要是图像转Blender工具展示，与本批尺寸／缺图机制无关，本批不转化、不复制图像、不扩成平台功能；不宣称该线索不存在或已全量收齐作者文章。BrushGlow署名测试仍属第三方自述，不计本库结果。上游awesome新增提交仅涉及防盗链／缓存；定向来源与筛选见[维护记录](../maintenance/reviews/2026-10-03-missing-input-branches-and-layouts.md)。

[EvoLink新版案例数据](https://github.com/EvoLinkAI/gpt-image-2.5-for-e-commerce/blob/main/data/gpt-image-2.5-cases.json)：2026-09-10核查三个作者提供的2.5案例，已整理C009–C011。下轮优先比较此数据文件；旧30章与41段保留提示词作为旧创意，不能因仓库更名就归为新版输出。
