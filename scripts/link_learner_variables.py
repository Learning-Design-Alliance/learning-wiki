#!/usr/bin/env python3
"""
link_learner_variables.py — link claims to the learner-variable pages they report on.

learning-design-spec joins a learner dimension to the research through its page in
learner-variables/ (spec/learners.md): a course whose learners vary on prior knowledge
reaches the claims about prior knowledge through that page. On 2026-10-10 only 7 of
the 12 pages had any inbound link and nothing linked to prior-knowledge, so the join
reached almost nothing (maintainer's retest, PR #210).

For each learner variable, candidate claims come from the search index (its title,
definition and a few synonyms below). A model then reads each candidate's title and
evidence line and says whether the claim reports a finding about that characteristic,
and in which role:

    predictor  learners who differ on it learn or achieve differently
    moderator  an instructional effect differs with it (works for novices, not experts)
    outcome    instruction changes it (an intervention raises self-efficacy)

and with what marker (+ the finding shows the characteristic matters as the claim
says, ~ under conditions, - it did not matter here), whose strength is capped at what
the claim's recorded evidence allows (link_pages.strength_cap). Each kept link is
written both ways: onto the variable's `## Claims` and onto the claim's
`## Learner Variables`, so the variable page has its evidence and the claim says which
learner characteristic it is about. Decisions go to eval/runs/learner-links/ first.

    python3 scripts/link_learner_variables.py                 # dry run, every variable
    python3 scripts/link_learner_variables.py --apply
    python3 scripts/link_learner_variables.py --new --apply   # only claims new in the tree (batches)
"""
import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import link_pages as lp  # noqa: E402
import search_index  # noqa: E402

FOLDER = WIKI_ROOT / "learner-variables"
OUT_DIR = WIKI_ROOT / "eval" / "runs" / "learner-links"
GROUP = 15
# Words a claim about the characteristic tends to use, beyond the page's own title and
# definition. Retrieval only: the model decides.
SYNONYMS = {
    "access": "accessibility disability disabilities device devices internet broadband bandwidth "
              "visual impairment hearing deaf blind assistive technology",
    "affect-regulation": "anxiety frustration emotion emotional regulation stress test anxiety "
                         "failure coping math anxiety",
    "attention": "attention distraction focus attentional ADHD mind wandering vigilance",
    "belonging": "belonging social belonging stereotype threat identity inclusion relatedness "
                 "connectedness",
    "digital-literacy": "digital literacy computer skills technology proficiency interface "
                        "online navigation ICT skills",
    "domain-context": "authentic context workplace relevance situated profession setting "
                      "real-world relevance",
    "motivation": "motivation interest self-efficacy value engagement persistence "
                  "intrinsic extrinsic expectancy mindset",
    "prior-knowledge": "prior knowledge expertise novice novices experts background knowledge "
                       "pretest prior achievement expertise reversal",
    "reading-and-language": "reading comprehension reading ability English learners second "
                            "language literacy vocabulary multilingual bilingual",
    "self-regulation": "self-regulated learning metacognition planning monitoring executive "
                       "function self-control strategy use",
    "time-and-continuity": "time on task attendance absenteeism summer learning loss dosage "
                           "interruption continuity instructional time",
    "working-memory": "working memory cognitive load memory capacity element interactivity",
}
ROLE_TEXT = {"predictor": "learners who differ on it differ in outcomes",
             "moderator": "an instructional effect differs with it",
             "outcome": "instruction changes it"}

PROMPT = """A learning-design wiki has one page per learner characteristic. Designers reach the research
on a characteristic through that page, so it should link every claim that reports a finding about it.

LEARNER CHARACTERISTIC: {title}
Definition: {description}

CLAIMS (title, then the evidence the wiki records for it):
{claims}

For each claim, decide whether it reports a finding ABOUT this characteristic: learners who differ on it
learn or achieve differently ("predictor"); an instructional effect differs with it ("moderator"); or
instruction changes it ("outcome"). A claim that only mentions the word, or is about a different
characteristic, does not bear. Give a marker: "+" the finding shows the characteristic matters in the way the
claim states, "~" it matters only under conditions or the results are mixed, "-" it did not matter here (a
null result is "-", never "+"); then S, M or W from the evidence line.
Reply: {{"links": [{{"k": <claim number>, "bears": true, "role": "predictor|moderator|outcome",
 "marker": "+M"}}]}}  (list only claims that bear)"""


def variables() -> dict:
    out = {}
    for p in sorted(FOLDER.glob("*.md")):
        if p.stem == "index":
            continue
        rec = lp.record(f"learner-variables/{p.stem}", p)
        out[p.stem] = rec
    return out


def new_claims() -> set:
    r = subprocess.run(["git", "status", "--porcelain", "--", "claims"], cwd=WIKI_ROOT,
                       capture_output=True, text=True)
    return {Path(line[3:]).stem for line in r.stdout.splitlines() if line.startswith("??") or line[1] == "A"}


def linked_claims(path: Path) -> set:
    return set(re.findall(r"\]\(\.\./claims/([^)#]+)\.md", path.read_text(encoding="utf-8")))


def candidates(db, slug: str, rec: dict, limit: int, only: "set | None") -> list:
    query = f"{rec['title']} {rec['description']} {SYNONYMS.get(slug, '')}"
    rows = search_index.query(db, query, folder="claims", limit=limit, mode="OR")
    have = linked_claims(FOLDER / f"{slug}.md")
    out = []
    for r in rows:
        claim = r[2]
        if claim in have or (only is not None and claim not in only):
            continue
        path = WIKI_ROOT / "claims" / f"{claim}.md"
        if path.exists():
            out.append(lp.record(f"claims/{claim}", path))
    return out


