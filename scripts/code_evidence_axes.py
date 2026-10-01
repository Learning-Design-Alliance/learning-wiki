#!/usr/bin/env python3
"""
code_evidence_axes.py — PILOT. Code claim evidence entries as cells on five axes
(evidence-dimensions.json, through scripts/evidence_dimensions.py): learners L, goal properties G, conditions C, the
design variable changed D, and outcome O, each with a result direction and design.

One entry can give several cells (one per contrast x outcome it reports, at most 4).
Every cell must quote the study's own text for its direction; a quote that is not
verbatim in the text leaves the cell in the record with quote_ok false, and the
renderer treats its direction as "?". An entry with no text of its study is coded
from the entry and marked basis "entry": its cells are shown, flagged, never counted
as known. Nothing here writes to a wiki page.

    python3 scripts/code_evidence_axes.py --pages elements/worked-examples ... --check
    python3 scripts/code_evidence_axes.py --pages ... --code [--run b] [--budget 1]
    python3 scripts/code_evidence_axes.py --new --code       # claims added in the working tree (the batch)
    python3 scripts/code_evidence_axes.py --contrasts [--run cells]

Cells go to eval/runs/evidence-axes/<run>.ndjson (default run "cells", the store the
batch adds to and render_evidence_map.py reads), keyed like code_kind_rigour.py, so
an unchanged entry is not paid for twice within a run. --run b codes the same entries
again independently, for the agreement check. --contrasts names each new cell's
contrast; only contrasts not yet named are sent.
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import check_load_bearing as clb  # noqa: E402
import code_kind_rigour as ckr  # noqa: E402
import okf_lib  # noqa: E402

import evidence_dimensions as dims  # noqa: E402
AXES = dims.axes()
OUTDIR = WIKI_ROOT / "eval" / "runs" / "evidence-axes"
SYSTEM = "You code research evidence for a learning-design wiki. Reply with JSON only."


def decision_claims(pages: list) -> set:
    out = set()
    for p in pages:
        t = (WIKI_ROOT / f"{p}.md").read_text(encoding="utf-8")
        if "## Design Decisions" not in t:
            continue
        sec = t[t.index("## Design Decisions"):]
        m = re.search(r"\n## (?!Design Decisions)", sec)
        out |= set(re.findall(r"\.\./claims/([^)#]+)\.md", sec[:m.start()] if m else sec))
    return out


def jobs(claims: set):
    for job in ckr.entries():
        if job[0]["claim"] in claims:
            yield job


def norm(s: str) -> str:
    """Letters and digits only: PDF text splits words at line ends ("ex- pected") and
    loses spacing, so whitespace and punctuation are not evidence either way."""
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def vocab(axis: str, field: str) -> list:
    return list(AXES[axis][field])


def prompt_for(block: str, basis: str, source: str, text) -> str:
    study = (f"## The study ({basis}: {source})\n{text}\n\n" if text else
             "## The study\nNo text of the study is available; only the wiki's entry below.\n\n")
    return f"""{study}## The wiki's evidence entry
{block}

## Task
Code the findings this entry reports as CELLS. A cell is one contrast (a treatment against a
comparison) on one outcome. Give at most 4 cells, the ones the entry relies on. For each cell use
ONLY these values (definitions: {json.dumps({a: AXES[a] for a in ('G','L','C','D','O','result')}, ensure_ascii=False)}).

Rules:
- Take every value from the study's text above, not from the wiki's entry. "?" whenever the text does not say.
- direction "0" ONLY if the text reports an equivalence test or adequate power; a non-significant
  difference without that is "ns".
- "quote": the sentence(s) from the STUDY TEXT that show the direction, copied exactly. If there is
  no study text, quote the entry and say so in "note".
- For a synthesis, code the pooled result, and code L/G/C as what the included studies covered ("mixed" if they vary).

