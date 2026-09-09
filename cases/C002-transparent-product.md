# C002 · 透明背景商品素材

[来源明确的提示词](README.md) · [首页](../README.md)

## 准备材料

上传一张轮廓完整的商品照片。

将双花括号内容换成自己的信息，然后整段复制。

## 完整中文提示词

```text
将照片中的商品单独提取到透明背景，居中完整展示。商品轮廓、颜色、材质和标签保持，不添加投影、底板或棋盘格，输出PNG图片。
```

## 接着修改

上传上一轮结果，涉及参考图的任务同时保留原图；每次只发一条修改指令。

```text
只清理商品{{边缘部位}}的残留底色，保留商品及透明背景，不重新设计标签。
```

## 使用提示

API设置background=transparent、output_format=png。下载原始PNG检查透明通道；截图或画出的棋盘格不能当透明素材。

画布沿用输入图比例；模型与可用设置见[模型说明](../guides/models.md)。

## 来源

[官方2.5示例 · Flare / Sunburst](https://developers.openai.com/api/docs/guides/image-prompting#create-a-transparent-product-cutout)。核查日期：2026-09-09。中文正文为本库根据该任务整理，加入适用的输入和操作要求，不是官方逐字译文。

相关任务：[商品主图](../prompts/ecommerce/EC01.md) · [一品多图](../ecommerce/product-kit.md)
