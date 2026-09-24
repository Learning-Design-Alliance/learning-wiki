# Pre-extractor test

**The question:** is it worth updating the droplet extractor (GLM 5.3 Flash, tuned over 130
prompt versions) to the new inclusion criteria and fields? Or should extraction move into a
Claude Code session, where Opus subagents run in parallel with tools?

## Arms

| arm | what | run id |
|---|---|---|
| `glm-v99` | GLM 5.3 Flash on CURRENT: the droplet as it runs today | `pxt-glm-v99` |
| `glm-v130` | the same model on v130: new criteria, not yet tuned | `pxt-glm-v130` |
| `opus-v130` | Opus 5.5 via OpenRouter, one call, no tools | `pxt-opus55-v130` |
| `agent` | a Claude Code subagent (Opus 5.5) on v130, with the whole article, Crossref, the wiki and a quote self-check | `pxt-agent-opus55` |

Each comparison isolates one change: `glm-v130` against `glm-v99` is the criteria change,
`opus-v130` against `glm-v130` is the model, and `agent` against `opus-v130` is the tools.

## Corpus: `manifest.json`, 19 articles

- **benchmark (9):** the fetchable part of `eval/corpus/manifest.json`. Every prompt version
  was tuned on these, so they flatter GLM.
- **holdout (8):** ERIC articles from `discover_articles.py` that no arm has seen. The
  decision rule reads only these.
- **reject-probe (2):** PMC hits that are not about learning. Under `INCLUSION.md` the right
  answer is to reject them. The headless contract has no way to reject a source.

## Scoring

The scoring reuses code this repo already trusts: `validator.py`, the `judge.py` judges (GPT
and Gemini, so no Anthropic judge scores an Anthropic arm), and `classify_doi`. It adds a
substring check on every `source_quote`. The decision rule is written in
`scripts/eval/pre_extractor_test.py`, before any result was read.

## Running it

```bash
# headless arms (needs an OpenRouter key WITH credit, ~$6 total)
eval/pre-extractor-test/run_headless.sh

# agent arm: prepare task folders, run one subagent per folder
# (each reads TASK.md and writes output.json), then record each one
python3 -m scripts.eval.agent_arm prepare --run-id pxt-agent-opus55
python3 -m scripts.eval.agent_arm record --run-id pxt-agent-opus55 --article <id> \
    --wall-s <s> --total-tokens <n> --tool-uses <n> --judges gpt gemini

python3 -m scripts.eval.pre_extractor_test     # -> REPORT.md
```

Per-article records land in `eval/runs/pxt-*`, which is gitignored like every other run.
`REPORT.md` is committed.
