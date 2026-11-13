#!/usr/bin/env python3
"""
graph_search.py — search the wiki as a typed graph, by design variable, for candidate claims.

Some questions are slow to answer by reading pages: which findings for a design variable come
from adults, which are known nulls, where a finding's direction flips with learner expertise
or delay, where one study reports opposite signs on two outcomes, which designs differ by
one element. This loads the edges the wiki already holds in structured form and answers those
questions as lists of candidates. It reads the wiki and writes only its own cache.

**What it returns is a list of candidates to read, not evidence.** Most of the structure it
searches is the coded evidence cells (`eval/runs/evidence-axes/cells/`), and a cell is a label
a language model wrote (`code_evidence_axes.py`): the quote in each cell is checked against the
source text (`quote_ok`), but no human-coded reference sample and no agreement figure exist
for any field. So a cell is used to find and rank claims, never as evidence for one. Read the
claim page, and its source, before relying on a row.

Nodes (id "<kind>/<slug>"):
  pattern, element, design, principle, learner-variable, strategy   from the wiki-index shards
  claim      claim frontmatter: title, per-source q, i, kind, n
  source     one study, keyed by DOI, else by author-year id (so a study split over claims counts once)
  variable   a design variable: evidence-dimensions.json, design-variable D.variable

Edges (each from a structured field, except where marked):
  page -cites-> claim     reverse-index.json, with the citation marker's polarity (+ ~ -) and strength (S M W)
  page -links-> page      reverse-index.json, among pattern, element and design pages
  claim -from-> source    claim frontmatter `sources`
  claim -tests-> variable the coded evidence cells, read only through evidence_cells.py: direction,
                          study design, learner age and expertise, outcome, timing, effect, quote check

Every result row names its basis, so a reader can see what each row rests on:
  basis              cell                 a coded cell matched the variable and direction asked for
                     keyword+marker       no cell for the variable; the title matched VARIABLE_KEYWORDS
                                          and the citing pages' markers (or the title's wording) gave the direction
                     marker               an element, pattern or design page cites the claim [-]
                     keyword+regex        the title matched the variable and MODERATOR_RE (a boundary in prose)
  population_basis   cell | regex         the learner age from the cells, else ADULT_RE/CHILD_RE over the
                                          claim's title, subclaims and `n:` fields
Where a fallback answers, the row says so; a row resting on a keyword or a regex is weaker than
one resting on a cell, which is itself only a model's label.

Ranking: highest q among the claim's sources, whether a design-side page (element, pattern,
design) cites it, the number of distinct studies, the matching cells whose quote was found, and
whether an effect size is printed.

    python3 scripts/graph_search.py build                            # parse and cache (~1 min)
    python3 scripts/graph_search.py evidence --variable spacing --direction + --age adult --min-q 3
    python3 scripts/graph_search.py nulls --variable interleaving
    python3 scripts/graph_search.py boundaries --variable worked-examples
    python3 scripts/graph_search.py crossovers --variable spacing    # opposite signs, one claim or one study
    python3 scripts/graph_search.py paths --page elements/retrieval-practice
    python3 scripts/graph_search.py one-diff                         # designs differing in one element

The cache is `.cache/graph-search/`, ignored, keyed by the commit, and skipped while the inputs
(claims, cells, indexes) have uncommitted changes; `--rebuild` forces a fresh parse. Standard
library only. Tests: `python3 scripts/test_graph_search.py`, on a synthetic wiki.
"""
from __future__ import annotations

import argparse
import collections
import contextlib
import json
import pickle
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import evidence_cells  # noqa: E402
import evidence_dimensions as ed  # noqa: E402
import okf_lib  # noqa: E402

WIKI_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = WIKI_ROOT / ".cache" / "graph-search"
CACHE_VERSION = 1
INPUTS = ["claims", "eval/runs/evidence-axes", "reverse-index.json", "wiki-index"]

PAGE_KINDS = {"patterns": "pattern", "elements": "element", "designs": "design", "principles": "principle",
              "learner-variables": "learner-variable", "strategies": "strategy"}
LINKABLE = ("patterns", "elements", "designs")
DESIGN_SIDE = ("element", "pattern", "design")
EXPERIMENTAL = {"randomized", "controlled-nonrandom", "within-subject", "synthesis-experimental"}

