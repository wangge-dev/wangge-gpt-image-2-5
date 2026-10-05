# 两个来源库的盘点与改写对应

## 2026-10-05成片、系列一致性与目录拼贴来源复核

重读buluslan固定提交`a3673fb6f316664280e6abd90a60a578c6fb2228`的[03俯拍模板](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/03-flat-lay.json)与[10包装模板](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/10-packaging.json)，以及awesome固定版本中G25对应的Case485正文与作者署名。保留EC03／EC10六个原变体键、三张适配卡原source_key和出处；旧创意仅标面向2.5适配，不将旧图当本轮结果。EC32保持本库原创，新增首张无母版完整分支；G25新增单照片目录完整分支。

四仓HEAD与10-03记录一致：freestylefly `65a9c57a1968a13f2f1997c58409cac9aa146bc7`，fork `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`，buluslan `73abd50bf2b689b5a453f28ddd7b0016415deec6`，EvoLink `963b1f40bfbe5ff81f0c9684587face6a500bc9a`。来源盘点541／35／506不变；基础词548、完整变体141（电商93个）。本轮没有新增来源图片或许可范围；40条预览及原归属不变。

方法依据为[官方提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)的参考职责、布局和编辑边界。定向读取Simon当前主页及BrushGlow指南的参考分工／局部返工段，没有转化独立新案例；不宣称作者全量检索或原作者X帖已直接可读。详见[维护记录](../maintenance/reviews/2026-10-05-production-consistency-catalog.md)。

## 2026-10-03缺图分支与构图示意来源复核

重读buluslan固定提交`a3673fb6f316664280e6abd90a60a578c6fb2228`的[13尺寸模板](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/13-size-spec.json)与[19网格模板](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/19-multi-angle-grid.json)。保留署名、source_key与六个来源变体键；尺寸冲突属于本库填写示例，不归责原模板。新增单图尺寸、单图可见外观两个本库变体，仍标旧创意面向2.5适配、未生图实测。官方[提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)的构图、参考分工与单点修改原则用于修订，不是能力或实测保证。

四仓HEAD本轮实读：freestylefly `65a9c57a1968a13f2f1997c58409cac9aa146bc7`（相较上次3个提交仅修改middleware.ts和vercel.json的防盗链／缓存，无提示词文件变化），fork `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`，buluslan `73abd50bf2b689b5a453f28ddd7b0016415deec6`，EvoLink `963b1f40bfbe5ff81f0c9684587face6a500bc9a`。未追账号、支付或平台部署功能。来源盘点541／35／506不变，基础词548、完整变体139（电商92个）。

为EC49、EC50、EC52新增[本库原创SVG示意](../assets/layouts/README.md)，适用根目录MIT许可，不使用第三方图片；画廊有预览条目37→40，三张标为构图示意而非实测。其余图片归属不变，未下载、生成或付费采集新图。作者定向跟进与候选不转化原因见[本批记录](../maintenance/reviews/2026-10-03-missing-input-branches-and-layouts.md)。

## 2026-10-02高频成片补强批来源复核

