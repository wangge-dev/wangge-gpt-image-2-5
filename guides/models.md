# 模型与版本说明

核查日期：2026-09-09。API 型号、ChatGPT 界面名称与调用平台分别记录。

| 名称 | 已核实的定位 | 本库记录方式 |
| --- | --- | --- |
| GPT Image 2.5 Flare | 面向快速、日常高质量生成 | `gpt-image-2.5-flare`，另记返回的版本信息 |
| GPT Image 2.5 Sunburst | 重视生成与编辑精度 | `gpt-image-2.5-sunburst`，另记返回的版本信息 |
| ChatGPT Images 2.5 | ChatGPT 图像产品 | 保存可见版本依据；不能擅自推断为 Flare 或 Sunburst |

来源：[Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) · [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)。

官方发布于 2026-09-08，涉及主体保真、编辑一致性与速度改进；Sketch、模板和图片评论属于产品操作体验，不能等同为 API 参数。来源：[发布说明](https://openai.com/index/introducing-chatgpt-images-2-5/)。

## 开始一个实验

1. 选一条 [实验提示词](../experiments/README.md)，准备自己可使用的输入素材。
2. 在实际平台选择目标型号。无法确认时写“版本未确认”，先留在实验区。
3. 记录请求中实际选择的尺寸、质量、格式、输入图和模型；不要让提示词中的“4K”代替请求参数。
4. 保存原始输出，再判断是否需要修改。挑出最佳结果时也记录总尝试次数。
5. 以 [实验记录模板](../experiments/record-template.md) 保存结果。

本库首版未执行 API 请求，不提供经过运行验证的 API 示例。API 接入时以当天官方文档为准。费用以真实使用量记录，不用旧版每张价格估算新版费用。

## 选择实验对象：本库的建议

普通创意先试 Flare；对商品或局部编辑要求高的任务优先评估 Sunburst。
比较二者时保持输入、提示词和可共用的请求设置一致。相同质量档位不等于相同输出质量。
有需要才比较，失败可以改提示词或任务设计，不必机械提高档位。

[返回首页](../README.md)
