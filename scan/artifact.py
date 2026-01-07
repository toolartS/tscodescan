import datetime
from pathlib import Path

def write_artifact(root, repo, tree, summary, diagnose, files, raw, idtag):
    outdir = Path.home() / "storage" / "downloads" / "Scan" / repo
    outdir.mkdir(parents=True, exist_ok=True)

    name = "scan"
    if raw:
        name += "-raw"
    if idtag:
        name += f"-{idtag}"
    name += f"-{repo}.txt"

    out = outdir / name

    with out.open("w", errors="ignore") as o:
        o.write("========================================\n")
        o.write(f"ARTIFACT: {repo}\n")
        o.write(f"GENERATED: {datetime.datetime.now()}\n")
        o.write("========================================\n\n")

        o.write("TREE\n----\n")
        o.write(tree + "\n\n")

        o.write(summary + "\n\n")

        o.write("DIAGNOSE\n--------\n")
        o.write(diagnose + "\n\n")

        o.write("CONTEXT (SOURCE)\n----------------\n")
        for f in files:
            o.write(f"\n=== {f.relative_to(root)} ===\n")
            try:
                o.write(f.read_text(errors="ignore"))
            except:
                o.write("[READ ERROR]\n")

    print(f"[OK] Artifact created: {out}")
