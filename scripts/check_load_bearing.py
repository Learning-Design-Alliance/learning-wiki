#!/usr/bin/env python3
"""
check_load_bearing.py — judge the claims the wiki leans on hardest, against their articles.

The unattended batch runs with no gating judge (CLAUDE.md, 2026-09-26): GLM writes
claims at $0.0027 an article, and a GPT judge would add $0.0047 to catch the ~13% of
extractions that misstate their article in ways the validator cannot see. Most of
those claims are cited by one page, or none. The ones that matter are the ones many
pages rest on, so this spends the judge there and only there:

1. **Rank** every claim by load: the distinct pages that link to it
   (`reverse-index.json`), non-claim pages first, since a principle or strategy
   citing a claim is a design decision resting on it, where a `## Related Claims`
   link is a neighbour. Merge targets (a claim with `aliases:`) carry the pages
   that cited every claim folded into them, so they rank by that load already.
2. **Find each study's text.** The unit judged is one `### ` evidence entry, with
   the claim and the subclaims that point at it. Its text is the article the
   pipeline fetched (`eval/corpus/cache/<id>.txt`) when the manifest says this
   claim came from an article whose title the entry's citation carries; otherwise
   the abstract OpenAlex holds for the entry's DOI (cached beside it as
   `doi-*.txt`). The most-cited claims are almost all of the second kind: of the
   137 claims three or more design pages cite (2026-09-27), 3 came from a batch.
   An entry with neither is reported as not checkable, never as passing.
3. **Judge** the entry against that text: does every subclaim, number, design,
   population and direction it states appear there? The judge sees the page as a
   reader does, after every later edit, merge and repair. On an abstract it may
   answer `unverifiable` for detail an abstract would not carry, which is not a
   failure and not a pass.

Nothing is written to any page. The procedure for acting on what this finds, and for
running it regularly, is `eval/load-bearing/README.md`. A failure names what the judge
found, for a person to read (the judge is a model and has been wrong about this pipeline before: read
its failures before trusting them, CLAUDE.md batch 7). Results go to `--out`, and a
claim already judged against the same page text and article is not paid for again.

    python3 scripts/check_load_bearing.py --rank --top 40          # the ranking, free
    python3 scripts/check_load_bearing.py --top 100 --budget 1.00  # judge the top 100
    python3 scripts/check_load_bearing.py --report                 # what earlier runs found
    python3 scripts/check_load_bearing.py --claims <slug>          # re-judge after a fix
    python3 scripts/check_load_bearing.py --dismiss "<slug>#<entry>" --because judge-wrong --reason "..."
"""
import argparse
import collections
import concurrent.futures
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402
import page_identity as pid  # noqa: E402

CACHE = WIKI_ROOT / "eval" / "corpus" / "cache"
OUT = WIKI_ROOT / "eval" / "runs" / "load-bearing" / "judged.ndjson"
# Committed, append-only: a person's (or a session's) triage of a failure the
# judge got wrong. Keyed on the entry's text, so an edit to the entry re-opens it.
REVIEWED = WIKI_ROOT / "eval" / "load-bearing" / "reviewed.ndjson"
DISMISS_REASONS = ("judge-wrong", "registry-wrong")
MAX_ARTICLE = 60_000

SYSTEM = """\
You are checking one evidence entry on a learning-science wiki page against the study it \
cites. You are given the page's claim, the subclaims that rest on this study, and the entry \
(citation, q/i/n codes, description), and the study's text: the full article, or only its \
abstract. A model wrote the page; your job is to find anything it says about this study that \
the study does not support. Do not grade the study's own quality.

Check each of these against the study:
- every subclaim and the entry's description: does the study find this, in this direction, \
for this population and outcome? Not overstated, not generalised past what was studied? \
Does the study bear on the claim at all?
- every number (sample sizes, statistics, effect sizes, percentages): present in the article \
and attached to the right thing? An ANOVA's degrees of freedom are not a sample size.
- the design (experiment, quasi-experiment, correlational, review, argument) and the q/i codes \
it implies. A correlation reported as a cause, or a non-significant result reported as \
"no effect", is a misstatement.
- quotes: in the article?
- the citation: right authors, year, title. A catalogue URL (ERIC, PMC, arXiv) the article \
does not print is added by the pipeline and is not an error.

Output ONLY a JSON object, no fences:
{"verdict": "pass" | "fail" | "unverifiable" | "not-this-study",
 "issues": ["each specific misstatement: what the page says, and what the study says"]}
"fail": something the entry or its subclaims say contradicts or overstates the study. \
ON AN ABSTRACT, absence is never a failure: an abstract omits most of a paper, so a detail it \
does not mention is "unverifiable". Fail on an abstract only when the abstract contradicts the \
entry: it reports the opposite finding, a different kind of work (a framework or argument \
presented as an empirical review or experiment), or a different population, outcome or scope \
that rules out what the entry says. \
"unverifiable": only an abstract was given, and what the entry says is not in it but is not \
contradicted by it. "not-this-study": the text given is a different work \
from the one cited. Minor wording is not a failure."""
VERDICTS = ("pass", "fail", "unverifiable", "not-this-study")


