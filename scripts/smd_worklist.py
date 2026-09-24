#!/usr/bin/env python3
"""
smd_worklist.py — which WWC and Evidence for ESSA reviews to extract next.

CLAUDE.md sets the extraction target as depth on ONE scale: 30 studies whose
effects sit on the standardised-mean-difference axis, because that is the axis
What Works Clearinghouse and Evidence for ESSA already report on. Both publish
their reviews as pages with a fixed format, and the Renaissance AI and
Education Resource Hub (github.com/jchoi92k/Learning-Engineering-Resource-Hub)
has already catalogued a few hundred of those pages. This turns that catalogue
into a ranked worklist.

What it does NOT do, each on purpose:

- **It stores nothing from the hub.** It reads the hub's published `data.json`
  at run time (or a local copy, `--hub`) and prints to stdout. That repo carries
  no licence yet, so its data does not get committed here. If you want the
  output on disk, write it under `eval/` (gitignored).
- **It copies no description.** The hub's descriptions are partly model-written
  (its own `description_source` says `llm-summary` on most WWC rows), and some
  quote an effect size. An effect size read off a summary of a summary is how
  the fabrications this repo has catalogued get in. The worklist says which page
  to read; the numbers come from the page itself.
- **It does not rank by the review's verdict.** "No discernible effects" and a
  Tier 1 rating are equally good candidates: a null result measured on the SMD
  axis is part of the family, and dropping nulls is publication bias built into
  a worklist.
- **It does not assert that any single page reports a d or g.** `tier` records
  the *format* the publisher documents for that kind of page, and `basis` says
  so. Confirm on the page before writing a record.

Ranking, by columns printed rather than one opaque score:

1. `tier` — `smd` for WWC intervention reports and ESSA program pages (both
   report standardised effect sizes by design); `pointer` for WWC practice
   guides, which carry recommendations and point to studies rather than
   reporting an estimate of their own.
2. `cited` — wiki pages that already link to this exact URL. A record for a
   source the wiki cites is reusable at once, the same "rank by reuse" rule as
   `citation_worklist.py`.
3. `both` — the programme has a review in both WWC and ESSA. Two independent
   reviews of one intervention can be checked against each other.
4. `named` — wiki pages that mention the programme by name: a whole-word,
   CASE-SENSITIVE phrase match on the name as the publisher capitalises it, and
   on its acronym if it has one. Case-insensitive matching was tried and counted
   "second step" and "pathway" in ordinary prose as the programmes Second Step
   and Pathway. It is still a phrase match, not a verified join — "Culturally
   Responsive Classroom" contains "Responsive Classroom" — so it ranks last, and
   `--program` shows which pages matched before anyone trusts the count.

Rows already recorded (the URL appears in `observations/`) or already reviewed
(in `sources/manifest.ndjson`) drop out unless `--all` is passed, so the list
shrinks as you work.

    python3 scripts/smd_worklist.py                    # top 40, markdown table
    python3 scripts/smd_worklist.py --limit 0          # every row
    python3 scripts/smd_worklist.py --tier smd --json  # machine-readable
    python3 scripts/smd_worklist.py --program "Success for All"
    python3 scripts/smd_worklist.py --hub /path/to/data.json
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))  # for scripts.eval.compliance
import okf_lib

WIKI_ROOT = Path(__file__).parent.parent
HUB_URL = "https://jchoi92k.github.io/Learning-Engineering-Resource-Hub/data.json"

WWC = "What Works Clearinghouse"
ESSA = "Evidence for ESSA"

# The format each kind of page is documented to have. A property of the
# publisher's page type, not of any one page — hence "basis", not a finding.
KINDS = {
    "wwc-intervention-report": (
        "smd",
        "WWC intervention reports give an effect size (Hedges' g) and "
        "improvement index per outcome domain, from studies meeting WWC standards",
    ),
    "essa-program-page": (
        "smd",
        "Evidence for ESSA program pages give an effect size per qualifying "
        "study and an average across them",
    ),
    "wwc-practice-guide": (
        "pointer",
        "WWC practice guides rate recommendations and list supporting studies; "
        "they report no estimate of their own — extract the studies they cite",
    ),
}

URL_RE = re.compile(r"https?://[^\s)<>\]\"'`]+")


def url_key(url: str) -> str:
    """Scheme-, www-, case- and trailing-slash-insensitive. WWC serves the same
    report at /ncee/wwc/ and /ncee/WWC/, and the hub carries both spellings."""
    u = url.strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    u = u.split("#")[0]
    return u.rstrip("/.,;")


def classify(entry: dict) -> str | None:
    path = url_key(entry["url"])
    if entry["source"] == WWC:
        if "/interventionreport/" in path:
            return "wwc-intervention-report"
        if "/practiceguide/" in path:
            return "wwc-practice-guide"
    elif entry["source"] == ESSA and "/program/" in path:
        return "essa-program-page"
    return None


def program_name(title: str) -> tuple[str, str | None, str | None]:
    """(name, acronym, variant) from a hub title.

    `Evidence for ESSA: Peer-Assisted Learning Strategies (PALS) — Reading`
    -> ("Peer-Assisted Learning Strategies", "PALS", "Reading")
    """
    t = re.sub(r"[®™©]", "", title)
    t = re.sub(r"^\s*Evidence for ESSA\s*:\s*", "", t)
    t = re.sub(r"\s*[—–-]\s*Evidence for ESSA\s*$", "", t)
    variant = None
    parts = re.split(r"\s+[—–]\s+", t, maxsplit=1)
    if len(parts) == 2:
        t, variant = parts[0], parts[1].strip()
    acronym = None
    m = re.search(r"\(([A-Z][A-Za-z0-9&]{1,9})\)", t)
    if m and sum(c.isupper() for c in m.group(1)) >= 2:
        acronym = m.group(1)
    name = re.sub(r"\s*\([^)]*\)", "", t).strip(" :")
    return name, acronym, variant


def cluster_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def load_hub(src: str) -> list[dict]:
    if re.match(r"https?://", src):
        import warnings

        import requests
        with warnings.catch_warnings():
            # compliance warns when no contact email is set, which matters for
            # a crawl; this is one GET of one static file.
            warnings.simplefilter("ignore")
            from scripts.eval import compliance

        resp = requests.get(src, headers={"User-Agent": compliance.USER_AGENT}, timeout=60)
        resp.raise_for_status()
        data = resp.json()
    else:
        data = json.loads(Path(src).read_text(encoding="utf-8"))
    return data["entries"]


def load_wiki() -> dict[str, str]:
    """{bundle-relative path: text} for every content page."""
    pages = {}
    for folder in okf_lib.CONTENT_FOLDERS:
        for p in sorted((WIKI_ROOT / folder).glob("*.md")):
            if p.name == "index.md":
                continue
            pages[f"{folder}/{p.name}"] = p.read_text(encoding="utf-8")
    return pages


def urls_in(text: str) -> set[str]:
    return {url_key(u) for u in URL_RE.findall(text)}


def known_urls() -> tuple[set[str], set[str]]:
    """(URLs named in observations/, URLs and ids in the source manifest)."""
    recorded = set()
    for p in (WIKI_ROOT / "observations").glob("*.yaml"):
        recorded |= urls_in(p.read_text(encoding="utf-8"))
    reviewed = set()
    manifest = WIKI_ROOT / "sources" / "manifest.ndjson"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rec = json.loads(line)
            reviewed |= urls_in(rec.get("id") or "")
            reviewed |= urls_in(json.dumps(rec))
    return recorded, reviewed


def name_patterns(name: str, acronym: str | None) -> list[re.Pattern]:
    pats = []
    # A one-word name shorter than 6 characters ("Voyager", fine; "Read", not)
    # matches ordinary prose, so only the acronym is trusted for those.
    if len(name.split()) >= 2 or len(name) >= 6:
        pats.append(re.compile(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])"))
    if acronym and len(acronym) >= 3:
        pats.append(re.compile(r"(?<![\w-])" + re.escape(acronym) + r"(?![\w-])"))
    return pats


def named_in(name: str, acronym: str | None, pages: dict[str, str]) -> list[str]:
    """Pages matching name_patterns. A plain substring test first, because a
    look-around regex over ~3,700 pages per programme is minutes, not seconds."""
    pats = name_patterns(name, acronym)
    needles = [name] if len(name.split()) >= 2 or len(name) >= 6 else []
    if acronym and len(acronym) >= 3:
        needles.append(acronym)
    hits = []
    for path, text in pages.items():
        if not any(n in text for n in needles):
            continue
        if any(x.search(text) for x in pats):
            hits.append(path)
    return hits


def build(entries: list[dict], pages: dict[str, str]) -> list[dict]:
    page_urls = {path: urls_in(text) for path, text in pages.items()}
    cited_by = defaultdict(list)
    for path, us in page_urls.items():
        for u in us:
            cited_by[u].append(path)
    recorded, reviewed = known_urls()

    rows = []
    for e in entries:
        kind = classify(e)
        if not kind:
            continue
        tier, basis = KINDS[kind]
        name, acronym, variant = program_name(e["title"])
        k = url_key(e["url"])
        rows.append({
            "program": name,
            "acronym": acronym,
            "variant": variant,
            "source": e["source"],
            "kind": kind,
            "tier": tier,
            "basis": basis,
            "url": e["url"],
            "document_url": e.get("document_url"),
            "hub_num": e.get("num"),
            "published": e.get("published_date") or None,
            "cited_by": sorted(cited_by.get(k, [])),
            "state": "recorded" if k in recorded else "reviewed" if k in reviewed else "new",
            "_key": k,
            "_cluster": cluster_key(name),
        })

    # The hub has the same report under two URL spellings; keep one row.
    seen, deduped = set(), []
    for r in rows:
        if r["_key"] not in seen:
            seen.add(r["_key"])
            deduped.append(r)
    rows = deduped

    # Name mentions are computed once per programme, not per row.
    mentions = {}
    for r in rows:
        c = r["_cluster"]
        if c in mentions:
            continue
        mentions[c] = sorted(named_in(r["program"], r["acronym"], pages))

    sources_by_cluster = defaultdict(set)
    for r in rows:
        sources_by_cluster[r["_cluster"]].add(r["source"])
    for r in rows:
        r["named_in"] = mentions[r["_cluster"]]
        r["both"] = len(sources_by_cluster[r["_cluster"]]) > 1

    rows.sort(key=lambda r: (
        r["tier"] != "smd",
        -len(r["cited_by"]),
        not r["both"],
        -len(r["named_in"]),
        r["program"].lower(),
    ))
    return rows


def public(r: dict) -> dict:
    return {k: v for k, v in r.items() if not k.startswith("_")}


def md_cell(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|")


def print_table(rows: list[dict]) -> None:
    print("| # | programme | source | tier | cited | both | named | url |")
    print("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        label = r["program"] + (f" — {r['variant']}" if r["variant"] else "")
        src = "WWC" if r["source"] == WWC else "ESSA"
        if r["kind"] == "wwc-practice-guide":
            src += " guide"
        print(f"| {i} | {md_cell(label)} | {src} | {r['tier']} | {len(r['cited_by'])} "
              f"| {'yes' if r['both'] else ''} | {len(r['named_in'])} | {r['url']} |")


def print_program(rows: list[dict], query: str) -> int:
    q = cluster_key(query)
    hits = [r for r in rows if q in r["_cluster"] or (r["acronym"] and q == r["acronym"].lower())]
    if not hits:
        print(f"no WWC/ESSA row matches {query!r}", file=sys.stderr)
        return 1
    for r in hits:
        print(f"{r['program']}" + (f" — {r['variant']}" if r["variant"] else "")
              + f"  [{r['source']}, {r['kind']}, {r['state']}]")
        print(f"  url:       {r['url']}")
        if r["document_url"]:
            print(f"  document:  {r['document_url']}")
        print(f"  tier:      {r['tier']} — {r['basis']}")
        print(f"  cited by:  {len(r['cited_by'])}")
        for p in r["cited_by"]:
            print(f"    {p}")
        pats = name_patterns(r["program"], r["acronym"])
        print(f"  named in:  {len(r['named_in'])}  (phrase match on "
              + ", ".join(repr(p.pattern) for p in pats) + ")")
        for p in r["named_in"]:
            print(f"    {p}")
        print()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--hub", default=HUB_URL, help="data.json URL or local path (default: the hub's published copy)")
    ap.add_argument("--tier", choices=["smd", "pointer"], help="only this tier")
    ap.add_argument("--source", choices=["wwc", "essa"], help="only this publisher")
    ap.add_argument("--all", action="store_true", help="include rows already recorded or reviewed")
    ap.add_argument("--limit", type=int, default=40, help="rows to print (0 = all)")
    ap.add_argument("--json", action="store_true", help="NDJSON, one row per line")
    ap.add_argument("--program", help="everything on one programme, including which pages matched")
    args = ap.parse_args()

    try:
        entries = load_hub(args.hub)
    except Exception as exc:  # network, JSON or shape — say which, then stop
        print(f"could not load the hub from {args.hub}: {exc}", file=sys.stderr)
        return 2
    rows = build(entries, load_wiki())

    if args.program:
        return print_program(rows, args.program)

    total = len(rows)
    if not args.all:
        rows = [r for r in rows if r["state"] == "new"]
    if args.tier:
        rows = [r for r in rows if r["tier"] == args.tier]
    if args.source:
        rows = [r for r in rows if r["source"] == (WWC if args.source == "wwc" else ESSA)]
    shown = rows if args.limit == 0 else rows[: args.limit]

    if args.json:
        for r in shown:
            print(json.dumps(public(r), ensure_ascii=False))
        return 0

    n_smd = sum(r["tier"] == "smd" for r in rows)
    n_both = len({r["_cluster"] for r in rows if r["both"]})
    print(f"{total} WWC/ESSA review pages in the hub; {len(rows)} after filters "
          f"({n_smd} smd-tier, {len(rows) - n_smd} pointer); "
          f"{n_both} programmes reviewed by both.\n")
    print_table(shown)
    if len(shown) < len(rows):
        print(f"\n… {len(rows) - len(shown)} more; --limit 0 for all.")
    print("\ntier is the publisher's documented page format, not a check of this page — "
          "confirm the effect size on the page itself before writing a record.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
