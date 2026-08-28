#!/usr/bin/env python3
"""
dashboard_server.py — Serves eval/runs/ (same as `python3 -m http.server`
did before) plus five POST endpoints the landing page's buttons/forms
submit to — without these, static-file serving alone gives the page
nothing to actually execute:
  /launch-auto-optimize   start a search ("Launch N more rounds") — baseline
                           is the previous search's own recorded state when
                           that looks trustworthy (see
                           _resolve_baseline_for_launch), else --baseline-run
                           is simply omitted from the launched argv and
                           eval_harness.py's cmd_auto_optimize resolves it
                           itself (the run that tested the live current
                           prompt version) — the SAME resolution the systemd
                           unit and a bare CLI call get, one implementation
                           rather than a second copy that can drift out of
                           sync with it (see eval_harness.py's
                           _resolve_default_baseline_run for why that
                           matters)
  /delete-run             rm -rf one run directory ("Delete" per row)
  /rerun-run              retry only a run's previously-failed pairs
                           ("Rerun" per row), reconstructed from its own
                           queue.json — for recovering from something
                           transient (a billing cap, an expired key)
                           without re-paying for pairs that already
                           succeeded
  /set-current-version    roll scripts/eval/prompt_versions/CURRENT to a
                           specific version by hand (a billing-cap or
                           contaminated round used to mean SSHing in for
                           this and the rm -rf above every time)
  /use-as-baseline        ("Use as baseline" per row) roll BOTH the live
                           prompt version AND auto-optimize's own
                           continuation pointer back to a specific earlier
                           run in one action — /set-current-version alone
                           only changes what a manual `run` uses next;
                           "Launch more rounds" ignores it and always
                           resumes from .auto_optimize_state.json's
                           current_run_id (a growing lineage can plateau or
                           regress in cost/latency for many rounds without
                           quality moving, and continuing to build on it
                           forever isn't the only option)
  /stop-auto-optimize     ("Stop" button, shown while a search is live) —
                           kills the actual running search process by its
                           recorded pid (eval/runs/.auto_optimize.lock),
                           for exactly the "I launched this against the
                           wrong baseline" case: there was previously no
                           way to interrupt a running search short of
                           SSHing in to kill it by hand. Marks the stopped
                           run "stopped_by_user" rather than a clean-stop
                           status, so it's never silently reused as the
                           next launch's continuation baseline — pick one
                           explicitly with "Use as baseline" instead.
  /launch-scrape          start a discover_articles.py + fetch_article.py
                           batch (scripts/run_scrape_batch.py) — separate
                           from auto-optimize's own launch/lock/state, since
                           these are two independent long-running jobs a
                           user could otherwise (mistakenly) run at once.
                           Progress renders at /scrape.html.
  /stop-scrape             kills the running scrape batch by its recorded
                           pid (eval/runs/.scrape.lock), same pattern as
                           /stop-auto-optimize.

Stdlib only, deliberately: this process is always-on
(eval-harness-web.service), so it stays minimal rather than pulling in a
web framework for four endpoints.

Security note: binds to 127.0.0.1 only (see eval-harness-web.service) —
reachable only through an SSH tunnel by whoever holds the droplet's SSH
key, the same trust boundary as every other command in this harness.
Still validates every input it accepts (run ids and version strings are
checked against a strict allow-list pattern before touching the
filesystem) and never shells out with string-interpolated input
(subprocess with an argv list, not shell=True).
"""

import html
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
RUNS_DIR = WIKI_ROOT / "eval" / "runs"
AUTO_OPTIMIZE_CONFIG = WIKI_ROOT / "deploy" / "auto-optimize-config.env"
STATE_PATH = RUNS_DIR / ".auto_optimize_state.json"
LOCK_PATH = RUNS_DIR / ".auto_optimize.lock"
PROMPT_VERSIONS_DIR = WIKI_ROOT / "scripts" / "eval" / "prompt_versions"
VENV_PYTHON = WIKI_ROOT / "venv" / "bin" / "python"
SECRETS_ENV_FILE = Path("/etc/eval-harness.env")
PORT = 8080
MAX_ROUNDS = 20
_SAFE_RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
_SAFE_VERSION_RE = re.compile(r"^v\d+$")

