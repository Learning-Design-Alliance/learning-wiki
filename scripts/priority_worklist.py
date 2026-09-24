#!/usr/bin/env python3
"""
priority_worklist.py — what to extract next, from every source of priority at once.

Three queues, each answering a different question, printed side by side rather
than blended into one score (a blended score hides why a row is there):

  record  Articles the wiki already cites that have no structured record in
          observations/. The article is known; the work is reading it. Ranked
          by reuse (distinct pages citing the DOI), after the SMD tier below,
          because a record for a source cited on 30 pages repays itself 30
          times — the same rule as citation_worklist.py.
  hub     WWC intervention reports and Evidence for ESSA program pages the
          Renaissance hub catalogues and nobody here has reviewed yet. Taken
          from smd_worklist.py, which reads the hub at run time and commits
          nothing (the hub has no licence yet).
  gap     Claims with no coded evidence at all, ranked by how many pages cite
          the claim. Here the work is FINDING a source, so the row is a search
          target, not an article.

The `record` tier follows CLAUDE.md's extraction target (depth in one scale):
`smd` when the claim's evidence entry for that DOI mentions a d, g, SMD or
Hedges/Cohen effect; `convertible` for r, an odds or risk ratio, or eta
squared; `meta` for a meta-analysis that names no statistic (in education
those nearly always pool d or g); blank otherwise. It is read off the wiki's
own prose, so it is a hint about where to look, never a statement of what the
article reports. Few entries state a statistic at all, so most rows are blank.

`state` on a `record` row is `ingested` when the manifest says the pipeline has
already processed that article. Those stay in the queue: an ingested article has
claims but still no structured record, and is the cheapest to record because
its text has already been fetched once.

## How it stays in sync

Nothing here is a list anyone maintains, so there is no list to go stale. Every
row is derived at run time from committed state, and drops out on the next run
once the work lands:

- a DOI leaves `record` when an observations/ file names it;
- a hub page leaves `hub` when observations/ or sources/manifest.ndjson names it;
- a claim leaves `gap` when it gets a coded evidence entry;
- a hub page the manifest has settled (ingested, or rejected as a verdict)
  leaves `hub`, via the same manifest discovery already reads.

Work in progress is the one thing committed state cannot see. So pushed branches
ahead of main are scanned (`--in-flight`, on by default; `--no-in-flight` to
skip): a row whose DOI, URL or claim a recent branch touches is marked
`in-flight` with the branch name rather than dropped, since a branch can be
abandoned. A branch counts as working on a claim only when it adds an evidence
heading (`### Author Year`) to it, since a wiki-wide citation pass touches
hundreds of claims and is work on none of them; on a source, when it adds that
DOI or URL to observations/. Pushing early is therefore how you say "I'm on this".

    python3 scripts/priority_worklist.py                  # all three, top 15 each
    python3 scripts/priority_worklist.py --queue record --limit 40
    python3 scripts/priority_worklist.py --json           # NDJSON, one row per line
    python3 scripts/priority_worklist.py --no-hub         # offline

Output goes to stdout only. Hub-derived rows must not be committed (see above);
write a copy under eval/ (gitignored) if you want one on disk.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_citations as cc
import okf_lib

WIKI_ROOT = Path(__file__).parent.parent

SMD_RE = re.compile(r"\b(?:cohen'?s\s+d|hedges'?\s*g|smd|standardi[sz]ed mean difference"
                    r"|(?<![\w.])[dg]\s*=\s*[-−–]?\s*\.?\d)", re.I)
CONVERTIBLE_RE = re.compile(r"(?:\bodds ratio\b|\brisk ratio\b|\bOR\s*=|\bRR\s*=|η²|eta[- ]squared"
                            r"|(?<![\w.])r\s*=\s*[-−–]?\s*\.?\d)", re.I)
DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>)\]]+", re.I)


def norm_doi(doi: str) -> str:
    return doi.strip().rstrip(".,;").lower()


def observation_dois() -> set[str]:
    out = set()
    for p in (WIKI_ROOT / "observations").glob("*.yaml"):
        out |= {norm_doi(d) for d in DOI_RE.findall(p.read_text(encoding="utf-8"))}
    return out


def settled_dois() -> set[str]:
    """DOIs of every source the manifest has settled for good."""
    out = set()
    for e in okf_lib.load_manifest():
        if not okf_lib.manifest_rejection_is_final(e):
            continue
        for s in (e.get("doi") or "", e.get("id") or ""):
            out |= {norm_doi(d) for d in DOI_RE.findall(s)}
    return out


def evidence_block(text: str, line: str) -> str:
    """The claim evidence entry around one citation line: from the line to the
    next heading. Only this entry is read, so one page's d does not tier
    every DOI on it. Searched in the BODY: frontmatter `sources:` repeats each
    citation as a title, and matching there reads the next entries' titles."""
    text = okf_lib.split_frontmatter(text)[1]
    i = text.find(line)
    if i == -1:
        return ""
    m = re.search(r"^#{2,3} ", text[i + len(line):], re.M)
    return text[i:i + len(line) + (m.start() if m else len(text))]