def judge(slug: str, rec: dict, group: list, model: str, key: str) -> list:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    listing = "\n".join(f"{i + 1}. {c['title']} [evidence: {c['evidence'] or 'none recorded'}]"
                        for i, c in enumerate(group))
    prompt = PROMPT.format(title=rec["title"], description=rec["description"], claims=listing)
    gen = oc.generate(model, "You classify research claims for a learning-design wiki. Reply with JSON only.",
                      prompt, key, max_tokens=2500)
    try:
        d = extract_json(gen.raw_text)
    except Exception:
        return [{"variable": slug, "error": (gen.raw_text or "")[:200], "cost_usd": gen.cost_usd}]
    out = []
    for item in (d or {}).get("links") or []:
        k = item.get("k")
        if not (isinstance(k, int) and 1 <= k <= len(group)) or not item.get("bears"):
            continue
        marker, role = item.get("marker"), item.get("role")
        if not (isinstance(marker, str) and lp.MARKER_RE.match(marker)) or role not in ROLE_TEXT:
            continue
        claim = group[k - 1]
        cap = lp.strength_cap(claim["evidence"])
        if "WMS".index(marker[1]) > "WMS".index(cap):
            marker = marker[0] + cap
        out.append({"variable": slug, "claim": claim["key"].split("/", 1)[1], "title": claim["title"],
                    "role": role, "marker": marker})
    if out:
        out[0]["cost_usd"] = gen.cost_usd
    else:
        out.append({"variable": slug, "none": True, "cost_usd": gen.cost_usd})
    return out


def add_lines(text: str, heading: str, lines: list, before: tuple) -> str:
    """Append lines (skipping links already present) under `heading`, creating the
    section before the first of `before` that exists, else at the end."""
    lines = [l for l in lines if re.search(r"\]\(([^)]+)\)", l).group(1) not in text]
    if not lines:
        return text
    m = re.search(rf"^{re.escape(heading)}[ \t]*\n", text, re.M)
    if m:
        nxt = re.search(r"^#{1,3} ", text[m.end():], re.M)
        cut = m.end() + (nxt.start() if nxt else len(text) - m.end())
        block = text[m.end():cut].rstrip("\n")
        block = "\n".join(l for l in block.split("\n") if l.strip() != "-")
        rest = text[cut:]
        return text[:m.end()] + (block + "\n" if block.strip() else "") + "\n".join(lines) + \
            ("\n\n" + rest if rest else "\n")
    for b in before:
        mb = re.search(rf"^{re.escape(b)}[ \t]*$", text, re.M)
        if mb:
            return text[:mb.start()] + f"{heading}\n" + "\n".join(lines) + "\n\n" + text[mb.start():]
    return text.rstrip("\n") + f"\n\n{heading}\n" + "\n".join(lines) + "\n"


def apply(links: list, vars_: dict) -> dict:
    by_var, by_claim = {}, {}
    for l in links:
        by_var.setdefault(l["variable"], []).append(l)
        by_claim.setdefault(l["claim"], []).append(l)
    for slug, ls in by_var.items():
        path = FOLDER / f"{slug}.md"
        lines = [f"- [{l['title']}](../claims/{l['claim']}.md) [{l['marker']}] — {ROLE_TEXT[l['role']]}"
                 for l in sorted(ls, key=lambda x: x["title"].lower())]
        text = path.read_text(encoding="utf-8")
        path.write_text(add_lines(text, "## Claims", lines, ("## Related Learner Variables", "## Examples",
                                                               "## Key Sources")), encoding="utf-8")
    for claim, ls in by_claim.items():
        path = WIKI_ROOT / "claims" / f"{claim}.md"
        lines = [f"- [{vars_[l['variable']]['title']}](../learner-variables/{l['variable']}.md) — "
                 f"{l['role']}: {ROLE_TEXT[l['role']]}" for l in ls]
        text = path.read_text(encoding="utf-8")
        path.write_text(add_lines(text, "## Learner Variables", lines, ("## Related Claims",)), encoding="utf-8")
    return {"variable_pages": len(by_var), "claim_pages": len(by_claim), "links": len(links)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--new", action="store_true", help="only claims added in the working tree")
    ap.add_argument("--variables", nargs="+", help="these learner-variable slugs only")
    ap.add_argument("--limit", type=int, default=120, help="candidate claims per variable")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=12)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    vars_ = variables()
    only = new_claims() if args.new else None
    if only is not None and not only:
        print("no new claims")
        return
    db = search_index.ensure()
    jobs = []
    for slug, rec in vars_.items():
        if args.variables and slug not in args.variables:
            continue
        cands = candidates(db, slug, rec, args.limit if only is None else 400, only)
        jobs += [(slug, rec, cands[i:i + GROUP]) for i in range(0, len(cands), GROUP)]
    print(f"{len(jobs)} group(s) of up to {GROUP} candidate claims across {len(vars_)} learner variables")
    results = []
    with concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
        for r in ex.map(lambda j: judge(j[0], j[1], j[2], args.model, key), jobs):
            results += r
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = Path(args.out) if args.out else OUT_DIR / ("new.ndjson" if args.new else "all.ndjson")
    out.write_text("".join(json.dumps(r) + "\n" for r in results), encoding="utf-8")
    links = [r for r in results if r.get("claim")]
    cost = sum(r.get("cost_usd") or 0 for r in results)
    errors = sum(1 for r in results if r.get("error"))
    counts = {}
    for l in links:
        counts[l["variable"]] = counts.get(l["variable"], 0) + 1
    print(f"links: {len(links)} {dict(sorted(counts.items()))}; errors {errors}; cost ${cost:.3f}; -> {out}")
    if args.apply:
        print("applied:", apply(links, vars_))


if __name__ == "__main__":
    main()
