# 2026-09-19 定时维护

## 来源核查

- OpenAI 官方[图像提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)仍是本轮关于主体、构图、参考图职责、编辑保留项和逐项返工的主要依据。
- `freestylefly/awesome-gpt-image-2`：`0dc09c46c8a30b1fdd89c18cc78a894dac2104e3`，最新变更仍为赞助内容。
- `wangge-dev/awesome-gpt-image-2`：`b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`，无可转化的新2.5内容。
- `buluslan/gpt-image2-ecommerce`：更新到`73abd50bf2b689b5a453f28ddd7b0016415deec6`，本次只恢复作者署名、版本号和简介，没有新增提示词；模板正文仍按原提交追溯。
- `EvoLinkAI/gpt-image-2.5-for-e-commerce`：`963b1f40bfbe5ff81f0c9684587face6a500bc9a`，无可转化的新案例。
- [GPT Image 2.5提示词指南（二次整理）](https://gptimage2-5.art/blog/gpt-image-2-5-prompt-guide)：读取完整页面，取三参考职责、Keep清单和单变量编辑的组织原则；页面自述测试不计入本库实测。

## 本批内容

新增EC53“商品、模特与氛围三参考图职责绑定”、EC54“数码主机、屏幕截图与配件清单一页对应”、T410“同一电商成片单变量返工与保留清单”。

- EC53把商品外观、获准成年模特身份和氛围图的色调/光线/背景拆成三个唯一职责，避免参考图串入人物、商品或文字。
- EC54把数码主机、已校对屏幕和真实配件清单放进一张详情图，屏幕与数量只按输入资料，禁止凭外观补写参数。
- T410把已批准成片的返工限定为一个变量，并列出完整保留清单；无法单变量修改时停止，不把混合修改写成成功。

三条均提供完整正文、无占位符示例、局部返工、真实性边界和来源说明；均标为面向Image 2.5整理、未生图实测。

## 检查

- `python scripts/build_library.py`：519张JSON卡，132个完整变体。
- `python scripts/build_gallery.py`：539条画廊记录。
- `python scripts/check_ecommerce_kits.py`：8套任务包、48步通过。
- `python scripts/check_links.py`：3233个本地Markdown链接通过。
- JSON唯一性、字段完整性、示例无未填写变量、`git diff --check`通过。

当前539条基础提示词、54套电商场景；本批未生图、未付费采集。
