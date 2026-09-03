#!/usr/bin/env python3
"""
log_source_review.py — Append one entry to sources/manifest.ndjson recording
that a source article was reviewed by the ingest pipeline (ingested or
rejected). Thin CLI wrapper around okf_lib.append_manifest_entry, for use by
the /ingest-article skill's manual flow (scripts/ingest_extractions.py calls
the library function directly instead).

Usage:
    python3 scripts/log_source_review.py \
        --id doi:10.1234/example --title "Some Paper Title" \
        --status ingested --pages claims/foo.md elements/bar.md

    python3 scripts/log_source_review.py \
        --id doi:10.1234/other --title "Some Other Paper" \
        --status rejected --reason "out of scope: not learning-science"
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok


def main():
    parser = argparse.ArgumentParser(description="Log a source review to sources/manifest.ndjson")
    parser.add_argument("--id", required=True, help='Source identifier, e.g. "doi:10.1234/x" or "eric-ed123456"')
    parser.add_argument("--title", required=True, help="Source title")
    parser.add_argument("--doi", default=None, help="DOI, if separate from --id")
    parser.add_argument("--status", required=True, choices=["ingested", "rejected"])
    parser.add_argument("--reason", default=None, help="Required if --status rejected")
    parser.add_argument("--pages", nargs="*", default=None, help="Bundle-relative page paths, required if --status ingested")
    # okf_lib.append_manifest_entry has taken `citations` since Gate 3 landed, but
    # this wrapper never exposed it — so every manually ingested source wrote a
    # bare "ingested", which CLAUDE.md is explicit must not be read as "the
    # citations were checked". The automated path (ingest_extractions.py) calls
    # the library directly and was unaffected, which is why the gap survived.
    parser.add_argument("--citations", default=None, metavar="JSON",
                        help='What the citation gate found, as a JSON object: '
                             '\'{"checked": 6, "crossref_reachable": true, "removed": [], '
                             '"flagged": ["..."]}\'. Omit only when no gate was run — '
                             'and prefer "crossref_reachable": false, which records that '
                             'the lookup could not run, over saying nothing.')
    args = parser.parse_args()

    citations = json.loads(args.citations) if args.citations else None
    if citations is not None and args.status != "ingested":
        parser.error("--citations only applies to --status ingested")

    ok.append_manifest_entry(
        source_id=args.id,
        title=args.title,
        status=args.status,
        doi=args.doi,
        reason=args.reason,
        pages=args.pages,
        citations=citations,
    )
    print(f"Logged {args.status}: {args.id} -> sources/manifest.ndjson")


if __name__ == "__main__":
    main()
