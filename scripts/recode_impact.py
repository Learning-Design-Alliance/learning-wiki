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

`--fill` runs the other direction (2026-10-13): entries coded `i?` whose study's full text is
cached, where the paper may print an effect size the extraction missed (14,843 of them). The same
verbatim and bin rules apply, and a second model (`--confirm-model`) must return the same kind and
value on its own, because a quote can be genuine and belong to another finding. An entry is
changed only when both agree on a printed statistic; every other answer leaves it as it was.
Measured before a full run (2026-10-13): 3 of 150 random entries and 2 of 150 causal,
quant-synthesis or associational ones gained a confirmed statistic ($0.40 a sample). In 133 of the
first 150 the paper prints no effect size for that finding (means, F tests, p values), so the gap
is mostly the literature's, and a full run (~7,900 entries, ~$21) was judged not worth it. The
second model rejected real mistakes in those samples: a baseline-equivalence g taken for the
outcome, and one end of a printed range taken as the value.

    python3 scripts/recode_impact.py --fill --limit 200 --check   # a sample, read before applying
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
    "d": r"\bd\b|cohen|effect[- ]size|dbar|d̄", "g": r"\bg\b|hedges|effect[- ]size|ḡ|gbar",
    "smd": r"smd|standardi[sz]ed mean|effect[- ]size|standard deviation",
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


FILL_SYSTEM = SYSTEM.replace(
    "The entry codes an effect size (i1 small, i2 medium, i3 large) but prints no statistic.",
    "The entry records no effect size (i?). The study may print one the entry missed.")


def fill_targets() -> list:
    """(claim, anchor) for each entry coded i? whose study's full text is cached."""
    pages = clb.claim_pages()
    src, al = clb.sources_of(), clb.aliases(pages)
    out = []
    for slug, path in pages.items():
        arts = list(src.get(slug, []))
        for a in al.get(slug, []):
            arts += [x for x in src.get(a, []) if x not in arts]
        if not arts:
            continue
        title, units = clb.units(path)
        raw = path.read_text(encoding="utf-8")
        for anchor, block, subs in units:
            m = CODES_LINE.search(block)
            if not m or not re.search(r"\bi\?", m.group(0)):
                continue
            # Only kinds that report effect sizes: in a 150-entry sample 133 printed none, most of them
            # qualitative, descriptive or design entries. units() leaves the kind span out of the block,
            # so it is read from the page's own codes line.
            head = block.split("\n", 1)[0]
            at = raw.find(head + "\n")
            line = re.search(r"^`q[^\n]*$", raw[at:at + 3000], re.M) if at >= 0 else None
            if not line or not re.search(r"`(?:causal|quant-synthesis|associational) · r", line.group(0)):
                continue
            hit = clb.cached_article(block, arts)
            if hit:
                out.append({"claim": slug, "entry": anchor, "title": title, "block": block, "subs": subs,
                            "basis": "full text", "source": hit[0], "text": hit[1]})
    return out


def ask(t: dict, model: str, key: str, system: str = None) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    text = t["text"] if len(t["text"]) <= MAX_TEXT else t["text"][:MAX_TEXT] + "\n[TRUNCATED]"
    prompt = (f"## The study ({t['basis']})\n{text}\n\n## The wiki claim\n{t['title']}\n\n"
              f"## The evidence entry\n{t['block']}\n\nSubclaims resting on it:\n" + "\n".join(t["subs"]))
    gen = oc.generate(model, system or SYSTEM, prompt, key, max_tokens=3000)
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
I_SPAN = re.compile(r"\bi[0-3](?:-i[0-3?])?(?:\s*·\s*[^`·]*?)?(?=\s*·\s*n=|\s*`)")


def new_i_text(dec: dict) -> str:
    if dec["i"] is None:
        return "i? · " + dec["why"]
    return f"i{dec['i']} · {LABEL[dec['i']]}, {KIND_SHOWN[dec['kind']]} = {dec['value']}"