def tier_of(block: str) -> str:
    if SMD_RE.search(block):
        return "smd"
    if CONVERTIBLE_RE.search(block):
        return "convertible"
    if re.search(r"meta-?analy", block, re.I):
        return "meta"
    return ""


TIER_RANK = {"smd": 0, "convertible": 1, "meta": 2, "": 3}


def record_queue() -> list[dict]:
    by_key = cc.load_all_citations()
    recorded, settled = observation_dois(), settled_dois()
    rows: dict[str, dict] = {}
    texts: dict[str, str] = {}
    for key, entries in by_key.items():
        for e in entries:
            if not e["doi"]:
                continue
            d = norm_doi(e["doi"])
            if d in recorded:
                continue
            r = rows.setdefault(d, {"queue": "record", "doi": d, "key": key, "pages": set(),
                                    "claims": set(), "tier": "", "citation": e["line"][:160]})
            r["pages"].add(e["source"])
            if e["source"].startswith("claims/"):
                r["claims"].add(e["source"][len("claims/"):-3])
                if e["source"] not in texts:
                    texts[e["source"]] = (WIKI_ROOT / e["source"]).read_text(encoding="utf-8")
                t = tier_of(evidence_block(texts[e["source"]], e["line"]))
                if TIER_RANK[t] < TIER_RANK[r["tier"]]:
                    r["tier"] = t
                r["citation"] = e["line"][:160]
    out = []
    for r in rows.values():
        r["state"] = "ingested" if r["doi"] in settled else "new"
        r["pages"], r["claims"] = sorted(r["pages"]), sorted(r["claims"])
        out.append(r)
    # A record anchors to a claim; one cited only from strategy pages has
    # nowhere to attach an appears_in edge, so claims first.
    out.sort(key=lambda r: (TIER_RANK[r["tier"]], not r["claims"], -len(r["pages"]), r["doi"]))
    return out


def hub_queue(src: str) -> tuple[list[dict], str]:
    import smd_worklist as sw
    try:
        entries = sw.load_hub(src)
    except Exception as exc:  # the hub being down must not sink the other queues
        return [], f"hub unavailable ({exc.__class__.__name__}); its queue is empty this run"
    rows = [r for r in sw.build(entries, sw.load_wiki()) if r["state"] == "new"]
    return [{"queue": "hub", "program": r["program"], "source": r["source"], "tier": r["tier"],
             "url": r["url"], "pages": r["cited_by"], "both": r["both"],
             "named_in": len(r["named_in"]), "state": "new"} for r in rows], ""


def gap_queue() -> list[dict]:
    rev = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))
    inbound = rev.get("edges", {}).get("claims", {})
    rows = []
    for p in sorted((WIKI_ROOT / "claims").glob("*.md")):
        if p.name == "index.md":
            continue
        text = p.read_text(encoding="utf-8")
        if "> **Evidence** · none recorded yet" not in text:
            continue
        slug = p.stem
        fm = okf_lib.parse_frontmatter_scalars(okf_lib.split_frontmatter(text)[0])
        citers = inbound.get(slug, {})
        n = sum(len(v) for v in citers.values())
        rows.append({"queue": "gap", "claim": slug, "title": (fm or {}).get("title") or slug,
                     "cited_by": n, "state": "new"})
    rows.sort(key=lambda r: (-r["cited_by"], r["claim"]))
    return rows


