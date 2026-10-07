#!/usr/bin/env python3
"""
code_kind_rigour.py — code every claim evidence entry with an evidence KIND and a
RIGOUR tier judged within that kind (evidence-scales.json; rubric in
eval/kind-rigor/RUBRIC.md), and write it as a span on the entry's codes line:

    `q2 · interview study` · `i?` · `n=14` · `qualitative · r3`

`q` stays as it is. It places a study on the causal-design ladder, which is useful
for a causal question and says nothing about how well a qualitative study, a design
case or an argument was done; kind + rigour does, which is why it was adopted
(maintainer decision, 2026-09-29, after the pilot in kind_rigor_pilot.py).

    python3 scripts/code_kind_rigour.py --check            # what would be coded, no calls
    python3 scripts/code_kind_rigour.py --code             # call the model; decisions only
    python3 scripts/code_kind_rigour.py --apply            # write recorded decisions to pages
    python3 scripts/code_kind_rigour.py --code --apply --new   # entries with no kind yet (the batch)

Each entry is judged against its study's own text: the fetched article when the claim
came from a batch, else the OpenAlex abstract for its DOI. With neither, the kind is
coded from the entry and the rigour is `r?`, because rigour judged from the wiki's own
paraphrase of a study is the thing this scale exists to stop. Decisions go to
eval/runs/kind-rigor/coded.ndjson keyed by the entry's text, so an unchanged entry is
never paid for twice and an edited one is re-coded. Run sync_evidence_codes.py
--apply afterwards to mirror the codes into frontmatter.
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
import okf_lib  # noqa: E402

OUT = WIKI_ROOT / "eval" / "runs" / "kind-rigor" / "coded.ndjson"
RUBRIC = (WIKI_ROOT / "eval" / "kind-rigor" / "RUBRIC.md").read_text(encoding="utf-8")
KINDS = list(okf_lib.EVIDENCE_KINDS)
SYSTEM = "You appraise research evidence for a learning-design wiki. Reply with JSON only."
KR_SPAN = re.compile(r"\s*·\s*`(?:" + "|".join(KINDS) + r")\s*·\s*r\s*[1-3?]`")
Q_SPAN = re.compile(r"`[^`\n]*\bq\s*[0-9?](?![0-9A-Za-z])[^`\n]*`")


def entries(new_only: bool = False):
    """(row, anchor, block, source, basis, text) for every entry with a codes line."""
    pages = clb.claim_pages()
    for r in clb.ranking(pages):
        _, units = clb.units(pages[r["claim"]])
        # units() strips the kind span before hashing, so "has it a kind yet" must be
        # read from the page itself. Read from the block, every entry looked new, and
        # only the ignored decision cache kept --new from re-coding the corpus: in a
        # fresh container (batch 13, 2026-10-07) it re-coded 3,400 entries and reset
        # rigour to r? wherever it had no text of the study.
        coded = set()
        if new_only:
            ev = okf_lib.get_section(pages[r["claim"]].read_text(encoding="utf-8"), "Evidence") or ""
            for part in re.split(r"(?m)^(?=### )", ev):
                if part.startswith("### ") and KR_SPAN.search(part):
                    coded.add(okf_lib.slugify(part.split("\n", 1)[0][4:].strip()))
        for anchor, block, _ in units:
            codes = okf_lib.parse_evidence_codes(block)
            if "q" not in codes or (new_only and anchor in coded):
                continue
            hit = clb.cached_article(block, r["articles"])
            if hit:
                yield r, anchor, block, hit[0], "full text", hit[1]
                continue
            m = clb.DOI_RE.search(block)
            yield r, anchor, block, ("doi:" + m.group(0).rstrip(".,;")) if m else "", "abstract" if m else "entry", None


def key(claim: str, anchor: str, block: str) -> str:
    return clb.digest(claim, anchor, KR_SPAN.sub("", block))


def done() -> dict:
    out = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                out[d["key"]] = d
    return out


def code_one(job: tuple, api_key: str, model: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    r, anchor, block, source, basis, text = job
    if basis == "abstract":
        text = clb.openalex_abstract(source[4:])
        if not text:
            basis = "entry"
    if text and len(text) > 30000:
        text = text[:30000] + "\n[TRUNCATED]"
    study = (f"## The study ({basis}: {source})\n{text}\n\n" if basis != "entry" else
             "## The study\nNo text of the study is available; only the wiki's entry below.\n\n")
    prompt = (f"{RUBRIC}\n\n{study}## The wiki's evidence entry\n{block}\n\n"
              'Code this study. Reply: {"kind": one of ' + json.dumps(KINDS) + ', "rigour": 1, 2, 3 or "?", '
              '"why": "one sentence naming the criteria met or missed"}. Rigour is "?" when the text you '
              "have cannot show whether the kind's criteria are met.")
    gen = oc.generate(model, SYSTEM, prompt, api_key, max_tokens=1500)
    d = extract_json(gen.raw_text) or {}
    kind, rig = d.get("kind"), d.get("rigour")
    if kind not in KINDS:
        raise ValueError(f"no usable kind for {r['claim']}#{anchor}: {gen.raw_text[:120]!r}")
    rig = int(rig) if str(rig) in ("1", "2", "3") else "?"
    if basis == "entry":
        rig = "?"
    return {"key": key(r["claim"], anchor, block), "claim": r["claim"], "entry": anchor,
            "basis": basis, "source": source, "kind": kind, "rigour": rig,
            "why": d.get("why"), "cost_usd": gen.cost_usd}


def apply(decisions: dict) -> tuple:
    """Write each recorded decision onto its entry's codes line, replacing any older span."""
    pages = clb.claim_pages()
    written = entries_written = 0
    for slug, path in pages.items():
        text = path.read_text(encoding="utf-8")
        ev = okf_lib.get_section(text, "Evidence")
        if not ev:
            continue
        new_ev, parts = ev, re.split(r"(?m)^(?=### )", ev)
        out = []
        for part in parts:
            if not part.startswith("### "):
                out.append(part)
                continue
            anchor = okf_lib.slugify(part.split("\n", 1)[0][4:].strip())
            d = decisions.get(key(slug, anchor, re.sub(r"<!--.*?-->", "", part, flags=re.S).strip()))
            if d:
                lines = part.split("\n")
                for i, line in enumerate(lines):
                    if Q_SPAN.search(line):
                        want = KR_SPAN.sub("", line).rstrip() + f" · `{d['kind']} · r{d['rigour']}`"
                        if want != line:
                            lines[i] = want
                            entries_written += 1
                        break
                part = "\n".join(lines)
            out.append(part)
        new_ev = "".join(out)
        if new_ev != ev:
            path.write_text(text.replace(ev, new_ev, 1), encoding="utf-8")
            written += 1
    return written, entries_written


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--code", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--new", action="store_true", help="only entries with no kind yet")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--budget", type=float, default=8.0, help="stop calling once this many dollars are spent")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=12)
    args = ap.parse_args()
    seen = done()
    jobs = [j for j in entries(args.new) if key(j[0]["claim"], j[1], j[2]) not in seen]
    if args.limit:
        jobs = jobs[: args.limit]
    bases = {}
    for j in jobs:
        bases[j[4]] = bases.get(j[4], 0) + 1
    print(f"{len(seen)} decisions recorded; {len(jobs)} entries to code {bases}")
    if args.code and jobs:
        api_key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
        OUT.parent.mkdir(parents=True, exist_ok=True)
        spent = errors = 0
        with OUT.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
            futs = {ex.submit(code_one, j, api_key, args.model): j for j in jobs}
            for n, f in enumerate(concurrent.futures.as_completed(futs), 1):
                try:
                    d = f.result()
                except Exception as e:
                    errors += 1
                    print("  error:", str(e)[:160])
                    continue
                spent += d.get("cost_usd") or 0
                seen[d["key"]] = d
                fh.write(json.dumps(d) + "\n")
                fh.flush()
                if n % 200 == 0:
                    print(f"  {n}/{len(jobs)} coded, ${spent:.3f}", flush=True)
                if spent > args.budget:
                    print(f"budget ${args.budget} reached; stopping")
                    for other in futs:
                        other.cancel()
                    break
        print(f"coded {len(jobs) - errors} (errors {errors}), ${spent:.3f}")
    if args.apply:
        pages, n = apply(seen)
        print(f"wrote {n} codes lines on {pages} claim page(s); now run sync_evidence_codes.py --apply")


if __name__ == "__main__":
    main()
