#!/usr/bin/env python3
"""
settle_candidates.py — decide what each principle or pattern candidate becomes.

Pass 2 of the candidate process (candidates_lib.py has the why). Ingest puts every
principle and pattern an extraction proposes into eval/candidates/candidates.ndjson
instead of writing a page. This shows each open candidate, with the claims it cites,
the canonical principle and pattern pages nearest to it (BM25) and the open
candidates from other sources nearest to it, to one model, which answers:

    attach N   the candidate is canonical page N's idea, or a narrower case of it
    join N     it is the same idea as open candidate N, from another source
    new        a general idea nothing listed covers; it waits for a second source
    design     a design for one setting, course, population or product
    drop       too thin for a page: one finding restated, or an opinion

and, for `attach`, which of the candidate's claims bear on that page, with what
marker, and whether each tests the page's own relationship. With --apply:

    attach  each claim that bears on the page is listed under the page's
            `## Further evidence, not yet read against this model` (a converted page)
            or `### Claims` (any other), its marker capped at what the claim's
            recorded evidence allows (link_pages.strength_cap), with the source and
            the candidate's title beside it. A claim the page already links is skipped.
    design  written as a draft page in designs/, from the candidate's own fields.

and every decision is appended to eval/candidates/decisions.ndjson. `new` and `join`
stay open and are asked again on the next run, when a later batch may have brought
the matching page or the second source.

A cluster (candidates joined to one another) is PROMOTED when it rests on two
independent sources, or on one synthesis: a claim it cites whose evidence entry is a
quant-synthesis or review coded q3 or above. Promotion writes nothing: `--report`
lists the promoted clusters for an agent to write as canonical pages in the
conditional-model format (principle-pattern-authoring.md), and the canonical pages
whose attached claims test their relationship, for an agent to update.

Canonical pages are the principles and patterns the 2026-10-02 triage classed as
canonical (eval/page-triage/triage.tsv), plus every page converted since.

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
import sqlite3
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

Outcomes:
- "attach": the candidate states a canonical page's idea, or a narrower case of it (one setting, population,
  medium or component), so its evidence belongs on that page. Give "n", the page's number in the CANONICAL
  INDEX. Check the whole index, not only the pages shown. Prefer attach whenever a reader of that page should
  see this source.
- "join": no canonical page fits, but an open candidate states the same general idea. Give "n", its letter.
- "new": a general, reusable principle or pattern that no page in the whole CANONICAL INDEX covers, even as a
  broader idea. Name the closest index page in "why" and say what it lacks.
- "design": a specific course, programme, lesson sequence or product for one setting or population.
- "drop": not a page: it restates one empirical finding (that is a claim), or is an aspiration or opinion
  with no actionable design content, or is too vague to act on.

For "attach" only, judge each of the candidate's claims against THAT page: "bears" (is the claim directly
about the page's practice or idea?), "marker" (+ supports the page, ~ depends on conditions, - counts against
it; then S/M/W from the claim's evidence line, e.g. "+W"), and "tests" (does the claim test the page's central
relationship, as opposed to illustrating it?). A null, non-significant or "no difference" result is never "+":
it is "~" (the relationship did not show here) or "-" (it counts against the page).
Reply: {{"outcome": "...", "n": <number or letter or null>, "why": "one sentence",
 "claims": [{{"k": <claim number>, "bears": true, "marker": "+W", "tests": false}}]}}"""


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
    for folder in ("principles", "patterns"):
        for r in search_index.query(db, text, folder=folder, limit=40, mode="OR"):
            key = f"{r[1]}/{r[2]}"
            if key in canon and key != cand.get("page"):
                found.append((r[6], key))
    return [k for _, k in sorted(found, key=lambda x: -x[0])[:k]]


