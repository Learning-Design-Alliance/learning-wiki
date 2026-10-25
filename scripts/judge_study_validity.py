#!/usr/bin/env python3
"""
judge_study_validity.py — does a causal claim rest on a study that can carry it?

The load-bearing judge (check_load_bearing.py) asks whether an evidence entry says what
its study says. This asks the next question, the one an audit of AI-in-education
meta-analyses (O'Neill, preprint, 2026) found failing in 61% of the primary studies it
vetted: does the study measure what the claim says it found, and does its design let
that be attributed to the thing the claim names? Four checks, the audit's own
categories, on one evidence entry of a causal claim against its study's text:

  outcome      the claim says learning, achievement or skill improved, and the study
               measured perceptions, satisfaction, self-efficacy, motivation or anxiety
               (a Likert scale of perceived learning is not learning). The commonest
               failure the audit found (15 of 59 studies).
  comparison   what the effect was measured against: a randomised group, a
               non-randomised group, the same group before (pre-post), nothing, or a
               group that also used the intervention.
  isolation    the intervention arrived bundled with something else that could explain
               the effect (an AI tool together with gamification, a new curriculum, extra
               time), so the claim's cause is not separable.
  unit         the analysis counted students where classes, teams or schools were what
               was assigned, inflating n.

The judge reports what it read; it never edits a page. A finding goes to a person or
agent, who acts on it as eval/source-validity/README.md says: retitle the claim to what
was measured, add the design's limit to the entry, correct a q that overstates the design,
or remove a claim nothing in the study supports. Verdicts are cached per entry text and
source, so a re-run pays only for what changed.

    python3 scripts/judge_study_validity.py --scope ai --budget 5          # AI-era causal entries
    python3 scripts/judge_study_validity.py --scope causal --budget 60     # every causal entry
    python3 scripts/judge_study_validity.py --new                          # a batch's new claims
    python3 scripts/judge_study_validity.py --claims slug-a slug-b
    python3 scripts/judge_study_validity.py --report [--all]
    python3 scripts/judge_study_validity.py --annotate --apply   # the Design limits line, from agreed findings
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

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import check_load_bearing as clb  # noqa: E402

OUT = WIKI_ROOT / "eval" / "runs" / "study-validity" / "judged.ndjson"
# Every entry the first judge flags is judged again by a model from another provider, and
# only a problem both report counts (the repo's rule for acting on a model's reading:
# judge_claim_merges.py, sort_claims.py). Measured 2026-10-25 on 1,303 AI-era entries: the
# first judge alone flagged 42%, its "bundled intervention" reading most liberally.
CONFIRM = WIKI_ROOT / "eval" / "runs" / "study-validity" / "confirmed.ndjson"
SECOND = "deepseek/deepseek-v4-pro"
REVIEWED = WIKI_ROOT / "eval" / "source-validity" / "study-reviewed.ndjson"
COVERAGE = WIKI_ROOT / "eval" / "source-validity" / "coverage.json"
AI = re.compile(r"chat\s*-?gpt|generative (?:ai|artificial)|gen-?ai\b|large language model|\bLLMs?\b|"
                r"chatbot|artificial intelligence|\bAI\b|intelligent tutor|\bGPT", re.I)
CAUSAL = re.compile(r"`causal\s*·\s*r[1-3?]`")
OUTCOMES = ("performance", "self-report", "behaviour", "affective-clinical", "mixed", "unclear")
COMPARISONS = ("randomised", "non-randomised-groups", "pre-post-single-group", "none",
               "comparison-also-treated", "unclear")

SYSTEM = """\
You are auditing one evidence entry on a learning-science wiki page against the study it \
cites. The page makes a causal claim. Your job is not to check the wording (another judge \
does that) but whether the STUDY, as reported, can carry a claim of this kind. Read the \
study, then answer from it, quoting it.

1. outcome_measured: what the study actually measured as the outcome the claim rests on.
   performance = a test, task, graded work or other measured performance;
   self-report = questionnaire or Likert ratings of perceived learning, satisfaction, \
attitudes, self-efficacy, motivation, engagement;
   behaviour = observed or logged behaviour (time on task, usage, participation);
   affective-clinical = anxiety, depression, wellbeing scales;
   mixed = more than one of these, with the claim resting on both; unclear = cannot tell.
