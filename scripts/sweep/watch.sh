#!/bin/bash
# Exits with a HOLD line as soon as the driver writes ATTENTION; otherwise runs until killed.
# Run as a background task so an agent session is woken at the hold.
W=$(cd "$(dirname "$(readlink -f "$0")")/../.." && pwd)
J=${SWEEP_DIR:-$W/eval/runs/sweep}
while true; do
  [ -e "$J/ATTENTION" ] && { echo "HOLD $(date +%H:%M:%S): $(cut -f1,2 "$J/ATTENTION" | tr '\n' ' ')"; exit 0; }
  sleep 30
done
