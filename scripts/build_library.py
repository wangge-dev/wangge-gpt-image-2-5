"""Render reviewed prompt content into GitHub-readable cards. No network or generation calls."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.rstrip() + '\n', encoding='utf-8', newline='\n')

def render(entry):
    lines = [f"# {entry['id']} · {entry['title']}", '',
             '[全部提示词](../README.md) · [首页](../../README.md)', '',
             f"**分类：{entry['category']} · {entry['kind']}**", '',
             entry['use'], '', '## 准备材料与变量', '',
             entry['inputs'], '',
             '将下表中的值按实际任务填写，然后复制正文。示例值用于说明填写方式，不是已核实的商品事实。' if entry['variables'] else '本卡没有文字变量，准备好正文要求的参考图即可复制。', '']
    if entry['variables']:
        lines += ['| 变量 | 填写示例或说明 |', '| --- | --- |']
    for k,v in entry['variables'].items():
        lines.append(f'| `{{{{{k}}}}}` | {v.replace(chr(10), "；").replace("|", "／")} |')
    if entry.get('example'):
        lines += ['', '## 拿来就用的具体示例', '', entry.get('example_inputs', entry['inputs']), '', '按示例准备对应素材后，直接复制下段；其他商品使用后面的变量模板。', '', '```text', entry['example'], '```', '']
    lines += ['', '## 完整提示词', '', '```text', entry['prompt'], '```', '',
              '## 参数设置', '', f"建议画布：`{entry['size']}`；模型选择及格式见[模型说明](../../guides/models.md)。网页版可按相同比例描述画布。", '',
              ]
    if entry.get('usage_note'):
        lines += [entry['usage_note'], '']
    if entry.get('settings_note'):
        lines += [entry['settings_note'], '']
    if entry.get('variants'):
        lines += ['## 可复制变体', '', '选择一个版本，替换变量后整段复制；每段已包含基础要求。']
    for name, instruction in entry.get('variants', {}).items():
        lines += ['', f'### {name}', '', '```text', instruction if entry.get('variants_format') == 'complete' else entry['prompt'] + '\n\n' + instruction, '```']
    lines += ['', '修改前，将修改指令中的双花括号内容按实际问题填写；每次只处理一个位置。']
    lines += ['', '## 接着修改', '', '上传上一轮结果；涉及商品或人物时，同时保留原始参考图。', '', '```text', entry['edit'], '```', '', '## 来源', '']
    lines += [f"- [{s['label']}]({s['url']})" for s in entry['sources']]
    if entry.get('preview'):
        own = entry.get('preview_kind') == 'user_result'
        label = '生成示例 · wangge-dev / ChatGPT 网页版' if own else '原库参考'
        url = '../../' + entry['preview'] if own else entry['preview']
        lines += ['', label, '', f"![{entry['title']} · {label}]({url})"]
    lines += ['', '整理日期：2026-09-09。上游许可及第三方素材边界见[署名说明](../../ATTRIBUTIONS.md)。']
    return '\n'.join(lines)

def main():
    entries = json.loads((ROOT/'data/library.json').read_text(encoding='utf-8'))
    groups = {}
    for e in entries:
        write(f"prompts/{e['group']}/{e['id']}.md", render(e))
        groups.setdefault(e['group'], []).append(e)
    labels = {'ecommerce':'电商场景', 'templates':'通用模板', 'gallery':'精选创意'}
    lines = ['# 完整提示词索引', '', '[返回首页](../README.md)', '', f'共 {len(entries)} 张提示词卡，包含场景变体与后续修改指令。', '', '按用途找到卡片 → 准备参考图 → 替换变量 → 复制完整正文。', '']
    for g,items in groups.items():
        lines += [f"## {labels[g]} · {len(items)}", '', '| 提示词 | 用途 |', '| --- | --- |']
        lines += [f"| [{e['id']} {e['title']}]({g}/{e['id']}.md) | {e['use']} |" for e in items]
        lines += ['']
    lines += ['## 明确2.5来源 · 8', '', '[换装、透明商品、换语言、草图、图表、物品移除与广告牌：完整中文提示词](../cases/README.md)', '']
    write('prompts/README.md','\n'.join(lines))
    ec = groups.get('ecommerce', [])
    lines = ['# 电商提示词专区', '', '[首页](../README.md) · [全部提示词](../prompts/README.md)', '', f'{len(ec)} 套场景模板，包含完整变体与后续修改指令。先上传真实商品图，填写商品事实，再复制对应模板。', '', '## 按任务找提示词', '']
    for cat in dict.fromkeys(e['category'] for e in ec):
        lines += [f'### {cat}', '']
        lines += [f"- [{e['id']} {e['title']}](../prompts/ecommerce/{e['id']}.md)：{e['use']}" for e in ec if e['category']==cat]
        lines += ['']
    extensions = [e for e in entries if e['group']=='gallery' and e['category']=='Products & E-commerce']
    if extensions:
        lines += ['## 精选电商创意拓展', '']
        lines += [f"- [{e['id']} {e['title']}](../prompts/gallery/{e['id']}.md)" for e in extensions]
        lines += ['']
    lines += ['## 明确2.5来源的电商用法', '', '[参考换装](../cases/C001-reference-clothing.md) · [透明商品](../cases/C002-transparent-product.md) · [保留版式换语言](../cases/C003-layout-translation.md)', '']
    lines += ['## 一款商品连续出素材', '', '建议顺序：EC01 主图 → EC02 场景 → EC04 细节 → EC11 卖点 → EC13 尺寸 → EC05 活动。每次重新附商品原图，使用同一套真实文案和配色。', '', '需要可直接套用的整套任务单，见[一品多图组合](product-kit.md)。已有的[精准改字](../experiments/E003-copy-edit.md)、[多轮返工](../experiments/E005-revision-chain.md)与[跨境适配](../experiments/E006-localization.md)也可以直接使用。', '', '## 持续补充', '', '持续补充品类专用提示词、场景变体与编辑技巧。欢迎在[贡献说明](../CONTRIBUTING.md)中提交新需求。']
    write('ecommerce/README.md','\n'.join(lines))
    gallery = groups.get('gallery', [])
    category_names = {'Architecture & Spaces':'建筑与空间','Brand & Logos':'品牌与标志','Characters & People':'人物与角色','Charts & Infographics':'图表与科普','Documents & Publishing':'文档与出版','History & Classical Themes':'历史与古典','Illustration & Art':'插画与艺术','Other Use Cases':'其他创意','Photography & Realism':'摄影与写实','Posters & Typography':'海报与字体','Products & E-commerce':'商品与电商','Scenes & Storytelling':'场景与叙事','UI & Interfaces':'界面与资料卡'}
    lines = ['# 精选创意画廊', '', '[首页](../README.md) · [全部提示词](../prompts/README.md)', '', f'{len(gallery)} 条独立改写提示词，覆盖 {len(set(e["category"] for e in gallery))} 类创意。每张卡有完整正文、准备材料、后续修改与原作者来源。', '', '图片分别标注生成示例或原库参考，点击标题查看完整提示词。']
    for cat in dict.fromkeys(e['category'] for e in gallery):
        lines += ['', f'## {category_names.get(cat,cat)}', '']
        for e in gallery:
            if e['category'] == cat:
                lines += [f"### [{e['id']} {e['title']}](../prompts/gallery/{e['id']}.md)", '', f"![{e['title']}]({'../' + e['preview'] if e.get('preview_kind') == 'user_result' else e['preview']})", '', ("生成示例：wangge-dev / ChatGPT 网页版" if e.get("preview_kind") == "user_result" else f"原库参考：{e['sources'][0]['label']}"), '']
    write('gallery/README.md','\n'.join(lines))
    print(f'Rendered {len(entries)} prompt cards; {sum(len(e.get("variants",{})) for e in entries)} complete variants.')

if __name__ == '__main__':
    main()
