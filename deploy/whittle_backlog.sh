#!/usr/bin/env bash
# whittle_backlog.sh — repeatedly runs run_full_enrichment.sh until the
# wiki's draft/TODO backlog stops shrinking (convergence) or MAX_ROUNDS is
# hit. A single run_full_enrichment.sh pass never reaches zero on its own:
# each freshly-enriched page can cross-link to a concept that doesn't have
# a page yet, and create_missing_stubs() creates a new bare stub for it —
# so the backlog only fully drains after enough rounds that no page is
# spawning new stubs anymore.
#
# Uses wiki_health_check.py --incomplete-count for the exact (non-double-
# counting) total, so convergence is measured precisely rather than off
# enrich.py's own draft+TODO-may-overlap summary line.
#
#   nohup deploy/whittle_backlog.sh > eval/health/whittle.log 2>&1 &
#   disown
#   tail -f eval/health/whittle.log
#
# Override the round cap via env var if needed:
#   MAX_ROUNDS=20 deploy/whittle_backlog.sh
set -uo pipefail
cd "$(dirname "$0")/.."

MAX_ROUNDS="${MAX_ROUNDS:-10}"
prev_count=-1

for round in $(seq 1 "$MAX_ROUNDS"); do
  echo ""
  echo "########################################################################"
  echo "### whittle round $round/$MAX_ROUNDS ###"
  echo "########################################################################"
  deploy/run_full_enrichment.sh

  count=$(./venv/bin/python scripts/wiki_health_check.py --incomplete-count)
  echo ""
  echo "### round $round done: $count total incomplete page(s) remaining ###"

  if [ "$count" -eq 0 ]; then
    echo "### converged: 0 incomplete pages remaining — stopping ###"
    break
  fi
  if [ "$count" -eq "$prev_count" ]; then
    echo "### no progress since last round ($prev_count -> $count) — stopping rather than loop " \
         "forever on pages that keep failing to enrich (check for [ERROR] lines above) ###"
    break
  fi
  prev_count="$count"
done

echo ""
echo "=== whittle_backlog.sh finished after round $round ==="
