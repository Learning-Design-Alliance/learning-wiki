#!/usr/bin/env python3
"""
recode_impact.py — make every `i` code rest on a magnitude the source prints.

`i` codes a PRINTED effect size (CLAUDE.md, impact table): 3 large (d >= 0.8),
2 medium (0.4-0.79), 1 small (0.2-0.39), 0 negligible, `?` when the source prints
none. On 2026-09-27, 455 evidence entries coded `i1`-`i3` with no effect size or
test statistic anywhere in the entry, most from extraction batches: the extractor
wrote `q2 · i1` beside means with no SD, "significant" with no number, or a model's
"substantially improves". health_evidence.py counts them.

For each such entry this reads the study's own text (the article the pipeline
fetched, else the OpenAlex abstract for its DOI) and asks a model whether the
source prints an effect size for the finding the entry reports, and to quote it.
What the model says is not trusted on its own:

- A statistic is accepted only if its quote appears verbatim in the source (after
  whitespace and dash normalisation) and the value parses. The bin is then
  computed here, from the value, never taken from the model: d, g and SMD are
  binned directly; r, eta-squared and odds ratios through the standard conversions
  to d (Borenstein et al. 2009, ch. 7), for the bin only. The page shows the
  statistic as printed, so no converted number is ever written.
- Anything else becomes `i?`. On an abstract the entry says the abstract prints no
  effect size, since the paper may; with no source at all it says no source text
  was available to check.

The subclaims that point at a recoded entry take the same `i`, since an entry's
codes and its subclaims' must agree. Decisions go to `--out` before anything is
written, and `--from` re-applies a run without paying for it again.

    python3 scripts/recode_impact.py --check                 # what would change, and the cost so far
    python3 scripts/recode_impact.py --apply
    python3 scripts/recode_impact.py --apply --from eval/runs/impact-recode/run.ndjson
"""
import argparse
import concurrent.futures
import json
import math
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import check_load_bearing as clb  # noqa: E402
import health_evidence as he  # noqa: E402

OUT = WIKI_ROOT / "eval" / "runs" / "impact-recode" / "run.ndjson"
MAX_TEXT = 60_000
KINDS = ("d", "g", "smd", "r", "eta2", "partial_eta2", "or", "beta_std")

SYSTEM = """\
You check one evidence entry on a learning-science wiki page against the study it cites.
The entry codes an effect size (i1 small, i2 medium, i3 large) but prints no statistic.
Your only question: does the study's text PRINT an effect size for the finding this entry
reports? An effect size is a standardised magnitude: Cohen's d, Hedges' g, a standardised
mean difference, a correlation r, eta-squared or partial eta-squared, an odds ratio, or a
standardised beta. These are NOT effect sizes: a p-value, "significant", a t, F or chi-square
statistic alone, raw means or percentages without a standardised effect, an unstandardised
regression coefficient, R² or "variance explained" from a regression or path model, or a
model's AUC or accuracy.

Output ONLY a JSON object, no fences:
{"printed": true | false,
 "kind": "d" | "g" | "smd" | "r" | "eta2" | "partial_eta2" | "or" | "beta_std" | null,
 "value": <the number as printed, e.g. 0.52 or -0.31>, or null,
 "quote": "the shortest exact span of the text containing the statistic, copied character for character", or null,
 "finding": "a few words naming what the statistic measures"}
If several effect sizes are printed for the finding, give the one for its main outcome. If the
text prints none for this finding, answer "printed": false."""


def _norm(t: str) -> str:
    t = t.replace("−", "-").replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip().lower()


# The quote has to name the statistic it is: a bare ".166" beside "variance explained"
# in a path model was labelled η² by the model and would have been binned large.
KIND_WORDS = {
    "d": r"\bd\b|cohen|effect size", "g": r"\bg\b|hedges|effect size", "smd": r"smd|standardi[sz]ed mean|effect size",
    "r": r"\br\b|correlat", "eta2": r"η|eta", "partial_eta2": r"η|eta", "or": r"\bor\b|odds",
    "beta_std": r"β|beta",
}


