---
type: claim
title: Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics
description: Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics
id: model-migration-component-specific-metric-effects
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: udeshi-2026
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: udeshi-2026-2
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: udeshi-2026-3
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Migrating the Exercise main completion from GPT-4o to GPT-4.1 decreased tutor giving away the final answer by 96.66% ± 4.66% and increased behavioral engagement by 9.93% ± 2.11% in a do-no-harm test. [→ Udeshi 2026](#udeshi-2026)
`q2 i?` Migrating the Exercise Math Agent from GPT-4o to GPT-4.1 increased next-item correctness by 3.41% ± 3.41% and cognitive engagement by 19.29% ± 12.09% but decreased behavioral engagement by 3.54% ± 1.80%. [→ Udeshi 2026 (2)](#udeshi-2026-2)
`q2 i?` Migrating the Tutor Me input classifier from GPT-4.1 to GPT-4.1-mini increased cognitive engagement by 11.79% ± 8.52%, decreased time-to-first-token latency (P50) by 14.40% ± 1.30%, and increased procedural-problem classifications by 19.10% ± 4.90% without decreasing the proportion successfully solved. [→ Udeshi 2026 (3)](#udeshi-2026-3)

## Evidence

### Udeshi 2026

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment comparing AI tutor performance when the main Exercise completion was generated with GPT-4o versus GPT-4.1, run as a do-no-harm test that would launch if the newer model matched the incumbent's performance.

> "Tutor giving away final answer decreased by 96.66% ± 4.66% ● Behavioral engagement increased by 9.93% ± 2.11%"

### Udeshi 2026 (2)

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment comparing Math Agent completions generated with GPT-4o versus GPT-4.1, showing mixed effects across the three metrics for this component.

> "Next item correctness increased by 3.41% ± 3.41% ● Cognitive engagement increased by 19.29% ± 12.09% ● Behavioral engagement decreased by 3.54% ± 1.80%"

### Udeshi 2026 (3)

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

After building an offline evaluation dataset for the Tutor Me request classifier and observing higher-than-expected accuracy, the team tested a more compact model for lower computational impact and latency.

> "Cognitive engagement increased by 11.79% ± 8.52% ● Time to first token latency (P50) decreased by 14.40% ± 1.30%"

## Discussion


## Related Claims
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related
- [Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness](student-context-personalization-improves-tutor-metrics.md) — related
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](turn-level-convergence-gpt-4o-mini.md) — related
- [Cumulative rapid experimentation improved next-item correctness by 10% and cognitive engagement by 14% over five months](rapid-experimentation-cumulative-metric-gains.md) — related
