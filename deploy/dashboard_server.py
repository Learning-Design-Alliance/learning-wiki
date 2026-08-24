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

import json
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
VENV_PYTHON = WIKI_ROOT / "venv" / "bin" / "python"
PORT = 8080
MAX_ROUNDS = 20


def _parse_config_args() -> list:
    if not AUTO_OPTIMIZE_CONFIG.exists():
        return []
    match = re.search(r'^AUTO_OPTIMIZE_ARGS="(.*)"\s*$', AUTO_OPTIMIZE_CONFIG.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).split() if match else []


def _resolve_launch_args(rounds: int) -> list:
    """Builds the argv for `scripts/eval_harness.py auto-optimize`: rounds
    from the form; baseline-run from the last search's recorded state (so
    clicking "launch more rounds" continues forward from wherever the
    previous search left off) if one exists, else from whatever
    --baseline-run is already configured in auto-optimize-config.env; every
    other flag (candidates-per-round, concurrency, judges, ...) comes
    unchanged from that same config file."""
    args = _parse_config_args()

    baseline_run = None
    if STATE_PATH.exists():
        try:
            state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            baseline_run = state.get("current_run_id")
        except (json.JSONDecodeError, OSError):
            baseline_run = None

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


def _already_running() -> bool:
    try:
        result = subprocess.run(
            ["pgrep", "-f", "scripts/eval_harness.py auto-optimize"],
            capture_output=True, text=True, timeout=5,
        )
        return result.returncode == 0
    except (subprocess.SubprocessError, OSError):
        return False  # fail open rather than block every launch on a missing/broken pgrep


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
            self._respond_html(400, f"<p>rounds must be a whole number between 1 and {MAX_ROUNDS}.</p>"
                                     f'<p><a href="/">Back</a></p>')
            return

        if _already_running():
            self._respond_html(
                409, "<p>An auto-optimize search is already running — check the landing page's status "
                     'banner or its log before starting another.</p><p><a href="/">Back</a></p>')
            return

        if not VENV_PYTHON.exists():
            self._respond_html(500, f"<p>{VENV_PYTHON} not found — is the venv set up?</p>"
                                     f'<p><a href="/">Back</a></p>')
            return

        launch_args = _resolve_launch_args(rounds)
        log_path = RUNS_DIR / f"web-launch-{int(time.time())}.log"
        log_file = open(log_path, "w", encoding="utf-8")
        subprocess.Popen(
            [str(VENV_PYTHON), "-u", "scripts/eval_harness.py", "auto-optimize", *launch_args],
            cwd=str(WIKI_ROOT), stdout=log_file, stderr=subprocess.STDOUT,
            start_new_session=True,  # detach — keeps running after this request returns
        )

        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

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
