#!/usr/bin/env python3
"""
recover_corrupted_pages.py — Finds and repairs wiki pages corrupted by the
enrich.py OpenRouter JSON-wrapping bug: GLM occasionally returned a JSON
envelope (`{"answer": "---\\ntype: ..."}`) or a bare JSON object mirroring
the page's own frontmatter keys (`{"type": "strategy", "title": "...", ...}`)
instead of plain markdown, and — before write_enriched_page() gained its
InvalidPageContentError guard — this got written straight to disk with no
validation. A corrupted page's first non-blank line isn't the "---"
frontmatter delimiter every OKF content page (other than index.md/log.md)
requires, which is what this script detects.

For each corrupted page found:
  - If it existed with good (non-corrupted) content at --restore-from
    (default: 2be22874, the last commit before this session's enrichment
    batches began), restore that exact version via `git checkout <commit>
    -- <path>`.
  - Otherwise (created by the scraper pipeline after that commit and
    corrupted on its very first enrichment attempt — no earlier good
    version exists anywhere), reset it to a minimal draft stub
    (frontmatter only, title reconstructed from the filename, matching
    enrich.py's own STUB_TEMPLATES shape) so it re-enters the normal
    enrich.py backlog instead of fabricating content here.

Usage:
    python3 scripts/recover_corrupted_pages.py                  # dry run, report only
    python3 scripts/recover_corrupted_pages.py --apply
    python3 scripts/recover_corrupted_pages.py --apply --restore-from <sha>
"""

import argparse
import subprocess
import sys
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

# Every content folder. Derived rather than repeated: thirteen scripts each
# kept their own copy of this list, which is how learner-variables ended up
# missing from one of them for weeks. See okf_lib.CONTENT_FOLDERS.
PAGE_TYPES = tuple(ok.CONTENT_FOLDERS)
DEFAULT_RESTORE_COMMIT = "2be22874"
TODAY = date.today().isoformat()

TYPE_SINGULAR = {
    "principles": "principle",
    "elements": "element",
    "patterns": "pattern",
    "strategies": "strategy",
    "theories": "theory",
    "claims": "claim",
    "learner-variables": "learner-variable",
}


def _stub(page_type: str, name: str) -> str:
    extra = "id: \nevidence_strength:\n" if page_type == "claim" else ""
    return (
        f"---\ntype: {page_type}\ntitle: {name}\nstatus: draft\n"
        f"generated:\n  by: \"process:corruption-recovery\"\n  at: {TODAY}\n{extra}---\n\n# {name}\n"
    )


def find_corrupted() -> list[Path]:
    """A corrupted page's first non-blank line isn't the frontmatter
    delimiter '---' — the signature of every observed failure mode (raw
    JSON, a JSON-wrapped envelope, a leftover chain-of-thought preamble)."""
    corrupted = []
    for page_type in PAGE_TYPES:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            if not text.lstrip().startswith("---"):
                corrupted.append(path)
    return corrupted


def existed_clean_at(commit: str, relpath: str) -> bool:
    """True if `relpath` existed at `commit` AND that version itself starts
    with '---' — guards against restoring from an already-corrupted commit."""
    result = subprocess.run(
        ["git", "show", f"{commit}:{relpath}"],
        cwd=WIKI_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        return False
    return result.stdout.lstrip().startswith("---")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="Actually fix pages (default: dry-run report only)")
    parser.add_argument("--restore-from", default=DEFAULT_RESTORE_COMMIT,
                         help=f"Commit to restore pre-corruption content from (default: {DEFAULT_RESTORE_COMMIT})")
    args = parser.parse_args()

    # Fail loudly up front if the restore commit isn't reachable from here —
    # rather than silently treating every corrupted page as "needs a stub"
    # (data-losing) just because of a wrong cwd or an unfetched commit.
    check = subprocess.run(["git", "cat-file", "-e", args.restore_from], cwd=WIKI_ROOT, capture_output=True)
    if check.returncode != 0:
        print(f"ERROR: commit '{args.restore_from}' is not reachable from {WIKI_ROOT} — "
              f"nothing changed. Confirm with:\n  git -C {WIKI_ROOT} rev-parse {args.restore_from}")
        sys.exit(1)

    corrupted = find_corrupted()
    if not corrupted:
        print("No corrupted pages found (every page starts with '---').")
        return

    restorable, needs_stub = [], []
    for path in corrupted:
        relpath = str(path.relative_to(WIKI_ROOT))
        if existed_clean_at(args.restore_from, relpath):
            restorable.append(relpath)
        else:
            needs_stub.append(path)

    print(f"{len(corrupted)} corrupted page(s) found: "
          f"{len(restorable)} restorable from {args.restore_from}, "
          f"{len(needs_stub)} need a fresh draft stub (no clean prior version).")

    if not args.apply:
        print("\n-- restorable from git history --")
        for r in restorable:
            print(f"  {r}")
        print("\n-- needs draft-stub reset (never had clean content) --")
        for p in needs_stub:
            print(f"  {p.relative_to(WIKI_ROOT)}")
        print("\nDry run only — re-run with --apply to actually fix these.")
        return

    if restorable:
        subprocess.run(["git", "checkout", args.restore_from, "--", *restorable], cwd=WIKI_ROOT, check=True)
        print(f"Restored {len(restorable)} page(s) from {args.restore_from}.")

    for path in needs_stub:
        page_type = path.parent.name
        singular = TYPE_SINGULAR.get(page_type, page_type.rstrip("s"))
        name = path.stem.replace("-", " ").replace("_", " ").title()
        path.write_text(_stub(singular, name), encoding="utf-8")
    if needs_stub:
        print(f"Reset {len(needs_stub)} page(s) with no clean prior version to a draft stub.")


if __name__ == "__main__":
    main()
