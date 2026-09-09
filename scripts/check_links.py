"""Check repository-local Markdown file links. No network calls or file writes."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []
checked = 0
for page in root.rglob("*.md"):
    if ".git" in page.parts:
        continue
    content = re.sub(r"```.*?```", "", page.read_text(encoding="utf-8"), flags=re.S)
    for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", content):
        target = match.group(1).strip()
        if target.startswith("<"):
            target = target.split(">", 1)[0][1:]
        else:
            target = target.split(' "', 1)[0]
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        resolved = (page.parent / unquote(parsed.path)).resolve()
        checked += 1
        if not resolved.is_file():
            errors.append(f"{page.relative_to(root)} -> {target}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {checked} local file links checked; heading anchors and remote URLs not checked.")
