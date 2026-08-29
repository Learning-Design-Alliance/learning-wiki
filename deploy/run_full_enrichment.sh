#!/usr/bin/env bash
# run_full_enrichment.sh — runs enrich.py --provider openrouter across every
# CSV-backed page type (principles, elements, patterns, strategies) with a
# remaining stub/TODO backlog, one type at a time. Each type-level run
# already resumes safely and prints its own wiki-wide health-check summary
# at the end (see enrich.py's _post_batch_checks / wiki_health_check.py).
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
  echo "=== enriching type=$t (provider=$PROVIDER, concurrency=$CONCURRENCY) ==="
  echo "=================================================================="
  ./venv/bin/python scripts/enrich.py run --type "$t" --provider "$PROVIDER" --concurrency "$CONCURRENCY"
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "=== type=$t exited $rc — continuing to the next type ==="
  fi
done

echo ""
echo "=== full enrichment pass complete across: ${TYPES[*]} ==="
