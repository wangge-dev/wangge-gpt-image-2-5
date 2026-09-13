# 项目交接：wangge-gpt-image-2-5

更新时间：2026-09-13  
仓库：<https://github.com/wangge-dev/wangge-gpt-image-2-5>  
本地路径：`D:\codexo\wangge-gpt-image-2-5`  
分支：`main`

## 用户最终目标

建设一个独立、持续更新、真正面向GPT Image 2.5的中文提示词库。近期优先做到：电商用户提供商品素材后，能找到接下来需要制作的一整套素材，按顺序复制提示词，并知道每一步如何验收和返工。先堆提示词和跑通流程，统一生图测试放在后面。

## 当前完成状态

- 349条基础提示词：329张 `data/library.json` 卡、11条 `cases/`、9条 `experiments/`。
- 132个完整变体。
- 48套电商场景；EC01–EC48有填写完成的直接示例；另有55条精选创意；T224–T226补卡口盖、防脱螺钉面板和滑锁盖板状态。
- 八套六步电商品类包，共48个步骤：美妆、服饰、食品、家居、数码、小家电、箱包、母婴。
- 可筛选静态画廊已上线：<https://wangge-dev.github.io/wangge-gpt-image-2-5/browse/>。
- 3张用户在ChatGPT网页版生成的结果图；其余画廊图片为明确标注的外部参考。
- 最近已发布内容提交：`d9c48a3`。
- 本次交接提交将在本文件提交后记录于下方。

## 必读文件

1. `AGENTS.md`
2. `README.md`
3. `maintenance/README.md`
4. `maintenance/audits/2026-09-13-first-principles-adversarial-audit.md`
5. `data/README.md` 与 `data/library.json`
6. `ecommerce/README.md` 与 `ecommerce/kits/`
7. `discovery/backlog.md`、`discovery/author-watch.md`
8. `maintenance/reviews/2026-09-13-source-and-ecommerce-review.md`

主知识库项目卡：`C:\Users\Administrator\Documents\Obsidian Vault\00_项目\Image2.5个人玩法库持续建设.md`。可复用资产：`C:\Users\Administrator\Documents\Obsidian Vault\10_资产\模型专用案例库的持续维护方法.md`。

## 第一性判断

当前方案对“预设示例商品且资料齐全”已经形成可执行链路；对“用户只上传自己的商品图即可直接获得整套素材”只部分成立。八套任务包把示例SKU写进了六段正文，普通商品仍需逐段重写；多数步骤实际需要多角度图、细节照、场景图、参数表或说明书。

不要继续用更多固定SKU掩盖这个缺口。下一阶段应先让同一商品事实只填写一次，并明确单图能做什么、资料齐全能做什么。

## 审计任务处理状态

### P1 · 已完成（2026-09-13）

1. `ecommerce/kits/food.md` 第6步输入清单补上图1。
2. 设计八套任务包的统一商品事实单。至少包含：商品身份、外观不可变项、已提供图片及职责、真实规格、准确文字、允许出现的配件/组件、禁止推测项。
3. 每套拆成两条清楚路径：
   - 单图最小路径：只允许主图、有限场景和有依据的局部编辑；缺背面、微距、尺寸和结构时明确跳过。
   - 完整资料路径：多角度、细节、场景、参数和说明书齐全后执行全部六步。
4. 让六步引用同一份事实单；保留现有示例SKU作为填写示范。公开文案应把“直接执行”限定到准备完事实单之后。

### P2 · 已完成（2026-09-13）

1. `README.en.md:65` 的EC01–EC20改为EC01–EC25。
2. `data/README.md`：78改84、cases 5改11。
3. `ATTRIBUTIONS.md`：外部参考图28改29。
4. `discovery/backlog.md`：旧库未精选510改509，或改为由盘点动态计算的表达。
5. `maintenance/README.md`、`maintenance/update-prompt.md`、`discovery/sources.md`：原作者已核查提交更新为 `0dc09c46c8a30b1fdd89c18cc78a894dac2104e3`；不要改变现有卡片用于追溯内容的固定来源提交。
6. `scripts/build_library.py` 先完整渲染/验证，再写生成文件，避免异常留下半生成状态；保持简单，不增加分支门禁、哈希冻结或复杂事务。
7. 增加轻量任务包检查，验证每套6步、每步有来源/输入/正文/验收/返工、正文引用的图号已声明、直接复制区无 `{{...}}`。它只作为维护检查，不设置发布门禁。

完成记录见 `maintenance/reviews/2026-09-13-product-facts-and-kit-repair.md`。八套任务包现在先提交一次商品事实单，再选择单图最小路径或资料齐全路径；原示例 SKU 保留为填写示范。`scripts/check_ecommerce_kits.py` 已加入维护检查，构建脚本改为全部渲染成功后再写文件。本轮仍未生图。

### 后续统一生图测试

提示词链路修复后再执行。必须记录实际模型/子型号、日期、输入素材、提示词版本、尝试次数和结果，不可见型号时不猜测。优先每个品类先测主图、最难一致性步骤和一次局部返工，再决定是否跑完48步。失败分类：商品身份、文字、数量、结构、人物/空间、光影、局部返工。用户此前明确要求“后面再生图”，不要在没有新授权和明确入口时自动产生付费调用。

## 已验证证据

- `python scripts/check_links.py`：2277个本地Markdown链接通过。
- 326个JSON卡，无重复ID，生成卡齐全。
- 总条目346、变体132；八套任务包48步、48个文本块、无双花括号变量。
- `git status --short` 在审计开始及独立审查结束时为空。
- 安全、性能和并发未发现与当前静态仓库相称的高优先级问题。

## 维护和发布命令

在 `D:\codexo\wangge-gpt-image-2-5`：

```powershell
python scripts/build_library.py
python scripts/build_gallery.py
python scripts/check_links.py
git diff --check
git status --short
```

编辑 `data/library.json` 后必须重建卡片；编辑 `data/gallery-metadata.json` 后必须重建画廊。任务包目前是 `ecommerce/kits/*.md` 独立维护，入口由 `scripts/build_library.py` 生成到 `ecommerce/README.md`。提交前只加入本仓库本次文件，不强推，不覆盖用户修改。

正常 `git push origin HEAD` 偶尔发生连接重置。只有正常推送确实失败时，历史任务使用过 `D:\codexo\.tmp\image25-sources\publish_git_api.py` 上传原Git对象并快进；该脚本不在仓库内，不应当成项目依赖。发布后通过GitHub提交页核对远端SHA。

## 来源状态

- `freestylefly/awesome-gpt-image-2` 最新已核查 `0dc09c46...`，相对已处理 `073d105...` 只有赞助内容。
- `wangge-dev/awesome-gpt-image-2` 已核查 `b477278b...`。
- `buluslan/gpt-image2-ecommerce` 已核查 `a3673fb...`。
- EvoLink的三个作者提供2.5案例已整理为C009–C011。
- 官方2.5章节、共享方法、作者自述模型和本库实际输出必须继续分开标注。

## 交接边界

本轮只读审查没有修复上述内容问题，也没有删除文件或生成图片。只新增审计报告和本交接文件。下一任务应从P1开始，修复后更新CHANGELOG和维护记录、运行验证、提交并推送，再把结果回写主知识库项目卡。

交接提交：待本文件提交后更新或由下一任务用 `git log -1 --oneline` 获取。