def in_flight(days: int) -> dict[str, str]:
    """{doi, url or claims/<slug>: branch} for work on pushed branches ahead of
    main that committed within `days`. Best effort: no git, no marks."""
    marks: dict[str, str] = {}

    def git(*a):
        return subprocess.run(["git", *a], cwd=WIKI_ROOT, capture_output=True,
                              text=True, check=True).stdout
    import time
    try:
        refs = git("for-each-ref", "--format=%(refname:short) %(committerdate:unix)",
                   "refs/remotes/origin").splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    cutoff = time.time() - days * 86400
    for line in refs:
        ref, _, ts = line.strip().rpartition(" ")
        if not ref or ref in ("origin/main", "origin/HEAD", "origin"):
            continue
        try:
            if float(ts) < cutoff:
                continue
            if git("rev-list", "--count", f"origin/main..{ref}").strip() == "0":
                continue
            diff = git("diff", "--no-color", "-U0", f"origin/main...{ref}")
        except (subprocess.CalledProcessError, ValueError):
            continue  # one unreadable ref must not hide the others
        branch = ref[len("origin/"):]
        path = None
        for d in diff.splitlines():
            if d.startswith("+++ "):
                path = d[6:] if d.startswith("+++ b/") else None
            elif not d.startswith("+") or not path:
                continue
            elif path.startswith("claims/") and path.endswith(".md"):
                # Only a new evidence entry counts. A wiki-wide citation pass
                # touches hundreds of claims and is not work on any of them.
                if d.startswith("+### "):
                    marks.setdefault(path, branch)
            elif path.startswith("observations/"):
                for doi in DOI_RE.findall(d):
                    marks.setdefault(norm_doi(doi), branch)
                for url in re.findall(r"https?://\S+", d):
                    marks.setdefault(url.rstrip("\"'),.").lower(), branch)
    return marks


def mark(rows: list[dict], marks: dict[str, str]) -> None:
    for r in rows:
        keys = [r.get("doi"), (r.get("url") or "").lower() or None]
        keys += [f"claims/{c}.md" for c in r.get("claims", [])]
        if r.get("claim"):
            keys.append(f"claims/{r['claim']}.md")
        for k in keys:
            if k and k in marks:
                r["state"], r["branch"] = "in-flight", marks[k]
                break


def show(title: str, rows: list[dict], limit: int, fmt) -> None:
    print(f"## {title}: {len(rows)}\n")
    for r in rows[:limit] if limit else rows:
        flag = f"  [in-flight: {r['branch']}]" if r["state"] == "in-flight" else ""
        print("  " + fmt(r) + flag)
    if limit and len(rows) > limit:
        print(f"  ... and {len(rows) - limit} more (--limit 0 for all)")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--queue", choices=["record", "hub", "gap"], action="append",
                    help="only these queues (repeatable; default all three)")
    ap.add_argument("--limit", type=int, default=15, help="rows per queue (0 = all)")
    ap.add_argument("--json", action="store_true", help="NDJSON, one row per line")
    ap.add_argument("--no-hub", action="store_true", help="skip the network fetch of the hub")
    ap.add_argument("--hub", default=None, help="hub data.json URL or local path")
    ap.add_argument("--no-in-flight", action="store_true", help="do not scan pushed branches")
    ap.add_argument("--days", type=int, default=14, help="branches older than this are ignored")
    args = ap.parse_args()
    queues = args.queue or ["record", "hub", "gap"]

    notes = []
    out: dict[str, list[dict]] = {}
    if "record" in queues:
        out["record"] = record_queue()
    if "hub" in queues:
        if args.no_hub:
            out["hub"], _ = [], notes.append("hub skipped (--no-hub)")
        else:
            import smd_worklist as sw
            out["hub"], note = hub_queue(args.hub or sw.HUB_URL)
            if note:
                notes.append(note)
    if "gap" in queues:
        out["gap"] = gap_queue()

    if not args.no_in_flight:
        marks = in_flight(args.days)
        for rows in out.values():
            mark(rows, marks)

    if args.json:
        for rows in out.values():
            for r in rows[:args.limit] if args.limit else rows:
                print(json.dumps(r, ensure_ascii=False))
        for n in notes:
            print(n, file=sys.stderr)
        return 0

    for n in notes:
        print(f"note: {n}\n")
    if "record" in out:
        show("record — cited articles with no structured record", out["record"], args.limit,
             lambda r: f"{r['tier'] or '-':11} {len(r['pages']):3} pages  {len(r['claims']):2} claims  "
                       f"{'ingested' if r['state'] == 'ingested' else '        '}  {r['doi']}  ({r['key']})")
    if "hub" in out:
        show("hub — WWC/ESSA reviews not yet read", out["hub"], args.limit,
             lambda r: f"{r['tier']:7} {len(r['pages']):2} cite  {'both' if r['both'] else '    '}  "
                       f"{r['program'][:50]:50}  {r['url']}")
    if "gap" in out:
        show("gap — claims with no evidence, to find a source for", out["gap"], args.limit,
             lambda r: f"{r['cited_by']:4} cited by   {r['claim']}  — {r['title'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
