#!/usr/bin/env python3
"""
dashboard_server.py — Serves eval/runs/ (same as `python3 -m http.server`
did before) plus one POST endpoint, /launch-auto-optimize, so the landing
page's "Launch N more rounds" button can actually start a search — without
this, the button would have nothing to submit to, since a plain static
file server can't execute anything.

Stdlib only, deliberately: this process is always-on
(eval-harness-web.service), so it stays minimal rather than pulling in a
web framework for one endpoint.

Security note: binds to 127.0.0.1 only (see eval-harness-web.service) —
reachable only through an SSH tunnel by whoever holds the droplet's SSH
key, the same trust boundary as every other command in this harness.
Still validates the one input it accepts and never shells out with
string-interpolated input (subprocess with an argv list, not shell=True).
"""

import html
import json
import os
import re
import subprocess
import time
import urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
RUNS_DIR = WIKI_ROOT / "eval" / "runs"
AUTO_OPTIMIZE_CONFIG = WIKI_ROOT / "deploy" / "auto-optimize-config.env"
STATE_PATH = RUNS_DIR / ".auto_optimize_state.json"
LOCK_PATH = RUNS_DIR / ".auto_optimize.lock"
VENV_PYTHON = WIKI_ROOT / "venv" / "bin" / "python"
SECRETS_ENV_FILE = Path("/etc/eval-harness.env")
PORT = 8080
MAX_ROUNDS = 20


def _child_env() -> dict:
    """Environment for the spawned auto-optimize subprocess. This service
    (eval-harness-web.service) has no EnvironmentFile= of its own, so
    without this the child only inherits this bare process's environment
    — it does call eval_harness.py's own _load_secrets_env() at the top of
    its main(), but that runs too late for any module that reads an env
    var into a module-level constant at import time (scripts/eval/
    compliance.py's CONTACT_EMAIL does exactly this): by the time main()
    backfills os.environ, that constant is already frozen from whatever
    was there at interpreter start. Loading the secrets file here and
    passing a complete env explicitly avoids that whole class of
    import-order bug, not just this one variable — this is exactly how
    EVAL_HARNESS_CONTACT_EMAIL kept showing as unset in a web-launched
    run even after being set correctly in the file."""
    env = os.environ.copy()
    if SECRETS_ENV_FILE.exists():
        try:
            text = SECRETS_ENV_FILE.read_text(encoding="utf-8")
        except OSError:
            return env
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key, value = key.strip(), value.strip()
            if key:
                env[key] = value
    return env


def _parse_config_args() -> list:
    if not AUTO_OPTIMIZE_CONFIG.exists():
        return []
    match = re.search(r'^AUTO_OPTIMIZE_ARGS="(.*)"\s*$', AUTO_OPTIMIZE_CONFIG.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).split() if match else []


# Statuses cmd_auto_optimize actually reaches on a clean stop — safe to
# treat their current_run_id as a real, complete baseline to build on.
GOOD_BASELINE_STATUSES = {"completed", "stopped_no_findings", "stopped_time_budget"}


def _resolve_baseline_from_state() -> str:
    """The run id to continue from, or None to fall back to whatever
    --baseline-run is configured in auto-optimize-config.env. Deliberately
    does NOT just trust current_run_id at face value — a state file stuck
    on "running"/"starting" from a process that died uncleanly (SSH
    disconnect, kill -9) points at a run that may be mid-round or
    contaminated (this is exactly what happened live: a dead search's
    current_run_id had generation errors from concurrent-with-another-
    search API rate limiting, and blindly reusing it as the next baseline
    would just fail again). Also refuses a status that reflects a baseline
    known to be broken (stopped_error, stopped_generation_errors) or
    anything unrecognized, rather than silently building on top of it."""
    if not STATE_PATH.exists():
        return None
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    status = state.get("status")
    if status in ("running", "starting"):
        if not _already_running():
            return None  # stale snapshot from a process that's no longer alive
    elif status not in GOOD_BASELINE_STATUSES:
        return None

    return state.get("current_run_id")