def system_prompt(index: list) -> str:
    """The canonical index, the same in every call so the provider can cache it."""
    return (SYSTEM + "\n\nCANONICAL INDEX (every canonical principle and pattern page):\n"
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
    prompt = PROMPT.format(
        ctype=cand.get("type", "principle"), source=short_source(cand), title=cand.get("title", ""),
        description=(cand.get("description") or "")[:900], extra="\n".join(extra),
        claims="\n".join(f"{i + 1}. {c['title']} [evidence: {c['evidence'] or 'none recorded'}]"
                         for i, c in enumerate(claims)) or "(none)",
        canon="\n".join(f"{pos[r['key']] + 1}. [{r['folder'][:-1]}] {r['title']} — {r['description'][:220]}"
                         for r in canon_recs) or "(none near)",
        open="\n".join(f"{chr(65 + i)}. [{r.get('type')}] {r.get('title')} — {(r.get('description') or '')[:200]}"
                       f" (from {short_source(r)})" for i, r in enumerate(open_rows)) or "(none near)")
    for attempt in range(2):   # one resample: a reply with no JSON in it is a fault, not an answer
        gen = oc.generate(model, system, prompt, api_key, max_tokens=2500)
        try:
            d = extract_json(gen.raw_text)
            break
        except Exception:
            d = None
    if not isinstance(d, dict) or d.get("outcome") not in cl.OUTCOMES:
        return {"id": cand["id"], "outcome": "error", "why": (gen.raw_text or "")[:200],
                "cost_usd": gen.cost_usd}
    out = {"id": cand["id"], "outcome": d["outcome"], "why": d.get("why"), "model": model,
           "cost_usd": gen.cost_usd, "at": date.today().isoformat()}
    n = d.get("n")
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

    index = [rec(k) for k in sorted(canon) if k in pages]
    system = system_prompt(index)

    def one(cand):
        db = sqlite3.connect(search_index.DB_PATH)
        try:
            near = [rec(k) for k in canon_neighbours(db, cand, canon) if k in pages]
            return decide(cand, near, sim.near(cand), api_key, model, index, system)
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


def write_design(cand: dict, actor: str) -> str | None:
    import ingest_extractions as ie
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
    return f"{folder}/{slug}.md"


# ---------------------------------------------------------------- report

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
        synth = any(c["synthesis"] for m in members for c in cited_claims(m))
        out.append({"members": members, "sources": len(sources), "synthesis": synth,
                    "promote": len(sources) >= 2 or synth})
    return sorted(out, key=lambda g: (-g["promote"], -g["sources"]))


def report(cands: dict, decisions: dict) -> None:
    outcome = collections.Counter(d["outcome"] for d in decisions.values())
    print(f"{len(cands)} candidates; {len(cands) - len(decisions)} not yet settled; decisions: {dict(outcome)}")
    groups = clusters(cands, decisions)
    prom = [g for g in groups if g["promote"]]
    print(f"\nopen clusters: {len(groups)}; promoted: {len(prom)}")
    for g in prom:
        why = f"{g['sources']} sources" + (", a synthesis" if g["synthesis"] else "")
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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write attachments and designs, and record decisions")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--backlog", action="store_true", help="dry run over pre-ledger batch pages")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=None, help="decisions file for --backlog")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--by", default="process:settle-candidates")
    args = ap.parse_args()

    if args.report:
        report(cl.load_candidates(), cl.load_decisions())
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
    todo = [c for i, c in cands.items() if decisions.get(i, {}).get("outcome") not in cl.SETTLED]
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
    attached = designs = 0
    for d in decs:
        if d["outcome"] == "attach":
            attached += write_attach(d, cands[d["id"]])
        elif d["outcome"] == "design":
            path = write_design(cands[d["id"]], args.by)
            if path:
                d["page"] = path
                designs += 1
    cl.append_decisions([d for d in decs if d["outcome"] != "error"])
    if designs:
        import subprocess
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "add_type_banner.py"), "--apply"],
                       cwd=WIKI_ROOT, check=False)
    print(f"applied: {attached} claim link(s) attached, {designs} design page(s) written; "
          f"decisions -> {cl.DECISIONS.relative_to(WIKI_ROOT)}")
    report(cands, cl.load_decisions())


if __name__ == "__main__":
    main()
