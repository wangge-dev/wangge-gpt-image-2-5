# 持续追踪来源

维护核查日期：2026-09-09。来源优先级依据具体证据，不依据转发数量。

| ID | 来源 | 用途 | 本轮状态 |
| --- | --- | --- | --- |
| S01 | [OpenAI 发布](https://openai.com/index/introducing-chatgpt-images-2-5/) | 发布事实、产品功能 | 正文已核查 |
| S02 | [官方提示词指南](https://developers.openai.com/api/docs/guides/image-prompting) | 必须定位 GPT Image 2.5 章节 | 章节与示例标签已核查 |
| S03 | [Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) | 型号与调用能力 | 正文已核查 |
| S04 | [Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) | 型号与调用能力 | 正文已核查 |
| S05 | [Simon 的 2.5 记录](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) | 原作者示例与后续线索 | 正文、指令、型号已核查 |
| S06 | [TechRadar 上手](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-images-2-5-is-out-ive-been-testing-it-for-24-hours-and-these-are-the-3-new-features-youll-actually-use) | ChatGPT 操作体验 | 正文已核查，不用于 API 型号证明 |
| S07 | [YouMind](https://youmind.com/zh-CN/gpt-image-2-prompts) | 发现创作者与原帖 | 规划期发现候选，正式条目待追溯 |
| S08 | [Promptowy 编辑实验](https://promptowy.com/edycja-komentarzem-test/) | 观察实验记录方法 | 规划期核查：作者不能确认模型，不作为 2.5 效果证据 |
| S09 | [awesome-gpt-image-2](https://github.com/wangge-dev/awesome-gpt-image-2) | 旧提示词创意与通用模板适配 | 已盘点541案例与22模板索引；已改写部分见来源盘点 |
| S10 | [gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) | 电商场景与变体适配 | 25模板与88变体方向已处理，持续检查新增文件 |

新增[作者后续追踪](author-watch.md)，明确2.5来源优先，旧创意适配单独记录。

## 滚动检索

每轮查询日期窗口覆盖上次成功检索之后，并重叠 2 天；失败来源保留上次成功时间。
第一轮从 2026-09-08 起搜。搜索日期只帮助定位，最终核对原帖时间和模型。

- `"gpt-image-2.5-sunburst" "product"`
- `"gpt-image-2.5-flare" "editing"`
- `"ChatGPT Images 2.5" "prompt"`
- `"Image 2.5" 商品 保真`
- `"Image 2.5" 中文 改字`
- `"gpt-image-2.5" packaging multi-turn`

轮换扩展词：garment、jewelry、glass、label、infographic、sketch、poster、comparison、failure。
渠道：官方文档、作者网站、GitHub、X、Reddit、公开中文文章。先查公开入口，不自动启用付费采集接口。

发现一条有价值原帖后，追作者的后续与回复，分清独立案例和同案转载。检索结果不全时保留覆盖范围，不宣称全网收齐。

[候选清单](backlog.md) · [维护流程](../maintenance/README.md)


## awesome-gpt-image-2 双源追踪

分别检查[原作者仓库](https://github.com/freestylefly/awesome-gpt-image-2)与[个人 fork](https://github.com/wangge-dev/awesome-gpt-image-2)的最新提交。各自记录上次成功核查的提交；fork未同步不代表上游无更新。以原作者案例链接和案例编号去重，同一创意只修订已有卡片。上游展示标签不能替代实际模型记录。2026-09-10原作者已核查至073d105d4dbb3f3afcd2e7cd194cee3a557b0999；fork此前核查至b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4，下轮重新读取远端。
