#!/usr/bin/env python3
"""
triage_design_pages.py — sort every principle and pattern page into what it is, so the
canonical ones can be converted to the conditional-model format and the rest folded into
or linked from them (CLAUDE.md, 2026-10-02). Writes no page.

    python3 scripts/triage_design_pages.py --run a [--model M]   # classify every page
    python3 scripts/triage_design_pages.py --table               # merge runs into the table

Each page is shown with its same-kind BM25 neighbours (title, description, inbound links,
claims cited) and classed as one of:

  canonical  the general, reusable page for its idea: the one to convert
  duplicate  the same idea as a neighbour that should be canonical: merge, keep an alias
  variant    a narrower version, one source's framing or one application of a canonical
             idea: keep, and link it from the canonical page
  design     (patterns) a design for one setting, course, population or product, which the
             settled rule says is never a pattern
  misfiled   not a principle or pattern at all (a strategy, element, theory or claim)

Two runs by models of different families are kept apart (eval/runs/page-triage/<run>.ndjson,
ignored); --table writes eval/page-triage/triage.tsv with both verdicts and an `agree`
column, so a person reviews the disagreements first. The page's own numbers (inbound links,
claims, sources that wrote it) are facts and are in the table beside the verdicts, which are
not.
"""
import argparse
import collections
import concurrent.futures
import json
import os
import re
import sys
import time
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
import search_index  # noqa: E402

KINDS = ("principles", "patterns")
RUNS = WIKI_ROOT / "eval" / "runs" / "page-triage"
TABLE = WIKI_ROOT / "eval" / "page-triage" / "triage.tsv"
CLASSES = ("canonical", "duplicate", "variant", "design", "misfiled")
COMMENT = re.compile(r"<!--.*?-->", re.S)
CLAIM = re.compile(r"\.\./claims/([^)#\s]+)\.md")
SYSTEM = "You are curating a learning-design wiki. Reply with JSON only."


def inbound_counts() -> dict:
    ri = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))
    out = {}
    for kind in KINDS:
        for slug, by in (ri.get("edges", {}).get(kind) or {}).items():
            out[f"{kind}/{slug}"] = sum(len(v) for v in by.values())
    return out


def sources_per_page() -> collections.Counter:
    c = collections.Counter()
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("status") == "ingested":
            for p in rec.get("pages") or []:
                c[p[:-3]] += 1
    return c


def pages() -> dict:
    inbound, srcs = inbound_counts(), sources_per_page()
    out = {}
    for kind in KINDS:
        for p in sorted((WIKI_ROOT / kind).glob("*.md")):
            if p.stem == "index":
                continue
            text = p.read_text(encoding="utf-8")
            fm_lines, body = okf_lib.split_frontmatter(text)
            fm = okf_lib.parse_frontmatter_scalars(fm_lines)
            live = COMMENT.sub("", body)
            key = f"{kind}/{p.stem}"
            out[key] = {
                "key": key, "kind": kind, "slug": p.stem,
                "title": str(fm.get("title") or p.stem), "description": str(fm.get("description") or "")[:400],
                "status": str(fm.get("status") or "?"), "inbound": inbound.get(key, 0),
                "claims": len(set(CLAIM.findall(live))), "sources": srcs.get(key, 0),
                "converted": "## Conditional relationship" in live or "## Description and scope" in live,
                "grain": str(fm.get("grain_size") or ""), "chars": len(text),
                "excerpt": re.sub(r"\n{2,}", "\n", re.sub(r"(?m)^> .*$", "", live)).strip()[:1500],
            }
    return out


def neighbours(db, rec: dict, allp: dict, k: int = 10) -> list:
    """BM25 neighbours on title and description, then on the slug's own words, whose
    short general pages (`worked-examples`) a long description can bury."""
    keys = []
    for text, n in ((rec["title"] + " " + rec["description"], 8), (rec["slug"].replace("-", " "), 6)):
        for r in search_index.query(db, text, folder=rec["kind"], limit=n + 1, mode="OR"):
            x = f"{r[1]}/{r[2]}"
            if x != rec["key"] and x in allp and x not in keys:
                keys.append(x)
    return [allp[x] for x in keys][:k]


def prompt(rec: dict, cands: list) -> str:
    kind = rec["kind"][:-1]
    listing = "\n".join(f"- {c['slug']}: {c['title']} — {c['description'][:220]} [inbound links {c['inbound']}, "
                        f"claims cited {c['claims']}, written by {c['sources']} source(s)]" for c in cands)
    return f"""A {kind} page in a learning-design wiki, and the most similar {kind} pages.

In this wiki a PRINCIPLE states a conditional relationship between a learner's state, an activity and an outcome.
A PATTERN is a reusable, research-based design, general across domains and contexts. A course or lesson for a
particular setting, population, subject or product (a self-paced mobile language course, a clinical onboarding
programme, a Duolingo-style app, one study's session procedure) is a DESIGN, never a pattern.

## The page: {rec['slug']}
Title: {rec['title']}
Description: {rec['description']}
Inbound links {rec['inbound']}, claims cited {rec['claims']}, written by {rec['sources']} source(s), status {rec['status']}
Opening text:
{rec['excerpt']}

## Similar {kind} pages
{listing or '(none)'}

Classify the page as exactly one of:
- "canonical": the general, reusable page for its idea; no similar page above covers the same idea more generally.
- "duplicate": the same idea as one similar page, which should be the single page for it.
- "variant": a narrower version, one source's framing or one application of the idea of one similar page that is
  more general; worth keeping and linking from that page.
- "design": {'a design for one setting, course, population, subject or product (patterns only)' if kind == 'pattern' else 'not used for principles; choose another class'}.
- "misfiled": not a {kind} at all; say what kind it is (strategy, element, theory, claim, process, method, or design).
For duplicate and variant, name the similar page's slug that should be canonical, exactly as listed. A page framed by
one study, programme, course or product is a "variant" even when its general page is not listed: then give canonical
null. Use "canonical" only for a page that states the idea generally.
Reply: {{"class": "...", "canonical": "slug or null", "suggested_kind": "kind or null", "reason": "one sentence"}}"""


