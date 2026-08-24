#!/usr/bin/env bash
# run.sh — systemd ExecStart target. Reads RUN_ARGS from the environment
# (set in /etc/eval-harness.env via the unit's EnvironmentFile) and execs the
# harness so it becomes PID 1 of this service (clean signal handling, and
# `systemctl stop` reaches it directly instead of a shell wrapper).
set -euo pipefail
cd "$(dirname "$0")/.."

if [ -z "${RUN_ARGS:-}" ]; then
  echo "RUN_ARGS is not set — edit /etc/eval-harness.env first." >&2
  exit 1
fi

# -u: unbuffered stdout/stderr. Without it, Python block-buffers stdout when
# it isn't a TTY (i.e. always, under systemd) — progress prints can sit
# unflushed until the buffer fills or the process exits, making a run look
# stuck in `journalctl` even though it's actively working (results are still
# written to disk per pair regardless; this only affects live log visibility).
#
# Intentionally unquoted: RUN_ARGS is a space-separated arg list, not one string.
exec ./venv/bin/python -u scripts/eval_harness.py run $RUN_ARGS
