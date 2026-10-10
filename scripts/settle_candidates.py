#!/usr/bin/env python3
"""
settle_candidates.py — decide what each principle, pattern, element or theory candidate becomes.

Pass 2 of the candidate process (candidates_lib.py has the why). Ingest puts every
principle and pattern an extraction proposes into eval/candidates/candidates.ndjson
instead of writing a page. This shows each open candidate, with the claims it cites,
the canonical principle and pattern pages nearest to it (BM25) and the open
candidates from other sources nearest to it, to one model, which answers:

    attach N   the candidate is canonical page N's idea, or a narrower case of it
    join N     it is the same idea as open candidate N, from another source
    new        a general idea nothing listed covers; it waits for a second source
    design     one setting's design: a course, lesson sequence or one site's implementation
    product    a named product or programme others adopt, or one programme's own framework,
               tool or indicator (with its name, kind and a one-line description)
    research-method  a method for studying learning or evaluating education that is
               specific to education or especially useful there (with its name);
               general social-science methods are drops
    drop       too thin for a page: one finding restated, or an opinion

and, for `attach`, which of the candidate's claims bear on that page, with what
marker, and whether each tests the page's own relationship. With --apply:

    attach  each claim that bears on the page is listed under the page's
            `## Further evidence, not yet read against this model` (a converted page)
            or `### Claims` (any other), its marker capped at what the claim's
            recorded evidence allows (link_pages.strength_cap), with the source and
            the candidate's title beside it. A claim the page already links is skipped.
    design  written as a draft page in designs/, from the candidate's own fields.
    product, research-method  written to the page in products/ or research-methods/
            for that name (write_named): a new draft page, or a component or account,
            claims and source added to the page the name already has.

and every decision is appended to eval/candidates/decisions.ndjson. `new` and `join`
stay open and are asked again on the next run, when a later batch may have brought
the matching page or the second source.

A cluster (candidates joined to one another) is PROMOTED when it rests on two
independent sources (different articles with no author in common and not published by
the same organisation: `independent`), or on one synthesis: a claim it cites whose evidence entry is a
quant-synthesis or review coded q3 or above. Promotion writes nothing: `--report`
lists the promoted clusters for an agent to write as canonical pages in the
conditional-model format (principle-pattern-authoring.md), and the canonical pages
whose attached claims test their relationship, for an agent to update.

Canonical pages are the principles and patterns the 2026-10-02 triage classed as
canonical (eval/page-triage/triage.tsv), plus every page converted since.

Elements and theories (2026-10-09) are decided the same way against their own
canonical index: every element or theory page no batch wrote (the curated ones),
plus any batch page ten or more pages link to. After the decisions, links the
source's own pages make to the candidate are resolved: to the page it attaches to,
to its design, product or research-method page, or unlinked (resolve_links).
Until 2026-10-10 a product, tool or one programme's framework was an "artifact",
recorded and written nowhere; products/ and research-methods/ replaced it, and
those candidates are no longer settled, so the next run asks them again.

    python3 scripts/settle_candidates.py                    # settle open candidates (dry run)
    python3 scripts/settle_candidates.py --apply            # and write attachments and designs
    python3 scripts/settle_candidates.py --report           # clusters, promotions, update queue
    python3 scripts/settle_candidates.py --backlog --out eval/runs/candidates/backlog.ndjson
        # the principle and pattern pages batches wrote before the ledger, settled as
        # if they were candidates; writes nothing, so the backlog can be measured first
"""
import argparse
import collections
import concurrent.futures
import csv
import json
import math
import os
import re
import unicodedata
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import candidates_lib as cl  # noqa: E402
import link_pages as lp  # noqa: E402
import okf_lib  # noqa: E402
import search_index  # noqa: E402

TRIAGE = WIKI_ROOT / "eval" / "page-triage" / "triage.tsv"
FAMILY = {"principle": "pp", "pattern": "pp", "element": "elements", "theory": "theories"}
FAMILY_FOLDERS = {"pp": ("principles", "patterns"), "elements": ("elements",), "theories": ("theories",)}
ET_CANON_INBOUND = 10   # a batch-written element or theory this many pages link to is canonical
FURTHER = "Further evidence, not yet read against this model"
CONVERTED_MARK = "\n## " + FURTHER  # every converted page has it; the other headings vary by wave
SYSTEM = "You organise a learning-design wiki. Reply with one JSON object and nothing else."
DEFAULT_MODEL = "openai/gpt-5.6-luna"
WORD = re.compile(r"[a-z][a-z-]+")
STOP = set("""a an the and or of to in on for with by from as at is are be this that these those it its
their them they we our can should not into over more most less than when which who what how use using
learners learner learning students student teaching teacher teachers instruction instructional""".split())

PROMPT = """A learning-design wiki keeps ONE canonical page per general principle or pattern. A principle is a
design recommendation; a pattern is a reusable instructional design. Both are general: reusable across
domains and settings. A course or programme for one setting is a DESIGN, never a pattern. Extraction read one
article and proposed the CANDIDATE below. Decide what it becomes.

CANDIDATE [{ctype}] from {source}
Title: {title}
{description}
{extra}
Claims it cites:
{claims}

CANONICAL PAGES nearest by text (numbers refer to the full CANONICAL INDEX in the system message, which lists
every canonical page; a page there that is not shown here may fit better):
{canon}

OPEN CANDIDATES (proposed from other sources, not yet pages):
{open}

PRODUCT AND RESEARCH-METHOD PAGES the wiki already has (reuse a name exactly when the candidate is one of
these or part of one):
{named}

Outcomes:
- "attach": the candidate states a canonical page's idea, or a narrower case of it (one setting, population,
  medium or component), so its evidence belongs on that page. Give "n", the page's number in the CANONICAL
  INDEX. Check the whole index, not only the pages shown. Prefer attach whenever a reader of that page should
  see this source.
- "join": no canonical page fits, but an open candidate states the same general idea. Give "n", its letter.
- "new": a general, reusable principle or pattern that no page in the whole CANONICAL INDEX covers, even as a
  broader idea. Name the closest index page in "why" and say what it lacks.
- "design": one setting's design: a course, lesson sequence, or one school's, district's or study's
  implementation, described for its learners and setting.
- "product": a named product or programme that others adopt or use: software, an app or platform, a
  curriculum or programme package, an assessment, test or measurement instrument, a dataset, a branded
  intervention or initiative; or one such programme's or organisation's own framework, model, indicator,
  rubric or theory of change. Give "name", the product or programme it is or belongs to, as its maker names
  it: the programme or initiative, not the component (the To&Through Milestones Tool, Online Tool and data
  tool all belong to "To&Through Project"; the CRIS Menu belongs to "College Readiness Indicator Systems
  (CRIS)"), "product_kind" (one of software,
  curriculum, assessment, dataset, programme, framework) and "product_description", one sentence on what
  that product or programme is and who makes or runs it.
- "research-method": a method for studying learning or evaluating education that is specific to education
  or especially useful there: cluster-randomised trials of schools and their power, evidence standards such
  as the What Works Clearinghouse's, design-based research, knowledge tracing, learning analytics methods,
  growth and value-added models, early-warning indicator construction. Give "name". A general social-science
  method (regression, surveys, interviews, factor analysis, qualitative coding) is "drop".
- "drop": not a page: it restates one empirical finding (that is a claim), or is an aspiration or opinion
  with no actionable design content, or is too vague to act on.

For "attach" only, judge each of the candidate's claims against THAT page: "bears" (is the claim directly
about the page's practice or idea?), "marker" (+ supports the page, ~ depends on conditions, - counts against
it; then S/M/W from the claim's evidence line, e.g. "+W"), and "tests" (does the claim test the page's central
relationship, as opposed to illustrating it?). A null, non-significant or "no difference" result is never "+":
it is "~" (the relationship did not show here) or "-" (it counts against the page).
Reply: {{"outcome": "...", "n": <number or letter or null>, "why": "one sentence",
 "name": <for product or research-method>, "product_kind": ..., "product_description": ...,
 "claims": [{{"k": <claim number>, "bears": true, "marker": "+W", "tests": false}}]}}"""