def as_d(kind: str, value: float):
    """|d| equivalent of a printed effect size, for choosing a bin only."""
    v = abs(value)
    if kind in ("d", "g", "smd", "beta_std"):
        return v
    if kind == "r":
        return None if v >= 1 else 2 * v / math.sqrt(1 - v * v)
    if kind in ("eta2", "partial_eta2"):
        return None if v >= 1 else 2 * math.sqrt(v / (1 - v))
    if kind == "or":
        return None if value <= 0 else abs(math.log(value)) * math.sqrt(3) / math.pi
    return None


def bin_of(d: float) -> int:
    return 3 if d >= 0.8 else 2 if d >= 0.4 else 1 if d >= 0.2 else 0


LABEL = {3: "large effect", 2: "medium effect", 1: "small effect", 0: "negligible effect"}
KIND_SHOWN = {"d": "d", "g": "g", "smd": "SMD", "r": "r", "eta2": "η²", "partial_eta2": "partial η²",
              "or": "OR", "beta_std": "standardised β"}


def targets() -> list:
    """(claim, anchor) for each entry health_evidence.py flags, with its source text."""
    pages = clb.claim_pages()
    flagged = he.evidence(pages)["impact_no_statistic"]
    src, al = clb.sources_of(), clb.aliases(pages)
    out = []
    for e in flagged:
        slug, anchor = e.split("#", 1)
        arts = list(src.get(slug, []))
        for a in al.get(slug, []):
            arts += [s for s in src.get(a, []) if s not in arts]
        title, units = clb.units(pages[slug])
        block, subs = next((b, s) for a, b, s in units if a == anchor)
        hit = clb.cached_article(block, arts)
        basis, source, text = "none", None, None
        if hit:
            basis, source, text = "full text", hit[0], hit[1]
        else:
            m = clb.DOI_RE.search(block)
            if m:
                doi = m.group(0).rstrip(".,;")
                text = clb.openalex_abstract(doi)
                if text:
                    basis, source = "abstract", "doi:" + doi
        out.append({"claim": slug, "entry": anchor, "title": title, "block": block, "subs": subs,
                    "basis": basis, "source": source, "text": text})
    return out


def ask(t: dict, model: str, key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    text = t["text"] if len(t["text"]) <= MAX_TEXT else t["text"][:MAX_TEXT] + "\n[TRUNCATED]"
    prompt = (f"## The study ({t['basis']})\n{text}\n\n## The wiki claim\n{t['title']}\n\n"
              f"## The evidence entry\n{t['block']}\n\nSubclaims resting on it:\n" + "\n".join(t["subs"]))
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=3000)
    data = extract_json(gen.raw_text)
    return {"answer": data if isinstance(data, dict) else None, "cost_usd": gen.cost_usd}


def decide(t: dict, answer) -> dict:
    """The new code for one entry, from the model's answer checked against the text."""
    if t["basis"] == "none":
        return {"i": None, "why": "no source text available to check; the entry prints no effect size"}
    a = answer or {}
    if a.get("printed") and a.get("kind") in KINDS and isinstance(a.get("value"), (int, float)) \
            and isinstance(a.get("quote"), str):
        quote_ok = _norm(a["quote"]) in _norm(t["text"])
        value_ok = (_value_in(a["quote"], a["value"])
                    and bool(re.search(KIND_WORDS[a["kind"]], a["quote"], re.I))
                    and not re.search(r"R\s*²|R\^?2\b|variance explained", a["quote"]))
        d = as_d(a["kind"], float(a["value"])) if quote_ok and value_ok else None
        if d is not None:
            return {"i": bin_of(d), "kind": a["kind"], "value": a["value"], "quote": a["quote"],
                    "why": f"{KIND_SHOWN[a['kind']]} = {a['value']} printed in the {t['basis']}"}
        # The note is what a reader sees on the page; the rejected answer stays in the record.
        return {"i": None, "why": f"no effect size could be confirmed in the {t['basis']}", "rejected": a}
    if t["basis"] == "abstract":
        return {"i": None, "why": "the abstract prints no effect size; the full text may"}
    return {"i": None, "why": "the article prints no effect size for this finding"}


