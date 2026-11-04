#!/bin/bash
# Start the sweep driver detached, so it outlives the shell. Run it from a shell with the current
# HTTPS_PROXY: after a container restart the proxy port changes and a process keeps the old one.
D=$(dirname "$(readlink -f "$0")")
setsid nohup bash "$D/drive.sh" > /dev/null 2>&1 < /dev/null &
echo "driver started (state in ${SWEEP_DIR:-eval/runs/sweep})"
