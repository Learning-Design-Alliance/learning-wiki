"""
pre_extractor_test.py — should the droplet extractor be updated, or should
extraction move into a Claude Code session?

Four arms read the same 19 articles (eval/pre-extractor-test/manifest.json):

  glm-v99     z-ai/glm-5.3-flash on CURRENT (v99): the droplet as it runs today
  glm-v130    the same model on v130: the droplet with the new criteria, untuned
  opus-v130   anthropic/claude-opus-5.5 on v130, headless, one call, no tools
  agent       a Claude Code subagent (Opus 5.5) on v130 with tools
              (scripts/eval/agent_arm.py)

glm-v130 against glm-v99 says what the criteria change costs the tuned
model. opus-v130 against glm-v130 isolates the model. agent against
opus-v130 isolates the tools: whole article, Crossref, quote self-checks.

Everything is scored by code this repo already trusts, plus two checks that
do not depend on an LLM's opinion:

  * quotes    every evidence `source_quote` is looked up in the article text.
              A quote that is not a substring is fabricated or mangled.
  * DOIs      every DOI in the output is resolved against Crossref and
              classified with resolve_doi_conflicts.classify_doi, the call
              the pipeline itself makes. `error` is reported separately and
              never counted as wrong (CLAUDE.md, settled).

The decision rule is written below, before the numbers, and the report
applies it mechanically.

    python3 -m scripts.eval.pre_extractor_test          # writes REPORT.md
"""

import json
import re
import statistics
import unicodedata
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WIKI_ROOT / "scripts"))

import check_citations as cc  # noqa: E402
import resolve_doi_conflicts as rdc  # noqa: E402
from scripts.eval import fetch_article  # noqa: E402

TEST_DIR = WIKI_ROOT / "eval" / "pre-extractor-test"
RUNS_DIR = WIKI_ROOT / "eval" / "runs"

ARMS = [
    ("glm-v99", "pxt-glm-v99", "z-ai/glm-5.3-flash"),
    ("glm-v130", "pxt-glm-v130", "z-ai/glm-5.3-flash"),
    ("opus-v130", "pxt-opus55-v130", "anthropic/claude-opus-5.5"),
    ("agent", "pxt-agent-opus55", "claude-code-agent/opus-5.5"),
]

DECISION_RULE = """\
Written before any result was read.

1. Quality comes first, and on the HOLDOUT set only. The benchmark is what
   130 prompt versions were tuned on, so it flatters glm-v99 by construction.
2. An arm is "clean" when fewer than 5% of its source_quotes fail the
   substring check and it asserts no DOI Crossref resolves to another paper.
   A fabricated quote or a wrong DOI is the failure mode this repo has lost
   weeks to; a better judge score does not buy it back.
3. Among clean arms, the best is the one with the highest mean judge score
   (GPT and Gemini averaged; no Anthropic judge scores an Anthropic arm).
   Any clean arm within 0.25 points of it counts as tied.
4. Among tied arms, the cheapest per 1,000 included articles wins.
5. Updating the droplet is worth it only if glm-v130 is in that tied set:
   then prompt tuning has a small gap to close and GLM's price wins. If it is
   not, the gap is what tuning would have to close, and v99 -> v126 did not
   raise GLM's judge score above 4.5 in 27 versions.
6. The reject probes (two biomedical papers) are reported, not scored into
   the rule: the headless contract cannot say "reject", so a headless arm
   producing zero contributions is the best it can do.
"""

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]]+")


def _norm(s: str) -> str:
    """Letters and digits only, after NFKC. PDF text breaks words across
    lines ("mem- ory", "testimo nial") and uses ligatures, and a verbatim
    copy of that text should not count as a fabrication; a paraphrase still
    fails, because it changes the letters."""
    s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"[^0-9a-z]+", "", s)


