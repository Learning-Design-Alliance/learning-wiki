#!/usr/bin/env python3
"""
link_claims.py — connect each claim to the claims it bears on.

Extraction writes claims one article at a time, and nothing links a new claim to
the ones already here: on 2026-09-26, 1,226 of 2,248 claim pages had no link in or
out, and 89% rested on a single study. So for each claim this retrieves the eight
most similar claims from the search index (search_index.py, BM25 over title,
description and body) and asks a model which of them it relates to, and how:

    same         the same proposition, reworded (a merge candidate)
    general      a broader claim this one is an instance of, or tests
    specific     a narrower finding that is an instance of this one
    contradicts  a finding opposite to this one
    related      same topic, a different proposition

`--apply` writes each relation into BOTH pages' `## Related Claims`, labelled, so
an orphan joins the graph and a general claim lists the findings that bear on it.
It moves no evidence: filing a finding's study under a general claim's `## Evidence`
is an editorial act (CLAUDE.md, the research layer), and `same` pairs are only
proposed. `merge_claims.py` performs a merge once someone has looked.

Every decision is written to `--out` (NDJSON) before anything is applied, so a run
can be audited and re-applied without paying for it twice.

    python3 scripts/link_claims.py --all --out eval/runs/claim-links/all.ndjson
    python3 scripts/link_claims.py --new --apply          # claims added in the working tree
    python3 scripts/link_claims.py --apply --from eval/runs/claim-links/all.ndjson
"""
import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
import search_index  # noqa: E402

RELATIONS = ("same", "general", "specific", "contradicts", "related")
REVERSE = {"same": "same", "general": "specific", "specific": "general",
           "contradicts": "contradicts", "related": "related"}
LABEL = {
    "same": "possibly the same claim (merge candidate)",
    "general": "a broader claim this one bears on",
    "specific": "a narrower finding that bears on this claim",
    "contradicts": "reports the opposite",
    "related": "related",
}
LINE_RE = re.compile(r"^- \[[^\]]*\]\(([^)]+)\.md\)")
SUBCLAIM_RE = re.compile(r"^`q\S* i\S*`\s+(.+?)\s*\[→", re.M)
SYSTEM = "You compare research claims for a learning-design wiki. Reply with one JSON object and nothing else."


def claim_record(slug: str) -> dict:
    text = (WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8")
    fm_lines, body = okf_lib.split_frontmatter(text)
    fm = okf_lib.parse_frontmatter_scalars(fm_lines)
    subs = SUBCLAIM_RE.findall(body)
    return {"slug": slug, "title": str(fm.get("title") or slug), "finding": (subs[0] if subs else "")[:300]}


def new_claims() -> list:
    """Claim pages added in the working tree: untracked, or staged as added."""
    out = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "claims/"],
                         cwd=WIKI_ROOT, capture_output=True, text=True).stdout.split()
    out += subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", "HEAD", "--", "claims/"],
                          cwd=WIKI_ROOT, capture_output=True, text=True).stdout.split()
    return sorted({Path(p).stem for p in out if p.endswith(".md") and not p.endswith("index.md")})


def candidates(db, rec: dict, k: int = 8) -> list:
    rows = search_index.query(db, rec["title"] + " " + rec["finding"], folder="claims", limit=k + 1, mode="OR")
    return [r[2] for r in rows if r[2] != rec["slug"]][:k]


def classify(rec: dict, cands: list, key: str, model: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    listing = "\n".join(f"{i + 1}. {c['title']} — {c['finding']}" for i, c in enumerate(cands))
    prompt = f"""CLAIM: {rec['title']}
Its main finding: {rec['finding']}

OTHER CLAIMS:
{listing}

For each OTHER claim that bears on CLAIM, give its number and relation:
- "same": the SAME proposition, reworded: one title could replace the other with nothing
  gained or lost (same intervention or variable, same outcome, same direction). A claim about
  a different intervention, outcome, population or condition is NOT "same", however close.
- "general": a broader claim that CLAIM is an instance of, or tests.
- "specific": a narrower finding that is an instance of CLAIM.
- "contradicts": reports the opposite of CLAIM.
- "related": the same topic, but a different proposition.
Leave out any claim that is unrelated. Most lists have no "same"; when unsure between "same" and
"related", answer "related".
Reply: {{"links": [{{"n": <number>, "relation": "<relation>"}}]}}"""
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=6000,
                      reasoning_effort="low" if "glm" in model else None)
    data = extract_json(gen.raw_text)
    links = []
    for item in (data.get("links") or []) if isinstance(data, dict) else []:
        n, rel = item.get("n"), item.get("relation")
        if isinstance(n, int) and 1 <= n <= len(cands) and rel in RELATIONS:
            links.append({"target": cands[n - 1]["slug"], "relation": rel})
    return {"claim": rec["slug"], "candidates": [c["slug"] for c in cands], "links": links,
            "model": model, "cost_usd": gen.cost_usd, "provider": gen.provider}


