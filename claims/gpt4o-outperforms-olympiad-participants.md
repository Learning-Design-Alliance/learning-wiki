---
type: claim
title: Physics Olympiad participants scored significantly worse than all tested GPT-4o prompting setups on aggregated Olympiad problems, with large effect sizes
description: Physics Olympiad participants scored significantly worse than all tested GPT-4o prompting setups on aggregated Olympiad problems, with large effect sizes
id: gpt4o-outperforms-olympiad-participants
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
    kind: causal
    rigour: 1
---

# Physics Olympiad participants scored significantly worse than all tested GPT-4o prompting setups on aggregated Olympiad problems, with large effect sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Physics Olympiad participants consistently performed worse than all tested GPT-4o setups irrespective of prompting technique, with large effect sizes (d = 0.87 to 1.25). [→ Tschisgale 2025](#tschisgale-2025)

## Evidence

### Tschisgale 2025

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i3` · `causal · r1`

Simulated exam-level analysis of scored solutions: GPT-4o under no, general, CoT, and single-shot CoT prompting was compared with Olympiad participants via Welch's t-tests on 100,000 sampled six-problem combinations; Table II reports Cohen's d of 0.87, 1.25, 1.17, and 1.19, i.e., "large effect sizes".

> "Moreover, Physics Olympiad participants consistently perform ed worse t han all tested GPT -4o setups, irrespective of the employed prompting technique, with large effect sizes."

## Discussion


## Related Claims
- [The reasoning model o1-preview with general prompting outperformed all GPT-4o prompting setups and Physics Olympiad participants on aggregated Olympiad problem scores, with very large to huge effect sizes](o1-preview-outperforms-gpt4o-and-olympiad-participants.md) — related
- [Prompting technique had little effect on GPT-4o's Olympiad problem-solving performance, with no or only small effect sizes among general, CoT, and single-shot CoT prompting](prompting-little-effect-gpt4o-physics-problems.md) — related
- [Score variance differed markedly: Olympiad participants' scores showed substantially higher variance than LLM scores, with o1-preview's scores the most narrowly distributed](score-variance-students-higher-than-llms.md) — related
- [LLM-generated Olympiad solutions show characteristic errors: assuming rather than deriving key relations, misrepresenting problem geometry in energy analyses, and omitting solution evaluation](llm-characteristic-errors-olympiad-solutions.md) — related
