# C002 · 透明背景商品素材

[来源明确的提示词](README.md) · [首页](../README.md)

## 准备材料

上传一张轮廓完整的商品照片。

本卡首轮正文无需填写变量；按上述要求上传图片即可直接复制。后续修改时再填写具体问题。

## 完整中文提示词

```text
将照片中的商品完整提取到真正透明的背景上，居中展示，四周留出均匀安全边距。精确保留商品几何比例、颜色、材质、标签文字、透明或半透明部位以及原有边缘细节。轮廓清晰，无白边、黑边、残留底色或毛边；只做轻微清理，不重新设计商品。不要添加纯色底、棋盘格、场景、投影、底板、文字或水印。输出带真实 Alpha 通道的 PNG 或 WebP。
```

## 接着修改

上传上一轮结果，涉及参考图的任务同时保留原图；每次只发一条修改指令。

```text
只清理商品{{边缘部位}}的{{白边、黑边、残留底色或毛边}}，保留商品其余像素、标签、透明或半透明细节与真实透明背景，不添加阴影，不重新设计商品。
```

## 使用提示

API 设置 `background=transparent`，`output_format=png` 或 `webp`；PNG 不设置 `output_compression`。下载原始文件并检查是否真实包含 Alpha 通道，截图、白底图或画出的棋盘格都不能当透明素材。玻璃、毛发、阴影和商品边缘需要分别放到白、黑两种检查底上观察；后续继续编辑时重新写明“保持透明背景”。

画布沿用输入图比例；模型与可用设置见[模型说明](../guides/models.md)。

## 来源

[官方2.5示例 · Flare / Sunburst](https://developers.openai.com/api/docs/guides/image-prompting#create-a-transparent-product-cutout)；[buluslan 2.5透明抠图场景](https://github.com/buluslan/gpt-image2-ecommerce/blob/main/references/scenarios/transparent-cutout.json)。核查日期：2026-09-28。中文正文为本库根据官方任务整理，并补充边缘返工和 Alpha 验收要求，不是官方逐字译文。本轮只更新提示词与检查方法，未运行生图。

相关任务：[商品主图](../prompts/ecommerce/EC01.md) · [一品多图](../ecommerce/product-kit.md)
