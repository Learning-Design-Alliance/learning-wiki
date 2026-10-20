---
type: claim
title: "Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance"
description: "Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance"
id: sim-to-real-strategy-shift-feynman-to-coach
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: po-chin-chang-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20138"
    title: "Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)"
    author: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Live feedback shifts the router's strategy from the Feynman prompt favored in simulation to the scaffolding Coach prompt, with superior live performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` After live feedback the router switched from the Feynman strategy to the scaffolding Coach strategy, yielding superior live performance (p=0.0253). [→ Po-Chin Chang 2026](#po-chin-chang-2026)

## Evidence

### Po-Chin Chang 2026

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)

`q3 · i?` · `causal · r2`

Daily score and prompt-probability analysis during live deployment (Figure 5). The strategy "switched to the scaffoldingCoachstrategy after live feedback", with the shift associated with superior live performance (p=0.0253); no effect size printed.

> "Initially favoring the deeper reasoningFeynmanstrategy from simulation, the strategy switched to the scaffoldingCoachstrategy after live feedback. This shift aligned the strategy with student needs, yielding superior live performance (p= 0.0253, App. N)."

## Discussion


## Related Claims
- [The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset](router-reduces-turns-long-conversations.md) — related
- [In simulation the router matches the empirically optimal subject strategy in 8 of 13 subjects, but retreats to a safe strategy where gains are marginal](router-subject-strategy-alignment-simulation.md) — related
- [In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios](prompt-router-beats-static-baselines-simulation.md) — related
- [A scaffolded AI Study Coach produced no assignment-performance or concept-inventory advantage over unrestricted AI use in a master's programming course pilot](scaffolded-coach-no-assignment-performance-advantage.md) — related
- [A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable](stochastic-router-higher-conversion-rate.md) — related
