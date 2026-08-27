#!/usr/bin/env bash
# live_view.sh — open an SSH tunnel to the droplet's dashboard server and open
# it in your browser. Run from your Mac. Leave it running in its own terminal
# tab (Ctrl-C to stop the tunnel when you're done watching).
#
# Usage: deploy/live_view.sh <droplet-ip> [run-id]
set -euo pipefail

DROPLET_IP="${1:?Usage: deploy/live_view.sh <droplet-ip> [run-id]}"
RUN_ID="${2:-do-batch-1}"
PORT=8080

echo "Tunneling localhost:${PORT} -> ${DROPLET_IP}:${PORT} (Ctrl-C to stop)"
( sleep 1 && open "http://localhost:${PORT}/${RUN_ID}/report.html" ) &
ssh -N -L "${PORT}:127.0.0.1:${PORT}" "root@${DROPLET_IP}"
