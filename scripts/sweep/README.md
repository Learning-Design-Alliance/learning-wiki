# The source sweep driver

The sweep reads every article the screening passed (`eval/screening/`, see
`scripts/screen_sources.py`) in batches of 120 (`SWEEP_TAKE` overrides; 80 until 2026-11-07, raised so the whole-wiki steps run once per 120 articles), through `scripts/run_scrape_batch.py`. These scripts
run it one batch at a time and stop after each batch for triage. They were committed on 2026-11-04,
after a container reset wiped the scratch copies along with the ignored queues and caches.

| File | What it does |
|---|---|
| `rebuild_queues.py` | Writes `eval/runs/queues/sweep-*.ndjson` from committed data: universe members, both models' screening votes, and the manifest. Run it on a fresh container. |
| `drive.sh` | Runs the next batch from the first queue with unsettled entries (PubMed Central, arXiv, ERIC, then split votes), writes `ATTENTION` and waits until it is removed. |
| `start.sh` | Starts `drive.sh` detached from the shell. |
| `watch.sh` | Exits with a `HOLD` line when `ATTENTION` appears, so a waiting agent session is woken. |

State lives in `$SWEEP_DIR` (default `eval/runs/sweep/`, ignored): `drive.log`, one log per batch,
`ATTENTION`, the per-tranche batch counters and `PAUSE`.

## On a fresh container

```bash
python3 -m pip install -r requirements-eval.txt
python3 scripts/sweep/rebuild_queues.py
bash scripts/sweep/start.sh
```

Set `counter-<tranche>` in `$SWEEP_DIR` to the last batch number used, or labels restart at 1.

## At a hold

`ATTENTION` names the batch and its log, and adds `batch-failed` or `short-batch`. A short batch is
one that generated from under 90% of the articles it took, usually because the proxy moved
mid-batch. Triage follows CLAUDE.md (the batch's own health and attention lines, the regen chain,
lint 0). Then commit, merge main with `scripts/merge_main.py`, push, remove `ATTENTION`, and open
the PR. The driver does not commit. Touch `$SWEEP_DIR/PAUSE` to stop it after the current batch.

After a container restart the proxy port changes, and a running driver keeps the old one. Compare
`/proc/<pid>/environ` with `$HTTPS_PROXY`, kill the driver tree by pid (never `pkill -f`) and
`start.sh` again. Finish a batch interrupted after ingest with `run_scrape_batch.py --post-only`;
never run ingest again.
