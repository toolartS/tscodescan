import argparse, os
from pathlib import Path

from scan.tree import build_tree
from scan.summary import render_summary
from scan.diagnose import diagnose_repo
from scan.collect import collect_files
from scan.artifact import write_artifact

def main():
    p = argparse.ArgumentParser("tsc")
    p.add_argument("path", nargs="?", default=".")
    p.add_argument("-i", nargs="?", const=True)
    p.add_argument("-r", action="store_true")
    p.add_argument("--web", help="scan visible text from web url")

    args = p.parse_args()

    root = os.path.abspath(args.path)
    repo = os.path.basename(root)

    tree = build_tree(root)
    summary = render_summary(root)
    diagnose = diagnose_repo(root)

    if args.web:
        from scan.web.orchestrator import scan_web_text
        text = scan_web_text(args.web, args.web_from)

        if not args.i:
            print(text)
            return

        repo = args.web.replace("://", "_").replace("/", "_")

        write_artifact(
            root="WEB",
            repo=repo,
            tree="(web)",
            summary="WEB TEXT SNAPSHOT",
            diagnose="N/A",
            files=[],
            raw=False,
            idtag=args.i if args.i is not True else None
        )
        return

    if not args.i:
        print(tree)
        print()
        print(summary)
        print()
        print("DIAGNOSE:")
        print(diagnose)
        return

    files = collect_files(root, raw=args.r)
    idtag = None if args.i is True else args.i
    write_artifact(root, repo, tree, summary, diagnose, files, args.r, idtag)

if __name__ == "__main__":
    main()
