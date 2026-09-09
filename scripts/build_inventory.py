"""Build source inventory from downloaded cases.json, style-library.json and ecom.json.
Usage: python scripts/build_inventory.py SOURCE_DIRECTORY
This indexes sources, not automatically reviewing or rewriting their content.
"""
import csv,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SHA='b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4'
EC_SHA='a3673fb6f316664280e6abd90a60a578c6fb2228'
def main():
    source=Path(sys.argv[1])
    cases=json.loads((source/'cases.json').read_text(encoding='utf-8'))['cases']
    templates=json.loads((source/'style-library.json').read_text(encoding='utf-8'))['templates']
    ecommerce=json.loads((source/'ecom.json').read_text(encoding='utf-8'))
    library=json.loads((ROOT/'data/library.json').read_text(encoding='utf-8'))
    lookup={(e['group'],str(e['source_key'])):e for e in library}
    rows=[]
    for group,items in [('gallery',cases),('templates',templates),('ecommerce',ecommerce)]:
        for s in items:
            key=str(s['_source_file'] if group=='ecommerce' else s['id'])
            e=lookup.get((group,key))
            title=s['name'] if group=='ecommerce' else s['title']['zh'] if group=='templates' else s['title']
            if group=='gallery':
                url=f'https://github.com/wangge-dev/awesome-gpt-image-2/blob/{SHA}/docs/gallery-part-{1 if s["id"]<=165 else 2}.md#case-{s["id"]}'
            elif group=='templates':
                url=f'https://github.com/wangge-dev/awesome-gpt-image-2/blob/{SHA}/docs/templates.md#{s["anchor"]}'
            else:
                url=f'https://github.com/buluslan/gpt-image2-ecommerce/blob/{EC_SHA}/references/templates/{key}'
            rows.append(dict(source_group=group,source_id=key,title=title,category=s.get('category','电商场景'),source_version=EC_SHA if group=='ecommerce' else SHA,source_url=url,original_author=s.get('sourceLabel','buluslan / Buluu@新西楼' if group=='ecommerce' else 'awesome-gpt-image-2 / freestylefly'),original_url=s.get('sourceUrl',''),decision='改写收录' if e else '后续精选',target=f"prompts/{group}/{e['id']}.md" if e else '',reason='；'.join(e['adaptation']) if e else '已做索引盘点，尚未逐条改写与内容审核；后续按差异和用途精选，不计为2.5适配内容',source_variants=';'.join(s.get('variants',{})) if group=='ecommerce' else '',adapted_variants=';'.join(e.get('source_variant_keys',[])) if e else ''))
    out=ROOT/'sources';out.mkdir(exist_ok=True)
    with (out/'inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
    lines=['# 两个来源库的盘点与改写对应', '', '[首页](../README.md) · [完整CSV](inventory.csv)', '', '盘点日期：2026-09-09。覆盖源库结构化案例索引、模板索引与电商模板文件。全量索引不等于全量逐条精读或全量改写。', '', '| 来源范围 | 索引项 | 已改写 | 后续精选 |', '| --- | ---: | ---: | ---: |']
    for group,name in [('gallery','旧库案例'),('templates','旧库模板索引'),('ecommerce','电商模板')]:
        items=[r for r in rows if r['source_group']==group];done=sum(r['decision']=='改写收录' for r in items)
        lines.append(f'| {name} | {len(items)} | {done} | {len(items)-done} |')
    lines += ['', f'来源版本：awesome `{SHA}`；ecommerce `{EC_SHA}`。版本用于追溯原文，不限制未来更新。', '', '案例索引541项，编号1至544，缺12、169、170。模板JSON有22项；其Markdown正文还有未独立进入JSON的签名、品牌人格等扩展，列入待补充，不宣传为全文所有模板均已迁移。电商25个文件中的88个变体方向均已处理。', '', '## 已改写条目', '', '| 原条目 | 适配卡 |', '| --- | --- |']
    lines += [f"| [{r['source_id']} {r['title'].replace('|','／')}]({r['source_url']}) | [{r['target'].split('/')[-1]}](../{r['target']}) |" for r in rows if r['target']]
    lines += ['', '## 待精选案例按来源分类', '', '| 分类 | 条目数 |', '| --- | ---: |']
    lines += [f'| {k} | {v} |' for k,v in Counter(r['category'] for r in rows if not r['target']).items()]
    lines += ['', '不以机械套前后缀改写余下案例。后续优先新构图、新编辑任务或电商实际用途，再处理同类变体。所有条目在CSV中有标题、出处、状态与说明，未改写部分不进入提示词统计。']
    (out/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print(f'Indexed {len(rows)} source items; {sum(bool(r["target"]) for r in rows)} mapped adaptations.')
if __name__=='__main__': main()
