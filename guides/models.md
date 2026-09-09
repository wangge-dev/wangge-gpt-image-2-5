# 模型与版本说明

核查日期：2026-09-09。API 型号、ChatGPT 界面名称与调用平台分别记录。

| 名称 | 已核实的定位 | 本库记录方式 |
| --- | --- | --- |
| GPT Image 2.5 Flare | 面向快速、日常高质量生成 | `gpt-image-2.5-flare`，另记返回的版本信息 |
| GPT Image 2.5 Sunburst | 重视生成与编辑精度 | `gpt-image-2.5-sunburst`，另记返回的版本信息 |
| ChatGPT Images 2.5 | ChatGPT 图像产品 | 保存可见版本依据；不能擅自推断为 Flare 或 Sunburst |

来源：[Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) · [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)。

官方发布于 2026-09-08，涉及主体保真、编辑一致性与速度改进；Sketch、模板和图片评论属于产品操作体验，不能等同为 API 参数。来源：[发布说明](https://openai.com/index/introducing-chatgpt-images-2-5/)。

## 复制提示词开始制作

1. 选一条 [完整提示词](../prompts/README.md)，按卡片准备素材、替换变量。
2. 在实际平台选择目标型号。无法确认时不要把生成结果标为明确的2.5实测。
3. 记录请求中实际选择的尺寸、质量、格式、输入图和模型；不要让提示词中的“4K”代替请求参数。
4. 保存原始输出，再判断是否需要修改。挑出最佳结果时也记录总尝试次数。
5. 以 [实验记录模板](../experiments/record-template.md) 保存结果。

本库首版未执行 API 请求，不提供经过运行验证的 API 示例。API 接入时以当天官方文档为准。费用以真实使用量记录，不用旧版每张价格估算新版费用。

## 参数与画布

两个2.5型号支持 `quality=auto/low/medium/high/xhigh/max`。默认可用 `auto`；卡片画布是本库起步建议，不是必须参数。

| 比例 | 本库使用的尺寸 |
| --- | --- |
| 方形 | `1024x1024` |
| 横版／竖版 | `1536x1024`／`1024x1536` |
| 4:5／3:4 | `1536x1920`／`1152x1536` |
| 16:9／长卷3:1 | `2048x1152`／`3072x1024` |

自定义尺寸两边须为16的倍数，长宽比在1:3至3:1内，单边不超过3840，总像素655,360至8,294,400；超过2560×1440像素面积的分辨率为实验支持。透明图设置 `background=transparent`，格式使用PNG或WebP，白底不等于透明。来源：[官方输出设置](https://developers.openai.com/api/docs/guides/image-generation#size-and-quality-options)。

例如旧提示词的“2000×2500”不符合两边16倍数；“8K”也不能替代实际输出尺寸。卡片仅提供提示词，不提供已运行的API集成保证。

## 选择模型：本库的建议

普通创意先试 Flare；对商品或局部编辑要求高的任务优先评估 Sunburst。
比较二者时保持输入、提示词和可共用的请求设置一致。相同质量档位不等于相同输出质量。
有需要才比较，失败可以改提示词或任务设计，不必机械提高档位。

[返回首页](../README.md)
