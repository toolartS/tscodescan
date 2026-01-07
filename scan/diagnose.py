from pathlib import Path

def human_size(n: int) -> str:
    for unit in ['B','KB','MB','GB','TB']:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} PB"

def diagnose_repo(root: str) -> str:
    root = Path(root)
    out = []

    if (root / ".git").exists():
        out.append("✔ Git repository detected")
    else:
        out.append("✖ Not a git repository")

    for d in ['build','dist','.venv','.git']:
        if (root / d).exists():
            out.append(f"⚠ Noise: {d}")

    size = sum(
        f.stat().st_size
        for f in root.rglob("*")
        if f.is_file()
    )
    out.append(f"Repo size: {human_size(size)}")

    return "\n".join(out)