def quote_audit(parsed: dict, article_norm: str) -> tuple:
    quotes = []
    for c in parsed.get("contributions") or []:
        for e in c.get("evidence") or []:
            if isinstance(e, dict) and e.get("source_quote"):
                quotes.append(e["source_quote"])
    for o in (parsed.get("study_record") or {}).get("observations") or []:
        if isinstance(o, dict) and o.get("source_quote"):
            quotes.append(o["source_quote"])
    bad = [q for q in quotes if _norm(q) not in article_norm]
    return len(quotes), bad


def _dois(parsed: dict) -> set:
    blob = json.dumps({k: v for k, v in parsed.items() if k != "study_record"})
    return {d.rstrip(".,;)").lower() for d in DOI_RE.findall(blob)}


def doi_audit(parsed: dict, title: str, article_norm: str) -> dict:
    """Classify each DOI against the manifest title and, when the extraction's
    own article title is printed in the article, against that too: ERIC and
    PMC metadata often carry only a short title, and classify_doi's
    containment guard rightly refuses a short title as proof."""
    titles = [title]
    own = ((parsed.get("article") or {}).get("title") or "").strip()
    if own and _norm(own) in article_norm:
        titles.append(own)
    out = {"verified": [], "wrong_paper": [], "not_found": [], "error": []}
    for doi in sorted(_dois(parsed)):
        statuses = [rdc.classify_doi(doi, cc._words_from_text(t), t)["status"] for t in titles]
        status = "verified" if "verified" in statuses else statuses[0]
        out.setdefault(status, []).append(doi)
    return out


def load(run_id: str, model: str) -> dict:
    d = RUNS_DIR / run_id / model.replace("/", "__")
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in d.glob("*.json")} if d.exists() else {}


def _judge_mean(rec: dict):
    s = [v.get("average_score") for k, v in (rec.get("judges") or {}).items()
         if k in ("gpt", "gemini") and isinstance(v, dict) and v.get("average_score") is not None]
    return sum(s) / len(s) if s else None


def _judge_fails(rec: dict) -> int:
    return sum(1 for k, v in (rec.get("judges") or {}).items()
               if k in ("gpt", "gemini") and isinstance(v, dict) and v.get("verdict") == "fail")


def score_arm(label, run_id, model, articles, texts) -> dict:
    recs = load(run_id, model)
    rows = []
    for a in articles:
        r = recs.get(a["id"])
        row = {"id": a["id"], "set": a["test_set"], "present": r is not None}
        if r:
            p = r.get("parsed") or {}
            gen = r.get("generation") or {}
            n_q, bad_q = quote_audit(p, texts[a["id"]]) if p else (0, [])
            row.update({
                "gen_error": "error" in gen,
                "passed": (r.get("validation") or {}).get("passed"),
                "completeness": (r.get("validation") or {}).get("completeness_score"),
                "n_contrib": len(p.get("contributions") or []),
                "has_study_record": bool(p.get("study_record")),
                "rejected": (p.get("inclusion") or {}).get("verdict") == "reject",
                "judge": _judge_mean(r),
                "judge_fails": _judge_fails(r),
                "quotes": n_q, "bad_quotes": bad_q,
                "dois": doi_audit(p, a["title"], texts[a["id"]]) if p else {},
                "cost": gen.get("cost_usd"),
                "cost_bracket": gen.get("cost_bracket_usd"),
                "latency": gen.get("latency_s"),
                "tokens": gen.get("total_tokens") or ((gen.get("prompt_tokens") or 0) + (gen.get("completion_tokens") or 0)),
            })
        rows.append(row)
    return {"label": label, "rows": rows}


