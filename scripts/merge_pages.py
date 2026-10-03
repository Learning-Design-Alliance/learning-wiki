#!/usr/bin/env python3
"""
merge_pages.py — fold a duplicate page into the page it duplicates, within one kind
(principles, patterns, elements, strategies, ...). The claims version is merge_claims.py.

    python3 scripts/merge_pages.py patterns keep fold [keep fold ...]       # dry run
    python3 scripts/merge_pages.py patterns --apply --pairs pairs.tsv       # keep<TAB>fold

For each pair:

- Every bullet of <fold> that <keep> lacks joins <keep>'s section of the same name
  (Requirements, Constraints, Claims, Related ..., Examples, Key Sources, ...). A bullet is
  already there when its text is, or when every page it links is already linked in that
  section. A claim-link bullet with no matching section joins <keep>'s
  `## Further evidence, not yet read against this model` (a converted page) or its
  `### Claims`, so every claim <fold> cited stays cited, with its marker, live.
- <fold>'s `sources:` entries whose id <keep> lacks are appended to <keep>'s frontmatter.
- <fold>'s whole body is kept verbatim in a `<!-- merged ... -->` block at the end of
  <keep>, so nothing is lost, and links inside it count for nothing (CLAUDE.md, 2026-10-02).
- <fold>'s file is removed and `update_links_for_renames.py` repoints every link to it and
  records its slug (and its aliases) as aliases of <keep>.

Deciding that two pages are one, and which survives, is the editorial act; the triage
table (`eval/page-triage/`) only proposes pairs.
"""
import argparse
import datetime
import re
import subprocess
import sys
import tempfile
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
import okf_lib  # noqa: E402
import page_identity as pid  # noqa: E402

HEAD = re.compile(r"^(#{2,4}) +(.+?)\s*$")
LINK = re.compile(r"\]\(<?([^)>\s#]+\.md)")
BULLET = re.compile(r"^(?:[-*] |\d+\. )")
COMMENT = re.compile(r"<!--.*?-->", re.S)
FURTHER = "## Further evidence, not yet read against this model"
TAIL = ("Related ", "Examples", "Key Sources", "Impact")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\[[+~-][SMW]\]|\[X\]", "", s)).strip().lower()


def parse(body: str) -> list:
    """[(heading_name or None, [lines])], heading lines included in each block."""
    blocks, name, cur = [], None, []
    for line in body.split("\n"):
        m = HEAD.match(line)
        if m:
            blocks.append((name, cur))
            name, cur = m.group(2).strip(), [line]
        else:
            cur.append(line)
    blocks.append((name, cur))
    return blocks


def bullets(lines: list) -> list:
    return [l for l in lines if BULLET.match(l) and l.strip() not in ("-", "1.")]


def has(lines: list, bullet: str, page_links: set) -> bool:
    text = norm(bullet)
    if any(norm(l) == text for l in lines):
        return True
    targets = {Path(t).name for t in LINK.findall(bullet)}
    here = {Path(t).name for l in lines for t in LINK.findall(l)}
    if targets and "claims" in bullet and targets <= page_links:
        return True                     # the claim is cited elsewhere on the page already
    return bool(targets) and targets <= here


def extend(lines: list, bullet: str) -> bool:
    """Replace a bullet of <keep> that <fold>'s bullet extends (`**Head**` against
    `**Head**: why`), which loses nothing; True when it did."""
    b = norm(bullet)
    for i, l in enumerate(lines):
        if BULLET.match(l) and norm(l) and b.startswith(norm(l)):
            lines[i] = bullet
            return True
    return False


def covered(lines: list, bullet: str) -> bool:
    """A bullet of <keep> already says it, or says more (fold's text is its prefix)."""
    b = norm(bullet)
    return any(BULLET.match(l) and norm(l).startswith(b) for l in lines)


def insert(blocks: list, idx: int, new: list) -> None:
    name, lines = blocks[idx]
    end = len(lines)
    while end > 1 and not lines[end - 1].strip():
        end -= 1
    lines[end:end] = new


