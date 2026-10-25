---
type: claim
title: The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset
description: The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset
id: router-reduces-turns-long-conversations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: po-chin-chang-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: po-chin-chang-2026-2
    resource: "https://arxiv.org/abs/2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Po-Chin Chang 2026 (2): groups were assigned but students were analysed as independent (read from the study by two models, 2026-10-25)

## Subclaims
`q3 i?` In the subset of conversations with turns≥5, the router guided students through interactions in fewer turns (N=381, p=0.0073). [→ Po-Chin Chang 2026](#po-chin-chang-2026)
`q3 i?` Across the unfiltered dataset the reduction in conversational turns does not reach statistical significance (p=0.63). [→ Po-Chin Chang 2026 (2)](#po-chin-chang-2026-2)

## Evidence

### Po-Chin Chang 2026

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)

`q3 · i?` · `causal · r2`

Live A/B deployment analysis restricted to longer conversations (turns≥5, N=381). The router "enhanced instructional efficiency" with a statistically significant turn reduction (p=0.0073); no effect size is printed.

> "the routing model enhanced instructional efficiency, guiding students through many interactions (turns≥5 ) in fewer turns (N= 381 ,p= 0.0073 ; App. M)."

### Po-Chin Chang 2026 (2)

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138

`q3 · i?` · `causal · r2`

Same deployment, unfiltered sessions: the turn reduction "remains visible" but is not significant (p=0.63), which the authors attribute to high variance from short, noisy interactions.

> "While this reduction in conversational turns remains visible across the unfiltered dataset, the difference does not reach statistical significance (p= 0.63 ) due to the high variance from short, noisy interactions."

## Discussion


## Related Claims
- [A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable](stochastic-router-higher-conversion-rate.md) — related
- [In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios](prompt-router-beats-static-baselines-simulation.md) — related
- [In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal](router-subject-strategy-alignment-simulation.md) — related
- [Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance](sim-to-real-strategy-shift-feynman-to-coach.md) — related
