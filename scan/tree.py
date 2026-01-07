import os
from pathlib import Path

IGNORE_DIRS = {
    '.git', '.venv', 'venv', 'build', 'dist',
    '__pycache__', '.pytest_cache', '.mypy_cache',
    '.egg-info'
}

IGNORE_SUFFIX = (
    '.bak', '.final', '.semantic', '.final_rewrite'
)

def is_ignored_file(name: str) -> bool:
    return any(name.endswith(s) for s in IGNORE_SUFFIX)

def build_tree(root: str) -> str:
    root = os.path.abspath(root)
    lines = []

    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        level = base.replace(root, '').count(os.sep)
        indent = '  ' * level

        lines.append(f"{indent}{os.path.basename(base) or base}/")

        for f in files:
            if is_ignored_file(f):
                continue
            lines.append(f"{indent}  {f}")

    return "\n".join(lines)