逐项重读buluslan固定提交`a3673fb6f316664280e6abd90a60a578c6fb2228`的05促销与14套装JSON；EC05／EC14保留原署名、source_key及七个来源变体键，不增加旧库改写数量。EC31仍为本库原创，新增细节近照／商品定位完整变体；当前548条基础提示词、137个完整变体（电商90个）。方法依据为[官方GPT Image 2.5章节](https://developers.openai.com/api/docs/guides/image-prompting)的参考职责、准确文字和成品布局，旧模板只标面向2.5适配，不算本库实测。

2026-10-02读取四仓远端HEAD，与10-01记录一致：freestylefly `b93c18ad45397c828fcc39a1ed347830433b3de4`、个人fork `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`、buluslan `73abd50bf2b689b5a453f28ddd7b0016415deec6`、EvoLink `963b1f40bfbe5ff81f0c9684587face6a500bc9a`。来源盘点541／35／506、37张预览与证据归属不变，未采集新图片。作者滚动检索与主页／指南复核未带来本批独立新案例，不宣称全网或作者全文已收齐。

## 2026-10-01编辑与一致性批来源复核

T26、T30、T343、EC51保留原创身份与source_key，只借用旧库的共同网格／品牌色机制，不新增旧库精选数。重读[OpenAI提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)的2.5编辑、参考职责、尺寸与保留边界；Simon的9月8日原文和BrushGlow指南仍可读，不全量回扫作者文章，不采纳其质量／测试结论。四个来源仓库HEAD与下方上批记录一致。

新增只去商品偏色和局部光学适配两个完整变体；总量548条基础提示词、136个完整变体，电商89个。来源CSV的541／35／506口径、37张预览及来源归属不变；没有生图或采集新图片。

## 2026-10-01成片补强批来源复核

EC49、EC50、EC52、T410与EC12完成实质修订；方法依据为[官方GPT Image 2.5章节](https://developers.openai.com/api/docs/guides/image-prompting)的构图、参考职责、一次一变量与保护区域限制。EC12另逐项重读buluslan固定提交`a3673fb6f316664280e6abd90a60a578c6fb2228`的12号模板，保留三种原变体键与署名，只将泛化风格词重构为空间机制和商品事实边界；旧Image 2模板不当作2.5实测。

本轮读取远端HEAD：freestylefly `b93c18ad45397c828fcc39a1ed347830433b3de4`、个人fork `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`、buluslan `73abd50bf2b689b5a453f28ddd7b0016415deec6`、EvoLink `963b1f40bfbe5ff81f0c9684587face6a500bc9a`。Simon的9月8日原文和BrushGlow的9月11日指南仍可读；本批不新增作者输出案例或复制第三方图片，旧库CSV的541／35／506口径不变。两个新增变体是本库资料降级方案，不新增旧库精选数。

## 2026-10-01定向复核与实质修订

本批逐项重读buluslan固定提交`a3673fb6f316664280e6abd90a60a578c6fb2228`的01主图、02场景和11信息图JSON，并核对[OpenAI图像提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)的参考职责、保留项和单变量编辑原则。EC01、EC02、EC11及11个完整变体已修订；原来源署名和source_key不变，不增加旧库已改写数量，不把原Image 2模板或未运行中文稿说成2.5实测。

远端HEAD已读取：buluslan`73abd50bf2b689b5a453f28ddd7b0016415deec6`、freestylefly`b93c18ad45397c828fcc39a1ed347830433b3de4`、wangge-dev fork`b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`。三个公开主页可读；上游2.5专区仍明确说明精确工具型号未核实，不当作本库输出。本轮只是定向复核，不代表已精读全部新增提交。旧库存量盘点和CSV保持原口径。

[首页](../README.md) · [完整CSV](inventory.csv)

盘点日期：2026-09-09。覆盖源库结构化案例索引、模板索引与电商模板文件。全量索引不等于全量逐条精读或全量改写。

| 来源范围 | 索引项 | 已改写 | 后续精选 |
| --- | ---: | ---: | ---: |
| 旧库案例 | 541 | 35 | 506 |
| 旧库模板索引 | 22 | 22 | 0 |
| 电商模板 | 25 | 25 | 0 |

来源版本：awesome `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`；ecommerce 当前 `73abd50bf2b689b5a453f28ddd7b0016415deec6`（本轮仅恢复作者署名与版本号，模板正文仍以 `a3673fb6f316664280e6abd90a60a578c6fb2228` 链接追溯）。版本用于追溯原文，不限制未来更新。

案例索引541项，编号1至544，缺12、169、170。模板JSON有22项；其Markdown正文还有未独立进入JSON的签名、品牌人格等扩展，列入待补充，不宣传为全文所有模板均已迁移。电商25个文件中的88个变体方向均已处理，其中2个重复方向合并到基础正文，提供86个来源变体；另有本库新增的7个变体（无利益点首屏、无价格活动、局部光学适配、细节证据模块、单图尺寸、单图可见外观、首张无母版活动），当前电商合计93个。

## 已改写条目

| 原条目 | 适配卡 |
| --- | --- |
| [544 幼儿词汇拆解学习卡](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-544) | [G07.md](../prompts/gallery/G07.md) |
| [543 旅行纪念珐琅徽章](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-543) | [G21.md](../prompts/gallery/G21.md) |
| [542 黑白排版侧脸肖像海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-542) | [G19.md](../prompts/gallery/G19.md) |
| [541 50/50 混合媒介回忆卡](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-541) | [G09.md](../prompts/gallery/G09.md) |
| [536 春日樱花回眸电影人像](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-536) | [G17.md](../prompts/gallery/G17.md) |
| [535 同一人脸十二款发型 Lookbook](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-535) | [G05.md](../prompts/gallery/G05.md) |
| [532 六宫格柠檬饮料微缩广告](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-532) | [G22.md](../prompts/gallery/G22.md) |
| [531 水晶框国家旅行广告海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-531) | [G20.md](../prompts/gallery/G20.md) |
| [525 酒红棚拍男士时尚肖像](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-525) | [G18.md](../prompts/gallery/G18.md) |
| [523 曼哈顿公园水彩旅行插画](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-523) | [G13.md](../prompts/gallery/G13.md) |
| [522 儿童故事书手绘头像](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-522) | [G06.md](../prompts/gallery/G06.md) |
| [520 月面宇航员 T 恤图形](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-520) | [G14.md](../prompts/gallery/G14.md) |
| [519 薄荷玫瑰香水电商图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-519) | [G23.md](../prompts/gallery/G23.md) |
| [517 杯内鱼眼夏日冰饮广告](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-517) | [G24.md](../prompts/gallery/G24.md) |
| [510 Bichon Shop 拟物 App 图标](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-510) | [G03.md](../prompts/gallery/G03.md) |
| [496 水雕品牌 Logo 六宫格](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-496) | [G04.md](../prompts/gallery/G04.md) |
| [494 电动巴士工程信息图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-494) | [G08.md](../prompts/gallery/G08.md) |
| [489 城市地图微缩旅行海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-489) | [G01.md](../prompts/gallery/G01.md) |
| [487 法式药妆商业分镜封面](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-487) | [G27.md](../prompts/gallery/G27.md) |
| [485 时尚目录电商拼贴](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-485) | [G25.md](../prompts/gallery/G25.md) |
| [475 企鹅造型包装结构板](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-475) | [G26.md](../prompts/gallery/G26.md) |
| [470 本地生活小店异形展架](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-470) | [G31.md](../prompts/gallery/G31.md) |
| [449 奢华机械腕表技术图鉴](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-449) | [G35.md](../prompts/gallery/G35.md) |
| [453 企业级商用画册视觉系统](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-453) | [G10.md](../prompts/gallery/G10.md) |
| [419 可颂烘焙流程 Storyboard](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-419) | [G28.md](../prompts/gallery/G28.md) |
| [411 极简建筑地标海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-411) | [G02.md](../prompts/gallery/G02.md) |
| [402 3D 小红书个人资料卡](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-402) | [G29.md](../prompts/gallery/G29.md) |
| [387 Netflix 首页主视觉 UI](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-387) | [G30.md](../prompts/gallery/G30.md) |
| [373 高端肉类海鲜品牌英雄图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-373) | [G34.md](../prompts/gallery/G34.md) |
| [365 科学家收藏级玩具发布板](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-365) | [G33.md](../prompts/gallery/G33.md) |
| [368 印度餐厅菜单改造宣传图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-368) | [G15.md](../prompts/gallery/G15.md) |
| [363 磁场铁粉 Logo 物理成像](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-363) | [G16.md](../prompts/gallery/G16.md) |
| [338 《赤壁怀古》长卷图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-338) | [G11.md](../prompts/gallery/G11.md) |
| [337 《短歌行》诗词意境图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-337) | [G12.md](../prompts/gallery/G12.md) |
| [ui-screenshot-system UI 截图系统](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-ui) | [T01.md](../prompts/templates/T01.md) |
| [infographic-engine 信息图引擎](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-infographic) | [T02.md](../prompts/templates/T02.md) |
| [scientific-scale-diagram 科学尺度缩放图](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-infographic) | [T03.md](../prompts/templates/T03.md) |
| [poster-layout-system 海报排版系统](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) | [T04.md](../prompts/templates/T04.md) |
| [sports-campaign-poster 运动商业 Campaign](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) | [T05.md](../prompts/templates/T05.md) |
| [conceptual-typography-poster 概念字体海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) | [T06.md](../prompts/templates/T06.md) |
| [ink-double-exposure-poster 水墨双重曝光海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) | [T07.md](../prompts/templates/T07.md) |
| [nature-science-poster 自然科普海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) | [T08.md](../prompts/templates/T08.md) |
| [product-commerce-visual 商品商业视觉](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-product) | [T09.md](../prompts/templates/T09.md) |
| [personalized-beauty-report 个性化美妆报告](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-product) | [T10.md](../prompts/templates/T10.md) |
| [brand-identity-package 品牌身份包](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-brand) | [T11.md](../prompts/templates/T11.md) |
| [brand-touchpoint-board 品牌触点视觉板](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-brand) | [T12.md](../prompts/templates/T12.md) |
| [architecture-space 建筑与空间](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-architecture) | [T13.md](../prompts/templates/T13.md) |
| [realistic-photography 写实摄影](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-photo) | [T14.md](../prompts/templates/T14.md) |
| [street-accident-moment 街头意外瞬间摄影](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-photo) | [T15.md](../prompts/templates/T15.md) |
| [illustration-art-style 插画与艺术风格](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-illustration) | [T16.md](../prompts/templates/T16.md) |
| [character-design-sheet 角色设定表](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-character) | [T17.md](../prompts/templates/T17.md) |
| [3d-collectible-toy 3D 收藏玩具](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-character) | [T18.md](../prompts/templates/T18.md) |
| [scene-storytelling 场景叙事](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-scene) | [T19.md](../prompts/templates/T19.md) |
| [history-classical-themes 历史与古风题材](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-history) | [T20.md](../prompts/templates/T20.md) |
| [document-publishing 文档与出版物](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-document) | [T21.md](../prompts/templates/T21.md) |
| [concept-product-breakdown 概念产品研发拆解](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-other) | [T22.md](../prompts/templates/T22.md) |
| [01-hero-image.json 白底/纯色底产品主图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/01-hero-image.json) | [EC01.md](../prompts/ecommerce/EC01.md) |
| [02-lifestyle-scene.json 场景化生活图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/02-lifestyle-scene.json) | [EC02.md](../prompts/ecommerce/EC02.md) |
| [03-flat-lay.json 平铺图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/03-flat-lay.json) | [EC03.md](../prompts/ecommerce/EC03.md) |
| [04-detail-macro.json 细节微距图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/04-detail-macro.json) | [EC04.md](../prompts/ecommerce/EC04.md) |
| [05-poster-banner.json 促销海报/Banner](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/05-poster-banner.json) | [EC05.md](../prompts/ecommerce/EC05.md) |
| [06-social-media.json 社交媒体素材](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/06-social-media.json) | [EC06.md](../prompts/ecommerce/EC06.md) |
| [07-ugc-style.json UGC风格/买家秀](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/07-ugc-style.json) | [EC07.md](../prompts/ecommerce/EC07.md) |
| [08-model-showcase.json 模特展示图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/08-model-showcase.json) | [EC08.md](../prompts/ecommerce/EC08.md) |
| [09-before-after.json 使用前后对比图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/09-before-after.json) | [EC09.md](../prompts/ecommerce/EC09.md) |
| [10-packaging.json 包装设计展示](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/10-packaging.json) | [EC10.md](../prompts/ecommerce/EC10.md) |
| [11-infographic.json 信息图/A+Content](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/11-infographic.json) | [EC11.md](../prompts/ecommerce/EC11.md) |
| [12-creative-concept.json 创意概念广告图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/12-creative-concept.json) | [EC12.md](../prompts/ecommerce/EC12.md) |
| [13-size-spec.json 尺寸规格+使用步骤图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/13-size-spec.json) | [EC13.md](../prompts/ecommerce/EC13.md) |
| [14-multi-product.json 多产品套装/组合展示](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/14-multi-product.json) | [EC14.md](../prompts/ecommerce/EC14.md) |
| [15-livestream.json 电商直播间场景](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/15-livestream.json) | [EC15.md](../prompts/ecommerce/EC15.md) |
| [16-try-on-virtual.json 虚拟试穿/产品融入场景](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/16-try-on-virtual.json) | [EC16.md](../prompts/ecommerce/EC16.md) |
| [17-exploded-view.json 技术拆解/爆炸图](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/17-exploded-view.json) | [EC17.md](../prompts/ecommerce/EC17.md) |
| [18-ghost-mannequin.json 隐形模特](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/18-ghost-mannequin.json) | [EC18.md](../prompts/ecommerce/EC18.md) |
| [19-multi-angle-grid.json 产品多角度网格](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/19-multi-angle-grid.json) | [EC19.md](../prompts/ecommerce/EC19.md) |
| [20-magazine-editorial.json 杂志大片/封面](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/20-magazine-editorial.json) | [EC20.md](../prompts/ecommerce/EC20.md) |
| [21-seasonal-campaign.json 季节主题网格](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/21-seasonal-campaign.json) | [EC21.md](../prompts/ecommerce/EC21.md) |
| [22-luxury-atmospherics.json 奢华氛围渲染](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/22-luxury-atmospherics.json) | [EC22.md](../prompts/ecommerce/EC22.md) |
| [23-device-mockup.json 设备界面模型](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/23-device-mockup.json) | [EC23.md](../prompts/ecommerce/EC23.md) |
| [24-storefront.json 店铺门面/空间摄影](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/24-storefront.json) | [EC24.md](../prompts/ecommerce/EC24.md) |
| [25-sports-campaign.json 运动/健身广告](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/25-sports-campaign.json) | [EC25.md](../prompts/ecommerce/EC25.md) |

## 待精选案例按来源分类

| 分类 | 条目数 |
| --- | ---: |
| Illustration & Art | 57 |
| Posters & Typography | 88 |
| Scenes & Storytelling | 19 |
| Characters & People | 29 |
| Photography & Realism | 76 |
| Brand & Logos | 25 |
| Charts & Infographics | 51 |
| Products & E-commerce | 32 |
| UI & Interfaces | 71 |
| History & Classical Themes | 14 |
| Other Use Cases | 26 |
| Architecture & Spaces | 10 |
| Documents & Publishing | 9 |

不以机械套前后缀改写余下案例。后续优先新构图、新编辑任务或电商实际用途，再处理同类变体。所有条目在CSV中有标题、出处、状态与说明，未改写部分不进入提示词统计。

## 新版作者来源（不计入旧库盘点）

2026-09-19：[GPT Image 2.5提示词指南](https://gptimage2-5.art/blog/gpt-image-2-5-prompt-guide)公开页面已读。其三参考图职责、保留清单和一次只改一个变量可作为提示词组织方法；页面自述的五组测试没有转写为本库实测。对应整理为EC53、EC54和T410，来源与适配边界已写入数据卡。

2026-09-10：[C008战斗精灵图](../cases/C008-combat-sprite-sheet.md)来自Practical_Low29的公开原帖，含原提示词。2.5为作者自述，具体子型号未知；两个旧库提交版本未变化。

EvoLink来源专题：2026-09-10整理[C009–C011一品三用](../ecommerce/evolink-product-story.md)，对应作者9月9日提供的三组2.5案例。独立于两个旧库盘点，不改动旧库已改写数量。

2026-09-10：原作者上游073d105的527已改写为G32；532用于完善G22，不重复计入新主提示词。四组上游复现未返回具体模型ID。

2026-09-28：buluslan电商库已升级到0.3.3，README与SKILL公开列出39个场景及GPT Image 2.5 Flare/Sunburst路由。本库逐项读取其中4个新增场景：`bulk-product-swap`、`bulk-translate`、`motion-gif`改写为EC59–EC61；`transparent-cutout`与官方来源卡C002重复，只增强原卡的Alpha通道、边缘检查和后续编辑要求，不重复新增。来源仍保留作者和MIT项目链接，不把其运行或检查结果写成本库实测。

## 真实商品样板来源

2026-10-01标签与入口批不新增外部案例或改变来源归属，旧库盘点数量不变。348张商品模板的误归类已修正，528张JSON卡和20张来源／原创卡均有导航元数据；分类依据为本库现有任务、用途和材料，而非填好示例中的SKU。后续参考图逐项核来源及许可，构图示意与实际输出分别标注，不把标签修订算作新提示词或新实测。

| 样板 | 输入来源与许可 | 当前状态 |
| --- | --- | --- |
| [System76 Launch 2](../ecommerce/samples/system76-launch-2.md) | 三张 System76 技术照片，Wikimedia Commons，CC BY-SA 4.0；另核对官方技术规格 | 四段提示词待运行，未生成 |
| [约1949年 NIVEA Creme 铁盒](../ecommerce/samples/nivea-creme-1949-tin.md) | Berthold Werner 历史包装实拍，Wikimedia Commons，CC BY-SA 4.0 | 四段提示词待运行；不外推功效、内容物或当前销售属性 |
| [白色 IKEA LACK 桌](../ecommerce/samples/ikea-lack-white-table.md) | Juhan Sonin 实拍，Wikimedia Commons，CC BY 2.0 | 四段提示词待运行；不把当前官网参数拼接到旧照片 |

2026-09-29 对后两份来源做了文件页级核对并保留原图。当前 IKEA 官网可作为另行核对在售型号的入口，但本轮照片不能证明具体货号、年代或尺寸，因此未将官网销售参数写入这份单图样板。三份样板只有在界面能读到具体 GPT Image 2.5 型号时才进入实际执行记录。