# Title keywords per design variable: the fallback for a claim with no coded cell for it. Keys are
# D.variable values; a variable with no entry has no fallback.
VARIABLE_KEYWORDS = {
    "spacing": r"spac(ed|ing) (practice|repetition|retrieval|study|learning)|distributed practice|massed|cramm|"
               r"lag effect|inter-?study interval|\bISI\b",
    "retrieval-practice": r"retriev|testing effect|practice test|quizz|test-restudy|self-test",
    "interleaving": r"interleav|blocked practice",
    "worked-examples": r"worked[- ]example|example-based|expertise reversal|erroneous example",
    "fading": r"fading|faded|completion problem",
    "example-problem-sequencing": r"example.problem|problem.example",
    "problem-first": r"productive failure|problem[- ]solving (before|first)|before instruction|instruction first",
    "feedback-timing": r"(immediate|delayed) feedback|feedback timing",
    "feedback-presence": r"without (immediate )?feedback|no[- ]feedback|corrective feedback",
    "feedback-type": r"elaborat\w* feedback|explanatory feedback|feedback (type|level)|KR feedback",
    "practice-amount": r"overlearn|extra (massed )?practice|number of (problems|trials|practice)|more practice",
    "mastery-learning": r"mastery|until correct",
    "self-explanation": r"self-explan",
    "test-format": r"multiple-choice|short-answer",
    "case-comparison": r"case comparison|comparing (cases|examples)|contrasting cases",
    "guided-discovery": r"guided discovery|discovery learning|inquiry",
    "explicit-instruction": r"explicit instruction|direct instruction",
    "scaffolding": r"scaffold",
    "praise": r"\bpraise",
    "gamification": r"gamif",
}

ADULT_RE = re.compile(r"\b(undergrad\w*|college|universit\w*|adults?|post-?secondary|graduate students?|"
                      r"residents?|housestaff|interns|nurs\w+ students?|medical students?|trainees?|employees?|"
                      r"MOOC|workers?|professionals?)\b", re.I)
CHILD_RE = re.compile(r"\b(grade\s?\d|\d+(st|nd|rd|th)[- ]grad\w*|first-grade\w*|kindergarten|preschool\w*|"
                      r"children|pupils|elementary|primary school|middle school|high school|secondary school|"
                      r"year \d+ (students|pupils)|adolescen\w*|ninth|seventh|eighth|fourth|fifth|sixth)\b", re.I)
# Moderator wording in a claim title: a boundary condition stated only in prose.
MODERATOR_RE = re.compile(r"\b(only|but not|while|whereas|though|more for|less for|depends?|depending|"
                          r"moderat\w*|interact\w*|revers\w*|for novices|for experts|prior knowledge|expertise|"
                          r"concentrated among|regardless)\b", re.I)
# Null or harm wording in a claim title: the direction fallback when no marker gives one.
NULL_TITLE_RE = re.compile(r"\b(no (significant )?(difference|effect|benefit|advantage)|did not|does not|do not|"
                           r"not (significantly|superior|more effective)|no added|null|neither|failed to|"
                           r"reduces?|lower(s|ed)?|worse|impairs?|harms?|undermines?|negative)\b", re.I)
SOURCES_BLOCK_RE = re.compile(r"^sources:\n((?:[ \t]+[^\n]*(?:\n|\Z))*)", re.M)


# ------------------------------------------------------------------------------------ parsing

def fm_sources(fm: str) -> list[dict]:
    """A claim's `sources:` entries (id, resource, author, q, i, n, kind). A line reader, not a YAML
    parse: 72,000 YAML parses take minutes, and these keys are always flat scalars."""
    m = SOURCES_BLOCK_RE.search(fm + "\n")
    if not m:
        return []
    out, cur = [], None
    for line in m.group(1).splitlines():
        s = re.match(r"^\s+- id:\s*(.*)$", line)
        if s:
            cur = {"id": s.group(1).strip().strip('"')}
            out.append(cur)
            continue
        kv = re.match(r"^\s+(resource|author|q|i|n|kind|rigour):\s*(.*)$", line)
        if kv and cur is not None:
            cur[kv.group(1)] = kv.group(2).strip().strip('"')
    return out


def source_key(src: dict) -> str:
    """One key per study, so a study split across claims, or over two entries, counts once."""
    m = re.search(r"10\.\d{4,9}/[^\s\"'<>)\]]+", src.get("resource", ""))
    if m:
        return "doi:" + m.group(0).lower().rstrip(".")
    return "id:" + re.sub(r"-\d{1,2}$", "", src.get("id", ""))  # 'pyc-2007-2' is 'pyc-2007'


