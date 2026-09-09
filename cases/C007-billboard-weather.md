# C007 · 商品广告牌与天气修改

[全部来源提示词](README.md) · [首页](../README.md)

## 准备材料

上传商品正面照片。准备一条已经确认的广告短句。下方洗发水图片可用于理解官方案例；自己的商品应使用自己的照片。

## 拿来就用的具体示例

```text
使用上传的洗发水商品照片，制作一张夕阳下高速公路旁广告牌的写实效果图。广告牌展示同一款洗发水，并且只出现一次文案“Fresh and clean”。文字使用清楚的粗体无衬线字体，居中排版，文字和背景对比明显。保留商品外观，不新增水印或其他标志。输出一张完整图片。
```

## 完整中文提示词

```text
图1为商品依据。制作一张{{环境}}中的广告牌写实效果图。广告牌中展示图1的商品，保持商品外形、颜色和原包装。新增广告文案仅为“{{广告短句}}”，出现一次，使用清晰的粗体无衬线字体，居中并留出边距。广告牌透视、现场光线和投影协调，不添加其他宣传语或水印。输出一张图片。
```

变量示例：环境＝夕阳下的高速公路旁；广告短句＝Fresh and clean。广告短句按实际商品填写。

## 接着修改

收到第一轮图片后，上传这张结果再发送：

```text
把这张图改为下雪的冬日傍晚。保持广告牌位置、商品和文案不变，仅调整天气、季节环境与相应光照。
```

## 输入与结果

官方商品输入：

![官方洗发水输入](https://developers.openai.com/images/platform/guides/image-prompting/shampoo.webp)

官方 Sunburst 第一轮：

![夕阳广告牌示例](https://developers.openai.com/images/platform/guides/image-prompting/billboard-gpt-image-2-5-sunburst.webp)

官方 Sunburst 后续编辑：

![冬日广告牌示例](https://developers.openai.com/images/platform/guides/image-prompting/billboard-winter-gpt-image-2-5-sunburst.webp)

## 来源

[OpenAI 提示词指南：Refine an image across turns](https://developers.openai.com/api/docs/guides/image-prompting#refine-an-image-across-turns)，2026-09-09核查。图片为官方原提示词的输出，中文正文为本库整理。两轮分开发送，每轮使用上一步结果。
