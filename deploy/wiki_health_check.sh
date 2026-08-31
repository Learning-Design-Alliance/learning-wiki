#!/usr/bin/env bash
# wiki_health_check.sh — systemd ExecStart target for the nightly wiki
# health check timer. Runs the full check (including DOI resolution
# against Crossref — cached, so this is cheap after the first run) so
# drift gets caught even when the scraper isn't actively running new
# batches, and writes a dated report + appends to eval/health/history.ndjson.
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p eval/health
REPORT_PATH="eval/health/report-$(date -u +%Y%m%dT%H%M%SZ).md"

# wiki_health_check.py exits non-zero whenever it FOUND issues to report —
# the expected, normal state for a nightly monitoring job, not a crash.
# Don't let that mark this systemd unit "failed" every single night; a
# genuine crash still appears in `journalctl -u wiki-health-check` since
# output isn't suppressed, only the exit code is normalized. (Not `exec`,
# since something needs to run after it — the || true.)
./venv/bin/python -u scripts/wiki_health_check.py --out "$REPORT_PATH" || true