def as_int(x) -> int | None:
    try:
        return int(str(x).strip().strip('"'))
    except (TypeError, ValueError):
        return None


def text_population(texts: list[str]) -> str:
    a = any(ADULT_RE.search(t) for t in texts)
    c = any(CHILD_RE.search(t) for t in texts)
    return "mixed" if a and c else "adult" if a else "child" if c else "?"


def git(root: Path, *args) -> str | None:
    try:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                              check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def page_records(root: Path) -> list[dict]:
    """The page records, from the wiki-index shards (build_wiki_index.SHARD_DIR), as mcp_server.py reads them."""
    return [json.loads(line) for f in sorted((root / "wiki-index").glob("*/*.ndjson"))
            for line in f.read_text(encoding="utf-8").splitlines() if line.strip()]


@contextlib.contextmanager
def cell_store(root: Path):
    """Point evidence_cells at `root`'s store, so a synthetic wiki is read through the same reader."""
    saved = evidence_cells.STORE
    evidence_cells.STORE = root / "eval" / "runs" / "evidence-axes"
    try:
        yield
    finally:
        evidence_cells.STORE = saved


# ------------------------------------------------------------------------------------ the graph

class Graph:
    def __init__(self):
        self.nodes: dict[str, dict] = {}
        self.out: dict[str, list] = collections.defaultdict(list)    # id -> [(rel, dst, attrs)]
        self.inc: dict[str, list] = collections.defaultdict(list)    # id -> [(rel, src, attrs)]
        self.meta: dict = {}

    def add_node(self, nid: str, **attrs):
        self.nodes.setdefault(nid, {}).update(attrs)

    def add_edge(self, src: str, rel: str, dst: str, **attrs):
        self.out[src].append((rel, dst, attrs))
        self.inc[dst].append((rel, src, attrs))

    def edges(self, nid: str, rel: str, incoming: bool = False):
        return [(n, a) for r, n, a in (self.inc if incoming else self.out).get(nid, []) if r == rel]


def load(root: Path = WIKI_ROOT) -> Graph:
    g = Graph()
    g.meta = {"wiki_commit": git(root, "rev-parse", "--short", "HEAD") or "unknown", "cache_version": CACHE_VERSION}
    kinds = set(PAGE_KINDS.values())
    for rec in page_records(root):
        if rec.get("type") in kinds:
            g.add_node(f"{rec['type']}/{rec['id']}", type=rec["type"], title=rec.get("title", ""), path=rec.get("path"))
    for p in (root / "claims").glob("*.md"):
        if p.name == "index.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = okf_lib.FRONTMATTER_RE.match(text)
        fm, body = (m.group(1), text[m.end():]) if m else ("", text)
        srcs = fm_sources(fm)
        title = okf_lib.parse_frontmatter_scalars(fm.splitlines()).get("title", "") if fm else ""
        qs = [q for q in (as_int(s.get("q")) for s in srcs) if q is not None]
        subclaims = " ".join(re.findall(r"^`q\d[^`]*`\s*(.*)$", body, re.M))[:4000]
        nid = f"claim/{p.stem}"
        g.add_node(nid, type="claim", title=title, path=f"claims/{p.name}", max_q=max(qs) if qs else None,
                   has_effect_size=any(as_int(s.get("i")) is not None for s in srcs),
                   text_population=text_population([title, subclaims] + [s.get("n", "") for s in srcs]),
                   title_sign="-/0" if NULL_TITLE_RE.search(title) else "+?",
                   verified=bool(re.search(r"^verified:", fm, re.M)))
        for s in srcs:
            sk = "source/" + source_key(s)
            g.add_node(sk, type="source", author=s.get("author", "")[:80])
            g.add_edge(nid, "from", sk, q=as_int(s.get("q")), i=s.get("i"), kind=s.get("kind"), n=s.get("n", ""))
    # reverse-index.json: {target folder: {target slug: {source folder: [{slug, polarity?, strength?}]}}}
    ri = json.loads((root / "reverse-index.json").read_text(encoding="utf-8"))
    folder_kind = ri.get("kinds", {})
    for slug, by_folder in ri["edges"].get("claims", {}).items():
        for folder, lst in by_folder.items():
            if folder == "claims":
                continue
            for e in lst:
                g.add_edge(f"{folder_kind.get(folder, folder)}/{e['slug']}", "cites", f"claim/{slug}",
                           polarity=e.get("polarity"), strength=e.get("strength"))
    for tfolder in LINKABLE:
        for slug, by_folder in ri["edges"].get(tfolder, {}).items():
            for sfolder in LINKABLE:
                for e in by_folder.get(sfolder, []):
                    src, dst = f"{PAGE_KINDS[sfolder]}/{e['slug']}", f"{PAGE_KINDS[tfolder]}/{slug}"
                    if src != dst:
                        g.add_edge(src, "links", dst)
    n_cells = 0
    with cell_store(root):
        records = evidence_cells.read()
    for r in records:
        cid = f"claim/{r.get('claim')}"
        if cid not in g.nodes:
            continue
        for c in r.get("cells") or []:
            L, D, O, R = (c.get(k) or {} for k in ("L", "D", "O", "result"))
            var = (D.get("variable") or "?").strip()
            g.add_node(f"variable/{var}", type="variable")
            g.add_edge(cid, "tests", f"variable/{var}", direction=(R.get("direction") or "?").strip(),
                       design=R.get("design"), effect=R.get("effect"), age=(L.get("age") or "?").strip(),
                       expertise=(L.get("expertise") or "?").strip(), outcome=O.get("outcome"),
                       timing=O.get("timing"), treatment=D.get("treatment"), comparison=D.get("comparison"),
                       quote_ok=bool(c.get("quote_ok")), entry=r.get("entry"))
            n_cells += 1
    g.meta["cells"] = n_cells
    return g