# scrape (discover_articles.py + fetch_article.py) launch/lock/state — kept
# entirely separate from auto-optimize's own STATE_PATH/LOCK_PATH above,
# since these are two independent long-running jobs a user could otherwise
# (mistakenly) launch at once. scrape_report.py is stdlib-only (see its own
# module docstring) so it's safe to import directly here even though this
# server itself runs under system python, not the venv (see
# eval-harness-web.service) — unlike discover_articles.py/fetch_article.py,
# which need the venv's `requests` and are only ever launched as a
# subprocess, never imported into this process.
sys.path.insert(0, str(WIKI_ROOT))
from scripts.eval import scrape_report, model_catalog  # noqa: E402 - after sys.path fixup, deliberately

RUN_SCRAPE_SCRIPT = WIKI_ROOT / "scripts" / "run_scrape_batch.py"
SCRAPE_STATE_PATH = RUNS_DIR / ".scrape_state.json"
SCRAPE_LOCK_PATH = RUNS_DIR / ".scrape.lock"
SCRAPE_CORPUS_DIR = (WIKI_ROOT / "eval" / "corpus").resolve()


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


def _regenerate_index() -> None:
    """Runs the `index` command synchronously so a delete/rollback shows up
    on the landing page immediately on reload, instead of waiting for the
    next batch to report progress (see eval_harness.py's generate_index()
    docstring for why that gap exists at all). Fast — pure local file
    scanning, no API calls — so blocking the request for it is fine."""
    if not VENV_PYTHON.exists():
        return
    subprocess.run(
        [str(VENV_PYTHON), "scripts/eval_harness.py", "index"],
        cwd=str(WIKI_ROOT), env=_child_env(), capture_output=True,
    )


def _parse_config_args() -> list:
    if not AUTO_OPTIMIZE_CONFIG.exists():
        return []
    match = re.search(r'^AUTO_OPTIMIZE_ARGS="(.*)"\s*$', AUTO_OPTIMIZE_CONFIG.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1).split() if match else []


# Statuses cmd_auto_optimize actually reaches on a clean stop — safe to
# treat their current_run_id as a real, complete baseline to build on.
# "manually_reset" is the one status cmd_auto_optimize itself never
# writes — only _handle_use_as_baseline does, when a human deliberately
# points the search at an earlier run — and it's just as trustworthy as a
# clean stop.
GOOD_BASELINE_STATUSES = {"completed", "stopped_no_findings", "stopped_time_budget", "manually_reset"}


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


def _resolve_baseline_for_launch() -> tuple:
    """Returns (baseline_run, source). Only one tier lives here:
    .auto_optimize_state.json, if it looks trustworthy (see
    _resolve_baseline_from_state) — continues exactly where the last
    dashboard-driven search left off, which is dashboard-specific
    continuation semantics no other invocation path needs.

    Everything past that is deliberately NOT duplicated here: baseline_run
    of None just means --baseline-run is omitted from the launched argv,
    and eval_harness.py's own _resolve_default_baseline_run() takes over —
    the ONE canonical implementation of "what's the current best baseline,"
    also used by the systemd unit and a bare CLI call. This file used to
    carry its own second copy of that resolution (a from-CURRENT lookup,
    then a static auto-optimize-config.env fallback) and that second copy
    is exactly how a real incident happened: the systemd path never went
    through it at all, so fixing staleness here alone left that path just
    as exposed. One implementation, used everywhere, instead."""
    from_state = _resolve_baseline_from_state()
    if from_state:
        return from_state, "the previous search's own recorded state"
    return None, "eval_harness.py's own default (the run that tested the live current prompt version)"


def _resolve_launch_args(rounds: int, baseline_run: str) -> list:
    """Builds the argv for `scripts/eval_harness.py auto-optimize`: rounds
    from the form; baseline-run as resolved by _resolve_baseline_for_launch;
    every other flag (concurrency, judges, ...) comes unchanged from
    auto-optimize-config.env."""
    args = _parse_config_args()

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