ET_PROMPT = """A learning-design wiki keeps ONE canonical page per general {kind}. {what} Extraction read one
article and proposed the CANDIDATE below as a new {kind} page. Most such proposals restate a canonical page in
one source's words, or name something that is not a general {kind} at all. Decide what it becomes.

CANDIDATE [{ctype}] from {source}
Title: {title}
{description}
{extra}
Claims it cites:
{claims}

CANONICAL PAGES nearest by text (numbers refer to the full CANONICAL INDEX in the system message):
{canon}

OPEN CANDIDATES (proposed from other sources, not yet pages):
{open}

PRODUCT AND RESEARCH-METHOD PAGES the wiki already has (reuse a name exactly when the candidate is one of
these or part of one):
{named}

Outcomes:
- "attach": the candidate is a canonical page's {kind}, a variant of it, or a narrower case of it, so its
  evidence belongs on that page. Give "n", the page's number in the CANONICAL INDEX. Check the whole index.
  Prefer attach whenever a reader of that page should see this source.
- "join": no canonical page fits, but an open candidate is the same general {kind}. Give "n", its letter.
- "new": a general {kind}, used or studied beyond this one source, that no index page covers. Name the
  closest index page in "why" and say what it lacks.
- "design": one setting's design: a course, lesson sequence, or one school's, district's or study's
  implementation, described for its learners and setting.
- "product": a named product or programme that others adopt or use: software, an app or platform, a
  curriculum or programme package, an assessment, test or measurement instrument, a dataset, a branded
  intervention or initiative; or one such programme's or organisation's own framework, model, indicator,
  rubric or theory of change. Give "name", the product or programme it is or belongs to, as its maker names
  it: the programme or initiative, not the component (the To&Through Milestones Tool, Online Tool and data
  tool all belong to "To&Through Project"; the CRIS Menu belongs to "College Readiness Indicator Systems
  (CRIS)"), "product_kind" (one of software,
  curriculum, assessment, dataset, programme, framework) and "product_description", one sentence on what
  that product or programme is and who makes or runs it.
- "research-method": a method for studying learning or evaluating education that is specific to education
  or especially useful there: cluster-randomised trials of schools and their power, evidence standards such
  as the What Works Clearinghouse's, design-based research, knowledge tracing, learning analytics methods,
  growth and value-added models, early-warning indicator construction. Give "name". A general social-science
  method (regression, surveys, interviews, factor analysis, qualitative coding) is "drop".
- "drop": not a page: it restates one empirical finding (that is a claim), or is too vague to act on.

For "attach" only, judge each of the candidate's claims against THAT page: "bears" (is the claim directly
about the page's {kind}?), "marker" (+ supports or illustrates it, ~ depends on conditions, - counts against
it; then S/M/W from the claim's evidence line, e.g. "+W"), and "tests" (does the claim test the page's central
idea, as opposed to illustrating it?). A null, non-significant or "no difference" result is never "+".
Reply: {{"outcome": "...", "n": <number or letter or null>, "why": "one sentence",
 "name": <for product or research-method>, "product_kind": ..., "product_description": ...,
 "claims": [{{"k": <claim number>, "bears": true, "marker": "+W", "tests": false}}]}}"""

ET_WHAT = {
    "elements": ("instructional element",
                 "An element is a general building block of instruction (worked examples, feedback, a "
                 "rubric, a simulation, peer tutoring), reusable across courses and domains."),
    "theories": ("learning theory",
                 "A theory is a general explanatory framework of how people learn or are taught "
                 "(cognitive load theory, self-determination theory), not one study's model or one "
                 "programme's theory of change."),
}


# ---------------------------------------------------------------- canonical pages

def canonical_keys() -> set:
    keys = set()
    if TRIAGE.exists():
        for r in csv.DictReader(TRIAGE.open(encoding="utf-8"), delimiter="\t"):
            if r.get("verdict") == "canonical" and (WIKI_ROOT / f"{r['key']}.md").exists():
                keys.add(r["key"])
    for folder in ("principles", "patterns"):
        for p in (WIKI_ROOT / folder).glob("*.md"):
            if p.stem != "index" and CONVERTED_MARK in p.read_text(encoding="utf-8"):
                keys.add(f"{folder}/{p.stem}")
    edges = json.loads((WIKI_ROOT / "reverse-index.json").read_text(encoding="utf-8"))["edges"]
    for folder in ("elements", "theories"):
        inbound = {s: sum(len(v) for v in d.values()) for s, d in edges.get(folder, {}).items()}
        for p in (WIKI_ROOT / folder).glob("*.md"):
            if p.stem == "index":
                continue
            head = p.read_text(encoding="utf-8")[:800]
            if "process:wiki-ingest" not in head or inbound.get(p.stem, 0) >= ET_CANON_INBOUND:
                keys.add(f"{folder}/{p.stem}")
    return keys


