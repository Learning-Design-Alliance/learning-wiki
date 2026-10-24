#!/usr/bin/env python3
"""
evidence_cells.py — the store of coded evidence cells, one shard per claim-slug prefix.

A run lives in eval/runs/evidence-axes/<run>/, one NDJSON file per first two characters
of the claim slug (cells/co.ndjson holds every claim starting "co"). It was one file,
cells.ndjson, until 2026-10-24, when it reached 53 MB against GitHub's 100 MB limit and
grew by about 0.15 MB a batch. Shards rather than gzip: a compressed file is a new
binary blob on every batch (git cannot delta it, so history grows by the whole file each
time) and cannot be grepped or diffed; plain shards keep both, and a batch touches only
the shards of the claims it coded. A claim's records are always in one known file:

    grep '"claim": "spaced-practice' eval/runs/evidence-axes/cells/sp.ndjson

The largest shard was 2.4 MB at the split, so the layout has room for about forty times
the current corpus. Readers go through read(); a legacy single-file <run>.ndjson is still
read, so an uncommitted or older run keeps working, and write() retires it.

    python3 scripts/evidence_cells.py --migrate [--run cells]   # split a single-file run
    python3 scripts/evidence_cells.py --stats [--run cells]
"""
import argparse
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
STORE = WIKI_ROOT / "eval" / "runs" / "evidence-axes"


def shard(claim: str) -> str:
    """The shard a claim's records live in: its slug's first two characters."""
    return re.sub(r"[^a-z0-9-]", "_", (claim or "_").lower()[:2]).ljust(2, "_")


def run_dir(run: str = "cells") -> Path:
    return STORE / run


def legacy_file(run: str = "cells") -> Path:
    return STORE / f"{run}.ndjson"


def exists(run: str = "cells") -> bool:
    d = run_dir(run)
    return legacy_file(run).exists() or (d.is_dir() and any(d.glob("*.ndjson")))


def _lines(path: Path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            yield json.loads(line)


def read(run: str = "cells") -> list:
    """Every record in the run: the legacy single file first, then the shards in name order."""
    recs = []
    if legacy_file(run).exists():
        recs.extend(_lines(legacy_file(run)))
    d = run_dir(run)
    if d.is_dir():
        for p in sorted(d.glob("*.ndjson")):
            recs.extend(_lines(p))
    return recs


def keys(run: str = "cells") -> set:
    return {r["key"] for r in read(run)}


def append(run: str, rec: dict) -> None:
    """Add one record to its claim's shard."""
    d = run_dir(run)
    d.mkdir(parents=True, exist_ok=True)
    with open(d / f"{shard(rec['claim'])}.ndjson", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def write(run: str, recs: list) -> None:
    """Replace the run with these records, keeping their order within each shard. Shards
    left empty are removed, and so is a legacy single file, whose records are now here."""
    groups = {}
    for r in recs:
        groups.setdefault(shard(r["claim"]), []).append(r)
    d = run_dir(run)
    d.mkdir(parents=True, exist_ok=True)
    for name, rs in groups.items():
        (d / f"{name}.ndjson").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rs),
                                          encoding="utf-8")
    for p in d.glob("*.ndjson"):
        if p.stem not in groups:
            p.unlink()
    if legacy_file(run).exists():
        legacy_file(run).unlink()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="cells")
    ap.add_argument("--migrate", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if a.migrate:
        recs = read(a.run)
        before = sorted(json.dumps(r, sort_keys=True) for r in recs)
        write(a.run, recs)
        after = sorted(json.dumps(r, sort_keys=True) for r in read(a.run))
        if before != after:
            sys.exit("migration changed the records; nothing should differ")
        print(f"{len(recs)} records in {len(list(run_dir(a.run).glob('*.ndjson')))} shards under {run_dir(a.run)}")
    if a.stats or not a.migrate:
        sizes = sorted(((p.stat().st_size, p.name) for p in run_dir(a.run).glob("*.ndjson")), reverse=True)
        total = sum(s for s, _ in sizes)
        print(f"{len(sizes)} shards, {total / 1e6:.1f} MB; largest: "
              + ", ".join(f"{n} {s / 1e6:.2f} MB" for s, n in sizes[:5]))


if __name__ == "__main__":
    main()
