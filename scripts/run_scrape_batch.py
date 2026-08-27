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
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(WIKI_ROOT))

from scripts.eval import discover_articles, fetch_article, scrape_report

RUNS_DIR = WIKI_ROOT / "eval" / "runs"
SCRAPE_STATE_PATH = RUNS_DIR / ".scrape_state.json"
SCRAPE_CONSOLE_LOG_PATH = RUNS_DIR / ".scrape_console.log"
SCRAPE_REPORT_PATH = RUNS_DIR / "scrape.html"

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


def _save_state(state: dict) -> None:
    state["updated_at"] = _now()
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    SCRAPE_STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")
    SCRAPE_REPORT_PATH.write_text(scrape_report.render_html(state), encoding="utf-8")


def run(args) -> None:
    config = {
        "pmc": args.pmc, "eric": args.eric, "arxiv": args.arxiv,
        "arxiv_snapshot": args.arxiv_snapshot, "out": args.out,
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

    existing_manifest_path = discover_articles.EVAL_ROOT / "corpus" / "manifest.json"
    existing_ids = set()
    if existing_manifest_path.exists():
        existing = json.loads(existing_manifest_path.read_text(encoding="utf-8"))
        existing_entries = existing if isinstance(existing, list) else existing.get("articles", [])
        existing_ids = {e["id"] for e in existing_entries}

    topics = discover_articles.topics_from_wiki()
    state["discover"]["topics_seeded"] = len(topics)
    _save_state(state)

    targets = {}
    if args.pmc > 0:
        targets["pmc"] = args.pmc
    if args.eric > 0:
        targets["eric"] = args.eric
    if args.arxiv > 0 and not args.arxiv_snapshot:
        targets["arxiv"] = args.arxiv  # will correctly hit the live-API compliance block; see discover_articles.py

    manifest = []
    if targets:
        manifest = discover_articles.build_manifest(targets, topics, existing_ids)
        for source, target in targets.items():
            entry_source = _SOURCE_KEY_TO_ENTRY_SOURCE[source]
            found = sum(1 for e in manifest if e["source"] == entry_source)
            state["discover"]["by_source"][source] = {"found": found, "target": target}
        _save_state(state)

    if args.arxiv > 0 and args.arxiv_snapshot:
        arxiv_entries = discover_articles.build_arxiv_manifest_from_snapshot(
            Path(args.arxiv_snapshot), topics, args.arxiv,
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
    state["status"] = "completed"
    state["finished_at"] = _now()
    _save_state(state)
    print(f"=== scrape batch {args.label!r} done: {state['fetch']['ok']}/{state['fetch']['total']} "
          f"fetched successfully ===", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pmc", type=int, default=discover_articles.DEFAULT_TARGETS["pmc"])
    parser.add_argument("--eric", type=int, default=discover_articles.DEFAULT_TARGETS["eric"])
    parser.add_argument("--arxiv", type=int, default=discover_articles.DEFAULT_TARGETS["arxiv"])
    parser.add_argument("--arxiv-snapshot", default=None)
    parser.add_argument("--out", default=str(discover_articles.EVAL_ROOT / "corpus" / "manifest_bulk.json"))
    parser.add_argument("--label", default=None)
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