def _kill_and_reap(pid: int) -> None:
    """SIGTERM (escalating to SIGKILL after ~2.5s), then reap the zombie via
    waitpid. Found live, via this feature's own integration test: os.kill(pid, 0)
    (what _pid_is_alive() checks) keeps returning success for a process
    that has already exited but not yet been reaped — a kill-and-poll loop
    using only that check believes the process is still "alive" forever.
    This server never otherwise calls .wait()/.poll() on a process it
    Popen'd (each stop handler only has the pid, recorded in a lock file,
    not the original Popen object), and since it's always-on
    (eval-harness-web.service), every stopped auto-optimize/scrape job
    would leak a zombie for as long as the service keeps running without
    this. Shared by both stop handlers below."""
    os.kill(pid, signal.SIGTERM)
    for _ in range(10):
        try:
            reaped, _ = os.waitpid(pid, os.WNOHANG)
        except ChildProcessError:
            return  # already reaped, or this process was never our direct child
        if reaped == pid:
            return
        time.sleep(0.25)
    os.kill(pid, signal.SIGKILL)
    try:
        os.waitpid(pid, 0)  # blocking, but SIGKILL is uncatchable so this returns almost immediately
    except ChildProcessError:
        pass


def _reap_if_zombie(pid: int) -> bool:
    """Non-destructive liveness check that also clears a finished child
    instead of letting it masquerade as still-running forever. Plain
    os.kill(pid, 0) (what _pid_is_alive() checks) keeps reporting success
    for a process that already exited but was never reaped by its parent —
    confirmed live: a scrape batch launched via subprocess.Popen that
    finishes NORMALLY (not via the Stop button, which already reaps
    through _kill_and_reap) is never waited-on by this server, so it sits
    as a zombie and _scrape_already_running() reports "still running"
    indefinitely — every launch after the first successful scrape silently
    404s on the lock until the whole service is restarted, which just
    happens to reap it as a side effect of the old process exiting.
    Returns True only if the process is genuinely still running."""
    try:
        reaped_pid, _ = os.waitpid(pid, os.WNOHANG)
        return reaped_pid != pid  # 0 means still running; == pid means it was a zombie, now reaped
    except ChildProcessError:
        # Not this process's child (e.g. spawned by a since-restarted
        # instance of this service) — fall back to a plain existence check.
        return _pid_is_alive(pid)