def _call(model, text, key):
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    for attempt in range(6):
        try:
            g = oc.generate(model, SYSTEM, text, key, max_tokens=1500)
            d = extract_json(g.raw_text)
            if isinstance(d, dict):
                return d, g.cost_usd or 0
        except Exception as e:  # noqa: BLE001
            if attempt == 5:
                return {"error": str(e)[:200]}, 0
            time.sleep(6 * (attempt + 1))
    return {"error": "no JSON"}, 0


def run(name: str, model: str, workers: int, limit: int):
    allp = pages()
    db = search_index.ensure()
    RUNS.mkdir(parents=True, exist_ok=True)
    out = RUNS / f"{name}.ndjson"
    done = set()
    if out.exists():
        done = {json.loads(l)["key"] for l in out.read_text(encoding="utf-8").splitlines() if l.strip()}
    todo = [r for r in allp.values() if r["key"] not in done][: limit or None]
    jobs = [(r, neighbours(db, r, allp)) for r in todo]
    key = os.environ["OPENROUTER_API_KEY"]
    cost = 0.0
    print(f"{len(allp)} pages; {len(jobs)} to classify in run {name} with {model}")
    with open(out, "a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(_call, model, prompt(r, c), key): (r, c) for r, c in jobs}
        for f in concurrent.futures.as_completed(futs):
            r, c = futs[f]
            d, usd = f.result()
            cost += usd
            cand = {x["slug"] for x in c}
            if d.get("canonical") not in cand:
                d["canonical_unlisted"] = d.get("canonical")
                d["canonical"] = None
            fh.write(json.dumps({"key": r["key"], "model": model, "neighbours": sorted(cand), **d}) + "\n")
            fh.flush()
    print(f"run {name}: ${cost:.3f} -> {out}")


def combine(a: dict, b: dict) -> tuple:
    """(verdict, canonical, needs_review). Read from a sample of the two runs' disagreements
    (2026-10-02): GPT (run a) draws the design and misfiled lines where the settled rules
    do, DeepSeek (run b) calls most single-setting pages variants and most recommendation
    pages canonical. So agreement stands; design against variant is a design (both say it
    is not a general page); anything else is the GPT verdict, flagged for a person."""
    ca, cb = a.get("class"), b.get("class")
    target = a.get("canonical") if a.get("canonical") else b.get("canonical")
    if ca == cb:
        same = a.get("canonical") == b.get("canonical") or ca not in ("duplicate", "variant")
        return ca, target if ca in ("duplicate", "variant") else "", not same
    if {ca, cb} == {"design", "variant"}:
        return "design", "", False
    return ca or cb, target if (ca or cb) in ("duplicate", "variant") else "", True


def table():
    allp = pages()
    runs = {}
    for p in sorted(RUNS.glob("*.ndjson")):
        runs[p.stem] = {}
        for l in p.read_text(encoding="utf-8").splitlines():
            if l.strip():
                d = json.loads(l)
                runs[p.stem][d["key"]] = d
    names = sorted(runs)
    TABLE.parent.mkdir(parents=True, exist_ok=True)
    cols = ["key", "title", "status", "inbound", "claims", "sources", "converted"]
    for n in names:
        cols += [f"{n}_class", f"{n}_canonical", f"{n}_kind", f"{n}_reason"]
    cols += ["agree", "verdict", "verdict_canonical", "suggested_kind", "review"]
    lines = ["\t".join(cols)]
    tally = collections.Counter()
    for key, r in sorted(allp.items(), key=lambda kv: (-kv[1]["inbound"], kv[0])):
        row = [key, r["title"], r["status"], str(r["inbound"]), str(r["claims"]), str(r["sources"]),
               "yes" if r["converted"] else ""]
        verdicts = []
        for n in names:
            d = runs[n].get(key, {})
            row += [d.get("class", ""), d.get("canonical") or "", d.get("suggested_kind") or "",
                    (d.get("reason") or d.get("error") or "").replace("\t", " ").replace("\n", " ")]
            verdicts.append((d.get("class"), d.get("canonical") if d.get("class") in ("duplicate", "variant") else None))
        agree = "yes" if len(verdicts) > 1 and len(set(verdicts)) == 1 else ("class" if len(verdicts) > 1 and len({v[0] for v in verdicts}) == 1 else "no")
        row.append(agree if len(names) > 1 else "")
        a, b = runs.get("a", {}).get(key, {}), runs.get("b", {}).get(key, {})
        v, tgt, rev = combine(a, b)
        row += [v or "", tgt or "", a.get("suggested_kind") or b.get("suggested_kind") or "" if v == "misfiled" else "",
                "yes" if rev else ""]
        tally[(r["kind"], v, "review" if rev else "settled")] += 1
        lines.append("\t".join(row))
    TABLE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(allp)} rows -> {TABLE}")
    for k, v in sorted(tally.items(), key=lambda kv: str(kv[0])):
        print(" ", k, v)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--run")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--table", action="store_true")
    a = ap.parse_args()
    if a.run:
        run(a.run, a.model, a.workers, a.limit)
    if a.table:
        table()


if __name__ == "__main__":
    main()
