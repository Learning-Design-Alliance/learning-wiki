# OpenRouter ingestion eval harness

Test infrastructure for answering one question before building the real
scrape-and-ingest pipeline: **which OpenRouter model(s) are worth running at
scale, and is the quality increase from a bigger model worth its cost
increase?** It measures cost, speed, and quality (structural completeness +
LLM-judged faithfulness) for a fixed 10-article corpus, and is meant to be
rerun as often as needed — after a prompt change, before scaling from 10
articles to the first real batch, or when a new open-weight model ships.

This harness does **not** write to the real wiki (`claims/`, `principles/`,
etc.). Every generated page lives as structured JSON under `eval/runs/<run-id>/`
until you're satisfied with a model's numbers — see "From eval to a real
batch" below for the next step once you are.

**Running a batch that takes more than an hour or two?** Don't tie up your
laptop for it — see [deploy/README.md](../deploy/README.md) to run this
unattended on a cheap DigitalOcean droplet instead, with automatic resume on
crash/reboot.

## Setup

```bash
pip install -r requirements-eval.txt

export OPENROUTER_API_KEY=...      # https://openrouter.ai/keys
export ANTHROPIC_API_KEY=...       # or `ant auth login` — used for the Opus judge
export OPENAI_API_KEY=...          # used for the GPT judge
export EVAL_HARNESS_CONTACT_EMAIL=you@example.org   # sent in the User-Agent to arXiv/ERIC/NCBI
```

`EVAL_HARNESS_CONTACT_EMAIL` isn't optional politeness — NCBI's usage
guidelines specifically ask automated clients to identify a contact so they
can reach you before blocking your IP if a batch misbehaves. Every fetch also
goes through a robots.txt + rate-limit check (`scripts/eval/compliance.py`)
before it hits the network — see [SOURCES.md](SOURCES.md) for what each
source (arXiv/ERIC/PMC) actually allows, why PMC is fetched through the
BioC API instead of scraping article pages, and which official bulk-data
channels (or Kaggle/Hugging Face mirrors) to switch to once a batch grows
past a couple hundred articles.

Before spending any money, confirm the corpus still resolves — websites
reorganize, ERIC/PMC ids don't move but URLs occasionally do:

```bash
python3 -m scripts.eval.fetch_article
```

