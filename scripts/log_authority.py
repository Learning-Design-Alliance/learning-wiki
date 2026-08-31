#!/usr/bin/env python3
"""
log_authority.py — record one human-verified citation authority.

This is the command a person runs after checking a source against the
publisher, the book, or the article itself. See authorities.py for why the
file exists and why an agent must not write to it.

    # A book. No DOI is registered for it, and saying so is a verdict:
    # any DOI a later batch invents for ambrose-2010 is then provably wrong.
    python3 scripts/log_authority.py --key ambrose-2010 --by human:david \
      --title "How Learning Works: Seven Research-Based Principles for Smart Teaching" \
      --authors "Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., & Norman, M. K." \
      --publisher "Jossey-Bass" --isbn 978-0-470-61760-1 \
      --url https://www.wiley.com/en-be/shop/general-introductory-education/how-learning-works-seven-research-based-principles-for-smart-teaching-p-9780470617601 \
      --no-doi --note "Book; no DOI is registered for it."

    # An article whose DOI you confirmed at the publisher.
    python3 scripts/log_authority.py --key rosenshine-2012 --by human:david \
      --title "Principles of Instruction: Research-Based Strategies That All Teachers Should Know" \
      --journal "American Educator" --no-doi \
      --note "American Educator 36(1) 12-19, 39. AFT does not register DOIs; the four
              10.1080/00098655.2012.* spellings in the wiki are all invented."

--no-doi and --doi are deliberately separate flags, and neither is the
default: omitting both records "not established", which is a different and
weaker statement than "established that none exists". Nothing downstream may
act on the first and everything may act on the second.
"""

import argparse
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import authorities as au


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", required=True,
                    help="author-year key, e.g. ambrose-2010 (as check_citations.py forms it)")
    ap.add_argument("--by", required=True,
                    help="who verified it — must be human:<id>; an agent may not author one")
    ap.add_argument("--at", default=dt.date.today().isoformat(), help="ISO date (default: today)")
    ap.add_argument("--title")
    ap.add_argument("--authors")
    ap.add_argument("--year")
    ap.add_argument("--journal")
    ap.add_argument("--publisher")
    ap.add_argument("--isbn", action="append", metavar="ISBN",
                    help="checked against its ISBN-10/13 checksum before it is written. "
                         "Repeatable — a book has one per format, and they are not "
                         "alternatives: a page may cite any of them")
    ap.add_argument("--url")
    ap.add_argument("--note")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--doi", help="the DOI you confirmed at the publisher")
    g.add_argument("--no-doi", action="store_true",
                   help="record that NO DOI exists for this source — a verdict, so any DOI "
                        "asserted for this key afterwards is provably invented")
    args = ap.parse_args()

    entry = {"key": args.key, "verified": {"by": args.by, "at": args.at}}
    for f in ("title", "authors", "year", "journal", "publisher", "url", "note"):
        if getattr(args, f):
            entry[f] = getattr(args, f)
    if args.isbn:
        # One stays a plain string so the common case reads naturally in the
        # file; several become a list. Both shapes are read by isbns_of().
        entry["isbn"] = args.isbn[0] if len(args.isbn) == 1 else args.isbn
    if args.no_doi:
        entry["doi"] = None
    elif args.doi:
        entry["doi"] = args.doi

    problems = au.validate_entry(entry)
    if problems:
        print("Refusing to write this entry:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    existing = au.load_authorities().get(args.key)
    au.append_authority(entry)
    if existing:
        print(f"Appended a correction for {args.key} (the previous line is kept — the file "
              f"is append-only, so what was believed and when stays readable).")
    else:
        print(f"Recorded {args.key} in {au.AUTHORITIES_PATH.relative_to(au.WIKI_ROOT)}.")
    print("\nNext: python3 scripts/apply_authorities.py --check   (then --apply)")


if __name__ == "__main__":
    main()
