"""
candidates_lib.py — the principle and pattern candidate ledger.

Until 2026-10-07 every extraction wrote its principles and patterns straight into
`principles/` and `patterns/`, one page per article, named in that article's words.
Batches wrote 430 principles and 232 patterns that way, and the conversion waves
spent most of their effort folding them back into the canonical pages they
restated. A principle stated by one essay is not a page; it is a proposal.

So ingest now appends each principle or pattern contribution here, and
`settle_candidates.py` decides what it becomes:

    attach   it is a canonical page's idea, or a narrower case of it: its claims go
             onto that page as further evidence, and no page is written
    join     it is the same idea as another open candidate: the two form a cluster
    new      a general idea no canonical page or open candidate covers: it waits
    design   a design for one setting (the settled rule: never a pattern)
    drop     too thin to be a page: it restates one finding, or is an opinion
    product  a named product or programme others adopt (software, curriculum, assessment
             or instrument, dataset, branded programme or initiative), or one such
             programme's own framework, indicator or theory of change: written to or
             added to that product's page in products/ (maintainer, 2026-10-10)
    research-method  a method for studying learning or evaluating education that is
             specific to education or especially useful in it: a page in
             research-methods/. A general social-science method is a drop.
    artifact the outcome before products/ existed (2026-10-09); no longer given, and
             not settled, so those candidates are asked again
    promoted written (or converted) as a canonical page by an agent; settled

Elements and theories joined the ledger on 2026-10-09: batches were writing about 0.7
element and 0.4 theory pages an article, one page per source, mostly a product,
programme or one paper's framework ("REACH teacher evaluation system", "Chicago's
three-pronged theory of change"). Links the same article's claims and strategies make
to such a candidate are kept by ingest and resolved by settle: to the canonical page
it attaches to, to the design page it becomes, or unlinked.

A candidate may also be an existing page (`origin: page`, id `page:<kind>/<slug>`): the
batch-written principles and patterns from before the ledger that were not folded into a
canonical page (backlog-folds.ndjson records each fold and each refusal). They wait like any
`new` candidate, so a later batch's candidate can join them.

A cluster is PROMOTED, for an agent to write as a canonical page in the
conditional-model format, once it rests on two independent sources (no shared author and
not the same publishing organisation: settle_candidates.independent), or on one
synthesis (a meta-analysis or systematic review) coded q3 or above. Nothing here
writes a principle or pattern page.

Two append-only ledgers, committed, so a ledger survives the machine that ran the
batch and the next batch can see what the last one left waiting:

    eval/candidates/candidates/<xx>.ndjson   one line per candidate, as extracted
    eval/candidates/decisions/<xx>.ndjson    one line per settling decision; the latest
                                             line for a candidate is its state

Each is sharded by the first two characters of the candidate's slug (shard_key), the
rule the evidence cells use (2026-10-24). Until 2026-11-07 each was one file, and at
about 1 MB a batch candidates.ndjson had reached 50 MB against GitHub's 100 MB limit.
Every line for one candidate lands in one shard in the order written, so "first line
wins" (load_candidates) and "latest line wins" (load_decisions) mean what they did.
Read and write them only through this module.
"""
import json
import re
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
LEDGER_DIR = WIKI_ROOT / "eval" / "candidates"
CANDIDATES = LEDGER_DIR / "candidates"   # a directory of shards, <xx>.ndjson
DECISIONS = LEDGER_DIR / "decisions"
CANDIDATE_TYPES = ("principle", "pattern", "element", "theory")
OUTCOMES = ("attach", "join", "new", "design", "product", "research-method", "artifact", "drop", "promoted")
# Decisions after which a candidate is settled and never re-asked. `new` and `join`
# stay open: a later batch may bring the canonical page or the second source.
SETTLED = ("attach", "design", "product", "research-method", "drop", "promoted")
FIELDS = ("type", "slug", "title", "description", "requirements", "constraints",
          "target_learners", "target_learning_goals", "claims_cited", "related",
          "theory_supporting", "examples", "key_sources", "grain_size",
          # elements and theories
          "affordances", "context", "target_learning_objectives", "implications")


def candidate_id(article_id: str, ctype: str, slug: str) -> str:
    return f"{article_id}:{ctype}:{slug}"


def shard_key(cid: str) -> str:
    """The shard a candidate's lines live in: the first two characters of its slug
    (the part after the last ':'), lower-cased, anything outside [a-z0-9] as '_'."""
    head = re.sub(r"[^a-z0-9]", "_", cid.rsplit(":", 1)[-1][:2].lower())
    return head.ljust(2, "_")


def _read(ledger: Path) -> list:
    """Every line of a sharded ledger. Shards are read in name order; within one, in the
    order written, which is the only order the loaders rely on (one candidate, one shard)."""
    if not ledger.is_dir():
        return []
    rows = []
    for shard in sorted(ledger.glob("*.ndjson")):
        rows += [json.loads(l) for l in shard.read_text(encoding="utf-8").splitlines() if l.strip()]
    return rows


def _append(ledger: Path, rows: list) -> None:
    if not rows:
        return
    by_shard = {}
    for r in rows:
        by_shard.setdefault(shard_key(r["id"]), []).append(r)
    ledger.mkdir(parents=True, exist_ok=True)
    for key, group in sorted(by_shard.items()):
        with (ledger / f"{key}.ndjson").open("a", encoding="utf-8") as fh:
            for r in group:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def load_candidates() -> dict:
    """id -> candidate. A candidate written twice (a re-run of one batch) keeps its first line."""
    out = {}
    for r in _read(CANDIDATES):
        out.setdefault(r["id"], r)
    return out


def load_decisions() -> dict:
    """id -> its latest decision."""
    out = {}
    for r in _read(DECISIONS):
        out[r["id"]] = r
    return out


def from_contribution(contrib: dict, record: dict, run_id: str) -> dict:
    article_id = record["article_id"]
    citation = ((record.get("parsed") or {}).get("article") or {}).get("citation")
    row = {"id": candidate_id(article_id, contrib["type"], contrib["slug"]),
           "article_id": article_id, "article_title": record.get("article_title", ""),
           "citation": citation, "run_id": run_id, "origin": "extraction",
           "added_at": date.today().isoformat()}
    for f in FIELDS:
        if contrib.get(f) not in (None, "", []):
            row[f] = contrib[f]
    return row


def append_candidates(rows: list) -> list:
    """Append rows not already in the ledger; returns the ids appended."""
    have = load_candidates()
    new = [r for r in rows if r["id"] not in have]
    _append(CANDIDATES, new)
    return [r["id"] for r in new]


def append_decisions(rows: list) -> None:
    _append(DECISIONS, rows)