2. claim_says: what kind of outcome the claim (title and subclaims) says improved, using \
the same words.
3. outcome_mismatch: true when the claim says learning, achievement, skill or knowledge \
improved and the study measured only self-report, behaviour or affective outcomes for it.
4. comparison: what the effect was measured against.
   randomised = participants or clusters randomly assigned to conditions;
   non-randomised-groups = intact or self-selected groups;
   pre-post-single-group = one group measured before and after;
   none = no comparison at all; comparison-also-treated = the comparison group also \
received the intervention the claim names; unclear.
5. isolated: false when the intervention the claim names came bundled with another \
change (another tool, gamification, a new curriculum, more time, a different teacher) \
that could explain the effect, so the claim's cause cannot be separated. Say what it \
was bundled with.
6. unit_issue: true when conditions were assigned to classes, teams, schools or other \
groups but the analysis treats students as independent (n counted in students), or when \
the reported n is not the unit analysed. Give both numbers if the study states them.
7. design_overstated: true when the wiki entry describes a stronger design than the \
study reports (calls it randomised or experimental when it is not, or gives a control \
group the study lacks).

Report only what the text supports. If the text is an abstract and does not say, \
answer unclear rather than guessing. Reply with JSON only:
{"outcome_measured": "...", "claim_says": "...", "outcome_mismatch": true|false,
 "comparison": "...", "isolated": true|false, "bundled_with": "" ,
 "unit_issue": true|false, "unit_detail": "",
 "design_overstated": true|false,
 "quotes": ["short quotes from the study supporting the answers"],
 "summary": "one sentence a person can act on, or empty if nothing is wrong"}"""


def judge(job, model, key):
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    r, anchor, title, block, subs, source, basis, text, dg, pdg = job
    text = text if len(text) <= clb.MAX_ARTICLE else text[:clb.MAX_ARTICLE] + "\n\n[TRUNCATED]"
    prompt = (f"## The study ({basis}: {source})\n{text}\n\n## Wiki page claims/{r['claim']}.md\n"
              f"Claim: {title}\n\nSubclaims resting on this study:\n" + ("\n".join(subs) or "(none)")
              + f"\n\nEvidence entry:\n{block}")
    # the second model reasons at length before its JSON; 3000 tokens cut 113 replies short
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=3000 if model != SECOND else 9000)
    data = extract_json(gen.raw_text)
    if not isinstance(data, dict) or data.get("outcome_measured") not in OUTCOMES \
            or data.get("comparison") not in COMPARISONS:
        return {"error": "malformed reply", "cost_usd": gen.cost_usd}
    return {**{k: data.get(k) for k in ("outcome_measured", "claim_says", "outcome_mismatch", "comparison",
                                         "isolated", "bundled_with", "unit_issue", "unit_detail",
                                         "design_overstated", "quotes", "summary")},
            "cost_usd": gen.cost_usd}


def causal_anchors(path) -> set:
    """Anchors of the entries coded `causal`: units() drops the kind span, so read it here."""
    import okf_lib
    body = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    ev = okf_lib.get_section(body, "Evidence") or ""
    out = set()
    for chunk in re.split(r"(?m)^### ", ev)[1:]:
        heading, _, rest = chunk.partition("\n")
        if CAUSAL.search(rest):
            out.add(okf_lib.slugify(heading.strip()))
    return out


def problems(v: dict) -> list:
    out = []
    if v.get("outcome_mismatch"):
        out.append("outcome")
    if v.get("comparison") in ("none", "comparison-also-treated"):
        out.append("comparison")
    if v.get("isolated") is False and (v.get("bundled_with") or "").strip():
        out.append("isolation")       # an unnamed confound is the comparison's problem, not this one
    if v.get("unit_issue"):
        out.append("unit")
    if v.get("design_overstated"):
        out.append("design")
    return out


def agreed(v: dict, confirmed: dict):
    """The problems both judges report for this entry; None until the second has judged it."""
    first = problems(v)
    if not first:
        return []
    c = confirmed.get(v["digest"])
    if c is None or "error" in c:
        return None
    return [p for p in first if p in problems(c)]


def current_digests(claims) -> set:
    out = set()
    for c in claims:
        path = WIKI_ROOT / "claims" / f"{c}.md"
        if path.exists():
            title, entries = clb.units(path)
            out |= {clb.page_digest(c, title, b, s) for a, b, s in entries}
    return out


def open_findings(judged=None, confirmed=None, done=None):
    """Entries with an agreed problem nobody has decided, and entries awaiting the second judge."""
    judged = load(OUT) if judged is None else judged
    confirmed = load(CONFIRM) if confirmed is None else confirmed
    done = reviewed() if done is None else done
    rows, waiting = [], 0
    # Only verdicts on the page as it stands: a retitled or rewritten entry has a new
    # digest, and the verdict on its old text no longer says anything about it.
    current = current_digests({v["claim"] for v in judged.values()})
    for v in judged.values():
        if "error" in v or v["page_digest"] in done or v["page_digest"] not in current:
            continue
        a = agreed(v, confirmed)
        if a is None:
            waiting += 1
        elif a:
            rows.append({**v, "agreed": a, "second": confirmed[v["digest"]]})
    return rows, waiting


def load(path):
    out = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            out[rec["digest"]] = rec
    return out


def reviewed():
    out = {}
    if REVIEWED.exists():
        for line in REVIEWED.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            out[rec["page_digest"]] = rec
    return out


def select(pages, scope, claims, new):
    if claims:
        return [c for c in claims if c in pages]
    if new:
        import link_learner_variables as llv
        return [c for c in llv.new_claims() if c in pages]
    out = []
    for slug, p in pages.items():
        t = p.read_text(encoding="utf-8", errors="replace")
        if not CAUSAL.search(t):
            continue
        if scope == "ai" and not AI.search(t.split("## Evidence", 1)[0][:4000]):
            continue
        out.append(slug)
    return out


def report(show_all):
    judged = load(OUT)
    rows, waiting = open_findings(judged)
    c = collections.Counter(p for v in rows for p in v["agreed"])
    print(f"# Study validity: {len(judged)} entries judged, {len(rows)} with a problem both judges report "
          f"and nobody has decided" + (f", {waiting} awaiting the second judge" if waiting else ""))
    print("  " + ", ".join(f"{k} {n}" for k, n in c.most_common()))
    print()
    if show_all:
        for v in sorted(rows, key=lambda v: (-len(v["agreed"]), v["claim"])):
            print(f"- claims/{v['claim']}.md#{v['entry']}  [{', '.join(v['agreed'])}]")
            print(f"    {v.get('summary') or ''}")
            print(f"    second: {v['second'].get('summary') or ''}")
            print(f"    measured {v.get('outcome_measured')}; claim says {v.get('claim_says')}; "
                  f"comparison {v.get('comparison')}"
                  + (f"; bundled with {v['bundled_with']}" if v.get("bundled_with") else "")
                  + (f"; unit: {v['unit_detail']}" if v.get("unit_detail") else ""))
    return 1 if rows or waiting else 0


# Problems the page states rather than fixes: the study may report what the claim says, and a
# reader needs its limit. The other two (outcome, design) mean the page itself is wrong and are
# left open for a person or agent to rewrite.
STATED = ("comparison", "isolation", "unit")
LIMIT_TEXT = {
    "comparison": lambda v: ("no comparison group" if v.get("comparison") == "none"
                             else "the comparison group also received the intervention"),
    "isolation": lambda v: "the intervention came bundled with another change"
                           + (f" ({v['bundled_with'].strip().rstrip('.')})"
                              if 0 < len((v.get("bundled_with") or "").strip()) <= 90 else ""),
    "unit": lambda v: "groups were assigned but students were analysed as independent",
}
LIMITS_RE = re.compile(r"^>\s*\*\*Design limits\*\*\s*·")
HEADER_RE = re.compile(r"^>\s*\*\*(?:Claim|Evidence|Currency)\*\*")


def limits_line(path, verdicts):
    """The `> **Design limits** ·` line for a claim: per entry, the problems both judges agree
    on that a page states rather than fixes, keyed by the entry's heading."""
    import okf_lib
    heads = {okf_lib.slugify(h.strip()): h.strip()
             for h in re.findall(r"(?m)^### (.+)$", path.read_text(encoding="utf-8"))}
    parts = []
    for v in sorted(verdicts, key=lambda v: v["entry"]):
        texts = [LIMIT_TEXT[p](v) for p in v["agreed"] if p in STATED]
        if texts and v["entry"] in heads:
            parts.append(f"{heads[v['entry']]}: " + "; ".join(texts))
    if not parts:
        return None
    return ("> **Design limits** · " + " · ".join(parts)
            + f" (read from the study by two models, {max(v['judged_at'] for v in verdicts)})")


