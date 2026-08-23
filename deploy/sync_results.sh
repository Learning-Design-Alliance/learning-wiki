#!/usr/bin/env bash
# sync_results.sh — pull eval/runs/ back from the droplet to your machine.
# Run from your laptop, from the repo root.
#
# Usage: deploy/sync_results.sh <droplet-ip> [local-dest]
set -euo pipefail

DROPLET_IP="${1:?Usage: deploy/sync_results.sh <droplet-ip> [local-dest]}"
DEST="${2:-eval/runs}"

mkdir -p "$DEST"
rsync -avz --progress "root@${DROPLET_IP}:/opt/learning-wiki/eval/runs/" "$DEST/"

echo
echo "Synced to $DEST. Generate/refresh a report locally with:"
echo "  python3 scripts/eval_harness.py report --run-id <run-id>"
