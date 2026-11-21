---
type: claim
title: The reasoning model o1-preview with general prompting outperformed all GPT-4o prompting setups and Physics Olympiad participants on aggregated Olympiad problem scores, with very large to huge effect sizes
description: The reasoning model o1-preview with general prompting outperformed all GPT-4o prompting setups and Physics Olympiad participants on aggregated Olympiad problem scores, with very large to huge effect sizes
id: o1-preview-outperforms-gpt4o-and-olympiad-participants
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: tschisgale-2025
    resource: "https://doi.org/10.1103/6fmx-bsnl"
    title: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)"
    author: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P."
    q: 2
    i: 3
    kind: associational
    rigour: 2
---

# The reasoning model o1-preview with general prompting outperformed all GPT-4o prompting setups and Physics Olympiad participants on aggregated Olympiad problem scores, with very large to huge effect sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` o1-preview with general prompting substantially outperformed all other tested LLM setups and the Physics Olympiad participants, with very large to huge effect sizes (d = 2.28 versus participants). [→ Tschisgale 2025](#tschisgale-2025)

## Evidence

### Tschisgale 2025

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i3` · `associational · r2`

Simulated exam-level comparison: 600 LLM solutions to six Olympiad problems were scored with official schemes, and 100,000 randomly combined six-problem sets per setup were compared using Welch's t-tests and Cohen's d. The table reports d = 2.28 for o1-preview versus participants, described as "very large to huge effect sizes".

> "the o1-preview reasoning model in combination with general prompting substantially outperforms all other tested LLM setups and the Physics Olympiad participants, with very large to huge effect sizes."

## Discussion


## Related Claims
- [Physics Olympiad participants scored significantly worse than all tested GPT-4o prompting setups on aggregated Olympiad problems, with large effect sizes](gpt4o-outperforms-olympiad-participants.md) — related
- [On the Helicopter on Mars problem, none of the LLM-generated solutions received full credit although some student solutions did, despite o1-preview's highly consistent high scores](no-llm-full-credit-helicopter-problem.md) — a narrower finding that bears on this claim
- [Score variance differed markedly: Olympiad participants' scores showed substantially higher variance than LLM scores, with o1-preview's scores the most narrowly distributed](score-variance-students-higher-than-llms.md) — related
- [Prompting technique had little effect on GPT-4o's Olympiad problem-solving performance, with no or only small effect sizes among general, CoT, and single-shot CoT prompting](prompting-little-effect-gpt4o-physics-problems.md) — related