def summarise(arm: dict, subset: str) -> dict:
    rows = [r for r in arm["rows"] if r["present"] and (subset == "all-included" and r["set"] != "reject-probe"
                                                        or r["set"] == subset)]
    if not rows:
        return {}
    judged = [r["judge"] for r in rows if r.get("judge") is not None]
    nq = sum(r["quotes"] for r in rows)
    nbad = sum(len(r["bad_quotes"]) for r in rows)
    doi = {k: sum(len(r["dois"].get(k, [])) for r in rows) for k in ("verified", "wrong_paper", "not_found", "error")}
    costs = [r["cost"] or 0 for r in rows]
    lats = [r["latency"] for r in rows if r.get("latency")]
    return {
        "n": len(rows),
        "gen_errors": sum(1 for r in rows if r.get("gen_error")),
        "pass_rate": sum(1 for r in rows if r.get("passed")) / len(rows),
        "completeness": statistics.mean(r.get("completeness") or 0 for r in rows),
        "judge": statistics.mean(judged) if judged else None,
        "judged": len(judged),
        "judge_fails": sum(r.get("judge_fails", 0) for r in rows),
        "contrib": statistics.mean(r.get("n_contrib", 0) for r in rows),
        "study_records": sum(1 for r in rows if r.get("has_study_record")),
        "quotes": nq, "bad_quotes": nbad, "bad_quote_rate": nbad / nq if nq else 0.0,
        "doi": doi,
        "cost_per_article": statistics.mean(costs),
        "cost_low": statistics.mean((r.get("cost_bracket") or {}).get("low_usd", r["cost"] or 0) for r in rows),
        "cost_high": statistics.mean((r.get("cost_bracket") or {}).get("high_usd", r["cost"] or 0) for r in rows),
        "latency": statistics.median(lats) if lats else None,
    }


def _f(x, fmt="{:.2f}", none="—"):
    return none if x is None else fmt.format(x)