def cached(root: Path = WIKI_ROOT, cache: Path = CACHE_DIR, rebuild: bool = False) -> Graph:
    """The graph for HEAD, from the cache when the inputs have no uncommitted changes."""
    commit = git(root, "rev-parse", "--short", "HEAD")
    dirty = git(root, "status", "--porcelain", "--", *INPUTS)
    usable = commit and dirty == ""
    f = cache / f"graph-{commit}-v{CACHE_VERSION}.pickle"
    if usable and f.exists() and not rebuild:
        with f.open("rb") as fh:
            return pickle.load(fh)
    g = load(root)
    if usable:
        cache.mkdir(parents=True, exist_ok=True)
        for old in cache.glob("graph-*.pickle"):
            old.unlink()
        with f.open("wb") as fh:
            pickle.dump(g, fh)
    return g


# ------------------------------------------------------------------------------------ per-claim facts

def claim_ids(g: Graph):
    return [nid for nid, n in g.nodes.items() if n.get("type") == "claim"]


def claim_cells(g: Graph, cid: str, variable: str | None = None) -> list[dict]:
    return [dict(a, variable=v.split("/", 1)[1]) for v, a in g.edges(cid, "tests")
            if variable is None or v == f"variable/{variable}"]


def claim_population(g: Graph, cid: str, cells: list[dict] | None = None) -> tuple[str, str]:
    """(age band, basis): the cells' ages where any is coded, else the text regex."""
    cells = cells if cells is not None else claim_cells(g, cid)
    ages = {c["age"] for c in cells if c["age"] not in ("?", "")}
    if ages:
        return ("mixed" if len(ages) > 1 else ages.pop()), "cell"
    return g.nodes[cid].get("text_population", "?"), "regex"


def independent_sources(g: Graph, cid: str) -> int:
    return len({s for s, _ in g.edges(cid, "from")})


def citing_pages(g: Graph, cid: str, kinds=DESIGN_SIDE + ("principle",)) -> list[tuple]:
    return [(p, a.get("polarity"), a.get("strength")) for p, a in g.edges(cid, "cites", incoming=True)
            if p.split("/", 1)[0] in kinds]


def marker_direction(g: Graph, cid: str) -> str:
    """Every polarity the citing pages give the claim, e.g. '+~': one claim is often marked differently."""
    return "".join(sorted({a.get("polarity") for _, a in g.edges(cid, "cites", incoming=True)
                           if a.get("polarity")})) or "?"


def marker_majority(g: Graph, cid: str) -> str:
    """'+', '-', '~' or '?': the polarity most citing pages give (a tie is '~')."""
    c = collections.Counter(a.get("polarity") for _, a in g.edges(cid, "cites", incoming=True) if a.get("polarity"))
    if not c:
        return "?"
    top = c.most_common()
    return "~" if len(top) > 1 and top[0][1] == top[1][1] else top[0][0]


