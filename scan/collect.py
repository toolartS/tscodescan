import os
from pathlib import Path

IGNORE_DIRS = {
    '.git', '.venv', 'venv', 'build', 'dist',
    '__pycache__', '.pytest_cache', '.mypy_cache',
    '.egg-info'
}

BINARY_EXTS = {
    '.zip', '.tar', '.gz', '.whl', '.exe', '.apk', '.bin'
}

SOURCE_EXTS = {
    '.py', '.js', '.ts', '.html', '.css', '.md',
    '.sh', '.json', '.yaml', '.yml', '.toml', '.ini'
}

def collect_files(root: str, raw: bool = False):
    files = []
    root = Path(root)

    for base, dirs, fs in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for f in fs:
            p = Path(base) / f
            if p.suffix.lower() in BINARY_EXTS:
                continue
            if not raw and p.suffix.lower() not in SOURCE_EXTS:
                continue
            files.append(p)

    return files