def is_converted(key: str) -> bool:
    return CONVERTED_MARK in (WIKI_ROOT / f"{key}.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- claims

_claim_cache = {}


def claim_info(slug: str) -> dict | None:
    """Title, evidence line, and whether any entry is a synthesis at q3+."""
    if slug in _claim_cache:
        return _claim_cache[slug]
    path = WIKI_ROOT / "claims" / f"{slug}.md"
    info = None
    if path.exists():
        rec = lp.record(f"claims/{slug}", path)
        fm_lines, _ = okf_lib.split_frontmatter(path.read_text(encoding="utf-8"))
        synth = False
        try:
            import yaml
            fm = yaml.safe_load("\n".join(fm_lines)) or {}
            for s in fm.get("sources") or []:
                q = s.get("q")
                if s.get("kind") in ("quant-synthesis", "review") and isinstance(q, int) and q >= 3:
                    synth = True
        except Exception:
            pass
        info = {"slug": slug, "title": rec["title"], "evidence": rec["evidence"], "synthesis": synth}
    _claim_cache[slug] = info
    return info


def cited_claims(cand: dict) -> list:
    out, seen = [], set()
    for c in cand.get("claims_cited") or []:
        slug = c.get("slug") if isinstance(c, dict) else c
        if isinstance(slug, str) and slug not in seen and (info := claim_info(slug)):
            seen.add(slug)
            out.append({**info, "tag": c.get("tag") if isinstance(c, dict) else None})
    return out


# ---------------------------------------------------------------- open-candidate similarity

def _tokens(text: str) -> list:
    return [w for w in WORD.findall(text.lower()) if w not in STOP]


class Similar:
    """TF-IDF cosine over open candidates' titles and descriptions: small enough
    (hundreds of rows) that an index would be more code than it saves."""

    def __init__(self, cands: list):
        self.rows = cands
        self.vecs = []
        df = collections.Counter()
        toks = [_tokens(f"{c.get('title', '')} {c.get('title', '')} {c.get('description', '')}") for c in cands]
        for t in toks:
            df.update(set(t))
        n = max(len(cands), 1)
        self.idf = {w: math.log(n / d) + 1 for w, d in df.items()}
        for t in toks:
            tf = collections.Counter(t)
            v = {w: f * self.idf[w] for w, f in tf.items()}
            norm = math.sqrt(sum(x * x for x in v.values())) or 1
            self.vecs.append({w: x / norm for w, x in v.items()})

    def near(self, cand: dict, k: int = 5) -> list:
        tf = collections.Counter(_tokens(f"{cand.get('title', '')} {cand.get('title', '')} {cand.get('description', '')}"))
        v = {w: f * self.idf.get(w, 1) for w, f in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        scored = []
        for row, vec in zip(self.rows, self.vecs):
            if row["id"] == cand["id"] or row["article_id"] == cand["article_id"]:
                continue
            s = sum(x / norm * vec.get(w, 0) for w, x in v.items())
            if s > 0.08:
                scored.append((s, row))
        return [r for _, r in sorted(scored, key=lambda x: -x[0])[:k]]


# ---------------------------------------------------------------- deciding

def short_source(cand: dict) -> str:
    """'Surname et al. (2025)' from the citation, else the article title."""
    cit = cand.get("citation") or ""
    m = re.match(r"\s*(.+?)\.?\s*\((\d{4}[a-z]?)\)", cit)
    if not m or len(m.group(1)) > 300:
        return (cand.get("article_title") or cand["article_id"])[:90]
    authors, year = m.group(1), m.group(2)
    first = re.split(r",|&| and ", authors)[0].strip()
    several = bool(re.search(r"&| and |,.*,", authors)) or authors.count(",") > 1
    return f"{first}{' et al.' if several else ''} ({year})"


def canon_neighbours(db, cand: dict, canon: set, k: int = 10) -> list:
    text = f"{cand.get('title', '')} {cand.get('description', '')}"
    found = []
    for folder in FAMILY_FOLDERS[FAMILY.get(cand.get("type"), "pp")]:
        for r in search_index.query(db, text, folder=folder, limit=40, mode="OR"):
            key = f"{r[1]}/{r[2]}"
            if key in canon and key != cand.get("page"):
                found.append((r[6], key))
    return [k for _, k in sorted(found, key=lambda x: -x[0])[:k]]


def system_prompt(index: list, family: str = "pp") -> str:
    """The canonical index, the same in every call so the provider can cache it."""
    what = {"pp": "principle and pattern", "elements": "element", "theories": "theory"}[family]
    return (SYSTEM + f"\n\nCANONICAL INDEX (every canonical {what} page):\n"
            + "\n".join(f"{i + 1}. [{r['folder'][:-1]}] {r['title']}" for i, r in enumerate(index)))


def decide(cand: dict, canon_recs: list, open_rows: list, api_key: str, model: str,
           index: list, system: str) -> dict:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    claims = cited_claims(cand)
    pos = {r["key"]: i for i, r in enumerate(index)}
    extra = []
    for f, label in (("requirements", "Requirements"), ("constraints", "Constraints"),
                     ("target_learners", "Learners"), ("target_learning_goals", "Goals")):
        v = cand.get(f)
        if v:
            extra.append(f"{label}: " + "; ".join(map(str, v if isinstance(v, list) else [v]))[:300])
    family = FAMILY.get(cand.get("type"), "pp")
    template = PROMPT if family == "pp" else ET_PROMPT
    kind, what = ET_WHAT.get(family, ("", ""))
    prompt = template.format(
        kind=kind, what=what,
        ctype=cand.get("type", "principle"), source=short_source(cand), title=cand.get("title", ""),
        description=(cand.get("description") or "")[:900], extra="\n".join(extra),
        claims="\n".join(f"{i + 1}. {c['title']} [evidence: {c['evidence'] or 'none recorded'}]"
                         for i, c in enumerate(claims)) or "(none)",
        canon="\n".join(f"{pos[r['key']] + 1}. [{r['folder'][:-1]}] {r['title']} — {r['description'][:220]}"
                         for r in canon_recs) or "(none near)",
        named=named_pages_list(),
        open="\n".join(f"{chr(65 + i)}. [{r.get('type')}] {r.get('title')} — {(r.get('description') or '')[:200]}"
                       f" (from {short_source(r)})" for i, r in enumerate(open_rows)) or "(none near)")
    for attempt in range(2):   # one resample: a reply with no JSON in it is a fault, not an answer
        gen = oc.generate(model, system, prompt, api_key, max_tokens=2500)
        try:
            d = extract_json(gen.raw_text)
            break
        except Exception:
            d = None
    if isinstance(d, dict) and d.get("outcome") == "artifact":
        d["outcome"] = "product"   # the outcome's old name, which the model may still use
    if not isinstance(d, dict) or d.get("outcome") not in cl.OUTCOMES:
        return {"id": cand["id"], "outcome": "error", "why": (gen.raw_text or "")[:200],
                "cost_usd": gen.cost_usd}
    out = {"id": cand["id"], "outcome": d["outcome"], "why": d.get("why"), "model": model,
           "cost_usd": gen.cost_usd, "at": date.today().isoformat()}
    n = d.get("n")
    if d["outcome"] in ("product", "research-method"):
        name = d.get("name") if isinstance(d.get("name"), str) and d["name"].strip() else cand.get("title")
        out["name"] = name.strip()
        if d["outcome"] == "product":
            kind = d.get("product_kind")
            out["product_kind"] = kind if kind in PRODUCT_KINDS else None
            out["product_description"] = (d.get("product_description") or "").strip() or None
        return out
    if d["outcome"] == "attach":
        if not (isinstance(n, int) and 1 <= n <= len(index)) or index[n - 1]["key"] == cand.get("page"):
            return {**out, "outcome": "error", "why": f"attach without a valid page number: {n!r}"}
        target = index[n - 1]["key"]
        attached = []
        for item in d.get("claims") or []:
            k = item.get("k")
            if not (isinstance(k, int) and 1 <= k <= len(claims)) or not item.get("bears"):
                continue
            marker = item.get("marker")
            if not (isinstance(marker, str) and lp.MARKER_RE.match(marker)):
                continue
            cap = lp.strength_cap(claims[k - 1]["evidence"])
            if "WMS".index(marker[1]) > "WMS".index(cap):
                marker = marker[0] + cap
            attached.append({"claim": claims[k - 1]["slug"], "marker": marker, "tests": bool(item.get("tests"))})
        out.update(target=target, claims=attached)
    elif d["outcome"] == "join":
        idx = ord(n.upper()) - 65 if isinstance(n, str) and len(n) == 1 else -1
        if not 0 <= idx < len(open_rows):
            return {**out, "outcome": "new", "why": f"{d.get('why')} (join named no listed candidate: {n!r})"}
        out["with"] = open_rows[idx]["id"]
    return out


def verify_attachments(decs: list, cands: dict, model: str, concurrency: int) -> None:
    """A second read of every claim an `attach` decision would write, with
    link_pages' verifier: the deciding call judges fit and direction for all of a
    candidate's claims at once, and on batch 13 it attached null results as `+`
    and learning-style subgroup results to cognitive-load management. Only claims
    the verifier keeps, with the direction confirmed, are written; the rest are
    kept on the decision as `rejected`, so the record shows what was refused."""
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    pages = lp.all_pages()

    def one(dec, a):
        page = dec["target"]
        prec = lp.record(page, pages[page])
        crec = lp.record(f"claims/{a['claim']}", WIKI_ROOT / "claims" / f"{a['claim']}.md")
        sub = next((l for l in (WIKI_ROOT / "claims" / f"{a['claim']}.md").read_text(encoding="utf-8").split("\n")
                    if re.match(r"^`q[\d?]", l)), "")
        prompt = lp.VERIFY_PROMPT.format(
            kind=lp.KIND[prec["folder"]], ptitle=prec["title"],
            pdesc=(prec["description"] + " " + lp._desc_section(pages[page]))[:900],
            ctitle=crec["title"], cevidence="Evidence: " + (crec["evidence"] or "none recorded"),
            csub=("Subclaim: " + sub[:300]) if sub else "", marker=a["marker"],
            direction={"+": "supports the page", "~": "depends on conditions",
                       "-": "counts against the page"}[a["marker"][0]])
        gen = oc.generate(model, lp.SYSTEM, prompt, key, max_tokens=800)
        d = extract_json(gen.raw_text)
        return bool(d.get("keep")) and bool(d.get("direction_ok")), d.get("why"), gen.cost_usd

    jobs = [(d, a) for d in decs if d["outcome"] == "attach" for a in d.get("claims") or []]
    with concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        results = list(ex.map(lambda j: one(*j), jobs))
    for (d, a), (keep, why, cost) in zip(jobs, results):
        d["cost_usd"] = (d.get("cost_usd") or 0) + (cost or 0)
        a["verifier"] = why
        if not keep:
            d.setdefault("rejected", []).append(a)
    for d in decs:
        if d.get("rejected"):
            d["claims"] = [a for a in d["claims"] if a not in d["rejected"]]
    print(f"verified {len(jobs)} attachment(s): kept {len(jobs) - sum(len(d.get('rejected') or []) for d in decs)}")


def settle(cands: list, open_pool: list, model: str, concurrency: int) -> list:
    api_key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    canon = canonical_keys()
    pages = lp.all_pages()
    search_index.ensure().close()
    sim = Similar(open_pool)
    recs = {}

    def rec(k):
        if k not in recs:
            recs[k] = lp.record(k, pages[k])
        return recs[k]

    indexes, systems = {}, {}
    for family, folders in FAMILY_FOLDERS.items():
        indexes[family] = [rec(k) for k in sorted(canon) if k in pages and k.split("/")[0] in folders]
        systems[family] = system_prompt(indexes[family], family)

    def one(cand):
        db = sqlite3.connect(search_index.DB_PATH)
        family = FAMILY.get(cand.get("type"), "pp")
        try:
            near = [rec(k) for k in canon_neighbours(db, cand, canon) if k in pages]
            return decide(cand, near, sim.near(cand), api_key, model, indexes[family], systems[family])
        except Exception as e:
            return {"id": cand["id"], "outcome": "error", "why": f"{type(e).__name__}: {e}"[:300]}
        finally:
            db.close()

    with concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        return list(ex.map(one, cands))


# ---------------------------------------------------------------- writing

def write_attach(dec: dict, cand: dict) -> int:
    path = WIKI_ROOT / f"{dec['target']}.md"
    if not path.exists():
        return 0
    converted = is_converted(dec["target"])
    folder = dec["target"].split("/")[0]
    n = 0
    for a in dec.get("claims") or []:
        claim = f"claims/{a['claim']}"
        if lp.links_to(path, claim):
            continue
        info = claim_info(a["claim"])
        title = info["title"].replace("[", "(").replace("]", ")")
        note = (f" — attached {dec['at']} from {short_source(cand)}, which proposed "
                f"\"{(cand.get('title') or '').strip()}\""
                + ("; tests this page's relationship" if a.get("tests") else "") + ".")
        bullet = f"- [{title}](../claims/{a['claim']}.md) [{a['marker']}]{note}"
        if converted:
            heads = [FURTHER]
        else:
            heads = (["Supporting"] if a["marker"][0] == "+" else ["Contradicting"]) if folder == "patterns" else []
            heads += ["Claims"]
        lp.insert(path, heads, bullet, FURTHER if converted else "Claims")
        n += 1
    return n


PRODUCT_KINDS = ("software", "curriculum", "assessment", "dataset", "programme", "framework")
KIND_FOLDER = {"product": "products", "research-method": "research-methods"}
_NAME_GENERIC = {"the", "a", "an", "of", "and", "for", "in", "project", "program", "programme",
                 "initiative", "tool", "platform", "framework", "model", "method"}


def name_key(name: str) -> str:
    """One product or method, however a source words its name: filler and generic words
    out, so "To&Through Project" and "the To&Through project" are one page."""
    words = [w for w in re.findall(r"[a-z0-9]+", (name or "").lower()) if w not in _NAME_GENERIC]
    return " ".join(words) or " ".join(re.findall(r"[a-z0-9]+", (name or "").lower()))


def named_pages_list() -> str:
    """The titles of every products/ and research-methods/ page, for the prompt, so a
    later candidate is given an existing page's name rather than a new variant of it."""
    rows = []
    for folder, label in (("products", "product"), ("research-methods", "research method")):
        for p in sorted((WIKI_ROOT / folder).glob("*.md")):
            if p.stem != "index":
                m = re.search(r"^title:\s*(.+)$", p.read_text(encoding="utf-8")[:1500], re.M)
                if m:
                    rows.append(f"- [{label}] {m.group(1).strip().strip(chr(34))}")
    return "\n".join(rows) or "(none yet)"


def find_named_page(folder: str, name: str) -> "Path | None":
    key = name_key(name)
    for p in sorted((WIKI_ROOT / folder).glob("*.md")):
        if p.stem == "index":
            continue
        m = re.search(r"^title:\s*(.+)$", p.read_text(encoding="utf-8")[:1500], re.M)
        if m and name_key(m.group(1).strip().strip('"')) == key:
            return p
    return None


def _section_add(text: str, heading: str, lines: list, before: tuple) -> str:
    """Append lines (skipping any already present) under `heading`, creating it before
    the first of `before` that exists, else at the end."""
    lines = [l for l in lines if l and l not in text]
    if not lines:
        return text
    m = re.search(rf"^{re.escape(heading)}[ \t]*\n", text, re.M)
    if m:
        nxt = re.search(r"^#{1,3} ", text[m.end():], re.M)
        cut = m.end() + (nxt.start() if nxt else len(text) - m.end())
        block = [l for l in text[m.end():cut].rstrip("\n").split("\n") if l.strip() not in ("-", "")]
        rest = text[cut:]
        return text[:m.end()] + "\n".join(block + lines) + ("\n\n" + rest if rest else "\n")
    for b in before:
        mb = re.search(rf"^{re.escape(b)}[ \t]*$", text, re.M)
        if mb:
            return text[:mb.start()] + f"{heading}\n" + "\n".join(lines) + "\n\n" + text[mb.start():]
    return text.rstrip("\n") + f"\n\n{heading}\n" + "\n".join(lines) + "\n"


def write_named(cand: dict, dec: dict, actor: str) -> "str | None":
    """Write a `product` or `research-method` decision to its page: the page for that
    name if one exists (name_key), else a new draft page. The candidate is listed as a
    component (a product's framework, tool or indicator) or as a source's account (a
    method), with its cited claims, markers capped at their recorded evidence, and its
    source under Key Sources. Returns the page path relative to the wiki."""
    folder = KIND_FOLDER[dec["outcome"]]
    name = dec.get("name") or cand.get("title") or ""
    if not name_key(name):
        return None
    path = find_named_page(folder, name)
    citation = cand.get("citation") or ""
    claims = []
    for c in cited_claims(cand):
        tag = c.get("tag") if isinstance(c.get("tag"), str) and lp.MARKER_RE.match(c["tag"] or "") else None
        if tag:
            cap = lp.strength_cap(c["evidence"])
            if "WMS".index(tag[1]) > "WMS".index(cap):
                tag = tag[0] + cap
        claims.append(f"- [{c['title']}](../claims/{c['slug']}.md)" + (f" [{tag}]" if tag else ""))
    is_itself = name_key(re.split(r":| [-–—] ", cand.get("title", ""))[0]) == name_key(name)
    own = f"- **{cand.get('title', '').strip()}**: {(cand.get('description') or '').strip()} ({short_source(cand)})"
    tail = ("## Related Products and Programmes" if folder == "products" else "## Related Research Methods",
            "## Key Sources")
    if path is None:
        # Slugs are ASCII: fold accents (Español -> espanol) before slugifying.
        ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
        slug = okf_lib.slugify(ascii_name)[:90].strip("-")
        path = WIKI_ROOT / folder / f"{slug}.md"
        if path.exists():
            return None
        desc = dec.get("product_description") if folder == "products" else None
        desc = desc or (cand.get("description") or "").strip() or name
        fm = {"type": dec["outcome"], "id": slug, "title": name,
              "description": re.split(r"(?<=[.!?])\s", desc.strip(), maxsplit=1)[0][:300]}
        if folder == "products" and dec.get("product_kind"):
            fm["product_kind"] = dec["product_kind"]
        fm.update({"status": "draft", "generated": {"by": actor, "at": date.today().isoformat()}})
        middle = ("## Components\n<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->\n"
                  if folder == "products" else
                  "## Accounts\n<!-- How each source describes or uses the method -->\n")
        body = (f"\n# {name}\n\n## Description\n{desc}\n\n{middle}"
                f"\n### Claims\n\n{tail[0]}\n-\n\n## Key Sources\n-\n")
        path.write_text(okf_lib.dump_frontmatter(fm) + body, encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    section = "## Components" if folder == "products" else "## Accounts"
    if not (is_itself and section == "## Components"):
        text = _section_add(text, section, [own], ("### Claims",) + tail)
    text = _section_add(text, "### Claims", claims, tail)
    if citation:
        text = _section_add(text, "## Key Sources", [f"- {citation}"], ())
    path.write_text(text, encoding="utf-8")
    return f"{folder}/{path.name}"


_LINK = re.compile(r"\[([^\]]*)\]\(((?:\.\./[a-z-]+/)?([^)/#\s]+)\.md)(#[^)]*)?\)")


def resolve_links(cand: dict, dec: "dict | None", source_pages: dict) -> int:
    """Point the links an element or theory candidate's own source made to it (from that
    article's claims and strategies, which ingest left as written) at what it became:
    the canonical page it attaches to, the design page written for it, or, for any other
    outcome or none, no link (the text stays). A slug that is a page anyway is left alone."""
    folder = {"element": "elements", "theory": "theories"}.get(cand.get("type"))
    slug = cand.get("slug")
    if not folder or not slug or (WIKI_ROOT / folder / f"{slug}.md").exists():
        return 0
    target = None
    if dec and dec.get("outcome") == "attach":
        target = dec.get("target")
    elif dec and dec.get("outcome") in ("design", "product", "research-method") and dec.get("page"):
        target = dec["page"][:-3]
    n = 0
    for rel in source_pages.get(cand.get("article_id"), []):
        path = WIKI_ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")

        def fix(m):
            nonlocal n
            if m.group(3) != slug or (path.parent / m.group(2)).resolve() != (WIKI_ROOT / folder / f"{slug}.md").resolve():
                return m.group(0)
            n += 1
            if not target or not (WIKI_ROOT / f"{target}.md").exists():
                return m.group(1)
            tf, ts = target.split("/")
            dest = f"{ts}.md" if tf == path.parent.name else f"../{tf}/{ts}.md"
            return f"[{m.group(1)}]({dest})"

        out = _LINK.sub(fix, text)
        if out != text:
            path.write_text(out, encoding="utf-8")
    return n


def source_pages_by_article() -> dict:
    """article id -> the pages its latest ingest wrote (sources/manifest.ndjson)."""
    out = {}
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        m = json.loads(line)
        if m.get("status") == "ingested" and m.get("pages"):
            out[m["id"]] = m["pages"]
    return out


_GENERIC = {"the", "a", "an", "of", "and", "for", "in", "project", "program", "programme",
            "initiative", "intervention", "model", "curriculum", "course"}


def design_name_key(title: str) -> str:
    """A design's programme name: its title before the first colon or dash, without
    filler and generic words. "Tough As Nails: NSF-funded ..." and "Tough as Nails
    project: a K-8 ..." are one programme written up from two sources (batch 47)."""
    head = re.split(r":|\s[-–—]\s", title or "", maxsplit=1)[0]
    return " ".join(w for w in re.findall(r"[a-z0-9]+", head.lower()) if w not in _GENERIC)


def existing_design(title: str) -> "Path | None":
    """The design page already written for the programme this title names, if any.
    A name key of one word is too weak to match on."""
    key = design_name_key(title)
    if len(key.split()) < 2:
        return None
    for p in sorted((WIKI_ROOT / "designs").glob("*.md")):
        if p.stem == "index":
            continue
        m = re.search(r"^title:\s*(.+)$", p.read_text(encoding="utf-8")[:1500], re.M)
        if m and design_name_key(m.group(1).strip().strip('"')) == key:
            return p
    return None


def add_key_source(path: Path, citation: str) -> bool:
    """Append a citation to a page's `## Key Sources`, unless it is there already."""
    text = path.read_text(encoding="utf-8")
    if not citation or citation in text or "## Key Sources" not in text:
        return False
    head, tail = text.split("## Key Sources", 1)
    m = re.search(r"\n(?=## |<!--)", tail)
    cut = m.start() if m else len(tail)
    section = tail[:cut].rstrip("\n") + f"\n- {citation}\n"
    path.write_text(head + "## Key Sources" + section + ("\n" + tail[cut:].lstrip("\n") if tail[cut:].strip() else ""),
                    encoding="utf-8")
    return True


def write_design(cand: dict, actor: str) -> str | None:
    """Write the design page a candidate became, or, when the programme already has one
    (existing_design), add the candidate's source to that page's Key Sources and return it."""
    import ingest_extractions as ie
    same = existing_design(cand.get("title", ""))
    if same:
        add_key_source(same, cand.get("citation") or "")
        return f"designs/{same.name}"
    contrib = {k: cand[k] for k in cl.FIELDS if k in cand}
    contrib["type"] = "design"
    if cand.get("citation"):
        contrib["key_sources"] = [cand["citation"]]
    rendered = ie.render_page(contrib, actor)
    if not rendered:
        return None
    folder, slug, fm, body = rendered
    path = WIKI_ROOT / folder / f"{slug}.md"
    if path.exists():
        return None
    path.write_text(okf_lib.dump_frontmatter(fm) + "\n" + body, encoding="utf-8")
    # A pattern candidate's related slugs name pages in other folders (an element the same
    # article produced); ingest's repair points each at the folder that has it.
    ie.repair_cross_folder_links([f"{folder}/{slug}.md"])
    lines = []
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.search(r"\]\(([a-z0-9-]+)\.md\)", line)
        if m and not (WIKI_ROOT / folder / f"{m.group(1)}.md").exists():
            home = next((f for f in okf_lib.CONTENT_FOLDERS if (WIKI_ROOT / f / f"{m.group(1)}.md").exists()), None)
            if home:
                line = line.replace(f"({m.group(1)}.md)", f"(../{home}/{m.group(1)}.md)")
            elif line.lstrip().startswith("- "):
                continue          # a related page that does not exist anywhere
        lines.append(line)
    path.write_text("\n".join(lines), encoding="utf-8")
    return f"{folder}/{slug}.md"


# ---------------------------------------------------------------- report

_CATALOGUE = ("doi.org", "eric.ed.gov", "ncbi.nlm.nih.gov", "europepmc.org", "arxiv.org",
              "scholar.google", "semanticscholar.org", "openalex.org", "jstor.org", "researchgate.net")
_AUTHOR_STOP = {"and", "the", "for", "with", "et", "al", "eds", "ed", "inc", "llc", "jr"}


def source_identity(cand: dict) -> tuple:
    """(author words, organisations) for a candidate's source, from its citation.

    Author words are the capitalised words before the year: surnames and given names for
    people, the name itself for a corporate author ("Digital Promise"). Organisations are
    whatever the citation shows of its publisher: the domain of the first link that is
    not a catalogue or DOI resolver (consortium.uchicago.edu), the publisher named just
    before the link in a report citation ("Digital Promise"), and, for a report (not a
    journal article, whose DOI prefix is the journal publisher's), the DOI prefix, which
    is the registrant's (10.51388 is Digital Promise's)."""
    cit = cand.get("citation") or ""
    m = re.match(r"(.*?)\(\d{4}", cit)
    authors = m.group(1) if m and len(m.group(1)) < 400 else ""
    words = {w.lower() for w in re.findall(r"[A-Z][A-Za-z'’\-]{2,}", authors)} - _AUTHOR_STOP
    orgs = set()
    for url in re.findall(r"https?://([^/\s)]+)", cit):
        host = url.lower().removeprefix("www.")
        if not any(c in host for c in _CATALOGUE):
            orgs.add(host)
            break
    journal = bool(re.search(r"\d+\s*\(\d+[^)]*\)|,\s*\d+\s*[–-]\s*\d+", cit))
    if not journal:
        head = re.split(r"https?://", cit)[0].strip().rstrip(".")
        last = [x.strip() for x in re.split(r"\.\s+", head) if x.strip()]
        if len(last) >= 3 and not re.search(r"\d", last[-1]) and len(last[-1].split()) <= 6:
            orgs.add(last[-1].lower())
        doi = re.search(r"\b10\.(\d{4,9})/", cit)
        if doi:
            orgs.add(f"doi:10.{doi.group(1)}")
    return words, orgs


def independent(a: dict, b: dict) -> bool:
    """Two sources are independent when they come from different articles, share no
    author, and were not published by the same organisation (maintainer, 2026-10-10:
    one author or one organisation across several years is a research agenda, not
    independent confirmation). A source whose citation shows neither an author nor a
    publisher cannot be shown independent, and is not."""
    if a["article_id"] == b["article_id"]:
        return False
    wa, oa = source_identity(a)
    wb, ob = source_identity(b)
    if not (wa or oa) or not (wb or ob):
        return False
    return not (wa & wb) and not (oa & ob)


def clusters(cands: dict, decisions: dict) -> list:
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    open_ids = [i for i, d in decisions.items() if d["outcome"] in ("new", "join") and i in cands]
    for i in open_ids:
        find(i)
        w = decisions[i].get("with")
        if decisions[i]["outcome"] == "join" and w in cands and decisions.get(w, {}).get("outcome") in ("new", "join"):
            parent[find(i)] = find(w)
    groups = collections.defaultdict(list)
    for i in open_ids:
        groups[find(i)].append(cands[i])
    out = []
    for members in groups.values():
        sources = {m["article_id"] for m in members}
        firsts = list({m["article_id"]: m for m in members}.values())
        indep = any(independent(x, y) for i, x in enumerate(firsts) for y in firsts[i + 1:])
        # A synthesis counts only from an extracted candidate, whose cited claims are its own
        # article's. An existing page's claim links include every claim later linking added,
        # so for a page only two independent sources promote.
        synth = any(c["synthesis"] for m in members if m.get("origin") != "page" for c in cited_claims(m))
        out.append({"members": members, "sources": len(sources), "independent": indep, "synthesis": synth,
                    "promote": indep or synth})
    return sorted(out, key=lambda g: (-g["promote"], -g["sources"]))


def report(cands: dict, decisions: dict) -> None:
    outcome = collections.Counter(d["outcome"] for d in decisions.values())
    print(f"{len(cands)} candidates; {len(cands) - len(decisions)} not yet settled; decisions: {dict(outcome)}")
    groups = clusters(cands, decisions)
    prom = [g for g in groups if g["promote"]]
    print(f"\nopen clusters: {len(groups)}; promoted: {len(prom)}")
    for g in prom:
        why = (f"{g['sources']} sources" + (", independent" if g["independent"] else ", not independent")
               + (", a synthesis" if g["synthesis"] else ""))
        print(f"  PROMOTE ({why}):")
        for m in g["members"]:
            print(f"    - [{m.get('type')}] {m.get('title')}  ({short_source(m)})")
    tests = collections.defaultdict(list)
    for d in decisions.values():
        if d["outcome"] == "attach":
            for a in d.get("claims") or []:
                if a.get("tests"):
                    tests[d["target"]].append(a["claim"])
    print(f"\ncanonical pages with attached claims that test their relationship: {len(tests)}")
    for k, v in sorted(tests.items(), key=lambda x: -len(x[1])):
        print(f"  {k}: {', '.join(sorted(set(v)))}")
    designs = [d for d in decisions.values() if d["outcome"] == "design"]
    print(f"\ndesigns: {len(designs)}; dropped: {outcome.get('drop', 0)}")


# ---------------------------------------------------------------- backlog

FOLD_PROMPT = """A learning-design wiki keeps one canonical page per general principle or pattern. A first model
proposed folding PAGE into CANONICAL: PAGE's text would be kept in a comment on CANONICAL, its claims listed
there, and its links repointed. Decide whether that fold is right.

PAGE [{fkind}]: {ftitle}
{fdesc}

CANONICAL [{kkind}]: {ktitle}
{kdesc}

Fold only if PAGE states CANONICAL's idea, or a narrower case of it (one setting, population, medium or
component), so that a reader looking for PAGE's idea would be well served by CANONICAL. Refuse if PAGE's idea
is distinct, broader than CANONICAL, or only shares a topic or a word with it.
Reply: {{"fold": true/false, "why": "one clause"}}"""


def fold_backlog(path: Path, model: str, concurrency: int, apply: bool, out: Path) -> None:
    """Fold the backlog pages a --backlog run decided to attach, once a second read
    agrees. merge_pages.py does the fold (bullets, sources, the body in a merged
    comment, links repointed, an alias within one kind); markers it moved are then
    capped at what each claim's evidence allows."""
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    pages = lp.all_pages()
    decs = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    todo = [d for d in decs if d["outcome"] == "attach" and d["id"][5:] in pages and d["target"] in pages
            and d["id"][5:] != d["target"]]

    cache_path = WIKI_ROOT / "eval" / "runs" / "candidates" / "fold-check.ndjson"
    cache = {}
    if cache_path.exists():   # apply what the dry run decided, not a fresh sample of it
        for l in cache_path.read_text(encoding="utf-8").splitlines():
            r = json.loads(l)
            cache[(r["page"], r["target"])] = r

    def one(d):
        fold, keep = d["id"][5:], d["target"]
        if (fold, keep) in cache:
            return cache[(fold, keep)]
        for attempt in range(3):
            try:
                return ask(fold, keep, d)
            except Exception as e:
                err = f"{type(e).__name__}: {e}"[:200]
        return {"page": fold, "target": keep, "fold": False, "why": None, "error": err, "cost_usd": 0}

    def ask(fold, keep, d):
        f, k = lp.record(fold, pages[fold]), lp.record(keep, pages[keep])
        prompt = FOLD_PROMPT.format(
            fkind=lp.KIND[f["folder"]], ftitle=f["title"],
            fdesc=(f["description"] + " " + lp._desc_section(pages[fold]))[:900],
            kkind=lp.KIND[k["folder"]], ktitle=k["title"],
            kdesc=(k["description"] + " " + lp._desc_section(pages[keep]))[:900])
        gen = oc.generate(model, SYSTEM, prompt, key, max_tokens=800)
        v = extract_json(gen.raw_text) or {}
        return {"page": fold, "target": keep, "fold": bool(v.get("fold")), "why": v.get("why"),
                "first_why": d.get("why"), "cost_usd": gen.cost_usd, "at": date.today().isoformat()}

    with concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        results = list(ex.map(one, todo))
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in results
                                  if not r.get("error")), encoding="utf-8")
    kept = [r for r in results if r["fold"]]
    print(f"errors: {sum(bool(r.get('error')) for r in results)}")
    print(f"fold decisions read again: {len(results)}; confirmed {len(kept)}; "
          f"cost ${sum(r['cost_usd'] or 0 for r in results):.3f}")
    for r in results:
        if not r["fold"]:
            print(f"  refused {r['page']} -> {r['target']}: {r['why']}")
    if not apply:
        return
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh:
        for r in results:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    import merge_pages
    for r in kept:
        kkind, keep = r["target"].split("/")
        fkind, fold = r["page"].split("/")
        print(" ", merge_pages.merge(kkind, keep, fold if fkind == kkind else r["page"], True))
    capped = cap_markers(sorted({r["target"] for r in kept}))
    print(f"markers above their claim's cap lowered: {capped}")
    subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "build_indexes.py")], cwd=WIKI_ROOT,
                   capture_output=True)