def home_pages(g: Graph, variable: str, k: int = 4) -> set[str]:
    """The element and pattern pages most about a variable: the k whose cited claims carry the most cells
    coded with it, plus pages whose slug matches the variable's keywords. Computed, not hand-listed."""
    key = ("home", variable, k)
    if key not in g.meta:
        score = collections.Counter()
        for nid, n in g.nodes.items():
            if n.get("type") in ("element", "pattern"):
                for cid, _ in g.edges(nid, "cites"):
                    score[nid] += sum(1 for v, _ in g.edges(cid, "tests") if v == f"variable/{variable}")
        homes = {nid for nid, c in score.most_common(k) if c > 0}
        rx = VARIABLE_KEYWORDS.get(variable)
        if rx:
            homes |= {nid for nid, n in g.nodes.items() if n.get("type") in ("element", "pattern")
                      and re.search(rx, nid.split("/", 1)[1].replace("-", " "), re.I)}
        g.meta[key] = homes
    return g.meta[key]


def home_cited(g: Graph, cid: str, variables) -> int:
    if not variables:
        return 0
    homes = set().union(*(home_pages(g, v) for v in variables))
    return int(any(p in homes for p, _ in g.edges(cid, "cites", incoming=True)))


def design_linked(g: Graph, cid: str) -> int:
    return int(bool(citing_pages(g, cid, DESIGN_SIDE)))


def rank_key(g: Graph, cid: str, matched: list[dict]) -> tuple:
    n = g.nodes[cid]
    return (n.get("max_q") or 0, design_linked(g, cid), independent_sources(g, cid),
            sum(c["quote_ok"] for c in matched), int(bool(n.get("has_effect_size"))))


def row(g: Graph, cid: str, matched: list[dict], basis: str, **extra) -> dict:
    n = g.nodes[cid]
    age, pbasis = claim_population(g, cid)
    return dict(claim=cid.split("/", 1)[1], title=n.get("title", "")[:160], basis=basis, max_q=n.get("max_q"),
                sources=independent_sources(g, cid), effect_size_printed=n.get("has_effect_size"),
                population=age, population_basis=pbasis, marker_direction=marker_direction(g, cid),
                cells=[{k: c.get(k) for k in ("variable", "direction", "age", "expertise", "outcome", "timing",
                                              "design", "effect", "quote_ok")} for c in matched][:6],
                cited_by=[f"{p}[{pol or ''}{st or ''}]" for p, pol, st in citing_pages(g, cid)][:6],
                verified=n.get("verified"), **extra)


def keyword_for(variables) -> str | None:
    return "|".join(f"(?:{VARIABLE_KEYWORDS[v]})" for v in variables or [] if v in VARIABLE_KEYWORDS) or None


# ------------------------------------------------------------------------------------ queries

POS, NULLISH = {"+"}, {"ns", "0", "-"}


def q_evidence(g, variables=None, direction="+", min_q=3, age=None, expertise=None, timing=None,
               keyword=None, treatment=None, limit=40, strict_age=False):
    """Claims whose cells test one of `variables` with `direction`, at q >= min_q. A claim with no cell for
    the variable is included when `keyword` matches its title and its markers (or title wording) agree with
    `direction` (basis keyword+marker). `age` ranks matching rows first and unknown or mixed next, dropping
    other bands; `strict_age` keeps only cells coded with that age."""
    keyword = keyword or keyword_for(variables)
    want = POS if direction == "+" else NULLISH if direction in ("0", "null", "-", "ns") else {direction}
    trx = re.compile(treatment, re.I) if treatment else None
    out = []
    for cid in claim_ids(g):
        n = g.nodes[cid]
        if (n.get("max_q") or 0) < min_q:
            continue
        cells = claim_cells(g, cid)
        matched = [c for c in cells if (not variables or c["variable"] in variables) and c["direction"] in want
                   and (not expertise or c["expertise"] == expertise) and (not timing or c["timing"] == timing)
                   and (not trx or trx.search(f"{c.get('treatment')} {c.get('comparison')}"))]
        if age and strict_age:
            matched = [c for c in matched if c["age"] == age or (c["age"] == "?" and n.get("text_population") == age)]
        basis = "cell"
        title = n.get("title", "")
        if not matched:
            if not (keyword and re.search(keyword, title + " " + cid, re.I)) or \
                    any(c["variable"] in (variables or []) for c in cells) or (trx and not trx.search(title)):
                continue
            md = marker_majority(g, cid)
            sign_ok = (md == "+" and n.get("title_sign") != "-/0") if direction == "+" else \
                (md == "-" or n.get("title_sign") == "-/0")
            if not sign_ok:
                continue
            basis = "keyword+marker"
        pop, _ = claim_population(g, cid, cells)
        age_rank = 2 if not age or pop == age else 1 if pop in ("?", "mixed") else 0
        if age and age_rank == 0:
            continue
        out.append(((age_rank, home_cited(g, cid, variables)) + rank_key(g, cid, matched),
                    row(g, cid, matched, basis)))
    out.sort(key=lambda t: t[0], reverse=True)
    return [r for _, r in out[:limit]]


