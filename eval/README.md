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

Per-article detail — full generation output, every validator issue, every
judge score/issue — lives in `eval/runs/<run-id>/<model>/<article-id>.json`
if you need to see *why* a model scored the way it did rather than just the
aggregate.

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
