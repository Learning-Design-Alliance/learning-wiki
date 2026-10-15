---
type: claim
title: A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable
description: A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable
id: stochastic-router-higher-conversion-rate
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

# A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` The exploitation router's conversion rate is comparable with the static baseline (19.1% vs. 19.6%), while the exploration router yields a higher conversion rate (28.1%); the downstream improvement does not reach statistical significance. [→ Po-Chin Chang 2026](#po-chin-chang-2026)

## Evidence

### Po-Chin Chang 2026

Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer. (2026). Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring. https://arxiv.org/abs/2606.20138 [doi:10.48550/arxiv.2606.20138](https://doi.org/10.48550/arxiv.2606.20138)

`q3 · i?` · `causal · r2`

Live A/B test (N=656 sessions, 359 Dutch high-school students) comparing conversion rates. The exploration router's 28.1% exceeds the baseline's 19.6%, but the article states this "downstream improvement does not reach statistical significance".

> "the system-level comparison of the conversion rate (App. O) shows the exploitation router is comparable with the static baseline ( 19.1% vs. 19.6%). Interestingly, the exploration router yields a higher conversion rate 28.1%."

## Discussion


## Related Claims
- [Higher AI pedagogical scores are associated with exercise conversion in real student sessions](pedagogical-score-predicts-exercise-conversion.md) — related
- [In simulation, an adaptive prompt router outperforms two static prompt baselines on pedagogical score across 390 scenarios](prompt-router-beats-static-baselines-simulation.md) — related
- [The adaptive router reduces turns in long conversations (turns≥5) but not across the unfiltered dataset](router-reduces-turns-long-conversations.md) — related
