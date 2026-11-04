#!/usr/bin/env python3
"""
rebuild_queues.py — write the source sweep's ingest queues from committed data alone.

The sweep reads eval/runs/queues/sweep-*.ndjson, which is ignored, so a container reset loses it.
Everything it is made of is committed: each universe's members (eval/screening/<universe>.ndjson,
first line a header), both screening models' votes (eval/screening/decisions.ndjson) and what has
been settled (sources/manifest.ndjson). screen_sources.py --record needs the abstracts cache as well,
which is not committed, so this does the same sort without it.

A member the manifest already holds, by id or DOI, is skipped. Both models including it puts it in
its universe's queue; one including and one excluding puts it in sweep-split.ndjson (INCLUSION.md's
default is to include, and split votes run last). Both excluding should already be in the manifest
as rejected; any that is not is counted and left for screen_sources.py --record. A member with no
decision, or a missing vote, is counted and left out.

    python3 scripts/sweep/rebuild_queues.py           # write the queues and print the counts
    python3 scripts/sweep/rebuild_queues.py --check   # print the counts only
"""
import argparse
import collections
import json
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
SCREEN_DIR = WIKI_ROOT / "eval" / "screening"
QUEUE_DIR = WIKI_ROOT / "eval" / "runs" / "queues"
PMC_S3 = "https://pmc-oa-opendata.s3.amazonaws.com"  # scripts/eval/pmc_aws.py S3_BASE

UNIVERSES = ("pmc-teaching-trials", "arxiv-education-research", "eric-intervention-studies")


def entry(m, universe):
    """A queue entry in the shape discover_articles builds, so fetching works unchanged."""
    e = {k: m[k] for k in ("id", "title", "year", "doi") if m.get(k) is not None}
    sid = m["id"]
    if sid.startswith("pmc-"):
        uid = sid[4:]
        e |= {"source": "pubmed", "pmcid": f"PMC{uid}",
              "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{uid}",
              "fetch_url": f"{PMC_S3}/metadata/PMC{uid}.1.json"}
    elif sid.startswith("arxiv-"):
        aid = sid[6:]
        e |= {"source": "arxiv", "url": f"https://arxiv.org/abs/{aid}",
              "fetch_url": f"https://arxiv.org/pdf/{aid}"}
    elif sid.startswith("eric-"):
        eid = sid[5:].upper()
        e |= {"source": "eric", "url": f"https://eric.ed.gov/?id={eid}",
              "fetch_url": f"https://files.eric.ed.gov/fulltext/{eid}.pdf"}
    e |= {"authors": m.get("authors") or "et al.", "topic_hint": f"screen:{universe}"}
    return e


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="print the counts without writing")
    args = ap.parse_args()

    settled, dois = set(), set()
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        if line.strip():
            d = json.loads(line)
            settled.add(d["id"])
            if d.get("doi"):
                dois.add(d["doi"].lower())
    decisions = {}
    for line in (SCREEN_DIR / "decisions.ndjson").read_text(encoding="utf-8").splitlines():
        if line.strip():
            d = json.loads(line)
            decisions[(d["universe"], d["id"])] = d

    split = []
    for universe in UNIVERSES:
        lines = (SCREEN_DIR / f"{universe}.ndjson").read_text(encoding="utf-8").splitlines()[1:]
        queue, counts = [], collections.Counter()
        for line in lines:
            m = json.loads(line)
            rec = decisions.get((universe, m["id"]))
            if rec is None:
                counts["no decision"] += 1
                continue
            if m["id"] in settled or (m.get("doi") and m["doi"].lower() in dois):
                counts["settled"] += 1
                continue
            votes = [v.get("decision") for v in rec["votes"].values()]
            if None in votes:
                counts["missing vote"] += 1
            elif all(v == "include" for v in votes):
                queue.append(entry(m, universe))
                counts["queued"] += 1
            elif all(v == "exclude" for v in votes):
                counts["excluded, not in manifest"] += 1
            else:
                split.append(entry(m, universe))
                counts["split vote"] += 1
        print(f"{universe}: " + ", ".join(f"{k} {n}" for k, n in sorted(counts.items())))
        if not args.check:
            QUEUE_DIR.mkdir(parents=True, exist_ok=True)
            (QUEUE_DIR / f"sweep-{universe}.ndjson").write_text(
                "".join(json.dumps(q, ensure_ascii=False) + "\n" for q in queue), encoding="utf-8")
    print(f"split votes: {len(split)}")
    if not args.check:
        (QUEUE_DIR / "sweep-split.ndjson").write_text(
            "".join(json.dumps(q, ensure_ascii=False) + "\n" for q in split), encoding="utf-8")


if __name__ == "__main__":
    main()