def annotate(pages, apply):
    """Write or refresh the Design limits line on every claim with an agreed, stated problem,
    and record those findings as decided: the page now says them."""
    judged, confirmed = load(OUT), load(CONFIRM)
    by_claim = collections.defaultdict(list)
    for v in judged.values():
        if "error" in v or v["claim"] not in pages:
            continue
        a = agreed(v, confirmed)
        if a:
            by_claim[v["claim"]].append({**v, "agreed": a})
    done, written, recorded = reviewed(), 0, []
    for claim, vs in sorted(by_claim.items()):
        path = pages[claim]
        # only verdicts on the entry text as it stands now
        title, entries = clb.units(path)
        current = {a: clb.page_digest(claim, title, b, s) for a, b, s in entries}
        vs = [v for v in vs if current.get(v["entry"]) == v["page_digest"]]
        want = limits_line(path, vs)
        lines = path.read_text(encoding="utf-8").split("\n")
        at = next((i for i, l in enumerate(lines) if LIMITS_RE.match(l)), None)
        if at is None:
            last = max((i for i, l in enumerate(lines[:80]) if HEADER_RE.match(l)), default=None)
            if want is None or last is None:
                continue
            lines.insert(last + 1, want)
        elif want is None:
            del lines[at]
        elif lines[at] == want:
            continue
        else:
            lines[at] = want
        written += 1
        if apply:
            path.write_text("\n".join(lines), encoding="utf-8")
            for v in vs:
                if set(v["agreed"]) <= set(STATED) and v["page_digest"] not in done:
                    recorded.append({"claim": claim, "entry": v["entry"], "page_digest": v["page_digest"],
                                     "decision": "stated", "reason": "stated on the page as a design limit: "
                                     + ", ".join(v["agreed"]), "by": "process:study-validity",
                                     "at": time.strftime("%Y-%m-%d")})
    if apply and recorded:
        REVIEWED.parent.mkdir(parents=True, exist_ok=True)
        with REVIEWED.open("a", encoding="utf-8") as fh:
            for r in recorded:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Design limits line {'written' if apply else 'to write'} on {written} claims; "
          f"{len(recorded)} findings recorded as stated")