def _scrape_already_running() -> bool:
    """Same pattern as _already_running(), against SCRAPE_LOCK_PATH instead
    — unlike auto-optimize's lock (self-managed: cmd_auto_optimize() cleans
    up its own lock file when it finishes), this one is written AND
    destroyed entirely by this server, so nothing removes it when the
    scrape subprocess finishes on its own — see _reap_if_zombie() for why
    that made every scrape after the first one silently unlaunchable. Also
    only catches a scrape launched through the dashboard, not a bare CLI
    invocation run alongside it. Acceptable for now: the dashboard button
    is the primary way this gets launched."""
    if not SCRAPE_LOCK_PATH.exists():
        return False
    try:
        info = json.loads(SCRAPE_LOCK_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    pid = info.get("pid")
    if pid and _reap_if_zombie(pid):
        return True
    # Dead (freshly reaped above, or already gone) — the lock is stale;
    # clear it so it stops blocking every future launch attempt.
    SCRAPE_LOCK_PATH.unlink(missing_ok=True)
    return False


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(RUNS_DIR), **kwargs)

    def log_message(self, format, *args):
        pass  # static-file hits every 20s (auto-refresh) aren't worth journal noise

    def end_headers(self):
        # SimpleHTTPRequestHandler only sends Last-Modified by default, no
        # Cache-Control — enough for a browser to serve a stale index.html
        # (or .auto_optimize_console.log, or a run's own report.html) back
        # from its disk cache on the page's own 20s auto-refresh instead of
        # re-fetching, which reads as "it looked right, then reverted" even
        # though the file on disk never changed back. Every response here
        # is either generated fresh on each request or expected to change
        # between polls, so never let it be cached.
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def do_POST(self):
        handlers = {
            "/launch-auto-optimize": self._handle_launch,
            "/delete-run": self._handle_delete_run,
            "/set-current-version": self._handle_set_current_version,
            "/rerun-run": self._handle_rerun,
            "/use-as-baseline": self._handle_use_as_baseline,
            "/stop-auto-optimize": self._handle_stop_auto_optimize,
            "/launch-scrape": self._handle_launch_scrape,
            "/stop-scrape": self._handle_stop_scrape,
        }
        handler = handlers.get(self.path)
        if handler is None:
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="replace")
        form = urllib.parse.parse_qs(body)
        handler(form)

    def _handle_launch(self, form: dict) -> None:
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

        baseline_run, baseline_source = _resolve_baseline_for_launch()
        # baseline_run of None is NOT an error here — it means no dashboard-
        # specific state applies, so --baseline-run is left out of the argv
        # and eval_harness.py resolves it itself (see
        # _resolve_baseline_for_launch's docstring). The subprocess is the
        # one that errors out, visibly, if even that can't resolve anything.
        launch_args = _resolve_launch_args(rounds, baseline_run)
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

        baseline_desc = baseline_run if baseline_run else f"auto-resolved by {baseline_source}"
        self._respond(200, f"Launch started — {rounds} more round(s) queued, baseline: {baseline_desc}. "
                            f"Check the console log or the new run's own header to confirm the exact "
                            f"baseline once the first round starts.")

    def _handle_stop_auto_optimize(self, form: dict) -> None:
        """Kills the actual running auto-optimize process by the pid it
        recorded in its own cross-invocation lock (see eval_harness.py's
        _acquire_auto_optimize_lock) — the same lock that already answers
        "is a search running," now also used to find what to kill. There
        was previously no way to interrupt a launched search short of
        SSHing in and killing it by hand — exactly what's needed for "I
        launched this against the wrong baseline," where every extra
        (model, article) pair the process completes before you notice is
        wasted spend."""
        if not LOCK_PATH.exists():
            self._respond(400, "No auto-optimize search is currently running.")
            return
        try:
            info = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            info = {}
        pid = info.get("pid")
        if not pid or not _pid_is_alive(pid):
            LOCK_PATH.unlink(missing_ok=True)
            self._respond(400, "No auto-optimize search is currently running (a stale lock file was cleaned up).")
            return

        _kill_and_reap(pid)

        LOCK_PATH.unlink(missing_ok=True)

        run_id = None
        if STATE_PATH.exists():
            try:
                state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                state = {}
            run_id = state.get("current_run_id")
            state["status"] = "stopped_by_user"
            state["error_detail"] = "Stopped manually from the dashboard."
            state["updated_at"] = datetime.now(timezone.utc).isoformat()
            STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")

        _regenerate_index()
        note = (f" Its last run ({run_id}) is left on disk — delete it if it was testing against the "
                f"wrong baseline, or use \"Use as baseline\" on whichever run you actually want to "
                f"continue from." if run_id else "")
        self._respond(200, f"Stopped (pid {pid}).{note}")

    def _handle_launch_scrape(self, form: dict) -> None:
        try:
            pmc = int(form.get("pmc", ["0"])[0])
            eric = int(form.get("eric", ["0"])[0])
            arxiv = int(form.get("arxiv", ["0"])[0])
        except ValueError:
            self._respond(400, "pmc/eric/arxiv must be whole numbers.", redirect_to="/scrape.html")
            return
        if pmc < 0 or eric < 0 or arxiv < 0 or (pmc + eric + arxiv) == 0:
            self._respond(400, "pmc/eric/arxiv must be non-negative, and at least one must be > 0.",
                           redirect_to="/scrape.html")
            return

        # export.arxiv.org's robots.txt disallows the live search API outright
        # (see eval/SOURCES.md) — arxiv>0 must come from the local Kaggle
        # snapshot. This field is an optional override for an
        # already-downloaded file; left blank, run_scrape_batch.py resolves
        # it itself via kagglehub (discover_articles.resolve_arxiv_snapshot()
        # — auto-downloads and caches on first use, from KAGGLE_USERNAME/
        # KAGGLE_KEY in /etc/eval-harness.env). Only validated here when
        # actually given — an empty field is not an error.
        arxiv_snapshot = (form.get("arxiv_snapshot", [""])[0] or "").strip()
        arxiv_snapshot_path = None
        if arxiv_snapshot:
            arxiv_snapshot_path = (WIKI_ROOT / arxiv_snapshot).resolve() if not Path(arxiv_snapshot).is_absolute() \
                else Path(arxiv_snapshot)
            if not arxiv_snapshot_path.is_file():
                self._respond(400, f"arXiv snapshot not found: {arxiv_snapshot}", redirect_to="/scrape.html")
                return

        model = (form.get("model", [""])[0] or "").strip()
        if model and model not in model_catalog.MODEL_DESCRIPTIONS:
            self._respond(400, f"Unknown model: {model!r} — pick one from the dropdown.",
                           redirect_to="/scrape.html")
            return
        prompt_version = (form.get("prompt_version", [""])[0] or "").strip()
        refresh_cache = (form.get("refresh_cache", [""])[0] or "").strip() == "1"

        out = (form.get("out", [""])[0] or "").strip() or "eval/corpus/manifest_bulk.json"
        # Becomes an argv element passed to a subprocess (not shell-
        # interpolated, so not a command-injection vector) — but an
        # absolute or ../-escaping path could still point outside
        # eval/corpus/ at a file evalrunner can write, so constrain it.
        out_path = (WIKI_ROOT / out).resolve()
        if SCRAPE_CORPUS_DIR != out_path.parent and SCRAPE_CORPUS_DIR not in out_path.parents:
            self._respond(400, f"Output path must be inside eval/corpus/, got: {out}", redirect_to="/scrape.html")
            return

        if _scrape_already_running():
            self._respond(409, "A scrape batch is already running — check /scrape.html's status or "
                                "console log before starting another.", redirect_to="/scrape.html")
            return
        if not VENV_PYTHON.exists():
            self._respond(500, f"{VENV_PYTHON} not found — is the venv set up?", redirect_to="/scrape.html")
            return
        if not RUN_SCRAPE_SCRIPT.exists():
            self._respond(500, f"{RUN_SCRAPE_SCRIPT} not found.", redirect_to="/scrape.html")
            return

        label = f"scrape-{int(time.time())}"
        launch_args = ["--pmc", str(pmc), "--eric", str(eric), "--arxiv", str(arxiv),
                        "--out", str(out_path.relative_to(WIKI_ROOT)), "--label", label]
        if arxiv_snapshot_path:
            launch_args += ["--arxiv-snapshot", str(arxiv_snapshot_path)]
        if model:
            launch_args += ["--model", model]
        if prompt_version:
            launch_args += ["--prompt-version", prompt_version]
        if refresh_cache:
            launch_args += ["--refresh-cache"]
        log_path = RUNS_DIR / f"web-scrape-{int(time.time())}.log"
        log_file = open(log_path, "w", encoding="utf-8")
        proc = subprocess.Popen(
            [str(VENV_PYTHON), "-u", str(RUN_SCRAPE_SCRIPT), *launch_args],
            cwd=str(WIKI_ROOT), stdout=log_file, stderr=subprocess.STDOUT,
            start_new_session=True, env=_child_env(),
        )
        SCRAPE_LOCK_PATH.write_text(json.dumps({
            "pid": proc.pid, "label": label,
            "started_at": datetime.now(timezone.utc).isoformat(),
        }), encoding="utf-8")

        # Same reasoning as _handle_launch: an immediate-exit failure (bad
        # args, missing snapshot file, no wiki topics found) fires within a
        # second or two with no API calls needed, so a bounded wait catches
        # it and shows it directly instead of a blind redirect.
        time.sleep(2.5)
        if proc.poll() is not None and proc.returncode != 0:
            tail = _tail_log(log_path)
            SCRAPE_LOCK_PATH.unlink(missing_ok=True)
            self._respond(500, f"Scrape batch exited immediately (exit code {proc.returncode}) — it did "
                                f"not start.\n\nLast log lines:\n{tail}", redirect_to="/scrape.html")
            return

        self._respond(200, f"Scrape batch {label!r} launched (pmc={pmc}, eric={eric}, arxiv={arxiv}, "
                            f"out={out}). See /scrape.html for live progress.", redirect_to="/scrape.html")

    def _handle_stop_scrape(self, form: dict) -> None:
        """Same pattern as _handle_stop_auto_optimize — see its docstring."""
        if not SCRAPE_LOCK_PATH.exists():
            self._respond(400, "No scrape batch is currently running.", redirect_to="/scrape.html")
            return
        try:
            info = json.loads(SCRAPE_LOCK_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            info = {}
        pid = info.get("pid")
        if not pid or not _pid_is_alive(pid):
            SCRAPE_LOCK_PATH.unlink(missing_ok=True)
            self._respond(400, "No scrape batch is currently running (a stale lock file was cleaned up).",
                           redirect_to="/scrape.html")
            return

        _kill_and_reap(pid)
        SCRAPE_LOCK_PATH.unlink(missing_ok=True)

        if SCRAPE_STATE_PATH.exists():
            try:
                state = json.loads(SCRAPE_STATE_PATH.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                state = {}
            state["status"] = "stopped_by_user"
            state["finished_at"] = datetime.now(timezone.utc).isoformat()
            SCRAPE_STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
            (RUNS_DIR / "scrape.html").write_text(scrape_report.render_html(state), encoding="utf-8")

        self._respond(200, f"Stopped scrape batch (pid {pid}).", redirect_to="/scrape.html")

    def _handle_delete_run(self, form: dict) -> None:
        run_id = (form.get("run_id", [""])[0] or "").strip()
        if not run_id or not _SAFE_RUN_ID_RE.match(run_id):
            self._respond(400, f"Invalid run id: {run_id!r}")
            return

        target = (RUNS_DIR / run_id).resolve()
        if target.parent != RUNS_DIR.resolve() or not target.is_dir():
            self._respond(404, f"No such run directory: {run_id}")
            return

        state = {}
        if STATE_PATH.exists():
            try:
                state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                state = {}
        if state.get("current_run_id") == run_id and _already_running():
            self._respond(409, f"{run_id} is the currently-running search's active run — wait for it to "
                                f"finish (or stop it) before deleting its directory.")
            return

        shutil.rmtree(target)
        _regenerate_index()

        note = ""
        if state.get("current_run_id") == run_id:
            note = (f" Note: {run_id} was the last search's recorded baseline "
                    f"(.auto_optimize_state.json) — set a new current prompt version and/or update "
                    f"deploy/auto-optimize-config.env's --baseline-run before launching again, or the "
                    f"next round will fail immediately with \"no completed results to learn from.\"")
        self._respond(200, f"Deleted {run_id}.{note}")

    def _handle_rerun(self, form: dict) -> None:
        run_id = (form.get("run_id", [""])[0] or "").strip()
        if not run_id or not _SAFE_RUN_ID_RE.match(run_id):
            self._respond(400, f"Invalid run id: {run_id!r}")
            return

        run_dir = (RUNS_DIR / run_id).resolve()
        if run_dir.parent != RUNS_DIR.resolve() or not run_dir.is_dir():
            self._respond(404, f"No such run directory: {run_id}")
            return

        queue_path = run_dir / "queue.json"
        if not queue_path.exists():
            self._respond(400, f"{run_id} has no queue.json (an older run, from before this metadata was "
                                f"recorded) — nothing to reconstruct a rerun from.")
            return
        try:
            meta = json.loads(queue_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            self._respond(500, f"Could not read {run_id}/queue.json: {e}")
            return

        models = meta.get("models") or []
        article_ids = meta.get("article_ids") or []
        if not models or not article_ids:
            self._respond(400, f"{run_id}/queue.json is missing models or article_ids (an older run) — "
                                f"nothing to reconstruct a rerun from.")
            return

        if _already_running():
            self._respond(409, "An auto-optimize search is currently running — wait for it to finish "
                                "before rerunning a batch (running both at once risks the same OpenRouter "
                                "rate-limit contention that caused this session's earlier problems).")
            return
        if not VENV_PYTHON.exists():
            self._respond(500, f"{VENV_PYTHON} not found — is the venv set up?")
            return

        run_args = ["--run-id", run_id, "--models", *models, "--articles", *article_ids,
                    "--retry-errors-only"]
        if meta.get("prompt_version"):
            run_args += ["--prompt-version", meta["prompt_version"]]
        if meta.get("judges"):
            run_args += ["--judges", *meta["judges"]]
        if meta.get("max_tokens"):
            run_args += ["--max-tokens", str(meta["max_tokens"])]
        if meta.get("gpt_judge_model"):
            run_args += ["--gpt-judge-model", meta["gpt_judge_model"]]
        if meta.get("gemini_judge_model"):
            run_args += ["--gemini-judge-model", meta["gemini_judge_model"]]
        if meta.get("concurrency"):
            run_args += ["--concurrency", str(meta["concurrency"])]
        if meta.get("max_correction_attempts"):
            run_args += ["--max-correction-attempts", str(meta["max_correction_attempts"])]
        if meta.get("ground_truth"):
            run_args += ["--ground-truth"]
        if meta.get("require_source_quotes"):
            run_args += ["--require-source-quotes"]
        if meta.get("consistency_samples", 1) and meta["consistency_samples"] > 1:
            run_args += ["--consistency-samples", str(meta["consistency_samples"])]

        log_path = RUNS_DIR / f"web-rerun-{int(time.time())}.log"
        log_file = open(log_path, "w", encoding="utf-8")
        proc = subprocess.Popen(
            [str(VENV_PYTHON), "-u", "scripts/eval_harness.py", "run", *run_args],
            cwd=str(WIKI_ROOT), stdout=log_file, stderr=subprocess.STDOUT,
            start_new_session=True, env=_child_env(),
        )

        # Same reasoning as _handle_launch: a bad reconstruction (an
        # unresolvable model/article id, a missing prompt version file)
        # fails within the first second or two, no API calls needed.
        time.sleep(2.5)
        if proc.poll() is not None and proc.returncode != 0:
            tail = _tail_log(log_path)
            self._respond(500, f"Rerun of {run_id} exited immediately (exit code {proc.returncode}).\n\n"
                                f"Last log lines:\n{tail}")
            return

        self._respond(200, f"Rerun started for {run_id} — retrying only its previously-failed pairs.")

    def _handle_set_current_version(self, form: dict) -> None:
        version = (form.get("version", [""])[0] or "").strip()
        if not version or not _SAFE_VERSION_RE.match(version):
            self._respond(400, f"Invalid version: {version!r} (expected e.g. v15)")
            return

        version_file = PROMPT_VERSIONS_DIR / f"{version}.txt"
        if not version_file.is_file():
            self._respond(404, f"No such prompt version file: {version_file.name}")
            return

        (PROMPT_VERSIONS_DIR / "CURRENT").write_text(version + "\n", encoding="utf-8")
        _regenerate_index()
        self._respond(200, f"Current prompt version set to {version}.")

    def _handle_use_as_baseline(self, form: dict) -> None:
        """Rolls BOTH the live prompt version and auto-optimize's own
        continuation pointer back to an earlier run in one action —
        /set-current-version alone only changes what the next manual `run`
        uses; "Launch more rounds" ignores CURRENT entirely and always
        resumes from .auto_optimize_state.json's current_run_id (see
        _resolve_baseline_from_state). Without also rewriting that file, a
        user rolling CURRENT back in the UI and then clicking "Launch more
        rounds" would silently keep building on the lineage they just
        tried to abandon."""
        run_id = (form.get("run_id", [""])[0] or "").strip()
        if not run_id or not _SAFE_RUN_ID_RE.match(run_id):
            self._respond(400, f"Invalid run id: {run_id!r}")
            return

        run_dir = (RUNS_DIR / run_id).resolve()
        if run_dir.parent != RUNS_DIR.resolve() or not run_dir.is_dir():
            self._respond(404, f"No such run directory: {run_id}")
            return

        result_files = list(run_dir.glob("*/*.json"))
        if not result_files:
            self._respond(400, f"{run_id} has no completed results to build on.")
            return

        versions = set()
        for path in result_files:
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            if record.get("prompt_version"):
                versions.add(record["prompt_version"])
        if len(versions) != 1:
            self._respond(400, f"{run_id} tested {len(versions)} distinct prompt version(s) "
                                f"({', '.join(sorted(versions)) or 'none'}) — expected exactly one to roll "
                                f"back to unambiguously.")
            return
        version = next(iter(versions))

        version_file = PROMPT_VERSIONS_DIR / f"{version}.txt"
        if not version_file.is_file():
            self._respond(404, f"{run_id}'s prompt version {version} has no saved file "
                                f"({version_file.name}) — can't roll CURRENT back to it.")
            return

        if _already_running():
            self._respond(409, "An auto-optimize search is currently running — stop it before changing "
                                "the baseline it would resume from.")
            return

        (PROMPT_VERSIONS_DIR / "CURRENT").write_text(version + "\n", encoding="utf-8")

        prior_prefix = None
        if STATE_PATH.exists():
            try:
                prior_prefix = json.loads(STATE_PATH.read_text(encoding="utf-8")).get("run_id_prefix")
            except (json.JSONDecodeError, OSError):
                prior_prefix = None

        STATE_PATH.write_text(json.dumps({
            "baseline_run": run_id,
            "current_run_id": run_id,
            "prompt_version": version,
            "round": 0,
            "rounds_total": 0,
            "status": "manually_reset",
            "error_detail": None,
            "run_id_prefix": prior_prefix,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }, indent=2), encoding="utf-8")

        _regenerate_index()
        self._respond(200, f"Baseline reset: current prompt version is now {version}, and the next "
                            f"\"Launch more rounds\" will continue from {run_id}.")

    def _wants_json(self) -> bool:
        # The landing page's launch form submits via fetch() with this
        # header so it can show the result as a JS dialog instead of
        # navigating to a whole separate page for a one-line status
        # message; anything else (a bare curl, a browser with JS off)
        # still gets a normal HTML page back.
        return "application/json" in self.headers.get("Accept", "")

    def _respond(self, status: int, message: str, redirect_to: str = "/") -> None:
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
            self.send_header("Location", redirect_to)
            self.end_headers()
            return
        self._respond_html(status, f"<pre>{html.escape(message)}</pre><p><a href=\"{redirect_to}\">Back</a></p>")

    def _respond_html(self, status: int, body: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))


def _ensure_scrape_page_exists() -> None:
    """scrape.html is normally (re)written by run_scrape_batch.py's own
    _save_state() while a batch is actually running — between batches
    nothing ever touches it again, which used to mean a `git pull` +
    service restart to pick up a scrape_report.py template change had no
    visible effect until the next real scrape ran: confusing enough, live,
    that it's worth this comment. So this now unconditionally re-renders
    scrape.html from whatever .scrape_state.json currently holds (a no-op
    on the state itself — render_html() is a pure function of it — so this
    can never lose real progress, it just re-applies the current template
    code to it) every time the service starts, i.e. every deploy. A
    droplet where no batch has ever run has no state file, so this
    correctly falls back to an empty/placeholder render, same as before."""
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    state = {}
    if SCRAPE_STATE_PATH.exists():
        try:
            state = json.loads(SCRAPE_STATE_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            state = {}
    (RUNS_DIR / "scrape.html").write_text(scrape_report.render_html(state), encoding="utf-8")


def _ensure_home_page_exists() -> None:
    """index.html is the actual dashboard home now (see home_report.py's
    docstring for why), written alongside optimizer.html by
    eval_harness.py's generate_index(). Re-running that at every service
    start (not just when index.html happens to be missing) means a deploy
    that changes home_report.py/index_report.py's templates is visible
    immediately, the same fix as _ensure_scrape_page_exists() above and
    for the identical reason — this uses the real, authoritative
    regeneration path (_regenerate_index(), already used after every
    stop/delete/rerun action) rather than a separate reimplementation that
    would have to duplicate its run-counting logic to avoid regressing the
    displayed count back to zero on every restart."""
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    _regenerate_index()


def main() -> None:
    _ensure_scrape_page_exists()
    _ensure_home_page_exists()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Serving {RUNS_DIR} on http://127.0.0.1:{PORT} "
          f"(static files + POST /launch-auto-optimize, /delete-run, /rerun-run, /set-current-version, "
          f"/launch-scrape, /stop-scrape) — scraper progress at /scrape.html")
    server.serve_forever()


if __name__ == "__main__":
    main()