def claim_pages() -> dict:
    return {p.stem: p for p in (WIKI_ROOT / "claims").glob("*.md") if p.stem != "index"}


def load() -> dict:
    """slug -> {"designs": n non-claim pages citing it, "claims": n claims linking it}."""
    rev = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))
    out = collections.defaultdict(lambda: {"designs": 0, "claims": 0})
    for slug, by_kind in (rev.get("edges", {}).get("claims") or {}).items():
        for kind, rows in by_kind.items():
            out[slug]["claims" if kind == "claims" else "designs"] += len(rows)
    return out


def aliases(pages: dict) -> dict:
    """slug -> [its aliases], for claims that absorbed others."""
    out = {}
    for slug, path in pages.items():
        fm, _ = pid.split_fm(path.read_text(encoding="utf-8"))
        a = pid.read_aliases(fm) if fm is not None else []
        if a:
            out[slug] = a
    return out


def sources_of() -> dict:
    """claim slug (current or retired) -> [{id, title}] of the articles that wrote it."""
    out = collections.defaultdict(list)
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except ValueError:
            continue
        if rec.get("status") != "ingested":
            continue
        for p in rec.get("pages") or []:
            if p.startswith("claims/") and p.endswith(".md"):
                slug = p[len("claims/"):-3]
                if not any(s["id"] == rec["id"] for s in out[slug]):
                    out[slug].append({"id": rec["id"], "title": rec.get("title") or ""})
    return out


def ranking(pages: dict) -> list:
    ld, al, src = load(), aliases(pages), sources_of()
    rows = []
    for slug in pages:
        arts = list(src.get(slug, []))
        for a in al.get(slug, []):
            arts += [s for s in src.get(a, []) if s not in arts]
        rows.append({"claim": slug, "designs": ld[slug]["designs"], "claims": ld[slug]["claims"],
                     "merged": len(al.get(slug, [])), "articles": arts})
    rows.sort(key=lambda r: (-r["designs"], -r["claims"], r["claim"]))
    return rows


DOI_RE = re.compile(r"10\.\d{4,9}/[^\s)\]>]+", re.I)
ENTRY_RE = re.compile(r"(?m)^### ")
_WORD = re.compile(r"[a-z0-9]+")


def units(path: Path) -> tuple:
    """(claim title, [(anchor, entry block, [subclaims pointing at it])])."""
    fm_lines, body = okf_lib.split_frontmatter(path.read_text(encoding="utf-8"))
    title = str(okf_lib.parse_frontmatter_scalars(fm_lines).get("title") or path.stem)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    evidence = okf_lib.get_section(body, "Evidence") or ""
    subclaims = (okf_lib.get_section(body, "Subclaims") or "").splitlines()
    out = []
    for chunk in ENTRY_RE.split(evidence)[1:]:
        heading, _, rest = chunk.partition("\n")
        anchor = okf_lib.slugify(heading.strip())
        subs = [l.strip() for l in subclaims if f"(#{anchor})" in l]
        out.append((anchor, ("### " + chunk).strip(), subs))
    return title, out


def _words(text: str) -> set:
    return set(_WORD.findall((text or "").lower()))


def cached_article(block: str, articles: list):
    """The fetched article this entry cites: a manifest source of the claim whose
    title the entry's citation carries (80% of its first eight words)."""
    have = _words(block[:600])
    for a in articles:
        title = [w for w in _WORD.findall(a["title"].lower()) if len(w) > 2][:8]
        path = CACHE / f"{a['id']}.txt"
        if title and path.exists() and sum(w in have for w in title) / len(title) >= 0.8:
            return a["id"], path.read_text(encoding="utf-8", errors="replace")
    return None