Reply: {{"cells": [{{"L": {{"expertise": ..., "age": ...}}, "G": {{"knowledge_type": ..., "element_interactivity": ...}},
"C": {{"setting": ..., "duration": ...}}, "D": {{"variable": ..., "treatment": "short phrase", "comparison": "short phrase"}},
"O": {{"outcome": ..., "timing": ..., "outcome_detail": "short phrase"}},
"result": {{"direction": ..., "design": ..., "effect": "the printed effect size or null"}}, "quote": "...", "note": "..."}}]}}"""


def valid(cell: dict) -> list:
    bad = []
    for axis, fields in (("L", ("expertise", "age")), ("G", ("knowledge_type", "element_interactivity")),
                         ("C", ("setting", "duration")), ("D", ("variable",)), ("O", ("outcome", "timing")),
                         ("result", ("direction", "design"))):
        for f in fields:
            v = (cell.get(axis) or {}).get(f)
            if dims.normalize(f, v) not in AXES[axis][f]:
                bad.append(f"{axis}.{f}={v!r}")
    return bad


def code_one(job, api_key, model, run):
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    r, anchor, block, source, basis, text = job
    if basis == "abstract":
        text = clb.openalex_abstract(source[4:])
        if not text:
            basis = "entry"
    full = text
    if text and len(text) > 30000:
        text = text[:30000] + "\n[TRUNCATED]"
    gen = _retry(lambda: oc.generate(model, SYSTEM, prompt_for(block, basis, source, text if basis != "entry" else None),
                                     api_key, max_tokens=4000))
    d = extract_json(gen.raw_text) or {}
    cells = []
    for c in (d.get("cells") or [])[:4]:
        q = c.get("quote") or ""
        # checked against the whole article: the entry carries its own verbatim quote,
        # often from a Results section past the truncation, and the coder may reuse it
        c["quote_ok"] = bool(full) and len(norm(q)) >= 16 and norm(q) in norm(full)
        c["invalid"] = valid(c)
        cells.append(c)
    return {"key": ckr.key(r["claim"], anchor, block), "claim": r["claim"], "entry": anchor, "run": run,
            "basis": basis, "source": source, "codes": okf_lib.parse_evidence_codes(block),
            "cells": cells, "cost_usd": gen.cost_usd}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--pages", nargs="+", help="the claims these pages' Design Decisions cite")
    src.add_argument("--new", action="store_true", help="claim pages added in the working tree")
    src.add_argument("--claims", nargs="+", help="these claim slugs")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--code", action="store_true")
    ap.add_argument("--run", default="cells")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--budget", type=float, default=1.0)
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    if a.new:
        from link_claims import new_claims
        claims = set(new_claims())
    else:
        claims = set(a.claims) if a.claims else decision_claims(a.pages)
    out = OUTDIR / f"{a.run}.ndjson"
    have = set()
    if out.exists():
        have = {json.loads(l)["key"] for l in out.read_text(encoding="utf-8").splitlines() if l.strip()}
    todo = [j for j in jobs(claims) if ckr.key(j[0]["claim"], j[1], j[2]) not in have]
    by = {}
    for j in todo:
        by[j[4]] = by.get(j[4], 0) + 1
    print(f"{len(claims)} claims; {len(todo)} entries to code ({len(have)} already in run {a.run}) {by}")
    if a.check or not a.code:
        return
    key = os.environ["OPENROUTER_API_KEY"]
    OUTDIR.mkdir(parents=True, exist_ok=True)
    spent = errors = 0
    with open(out, "a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(a.workers) as ex:
        futs = [ex.submit(code_one, j, key, a.model, a.run) for j in todo]
        for f in concurrent.futures.as_completed(futs):
            try:
                rec = f.result()
            except Exception as e:  # noqa: BLE001
                errors += 1
                print("error:", str(e)[:160])
                continue
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            spent += rec["cost_usd"] or 0
            if spent > a.budget:
                print(f"budget ${a.budget} reached")
                ex.shutdown(cancel_futures=True)
                break
    print(f"coded {len(todo) - errors} (errors {errors}), ${spent:.3f} -> {out}")


def _retry(call, tries=6):
    import time
    for i in range(tries):
        try:
            return call()
        except Exception as e:  # noqa: BLE001
            if "rate-limited" not in str(e) and "429" not in str(e) or i == tries - 1:
                raise
            time.sleep(10 * (i + 1))


def assign_contrasts(run="cells", model="openai/gpt-5.6-luna"):
    """Name each cell's contrast canonically, per design variable, so a map row is one
    contrast ("spaced vs massed") rather than a variable ("spacing"), and flag cells coded
    the other way round (treatment and comparison swapped) so their direction can be read
    against the canonical orientation. Written to <run>-contrasts.json, keyed by
    variable and the exact treatment/comparison text."""
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    recs = [json.loads(l) for l in (OUTDIR / f"{run}.ndjson").read_text(encoding="utf-8").splitlines() if l.strip()]
    pairs = {}
    for r in recs:
        for c in r["cells"]:
            d = c.get("D") or {}
            pairs.setdefault(d.get("variable"), set()).add((d.get("treatment") or "", d.get("comparison") or ""))
    path = OUTDIR / f"{run}-contrasts.json"
    out = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    cost = 0.0
    for var, ps in sorted(pairs.items(), key=lambda kv: str(kv[0])):
        ps = sorted(p for p in ps if f"{var}\t{p[0]}\t{p[1]}" not in out)
        if not ps:
            continue
        listing = "\n".join(f"{i + 1}. {t} VS {c}" for i, (t, c) in enumerate(ps))
        prompt = f"""Design variable: {var}
Below are contrasts coded from studies, each "treatment VS comparison".
Group them into canonical contrasts a course designer would recognise as one choice, as "A vs B"
with A the option the variable names or the more intensive one (e.g. "spaced vs massed",
"longer vs shorter gaps", "expanding vs equal intervals", "immediate vs delayed feedback").
Keep genuinely different choices apart; do not merge "spaced vs massed" with "longer vs shorter gaps".
For each numbered contrast give its canonical label and whether its treatment is the A side
(true) or the B side (false, i.e. coded the other way round).
{listing}
Reply: {{"items": [{{"n": 1, "label": "A vs B", "treatment_is_a": true}}]}}"""
        g = _retry(lambda: oc.generate(model, SYSTEM, prompt, os.environ["OPENROUTER_API_KEY"], max_tokens=6000))
        cost += g.cost_usd or 0
        d = extract_json(g.raw_text) or {}
        for it in d.get("items") or []:
            try:
                t, c = ps[int(it["n"]) - 1]
            except (KeyError, ValueError, IndexError, TypeError):
                continue
            out[f"{var}\t{t}\t{c}"] = {"label": it.get("label"), "treatment_is_a": bool(it.get("treatment_is_a", True))}
        path.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(out)} contrasts labelled across {len(pairs)} variables, ${cost:.3f} -> {path}")


if __name__ == "__main__" and "--contrasts" in sys.argv:
    _run = sys.argv[sys.argv.index("--run") + 1] if "--run" in sys.argv else "cells"
    if (OUTDIR / f"{_run}.ndjson").exists():
        assign_contrasts(_run)
    else:
        print(f"no cells in run {_run}; nothing to name")
    sys.exit(0)


if __name__ == "__main__":
    main()