def dismiss(target, reason, by, pages):
    claim, _, anchor = target.partition("#")
    claim = claim.removeprefix("claims/").removesuffix(".md")
    title, entries = clb.units(pages[claim])
    match = [(b, s) for a, b, s in entries if a == anchor]
    if not match:
        raise SystemExit(f"claims/{claim}.md has no evidence entry #{anchor}")
    rec = {"claim": claim, "entry": anchor, "page_digest": clb.page_digest(claim, title, *match[0]),
           "decision": "checked", "reason": reason, "by": by, "at": time.strftime("%Y-%m-%d")}
    REVIEWED.parent.mkdir(parents=True, exist_ok=True)
    with REVIEWED.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"recorded claims/{claim}.md#{anchor} as checked")


def run_pool(todo, model, out, budget, concurrency, key):
    spent, n = 0.0, 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as ex, out.open("a", encoding="utf-8") as fh:
        futs = {}
        it = iter(todo)

        def submit():
            j = next(it, None)
            if j is not None:
                futs[ex.submit(judge, j, model, key)] = j
        for _ in range(concurrency):
            submit()
        while futs:
            fut = next(concurrent.futures.as_completed(list(futs)))
            j = futs.pop(fut)
            try:
                v = fut.result()
            except Exception as e:      # a failed call is retried next run, never recorded as a pass
                print(f"  {j[0]['claim']}#{j[1]}: {e}", file=sys.stderr)
                v = None
            if v is not None:
                spent += v.get("cost_usd") or 0
                if "error" not in v:
                    rec = {"claim": j[0]["claim"], "entry": j[1], "source": j[5], "basis": j[6],
                           "digest": j[8], "page_digest": j[9], "model": model,
                           "judged_at": time.strftime("%Y-%m-%d"), **v}
                    fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    fh.flush()
                n += 1
                if n % 100 == 0:
                    print(f"  {model}: {n}/{len(todo)} ${spent:.2f}", file=sys.stderr)
            if spent < budget:
                submit()
    return spent, n


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scope", choices=["ai", "causal"], default="ai")
    ap.add_argument("--claims", nargs="+")
    ap.add_argument("--new", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--budget", type=float, default=5.0)
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--offline", action="store_true", default=True,
                    help="use only cached texts and abstracts (default)")
    ap.add_argument("--annotate", action="store_true",
                    help="write the Design limits line from agreed findings (with --apply)")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dismiss", metavar="CLAIM#ENTRY", help="record that a finding was read and handled")
    ap.add_argument("--reason", default="")
    ap.add_argument("--by", default="claude/unspecified")
    a = ap.parse_args()
    pages = {p.stem: p for p in (WIKI_ROOT / "claims").glob("*.md") if p.stem != "index"}
    if a.dismiss:
        if not a.reason:
            raise SystemExit("--reason is required")
        dismiss(a.dismiss, a.reason, a.by, pages)
        return
    if a.report:
        sys.exit(report(a.all))
    if a.annotate:
        annotate(pages, a.apply)
        return
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set")
    want = set(select(pages, a.scope, a.claims, a.new))
    rows = [r for r in clb.ranking(pages) if r["claim"] in want]
    jobs, skipped = clb.entry_jobs(rows, pages, offline=a.offline)
    # only the causal entries of those claims
    anchors = {c: causal_anchors(pages[c]) for c in want}
    jobs = [j for j in jobs if j[1] in anchors[j[0]["claim"]]]
    done = load(OUT)
    todo = [j for j in jobs if j[8] not in done]
    print(f"{len(want)} claims, {len(jobs)} causal entries with a text, {len(todo)} to judge "
          f"(no text: {sum(v for k, v in skipped.items() if not k.startswith('_'))})", file=sys.stderr)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    spent, n = run_pool(todo, a.model, OUT, a.budget, a.concurrency, key)
    # the second judge, on every entry the first flagged and it has not yet read
    judged, confirmed = load(OUT), load(CONFIRM)
    flagged = [j for j in jobs if j[8] in judged and problems(judged[j[8]]) and j[8] not in confirmed]
    if flagged and spent < a.budget:
        print(f"second judge ({SECOND}) on {len(flagged)} flagged entries", file=sys.stderr)
        s2, n2 = run_pool(flagged, SECOND, CONFIRM, a.budget - spent, a.concurrency, key)
        spent += s2
    print(f"judged {n}, ${spent:.2f}", file=sys.stderr)
    if not (a.claims or a.new):
        judged = load(OUT)
        live = {j[8] for j in jobs}      # verdicts on the entries as they stand
        mine = [v for v in judged.values() if "error" not in v and v["digest"] in live]
        confirmed = load(CONFIRM)
        c = collections.Counter(p for v in mine for p in (agreed(v, confirmed) or []))
        cov = json.loads(COVERAGE.read_text(encoding="utf-8")) if COVERAGE.exists() else {}
        cov[f"study-{a.scope}"] = {"scope": "causal entries on AI claims" if a.scope == "ai" else "every causal entry",
                                   "entries_in_scope": len(jobs), "entries_judged": len(mine),
                                   "entries_without_text": sum(v for k, v in skipped.items() if not k.startswith("_")),
                                   "found": dict(c), "found_note": "problems both judges report",
                                   "at": time.strftime("%Y-%m-%d")}
        COVERAGE.parent.mkdir(parents=True, exist_ok=True)
        COVERAGE.write_text(json.dumps(cov, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sys.exit(report(False))


if __name__ == "__main__":
    main()