def q_nulls(g, variables=None, min_q=3, age=None, keyword=None, limit=40):
    """Known nulls or harms: cells with direction ns, 0 or - from an experimental design (or a synthesis of
    experiments) whose quote was found in the source; keyword rows whose markers or title say null or harm;
    and claims an element, pattern or design page cites [-]."""
    keyword = keyword or keyword_for(variables)
    rows = q_evidence(g, variables, "null", min_q, age, keyword=keyword, limit=10 ** 9)
    rows = [r for r in rows if r["basis"] != "cell" or
            any(c["quote_ok"] and c.get("design") in EXPERIMENTAL for c in r["cells"])]
    seen = {r["claim"] for r in rows}
    for cid in claim_ids(g):
        slug = cid.split("/", 1)[1]
        if slug in seen or (g.nodes[cid].get("max_q") or 0) < min_q:
            continue
        title_hit = keyword and re.search(keyword, g.nodes[cid].get("title", "") + " " + cid, re.I)
        cell_hit = variables and any(c["variable"] in variables for c in claim_cells(g, cid))
        on_topic = bool(title_hit or cell_hit) if (variables or keyword) else True
        if on_topic and any(pol == "-" for _, pol, _ in citing_pages(g, cid, DESIGN_SIDE)):
            rows.append(row(g, cid, [], "marker"))
    rows.sort(key=lambda r: (home_cited(g, "claim/" + r["claim"], variables), r["max_q"] or 0, r["sources"],
                             len(r["cells"])), reverse=True)
    return rows[:limit]


def q_boundaries(g, variables=None, min_q=3, limit=40, keyword=None):
    """Boundary conditions. within_claim: one claim whose cells for a variable go + at one level of learner
    expertise, age or timing and -/ns at another (a moderator); or + and -/ns split on no coded axis; or, with
    no cell, moderator wording in a title that matches the variable (basis keyword+regex). strata: per
    variable, the direction tally by (age, expertise) over quote-checked cells. pages_for_and_against:
    element and pattern pages citing some claims [+] and others [-]."""
    keyword = keyword or keyword_for(variables)
    within = []
    for cid in claim_ids(g):
        if (g.nodes[cid].get("max_q") or 0) < min_q:
            continue
        by_var = collections.defaultdict(list)
        for c in claim_cells(g, cid):
            if (not variables or c["variable"] in variables) and c["direction"] in ("+", "-", "ns", "0"):
                by_var[c["variable"]].append(c)
        for var, cs in by_var.items():
            for axis in ("expertise", "age", "timing"):
                signs = collections.defaultdict(set)
                for c in cs:
                    if c[axis] not in ("?", None, "mixed"):
                        signs[c[axis]].add("+" if c["direction"] == "+" else "-/ns")
                levels = [lv for lv, s in signs.items() if len(s) == 1]
                if len({next(iter(signs[lv])) for lv in levels}) == 2:
                    within.append(((2, home_cited(g, cid, variables)) + rank_key(g, cid, cs),
                                   row(g, cid, cs, "cell", moderator=axis,
                                       flips={lv: next(iter(signs[lv])) for lv in levels})))
                    break
            else:
                if len({"+" if c["direction"] == "+" else "-/ns" for c in cs}) == 2:
                    within.append(((1, home_cited(g, cid, variables)) + rank_key(g, cid, cs),
                                   row(g, cid, cs, "cell", moderator="not on a coded axis")))
        title = g.nodes[cid].get("title", "")
        if keyword and not by_var and MODERATOR_RE.search(title) and re.search(keyword, title + " " + cid, re.I):
            within.append(((0, home_cited(g, cid, variables)) + rank_key(g, cid, []),
                           row(g, cid, [], "keyword+regex", moderator="title wording")))
    within.sort(key=lambda t: t[0], reverse=True)
    strata = {}
    for var in variables or sorted(ed.values("variable")):
        tally = collections.defaultdict(collections.Counter)
        for cid in claim_ids(g):
            if (g.nodes[cid].get("max_q") or 0) < min_q:
                continue
            for c in claim_cells(g, cid, var):
                if c["quote_ok"] and c["direction"] in ("+", "-", "ns", "0"):
                    tally[(c["age"], c["expertise"])]["+" if c["direction"] == "+" else "-/ns"] += 1
        strata[var] = {f"{a}|{e}": dict(t) for (a, e), t in tally.items() if sum(t.values()) >= 3}
    mixed_pages = []
    for nid, n in g.nodes.items():
        if n.get("type") not in ("element", "pattern"):
            continue
        pols = collections.Counter(a.get("polarity") for _, a in g.edges(nid, "cites"))
        if pols.get("+") and pols.get("-"):
            mixed_pages.append({"page": nid, "for": pols["+"], "mixed": pols.get("~", 0), "against": pols["-"],
                                "basis": "marker"})
    mixed_pages.sort(key=lambda r: r["against"], reverse=True)
    return {"within_claim": [r for _, r in within[:limit]], "strata": strata,
            "pages_for_and_against": mixed_pages[:limit]}


