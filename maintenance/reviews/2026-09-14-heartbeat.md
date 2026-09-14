# 2026-09-14 定时维护

## 来源核查

- OpenAI GPT Image 2.5提示词指南可访问，继续支持参考图职责、文字控制和局部编辑的整理方法。
- `freestylefly/awesome-gpt-image-2` 仍为 `0dc09c46c8a30b1fdd89c18cc78a894dac2104e3`，最新变更仅为赞助内容。
- `wangge-dev/awesome-gpt-image-2` 仍为 `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`。
- `buluslan/gpt-image2-ecommerce` 仍为 `a3673fb6f316664280e6abd90a60a578c6fb2228`。
- `EvoLinkAI/gpt-image-2.5-for-e-commerce` 仍为 `963b1f40bfbe5ff81f0c9684587face6a500bc9a`。

## 本批内容

新增EC49–EC52，覆盖搜索缩略图主图、详情首屏、单商品换背景和活动主视觉。它们按最新路线纠偏，优先主体占比、留白、安全区、阅读动线和信息层级；与EC01、EC05、EC31的差异分别是缩略图安全区、首屏单利益点动线和四层固定排版，EC51新增背景白名单与高风险商品保护区。

当前516张JSON卡、536条基础提示词、132个完整变体、52套电商场景。未调用生图。

## 检查

- `build_library.py`、`build_gallery.py`完成。
- 八套任务包48步通过。
- 3216个本地Markdown链接通过。
- `git diff --check`通过。