_EN = {"the", "of", "and", "to", "in", "that", "is", "for", "with", "was", "were", "on", "are", "this"}
_OTHER = {"el", "la", "de", "que", "los", "las", "del", "en", "una", "por", "para", "con", "se", "da",
          "do", "das", "dos", "um", "uma", "der", "die", "und", "le", "les", "des", "et"}


def abstract_usable(text: str) -> bool:
    """False for an abstract in another language than English. OpenAlex attaches a
    citing thesis's Spanish abstract to some classics (Wood, Bruner & Ross 1976;
    Deci 1971; Alfieri et al. 2011, found 2026-09-27) under the right DOI and title;
    judged against it, every entry reads as not the study."""
    words = _WORD.findall(text.split("ABSTRACT:", 1)[-1].lower())[:300]
    en = sum(w in _EN for w in words)
    other = sum(w in _OTHER for w in words)
    return en >= other


def openalex_abstract(doi: str):
    """(title, year, abstract) from OpenAlex, cached as eval/corpus/cache/doi-*.txt.
    None when the lookup fails or the record has no abstract; a failure is not cached."""
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", doi.lower())
    path = CACHE / f"doi-{safe}.txt"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        return text if text and abstract_usable(text) else None
    import urllib.parse
    import urllib.request
    q = urllib.parse.urlencode({"select": "title,publication_year,abstract_inverted_index,authorships",
                                "mailto": "contact@learningdesignalliance.org",
                                **({"api_key": os.environ["OPENALEX_API_KEY"]} if os.environ.get("OPENALEX_API_KEY") else {})})
    try:
        with urllib.request.urlopen(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}?{q}", timeout=30) as r:
            d = json.load(r)
    except Exception as e:
        if getattr(e, "code", None) == 404:
            CACHE.mkdir(parents=True, exist_ok=True)
            path.write_text("", encoding="utf-8")
        return None
    inv = d.get("abstract_inverted_index") or {}
    words = sorted(((i, w) for w, idx in inv.items() for i in idx))
    abstract = " ".join(w for _, w in words)
    authors = ", ".join((a.get("author") or {}).get("display_name") or "" for a in (d.get("authorships") or [])[:6])
    text = (f"{d.get('title') or ''} ({d.get('publication_year') or ''}). {authors}\n\nABSTRACT: {abstract}"
            if abstract else "")
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return text if text and abstract_usable(text) else None


def digest(*parts: str) -> str:
    return hashlib.sha256("\n\x00".join(parts).encode("utf-8")).hexdigest()[:16]


def done_before(out: Path) -> dict:
    seen = {}
    if out.exists():
        for line in out.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("verdict") in VERDICTS:
                seen[r["digest"]] = r
    return seen


def judge(claim: str, title: str, block: str, subs: list, source: str, basis: str, text: str,
          model: str, key: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    text = text if len(text) <= MAX_ARTICLE else text[:MAX_ARTICLE] + "\n\n[TRUNCATED]"
    prompt = (f"## The study ({basis}: {source})\n{text}\n\n"
              f"## Wiki page claims/{claim}.md\nClaim: {title}\n\nSubclaims resting on this study:\n"
              + ("\n".join(subs) or "(none)") + f"\n\nEvidence entry:\n{block}")
    t0 = time.monotonic()
    gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=4000)
    data = extract_json(gen.raw_text)
    verdict = data.get("verdict") if isinstance(data, dict) else None
    return {"verdict": verdict if verdict in VERDICTS else "error",
            "issues": (data.get("issues") or []) if isinstance(data, dict) else [],
            "cost_usd": gen.cost_usd, "provider": gen.provider, "latency_s": round(time.monotonic() - t0, 1)}


def page_digest(claim: str, title: str, block: str, subs: list) -> str:
    """The entry as the page states it, without the source text, which is cached
    per machine and may differ between two checkouts."""
    return digest(claim, title, block, "\n".join(subs))


def load_reviewed() -> dict:
    """page digest -> the latest review of that exact entry text."""
    out = {}
    if REVIEWED.exists():
        for line in REVIEWED.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
            except ValueError:
                continue
            out[r["page_digest"]] = r
    return out


