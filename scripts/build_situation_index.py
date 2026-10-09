#!/usr/bin/env python3
"""
build_situation_index.py — what changes for which learners, goals and settings, across pages.

A converted principle or pattern carries `## Fitting the design to a situation`: the
facts that most change the decision, each with the question to ask when a brief omits
it, and a table `| If the brief says… | Then change… | Basis |` whose rows name the
situation with tags from evidence-dimensions.json (`novice`, `online-self-paced`,
`procedure`, `workplace-clinical`, ...). That table is the design guidance a learner
and context analysis needs, but it lived only inside its page: a designer with novices
in a self-paced course could not ask which pages say what to change for them. The
scale test of 2026-10-09 found no search reaching it (no converted page in the top
five for ten learner-analysis queries).

This collects every row, keyed by tag, so the MCP server's `situations` tool and the
site's "Design for a situation" pages can answer that question from all pages at once.
It writes nothing on any page: the tables stay where they are written, and this file is
derived from them like wiki-index.json.

Each row keeps its three cells as written, with links made bundle-relative
(`claims/x.md`), the tags in its first cell, each tag's field in evidence-dimensions.json,
the claims its basis links with their markers, and `basis`: `claim` when the basis cites
a claim and does not open with "untested", `untested` when it says so, else `other`. A
row whose basis carries a claim to learners or settings it did not test says so in its
own words; that wording is kept, never summarised into the flag.

    python3 scripts/build_situation_index.py            # write situation-index.json
    python3 scripts/build_situation_index.py --check    # is the committed copy current?
    python3 scripts/build_situation_index.py --tags     # the tag vocabulary, with counts
"""

import argparse
import posixpath
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402
import evidence_dimensions as ed  # noqa: E402

WIKI_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = WIKI_ROOT / "situation-index.json"
FOLDERS = ("principles", "patterns", "elements", "designs")
HEADING = "## Fitting the design to a situation"
# The evidence-dimensions fields a situation row is written in, in the order a designer
# analyses them: learners, then the goal, then the setting.
FIELDS = ("expertise", "age", "population_band", "knowledge_type", "element_interactivity",
          "setting", "duration")
GROUPS = {"expertise": "learners", "age": "learners", "population_band": "learners",
          "knowledge_type": "goal", "element_interactivity": "goal",
          "setting": "context", "duration": "context"}

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_SECTION = re.compile(r"^## Fitting the design to a situation[^\n]*\n(.*?)(?=^## |\Z)", re.S | re.M)
_TAG = re.compile(r"`([a-z0-9][a-z0-9-]*)`")
_LINK = re.compile(r"\[([^\]]*)\]\((<[^>]+>|[^()\s]*(?:\([^()\s]*\)[^()\s]*)*)\)(\s*\[([+~\-X])([SMW]?)\])?")
_FACT = re.compile(r"^- \*\*(.+?)\*\*\s*(.*)$")

# Most rows (690 of 1,117 on 2026-10-09) name their situation in words, not tags: "Time is
# one session only", "Adults in work settings", "One teacher, a large class". These read a
# controlled value from such wording in the row's first cell, kept apart from the written
# tags as `inferred_tags`. Each was checked against the rows it matches; patterns that also
# caught the facilitator ("scarce adult time") or the teacher ("an inexperienced teacher")
# rather than the learners were left out, so `advanced` is never inferred.
INFERRED = {
    "single-session": r"\b(one|single) (session|sitting|lesson|visit|workshop)\b|\bone-off\b",
    "workplace-clinical": r"\bworkplace|\bwork settings?\b|\bclinical\b|\bon the job\b",
    "classroom": r"\bone teacher\b|\blarge class\b|\bwhole class\b",
    "online-self-paced": r"self-paced|\bno (live )?teacher present\b|\bno live (teacher|instructor)\b",
    "online-instructor-led": r"\blive online\b|\bvideo call|\bsynchronous online\b|\bwebinar",
    "novice": r"\bnovices?\b|\bbeginners?\b|\bno prior (knowledge|experience)\b",
    "child": r"\bchildren\b|\bprimary age\b|\bearly years\b|\bkindergarten\b",
    "adult": r"\badult learners\b|^adults\b",
}
_INFERRED = {tag: re.compile(p, re.I) for tag, p in INFERRED.items()}


def tag_vocabulary() -> dict:
    """{tag: {field, group, meaning}} from evidence-dimensions.json. A value two fields
    share ("mixed", "?") is left out: in a brief's first cell it says nothing."""
    seen, vocab = {}, {}
    for field in FIELDS:
        for value, meaning in ed.values(field).items():
            seen.setdefault(value, []).append((field, meaning))
    for value, owners in seen.items():
        if len(owners) == 1:
            field, meaning = owners[0]
            vocab[value] = {"field": field, "group": GROUPS[field], "meaning": meaning}
    return vocab


def _split_row(line: str) -> list:
    """The cells of a markdown table row; a `|` inside a link or code span is kept."""
    cells, buf, depth, code = [], "", 0, False
    for ch in line.strip().strip("|"):
        if ch == "`":
            code = not code
        elif not code and ch in "[(":
            depth += 1
        elif not code and ch in "])":
            depth = max(0, depth - 1)
        if ch == "|" and not code and depth == 0:
            cells.append(buf.strip())
            buf = ""
        else:
            buf += ch
    cells.append(buf.strip())
    return cells


