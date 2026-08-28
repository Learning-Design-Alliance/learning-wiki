#!/usr/bin/env python3
"""
run_scrape_batch.py — Orchestrates one full "scrape" batch: discover_articles.py
then fetch_article.py's prefetch-verify, as a single long-running process so the
web dashboard can launch/monitor/stop it exactly like it already does for
auto-optimize (eval_harness.py's cmd_auto_optimize) — one subprocess, one pid to
kill, one console log tailed live, one JSON state file that
scripts/eval/scrape_report.py renders into eval/runs/scrape.html.

Usage:
    python3 scripts/run_scrape_batch.py --pmc 200 --eric 700 --arxiv 0 \
        [--arxiv-snapshot PATH] --out eval/corpus/manifest_real.json [--label NAME]

Discovery runs in-process (calling discover_articles.py's own functions
directly, not as a subprocess) so this stays one pid with one continuous
console log. Prefetch-verify is reimplemented here as a per-entry loop
(rather than shelling out to fetch_article.py's own main()) purely so
progress can be recorded after every article instead of only at the end —
it calls the exact same fetch_article.fetch_article_text() every other
caller in this project uses, nothing source-specific is duplicated.
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(WIKI_ROOT))

from scripts.eval import discover_articles, fetch_article, scrape_report

RUNS_DIR = WIKI_ROOT / "eval" / "runs"
SCRAPE_STATE_PATH = RUNS_DIR / ".scrape_state.json"
SCRAPE_HISTORY_PATH = RUNS_DIR / ".scrape_history.json"
SCRAPE_CONSOLE_LOG_PATH = RUNS_DIR / ".scrape_console.log"
SCRAPE_REPORT_PATH = RUNS_DIR / "scrape.html"
MAX_HISTORY = 20

# entry["source"] values differ from the CLI/config vocabulary for PMC only
# (search_pmc() sets "pubmed", to match the existing benchmark manifest.json
# convention) — see discover_articles.py.
_SOURCE_KEY_TO_ENTRY_SOURCE = {"pmc": "pubmed", "eric": "eric", "arxiv": "arxiv"}


class _ConsoleTee:
    """Same pattern as eval_harness.py's _ConsoleTee (see its docstring) —
    duplicated rather than imported so this script stays runnable standalone
    without pulling in eval_harness.py's much larger module. Duplicates
    every write to the real stream AND a fixed log file
    (SCRAPE_CONSOLE_LOG_PATH), so the dashboard can show live console
    output regardless of how this was launched (the web button, a bare CLI
    invocation, ...)."""

    def __init__(self, stream, log_file):
        self._stream = stream
        self._log_file = log_file

    def write(self, s):
        self._stream.write(s)
        self._log_file.write(s)
        self._log_file.flush()

    def flush(self):
        self._stream.flush()
        self._log_file.flush()

    def isatty(self):
        return False


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_history() -> list:
    if not SCRAPE_HISTORY_PATH.exists():
        return []
    try:
        return json.loads(SCRAPE_HISTORY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _trim_state_for_history(state: dict) -> dict:
    """Drops the per-article fetch.results list (can be hundreds of entries)
    before archiving — a past run's aggregate ok/fail counts are what a
    history table needs, not the full per-article detail, which would make
    .scrape_history.json grow unboundedly."""
    trimmed = dict(state)
    fetch = dict(trimmed.get("fetch") or {})
    fetch.pop("results", None)
    trimmed["fetch"] = fetch
    trimmed.pop("pid", None)
    return trimmed


def _archive_current_state_if_any() -> None:
    """Called once, before a new batch's first _save_state() overwrites
    .scrape_state.json — .scrape_state.json is a singleton (today's whole
    "previous runs" gap: there was no history at all, just whatever the
    last batch left behind), so this is the one hook point that preserves
    it: whatever the previous batch's last-recorded state was (completed,
    errored, or killed mid-run and never updated again) gets appended to
    .scrape_history.json right before it would otherwise be lost."""
    if not SCRAPE_STATE_PATH.exists():
        return
    try:
        prev_state = json.loads(SCRAPE_STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return
    history = _load_history()
    history.append(_trim_state_for_history(prev_state))
    history = history[-MAX_HISTORY:]
    SCRAPE_HISTORY_PATH.write_text(json.dumps(history, indent=2), encoding="utf-8")


def _save_state(state: dict) -> None:
    state["updated_at"] = _now()
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    SCRAPE_STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    SCRAPE_REPORT_PATH.write_text(scrape_report.render_html(state, history=_load_history()), encoding="utf-8")


def _run_chained_step(cmd: list, log_path: Path) -> int:
    """Runs a generation/ingestion step as a real subprocess (not an
    in-process import of eval_harness.py/ingest_extractions.py — both are
    large modules with their own sys.path and secrets-loading side effects
    better kept isolated), writing its stdout/stderr straight into the same
    console log file _ConsoleTee already tees this process's own output
    into, so the dashboard's live console shows generation/ingestion
    progress with no extra plumbing. Returns the subprocess's exit code."""
    with open(log_path, "a", encoding="utf-8") as f:
        proc = subprocess.run(cmd, cwd=str(WIKI_ROOT), stdout=f, stderr=subprocess.STDOUT)
    return proc.returncode


