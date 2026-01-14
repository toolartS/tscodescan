from collections import Counter
from pathlib import Path

IGNORE_DIRS = {
    '.git', '.venv', 'venv', 'build', 'dist',
    '__pycache__', '.pytest_cache', '.mypy_cache',
    '.egg-info'
}

def analyze_repo(root: str):
    counter = Counter()
    root = Path(root)

    for p in root.rglob("*"):
        if not p.is_file():
            continue

        if any(part in IGNORE_DIRS for part in p.parts):
            continue

        ext = p.suffix.lower() or "<noext>"
        counter[ext] += 1

    return counter

def render_summary(root: str) -> str:
    counter = analyze_repo(root)
    total = sum(counter.values())

    lines = [
        "# =============================================",
        "# TSCODESCAN SUMMARY",
        "# =============================================",
        "",
        f"Total files: {total}",
        "",
        "File Extensions:",
    ]

    for ext in sorted(counter):
        lines.append(f"- {ext}: {counter[ext]}")

    return "\n".join(lines)
