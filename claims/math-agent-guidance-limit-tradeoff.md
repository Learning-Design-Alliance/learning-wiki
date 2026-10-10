---
type: claim
title: Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement
description: Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement
id: math-agent-guidance-limit-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: udeshi-2026
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Focusing the Math Agent on analyzing student math steps decreased tutor giving away the final answer by 85.5% ± 5.56% and time-to-first-token latency by 7.85% ± 0.57%, increased behavioral engagement by 7.66% ± 2.25%, but decreased cognitive engagement by 18.09% ± 7.45%. [→ Udeshi 2026](#udeshi-2026)

## Evidence

### Udeshi 2026

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment removing the Math Agent's verbose guidance section, hypothesizing it was no longer necessary with recent LLM improvements. The authors report the guidance section "previously was influencing the LLM response too much and diluting the main workflow system prompt."

> "Tutor giving away final answer decreased by 85.5% ± 5.56% ● Cognitive engagement decreased by 18.09% ± 7.45% ● Time to first token latency (P50) decreased by 7.85% ± 0.57% ● Behavioral engagement increased by 7.66% ± 2.25%"

## Discussion


## Related Claims
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness](student-context-personalization-improves-tutor-metrics.md) — related
- [Reducing Math Agent output and disabling it for non-math courses reduced latency and increased behavioral engagement](math-agent-reduction-livelatency-engagement-gains.md) — related
