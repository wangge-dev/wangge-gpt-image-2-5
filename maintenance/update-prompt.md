# 可复制的持续填充指令

```text
维护 wangge-dev/wangge-gpt-image-2-5 的中文 Image 2.5 提示词库。先读 AGENTS.md、maintenance/README.md、来源盘点与最近记录。
检查官方2.5说明、awesome-gpt-image-2、gpt-image2-ecommerce 及原作者公开新提示词。追原文和版本，按创意去重。允许旧提示词对照适配，保留署名并说明改变，不把旧图当2.5结果。
优先电商，也补通用创意。完成正文、输入材料、变量示例、完整变体和修改指令；未生图不阻止收录，资料缺失进入待补充清单。
编辑 data/library.json，运行 python scripts/build_library.py。更新来源对应，检查变量、数量、文案冲突、参考图职责与署名，运行 python scripts/check_links.py。审阅差异后只提交本次本仓库文件并正常推送，不覆盖用户修改、不强推。
记录来源访问成功与失败、实际新增或修订、检查与同步结果。无实质变化不凑更新，不自动收费生图。重要新增、事实修订、失败或需用户输入时通知。
```


## awesome-gpt-image-2 双源追踪

分别检查[原作者仓库](https://github.com/freestylefly/awesome-gpt-image-2)与[个人 fork](https://github.com/wangge-dev/awesome-gpt-image-2)的最新提交。各自记录上次成功核查的提交；fork未同步不代表上游无更新。以原作者案例链接和案例编号去重，同一创意只修订已有卡片。上游展示标签不能替代实际模型记录。2026-09-10原作者已核查至073d105d4dbb3f3afcd2e7cd194cee3a557b0999；fork此前核查至b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4，下轮重新读取远端。
