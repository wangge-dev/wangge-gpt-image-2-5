# 两个来源库的盘点与改写对应

[首页](../README.md) · [完整CSV](inventory.csv)

盘点日期：2026-09-09。覆盖源库结构化案例索引、模板索引与电商模板文件。全量索引不等于全量逐条精读或全量改写。

| 来源范围 | 索引项 | 已改写 | 后续精选 |
| --- | ---: | ---: | ---: |
| 旧库案例 | 541 | 31 | 510 |
| 旧库模板索引 | 22 | 22 | 0 |
| 电商模板 | 25 | 25 | 0 |

来源版本：awesome `b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4`；ecommerce `a3673fb6f316664280e6abd90a60a578c6fb2228`。版本用于追溯原文，不限制未来更新。

案例索引541项，编号1至544，缺12、169、170。模板JSON有22项；其Markdown正文还有未独立进入JSON的签名、品牌人格等扩展，列入待补充，不宣传为全文所有模板均已迁移。电商25个文件中的88个变体方向均已处理，其中2个重复方向合并到基础正文，目前提供86个独立复制变体。

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
| [453 企业级商用画册视觉系统](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-453) | [G10.md](../prompts/gallery/G10.md) |
| [419 可颂烘焙流程 Storyboard](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-419) | [G28.md](../prompts/gallery/G28.md) |
| [411 极简建筑地标海报](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-411) | [G02.md](../prompts/gallery/G02.md) |
| [402 3D 小红书个人资料卡](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-402) | [G29.md](../prompts/gallery/G29.md) |
| [387 Netflix 首页主视觉 UI](https://github.com/wangge-dev/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-387) | [G30.md](../prompts/gallery/G30.md) |
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
| Products & E-commerce | 35 |
| UI & Interfaces | 71 |
| History & Classical Themes | 14 |
| Other Use Cases | 26 |
| Architecture & Spaces | 10 |
| Documents & Publishing | 9 |

不以机械套前后缀改写余下案例。后续优先新构图、新编辑任务或电商实际用途，再处理同类变体。所有条目在CSV中有标题、出处、状态与说明，未改写部分不进入提示词统计。