def set_subclaims(text: str, anchor: str, dec: dict) -> str:
    """Give the subclaims resting on `anchor` the entry's i. They may link the heading's
    slug with its accents folded (#hilppo-stevens-2024 for "Hilppö & Stevens 2024"),
    since fix_dead_anchors.py repairs links that way."""
    import unicodedata
    folded = unicodedata.normalize("NFKD", anchor).encode("ascii", "ignore").decode()
    code = "?" if dec["i"] is None else str(dec["i"])
    for a in {anchor, folded}:
        text = re.sub(rf"^(`q\S*) i[0-3?](`[^\n]*\(#{re.escape(a)}\))",
                      lambda mm: f"{mm.group(1)} i{code}{mm.group(2)}", text, flags=re.M)
    return text


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
    text = set_subclaims(text, anchor, dec)
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
    ap.add_argument("--redecide", action="store_true", help="with --from, re-apply the rules to the stored answers")
    ap.add_argument("--limit", type=int, help="only the first N entries (a sample to read first)")
    ap.add_argument("--seed", type=int, default=0, help="with --limit, which sample")
    ap.add_argument("--fill", action="store_true",
                    help="i? entries with cached full text: fill an effect size both models confirm")
    ap.add_argument("--confirm-model", default="z-ai/glm-5.3-flash",
                    help="with --fill, the second model that must return the same statistic")
    args = ap.parse_args()
    if args.fill:
        return fill(args)

    if args.from_file:
        decisions = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
        if args.redecide:
            # Re-run decide() on the stored answers, e.g. after a rule changed; no model call.
            by = {(t["claim"], t["entry"]): t for t in targets()}
            for d in decisions:
                t = by.get((d["claim"], d["entry"]))
                if t and "error" not in d:
                    for k in ("i", "why", "kind", "value", "quote", "rejected"):
                        d.pop(k, None)
                    d.update(decide(t, d.get("answer")))
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


def fill(args) -> None:
    """The --fill direction: never writes an i?, only a statistic two models agree on."""
    out = args.out if args.out != OUT else OUT.with_name("fill.ndjson")
    decisions = [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines() if l.strip()] \
        if out.exists() else []
    if not args.from_file:
        key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
        done = {(d["claim"], d["entry"]) for d in decisions}
        ts = [t for t in fill_targets() if (t["claim"], t["entry"]) not in done]
        if args.limit:
            import random
            random.Random(args.seed).shuffle(ts)
            ts = ts[:args.limit]
        print(f"{len(ts)} i? entries with full text to check ({len(done)} already decided)", flush=True)

        def work(t):
            try:
                first = ask(t, args.model, key, FILL_SYSTEM)
                dec = decide(t, first["answer"])
                cost = first["cost_usd"] or 0
                if dec["i"] is not None:
                    second = ask(t, args.confirm_model, key, FILL_SYSTEM)
                    cost += second["cost_usd"] or 0
                    other = decide(t, second["answer"])
                    same = (other["i"] is not None and other.get("kind") == dec["kind"]
                            and abs(float(other["value"]) - float(dec["value"])) < 1e-9)
                    if not same:
                        dec = {"i": None, "why": "the second model did not return the same statistic",
                               "rejected": first["answer"], "second": second["answer"]}
                return {"claim": t["claim"], "entry": t["entry"], "source": t["source"],
                        "answer": first["answer"], "cost_usd": cost, **dec}
            except Exception as e:  # noqa: BLE001 - a failed call decides nothing
                return {"claim": t["claim"], "entry": t["entry"], "error": f"{type(e).__name__}: {e}"[:200]}

        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
            futs = [ex.submit(work, t) for t in ts]
            for n, fut in enumerate(concurrent.futures.as_completed(futs), 1):
                dec = fut.result()
                fh.write(json.dumps(dec, ensure_ascii=False) + "\n")
                fh.flush()
                decisions.append(dec)
                if n % 500 == 0:
                    print(n, flush=True)
    found = [d for d in decisions if "error" not in d and d.get("i") is not None]
    print(f"{len(decisions)} decided; {len(found)} with a printed effect size both models confirmed; "
          f"{sum(1 for d in decisions if 'error' in d)} errors; cost ${sum(d.get('cost_usd') or 0 for d in decisions):.2f}")
    for k in (3, 2, 1, 0):
        print(f"  i{k}: {sum(1 for d in found if d['i'] == k)}")
    if args.apply:
        written = sum(apply_one(d["claim"], d["entry"], d) for d in found)
        print(f"wrote {written} of {len(found)}")


if __name__ == "__main__":
    main()
