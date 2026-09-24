# Pre-extractor test

**The question:** is it worth updating the droplet extractor (GLM 5.3 Flash, tuned over 130
prompt versions) to the new inclusion criteria and fields? Or should extraction move into a
Claude Code session, where Opus subagents run in parallel with tools?

## Arms

| arm | what | run id |
|---|---|---|
| `glm-v99` | GLM 5.3 Flash on CURRENT: the droplet as it runs today | `pxt-glm-v99` |
| `glm-v124` | the same model on v124, the GLM-tuned prompt with the best pass rate (8/10 on the droplet) | `pxt-glm-v124` |
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

## Result, 2026-09-24

All five arms ran; the numbers are in `REPORT.md`. On the holdout:

| arm | validator pass | GPT judge | quotes not in article | study_record | rejected the probes | $/article |
|---|---|---|---|---|---|---|
| glm-v99 | 12% | 2.41 | 18% | 0/8 | no | $0.002 |
| **glm-v124** | **88%** | **4.19** | **3%** | **0/8** | **no (7 contributions each)** | **$0.003** |
| glm-v130 | 0% | 2.84 | 80% | 0/8 | no | $0.002 |
| opus-v130 | 62% | 4.41 | 3% | 4/8 | no (12–13 each) | $0.34 |
| agent | 100% | 4.22 | 0% | 4/8 | **yes** | $0.46–0.98 |

**The rule's answer: glm-v124, opus-v130 and agent tie on quality, and glm-v124 is by far
the cheapest.** The 10%-pass failures belong to the v99 lineage, not to GLM. v99 is what
CURRENT points to (the ratchet ranks by judge score), and v130 was built on it through
v128/v129. So v130's collapse says nothing about whether GLM can follow the new criteria.

**What v124 lacks is the new contract, not the quality**: no `study_record`, no way to
reject a source, and the pre-INCLUSION.md claim floor. So "update the droplet" means porting
v128–v130's three changes (the null `i`, the study record, the inclusion rules) onto v124
rather than onto v99, then rerunning this test. That is a ~$0.10 experiment.

Caveats: the Gemini judge scored nearly everything 5.0, so it barely separates the arms;
read the GPT column. The judges see at most 60k characters of each article. Eight holdout
articles is a small sample.

**Operational notes from the agent arm.** The parallel agents shared one scratchpad, so
their helper scripts collided; `TASK.md` now gives each agent its own folder. And the
first ingest of the agents' output found three pipeline bugs, all now fixed:
`enrich.verify_page_citations` matched the frontmatter `resource:` line (no title) and
recorded 168 correct DOIs as `wrong_paper`; `ingest_extractions` linked cross-type
siblings into the wrong folder (105 broken links); and it recorded an extractor's own
E2 rejection as the failed-run code `no-contributions-extracted`.