def run(slugs: list, out: Path, model: str, concurrency: int) -> list:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set")
    db = search_index.ensure()
    cache = {}

    def rec(s):
        if s not in cache:
            cache[s] = claim_record(s)
        return cache[s]

    # sqlite connections belong to one thread, so each worker opens its own on the
    # index ensure() just made current.
    db.close()
    import sqlite3
    results = []
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        def worker(slug):
            local = sqlite3.connect(search_index.DB_PATH)
            r = rec(slug)
            try:
                cands = [rec(c) for c in candidates(local, r)]
                return classify(r, cands, key, model) if cands else {"claim": slug, "candidates": [], "links": []}
            except Exception as e:
                return {"claim": slug, "error": f"{type(e).__name__}: {e}"[:300]}
        for res in ex.map(worker, slugs):
            fh.write(json.dumps(res) + "\n")
            fh.flush()
            results.append(res)
    return results


def _linked(text: str) -> set:
    section = okf_lib.get_section(text, "Related Claims") or ""
    return {Path(m.group(1)).name for m in (LINE_RE.match(l.strip()) for l in section.splitlines()) if m}


def add_link(slug: str, target: str, relation: str, titles: dict) -> bool:
    """Append one labelled bullet to `slug`'s ## Related Claims, unless the page
    already links `target` there. Returns whether the page changed."""
    path = WIKI_ROOT / "claims" / f"{slug}.md"
    if not path.exists() or not (WIKI_ROOT / "claims" / f"{target}.md").exists() or slug == target:
        return False
    text = path.read_text(encoding="utf-8")
    if target in _linked(text):
        return False
    title = titles.get(target) or target
    bullet = f"- [{title.replace('[', '(').replace(']', ')')}]({target}.md) — {LABEL[relation]}"
    lines = text.split("\n")
    head = next((i for i, l in enumerate(lines) if l.strip() == "## Related Claims"), None)
    if head is None:
        lines += ["", "## Related Claims", bullet]
    else:
        end = next((i for i in range(head + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        last = end
        while last > head + 1 and not lines[last - 1].strip():
            last -= 1
        # A section holding only the template's empty "- " placeholder gets it replaced.
        if last == head + 2 and lines[head + 1].strip() == "-":
            lines[head + 1] = bullet
        else:
            lines.insert(last, bullet)
    path.write_text("\n".join(lines), encoding="utf-8")
    return True


def apply(results: list) -> dict:
    titles = {}
    stats = {r: 0 for r in RELATIONS}
    stats.update(pages_changed=0, pairs=0, skipped_conflicting=0)
    seen = {}
    changed = set()
    for res in results:
        for link in res.get("links") or []:
            a, b, rel = res["claim"], link["target"], link["relation"]
            pair = tuple(sorted((a, b)))
            if pair in seen:                          # the other side already decided this pair
                if seen[pair] != (rel if a == pair[0] else REVERSE[rel]):
                    stats["skipped_conflicting"] += 1
                continue
            seen[pair] = rel if a == pair[0] else REVERSE[rel]
            for s in (a, b):
                if s not in titles:
                    try:
                        titles[s] = claim_record(s)["title"]
                    except FileNotFoundError:
                        titles[s] = s
            if add_link(a, b, rel, titles):
                changed.add(a)
            if add_link(b, a, REVERSE[rel], titles):
                changed.add(b)
            stats[rel] += 1
            stats["pairs"] += 1
    stats["pages_changed"] = len(changed)
    return stats


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--all", action="store_true", help="every claim page")
    src.add_argument("--new", action="store_true", help="claim pages added in the working tree")
    src.add_argument("--claims", nargs="+", help="these claim slugs")
    src.add_argument("--from", dest="from_file", help="apply a previous run's decisions without re-asking")
    ap.add_argument("--out", default=None, help="NDJSON of decisions (default eval/runs/claim-links/<mode>.ndjson)")
    ap.add_argument("--apply", action="store_true", help="write the links into the claim pages")
    ap.add_argument("--model", default="z-ai/glm-5.3-flash")
    ap.add_argument("--concurrency", type=int, default=16)
    args = ap.parse_args()

    if args.from_file:
        results = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        slugs = (sorted(p.stem for p in (WIKI_ROOT / "claims").glob("*.md") if p.stem != "index") if args.all
                 else new_claims() if args.new else args.claims)
        if not slugs:
            print("no claims to link")
            return
        mode = "all" if args.all else "new" if args.new else "claims"
        out = Path(args.out) if args.out else WIKI_ROOT / "eval" / "runs" / "claim-links" / f"{mode}.ndjson"
        print(f"linking {len(slugs)} claim(s) with {args.model}; decisions -> {out}", flush=True)
        results = run(slugs, out, args.model, args.concurrency)
        errors = sum(1 for r in results if r.get("error"))
        cost = sum(r.get("cost_usd") or 0 for r in results)
        print(f"asked {len(results)}, errors {errors}, cost ${cost:.4f}")

    rels = {}
    for r in results:
        for l in r.get("links") or []:
            rels[l["relation"]] = rels.get(l["relation"], 0) + 1
    print("proposed:", ", ".join(f"{v} {k}" for k, v in sorted(rels.items())) or "nothing")
    if args.apply:
        print("applied:", apply(results))
        same = sorted({tuple(sorted((r["claim"], l["target"]))) for r in results for l in r.get("links") or []
                       if l["relation"] == "same"})
        if same:
            print(f"{len(same)} merge candidate pair(s); review, then scripts/merge_claims.py <keep> <fold>:")
            for a, b in same[:20]:
                print(f"   {a}  <->  {b}")


if __name__ == "__main__":
    main()
