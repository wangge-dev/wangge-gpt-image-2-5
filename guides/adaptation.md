# Image 2 → Image 2.5：怎样对照改写

核查日期：2026-09-09。目标为 GPT Image 2.5 Flare / Sunburst。

官方指南允许沿用清楚的既有提示词，并不存在加模型名就生效的专用语法。指定参考图职责、准确文字、编辑时的改变与保留范围，以及逐次修改，是本库采用的指导方向。来源：[GPT Image 2.5 提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)。

以下是本库据此制定的编辑方法，不是官方逐条认证：

| 原提示词情况 | 本库处理 | 例子 |
| --- | --- | --- |
| 商品参考与风格冲突 | 商品服从原图，布景独立描述 | [香水](../prompts/gallery/G23.md) |
| 多张图职责不清 | 明确哪张管人物、商品、布局 | [模特展示](../prompts/ecommerce/EC08.md) |
| 只写“文字清晰” | 给准确文本、位置与次数 | [促销](../prompts/ecommerce/EC05.md) |
| “8K”代替参数 | 正文与画布设置分开 | [模型说明](models.md) |
| 猜测数据或背面 | 要求对应真实资料 | [多角度](../prompts/ecommerce/EC19.md) |
| 要求报告或视频 | 转成单页或静态分镜 | [分镜](../prompts/gallery/G27.md) |
| 要求像素不变 | 不作像素保证，必要时外部合成 | [回忆卡](../prompts/gallery/G09.md) |

“按2.5文档适配”表示审阅原文、处理具体冲突并补齐用法，不表示只有2.5能用，也不表示实测完成。旧图只展示原始创意。原文对应见[盘点](../sources/README.md)，内容检查见[改写记录](../maintenance/reviews/2026-09-09-adaptation.md)。