def q_crossovers(g, min_q=3, limit=40, keyword=None, variables=None):
    """Findings that separate explanations. within_claim: one claim whose cells for a variable have opposite
    signs on different outcomes or timings (practice accuracy down, retention up). same_study_pairs: two
    claims from one study with opposite directions, each from its cells, else its markers, else its title
    wording (the pair's basis names which)."""
    keyword = keyword or keyword_for(variables)
    a_rows = []
    for cid in claim_ids(g):
        if (g.nodes[cid].get("max_q") or 0) < min_q:
            continue
        by_var = collections.defaultdict(list)
        for c in claim_cells(g, cid):
            if c["direction"] in ("+", "-") and (not variables or c["variable"] in variables):
                by_var[c["variable"]].append(c)
        for var, cs in by_var.items():
            sig = {(c.get("outcome"), c.get("timing")): c["direction"] for c in cs}
            if len(set(sig.values())) == 2:
                a_rows.append(((home_cited(g, cid, variables),) + rank_key(g, cid, cs),
                               row(g, cid, cs, "cell", crossover={f"{o}|{t}": d for (o, t), d in sig.items()})))
                break
    a_rows.sort(key=lambda t: t[0], reverse=True)

    def sign(cid):
        cs = [c["direction"] for c in claim_cells(g, cid) if c["direction"] in ("+", "-", "ns", "0")]
        if cs:
            return ("+" if all(d == "+" for d in cs) else "-/0" if all(d != "+" for d in cs) else "mixed"), "cell"
        md = marker_direction(g, cid)
        if md in ("+", "-"):
            return ("+" if md == "+" else "-/0"), "marker"
        return g.nodes[cid].get("title_sign"), "regex"

    def on_topic(c):
        if not keyword and not variables:
            return True
        return bool((keyword and re.search(keyword, g.nodes[c].get("title", "") + " " + c, re.I)) or
                    (variables and any(x["variable"] in variables for x in claim_cells(g, c))))

    b_rows = []
    for sid, n in g.nodes.items():
        if n.get("type") != "source":
            continue
        cl = [c for c, _ in g.edges(sid, "from", incoming=True) if (g.nodes[c].get("max_q") or 0) >= min_q]
        if not 2 <= len(cl) <= 12:
            continue
        signed = {c: sign(c) for c in cl}
        pos = [c for c, (s, _) in signed.items() if s in ("+", "+?")]
        neg = [c for c, (s, _) in signed.items() if s == "-/0"]
        for p in pos[:3]:
            for q in neg[:3]:
                b_rows.append({"source": sid, "positive": p.split("/", 1)[1], "negative_or_null": q.split("/", 1)[1],
                               "basis": f"{signed[p][1]}/{signed[q][1]}", "max_q": g.nodes[p].get("max_q"),
                               "on_topic": on_topic(p) and on_topic(q),
                               "design_linked": design_linked(g, p) + design_linked(g, q),
                               "home_cited": home_cited(g, p, variables) + home_cited(g, q, variables),
                               "titles": [g.nodes[p]["title"][:120], g.nodes[q]["title"][:120]]})
    b_rows.sort(key=lambda r: (r["on_topic"], r["home_cited"], r["max_q"] or 0, r["design_linked"],
                               r["basis"] == "cell/cell"), reverse=True)
    return {"within_claim": [r for _, r in a_rows[:limit]], "same_study_pairs": b_rows[:limit]}


