#!/usr/bin/env python3
"""merge_main.py — bring origin/main into the current branch, settling the conflicts that are
not really conflicts.

Every PR here commits the same generated files (the README page-count block, checks.md,
evidence.md, every index.md, reverse-index.json, wiki-index.json, situation-index.json), and
most append to the same append-only logs (sources/manifest.ndjson, the decision ledgers). So
two branches that each add pages conflict on a dozen files even when their content never
touches. On 2026-11-02 seven small ingest PRs from one session (#461-#467) each made the
source-sweep PR conflict this way, and it took a hand merge each time.

What this does, after `git merge --no-commit origin/main`:

- **append-only logs** (APPEND_ONLY): keep every line from both sides (`git merge-file
  --union`). A line either side added is a record somebody wrote; dropping one loses it.
- **generated files** (GENERATED): take either side, then rebuild from the merged tree with
  the repo's own tools. Hand-merging a generated file is how a stale index gets committed.
- **README.md**: merged with its generated page-count block blanked out on all three sides,
  so a person's README edit and a count change cannot collide; the counts are rebuilt.
- **anything else that conflicts**: a real content conflict. The merge is aborted and the
  files listed, exit 2, because picking a side there needs someone who reads both.

Then it regenerates, runs lint, and commits only if lint is 0 (exit 1 and leaves the merge
uncommitted otherwise). Exit 0 with nothing done when main is already merged.

    python3 scripts/merge_main.py            # merge origin/main (fetches it first)
    python3 scripts/merge_main.py --dry-run  # say what would happen; change nothing
    python3 scripts/merge_main.py --no-fetch # use the origin/main already fetched
    python3 scripts/merge_main.py --ref origin/<branch>  # the same, for another ref

The working tree must be clean: a merge on top of a running batch's half-written pages would
commit them. `.gitattributes` marks the same append-only logs `merge=union`, so a plain local
`git merge` keeps both sides of them too; this script is the part that also rebuilds.
"""
from __future__ import annotations

import argparse
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

APPEND_ONLY = [
    "sources/manifest.ndjson",
    "sources/authorities.ndjson",
    "retracted.ndjson",
    "log.md",
    # newest-first dated entries: two PRs that each add one at the top conflict on nothing but
    # position, and keeping both is always right (2026-11-03, #480 and #481)
    "history/agent-log.md",
    "revisions/*.md",
    "eval/load-bearing/reviewed.ndjson",
    "eval/duplicates/*.ndjson",
    "eval/claim-merges/decisions.ndjson",
    "eval/candidates/decisions.ndjson",
    "eval/missing-dois/decisions.ndjson",
    "eval/removed/pages.ndjson",
]
GENERATED = [
    "index.md",
    "*/index.md",
    "checks.md",
    "evidence.md",
    "reverse-index.json",
    "wiki-index.json",
    "situation-index.json",
]
REGENERATE = [
    ["scripts/build_indexes.py"],
    ["scripts/build_evidence_report.py"],
    ["scripts/build_check_report.py"],
]
# Lines on a content page that a script writes from the rest of the page: the evidence and
# currency header lines (add_evidence_summary/_profile, add_currency) and the `generated:`
# stamp. Two branches that each add a claim to one page both rewrite them, and nothing else
# on the page need overlap. Blanked on all three sides before merging; rebuilt afterwards.
HEADER_LINE = re.compile(r"^(> \*\*(?:Evidence|Currency)\*\* · .*|  (?:by|at): .*)$", re.M)
HEADER_REGENERATE = [
    ["scripts/add_evidence_summary.py", "--apply"],
    ["scripts/add_evidence_profile.py", "--apply"],
    ["scripts/add_currency.py", "--apply"],
]
README_BLOCK = re.compile(r"(<!-- page-counts:start[^\n]*-->).*?(<!-- page-counts:end -->)", re.S)


def git(*args: str, check: bool = True, text_input: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          check=check, input=text_input)


