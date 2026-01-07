from collections import Counter
from pathlib import Path

LANGUAGE_MAP = {
    '.py': 'Python',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.html': 'HTML',
    '.css': 'CSS',
    '.md': 'Markdown',
}

def analyze_repo(root):
    counter = Counter()
    total = 0

    for p in Path(root).rglob("*"):
        if p.is_file():
            lang = LANGUAGE_MAP.get(p.suffix.lower())
            if lang:
                counter[lang] += 1
                total += 1

    return counter, total

def infer_identity(root):
    root = Path(root)
    if (root / "setup.py").exists() and (root / "scan/cli.py").exists():
        return "Python CLI Tool"
    return "Source Code Repository"

def render_summary(root):
    counter, total = analyze_repo(root)
    identity = infer_identity(root)

    lines = [
        "# =============================================",
        "# TSCODESCAN SUMMARY",
        "# =============================================",
        "",
        "Identity:",
        f"- {identity}",
        "",
        "Language Composition:",
    ]

    for lang, cnt in counter.most_common():
        pct = int(cnt / total * 100) if total else 0
        lines.append(f"- {lang:<10}: {cnt} files ({pct}%)")

    return "\n".join(lines)
