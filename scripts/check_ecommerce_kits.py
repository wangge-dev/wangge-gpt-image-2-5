"""Lightweight structural checks for the eight ecommerce workflow packages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KITS = ROOT / "ecommerce" / "kits"
EXPECTED = {"beauty", "apparel", "food", "home", "digital", "appliance", "bags", "baby"}


def image_numbers(text):
    numbers = {int(n) for n in re.findall(r"图(\d+)", text)}
    for start, end in re.findall(r"图(\d+)至图?(\d+)", text):
        numbers.update(range(int(start), int(end) + 1))
    return numbers


def check_kit(path):
    text = path.read_text(encoding="utf-8")
    errors = []
    for required in (
        "## 一次填写：商品事实单",
        "## 选择执行路径",
        "单图最小路径",
        "资料齐全路径",
        "### 只有图1时直接复制",
    ):
        if required not in text:
            errors.append(f"缺少 {required}")

    path_line = next((line for line in text.splitlines() if line.startswith("- 单图最小路径：")), "")
    if "只有图1时直接复制" not in path_line or "不要直接复制第1步" not in path_line:
        errors.append("单图最小路径未明确指向单图正文并避开多图第1步")

    single_section = re.search(
        r"(?ms)^### 只有图1时直接复制\n(.*?)(?=^## 1\.)",
        text,
    )
    if not single_section:
        errors.append("无法解析单图直接复制区")
    else:
        single_blocks = re.findall(r"```text\n(.*?)\n```", single_section.group(1), flags=re.S)
        if len(single_blocks) != 1:
            errors.append(f"单图直接复制区应为1个正文，实际{len(single_blocks)}")
        elif image_numbers(single_blocks[0]) != {1}:
            errors.append(f"单图直接复制区只能引用图1，实际{sorted(image_numbers(single_blocks[0]))}")
        elif "《商品事实单》" not in single_blocks[0]:
            errors.append("单图直接复制区未引用商品事实单")

    steps = re.split(r"(?m)^## (?=\d+\.)", text)[1:]
    if len(steps) != 6:
        errors.append(f"步骤数应为6，实际{len(steps)}")
    for index, step in enumerate(steps, 1):
        for required in ("来源卡：", "输入", "```text", "验收：", "返工："):
            if required not in step:
                errors.append(f"第{index}步缺少{required}")
        blocks = re.findall(r"```text\n(.*?)\n```", step, flags=re.S)
        if len(blocks) != 1:
            errors.append(f"第{index}步直接复制区应为1个，实际{len(blocks)}")
            continue
        if "{{" in blocks[0] or "}}" in blocks[0]:
            errors.append(f"第{index}步直接复制区含未填写变量")
        if "《商品事实单》" not in blocks[0]:
            errors.append(f"第{index}步直接复制区未引用商品事实单")
        source_line = next((line for line in step.splitlines() if line.startswith("来源卡：")), "")
        undeclared = image_numbers(blocks[0]) - image_numbers(source_line)
        if undeclared:
            errors.append(f"第{index}步正文引用未声明图号：{sorted(undeclared)}")
    return errors


def main():
    files = sorted(KITS.glob("*.md"))
    names = {path.stem for path in files}
    errors = []
    if names != EXPECTED:
        errors.append(f"任务包集合不一致：{sorted(names)}")
    for path in files:
        errors.extend(f"{path.name}: {error}" for error in check_kit(path))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(files)} ecommerce kits: 48 steps passed.")


if __name__ == "__main__":
    main()