def dismiss(target: str, because: str, reason: str, by: str, pages: dict) -> str:
    """Record that a failure was read and the page is right. Refuses an entry that
    does not exist, and records the text it vouches for, so any later edit to the
    entry re-opens it."""
    claim, _, anchor = target.partition("#")
    claim = claim.removeprefix("claims/").removesuffix(".md")
    if claim not in pages:
        raise SystemExit(f"no claim page {claim}")
    title, entries = units(pages[claim])
    match = [(b, s) for a, b, s in entries if a == anchor]
    if not match:
        raise SystemExit(f"claims/{claim}.md has no evidence entry #{anchor}")
    if not reason.strip():
        raise SystemExit("--reason is required: say what you checked and what it showed")
    rec = {"claim": claim, "entry": anchor, "page_digest": page_digest(claim, title, *match[0]),
           "decision": because, "reason": reason.strip(), "by": by, "at": time.strftime("%Y-%m-%d")}
    REVIEWED.parent.mkdir(parents=True, exist_ok=True)
    with REVIEWED.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return f"dismissed claims/{claim}.md#{anchor} as {because}"


def entry_jobs(rows: list, pages: dict) -> tuple:
    """[(row, anchor, title, block, subs, source, basis, text, digest)] for every
    evidence entry with a text to judge it against, and a count of those without."""
    jobs, skipped = [], collections.Counter()
    for r in rows:
        title, entries = units(pages[r["claim"]])
        for anchor, block, subs in entries:
            hit = cached_article(block, r["articles"])
            if hit:
                source, text, basis = hit[0], hit[1], "full text"
            else:
                m = DOI_RE.search(block)
                text = openalex_abstract(m.group(0).rstrip(".,;")) if m else None
                if not text:
                    skipped["no DOI" if not m else "no abstract"] += 1
                    continue
                source, basis = "doi:" + m.group(0).rstrip(".,;"), "abstract"
            jobs.append((r, anchor, title, block, subs, source, basis, text,
                         digest(r["claim"], title, block, "\n".join(subs), text),
                         page_digest(r["claim"], title, block, subs)))
    return jobs, skipped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--top", type=int, default=100, help="how many of the most-cited claims")
    ap.add_argument("--rank", action="store_true", help="print the ranking and stop; costs nothing")
    ap.add_argument("--claims", nargs="+", metavar="SLUG",
                    help="judge these claims instead of the top of the ranking (e.g. after fixing them)")
    ap.add_argument("--report", action="store_true", help="summarise what earlier runs found")
    ap.add_argument("--budget", type=float, default=1.0, help="stop starting judge calls past this many USD")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--out", type=Path, default=OUT)
    ap.add_argument("--dismiss", metavar="CLAIM#ENTRY",
                    help="record that this failure was checked and the page is right")
    ap.add_argument("--because", choices=DISMISS_REASONS,
                    help="judge-wrong: the source supports the page; registry-wrong: the text the judge "
                         "was given (an OpenAlex abstract, say) is not the cited work")
    ap.add_argument("--reason", default="", help="what you checked, and what it showed")
    ap.add_argument("--by", default="claude/unspecified", help="who checked: human:<id> or <tool>/unspecified")
    args = ap.parse_args()

    pages = claim_pages()
    if args.dismiss:
        if not args.because:
            raise SystemExit("--dismiss needs --because and --reason")
        print(dismiss(args.dismiss, args.because, args.reason, args.by, pages))
        return
    rows = ranking(pages)
    if args.claims:
        want = {c.removeprefix("claims/").removesuffix(".md") for c in args.claims}
        missing = want - set(pages)
        if missing:
            raise SystemExit(f"no claim page: {', '.join(sorted(missing))}")
        rows = [r for r in rows if r["claim"] in want]
    else:
        rows = rows[:args.top]
    if args.rank:
        print(f"{'designs':>7} {'claims':>6} {'merged':>6} {'studies':>7}  claim")
        for r in rows:
            print(f"{r['designs']:>7} {r['claims']:>6} {r['merged']:>6} "
                  f"{len(units(pages[r['claim']])[1]):>7}  {r['claim']}")
        return

    if args.report:
        # A verdict counts only while the entry still reads as it did when judged:
        # once a page is corrected, its old failure is stale, not open.
        judged = done_before(args.out)
        wanted = {r["claim"] for r in judged.values()}
        current = {j[-2]: j[-1] for j in entry_jobs([r for r in ranking(pages) if r["claim"] in wanted], pages)[0]}
        reviewed = load_reviewed()
        latest, dismissed, live = {}, collections.Counter(), set()
        for r in judged.values():
            if r["digest"] in current:
                live.add((r["claim"], r["entry"]))
                if r["verdict"] in ("fail", "not-this-study") and current[r["digest"]] in reviewed:
                    dismissed[reviewed[current[r["digest"]]]["decision"]] += 1
                    continue
                latest[(r["claim"], r["entry"])] = r
        stale = len({(r["claim"], r["entry"]) for r in judged.values()} - live)
        if stale:
            print(f"{stale} earlier verdict(s) are stale: the entry has changed since, so re-run to judge it again")
        c = collections.Counter(r["verdict"] for r in latest.values())
        b = collections.Counter(r["basis"] for r in latest.values())
        print(f"{len(latest)} evidence entries judged on {len({k[0] for k in latest})} claims: "
              f"{dict(c)}; basis {dict(b)}")
        if dismissed:
            print(f"{sum(dismissed.values())} failure(s) read and dismissed ({dict(dismissed)}); "
                  f"see {REVIEWED.relative_to(WIKI_ROOT)}")
        print()
        for r in sorted(latest.values(), key=lambda r: (-r["designs"], r["claim"])):
            if r["verdict"] in ("fail", "not-this-study"):
                label = r["verdict"].upper()
                if r["verdict"] == "not-this-study" and r["basis"] == "abstract":
                    # The DOI and OpenAlex's title agreed, or the lookup would not have
                    # returned it; a mismatch is then the registry's abstract field.
                    label = "ABSTRACT-IS-ANOTHER-WORK (check the OpenAlex record, not the page)"
                print(f"{label}  claims/{r['claim']}.md#{r['entry']}  "
                      f"({r['designs']} pages cite it; {r['basis']}: {r['source']})")
                for i in r["issues"]:
                    print(f"      - {i}")
        return

    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("OPENROUTER_API_KEY is not set")
    seen = done_before(args.out)
    jobs, skipped = entry_jobs(rows, pages)
    reviewed = load_reviewed()
    reused = sum(1 for j in jobs if j[-2] in seen)
    settled = sum(1 for j in jobs if j[-2] not in seen and j[-1] in reviewed)
    jobs = [j[:-1] for j in jobs if j[-2] not in seen and j[-1] not in reviewed]
    if settled:
        print(f"{settled} entr{'y' if settled == 1 else 'ies'} skipped: already reviewed at this text")
    print(f"{len(rows)} claims; {len(jobs)} evidence entries to judge, {reused} already judged; "
          f"not checkable: {dict(skipped) or 0}", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    spent, counts = 0.0, collections.Counter()
    with args.out.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
        pending, it = {}, iter(jobs)
        while True:
            while len(pending) < args.concurrency and spent < args.budget:
                job = next(it, None)
                if job is None:
                    break
                r, anchor, title, block, subs, source, basis, text, d = job
                pending[ex.submit(judge, r["claim"], title, block, subs, source, basis, text,
                                  args.model, key)] = job
            if not pending:
                break
            fut = next(concurrent.futures.as_completed(pending))
            r, anchor, title, block, subs, source, basis, text, d = pending.pop(fut)
            try:
                res = fut.result()
            except Exception as e:
                res = {"verdict": "error", "issues": [f"{type(e).__name__}: {e}"[:300]], "cost_usd": 0}
            spent += res.get("cost_usd") or 0
            counts[res["verdict"]] += 1
            fh.write(json.dumps({"claim": r["claim"], "entry": anchor, "source": source, "basis": basis,
                                 "designs": r["designs"], "claims": r["claims"], "merged": r["merged"],
                                 "digest": d, "model": args.model, "judged_at": time.strftime("%Y-%m-%d"),
                                 **res}) + "\n")
            fh.flush()
    left = len(jobs) - sum(counts.values())
    print(f"judged {sum(counts.values())}: {dict(counts)}; ${spent:.3f}"
          + (f"; stopped at the budget with {left} left" if left else ""))
    print(f"read the failures: python3 scripts/check_load_bearing.py --report --out {args.out}")


if __name__ == "__main__":
    main()
