# C006 · 移除手中物品

[全部来源提示词](README.md) · [首页](../README.md)

## 准备材料

上传一张人物手持物品的照片。物品和手部边缘要清楚；准备局部保留要求。

## 拿来就用的具体示例

适用于下方官方手持花朵的人物输入图。

```text
移除男子手中的花朵，保持男子本人、衣着、姿势与周围画面不变。输出一张编辑后的照片。
```

## 完整中文提示词

```text
从上传照片中移除{{待移除物品}}。只修补该物品占据的区域，使其与周围背景和可见手部自然衔接。保留人物身份、面部表情、衣服、姿势、构图和光线，不新增替代物品。输出一张编辑后的照片。
```

## 接着修改

```text
只清理{{残留位置}}的物品残影，保留已经正确的手部、人物与背景。
```

## 输入与结果

官方输入：

![手持花朵的男子](https://developers.openai.com/images/platform/guides/image-prompting/man-with-blue-hat.webp)

官方 Sunburst 示例：

![移除花朵后的官方示例](https://developers.openai.com/images/platform/guides/image-prompting/man-with-no-flower-gpt-image-2-5-sunburst.webp)

## 来源

[OpenAI 提示词指南：Remove an object](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object)，2026-09-09核查。图片为官方原提示词的示例；中文变量模板为本库扩写。若遮挡区域需要准确还原，另提供无遮挡照片。