def _bundle(text: str, folder: str) -> str:
    """Every relative link in `text` rewritten to a bundle path (`claims/x.md`)."""
    def fix(m):
        label, dest = m.group(1), m.group(2)
        raw = dest[1:-1] if dest.startswith("<") else dest
        if re.match(r"^[a-z]+:", raw) or raw.startswith("#"):
            return m.group(0)
        path, _, anchor = raw.partition("#")
        target = posixpath.normpath(posixpath.join(folder, path)) if path else ""
        new = target + (f"#{anchor}" if anchor else "")
        new = f"<{new}>" if dest.startswith("<") or "(" in new else new
        return f"[{label}]({new})" + (m.group(3) or "")
    return _LINK.sub(fix, text)


def _claims(basis: str) -> list:
    out = []
    for m in _LINK.finditer(basis):
        dest = m.group(2).strip("<>").partition("#")[0]
        if dest.startswith("claims/") and dest.endswith(".md"):
            claim = {"id": dest[len("claims/"):-3]}
            if m.group(4):
                claim["marker"] = m.group(4) + (m.group(5) or "")
            if claim not in out:
                out.append(claim)
    return out


def parse_page(path: Path, vocab: dict) -> tuple:
    """(page record, rows) for one page, or (None, []) when it has no situation table."""
    text = path.read_text(encoding="utf-8")
    if HEADING not in text:
        return None, []
    folder = path.parent.name
    body = _COMMENT.sub("", text)
    m = _SECTION.search(body)
    if not m:
        return None, []
    fm = okf_lib.parse_frontmatter_scalars(okf_lib.split_frontmatter(text)[0])
    key = f"{folder}/{path.stem}"
    facts, rows = [], []
    for line in m.group(1).splitlines():
        fact = _FACT.match(line)
        if fact and not line.startswith("| "):
            head, rest = fact.group(1).rstrip("."), fact.group(2)
            why, _, ask = rest.partition("If unstated, ask:")
            facts.append({"fact": head, "why": _bundle(why.strip(), folder), "ask": ask.strip()})
            continue
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| If the brief"):
            continue
        cells = _split_row(line)
        if len(cells) < 3:
            continue
        when, change, basis = (_bundle(c, folder) for c in cells[:3])
        tags = [t for t in dict.fromkeys(_TAG.findall(cells[0])) if t in vocab]
        inferred = [t for t, rx in _INFERRED.items() if t in vocab and t not in tags and rx.search(cells[0])]
        claims = _claims(basis)
        kind = ("untested" if basis.lower().lstrip("*_ ").startswith("untested")
                else "claim" if claims else "other")
        rows.append({"page": key, "if": when, "change": change, "basis": basis,
                     "basis_kind": kind, "tags": tags, "inferred_tags": inferred, "claims": claims})
    page = {"title": str(fm.get("title") or path.stem), "type": str(fm.get("type") or ""),
            "facts": facts, "rows": len(rows)}
    return page, rows


def build(root: Path = WIKI_ROOT) -> dict:
    vocab = tag_vocabulary()
    pages, rows = {}, []
    for folder in FOLDERS:
        for path in sorted((root / folder).glob("*.md")):
            if path.stem == "index":
                continue
            page, page_rows = parse_page(path, vocab)
            if page:
                pages[f"{folder}/{path.stem}"] = page
                rows.extend(page_rows)
    tags = {}
    for tag, spec in vocab.items():
        hits = [r for r in rows if tag in r["tags"] or tag in r["inferred_tags"]]
        if hits:
            tags[tag] = dict(spec, rows=len(hits), pages=len({r["page"] for r in hits}),
                             inferred=sum(tag in r["inferred_tags"] for r in hits),
                             with_claim=sum(r["basis_kind"] == "claim" for r in hits))
    return {
        "note": ("Rows of every page's 'Fitting the design to a situation' table, keyed by the "
                 "evidence-dimensions.json tags in their first cell. Generated by "
                 "scripts/build_situation_index.py; do not edit."),
        "fields": {f: GROUPS[f] for f in FIELDS},
        "tags": tags,
        "pages": pages,
        "rows": rows,
    }


def render(index: dict) -> str:
    return okf_lib.dump_json_records(index, depth=2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the committed situation-index.json is not what a rebuild would produce")
    ap.add_argument("--tags", action="store_true", help="print the tag vocabulary with counts")
    args = ap.parse_args()
    index = build()
    if args.tags:
        for tag, t in sorted(index["tags"].items(), key=lambda kv: (kv[1]["group"], -kv[1]["rows"])):
            print(f"{t['group']:9} {t['field']:22} {tag:24} rows {t['rows']:4}  pages {t['pages']:3}  "
                  f"with a claim {t['with_claim']:4}")
        return
    text = render(index)
    if args.check:
        current = OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.exists() else ""
        if current != text:
            print(f"{OUT_PATH.name} is stale — run python3 scripts/build_situation_index.py", file=sys.stderr)
            sys.exit(1)
        print(f"{OUT_PATH.name} is current ({len(index['rows'])} rows, {len(index['pages'])} pages)")
        return
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {OUT_PATH.name}: {len(index['rows'])} rows from {len(index['pages'])} pages, "
          f"{len(index['tags'])} tags")


if __name__ == "__main__":
    main()
