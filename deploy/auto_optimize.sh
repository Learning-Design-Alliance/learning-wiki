#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
source "$(dirname "$0")/auto-optimize-config.env"
if [ -z "${AUTO_OPTIMIZE_ARGS:-}" ]; then
  echo "AUTO_OPTIMIZE_ARGS is not set — edit deploy/auto-optimize-config.env first." >&2
  exit 1
fi
exec ./venv/bin/python -u scripts/eval_harness.py auto-optimize $AUTO_OPTIMIZE_ARGS