def decide(summaries: dict) -> list:
    lines = []
    clean = {k: s for k, s in summaries.items() if s and s["bad_quote_rate"] < 0.05 and s["doi"]["wrong_paper"] == 0}
    for k, s in summaries.items():
        if s and k not in clean:
            lines.append(f"- **{k}** is not clean: {s['bad_quotes']}/{s['quotes']} quotes not in the article, "
                         f"{s['doi']['wrong_paper']} DOI(s) resolving to another paper.")
    judged = {k: s for k, s in clean.items() if s["judge"] is not None}
    if not judged:
        lines.append("- No clean arm has a judge score, so the rule cannot pick a winner.")
        return lines
    best = max(judged, key=lambda k: judged[k]["judge"])
    tied = [k for k, s in judged.items() if s["judge"] >= judged[best]["judge"] - 0.25]
    lines.append(f"- Highest judge score among clean arms: **{best}** ({judged[best]['judge']:.2f}). "
                 f"Tied within 0.25: {', '.join(tied)}.")
    cheapest = min(tied, key=lambda k: judged[k]["cost_per_article"])
    lines.append(f"- Cheapest of the tied arms: **{cheapest}**.")
    if "glm-v130" in tied:
        lines.append("- glm-v130 is in the tied set, so **updating the droplet extractor is worth it** on quality grounds.")
    elif (summaries.get("glm-v130") or {}).get("judge") is None:
        lines.append("- glm-v130 has no scored output, so the rule cannot yet say whether updating the droplet is worth it.")
    else:
        lines.append("- glm-v130 is **not** in the tied set: updating the droplet means closing a "
                     f"{judged[best]['judge'] - (summaries.get('glm-v130') or {}).get('judge', 0):.2f}-point gap by prompt tuning"
                     + ("" if "glm-v130" in clean else ", and it also fails the cleanliness gate") + ".")
    return lines


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-wall", nargs="*", default=[],
                    help="label=seconds, the wall-clock each arm's whole batch took")
    args = ap.parse_args()
    walls = dict(x.split("=") for x in args.batch_wall)
    for label, run_id, _ in ARMS:
        f = RUNS_DIR / run_id / "batch_wall.json"
        if label not in walls and f.exists():
            walls[label] = json.loads(f.read_text(encoding="utf-8"))["seconds"]

    articles = json.loads((TEST_DIR / "manifest.json").read_text(encoding="utf-8"))["articles"]
    texts = {a["id"]: _norm(fetch_article.fetch_article_text(a)) for a in articles}
    arms = [score_arm(l, r, m, articles, texts) for l, r, m in ARMS]

    out = ["# Pre-extractor test — report", "",
           "Generated by `python3 -m scripts.eval.pre_extractor_test`. Arms and method are in that "
           "script's docstring; per-article records are under `eval/runs/pxt-*` (not committed).", "",
           "## Decision rule", "", DECISION_RULE]

    for subset in ("holdout", "benchmark", "all-included"):
        out += [f"## {subset}", "",
                "| arm | n | gen err | validator pass | completeness | judge (GPT+Gemini) | judge fails | contribs/article | study_record | quotes not in article | DOIs verified / wrong / 404 / lookup failed | $/article | median s/article |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for arm in arms:
            s = summarise(arm, subset)
            if not s:
                out.append(f"| {arm['label']} | 0 | | | | | | | | | | | |")
                continue
            cost = (f"${s['cost_low']:.3f}–{s['cost_high']:.3f}" if arm["label"] == "agent"
                    else f"${s['cost_per_article']:.4f}")
            d = s["doi"]
            out.append(f"| {arm['label']} | {s['n']} | {s['gen_errors']} | {s['pass_rate']:.0%} | {s['completeness']:.2f} | "
                       f"{_f(s['judge'])} ({s['judged']}) | {s['judge_fails']} | {s['contrib']:.1f} | {s['study_records']}/{s['n']} | "
                       f"{s['bad_quotes']}/{s['quotes']} ({s['bad_quote_rate']:.0%}) | "
                       f"{d['verified']} / {d['wrong_paper']} / {d['not_found']} / {d['error']} | {cost} | {_f(s['latency'], '{:.0f}')} |")
        out.append("")

    out += ["## Reject probes", "", "| arm | article | contributions | rejected |", "|---|---|---|---|"]
    for arm in arms:
        for r in arm["rows"]:
            if r["set"] == "reject-probe" and r["present"]:
                out.append(f"| {arm['label']} | {r['id']} | {r.get('n_contrib')} | {r.get('rejected')} |")
    out.append("")

    hold = {arm["label"]: summarise(arm, "holdout") for arm in arms}
    allinc = {arm["label"]: summarise(arm, "all-included") for arm in arms}
    out += ["## Cost and time per 1,000 articles", "",
            "From the all-included rows. Agent cost is a bracket (all context a cache read, vs all fresh input), "
            "because a subagent reports only total tokens. On a Claude subscription the marginal dollar cost is "
            "zero and the constraint is the plan's usage limit instead.", "",
            "| arm | $ per 1,000 | batch wall-clock (this test) |", "|---|---|---|"]
    for arm in arms:
        s = allinc[arm["label"]]
        if not s:
            continue
        c = (f"${s['cost_low'] * 1000:,.0f}–{s['cost_high'] * 1000:,.0f}" if arm["label"] == "agent"
             else f"${s['cost_per_article'] * 1000:,.2f}")
        w = walls.get(arm["label"])
        out.append(f"| {arm['label']} | {c} | {f'{float(w) / 60:.0f} min' if w else '—'} |")
    out += ["", "## What the rule says (holdout)", ""] + decide(hold) + [""]

    out += ["## Quotes not found in the article", "",
            "Every quote the substring check failed, so a reader can see whether it is a fabrication or a "
            "PDF-extraction artefact (ligatures, broken hyphenation) before trusting the column.", ""]
    for arm in arms:
        for r in arm["rows"]:
            for q in r.get("bad_quotes") or []:
                out.append(f"- **{arm['label']}** `{r['id']}`: {q[:220]}")
    out += ["", "## DOIs that did not verify", ""]
    for arm in arms:
        for r in arm["rows"]:
            for k in ("wrong_paper", "not_found"):
                for doi in (r.get("dois") or {}).get(k, []):
                    out.append(f"- **{arm['label']}** `{r['id']}`: {k} `{doi}`")
    (TEST_DIR / "REPORT.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {(TEST_DIR / 'REPORT.md').relative_to(WIKI_ROOT)}")


if __name__ == "__main__":
    main()