def _value_in(quote: str, value) -> bool:
    nums = [n.replace("−", "-") for n in re.findall(r"[-−]?\d*\.?\d+", quote)]
    for n in nums:
        try:
            if abs(float(n) - float(value)) < 1e-9 or abs(abs(float(n)) - abs(float(value))) < 1e-9:
                return True
        except ValueError:
            pass
    return False


CODES_LINE = re.compile(r"^`q[^\n]*`\s*$", re.M)
I_SPAN = re.compile(r"\bi[0-3](?:\s*·\s*[^`·]*?)?(?=\s*·\s*n=|\s*`)")


def new_i_text(dec: dict) -> str:
    if dec["i"] is None:
        return "i? · " + dec["why"]
    return f"i{dec['i']} · {LABEL[dec['i']]}, {KIND_SHOWN[dec['kind']]} = {dec['value']}"


def apply_one(claim: str, anchor: str, dec: dict) -> bool:
    path = WIKI_ROOT / "claims" / f"{claim}.md"
    text = path.read_text(encoding="utf-8")
    title, units = clb.units(path)
    block = next((b for a, b, _ in units if a == anchor), None)
    if block is None or block not in text:
        return False
    m = CODES_LINE.search(block)
    if not m:
        return False
    codes = m.group(0)
    new_codes, n = I_SPAN.subn(new_i_text(dec), codes, count=1)
    if n != 1:
        return False
    new_block = block.replace(codes, new_codes, 1)
    text = text.replace(block, new_block, 1)
    # Subclaims resting on this entry carry the same i.
    code = "?" if dec["i"] is None else str(dec["i"])
    text = re.sub(rf"^(`q\S*) i[0-3?](`[^\n]*\(#{re.escape(anchor)}\))",
                  lambda mm: f"{mm.group(1)} i{code}{mm.group(2)}", text, flags=re.M)
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="decide and report; write nothing to pages")
    ap.add_argument("--apply", action="store_true", help="write the decided codes")
    ap.add_argument("--from", dest="from_file", help="re-use decisions from an earlier run")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--limit", type=int, help="only the first N entries (a sample to read first)")
    ap.add_argument("--seed", type=int, default=0, help="with --limit, which sample")
    args = ap.parse_args()

    if args.from_file:
        decisions = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        key = os.environ.get("OPENROUTER_API_KEY")
        if not key:
            raise SystemExit("OPENROUTER_API_KEY is not set")
        ts = targets()
        if args.limit:
            import random
            random.Random(args.seed).shuffle(ts)
            ts = ts[:args.limit]
        print(f"{len(ts)} entries: " + ", ".join(f"{sum(1 for t in ts if t['basis'] == b)} {b}"
                                               for b in ("full text", "abstract", "none")), flush=True)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        decisions = []
        with args.out.open("w", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
            def work(t):
                if t["basis"] == "none":
                    return t, {"answer": None, "cost_usd": 0}
                try:
                    return t, ask(t, args.model, key)
                except Exception as e:
                    return t, {"answer": None, "cost_usd": 0, "error": f"{type(e).__name__}: {e}"[:200]}
            for t, res in ex.map(work, ts):
                if res.get("error"):
                    dec = {"claim": t["claim"], "entry": t["entry"], "error": res["error"]}
                else:
                    dec = {"claim": t["claim"], "entry": t["entry"], "basis": t["basis"], "source": t["source"],
                           "answer": res["answer"], "cost_usd": res["cost_usd"], **decide(t, res["answer"])}
                fh.write(json.dumps(dec, ensure_ascii=False) + "\n")
                fh.flush()
                decisions.append(dec)
        print(f"cost ${sum(d.get('cost_usd') or 0 for d in decisions):.3f}; decisions -> {args.out}")

    ok = [d for d in decisions if "error" not in d]
    tally = {}
    for d in ok:
        k = f"i{d['i']}" if d["i"] is not None else f"i? ({d['why'].split(';')[0]})"
        tally[k] = tally.get(k, 0) + 1
    print(f"{len(ok)} decided, {len(decisions) - len(ok)} errors:")
    for k, v in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"  {v:4}  {k}")
    if args.apply:
        written = sum(apply_one(d["claim"], d["entry"], d) for d in ok)
        print(f"wrote {written} of {len(ok)}")


if __name__ == "__main__":
    main()
