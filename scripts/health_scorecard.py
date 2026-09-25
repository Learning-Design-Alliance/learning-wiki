#!/usr/bin/env python3
"""
health_scorecard.py — one table of the wiki's health, at several commits, so
the effect of a batch is a measured difference rather than a claim.

    python3 scripts/health_scorecard.py                       # the working tree
    python3 scripts/health_scorecard.py --refs origin/main HEAD --worktree
    python3 scripts/health_scorecard.py --refs A B C --out eval/scorecard.md

Each ref is checked out into a throwaway `git worktree` and measured with the
CURRENT copy of scripts/, not the one committed at that ref. A number that
moves between columns then reflects the wiki changing, never the checker
changing. (Measuring each ref with its own scripts is the other defensible
choice, and it is wrong for a before/after table: a fixed checker would read
as a fixed wiki.)

What it counts is what the repo's own tools already count, gathered in one
place: wiki_health_check.run() for lint, citations, duplicates and drafts;
check_evidence_markers.scan(); observation_lib for study records; the source
manifest; and, per claim page, whether it has any coded evidence and whether
it carries the evidence header line. Nothing here makes a network call, so
DOI resolution is not in the table (wiki_health_check --skip-doi's rule).

Every row says which direction is better. The table never adds rows into one
score: a batch that adds 200 good pages and 30 broken links is two facts, and
a weighted sum would hide whichever one the weights chose.
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = WIKI_ROOT / "scripts"

# (key, label, better): better is "down", "up" or "" (context, not a target).
ROWS = [
    ("pages", "Content pages", ""),
    ("claims", "Claim pages", ""),
    ("lint_total", "Lint issues", "down"),
    ("broken_links", "  broken links", "down"),
    ("dead_anchors", "  dead anchors", "down"),
    ("claims_with_evidence", "Claims with coded evidence", "up"),
    ("claims_without_evidence", "Claims with no coded evidence", "down"),
    ("claims_evidence_pct", "Claims with coded evidence, %", "up"),
    ("claims_missing_header", "Claims missing the evidence header line", "down"),
    ("unmarked_citations", "Claim citations with no [±~][SMW] marker", "down"),
    ("observation_studies", "Structured study records", "up"),
    ("observations", "Observations in those records", "up"),
    ("manifest_ingested", "Sources ingested (manifest)", "up"),
    ("manifest_rejected", "Sources rejected (manifest)", ""),
    ("citation_conflicts", "Citation conflicts (one paper, 2+ DOIs)", "down"),
    ("doi_collisions", "DOI collisions (one DOI, 2+ papers)", "down"),
    ("metadata_conflicts", "Invented journal metadata", "down"),
    ("title_conflicts", "Invented titles", "down"),
    ("title_duplicates", "Near-duplicate titles (same folder)", "down"),
    ("cross_folder_needs_judgment", "Cross-folder slug collisions needing judgment", "down"),
    ("drafts", "Pages at status: draft", ""),
    ("draft_pct", "Pages at status: draft, %", "down"),
    ("todo_pages", "Pages with unfilled TODOs", "down"),
]


def collect() -> dict:
    """Measure the tree this script sits in. Run inside a worktree."""
    sys.path.insert(0, str(SCRIPTS))
    sys.path.insert(0, str(SCRIPTS / "eval"))
    import yaml
    import okf_lib as ok
    import wiki_health_check as whc
    import check_evidence_markers as cem
    import observation_lib as ol

    r = whc.run(skip_doi=True)
    out = {k: r[k] for k in ("citation_conflicts", "doi_collisions", "metadata_conflicts",
                             "title_conflicts", "title_duplicates", "cross_folder_needs_judgment")}
    out["lint_total"] = sum(r["lint"].values())
    out["broken_links"] = r["lint"].get("broken_links", 0)
    out["dead_anchors"] = r["lint"].get("dead_anchors", 0)
    inc = r["incomplete_pages"]
    out["pages"] = sum(v["total"] for v in inc.values())
    out["drafts"] = sum(v["draft"] for v in inc.values())
    out["draft_pct"] = round(100 * out["drafts"] / max(1, out["pages"]), 1)
    out["todo_pages"] = sum(v.get("todo", 0) for v in inc.values())

    with_ev = without_ev = no_header = 0
    for p in sorted((WIKI_ROOT / "claims").glob("*.md")):
        if p.name == "index.md":
            continue
        text = p.read_text(encoding="utf-8")
        m = ok.FRONTMATTER_RE.match(text)
        try:
            fm = (yaml.safe_load(m.group(1)) if m else None) or {}
        except yaml.YAMLError:
            fm = {}
        coded = any(isinstance(s, dict) and s.get("q") not in (None, "", "?")
                    for s in fm.get("sources") or [])
        with_ev += coded
        without_ev += not coded
        no_header += "> **Evidence** ·" not in text
    out["claims"] = with_ev + without_ev
    out["claims_with_evidence"] = with_ev
    out["claims_without_evidence"] = without_ev
    out["claims_evidence_pct"] = round(100 * with_ev / max(1, out["claims"]), 1)
    out["claims_missing_header"] = no_header
    out["unmarked_citations"] = len(cem.scan())

    records, _ = ol.load_all()
    real = {k: v for k, v in records.items() if not k.startswith("example-")}
    out["observation_studies"] = len(real)
    out["observations"] = sum(len((v or {}).get("observations") or []) for v in real.values())

    ing = rej = 0
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        if line.strip():
            status = json.loads(line).get("status")
            ing += status == "ingested"
            rej += status == "rejected"
    out["manifest_ingested"], out["manifest_rejected"] = ing, rej
    return out


def measure_ref(ref: str) -> dict:
    """Check `ref` out into a temporary worktree, put today's scripts in it,
    and run collect() there."""
    tmp = Path(tempfile.mkdtemp(prefix="scorecard-"))
    wt = tmp / "tree"
    subprocess.run(["git", "-C", str(WIKI_ROOT), "worktree", "add", "--detach", "-q", str(wt), ref],
                   check=True)
    try:
        shutil.rmtree(wt / "scripts")
        shutil.copytree(SCRIPTS, wt / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        res = subprocess.run([sys.executable, "-W", "ignore", str(wt / "scripts" / "health_scorecard.py"),
                              "--collect"], capture_output=True, text=True, cwd=wt)
        if res.returncode != 0:
            raise RuntimeError(f"measuring {ref} failed:\n{res.stderr[-2000:]}")
        return json.loads(res.stdout.strip().splitlines()[-1])
    finally:
        subprocess.run(["git", "-C", str(WIKI_ROOT), "worktree", "remove", "--force", str(wt)], check=False)
        shutil.rmtree(tmp, ignore_errors=True)


def _fmt(v) -> str:
    return f"{v:,}" if isinstance(v, int) else f"{v}"


def _delta(a, b, better: str) -> str:
    d = b - a
    if not d:
        return "·"
    sign = f"+{d:,}" if isinstance(d, int) and d > 0 else (f"{d:,}" if isinstance(d, int) else f"{d:+.1f}")
    if not better:
        return sign
    good = (d < 0) == (better == "down")
    return f"{sign} {'✓' if good else '✗'}"


def render(columns: list) -> str:
    """columns: [(label, metrics)]. Deltas are against the previous column."""
    head = "| metric | better |" + "".join(
        f" {lab} |" + (" Δ |" if i else "") for i, (lab, _) in enumerate(columns))
    sep = "|---|---|" + "".join("---:|" + ("---:|" if i else "") for i in range(len(columns)))
    lines = [head, sep]
    for key, label, better in ROWS:
        row = f"| {label} | {'↓' if better == 'down' else '↑' if better == 'up' else ''} |"
        for i, (_, m) in enumerate(columns):
            row += f" {_fmt(m.get(key, '—'))} |"
            if i:
                prev = columns[i - 1][1].get(key)
                row += f" {_delta(prev, m.get(key), better) if prev is not None and m.get(key) is not None else ''} |"
        lines.append(row)
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--collect", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--refs", nargs="*", default=[], help="git refs to measure, oldest first")
    ap.add_argument("--labels", nargs="*", default=None, help="column labels, one per ref (and one for --worktree)")
    ap.add_argument("--worktree", action="store_true", help="also measure the uncommitted working tree, last")
    ap.add_argument("--out", default=None, help="write the table here as well as to stdout")
    args = ap.parse_args()

    if args.collect:
        print(json.dumps(collect()))
        return

    columns = []
    names = list(args.refs) + (["working tree"] if args.worktree or not args.refs else [])
    labels = args.labels or names
    for ref, lab in zip(names, labels):
        print(f"[measuring] {lab} ({ref})", file=sys.stderr)
        columns.append((lab, collect() if ref == "working tree" else measure_ref(ref)))

    shas = []
    for ref in args.refs:
        sha = subprocess.run(["git", "-C", str(WIKI_ROOT), "rev-parse", "--short", ref],
                             capture_output=True, text=True).stdout.strip()
        shas.append(f"`{ref}` = `{sha}`")
    table = render(columns)
    text = ("Measured with today's `scripts/` against each tree (see scripts/health_scorecard.py). "
            "Δ is against the column to its left; ✓/✗ says whether it moved the better way.\n\n"
            + (" · ".join(shas) + "\n\n" if shas else "") + table + "\n")
    print(text)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
