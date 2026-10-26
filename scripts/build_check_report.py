#!/usr/bin/env python3
"""
build_check_report.py — `checks.md`, how the wiki's claims are checked and how far.

Written for a reader deciding whether to trust the wiki (maintainer, 2026-10-25:
"transparency is key, especially if we want people to trust it"). evidence.md says
what the evidence adds up to; this page says what has been done to make sure each
claim is what its source says, and that the source can be believed, and how much of
the wiki each check has reached. Every number is computed from committed records,
so the page cannot claim more checking than the repository shows, and `--check`
fails in CI when it is stale.

Each step states three things: what it catches, what it cannot catch, and its
coverage. The last of those is the one a reader most needs and a methods page most
often leaves out.

    python3 scripts/build_check_report.py            # write checks.md
    python3 scripts/build_check_report.py --check    # exit 1 if stale
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402

OUT = WIKI_ROOT / "checks.md"
SV = WIKI_ROOT / "eval" / "source-validity"


def ndjson(path: Path) -> list:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "–"


def n(x):
    return f"{x:,}"


# Removal reasons, grouped for a reader. The log keeps every reason verbatim.
REMOVAL_GROUPS = [
    ("No verifiable source (no DOI after a Crossref and DataCite search)", r"no DOI|DOI belonged"),
    ("About how research is done, not a design decision", r"research.practice|research practice"),
    ("Local context only (one district, programme or year)", r"local context"),
    ("Source cannot be believed (impossible statistics, invented references, retraction)",
     r"source validity|impossible statistic|invented reference|anachron|retraction notice"),
    ("Citation chase: a retracted article or off-topic methods literature", r"citation chase"),
    ("Misfiled or thin page folded or dropped", r"thin |not a product|misfiled|wrong document|isolated page"),
]


def removal_groups(rows):
    c = collections.Counter()
    for r in rows:
        reason = r.get("reason") or ""
        for label, pat in REMOVAL_GROUPS:
            if re.search(pat, reason, re.I):
                c[label] += 1
                break
        else:
            c["Other (see eval/removed/pages.ndjson)"] += 1
    return c


def claim_stats():
    s = collections.Counter()
    for p in (WIKI_ROOT / "claims").glob("*.md"):
        if p.stem == "index":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = text.split("\n---", 1)[0]
        s["claims"] += 1
        if re.search(r"(?m)^source_checked:", fm):
            s["source_checked"] += 1
        if re.search(r"(?m)^verified:", fm):
            s["verified"] += 1
            if "human:" in fm.split("verified:", 1)[1][:400]:
                s["human"] += 1
        m = re.search(r"(?m)^recheck_by:\s*(\d{4})", fm)
        if m:
            s["recheck"] += 1
        ev = text.split("## Evidence", 1)[-1]
        entries = re.findall(r"(?m)^### ", ev)
        s["entries"] += len(entries)
        for line in ev.splitlines():
            if line.startswith("`q"):
                spans = " ".join(re.findall(r"`([^`]*)`", line))
                if re.search(r"\bi[0-3]\b", spans):
                    s["i_coded"] += 1
                if re.search(r"\bi\?", spans):
                    s["i_unknown"] += 1
                if re.search(r"\br[1-3]\b", spans):
                    s["rigour_coded"] += 1
        if re.search(r"https?://(?:dx\.)?doi\.org/10\.", ev):
            s["with_doi"] += 1
    return s


def overdue(year):
    out = 0
    for p in (WIKI_ROOT / "claims").glob("*.md"):
        m = re.search(r"(?m)^recheck_by:\s*(\d{4})", p.read_text(encoding="utf-8", errors="replace")[:3000])
        if m and int(m.group(1)) < year:
            out += 1
    return out


def build() -> str:
    import datetime
    today = datetime.date.today()
    cs = claim_stats()
    manifest = ndjson(WIKI_ROOT / "sources" / "manifest.ndjson")
    latest = {}
    for r in manifest:
        latest[r["id"]] = r
    ingested = [r for r in latest.values() if r.get("status") == "ingested"]
    rejected = [r for r in latest.values() if r.get("status") == "rejected"]
    rej = collections.Counter(r.get("reason_code") or "uncoded" for r in rejected)
    cit = [r["citations"] for r in ingested if isinstance(r.get("citations"), dict)]
    cit_ok = sum(1 for c in cit if c.get("crossref_reachable"))
    dois_removed = sum(len(c.get("removed") or []) for c in cit)
    dois_flagged = sum(len(c.get("flagged") or []) for c in cit)
    lb_reviewed = ndjson(WIKI_ROOT / "eval" / "load-bearing" / "reviewed.ndjson")
    authorities = ndjson(WIKI_ROOT / "sources" / "authorities.ndjson")
    removed = ndjson(WIKI_ROOT / "eval" / "removed" / "pages.ndjson")
    groups = removal_groups(removed)
    cov = json.loads((SV / "coverage.json").read_text(encoding="utf-8")) if (SV / "coverage.json").exists() else {}
    sv_reviewed = ndjson(SV / "reviewed.ndjson")
    st_reviewed = ndjson(SV / "study-reviewed.ndjson")
    retracted = ndjson(SV / "retracted.ndjson")
    dup = sum(len(ndjson(p)) for p in (WIKI_ROOT / "eval" / "duplicates").glob("*.ndjson"))
    merges = len(ndjson(WIKI_ROOT / "eval" / "claim-merges" / "decisions.ndjson"))
    od = overdue(today.year)

    L = []
    w = L.append
    w("# How Claims Are Checked")
    w("")
    w("> Generated by `scripts/build_check_report.py` from the repository's own records. Do not edit by hand.")
    w("")
    w("This wiki is written by language models, from published research, and checked by "
      "automated steps. **No page has yet been reviewed by a person**: every page reports its "
      "trust tier, and every one says *unverified*. This page sets out each check a claim "
      "passes on its way in and after, what each one catches and cannot catch, and how much of "
      "the wiki it has reached so far. What the evidence adds up to is on "
      "[State of the Evidence](evidence.md).")
    w("")
    w("## Health at a glance")
    w("")
    w("| | |")
    w("|---|---|")
    w(f"| Claims | {n(cs['claims'])}, from {n(len(ingested))} sources |")
    w(f"| Reviewed by a person | {n(cs['human'])} |")
    w(f"| Every evidence entry compared with its source by the faithfulness judge | {n(cs['source_checked'])} claims ({pct(cs['source_checked'], cs['claims'])}) |")
    w(f"| Claims citing at least one DOI | {n(cs['with_doi'])} claims ({pct(cs['with_doi'], cs['claims'])}) |")
    w(f"| Sources whose citations went through the Crossref identity gate | {n(cit_ok)} of {n(len(ingested))} |")
    if "stats" in cov:
        s = cov["stats"]
        w(f"| Sources read for impossible statistics and invented references | {n(s['sources_with_text'])} of {n(s['sources_ingested'])} ({s['at']}) |")
    if "retractions" in cov:
        r = cov["retractions"]
        w(f"| Cited DOIs checked for retraction | {n(r['dois_looked_up'])} of {n(r['dois_cited'])} ({r['at']}) |")
    w(f"| Retracted sources found and acted on | {n(len(retracted))} |")
    w(f"| Claims past their recheck year (fast-ageing kinds only) | {n(od)} of {n(cs['recheck'])} with one |")
    w(f"| Claims removed by a check, all time | {n(len(removed))} |")
    w("")
    w("## The checks, in the order a claim meets them")
    w("")

    def step(title, what, cannot, coverage):
        w(f"### {title}")
        w("")
        w(what)
        w("")
        w(f"**Cannot catch.** {cannot}")
        w("")
        w(f"**Coverage.** {coverage}")
        w("")

    step("1. Inclusion",
         "Each source is screened against the published [inclusion criteria](https://github.com/Learning-Design-Alliance/"
         "learning-wiki/blob/main/INCLUSION.md) before anything is extracted: opinion pieces, out-of-scope work, sources "
         "with nothing extractable and sources already covered are refused. Every decision, either way, is logged in "
         "`sources/manifest.ndjson`, so anyone can check whether a given article was reviewed.",
         "A source that is in scope and badly done. Inclusion is about what a source is, not how good it is.",
         f"{n(len(latest))} sources reviewed: {n(len(ingested))} ingested, {n(len(rejected))} refused "
         + "(" + ", ".join(f"{k} {n(v)}" for k, v in rej.most_common()) + ").")
    step("2. Extraction and structural validation",
         "A model reads the article and writes claims with their evidence. A validator refuses any extraction whose "
         "structure is broken, whose citation does not match the article, or whose codes are out of range; a refused "
         "article contributes nothing.",
         "A well-formed claim that misreads its article (step 5 looks for that).",
         f"{n(rej.get('validation-error', 0) + rej.get('parse-error', 0))} articles refused by the validator.")
    step("3. Citation identity",
         "Every DOI written on a page is resolved against Crossref (DataCite after a Crossref 404) and compared on title, "
         "first author and year. A DOI that resolves to a different paper is removed, because a wrong DOI reads as "
         "verified; one that cannot be settled is flagged for a person. Books, which no registry indexes, are checked by "
         "a person against the publisher and recorded in `sources/authorities.ndjson`.",
         "A citation with no DOI and no registry record; a correct citation to a study that is itself wrong.",
         f"{n(cit_ok)} of {n(len(ingested))} ingested sources passed the gate with the registry reachable; "
         f"{n(dois_removed)} DOIs removed as the wrong paper, {n(dois_flagged)} flagged for a person; "
         f"{n(len(authorities))} book citations verified by a person.")
    step("4. A verifiable source for every claim",
         "A claim whose evidence has no DOI after a Crossref and DataCite search is removed, unless it rests on a report "
         "from a named evaluation organisation (What Works Clearinghouse, MDRC, RAND and others) or a principle, pattern "
         "or ten or more designs depend on it, in which case it says so in an *Evidence quality* line.",
         "Whether the DOI'd source is any good.",
         f"{n(cs['with_doi'])} of {n(cs['claims'])} claims ({pct(cs['with_doi'], cs['claims'])}) cite a DOI; "
         f"{n(groups.get(REMOVAL_GROUPS[0][0], 0))} claims removed for having none.")
    step("5. Faithfulness to the source",
         "A second model, from a different provider, reads each evidence entry beside the article it cites (full text "
         "where an open copy exists, otherwise the abstract) and checks every number, direction, population and design "
         "the page states. It runs on every claim that three or more design pages cite, and on every new batch. A "
         "failure stops the batch until a person or agent has read it; a judge error is dismissed with a written reason.",
         "A claim checked only against an abstract, for detail an abstract does not carry. The judge is a model and "
         "has been wrong; its failures are read before they are acted on.",
         f"{n(cs['source_checked'])} claims ({pct(cs['source_checked'], cs['claims'])}) have had every evidence entry "
         f"compared with its source and passed; {n(len(lb_reviewed))} judge failures were read and recorded with a reason. "
         "Each claim states this on its page, in its *Currency* line.")
    stats = cov.get("stats", {})
    refs = cov.get("refs", {})
    step("6. Can the source be believed?",
         "Added 2026-10-25, after an audit of AI-in-education meta-analyses found that a study this wiki had made ten "
         "claims from reports an effect size of 1.374 (it cannot exceed 1) and cites five ChatGPT studies dated before "
         "ChatGPT existed. Each source's text is now read for statistics that cannot be right (a proportion of variance "
         "above 1, an ANOVA row whose mean square is not its sum of squares over its degrees of freedom, p values their "
         "own test statistics contradict), for references dated before the tool they name, and, for AI-era sources, "
         "for reference DOIs that do not exist or point to a different work. Every cited DOI is checked for a "
         "retraction, withdrawal or expression of concern. A high-severity finding stops the batch; a confirmed one "
         "removes the source's claims.",
         "Invented references that carry no DOI and no anachronism; errors that leave the arithmetic consistent; "
         "a source whose text was not available (abstract only).",
         (f"{n(stats.get('sources_with_text', 0))} of {n(stats.get('sources_ingested', 0))} sources read "
          f"({stats.get('at', 'not yet run')}): {n(stats.get('with_findings', 0))} with a finding, "
          f"{n(stats.get('high', 0))} high severity. " if stats else "Not yet run. ")
         + (f"Reference DOIs: {n(refs.get('dois_checked', 0))} DOIs from {n(refs.get('sources_checked', 0))} "
            f"{refs.get('scope', '')} resolved; {n(refs.get('with_findings', 0))} sources have one that does not "
            "resolve or names another work, listed for a person but not acted on automatically, because text "
            "extracted from a PDF breaks DOIs across lines and most of these are layout, not invention. " if refs else "")
         + f"{n(len(sv_reviewed))} findings decided: "
         + f"{n(sum(1 for r in sv_reviewed if r.get('decision') == 'confirmed'))} confirmed and acted on, "
         + f"{n(sum(1 for r in sv_reviewed if r.get('decision') == 'false-alarm'))} false alarms. "
         + f"{n(len(retracted))} retracted sources found"
         + (f"; of {n(cov['retractions']['dois_cited'])} DOIs the wiki cites, {n(cov['retractions'].get('dead', 0))} "
            f"were registered at neither Crossref nor DataCite when last checked ({cov['retractions']['at']})."
            if "retractions" in cov else "."))
    study = {k: v for k, v in cov.items() if k.startswith("study-")}
    cov_txt = " ".join(
        f"{v['scope']}: {n(v['entries_judged'])} of {n(v['entries_in_scope'])} judged ({v['at']}); found "
        + (", ".join(f"{k} {n(c)}" for k, c in sorted(v['found'].items(), key=lambda kv: -kv[1])) or "nothing")
        + "." for v in study.values()) or "Not yet run."
    step("7. Does the study measure what the claim says?",
         "Also added 2026-10-25, from the same audit's most common findings. For each causal claim a model reads the "
         "study and reports: whether the outcome is measured performance or only self-report (a claim that learning "
         "improved cannot rest on students' ratings of their own learning); what the effect was compared with (a "
         "randomised group, an intact class, the same students before, nothing); whether the intervention came bundled "
         "with something else that could explain it; and whether students were counted as independent where whole "
         "classes or teams were assigned. A finding is acted on by retitling the claim to what was measured, stating "
         "the design's limit, correcting a design code that overstates it, or removing the claim.",
         "Problems the paper does not report. The judge reads only what the study says about itself.",
         cov_txt + f" {n(len(st_reviewed))} findings read and acted on.")
    step("8. Evidence codes",
         "Each evidence entry carries a design tier (`q1`–`q4`), an impact code (`i0`–`i3`, which must rest on an effect "
         "size the source prints, otherwise `i?`), a sample size with its unit, and a kind with a rigour rating judged "
         "against that kind's own standard (an interview study and a trial are each rated for what they are). Rigour is "
         "coded from the article, never from the wiki's paraphrase of it.",
         "Whether a study's conclusion is true. The codes describe how a study was done, not whether it was right.",
         f"{n(cs['entries'])} evidence entries; {n(cs['i_coded'])} rest on a printed effect size and {n(cs['i_unknown'])} "
         f"report none (`i?`); {n(cs['rigour_coded'])} carry a rigour rating.")
    step("9. Duplicates and merges",
         "Two claims stating the same finding are merged, and two pages on the same thing are folded together, only "
         "when two models judge them the same; the decisions are kept, so a pair judged different is not raised again.",
         "Near-duplicates phrased far apart.",
         f"{n(dup + merges)} pair decisions recorded.")
    step("10. Currency",
         "Each claim states the year of its newest study and when its sources were last checked. Claims whose findings "
         "age quickly (the accuracy of a tool or model, local or general context such as baselines) carry a recheck "
         "year; past it the page says it is overdue rather than hiding it. Design findings carry none: research does "
         "not expire on a calendar.",
         "A finding superseded by newer research the wiki has not ingested.",
         f"{n(cs['recheck'])} claims carry a recheck year; {n(od)} are past it.")
    step("11. Structure",
         "A lint run on every change fails on broken links, misfiled pages, missing identity fields, stale generated "
         "files, embargoed research, and any claim citing a DOI recorded as retracted. Nothing merges while it fails.",
         "Anything about content.",
         "Every change to the wiki.")
    w("## Removed by a check")
    w("")
    w("Removals are logged with their reason in `eval/removed/pages.ndjson`; git history keeps every removed page.")
    w("")
    w("| Reason | Claims and pages |")
    w("|---|---|")
    for label, _ in REMOVAL_GROUPS + [("Other (see eval/removed/pages.ndjson)", None)]:
        if groups.get(label):
            w(f"| {label} | {n(groups[label])} |")
    w("")
    w("## What no check here does")
    w("")
    w("- **No person has reviewed a page.** The trust tier on every page says so. `stable` status requires a person's "
      "recorded review, and no page has one yet.")
    w("- **No check corrects for publication bias.** The literature over-reports positive results, and education "
      "technology more than most. A claim resting on published studies inherits that.")
    w("- **Most claims rest on one study.** One study in one setting has not been shown to hold elsewhere; "
      "[State of the Evidence](evidence.md) gives the share.")
    w("- **The checks are models and patterns.** They catch what they are built to catch, and each has been wrong; "
      "every failure they raise is read before it is acted on, and that reading is recorded.")
    w("")
    w("## Who wrote this, and the license")
    w("")
    w("Pages are written by language models from published research, under rules, templates and checks that "
      "people designed; the structure, editorial rules and code are human work. The content is licensed "
      "[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) wherever copyright exists in it. In several "
      "jurisdictions, including the United States, text an AI system produces without enough human creative control "
      "is not protected by copyright, so some pages may carry none and are to that extent in the public domain. "
      "Either way you may do at least what the license allows. Quoted passages remain their authors' work. "
      "The [LICENSE](https://github.com/Learning-Design-Alliance/learning-wiki/blob/main/LICENSE) file has the "
      "details; it is the project's position, not legal advice.")
    w("")
    w("Every record behind these numbers is in the [repository](https://github.com/Learning-Design-Alliance/learning-wiki): "
      "`sources/manifest.ndjson`, `eval/load-bearing/`, `eval/source-validity/`, `eval/removed/pages.ndjson`.")
    w("")
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = build()
    if a.check:
        old = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if old != text:
            print("checks.md is stale: run python3 scripts/build_check_report.py")
            sys.exit(1)
        return
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.relative_to(WIKI_ROOT)}")


if __name__ == "__main__":
    main()
