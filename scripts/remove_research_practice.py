#!/usr/bin/env python3
"""Remove the claims both sort models file as research practice (maintainer rule, 2026-10-16).

The same removal the check-in did by hand at every triage hold (2026-10-30 to 31: 224, 62 and 53
claims in three batches), run by the batch itself right after the sort, before the steps that
link, code and judge each claim spend time and money on claims about to go. The rule is
unchanged: a claim goes only when both sort models agree (a disputed sort has category null in
eval/claim-sort/sort.ndjson and stays). remove_pages.py does the removal and repairs the pages
that linked to it; links in log.md to a removed claim become plain text "title (removed DATE)",
as the triage did.

  python3 scripts/remove_research_practice.py            # list what would go
  python3 scripts/remove_research_practice.py --apply
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SORT = ROOT / "eval" / "claim-sort" / "sort.ndjson"
REASON = "research-practice claim, both sort models agree (maintainer rule 2026-10-16)"


def agreed() -> list[str]:
    """Live claims whose settled category is research-practice (the last record per claim wins)."""
    settled = {}
    if SORT.exists():
        for line in SORT.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                settled[r["claim"]] = r.get("category")
    return sorted(c for c, cat in settled.items()
                  if cat == "research-practice" and (ROOT / "claims" / f"{c}.md").exists())


def plain_log_links(slugs: set, date: str) -> int:
    p = ROOT / "log.md"
    if not p.exists():
        return 0
    n = 0

    def sub(m):
        nonlocal n
        if m.group(2) in slugs and not (ROOT / "claims" / f"{m.group(2)}.md").exists():
            n += 1
            return f"{m.group(1)} (removed {date})"
        return m.group(0)

    s = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"\[([^\]]+)\]\(claims/([^)\s]+)\.md\)", sub, s), encoding="utf-8")
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    slugs = agreed()
    print(f"{len(slugs)} claim(s) both sort models file as research practice")
    if not slugs or not args.apply:
        for s in slugs[:20]:
            print(f"  {s}")
        return
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write("".join(f"claims/{s}.md\n" for s in slugs))
        lst = f.name
    rc = subprocess.run([sys.executable, str(ROOT / "scripts" / "remove_pages.py"), "--list", lst,
                         "--reason", REASON, "--log", str(ROOT / "eval" / "removed" / "pages.ndjson"),
                         "--apply"], cwd=ROOT).returncode
    Path(lst).unlink(missing_ok=True)
    if rc:
        sys.exit(rc)
    n = plain_log_links(set(slugs), dt.date.today().isoformat())
    print(f"log.md links made plain: {n}")


if __name__ == "__main__":
    main()
