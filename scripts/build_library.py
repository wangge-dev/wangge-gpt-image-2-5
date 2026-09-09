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
             f"**分类：{entry['category']} · {entry['kind']} · 按 2.5 文档适配，未生图实测**", '',
             entry['use'], '', '## 准备材料与变量', '',
             entry['inputs'], '',
             '将下表中的值按实际任务填写，然后复制正文。示例值用于说明填写方式，不是已核实的商品事实。' if entry['variables'] else '本卡没有文字变量，准备好正文要求的参考图即可复制。', '']
    if entry['variables']:
        lines += ['| 变量 | 填写示例或说明 |', '| --- | --- |']
    for k,v in entry['variables'].items():
        lines.append(f'| `{{{{{k}}}}}` | {v.replace(chr(10), "；").replace("|", "／")} |')
    lines += ['', '## 完整提示词', '', '```text', entry['prompt'], '```', '',
              '## 参数设置', '', f"建议画布：`{entry['size']}`；模型选择及格式见[模型说明](../../guides/models.md)。这是本库的起步建议，不是效果保证。", '',
              ]
    if entry.get('settings_note'):
        lines += [entry['settings_note'], '']
    if entry.get('variants'):
        lines += ['## 可复制变体', '', '选择一个版本，替换变量后整段复制；每段已包含基础要求。']
    for name, instruction in entry.get('variants', {}).items():
        lines += ['', f'### {name}', '', '```text', entry['prompt'] + '\n\n本次版本调整（以此段替换基础正文中的对应布景、布局或风格，未提及要求继续保留）：\n' + instruction, '```']
    lines += ['', '## 接着修改', '', '上传上一轮结果；涉及商品或人物时，同时保留原始参考图。', '', '```text', entry['edit'], '```', '', '## 对照改写说明', '']
    lines += [f'- {x}' for x in entry['adaptation']]
    lines += ['', '适配依据：[2.5 适配规则](../../guides/adaptation.md)。这些方法可能同样适用于其他模型，不宣称 2.5 独占。', '', '## 来源', '']
    lines += [f"- [{s['label']}]({s['url']})" for s in entry['sources']]
    if entry.get('preview'):
        lines += ['', '**旧版参考图：来自原库，用于理解原始构图，不是本提示词的 Image 2.5 输出。**', '', f"![{entry['title']} · 原库旧版参考]({entry['preview']})", '', '原图归原作者；作者链接见上方。']
    lines += ['', '整理日期：2026-09-09。上游许可及第三方素材边界见[署名说明](../../ATTRIBUTIONS.md)。']
    return '\n'.join(lines)

def main():
    entries = json.loads((ROOT/'data/library.json').read_text(encoding='utf-8'))
    groups = {}
    for e in entries:
        write(f"prompts/{e['group']}/{e['id']}.md", render(e))
        groups.setdefault(e['group'], []).append(e)
    labels = {'ecommerce':'电商场景', 'templates':'通用模板', 'gallery':'精选创意'}
    lines = ['# 完整提示词索引', '', '[返回首页](../README.md)', '', f'共 {len(entries)} 张完整适配卡；变体不重复计数。均已完成文档适配，未生图实测。', '', '按用途找到卡片 → 准备参考图 → 替换变量 → 复制完整正文。', '']
    for g,items in groups.items():
        lines += [f"## {labels[g]} · {len(items)}", '', '| 提示词 | 用途 |', '| --- | --- |']
        lines += [f"| [{e['id']} {e['title']}]({g}/{e['id']}.md) | {e['use']} |" for e in items]
        lines += ['']
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
    lines += ['## 一款商品连续出素材', '', '建议顺序：EC01 主图 → EC02 场景 → EC04 细节 → EC11 卖点 → EC13 尺寸 → EC05 活动。每次重新附商品原图，使用同一套真实文案和配色。', '', '需要可直接套用的整套任务单，见[一品多图组合](product-kit.md)。已有的[精准改字](../experiments/E003-copy-edit.md)、[多轮返工](../experiments/E005-revision-chain.md)与[跨境适配](../experiments/E006-localization.md)也可以直接使用。', '', '## 持续补充', '', '资料稀缺的电商玩法长期保留在[待补充清单](../discovery/backlog.md)。发布前另行检查商品事实、文字和平台要求；本库不承诺投放或转化效果。']
    write('ecommerce/README.md','\n'.join(lines))
    gallery = groups.get('gallery', [])
    category_names = {'Architecture & Spaces':'建筑与空间','Brand & Logos':'品牌与标志','Characters & People':'人物与角色','Charts & Infographics':'图表与科普','Documents & Publishing':'文档与出版','History & Classical Themes':'历史与古典','Illustration & Art':'插画与艺术','Other Use Cases':'其他创意','Photography & Realism':'摄影与写实','Posters & Typography':'海报与字体','Products & E-commerce':'商品与电商','Scenes & Storytelling':'场景与叙事','UI & Interfaces':'界面与资料卡'}
    lines = ['# 精选创意画廊', '', '[首页](../README.md) · [全部提示词](../prompts/README.md)', '', f'{len(gallery)} 条独立改写提示词，覆盖 {len(set(e["category"] for e in gallery))} 类创意。每张卡有完整正文、准备材料、后续修改与原作者来源。', '', '**以下全部为原库旧版参考图，不是本库 Image 2.5 输出。** 点击标题进入适配卡。']
    for cat in dict.fromkeys(e['category'] for e in gallery):
        lines += ['', f'## {category_names.get(cat,cat)}', '']
        for e in gallery:
            if e['category'] == cat:
                lines += [f"### [{e['id']} {e['title']}](../prompts/gallery/{e['id']}.md)", '', f"![旧版参考 · {e['title']}]({e['preview']})", '', f"来源：{e['sources'][0]['label']}。本库改写：{e['adaptation'][0]}", '']
    write('gallery/README.md','\n'.join(lines))
    print(f'Rendered {len(entries)} prompt cards; {sum(len(e.get("variants",{})) for e in entries)} complete variants.')

if __name__ == '__main__':
    main()
