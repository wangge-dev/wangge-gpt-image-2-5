# 2026-11-02：活动日程成片、目标保护与服装证据

周一维护，起点为main的14f1f89，起始工作区干净，远端同SHA。执行用户已确认的独立成片与许可真实参考路线：完整可复制提示词是交付，实测可选；本批没有调用生图、付费采集、ChatGPT浏览器或账号支付功能，没有创建Skill。

## 本批三个实质交付

| 卡片 | 独立任务或实际冲突 | 改动与缺素材路径 |
| --- | --- | --- |
| [EC66](../../prompts/ecommerce/EC66.md)（新增原创） | 买家需要读清活动阶段的起止、时区和参与条件，不是EC52价格KV或T36内部时间线 | 4:5，上下信息区合计100%；1–3阶段与各自条件同块，不计算优惠、倒计时或实时状态。完整原照窗与商家文字职责分开；新增完整无商品图纯文字分支 |
| [EC16](../../prompts/ecommerce/EC16.md)（编辑实质修订） | 基础版保留真实目标，背景风格变体却可能重造房间；默认尺寸变量曾混合服装与空间 | 沿用图2原机位、画幅、人物／环境及遮挡；试穿与空间用独立尺寸变量，缺实测尺度或需要未知面就补材料。三个来源风格仅在目标本来具备该环境时沿用，不强改背景 |
| [EC18](../../prompts/ecommerce/EC18.md)（主图实质修订） | 平铺外观不证明撑起后的胸腰体积；开领卷袖可能暴露没有实拍的内侧 | 立体版要求已经实拍撑起的完整轮廓及相容内侧；保持真实开合，不凭空开领、卷袖或补标签。新增完整单图平铺原照分支；若也无完整单件平铺照则补素材，不靠新分支虚构材料 |

EC18单图返工不引用不存在的图2；EC66纯文字分支使用独立的适用范围与边界变量，不继承“图示杯具”或照片作者活动之类文案。三个基础示例均逐字等于本卡模板填入自身变量；完整分支只填自身实际引用变量。

布局先确定主体、原取景、安全区、阅读顺序及图文职责，再限定光影和背景。EC18在8%安全区内等比适配，不同时强定衣物宽高；原有构图示意同步改说明，仍非实测。EC16提示词保留目标构图不等于像素冻结，精确保留需外部局部合成。

本批按交付归为两条高频成片（主图与活动）、一条编辑，不新增结构核对卡。连续配比继续观察；下一批优先找有独立任务差异的主图、详情或商业视觉，不为比例硬凑卡，也不重复本批修复。

## 一张新真实参考，不是结果图

