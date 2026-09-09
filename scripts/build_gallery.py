"""Build a dependency-free gallery from the maintained prompt cards."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build():
    cards = json.loads((ROOT/'data/library.json').read_text(encoding='utf-8'))
    entries = []
    for card in cards:
        e = dict(card)
        e['path'] = f"prompts/{e['group']}/{e['id']}.md"
        e['task'] = e.get('task', e['category'])
        e['product_category'] = e.get('product_category', '通用品类' if e['group']=='ecommerce' else '非商品专项')
        e['reference'] = '需要' if e.get('requires_reference') or re.search(r'图[1一AB]|参考照|上传|参考图', e['prompt']) else '按卡片说明'
        e['has_result'] = e.get('preview_kind') == 'user_result'
        entries.append(e)
    for folder in ['cases', 'experiments']:
        for path in sorted((ROOT/folder).glob('[CE][0-9]*.md')):
            content = path.read_text(encoding='utf-8')
            blocks = re.findall(r'```(?:text)?\n(.*?)```',content,re.S)
            if not blocks:
                continue
            prep = re.search(r'## 准备(?:材料|素材)\n(.*?)(?=\n## )',content,re.S)
            template = re.search(r'## 完整中文提示词\n.*?```text\n(.*?)```',content,re.S)
            example = re.search(r'## 拿来就用的具体示例\n.*?```text\n(.*?)```',content,re.S)
            entry = dict(id=path.name.split('-')[0],title=content.splitlines()[0].split('·')[-1].strip(),path=path.relative_to(ROOT).as_posix(),prompt=(template.group(1) if template else blocks[0]).strip(),inputs=prep.group(1).strip() if prep else '请先阅读完整卡片的素材说明。',task='编辑任务',product_category='通用品类',reference='按卡片说明',has_result=False,kind='明确2.5来源' if folder=='cases' else '本库原创设计',variants={})
            if example:
                entry['example'] = example.group(1).strip()
            entries.append(entry)
    metadata = json.loads((ROOT/'data/gallery-metadata.json').read_text(encoding='utf-8'))
    for entry in entries:
        entry.update(metadata.get(entry['id'], {}))
    payload = json.dumps(entries, ensure_ascii=False).replace('<','\\u003c')
    template = (ROOT/'scripts/gallery-template.html').read_text(encoding='utf-8')
    output = ROOT/'browse/index.html'
    output.parent.mkdir(exist_ok=True)
    output.write_text(template.replace('__PROMPT_DATA__',payload),encoding='utf-8',newline='\n')
    print(f'Built gallery: {len(entries)} prompts')

if __name__ == '__main__':
    build()