def merge_body(kbody: str, fbody: str, keep_slug: str, fold_slug: str) -> tuple:
    # only <keep>'s live sections take bullets; a trailing deprecated or merged block
    # (which repeats the old section names) is carried over untouched
    m = re.search(r"(?m)^<!-- (?:deprecated|merged)", kbody)
    kbody, trailer = (kbody[:m.start()], kbody[m.start():]) if m else (kbody, "")
    kb = parse(kbody)
    fb = parse(COMMENT.sub("", fbody))
    live_links = lambda: {Path(t).name for _, ls in kb for l in ls for t in LINK.findall(COMMENT.sub("", l))}
    moved = 0
    converted = any(n == FURTHER[3:] for n, _ in kb)
    for name, lines in fb:
        if name is None:
            continue
        for b in bullets(lines):
            if re.match(r"\d+\. ", b):
                continue                # a numbered sequence is not merged line by line
            if f"]({keep_slug}.md" in b or f"]({fold_slug}.md" in b:
                continue                # a link to either page of the pair
            idx = next((i for i, (n, _) in enumerate(kb) if n == name), None)
            if idx is None or (converted and "../claims/" in b and not name.startswith(TAIL)):
                if "../claims/" not in b:
                    continue            # kept in the merged block only
                target = FURTHER[3:] if converted else "Claims"
                idx = next((i for i, (n, _) in enumerate(kb) if n == target), None)
                if idx is None:
                    tail = next((i for i, (n, _) in enumerate(kb) if n and n.startswith(TAIL)), len(kb))
                    head = FURTHER if converted else "### Claims"
                    kb.insert(tail, (head.lstrip("# "), [head, ""]))
                    idx = tail
            if has(kb[idx][1], b, live_links()) or covered(kb[idx][1], b):
                continue
            if not extend(kb[idx][1], b):
                insert(kb, idx, [b])
            moved += 1
    out = "\n".join(l for _, ls in kb for l in ls)
    if trailer:
        out = out.rstrip() + "\n\n" + trailer
    return out, moved


def merge_sources(kfm: str, ffm: str) -> str:
    fm_items = re.search(r"(?m)^sources:\n((?:  .*\n)+)", ffm + "\n")
    if not fm_items:
        return kfm
    items = re.split(r"(?m)^(?=  - )", fm_items.group(1))
    have = set(re.findall(r"(?m)^  - id: (\S+)", kfm))
    new = [i.rstrip("\n") for i in items if i.strip() and re.match(r"  - id: (\S+)", i)
           and re.match(r"  - id: (\S+)", i).group(1) not in have]
    if not new:
        return kfm
    m = re.search(r"(?m)^sources:\n((?:  .*\n)+)", kfm + "\n")
    if m:
        block = m.group(0).rstrip("\n")
        return kfm.replace(block, block + "\n" + "\n".join(new), 1)  # block is followed by its own newline
    return kfm.rstrip("\n") + "\nsources:\n" + "\n".join(new) + ("\n" if kfm.endswith("\n") else "")


