#!/usr/bin/env python3
"""
merge_claims.py — fold a duplicate claim page into the claim it duplicates.

    python3 scripts/merge_claims.py <keep> <fold> [<keep> <fold> ...]          # dry run
    python3 scripts/merge_claims.py --apply <keep> <fold>
    python3 scripts/merge_claims.py --apply --pairs pairs.tsv                   # keep<TAB>fold

For each pair, <fold>'s studies join <keep>'s page and <fold> stops existing as a
page but not as a name:

- Each `### ` evidence entry of <fold> whose study <keep> does not already carry
  (same DOI, or same heading) is appended to <keep>'s `## Evidence`. An entry for a
  study both pages carry is not duplicated; <fold>'s subclaims about it are pointed
  at <keep>'s entry instead, since a second finding from one study is still a finding.
- <fold>'s subclaims are appended under <keep>'s `## Subclaims`, their anchors
  rewritten to wherever the study now lives. <fold>'s `## Discussion` is appended as
  one attributed paragraph, and its `## Related Claims` are unioned in.
- <fold>'s file is removed and `update_links_for_renames.py` repoints every link to
  it and records its slug (and any aliases it had) as aliases of <keep>, so a design
  document that cites `research:<fold>` still resolves. That is how
  `patterns/4cid.md` was folded into its long twin (CLAUDE.md, 2026-09-02).

Nothing is invented or re-coded: entries move verbatim, with their q/i/n codes, and
`sync_evidence_codes.py`, `add_evidence_summary.py`, `fix_dead_anchors.py` and
`build_indexes.py` then re-derive the frontmatter, header, anchors and indexes.
Deciding that two claims are one is the editorial act; `link_claims.py` only
proposes pairs.
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402
import page_identity as pid  # noqa: E402

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s)\]>]+", re.I)
SUBCLAIM_LINE = re.compile(r"^`q\S* i\S*`.*$", re.M)
ANCHOR_LINK = re.compile(r"\(#([a-z0-9-]+)\)")


def anchor(heading: str) -> str:
    s = re.sub(r"[^\w\s-]", "", heading.lower(), flags=re.U)
    return re.sub(r"[\s_]+", "-", s.strip()).strip("-")


def sections(body: str) -> list:
    """[(heading or None, text)] at `## ` level, in order."""
    parts, cur, buf = [], None, []
    for line in body.split("\n"):
        if line.startswith("## "):
            parts.append((cur, "\n".join(buf)))
            cur, buf = line[3:].strip(), []
        else:
            buf.append(line)
    parts.append((cur, "\n".join(buf)))
    return parts


def entries(evidence: str) -> list:
    """[(heading, block)] for each `### ` entry."""
    out = []
    for chunk in re.split(r"(?m)^### ", evidence)[1:]:
        heading, _, rest = chunk.partition("\n")
        out.append((heading.strip(), "### " + chunk.rstrip("\n")))
    return out


def study_id(block: str, heading: str) -> str:
    m = DOI_RE.search(block)
    return ("doi:" + m.group(0).rstrip(".,;").lower()) if m else ("h:" + anchor(heading))


def merge_text(keep_text: str, fold_text: str, fold_slug: str, fold_title: str, keep_slug: str) -> str:
    kfm = okf_lib.FRONTMATTER_RE.match(keep_text)
    kprefix = keep_text[:kfm.end()] if kfm else ""
    kbody = keep_text[len(kprefix):]
    _, fbody = okf_lib.split_frontmatter(fold_text)
    ks, fs = sections(kbody), dict(sections(fbody))

    kev = dict(ks).get("Evidence", "")
    have = {study_id(b, h): anchor(h) for h, b in entries(kev)}
    have_anchors = set(have.values())
    moved, remap = [], {}
    for h, b in entries(fs.get("Evidence", "")):
        sid = study_id(b, h)
        if sid in have:
            remap[anchor(h)] = have[sid]
            continue
        a, heading = anchor(h), h
        n = 2
        while a in have_anchors:                  # a different study under the same heading
            heading = f"{h} ({n})"
            a = anchor(heading)
            n += 1
        if heading != h:
            b = b.replace(f"### {h}", f"### {heading}", 1)
        remap[anchor(h)] = a
        have[sid] = a
        have_anchors.add(a)
        moved.append(b)

    subs = []
    for line in SUBCLAIM_LINE.findall(fs.get("Subclaims", "")):
        subs.append(ANCHOR_LINK.sub(lambda m: f"(#{remap.get(m.group(1), m.group(1))})", line))

    fold_disc = (fs.get("Discussion") or "").strip()
    fold_disc = re.sub(r"<!--.*?-->", "", fold_disc, flags=re.S).strip()
    fold_related = [l for l in (fs.get("Related Claims") or "").splitlines()
                    if l.strip().startswith("- [") and f"({keep_slug}.md)" not in l]

    out = []
    for head, text in ks:
        if head is None:
            out.append(text)
            continue
        t = text.rstrip("\n")
        if head == "Subclaims" and subs:
            t = t + "\n\n" + "\n\n".join(s for s in subs if s not in t)
        elif head == "Evidence" and moved:
            t = t + "\n\n" + "\n\n".join(moved)
        elif head == "Discussion" and fold_disc:
            t = t + f"\n\n*Merged from “{fold_title}” ({fold_slug}):* " + fold_disc
        elif head == "Related Claims":
            existing = set(re.findall(r"\]\(([^)]+)\)", t))
            extra = [l for l in fold_related if re.search(r"\]\(([^)]+)\)", l).group(1) not in existing]
            t = "\n".join(l for l in t.split("\n") if f"({fold_slug}.md)" not in l)
            if extra:
                t = t.rstrip("\n") + "\n" + "\n".join(extra)
        out.append(f"## {head}\n\n{t.strip(chr(10))}\n")
    body = out[0].rstrip("\n") + "\n\n" + "\n".join(out[1:])
    return kprefix + body.rstrip("\n") + "\n"


def fold_aliases(fold_text: str) -> list:
    fm, _ = pid.split_fm(fold_text)
    return pid.read_aliases(fm) if fm is not None else []


def merge(keep: str, fold: str, apply: bool) -> str:
    kp, fp = WIKI_ROOT / "claims" / f"{keep}.md", WIKI_ROOT / "claims" / f"{fold}.md"
    if not kp.exists() or not fp.exists() or keep == fold:
        return f"SKIP {keep} <- {fold}: both pages must exist and differ"
    ktext, ftext = kp.read_text(encoding="utf-8"), fp.read_text(encoding="utf-8")
    ffm = okf_lib.parse_frontmatter_scalars(okf_lib.split_frontmatter(ftext)[0])
    merged = merge_text(ktext, ftext, fold, str(ffm.get("title") or fold), keep)
    moved = len(entries(dict(sections(merged)).get("Evidence", ""))) - len(
        entries(dict(sections(ktext)).get("Evidence", "")))
    if not apply:
        return f"would fold {fold} into {keep}: +{moved} evidence entr{'y' if moved == 1 else 'ies'}"
    fm, rest = pid.split_fm(merged)
    for a in fold_aliases(ftext):
        fm = pid.add_alias(fm, a)
    kp.write_text("---\n" + fm + rest, encoding="utf-8")
    fp.unlink()
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as t:
        t.write(f"claims/{fold}.md\tclaims/{keep}.md\n")
    subprocess.run([sys.executable, str(Path(__file__).parent / "update_links_for_renames.py"),
                    "--map", t.name, "--apply"], cwd=WIKI_ROOT, check=True, capture_output=True)
    # <keep>'s own links to <fold> are now links to itself; drop them. A page that
    # linked both now lists <keep> twice; keep the first bullet.
    text = kp.read_text(encoding="utf-8")
    kp.write_text("\n".join(l for l in text.split("\n")
                            if not (l.startswith("- [") and f"]({keep}.md)" in l)), encoding="utf-8")
    for page in (WIKI_ROOT / "claims").glob("*.md"):
        lines = page.read_text(encoding="utf-8").split("\n")
        seen, out, dup = set(), [], False
        for l in lines:
            m = re.match(r"^- \[[^\]]*\]\(([^)]+)\)", l)
            if m and m.group(1) == f"{keep}.md":
                if m.group(1) in seen:
                    dup = True
                    continue
                seen.add(m.group(1))
            out.append(l)
        if dup:
            page.write_text("\n".join(out), encoding="utf-8")
    return f"folded {fold} into {keep}: +{moved} evidence entr{'y' if moved == 1 else 'ies'}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slugs", nargs="*", help="keep fold [keep fold ...]")
    ap.add_argument("--pairs", type=Path, help="file of keep<TAB>fold lines")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    pairs = list(zip(args.slugs[::2], args.slugs[1::2]))
    if args.pairs:
        pairs += [tuple(l.split("\t")[:2]) for l in args.pairs.read_text().splitlines()
                  if l.strip() and not l.startswith("#")]
    for keep, fold in pairs:
        print(merge(keep.strip(), fold.strip(), args.apply))
    if args.apply and pairs:
        for step in (["sync_evidence_codes.py", "--apply"], ["add_evidence_summary.py", "--apply"],
                     ["fix_dead_anchors.py", "--apply"], ["build_indexes.py"]):
            subprocess.run([sys.executable, str(Path(__file__).parent / step[0]), *step[1:]],
                           cwd=WIKI_ROOT, capture_output=True)


if __name__ == "__main__":
    main()