def run(args) -> None:
    _archive_current_state_if_any()

    config = {
        "pmc": args.pmc, "eric": args.eric, "arxiv": args.arxiv,
        "arxiv_snapshot": args.arxiv_snapshot, "out": args.out,
        "model": args.model, "prompt_version": args.prompt_version,
    }
    state = {
        "label": args.label,
        "status": "discovering",
        "config": config,
        "discover": {"by_source": {}, "topics_seeded": 0, "done": False},
        "fetch": {"total": 0, "ok": 0, "fail": 0, "done": False, "results": []},
        "pid": os.getpid(),
        "started_at": _now(),
        "finished_at": None,
        "error_detail": None,
    }
    _save_state(state)

    print(f"=== scrape batch {args.label!r} starting: pmc={args.pmc} eric={args.eric} "
          f"arxiv={args.arxiv} out={args.out} ===", flush=True)

    existing_ids = discover_articles.load_excluded_ids()
    print(f"Excluding {len(existing_ids)} already-known article id(s) "
          f"(benchmark manifest + processed-articles registry).", flush=True)

    topics = discover_articles.topics_from_wiki()
    state["discover"]["topics_seeded"] = len(topics)
    _save_state(state)

    targets = {}
    if args.pmc > 0:
        targets["pmc"] = args.pmc
    if args.eric > 0:
        targets["eric"] = args.eric

    manifest = []
    if targets:
        manifest = discover_articles.build_manifest(targets, topics, existing_ids,
                                                      use_cache=not args.refresh_cache)
        for source, target in targets.items():
            entry_source = _SOURCE_KEY_TO_ENTRY_SOURCE[source]
            found = sum(1 for e in manifest if e["source"] == entry_source)
            state["discover"]["by_source"][source] = {"found": found, "target": target}
        _save_state(state)

    if args.arxiv > 0:
        # Always resolved to a local snapshot file — either the explicit
        # --arxiv-snapshot path, or an on-demand kagglehub download/cache
        # hit — never the live API; see discover_articles.resolve_arxiv_snapshot().
        print(f"Resolving arXiv snapshot (explicit path: {args.arxiv_snapshot or '(none — using kagglehub)'})...",
              flush=True)
        snapshot_path = discover_articles.resolve_arxiv_snapshot(args.arxiv_snapshot)
        print(f"Using arXiv snapshot: {snapshot_path}", flush=True)
        arxiv_entries = discover_articles.build_arxiv_manifest_from_snapshot(
            snapshot_path, topics, args.arxiv,
            existing_ids | {e["id"] for e in manifest},
        )
        manifest.extend(arxiv_entries)
        state["discover"]["by_source"]["arxiv"] = {"found": len(arxiv_entries), "target": args.arxiv}
        _save_state(state)

    state["discover"]["done"] = True
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({"articles": manifest}, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} candidate(s) to {out_path}.", flush=True)

    state["status"] = "fetching"
    state["fetch"]["total"] = len(manifest)
    _save_state(state)

    for entry in manifest:
        try:
            text = fetch_article.fetch_article_text(entry)
            state["fetch"]["ok"] += 1
            state["fetch"]["results"].append({"id": entry["id"], "ok": True,
                                               "chars_or_detail": f"{len(text):,} chars"})
            print(f"[OK]   {entry['id']:20s} {len(text):>8,} chars — {entry['title'][:60]}", flush=True)
        except Exception as e:  # noqa: BLE001 - one bad article must not abort the whole batch
            state["fetch"]["fail"] += 1
            state["fetch"]["results"].append({"id": entry["id"], "ok": False, "chars_or_detail": str(e)})
            print(f"[FAIL] {entry['id']:20s} {e}", flush=True)
        _save_state(state)

    state["fetch"]["done"] = True
    print(f"=== scrape batch {args.label!r} done: {state['fetch']['ok']}/{state['fetch']['total']} "
          f"fetched successfully ===", flush=True)

    if args.model:
        state["status"] = "generating"
        _save_state(state)
        print(f"\n=== generating with {args.model} (prompt version: "
              f"{args.prompt_version or 'CURRENT'}) ===", flush=True)
        gen_cmd = [sys.executable, "-u", "scripts/eval_harness.py", "run",
                   "--models", args.model, "--run-id", args.label,
                   "--manifest", args.out, "--max-tokens", "24000",
                   "--judges", "--overwrite"]
        if args.prompt_version:
            gen_cmd += ["--prompt-version", args.prompt_version]
        gen_rc = _run_chained_step(gen_cmd, SCRAPE_CONSOLE_LOG_PATH)
        if gen_rc != 0:
            state["status"] = "error"
            state["error_detail"] = f"Generation step exited {gen_rc} — see console log."
            state["finished_at"] = _now()
            _save_state(state)
            print(f"=== scrape batch {args.label!r} stopped: generation failed (exit {gen_rc}) ===", flush=True)
            return

        state["status"] = "ingesting"
        _save_state(state)
        print(f"\n=== ingesting {args.label!r} results into wiki pages ===", flush=True)
        ingest_cmd = [sys.executable, "-u", "scripts/ingest_extractions.py",
                      "--run-id", args.label, "--model", args.model, "--by", "claude/unspecified"]
        ingest_rc = _run_chained_step(ingest_cmd, SCRAPE_CONSOLE_LOG_PATH)
        if ingest_rc != 0:
            state["status"] = "error"
            state["error_detail"] = f"Ingest step exited {ingest_rc} — see console log."
            state["finished_at"] = _now()
            _save_state(state)
            print(f"=== scrape batch {args.label!r} stopped: ingest failed (exit {ingest_rc}) ===", flush=True)
            return

    state["status"] = "completed"
    state["finished_at"] = _now()
    _save_state(state)
    print(f"=== scrape batch {args.label!r} fully complete "
          f"({'discover+fetch+generate+ingest' if args.model else 'discover+fetch'} done) ===", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pmc", type=int, default=discover_articles.DEFAULT_TARGETS["pmc"])
    parser.add_argument("--eric", type=int, default=discover_articles.DEFAULT_TARGETS["eric"])
    parser.add_argument("--arxiv", type=int, default=discover_articles.DEFAULT_TARGETS["arxiv"])
    parser.add_argument("--arxiv-snapshot", default=None)
    parser.add_argument("--out", default=str(discover_articles.EVAL_ROOT / "corpus" / "manifest_bulk.json"))
    parser.add_argument("--label", default=None)
    parser.add_argument("--model", default=None,
                         help="OpenRouter model slug — if given, chains generation (--judges none, "
                              "--max-tokens 24000, --overwrite) and then ingest_extractions.py "
                              "straight after a successful discover+fetch, all under this same batch's "
                              "label as the run-id. Omit to keep this a discover+fetch-only batch, "
                              "same as before this option existed.")
    parser.add_argument("--prompt-version", default=None,
                         help="Only meaningful with --model. Omit to use whatever CURRENT is at run time.")
    parser.add_argument("--refresh-cache", action="store_true",
                         help="Ignore eval/corpus/.discovery_cache.json's cached PMC/ERIC search results "
                              "and re-query live instead — needed to actually exercise a change to "
                              "search_pmc()/search_eric() (e.g. a new filter), since a cache hit skips "
                              "calling them at all. Off by default so repeat batches stay fast/cheap.")
    args = parser.parse_args()
    if not args.label:
        args.label = f"scrape-{int(time.time())}"

    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    console_log_file = open(SCRAPE_CONSOLE_LOG_PATH, "w", encoding="utf-8")
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    sys.stdout = _ConsoleTee(orig_stdout, console_log_file)
    sys.stderr = _ConsoleTee(orig_stderr, console_log_file)
    try:
        run(args)
    except Exception as e:
        state = {}
        if SCRAPE_STATE_PATH.exists():
            try:
                state = json.loads(SCRAPE_STATE_PATH.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                state = {}
        state["status"] = "error"
        state["error_detail"] = f"{type(e).__name__}: {e}"
        state["finished_at"] = _now()
        _save_state(state)
        raise
    finally:
        sys.stdout, sys.stderr = orig_stdout, orig_stderr
        console_log_file.close()


if __name__ == "__main__":
    main()