def cap_markers(keys: list) -> int:
    """Lower every live claim marker on these pages that is stronger than the claim's
    recorded evidence allows (link_pages.strength_cap); direction is left alone."""
    n = 0
    for key in keys:
        path = WIKI_ROOT / f"{key}.md"
        if not path.exists():
            continue
        parts = re.split(r"(<!--.*?-->)", path.read_text(encoding="utf-8"), flags=re.S)

        def fix(m):
            nonlocal n
            info = claim_info(m.group(1))
            if not info:
                return m.group(0)
            cap = lp.strength_cap(info["evidence"])
            if "WMS".index(m.group(3)) > "WMS".index(cap):
                n += 1
                return m.group(0)[:-2] + cap + "]"
            return m.group(0)
        out = [x if x.startswith("<!--") else
               re.sub(r"\]\(\.\./claims/([^)#\s]+)\.md\)\s*\[([+~-])([SMW])\]", fix, x) for x in parts]
        path.write_text("".join(out), encoding="utf-8")
    return n


def backlog_candidates() -> list:
    """The principle and pattern pages batches wrote before the ledger existed, as
    candidates: each keeps the page key, so the dry run can say what it would fold into."""
    canon = canonical_keys()
    source = {}
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        e = json.loads(line)
        if e.get("status") != "ingested":
            continue
        for p in e.get("pages") or []:
            if p.startswith(("principles/", "patterns/")):
                source.setdefault(p[:-3], (e["id"], e.get("title", "")))
    out = []
    for key, (aid, atitle) in sorted(source.items()):
        path = WIKI_ROOT / f"{key}.md"
        if not path.exists() or key in canon:   # a canonical page is a target, not a candidate
            continue
        rec = lp.record(key, path)
        text = path.read_text(encoding="utf-8")
        claims = [{"slug": m.group(1), "tag": m.group(2)}
                  for m in re.finditer(r"\]\(\.\./claims/([^)#\s]+)\.md\)\s*\[([+~-][SMW])\]", text)]
        ks = re.search(r"^## Key Sources\s*\n- (.+)$", text, re.M)
        out.append({"id": f"page:{key}", "page": key, "article_id": aid, "article_title": atitle,
                    "type": key.split("/")[0][:-1], "slug": key.split("/")[1], "title": rec["title"],
                    "description": lp._desc_section(path) or rec["description"], "claims_cited": claims,
                    "citation": ks.group(1) if ks else None, "origin": "page"})
    return out