def _resolve_launch_args(rounds: int) -> list:
    """Builds the argv for `scripts/eval_harness.py auto-optimize`: rounds
    from the form; baseline-run from the last search's recorded state (so
    clicking "launch more rounds" continues forward from wherever the
    previous search left off) if that state looks trustworthy (see
    _resolve_baseline_from_state), else from whatever --baseline-run is
    already configured in auto-optimize-config.env; every other flag
    (concurrency, judges, ...) comes unchanged from that same config file."""
    args = _parse_config_args()
    baseline_run = _resolve_baseline_from_state()

    if baseline_run:
        if "--baseline-run" in args:
            idx = args.index("--baseline-run")
            args[idx + 1] = baseline_run
        else:
            args += ["--baseline-run", baseline_run]

    if "--rounds" in args:
        idx = args.index("--rounds")
        args[idx + 1] = str(rounds)
    else:
        args += ["--rounds", str(rounds)]

    return args


def _pid_is_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True  # process exists, just owned by someone else — treat as alive
    return True


def _tail_log(path: Path, n: int = 40) -> str:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "(log file unavailable)"
    return "\n".join(lines[-n:]) or "(empty log)"


def _already_running() -> bool:
    """Reads the same cross-invocation lockfile scripts/eval_harness.py's
    cmd_auto_optimize() itself enforces (eval/runs/.auto_optimize.lock),
    rather than a pgrep guess — that's the real, always-correct source of
    truth (it also catches a directly-invoked CLI search this endpoint
    never spawned), this check just avoids launching a subprocess only to
    have it immediately exit on the lock and leave a confusing log file."""
    if not LOCK_PATH.exists():
        return False
    try:
        info = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    pid = info.get("pid")
    return bool(pid and _pid_is_alive(pid))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(RUNS_DIR), **kwargs)

    def log_message(self, format, *args):
        pass  # static-file hits every 20s (auto-refresh) aren't worth journal noise

    def do_POST(self):
        if self.path != "/launch-auto-optimize":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="replace")
        form = urllib.parse.parse_qs(body)

        try:
            rounds = int(form.get("rounds", ["10"])[0])
        except ValueError:
            rounds = None

        if rounds is None or not (1 <= rounds <= MAX_ROUNDS):
            self._respond(400, f"rounds must be a whole number between 1 and {MAX_ROUNDS}.")
            return

        if _already_running():
            self._respond(409, "An auto-optimize search is already running — check the landing page's "
                                "status banner or its log before starting another.")
            return

        if not VENV_PYTHON.exists():
            self._respond(500, f"{VENV_PYTHON} not found — is the venv set up?")
            return

        launch_args = _resolve_launch_args(rounds)
        log_path = RUNS_DIR / f"web-launch-{int(time.time())}.log"
        log_file = open(log_path, "w", encoding="utf-8")
        proc = subprocess.Popen(
            [str(VENV_PYTHON), "-u", "scripts/eval_harness.py", "auto-optimize", *launch_args],
            cwd=str(WIKI_ROOT), stdout=log_file, stderr=subprocess.STDOUT,
            start_new_session=True,  # detach — keeps running after this request returns
            env=_child_env(),
        )

        # cmd_auto_optimize's safety gates (lock conflict, a baseline with
        # generation errors, no baseline directory, ...) all fire within
        # the first second or two — no API calls needed, just local file
        # checks — so a bounded wait here catches that class of failure
        # and shows it directly, instead of a blind redirect that looks
        # identical whether the search started or died instantly. A
        # legitimate, still-running search just falls through to the
        # normal redirect after this same wait.
        time.sleep(2.5)
        if proc.poll() is not None and proc.returncode != 0:
            tail = _tail_log(log_path)
            self._respond(500, f"auto-optimize exited immediately (exit code {proc.returncode}) — it did "
                                f"not start a search.\n\nLast log lines:\n{tail}")
            return

        self._respond(200, f"Launch started — {rounds} more round(s) queued.")

    def _wants_json(self) -> bool:
        # The landing page's launch form submits via fetch() with this
        # header so it can show the result as a JS dialog instead of
        # navigating to a whole separate page for a one-line status
        # message; anything else (a bare curl, a browser with JS off)
        # still gets a normal HTML page back.
        return "application/json" in self.headers.get("Accept", "")

    def _respond(self, status: int, message: str) -> None:
        if self._wants_json():
            body = json.dumps({"ok": status < 300, "message": message}).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if status < 300:
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
            return
        self._respond_html(status, f"<pre>{html.escape(message)}</pre><p><a href=\"/\">Back</a></p>")

    def _respond_html(self, status: int, body: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Serving {RUNS_DIR} on http://127.0.0.1:{PORT} (static files + POST /launch-auto-optimize)")
    server.serve_forever()


if __name__ == "__main__":
    main()