This fetches and caches all 10 articles' full text to `eval/corpus/cache/`
(gitignored — full article text isn't something to commit) and reports any
dead link. Fix `eval/corpus/manifest.json` before proceeding if anything fails.

## Choosing models

`eval_harness.py` takes any OpenRouter model slug. To see whether a bigger
model's quality gain is worth its cost, run a spread rather than one model —
e.g. a cheap MoE model, a mid-size dense model, and a flagship, so the report
shows a real cost/quality curve instead of two similarly-priced points:

```bash
python3 scripts/eval_harness.py run \
    --models \
        qwen/qwen3-30b-a3b \
        google/gemma-3-27b-it \
        qwen/qwen3-235b-a22b \
    --judges opus gpt
```

Verify slugs against <https://openrouter.ai/models> first — OpenRouter's
catalog and pricing change over time and this list will go stale.

## What gets measured

For each (model, article) pair:

1. **Generation** — the model reads the article and returns one JSON object
   describing every claim/principle/element/pattern/strategy/theory
   contribution (`scripts/eval/prompts.py` — a condensed version of
   `.claude/skills/ingest-article.md`'s instructions, adapted for a model
   without tool access). Latency, token usage, and cost are recorded — cost
   comes from OpenRouter's `/generation` stats endpoint when it's settled by
   the time we ask, falling back to the `/models` list-price table otherwise
   (`generation.cost_source` tells you which).
2. **Structural validation** (`scripts/eval/validator.py`) — a deterministic,
   free check: are all required fields present, well-typed, and internally
   consistent (e.g. every subclaim's `evidence_ref` actually matches an
   evidence anchor; every cross-linked slug is real or a sibling
   contribution, not invented)? This is the "did it accurately complete all
   required fields" half of quality — no LLM involved, so it's free and
   exactly reproducible.
3. **LLM judging** (`scripts/eval/judge.py`) — Claude Opus 5 and/or an OpenAI
   model read the *original article* plus the extraction and score
   faithfulness, accuracy, completeness, and schema fit 1-5, flagging any
   fabricated citation or finding. This is the half a structural check can't
   catch: does the content actually say what the article says?

## Reading the report

```bash
python3 scripts/eval_harness.py report --run-id <run-id>
```

Writes `eval/runs/<run-id>/report.md` (human-readable table) and
`summary.csv` (for spreadsheet/chart use), aggregating per model:
total generation cost, average latency, validator pass rate, average
completeness, average judge score, and — the number that actually answers
"is it worth it" — **cost per validated article**. A cheap model with a
70% pass rate and $0.002/article beats a flagship at 95% and $0.02/article
if 70% good pages plus a quick human triage is less total cost than getting
30% fewer pages to fix by hand; run the corpus with both to find out.

The same command also writes `report.html` — a visual dashboard (Summary /
Cost vs. quality / Per-model metrics / Failure patterns / Per-article detail
tabs) that auto-refreshes while a batch is running. On a droplet, see
[deploy/README.md](../deploy/README.md) for `live_view.sh`, which serves this
over an SSH tunnel so you can watch it update live instead of re-running
`report` and re-opening the file by hand.

**`eval/runs/index.html`** — the landing page at the root of that same
server (`http://localhost:8080/`) — lists every run that exists, each with
its live done/pending progress, avg judge score, total cost, and avg
latency so far, plus trend charts (quality, cost/article, latency) across
every run over time, one line per model, so "is the whole experiment
trending in the right direction" is a glance instead of opening N
dashboards. It's regenerated automatically every time any run's own report
regenerates (same live-while-running guarantee), or on demand:

```bash
python3 scripts/eval_harness.py index
```

Priority order matters here, not a weighted blend: the **"Best prompt
version per model"** leaderboard and **"Full trajectory by model"** tables
rank every result by validator pass rate first, completeness second — both
need to reach 100% — and only then by judge score (as close to 5/5 as
possible); cost and latency are shown muted, for context, never as part of
the ranking. This is a run's own numbers per model, never a cross-model
average — blending several unrelated models into one mean answers "did the
batch move," not "did this specific model actually get better."

On a droplet, the same page also has a **"Launch N more rounds"** button
(see [deploy/README.md](../deploy/README.md)) — the whole point of
`eval-harness-web.service` being a small custom server (`dashboard_server.py`)
rather than a plain static file server. It continues from wherever the
last `auto-optimize` search left off, so you don't need to SSH in and
recall a run-id every time you want to keep going.

A **model queue** panel sits above the tabs on every load — one row per
configured model showing done/error/pending counts against the total article
count, and a Done / Running / Queued badge (models run to completion one at a
time, in the order given to `--models`, so only the first incomplete model is
ever "running"; everything after it is still queued, not stuck). This is what
answers "is the batch done yet" and "why does the dashboard only show 2 of 5
models" — the answer to the latter is almost always "the other 3 haven't
started yet," which the queue panel now shows directly instead of leaving you
to infer it.

For the same answer without opening a browser:

```bash
python3 scripts/eval_harness.py status --run-id <run-id> --models <...>
```

Omit `--run-id`/`--models` on a droplet and they default to what's configured
in `deploy/run-config.env`'s `RUN_ARGS`, so you don't have to retype the
model list to check progress on the batch that's actually running there.
Prints a per-model progress bar plus an overall done/errors/pending count.

Per-article detail — full generation output, every validator issue, every
judge score/issue — lives in `eval/runs/<run-id>/<model>/<article-id>.json`,
and is also reachable by clicking a row in the dashboard's "Per-article
detail" tab, if you need to see *why* a model scored the way it did rather
than just the aggregate.

## Comparing runs and projecting cost

```bash
python3 scripts/eval_harness.py compare --baseline <run-id> --candidate <run-id>
python3 scripts/eval_harness.py project-cost --run-id <run-id> --sizes 10000 100000 1000000
```

`compare` diffs two runs model-by-model (judge scores, validator pass rate,
failure-pattern keyword tallies) — the tool for "did changing the prompt/
validator actually move the numbers," not just "does it feel better."

`project-cost` extrapolates a run's *measured* $/article to hypothetical
corpus sizes, split into generation-only cost and generation + a spot-check
QA judge pass (default 5% of articles, not every one — see the module
docstring in `scripts/eval/cost_projection.py` for why 100% double-judging
isn't the right production assumption). The corpus-size scenarios are
brackets to reason with, not a prediction of the real target count.

## Self-correction retries (`--max-correction-attempts`)

`run`/`optimize`/`auto-optimize` all default to a single shot per article —
deliberately: the whole point of this harness is measuring how a model does
on its **first** attempt, since that's what actually differentiates models
and prompts. Silently retrying until something passes would erase that
signal and make every model look artificially perfect.

Opt in explicitly when what you want instead is "how close to 100% can this
model get with a bounded self-correction budget":

```bash
python3 scripts/eval_harness.py run --models <...> --max-correction-attempts 3
```

On a validator failure, the model is shown its own previous output plus the
exact structural issues it triggered (field, message, severity — the same
data the dashboard's Failure patterns tab shows) and asked for a corrected
replacement; this repeats up to N times or until it passes, whichever comes
first. Each result keeps **both** numbers: `initial_passed` (the pure
first-attempt result) and `validation.passed` (the final, post-correction
result that feeds `validator_pass_rate` everywhere else) — so a model that
needed 2 retries to reach 100% is visible as such, not indistinguishable
from one that passed cleanly. Cost is cumulative across every attempt actually
made, not just the first.

## Prompt versioning, trend history, and auto-optimization

The extraction prompt (`scripts/eval/prompts.py`) is versioned, not a single
hardcoded string — the text lives in `scripts/eval/prompt_versions/vN.txt`,
with a changelog and a ratcheted `CURRENT` pointer (advances only when a
version is confirmed to improve on its predecessor; a regressed experiment
stays saved on disk but never becomes the default). Every result record
stamps which version produced it.

```bash
python3 scripts/eval_harness.py run --models <...> --prompt-version v2   # pin a specific version; omit for current
python3 scripts/eval_harness.py history                                  # trend across every run, grouped by version
python3 scripts/eval_harness.py optimize --baseline-run <run-id> --iterations 3
```

`history` is the cross-run view `compare` doesn't give you — not "did this
one change help" but "are we actually trending upward across every test
batch so far."

`optimize` automates the propose → re-run → compare → keep-or-reject loop:
it hands Claude Opus the baseline run's exact failure data (the same
validator issues and judge complaints shown on the dashboard's Failure
patterns tab — not a hand-picked summary) and asks for a revised prompt
addressing those specific patterns, saves it as a new version, re-runs it
against the same models and articles as the baseline, and only adopts it as
the new default if `compare`'s average judge-score delta clears
`--min-improvement` (default: any improvement at all). The loop stops the
moment a candidate doesn't improve, rather than continuing to spend on a
losing line — this costs real OpenRouter + Opus + judge money per iteration,
so `--iterations` is a hard cap, not a target to always hit. `optimize` is a
single lineage: one candidate at a time, tried in sequence.

## Running pairs in parallel

Every `run`/`optimize`/`auto-optimize` invocation takes `--concurrency N`
(default: 1, i.e. the original sequential behavior). Above 1, `(model,
article)` pairs are dispatched to a thread pool instead of run one at a
time — safe because each pair writes its own result file and the
OpenRouter/judge calls carry no shared state. Pick a concurrency that's
comfortable for your OpenRouter account's rate limits; there's no
provider-aware throttling beyond the existing 429 retry/backoff in
`openrouter_client.py`.

## Self-driving multi-candidate search (`auto-optimize`)

```bash
python3 scripts/eval_harness.py auto-optimize --baseline-run <run-id> \
    --rounds 3 --candidates-per-round 6 --concurrency 6 --time-budget-minutes 60
```

Where `optimize` tries one candidate at a time, `auto-optimize` is the
breadth-first version: each round proposes several *diverse* candidate
revisions in parallel — one per failure "lens" in `scripts/eval/
optimizer.py`'s `LENSES` (fabrication, omission, duplication, schema,
consolidate, general) — rather than one linear rephrasing, runs every
candidate's full batch concurrently (both across candidates and across
`(model, article)` pairs within each), and adopts the single best one that
clears `--min-improvement` as the next round's baseline. A round where
nothing improves stops the loop, same as `optimize`.

