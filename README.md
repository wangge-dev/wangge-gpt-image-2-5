# wangge-gpt-image-2-5

**旺哥的 Image 2.5 中文提示词库：找到想做的图，替换变量，整段复制。**

独立整理，以 OpenAI GPT Image 2.5 为目标，对照官方说明改写创意与电商提示词。保留原作者的创意和出处，补齐中文使用方式、参考图分工、准确文案与连续修改指令。

**首批内容：77 张适配卡 + 9 条原创提示词；其中 25 套电商场景含 88 个完整变体。** 另有 5 张官方／作者来源补充卡。变体和来源卡不重复计入提示词数量。

> 当前是“文档适配完成、未生图实测”。参考图来自旧案例，并逐张标明；不把旧图当 Image 2.5 输出。适配不等于模型独有，具体方法见[改写说明](guides/adaptation.md)。

## 直接找提示词

| 想做什么 | 入口 |
| --- | --- |
| 商品主图、场景、详情、促销、品牌图 | [电商专区 · 25 套场景](ecommerce/README.md) |
| 海报、信息图、人物、品牌、空间、UI | [通用模板 · 22 套](prompts/README.md#通用模板--22) |
| 发型目录、微缩广告、珐琅徽章等创意 | [精选画廊 · 30 条](gallery/README.md) |
| 改字、返工、跨境、一品多图 | [原创提示词 · 9 条](experiments/README.md) |
| 一款商品连续出一套素材 | [电商组合任务单](ecommerce/product-kit.md) |
| 浏览全部适配卡 | [完整索引](prompts/README.md) |

## 先看几个方向

以下缩略图均为 **原库旧版参考，不是本库 2.5 实测图**。点击标题查看完整改写提示词及原作者链接。

| [十二款发型](prompts/gallery/G05.md) | [旅行珐琅徽章](prompts/gallery/G21.md) | [薄荷玫瑰香水](prompts/gallery/G23.md) |
| --- | --- | --- |
| ![旧版发型参考](https://raw.githubusercontent.com/wangge-dev/awesome-gpt-image-2/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/data/images/case535.jpg) | ![旧版徽章参考](https://raw.githubusercontent.com/wangge-dev/awesome-gpt-image-2/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/data/images/case543.jpg) | ![旧版香水参考](https://raw.githubusercontent.com/wangge-dev/awesome-gpt-image-2/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/data/images/case519.jpg) |

## 怎么用

1. 打开卡片，按“准备材料”上传对应图片。
2. 将 `{{变量}}` 替换成自己的信息；表格里的商品数据只是填写示例。
3. 在实际工具中选择 Image 2.5，复制“完整提示词”或一个完整变体。
4. 需要返工时，带上上一轮结果与原始参考，使用卡片里的修改指令。

模型与画布设置见[使用说明](guides/models.md)。不用 API 也可以在支持相应模型的图像界面里使用正文；界面提供哪些设置以实际工具为准。

## 电商是长期特色

[白底主图](prompts/ecommerce/EC01.md) · [生活场景](prompts/ecommerce/EC02.md) · [中文促销](prompts/ecommerce/EC05.md) · [卖点详情](prompts/ecommerce/EC11.md) · [尺寸步骤](prompts/ecommerce/EC13.md) · [多角度](prompts/ecommerce/EC19.md) · [四季系列](prompts/ecommerce/EC21.md)

重点处理商品外观、准确文案、一品多图与连续修改。新玩法资料少时保留待补充项，不拿编造的功效、结构或评价凑内容。

## 持续更新与来源

发现新提示词 → 核对原文和版本 → 去重与对照改写 → 补充完整卡片 → 修订索引与来源记录。

- [维护流程](maintenance/README.md) · [自动更新状态](maintenance/automation.md) · [待补充清单](discovery/backlog.md)
- [两个来源库的全量索引盘点](sources/README.md)：541 个案例、22 个模板索引项、25 个电商模板分别记录处理状态；索引不冒充改写完成。
- [更新记录](CHANGELOG.md) · [贡献方式](CONTRIBUTING.md) · [署名与许可](ATTRIBUTIONS.md)
- [官方与作者的 2.5 来源补充](cases/README.md)

本项目由 wangge-dev 维护，与 OpenAI 无隶属关系。