def matches(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


def stage(path: str, n: int) -> str:
    r = git("show", f":{n}:{path}", check=False)
    return r.stdout if r.returncode == 0 else ""


def union(path: str) -> None:
    base, ours, theirs = (ROOT / f".merge_main.{k}" for k in ("base", "ours", "theirs"))
    try:
        for f, n in ((base, 1), (ours, 2), (theirs, 3)):
            f.write_text(stage(path, n))
        git("merge-file", "--union", str(ours), str(base), str(theirs), check=False)
        (ROOT / path).write_text(ours.read_text())
    finally:
        for f in (base, ours, theirs):
            f.unlink(missing_ok=True)
    git("add", "--", path)


def merge_readme() -> bool:
    """Merge README.md with the generated count block blanked on every side. False when the
    rest of the README genuinely conflicts."""
    blank = lambda s: README_BLOCK.sub(r"\1\n\2", s)
    files = {}
    for k, n in (("base", 1), ("ours", 2), ("theirs", 3)):
        files[k] = ROOT / f".merge_main.readme.{k}"
        files[k].write_text(blank(stage("README.md", n)))
    try:
        r = git("merge-file", str(files["ours"]), str(files["base"]), str(files["theirs"]), check=False)
        if r.returncode != 0:
            return False
        (ROOT / "README.md").write_text(files["ours"].read_text())
    finally:
        for f in files.values():
            f.unlink(missing_ok=True)
    git("add", "--", "README.md")
    return True


def merge_headers(path: str) -> bool:
    """Merge a content page with its generated header lines blanked on every side. False when
    anything else on the page conflicts. The blanked lines come back from whichever side was
    generated later; the header scripts then rebuild the evidence and currency lines."""
    if not path.endswith(".md") or "/" not in path:
        return False
    texts = {k: stage(path, n) for k, n in (("base", 1), ("ours", 2), ("theirs", 3))}
    blank = lambda s: HEADER_LINE.sub(lambda m: m.group(0).split(" · ")[0].split(":")[0] + " @@merge_main:regenerated@@", s)
    files = {k: ROOT / f".merge_main.hdr.{k}" for k in texts}
    try:
        for k, t in texts.items():
            files[k].write_text(blank(t))
        r = git("merge-file", str(files["ours"]), str(files["base"]), str(files["theirs"]), check=False)
        if r.returncode != 0:
            return False
        merged = files["ours"].read_text()
    finally:
        for f in files.values():
            f.unlink(missing_ok=True)
    at = lambda t: (re.search(r"^  at: (.*)$", t, re.M) or [None, ""])[1]
    donor = texts["theirs"] if at(texts["theirs"]) >= at(texts["ours"]) else texts["ours"]
    values = {m.group(0).split(" · ")[0].split(":")[0]: m.group(0) for m in HEADER_LINE.finditer(donor)}
    for k, t in texts.items():   # a line only one side has
        for m in HEADER_LINE.finditer(t):
            values.setdefault(m.group(0).split(" · ")[0].split(":")[0], m.group(0))
    out = re.sub(r"^(.*) @@merge_main:regenerated@@$", lambda m: values.get(m.group(1), m.group(0)), merged, flags=re.M)
    if "@@merge_main:regenerated@@" in out:
        return False
    (ROOT / path).write_text(out)
    git("add", "--", path)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--ref", default="origin/main", help="what to merge (default origin/main)")
    a = ap.parse_args()

    if not a.no_fetch:
        if a.ref.startswith("origin/"):
            git("fetch", "-q", "origin", a.ref[len("origin/"):])
    if git("merge-base", "--is-ancestor", a.ref, "HEAD", check=False).returncode == 0:
        print(f"{a.ref} is already merged; nothing to do")
        return 0
    behind = git("rev-list", "--count", f"HEAD..{a.ref}").stdout.strip()
    if git("status", "--porcelain").stdout.strip():
        print("working tree is not clean; refusing to merge over uncommitted work", file=sys.stderr)
        return 2

    if a.dry_run:
        r = git("merge-tree", "--write-tree", "--name-only", "HEAD", a.ref, check=False)
        lines = r.stdout.splitlines()
        conflicted = []
        for line in lines[1:]:
            if not line.strip():
                break
            conflicted.append(line.strip())
        real = [p for p in conflicted if not (matches(p, APPEND_ONLY) or matches(p, GENERATED) or p == "README.md")]
        print(f"{behind} commit(s) behind {a.ref}; {len(conflicted)} conflicting file(s): "
              f"{len(conflicted) - len(real)} settle automatically, {len(real)} need a person")
        for p in real:
            print(f"  needs a person: {p}")
        return 2 if real else 0

    git("merge", "--no-commit", "--no-ff", a.ref, check=False)
    conflicted = [p for p in git("diff", "--name-only", "--diff-filter=U").stdout.splitlines() if p]
    real, settled, headers = [], [], False
    for p in conflicted:
        if matches(p, APPEND_ONLY):
            union(p); settled.append(f"{p} (both sides kept)")
        elif matches(p, GENERATED):
            git("checkout", "--ours", "--", p); git("add", "--", p); settled.append(f"{p} (rebuilt)")
        elif p == "README.md" and merge_readme():
            settled.append("README.md (count block rebuilt)")
        elif merge_headers(p):
            headers = True; settled.append(f"{p} (header lines rebuilt)")
        else:
            real.append(p)
    if real:
        git("merge", "--abort", check=False)
        print("real content conflicts; merge aborted, nothing changed:", file=sys.stderr)
        for p in real:
            print(f"  {p}", file=sys.stderr)
        return 2

    for cmd in (HEADER_REGENERATE if headers else []) + REGENERATE:
        r = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            print(f"{' '.join(cmd)} failed; merge left uncommitted:\n{r.stderr[-2000:]}", file=sys.stderr)
            return 1
    lint = subprocess.run([sys.executable, "scripts/lint.py"], cwd=ROOT, capture_output=True, text=True)
    tail = (lint.stdout.strip().splitlines() or [""])[-1]
    if "Total issues: 0" not in tail:
        print(f"lint is not 0 after the merge ({tail}); merge left uncommitted for a look", file=sys.stderr)
        return 1
    git("add", "-A")
    msg = (f"Merge {a.ref} ({behind} commit(s)) with scripts/merge_main.py\n\n"
           + ("Settled automatically:\n" + "\n".join(f"- {s}" for s in settled) + "\n\n" if settled else "")
           + "Generated files rebuilt on the merged tree; lint 0.\n")
    git("commit", "-q", "-F", "-", text_input=msg)
    print(f"merged {behind} commit(s) from {a.ref}; {len(settled)} conflict(s) settled; lint 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
