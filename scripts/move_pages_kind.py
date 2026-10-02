#!/usr/bin/env python3
"""
move_pages_kind.py — move pages to another kind (folder), keeping every link working.

    python3 scripts/move_pages_kind.py moves.tsv            # report
    python3 scripts/move_pages_kind.py moves.tsv --apply    # move, then repoint

`moves.tsv` is one `<folder>/<slug>\\t<new-folder>` per line (a `#` line is a comment).
A move across kinds is not a rename an alias can carry: ids and aliases are unique per
kind, so `patterns/x` answering as `designs/x` would need an alias in another namespace.
So the inbound links are repointed (`update_links_for_renames.py --map`), and the page's
own same-folder links, which would otherwise point into its new folder, are first made
explicit (`](other.md)` -> `](../patterns/other.md)`).

For each move: `git mv`, `type:` set to the new kind, `id:` set to the slug where the new
kind carries one, and the banner rewritten (`add_type_banner.py`). A move whose target
already exists is refused and reported: that is a merge, not a move. Nothing else in the
page changes; its sections keep their old names, which is a reading for whoever converts it.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
import okf_lib  # noqa: E402
import page_identity as pid  # noqa: E402
from build_wiki_index import KINDS  # noqa: E402

SAME_FOLDER = re.compile(r"\]\((<?)([^)/<>\s#]+\.md)(#[^)>\s]*)?(>?)\)")


def read_moves(path: Path) -> list:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        key, new = line.split("\t")[:2]
        out.append((key.strip(), new.strip()))
    return out


def explicit_links(text: str, old_folder: str) -> str:
    """Same-folder links resolved against the page's old folder, made cross-folder."""
    def fix(m):
        tgt = m.group(2)
        if tgt == "index.md" or not (WIKI_ROOT / old_folder / tgt).exists():
            return m.group(0)
        return f"]({m.group(1)}../{old_folder}/{tgt}{m.group(3) or ''}{m.group(4)})"
    return SAME_FOLDER.sub(fix, text)


def retype(text: str, new_folder: str, slug: str) -> str:
    fm, rest = pid.split_fm(text)
    fm = re.sub(r"(?m)^type: .*$", f"type: {KINDS[new_folder]}", fm, count=1)
    if new_folder in pid.IDENTIFIED_TYPES:
        fm = pid.set_id(fm, slug)
    return "---\n" + fm + rest


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("moves", type=Path)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    done, refused = [], []
    for key, new in read_moves(a.moves):
        old_folder, slug = key.split("/", 1)
        src, dst = WIKI_ROOT / f"{key}.md", WIKI_ROOT / new / f"{slug}.md"
        if new not in okf_lib.CONTENT_FOLDERS or new == old_folder:
            refused.append((key, new, "not a content folder, or the same one"))
        elif not src.exists():
            refused.append((key, new, "no such page"))
        elif dst.exists():
            refused.append((key, new, f"{new}/{slug}.md exists: a merge, not a move"))
        else:
            done.append((key, new))
    for key, new, why in refused:
        print(f"  refused {key} -> {new}: {why}")
    print(f"{len(done)} move(s), {len(refused)} refused")
    if not a.apply or not done:
        return
    rename_map = WIKI_ROOT / ".cache" / "kind-moves.tsv"
    rename_map.parent.mkdir(exist_ok=True)
    lines = []
    # every page's same-folder links are made explicit before any page moves, so a link
    # between two moving pages still names where its target was
    for key, new in done:
        src = WIKI_ROOT / f"{key}.md"
        src.write_text(explicit_links(src.read_text(encoding="utf-8"), key.split("/", 1)[0]), encoding="utf-8")
    for key, new in done:
        old_folder, slug = key.split("/", 1)
        subprocess.run(["git", "mv", f"{key}.md", f"{new}/{slug}.md"], cwd=WIKI_ROOT, check=True)
        dst = WIKI_ROOT / new / f"{slug}.md"
        dst.write_text(retype(dst.read_text(encoding="utf-8"), new, slug), encoding="utf-8")
        lines.append(f"{key}.md\t{new}/{slug}.md")
    rename_map.write_text("\n".join(lines) + "\n", encoding="utf-8")
    py = sys.executable
    subprocess.run([py, "scripts/update_links_for_renames.py", "--map", str(rename_map), "--apply"],
                   cwd=WIKI_ROOT, check=True, stdout=subprocess.DEVNULL)
    subprocess.run([py, "scripts/add_type_banner.py", "--apply"], cwd=WIKI_ROOT, check=True,
                   stdout=subprocess.DEVNULL)
    print("moved; now run build_indexes.py and lint.py")


if __name__ == "__main__":
    main()
