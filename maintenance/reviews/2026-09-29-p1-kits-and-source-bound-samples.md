# 2026-09-29 P1任务包修复与来源绑定样板

## 本轮结论

本轮不扩提示词数量，先修复交接审计中两个会直接阻断使用的P1问题：八套“只有一张商品图”路径原先仍要求额外图片，六步正文又写死示例SKU。修复后，每个任务包都有独立单图正文，48段六步正文都直接引用当前《商品事实单》。专项检查已从只看结构升级为同时约束单图路径与事实单引用。

System76 Launch 2 的真实网页生图没有执行成功。浏览器控制在初次读取、一次重试和重置会话后的最后一次尝试中都返回 `Browsers: Error: nodeRepl.fetch request failed`，无法读取可信URL或具体图像型号。用户随后明确说明浏览器已打开，并授权现有浏览器仍失败时改用内置浏览器；现有浏览器读取仍返回同一错误，内置浏览器打开 `https://chatgpt.com/` 时首次等待30秒超时并重置控制内核，重置后的唯一重试再次超时并再次重置。按照恢复规则停止，没有上传素材、发送提示词、生成结果或局部返工，也没有用未知型号的通用生图替代。

## P1修复

涉及八个文件：

- `ecommerce/kits/apparel.md`
- `ecommerce/kits/appliance.md`
- `ecommerce/kits/baby.md`
- `ecommerce/kits/bags.md`
- `ecommerce/kits/beauty.md`
- `ecommerce/kits/digital.md`
- `ecommerce/kits/food.md`
- `ecommerce/kits/home.md`

每包的最小路径现在明确指向 `只有图1时直接复制`，该段只调用图1与《商品事实单》，只允许使用正面照片中可见的商品身份、颜色、轮廓、材质、文字和可见部件。未知侧背面、内部、配件、尺寸、功效、认证和价格一律不补。

六步正文中的白色T恤、深灰无线键盘、浅橡木床头柜等固定示例已移除，改为按当前事实单和该步实际来源图执行。示例事实单仍可帮助读者理解填写方式，但不再与可复制正文竞争。

`scripts/check_ecommerce_kits.py` 新增检查：

1. 每包必须有且仅有一个单图正文；
2. 最小路径必须明确指向该正文，不能再指向第1步；
3. 单图正文必须引用《商品事实单》，不得出现图2及以上；
4. 48段六步正文都必须直接引用《商品事实单》。

## 两份新的来源绑定执行包

### 历史 NIVEA Creme 铁盒

- 输入：Wikimedia Commons 的约1949年铁盒实拍，摄影者 Berthold Werner，CC BY-SA 4.0。
- 文件：`assets/samples/nivea-creme-1949-tin/source.jpg`。
- 执行包：`ecommerce/samples/nivea-creme-1949-tin.md`。
- 四段任务：白底档案图、复古陈列、字样与旧化细节、中文档案信息模块。
- 边界：不展示内容物、盒底或使用效果，不写成分、容量、功效、现价或当前在售结论。

### 白色 IKEA LACK 桌

- 输入：Wikimedia Commons 的单张实拍，摄影者 Juhan Sonin，CC BY 2.0。
- 文件：`assets/samples/ikea-lack-white-table/source.jpg`。
- 执行包：`ecommerce/samples/ikea-lack-white-table.md`。
- 四段任务：白底外观、卧室边桌场景、桌面与桌腿连接外观、中文证据边界模块。
- 边界：照片不能证明具体年代、货号、尺寸、材质、内部结构或承重，因此未把当前官网销售参数拼接到旧照片上，也不生成安装步骤。

两份执行表均保持“待运行”。它们提供的是来源绑定、许可边界和逐张可复制正文，不是模型实测结果。

## 画廊与统计修订

- 为T193–T197五张材质文字编辑卡增加 `task` 与 `product_category`，使其能从“局部编辑”和实际商品材质筛选进入。
- 元数据文件现有336条，其中316条对应528张JSON卡，另20条对应cases/experiments；仍有212张templates卡待分批补齐，不能机械归入同一电商品类。
- 修正 `data/README.md` 的528张JSON卡、`ecommerce/start-here.md` 的61套场景，以及维护说明里的当前统计口径。
- heartbeat 已由前一任务移交到当前任务，实际配置不含固定旧基线；本轮只在交接文档中同步这一事实，没有创建重复自动化。

## 验证结果与边界

- `python -X utf8 scripts/build_library.py`：生成528张卡，132个完整变体。
- `python -X utf8 scripts/build_gallery.py`：画廊嵌入548条提示词。
- `python -X utf8 scripts/check_ecommerce_kits.py`：八套、48步通过；同时覆盖新增单图正文和事实单引用规则。
- `python -X utf8 scripts/check_links.py`：3363个本地文件链接通过；该脚本不检查标题锚点和远端URL。
- 独立JSON核对：元数据336条，覆盖316/528张JSON卡，余212张；T193–T197的任务与商品品类已进入生成画廊。
- 两张来源图已本地打开检查，内容分别对应历史 NIVEA 铁盒和白色方桌；`git diff --check` 通过，只有Git对行尾转换的提示。

这些验证能证明文档结构、生成产物和本地链接一致，不能证明提示词在 GPT Image 2.5 下已生成成功。任何浏览器执行仍以界面可见具体型号为前提。
