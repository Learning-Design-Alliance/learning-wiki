#!/usr/bin/env python3
"""
remove_pages.py — take pages out of the wiki, and every link to them out of the pages that
point at them.

Written for the descriptive-context claims (maintainer, 2026-10-13: "Context claims are only
useful as filters on evidence, not evidence by itself"). A claim such as "Hispanic graduation
rates at study institutions rose 3.5 points" tests no design variable; the population and
setting it describes are already coded on the evidence entries of design claims, where they
filter that evidence. git history keeps every removed page.

A bullet that is nothing but a link to a removed page (with its marker) is dropped; a link in
running prose keeps its text and loses the link. Nothing else on the linking page changes.
Every removal is written to the log file named by --log, one JSON line per page, with the
reason given.

    python3 scripts/remove_pages.py --list removals.txt --reason "descriptive context" --dry-run
    python3 scripts/remove_pages.py --list removals.txt --reason "descriptive context" --apply
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402

LINK = re.compile(r"\[([^\]]*)\]\(<?([^)>\s#]+\.md)(#[^)>\s]*)?>?\)")
BARE_BULLET = re.compile(r"^\s*[-*]\s*(?:\*\*)?\[[^\]]*\]\([^)]*\)(?:\*\*)?\s*(?:\[[+~\-X][SMW]?\])?\s*$")


def inbound(keys: set) -> dict:
    """{linking page path: [removed keys it links to]}, from the reverse index built now. The committed
    copy lags any edit since the last build_indexes.py (2026-10-14: two links written by a batch's
    settle step were missed), so it is rebuilt from disk."""
    sys.path.insert(0, str(Path(__file__).parent))
    import build_reverse_index
    rev = build_reverse_index.build()["edges"]
    out = {}
    for key in keys:
        kind, slug = key.split("/", 1)
        for folder, slugs in (rev.get(kind, {}).get(slug) or {}).items():
            for s in slugs:
                s = s if isinstance(s, str) else s.get("slug") or s.get("id")
                src = f"{folder}/{s}"
                if src not in keys:
                    out.setdefault(WIKI_ROOT / folder / f"{s}.md", []).append(key)
    return out


def strip_links(path: Path, gone: set) -> int:
    """Remove links from `path` to any page in `gone` (keys like claims/<slug>). Returns the
    number of links removed."""
    text = path.read_text(encoding="utf-8")
    root = WIKI_ROOT.resolve()

    def target(href: str):
        try:
            return str((path.parent / unquote(href)).resolve().relative_to(root).with_suffix(""))
        except ValueError:
            return None

    removed = 0
    lines = []
    for line in text.split("\n"):
        hits = [m for m in LINK.finditer(line) if target(m.group(2)) in gone]
        if not hits:
            lines.append(line)
            continue
        removed += len(hits)
        if BARE_BULLET.match(line):
            continue
        lines.append(LINK.sub(lambda m: m.group(1) if target(m.group(2)) in gone else m.group(0), line))
    if removed:
        path.write_text("\n".join(lines), encoding="utf-8")
    return removed


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", required=True, help="file of <folder>/<slug> keys, one per line")
    ap.add_argument("--reason", required=True)
    ap.add_argument("--log", default=str(WIKI_ROOT / "eval" / "removed" / "pages.ndjson"))
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    keys = {l.strip().removesuffix(".md") for l in Path(args.list).read_text(encoding="utf-8").splitlines()
            if l.strip()}
    missing = sorted(k for k in keys if not (WIKI_ROOT / f"{k}.md").exists())
    keys -= set(missing)
    links = inbound(keys)
    print(f"{len(keys)} page(s) to remove ({len(missing)} already gone); "
          f"{sum(len(v) for v in links.values())} link(s) on {len(links)} other page(s)")
    if args.dry_run:
        return
    stripped = sum(strip_links(p, keys) for p in links if p.exists())
    log = Path(args.log)
    log.parent.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    with log.open("a", encoding="utf-8") as fh:
        for k in sorted(keys):
            fm_lines, _ = okf_lib.split_frontmatter((WIKI_ROOT / f"{k}.md").read_text(encoding="utf-8"))
            title = okf_lib.parse_frontmatter_scalars(fm_lines).get("title")
            fh.write(json.dumps({"page": k, "title": title, "removed_at": today, "reason": args.reason}) + "\n")
            (WIKI_ROOT / f"{k}.md").unlink()
    print(f"removed {len(keys)} page(s); {stripped} link(s) taken out; log -> {log}")


if __name__ == "__main__":
    main()
