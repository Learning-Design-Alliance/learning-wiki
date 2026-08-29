#!/usr/bin/env bash
# run_full_enrichment.sh — runs enrich.py --provider openrouter across every
# page type (principles, elements, patterns, strategies) with a remaining
# stub/TODO backlog, one type at a time. Each type-level run already
# resumes safely and prints its own wiki-wide health-check summary at the
# end (see enrich.py's _post_batch_checks / wiki_health_check.py).
#
# Two passes per type:
#   1. CSV-driven discovery (enrich.py's default) — matches pages to a CSV
#      row by slug and gives the model that row's real research-brief data
#      in the prompt, so it's used first for the pages it can reach.
#   2. --no-csv discovery — walks the folder on disk directly instead of
#      matching CSV rows by slug. Needed because scraper/ingest_extractions.py
#      pages use the source article's own filename convention (underscores,
#      punctuation preserved), not enrich.py's slugify() — so CSV-row
#      matching structurally can't reach them (confirmed: 0/1569 matched on
#      the strategies backlog). This pass has no CSV context to offer, so
#      it's strictly the fallback sweep, run after pass 1 so any page pass 1
#      already promoted past draft/TODO is correctly skipped here.
#
# Meant to be launched once and left running — across ~1600+ remaining
# strategies pages this can take hours. Background it so it survives an
# SSH disconnect:
#
#   nohup deploy/run_full_enrichment.sh > eval/health/full-enrichment.log 2>&1 &
#   disown
#   tail -f eval/health/full-enrichment.log
#
# Safe to re-run from scratch at any time: enrich.py only processes pages
# still status:draft or still carrying an unfilled <!-- TODO -->, so a
# re-run after a crash or manual interrupt just skips everything already
# done and picks up where it left off — no --overwrite, no bookkeeping.
#
# Override concurrency/provider via env vars if needed, e.g.:
#   ENRICH_CONCURRENCY=5 deploy/run_full_enrichment.sh
set -uo pipefail   # not -e: one type failing shouldn't stop the rest
cd "$(dirname "$0")/.."

CONCURRENCY="${ENRICH_CONCURRENCY:-8}"
PROVIDER="${ENRICH_PROVIDER:-openrouter}"
TYPES=(principles elements patterns strategies)

for t in "${TYPES[@]}"; do
  echo ""
  echo "=================================================================="
  echo "=== enriching type=$t (provider=$PROVIDER, concurrency=$CONCURRENCY) — pass 1/2: CSV-matched ==="
  echo "=================================================================="
  ./venv/bin/python scripts/enrich.py run --type "$t" --provider "$PROVIDER" --concurrency "$CONCURRENCY"
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "=== type=$t pass 1 exited $rc — continuing to pass 2 ==="
  fi

  echo ""
  echo "=================================================================="
  echo "=== enriching type=$t (provider=$PROVIDER, concurrency=$CONCURRENCY) — pass 2/2: --no-csv sweep ==="
  echo "=================================================================="
  ./venv/bin/python scripts/enrich.py run --type "$t" --provider "$PROVIDER" --concurrency "$CONCURRENCY" --no-csv
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "=== type=$t pass 2 exited $rc — continuing to the next type ==="
  fi
done

echo ""
echo "=== full enrichment pass complete across: ${TYPES[*]} ==="