def merge(kind: str, keep: str, fold: str, apply: bool) -> str:
    # <fold> may name another kind (`patterns/cognitive-load-theory` folded into a theory):
    # a misfiled page whose right kind already has the page. No alias can cross kinds, so
    # its links are repointed and its slug is not recorded on <keep>.
    fold_kind, fold = fold.split("/", 1) if "/" in fold else (kind, fold)
    cross = fold_kind != kind
    kp, fp = WIKI_ROOT / kind / f"{keep}.md", WIKI_ROOT / fold_kind / f"{fold}.md"
    if not kp.exists() or not fp.exists() or (keep == fold and not cross):
        return f"SKIP {keep} <- {fold}: both pages must exist and differ"
    ktext, ftext = kp.read_text(encoding="utf-8"), fp.read_text(encoding="utf-8")
    if cross:
        from move_pages_kind import explicit_links
        ftext = explicit_links(ftext, fold_kind)   # its same-folder links, made to resolve from <keep>
    kfm, kbody = pid.split_fm(ktext)
    ffm, fbody = pid.split_fm(ftext)
    body, moved = merge_body(kbody, fbody, keep, fold)
    fold_title = okf_lib.parse_frontmatter_scalars(okf_lib.split_frontmatter(ftext)[0]).get("title") or fold
    kept = re.sub(r"^\s*---\s*\n", "", fbody).strip()
    kept = kept.replace("<!--", "<!- -").replace("-->", "- ->")
    body = (body.rstrip() + f"\n\n<!-- merged {datetime.date.today().isoformat()} from {fold_kind}/{fold} (\"{fold_title}\"), "
            f"{'misfiled as a ' + fold_kind[:-1] + ' and' if cross else ''} a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.\n\n{kept}\n-->\n")
    fm = merge_sources(kfm, ffm)
    for a in ([] if cross else pid.read_aliases(ffm)):
        fm = pid.add_alias(fm, a)
    if not apply:
        return f"would fold {fold_kind}/{fold} into {kind}/{keep}: +{moved} bullet(s)"
    kp.write_text("---\n" + fm + body, encoding="utf-8")
    fp.unlink()
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as t:
        t.write(f"{fold_kind}/{fold}.md\t{kind}/{keep}.md\n")
    subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "update_links_for_renames.py"),
                    "--map", t.name, "--apply"], cwd=WIKI_ROOT, check=True, capture_output=True)
    dedupe(kind, keep)
    if cross:
        # update_links_for_renames records an alias for a same-slug move only when kinds match;
        # make sure no alias for the other kind's slug landed on <keep>.
        text = kp.read_text(encoding="utf-8")
        kfm2, rest = pid.split_fm(text)
        if fold in pid.read_aliases(kfm2) and fold not in pid.read_aliases(kfm):
            print(f"  note: {kind}/{keep} gained alias {fold!r} from the cross-kind map; check it")
    return f"folded {fold_kind}/{fold} into {kind}/{keep}: +{moved} bullet(s)"


def dedupe(kind: str, keep: str) -> None:
    """<keep>'s own links to itself go; a page now listing <keep> twice in one section keeps
    the first bullet. Only bullets whose sole link is <keep> are touched."""
    for page in WIKI_ROOT.glob("*/*.md"):
        if page.parent.name not in okf_lib.CONTENT_FOLDERS:
            continue
        text = page.read_text(encoding="utf-8")
        if f"{keep}.md" not in text:
            continue
        own = page == WIKI_ROOT / kind / f"{keep}.md"
        target = f"{keep}.md" if page.parent.name == kind else f"../{kind}/{keep}.md"
        out, seen, changed, in_comment = [], set(), False, False
        for line in text.split("\n"):
            in_comment = (in_comment or "<!--" in line) and "-->" not in line
            if HEAD.match(line):
                seen = set()
            links = LINK.findall(line)
            if not in_comment and BULLET.match(line) and links == [target]:
                if own or target in seen:
                    changed = True
                    continue
                seen.add(target)
            out.append(line)
        if changed:
            page.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind")
    ap.add_argument("slugs", nargs="*", help="keep fold [keep fold ...]")
    ap.add_argument("--pairs", type=Path, help="file of keep<TAB>fold lines")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    pairs = list(zip(a.slugs[::2], a.slugs[1::2]))
    if a.pairs:
        pairs += [tuple(x.strip() for x in l.split("\t")[:2]) for l in a.pairs.read_text().splitlines()
                  if l.strip() and not l.startswith("#")]
    for keep, fold in pairs:
        print(merge(a.kind, keep, fold, a.apply))
    if a.apply and pairs:
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "build_indexes.py")], cwd=WIKI_ROOT,
                       capture_output=True)


if __name__ == "__main__":
    main()