def mark_canonical(apply: bool) -> int:
    """Stamp `canonical: true` on every page in canonical_keys(), so search ranks the
    page the ledger settles against above the one-source pages on the same idea
    (build_wiki_index.py carries it into wiki-index.json). Only adds the key; a page
    that has it is left alone. Returns the number of pages (to be) stamped."""
    n = 0
    for key in sorted(canonical_keys()):
        path = WIKI_ROOT / f"{key}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        fm_lines, _ = okf_lib.split_frontmatter(text)
        if any(line.startswith("canonical:") for line in fm_lines):
            continue
        m = re.search(r"^status:", text, re.M)
        if not text.startswith("---\n") or not m or m.start() > text.find("\n---", 4):
            continue
        n += 1
        if apply:
            path.write_text(text[:m.start()] + "canonical: true\n" + text[m.start():], encoding="utf-8")
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write attachments and designs, and record decisions")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--backlog", action="store_true", help="dry run over pre-ledger batch pages")
    ap.add_argument("--fold-backlog", type=Path, metavar="DECISIONS",
                    help="fold the pages a --backlog run attached, after a second read (with --apply)")
    ap.add_argument("--mark-canonical", action="store_true",
                    help="stamp canonical: true on the canonical pages (with --apply; else count)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=None, help="decisions file for --backlog")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--by", default="process:settle-candidates")
    args = ap.parse_args()

    if args.mark_canonical:
        print(f"{mark_canonical(args.apply)} page(s) {'stamped' if args.apply else 'to stamp'} canonical: true")
        return
    if args.report:
        report(cl.load_candidates(), cl.load_decisions())
        return

    if args.fold_backlog:
        fold_backlog(args.fold_backlog, args.model, args.concurrency, args.apply,
                     cl.LEDGER_DIR / "backlog-folds.ndjson")
        return

    if args.backlog:
        cands = backlog_candidates()
        if args.limit:
            cands = cands[:args.limit]
        print(f"settling {len(cands)} pre-ledger batch pages as candidates (writes no page)")
        decs = settle(cands, cands, args.model, args.concurrency)
        out = Path(args.out or WIKI_ROOT / "eval" / "runs" / "candidates" / "backlog.ndjson")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("".join(json.dumps(d) + "\n" for d in decs), encoding="utf-8")
        byid = {c["id"]: c for c in cands}
        print(f"decisions -> {out}; cost ${sum(d.get('cost_usd') or 0 for d in decs):.3f}")
        report(byid, {d["id"]: d for d in decs if d["outcome"] != "error"})
        print(f"errors: {sum(d['outcome'] == 'error' for d in decs)}")
        return

    cands = cl.load_candidates()
    decisions = cl.load_decisions()
    canon = canonical_keys()
    todo = [c for i, c in cands.items() if decisions.get(i, {}).get("outcome") not in cl.SETTLED
            and c.get("page") not in canon]   # a page now canonical is a target, not a candidate
    if args.limit:
        todo = todo[:args.limit]
    if not todo:
        print("no open candidates")
        return
    pool = [c for i, c in cands.items() if decisions.get(i, {}).get("outcome") not in cl.SETTLED]
    print(f"settling {len(todo)} open candidate(s){'' if args.apply else ' (dry run)'}")
    decs = settle(todo, pool, args.model, args.concurrency)
    verify_attachments(decs, cands, args.model, args.concurrency)
    stats = collections.Counter(d["outcome"] for d in decs)
    print(f"outcomes: {dict(stats)}; cost ${sum(d.get('cost_usd') or 0 for d in decs):.3f}")
    for d in decs:
        c = cands[d["id"]]
        tgt = d.get("target") or d.get("with") or ""
        print(f"  {d['outcome']:7} {c.get('type')} {c.get('slug')}  {tgt}  — {d.get('why') or ''}"[:220])
    if not args.apply:
        return
    attached = designs = named = 0
    for d in decs:
        if d["outcome"] == "attach":
            attached += write_attach(d, cands[d["id"]])
        elif d["outcome"] == "design":
            path = write_design(cands[d["id"]], args.by)
            if path:
                d["page"] = path
                designs += 1
        elif d["outcome"] in ("product", "research-method"):
            path = write_named(cands[d["id"]], d, args.by)
            if path:
                d["page"] = path
                named += 1
    cl.append_decisions([d for d in decs if d["outcome"] != "error"])
    # Every element or theory candidate settled this run, whatever its outcome (an error
    # included), leaves no link to a page that does not exist.
    by_id = {d["id"]: d for d in decs}
    src = source_pages_by_article()
    relinked = sum(resolve_links(c, by_id.get(c["id"]), src) for c in todo
                   if c.get("type") in ("element", "theory"))
    if designs or named:
        import subprocess
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "add_type_banner.py"), "--apply"],
                       cwd=WIKI_ROOT, check=False)
    print(f"applied: {attached} claim link(s) attached, {designs} design page(s) written, "
          f"{named} product or research-method candidate(s) written, "
          f"{relinked} link(s) to element/theory candidates resolved; "
          f"decisions -> {cl.DECISIONS.relative_to(WIKI_ROOT)}")
    report(cands, cl.load_decisions())


if __name__ == "__main__":
    main()