def q_paths(g, page: str):
    """A page's cited claims and the design variables their cells code, with the directions."""
    folder, _, slug = page.removesuffix(".md").partition("/")
    nid = f"{PAGE_KINDS.get(folder, folder)}/{slug}"
    var = collections.defaultdict(collections.Counter)
    claims = g.edges(nid, "cites")
    for cid, _ in claims:
        for c in claim_cells(g, cid):
            var[c["variable"]][c["direction"]] += 1
    return {"page": nid, "claims_cited": len(claims),
            "claims_with_cells": sum(1 for cid, _ in claims if claim_cells(g, cid)), "basis": "cell",
            "variables": {v: dict(d) for v, d in sorted(var.items(), key=lambda kv: -sum(kv[1].values()))}}


def q_one_diff(g, limit=40):
    """Pairs of designs whose linked element sets differ by exactly one element."""
    sets = {}
    for nid, n in g.nodes.items():
        if n.get("type") == "design":
            els = frozenset(d for d, _ in g.edges(nid, "links") if d.startswith("element/"))
            if els:
                sets[nid] = els
    out = []
    items = sorted(sets.items())
    for i, (a, ea) in enumerate(items):
        for b, eb in items[i + 1:]:
            if len(ea ^ eb) == 1 and ea & eb:
                out.append({"a": a, "b": b, "shared": sorted(ea & eb), "differs": sorted(ea ^ eb), "basis": "links"})
    return {"designs_with_element_links": len(sets), "pairs": out[:limit]}


# ------------------------------------------------------------------------------------ CLI

def main(argv=None):
    variables = sorted(ed.values("variable"))
    ap = argparse.ArgumentParser(description=__doc__.strip().split("\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rebuild", action="store_true", help="ignore the cache")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build", help="parse and cache; print node and edge counts")

    def common(p, direction=False):
        p.add_argument("--variable", action="append", choices=variables, help="D.variable (repeatable)")
        p.add_argument("--min-q", type=int, default=3)
        p.add_argument("--keyword", help="title regex for claims with no cell (default: the variable's keywords)")
        p.add_argument("--limit", type=int, default=25)
        if direction:
            p.add_argument("--age", choices=sorted(ed.values("age")))
    e = sub.add_parser("evidence", help="claims testing a variable in one direction")
    common(e, True)
    e.add_argument("--direction", default="+", help="+ (default), - , ns, 0, or null for any of -/ns/0")
    e.add_argument("--expertise", choices=sorted(ed.values("expertise")))
    e.add_argument("--timing", choices=sorted(ed.values("timing")))
    e.add_argument("--treatment", help="regex over the cell's treatment and comparison")
    e.add_argument("--strict-age", action="store_true")
    common(sub.add_parser("nulls", help="known nulls and harms"), True)
    common(sub.add_parser("boundaries", help="moderators and flips"))
    common(sub.add_parser("crossovers", help="opposite signs within one claim or one study"))
    p = sub.add_parser("paths", help="a page's cited claims by design variable")
    p.add_argument("--page", required=True, help="e.g. elements/retrieval-practice")
    sub.add_parser("one-diff", help="designs that differ in one linked element")
    a = ap.parse_args(argv)

    g = cached(rebuild=a.rebuild)
    if a.cmd == "build":
        res = {"meta": g.meta, "nodes": dict(collections.Counter(n.get("type") for n in g.nodes.values())),
               "edges": dict(collections.Counter(r for es in g.out.values() for r, _, _ in es)),
               "claims_with_cells": sum(1 for c in claim_ids(g) if g.edges(c, "tests"))}
    elif a.cmd == "evidence":
        res = q_evidence(g, a.variable, a.direction, a.min_q, a.age, a.expertise, a.timing, a.keyword,
                         a.treatment, a.limit, a.strict_age)
    elif a.cmd == "nulls":
        res = q_nulls(g, a.variable, a.min_q, a.age, a.keyword, a.limit)
    elif a.cmd == "boundaries":
        res = q_boundaries(g, a.variable, a.min_q, a.limit, keyword=a.keyword)
    elif a.cmd == "crossovers":
        res = q_crossovers(g, a.min_q, a.limit, keyword=a.keyword, variables=a.variable)
    elif a.cmd == "paths":
        res = q_paths(g, a.page)
    else:
        res = q_one_diff(g)
    print(json.dumps({"wiki_commit": g.meta.get("wiki_commit"),
                      "note": "candidates to read, not evidence: cells are model-coded labels with no human reference",
                      "result": res}, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
