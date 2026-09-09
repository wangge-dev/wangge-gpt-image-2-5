# wangge-gpt-image-2-5

简体中文 · [English](README.en.md)

**旺哥的 Image 2.5 中文提示词库：找到想做的图，替换变量，整段复制。**

独立整理，以 OpenAI GPT Image 2.5 为目标，对照官方说明改写创意与电商提示词。保留原作者的创意和出处，补齐中文使用方式、参考图分工、准确文案与连续修改指令。

**99 条基础提示词 · 111 个完整变体 · 电商专区持续扩充。**

包含 78 张适配卡、14 条原创提示词和7条来源明确的中文提示词；30 套电商场景提供86个变体。


[打开可筛选画廊](https://wangge-dev.github.io/wangge-gpt-image-2-5/browse/) · 按任务、品类、参考图与生成示例筛选，展开即可复制。

## 直接找提示词

| 想做什么 | 入口 |
| --- | --- |
| 商品主图、场景、详情、促销、品牌图 | [电商专区 · 30 套场景](ecommerce/README.md) |
| 海报、信息图、人物、品牌、空间、UI | [通用模板 · 22 套](prompts/README.md#通用模板--22) |
| 发型目录、微缩广告、珐琅徽章等创意 | [精选画廊 · 31 条](gallery/README.md) |
| 改字、返工、跨境、一品多图 | [原创提示词 · 9 条](experiments/README.md) |
| 一款商品连续出一套素材 | [电商组合任务单](ecommerce/product-kit.md) |
| 换装、透明商品、换语言、草图与图表编辑 | [明确2.5来源 · 7条完整提示词](cases/README.md) |
| 浏览全部适配卡 | [完整索引](prompts/README.md) |

## 先看几个方向

点击标题查看提示词，或打开[网页版三组示例](guides/web-examples.md)。下方为 wangge-dev 使用 ChatGPT 网页版生成的示例。

| [十二款发型](prompts/gallery/G05.md) | [旅行珐琅徽章](prompts/gallery/G21.md) | [薄荷玫瑰香水](prompts/gallery/G23.md) |
| --- | --- | --- |
| ![发型生成示例](assets/results/G05.png) | ![徽章生成示例](assets/results/G21.png) | ![香水生成示例](assets/results/G23.png) |

## 怎么用

1. 打开卡片，按“准备材料”上传对应图片。
2. 将 `{{变量}}` 替换成自己的信息；表格里的商品数据只是填写示例。
3. 在实际工具中选择 Image 2.5，复制“完整提示词”或一个完整变体。
4. 需要返工时，带上上一轮结果与原始参考，使用卡片里的修改指令。

模型与画布设置见[使用说明](guides/models.md)。不用 API 也可以在支持相应模型的图像界面里使用正文；界面提供哪些设置以实际工具为准。

## 电商是长期特色

[白底主图](prompts/ecommerce/EC01.md) · [生活场景](prompts/ecommerce/EC02.md) · [中文促销](prompts/ecommerce/EC05.md) · [卖点详情](prompts/ecommerce/EC11.md) · [尺寸步骤](prompts/ecommerce/EC13.md) · [多角度](prompts/ecommerce/EC19.md) · [四季系列](prompts/ecommerce/EC21.md)

重点处理商品外观、准确文案、一品多图与连续修改。持续补充新品类、新构图与实用的编辑方法。

## 持续更新与来源

持续收集创意和电商用法，补充新提示词、场景变体与编辑技巧。

- [参考来源](sources/README.md)
- [更新记录](CHANGELOG.md) · [贡献方式](CONTRIBUTING.md) · [署名与许可](ATTRIBUTIONS.md)
- [官方与作者来源的完整中文提示词](cases/README.md)

本项目由 wangge-dev 维护，与 OpenAI 无隶属关系。