It's built to be started and left alone: it stops on `--rounds`,
`--time-budget-minutes` (checked between rounds, not mid-round — a round
already in flight finishes), or a non-improving round, whichever comes
first. After **every** round (not just at the end) it (re)writes
`eval/runs/auto-optimize-summary-<baseline-run>.md` and its visual
companion, `...html` — a diverging bar per candidate (green = improved,
red = regressed vs. that round's baseline, &#9733; marks the adopted one),
clickable through to each candidate's own full dashboard, plus the same
data as an accessible table — so it's a live view you can open mid-run, not
just a report available at the very end.

**Running it unattended on the droplet** (see
[deploy/README.md](../deploy/README.md) for the base setup): edit
`deploy/auto-optimize-config.env` (git-tracked, same pattern as
`run-config.env`) to set `--baseline-run` and the search parameters, commit,
`git pull` on the droplet, then:

```bash
sudo systemctl start eval-auto-optimize
journalctl -u eval-auto-optimize -f          # watch it live
```

Unlike `eval-harness.service`, this unit is **not** enabled at boot and has
**no** `Restart=` — it's a one-off bounded search you trigger by hand, not
an always-on service; a crash or completion doesn't relaunch it and keep
spending API budget unattended. Each candidate gets its own run directory
under `eval/runs/`, browsable the same way as any other run (via
`live_view.sh` or the plain directory listing at `http://localhost:8080/`
through the SSH tunnel) while the search is still in progress.

This spends real money faster than `optimize` — `--candidates-per-round 6`
means 6x the generation + judge cost of a single round, on top of 6 parallel
Opus calls for the proposals themselves. Start with a smaller
`--candidates-per-round` and shorter `--time-budget-minutes` the first time
to see real cost/round before committing to a full hour.

## Repeating the test

Everything is cached per (run, model, article), so a `run` is resumable —
rerunning the same command skips pairs that already have a result file
(`--overwrite` forces regeneration). Two common cases:

- **You tweaked the judge rubric or want a second judge's opinion, but don't
  want to re-pay for generation:**
  ```bash
  python3 scripts/eval_harness.py spotcheck --run-id <run-id> --judges opus gpt
  ```
  Re-parses and re-validates the cached raw output and re-runs judges only —
  zero OpenRouter cost.
- **You tweaked the generation prompt and need fresh output:** run `run`
  again with `--overwrite` (full generation cost again, as expected).

## From eval to a real batch

Once a model's numbers look good enough here, the same
`scripts/eval/{prompts,openrouter_client,validator}.py` modules are meant to
be reused (not rewritten) by a real batch-ingest script that renders the
validated JSON into actual OKF markdown pages under `claims/`, `principles/`,
etc. and opens a PR per source, the same way `.claude/skills/ingest-article.md`
does today — that script doesn't exist yet; build it against whichever
model(s) this harness recommends, and keep running `eval_harness.py` against
new manifest entries as new models or prompt versions show up, so cost/quality
tradeoffs stay visible instead of assumed.
