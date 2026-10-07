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

A cluster is PROMOTED, for an agent to write as a canonical page in the
conditional-model format, once it rests on two independent sources, or on one
synthesis (a meta-analysis or systematic review) coded q3 or above. Nothing here
writes a principle or pattern page.

Two append-only files, committed, so a ledger survives the machine that ran the
batch and the next batch can see what the last one left waiting:

    eval/candidates/candidates.ndjson   one line per candidate, as extracted
    eval/candidates/decisions.ndjson    one line per settling decision; the latest
                                        line for a candidate is its state
"""
import json
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
LEDGER_DIR = WIKI_ROOT / "eval" / "candidates"
CANDIDATES = LEDGER_DIR / "candidates.ndjson"
DECISIONS = LEDGER_DIR / "decisions.ndjson"
CANDIDATE_TYPES = ("principle", "pattern")
OUTCOMES = ("attach", "join", "new", "design", "drop")
# Decisions after which a candidate is settled and never re-asked. `new` and `join`
# stay open: a later batch may bring the canonical page or the second source.
SETTLED = ("attach", "design", "drop")
FIELDS = ("type", "slug", "title", "description", "requirements", "constraints",
          "target_learners", "target_learning_goals", "claims_cited", "related",
          "theory_supporting", "examples", "key_sources", "grain_size")


def candidate_id(article_id: str, ctype: str, slug: str) -> str:
    return f"{article_id}:{ctype}:{slug}"


def _read(path: Path) -> list:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def _append(path: Path, rows: list) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for r in rows:
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