- 接受：Akshaya govindasamy的[Coffee cup image.jpg](https://commons.wikimedia.org/wiki/File:Coffee_cup_image.jpg)，文件页及Commons imageinfo核对作者、Own work、CC BY-SA 4.0和3000×4000；实际下载原件并本地查看。原件带方向元数据，浏览器解码同尺寸。
- [本地原件与素材卡](../../assets/references/coffee-cup-image/README.md)完整保留相机、作者、日期标记；不裁切、不改色、不去署名。网页等比显示，放大查看仍完整。使用[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)标注，照片及适用改编不自动改标本库MIT，其他权利另核；不表示作者背书。
- EC66的照片只负责杯具可见外观及原环境，不证明容量、材质、安全、价格或在售SKU。两阶段文字是明确标注的排版练习，不代表作者、品牌、商店或平台真实活动，拍摄日期也不是活动日期。
- 未收录两张已查看的服装候选：[T-shirt mocup.jpg](https://commons.wikimedia.org/wiki/File:T-shirt_mocup.jpg)虽标CC0，但为两件叠穿且有鞋腿，不是本轮需要的完整单衣；[White simple T-shirt made by COQ manufacture.jpg](https://commons.wikimedia.org/wiki/File:White_simple_T-shirt_made_by_COQ_manufacture.jpg)虽有CC BY-SA 4.0，却是人物半身穿着取景，不能证明完整衣物轮廓、内侧或肖像授权。许可可读不等于任务材料充分。
- [参考入口](../../ecommerce/licensed-references.md)、[署名](../../ATTRIBUTIONS.md)、卡片Markdown与画廊元数据同步。现有输入预览卡共引用四个不同原件；不是全仓库全部历史照片总数，也不是六张新照片。

## 来源核查（本日实际查询）

[OpenAI当前2.5提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)核对构图、逐图职责、文字、编辑范围及多轮漂移边界。固定a3673fb的[16-try-on-virtual](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/16-try-on-virtual.json)与[18-ghost-mannequin](https://github.com/buluslan/gpt-image2-ecommerce/blob/a3673fb6f316664280e6abd90a60a578c6fb2228/references/templates/18-ghost-mannequin.json)全文重读，保留七个来源键、出处及旧创意适配定位，不把旧图称为2.5原生或本库实测。

| 仓库 | 本日核对的HEAD | 与上批比较 |
| --- | --- | --- |
| freestylefly/awesome-gpt-image-2 | 63e6176fa01be51c000108dacd72716d3e46784b | 未变 |
| wangge-dev/awesome-gpt-image-2 | b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4 | 未变 |
| buluslan/gpt-image2-ecommerce | 73abd50bf2b689b5a453f28ddd7b0016415deec6 | 未变 |
| EvoLinkAI/gpt-image-2.5-for-e-commerce | 963b1f40bfbe5ff81f0c9684587face6a500bc9a | 未变 |
| AtlasCloudAI/awesome-gpt-image-2.5-prompts | 97d420e8a4f97258bd8ee5186025170b45e7c182 | 相比6f85d1a有7提交，实际仅20份README修改，无案例数据／照片变动 |

Atlas实际读了[compare响应](https://github.com/AtlasCloudAI/awesome-gpt-image-2.5-prompts/compare/6f85d1a96b9fcfb32c7f40c06420f4582c6389ee...97d420e8a4f97258bd8ee5186025170b45e7c182)，没有因提交名“add prompts”宣称新案例。[Simon主页](https://simonwillison.net/)和[BrushGlow提示词指南](https://gptimage2-5.art/blog/gpt-image-2-5-prompt-guide)定向读取，本轮未取得可独立转化的新2.5成片案例；没有全量回扫所有作者与X帖。第三方测试描述不计本库实测。

[来源CSV](../../sources/inventory.csv)只改EC16／EC18两行处理理由，仍588条；旧gallery541／35／506及来源变体方向数不变。EC66为本库原创，不伪列来源新增案例。

## 当前数据与验证

当前533张JSON卡，加11条cases与9条experiments，共553条基础提示词；66电商、157完整变体（电商106）。451原创／91适配／11来源。画廊67条预览，其中24原创示意、6真实输入参考预览卡；31精选均有预览。3张历史用户结果及8个has_result案例ID未变。

实际执行通过：

- `python -X utf8 scripts/build_library.py`：533卡／157完整变体。
- `python -X utf8 scripts/build_gallery.py`：553基础提示词。
- 临时检查脚本比对提交前源数据：原532卡仅EC16、EC18变化，新增EC66；其余卡完整相同，旧变体键与来源保留。元数据也只改对应三卡，CSV只改上述两行。
- 三卡的模板填值等于示例、无未填占位符；两条新少素材分支不依赖缺失图片或未启用分支变量。
- 本地无头浏览器1365×900和360×900：三卡共30次正文切换、显示比对、复制与剪贴板回读通过；默认31精选、筛选与单卡入口、参考图解码、作者／许可／源页／职责、放大署名、无横向溢出及无页面脚本错误通过。
- 截图在D:/codexo/.tmp/image2-campaign-check-20261102；实际查看EC66手机端放大图及EC18桌面图，杯具相机与作者标记完整，衣物示意仍标非实测。

- `python -X utf8 scripts/check_ecommerce_kits.py`：8套任务包、48步通过。
- `python -X utf8 scripts/check_links.py`：3679个本地文件链接通过，不含标题锚点或外部URL；本批外部来源与许可由上述实际读取另核。
- `git diff --check`通过，无空白错误；只核对本批文件，不修改旧结果或无关用户内容。

构建、页面与复制检查不是模型实测，不声称成功率、成本或真人平台验收。

## 下一步与发布边界

继续独立高频成片与编辑／商业创意缺口，按用途而非数量补许可真实参考；不要求全库重新生图。浏览器连接故障不在本批处理。正常提交推送仅包含本批仓库文件，发布状态以提交、远端与Pages实读为准，本地构建通过不等于网站已更新；具体同步证据回写知识库项目卡。
