# C009 · 实拍商品换场景

[一品三用专题](../ecommerce/evolink-product-story.md) · [来源提示词](README.md)

## 准备材料

上传一张商品完整、标签清楚的实拍照片；场景示例使用浴室台面，适合护肤品。其他商品请修改模板中的场景。

## 拿来就用的具体示例

```text
编辑上传的护肤品实拍照片，只将商品周围环境换为干净的浅色浴室台面，远处是一条折叠白毛巾。保持商品原来的形状、比例、包装颜色、瓶盖、标志、标签文字和可见材质。商品位置和拍摄角度沿用原图；让新场景的光照与接触阴影自然协调。不要重新设计、改字、复制商品，也不要用道具遮住标签。输出一张图片。
```

## 完整中文提示词

```text
编辑图1商品实拍照，仅将周围场景替换为{{场景描述}}。保持商品的外形、比例、实际包装颜色、瓶盖、标志、标签文字、材质与可见细节，不把商品改成来源示例中的黄色。沿用原商品机位和完整轮廓，使环境光、反光及接触阴影自然一致。不要重新设计、换标签、复制商品或让道具遮挡商品。输出一张图片。
```

场景描述：例如“浅木桌面，背景是虚化绿植，左侧柔和窗光”；按商品用途填写。

## 接着修改

上传上一轮结果，并保留原商品参考；每次只改一个问题。

```text
只修正{{具体位置}}的{{偏差}}，恢复为原商品照片对应的外观。保留已经完成的背景与构图，不修改其他区域。
```

## 输入与结果

以下是EvoLink提供的原案例图片；本库中文正文经过改写，图片不表示该中文正文的实测结果。

![EvoLink输入图](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/1fce6dd6ef96719f1df31ca877454dcb01faa9c258f58196a35b5bffb3d82743.png)

EvoLink输入图

![EvoLink场景结果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/bbe9236ef819e9d482d893771869c8e74f3f5f5bb1e3481dd5f5f620eb60988d.png)

EvoLink场景结果 1

![EvoLink场景结果 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/aaa7d06817e79603fccbd4b219485e4cd596d50b2a5656adb6972da61b59b42b.png)

EvoLink场景结果 2

![EvoLink场景结果 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/efeef5411f7748670a6a2ae6189a16f9ff0ee54618813a1a5333d94d1cf8e1b2.png)

EvoLink场景结果 3

![EvoLink场景结果 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/6009fe4530420b44da15762282751ccfcc5086e3b6e329761c8b655bc67edbbe.png)

EvoLink场景结果 4

![EvoLink场景结果 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/gpt-image-2-for-e-commerce/.codex/gpt-image-2.5-migration/media/c757a80035c30c48246e098a9b561aa1f210e513a2271ad91a7e36f3db876e6c.png)

EvoLink场景结果 5

## 来源与关联

[EvoLink原案例](https://github.com/EvoLinkAI/gpt-image-2.5-for-e-commerce/blob/963b1f40bfbe5ff81f0c9684587face6a500bc9a/README_zh-CN.md#gpt-image-25-case-1) · [案例数据](https://github.com/EvoLinkAI/gpt-image-2.5-for-e-commerce/blob/963b1f40bfbe5ff81f0c9684587face6a500bc9a/data/gpt-image-2.5-cases.json)。来源日期2026-09-09，核查2026-09-10。作者将这组自制案例标为GPT Image 2.5，未逐图列出可独立核验的Flare／Sunburst记录；本库保留该归属，不推测子型号。

中文改写：wangge-dev；原提示词与来源图片：EvoLinkAI，依[CC BY 4.0声明](https://github.com/EvoLinkAI/gpt-image-2.5-for-e-commerce/blob/963b1f40bfbe5ff81f0c9684587face6a500bc9a/LICENSE)署名引用。改写补充了输入职责、准确文案、单张输出与局部修改要求。

相关已有用法：[生活场景模板](../prompts/ecommerce/EC02.md) · [同一商品换场景](../experiments/E001-product-scene.md)。
