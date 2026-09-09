# wangge-gpt-image-2-5

**旺哥的 Image 2.5 玩法与实测库：看来源，拿提示词，留住每次修改的经验。**

专门研究 OpenAI GPT Image 2.5，持续发现新玩法，并长期建设电商实战实验室。中文优先，独立整理；不批量迁移 Image 2 旧库。

> **首版状态 · 2026-09-09**
> 5 张有明确 2.5 来源的案例卡（4 张官方、1 张作者实测）；9 个原创待测试实验（含 6 个电商方向）；本仓库独立生图复现 **0** 次。案例卡是来源研究，不是我们的效果保证。展示图请从各卡片的原始来源查看，暂未转载第三方图片。

## 从这里开始

| 你现在要做什么 | 入口 |
| --- | --- |
| 了解 2.5 与具体模型 | [模型与版本说明](guides/models.md) |
| 找已经有来源依据的玩法 | [案例索引](cases/README.md) |
| 直接拿中文提示词试用 | [原创实验与提示词](experiments/README.md) |
| 做商品图、主图或连续返工 | [电商实战实验室](ecommerce/README.md) |
| 提交新玩法、错误或失败反馈 | [贡献说明](CONTRIBUTING.md) |
| 查看持续更新怎么运行 | [维护流程](maintenance/README.md) |

## 本周先看什么

- [在现有图表中添加角色](cases/C005-chart-character.md)：作者标明 Sunburst，附原图与结果。
- [透明商品素材](cases/C002-transparent-product.md)：官方 2.5 示例；需要区分真实透明与棋盘格画面。
- [一张商品图换场景](experiments/E001-product-scene.md)：原创实验，检查商品是否被改变。
- [中文主图只改日期](experiments/E003-copy-edit.md)：原创实验，检查局部修改是否影响包装。
- [三轮返工能否保留前面的修改](experiments/E005-revision-chain.md)：原创实验，逐轮留证。

## 电商实战实验室 · 长期保留

[商品保真](experiments/E001-product-scene.md) · [主图构图](experiments/E002-main-image.md) · [精确改字](experiments/E003-copy-edit.md) · [一品多图](experiments/E004-product-series.md) · [多轮返工](experiments/E005-revision-chain.md) · [跨境适配](experiments/E006-localization.md)

资料不足时保留任务和缺口。图片可用性、平台审核、点击率与转化率分别记录；没有投放数据时不作增长承诺。

## 我们怎样认定「2.5」

每条内容同时标明 **模型依据** 与 **复现状态**。官方示例、作者实测、个人实验不会混为一谈。
“在 2.5 上有效”不等于“只有 2.5 才能做”；只有同任务版本对比才能支持升级收益。
具体规则见 [来源与证据](guides/evidence.md)。

## 持续更新

新线索 → 核实来源与版本 → 整理候选 → 选择复现 → 收录结果 → 修订旧结论。

- [追踪来源与检索词](discovery/sources.md)
- [候选与缺口](discovery/backlog.md)
- [最近一次核查](maintenance/reviews/2026-09-09.md)
- [内容更新记录](CHANGELOG.md)
- [自动更新运行状态](maintenance/automation.md)

不以条目数量作为目标。没有新资料不凑更新，访问失败不当成没有新资料。新版本未来发布后另作归属，不悄悄替换本库的 2.5 结果。

## 使用与来源

原创实验替换 `{{变量}}` 后再试用；参考图由使用者提供。参数与提示词分开设置，模型选择见模型说明。
[来源与署名](ATTRIBUTIONS.md) · [许可证](LICENSE)

本项目由 wangge-dev 维护，与 OpenAI 无隶属关系。

