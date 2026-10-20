---
type: claim
title: Full reasoning traces worsened calibration bias and Brier scores relative to both other conditions
description: Full reasoning traces worsened calibration bias and Brier scores relative to both other conditions
id: full-traces-worsen-calibration-and-brier-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fernandes-2026
    resource: "https://doi.org/10.48550/arxiv.2605.25856"
    title: "Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R. (2026). Explaining Too Much? Understanding How Large Language Model Reasoning Traces Influence Performance and Metacognition. https://arxiv.org/abs/2605.25856 [doi:10.48550/arxiv.2605.25856](https://doi.org/10.48550/arxiv.2605.25856)"
    author: "Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R."
    q: 3
    i: 1
    kind: causal
    rigour: 3
  - id: fernandes-2026-2
    resource: "https://doi.org/10.48550/arxiv.2605.25856"
    title: "Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R. (2026). Explaining Too Much? Understanding How Large Language Model Reasoning Traces Influence Performance and Metacognition. https://arxiv.org/abs/2605.25856. [doi:10.48550/arxiv.2605.25856](https://doi.org/10.48550/arxiv.2605.25856)"
    author: "Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R."
    q: 3
    i: 2
    kind: causal
    rigour: 3
---

# Full reasoning traces worsened calibration bias and Brier scores relative to both other conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r3` · `q3` · `i1`–`i2`

## Subclaims
`q3 i1` Calibration bias differed significantly across conditions, with Full-trace showing greater overconfidence (M = 0.265) than Answer-only (M = 0.189). [→ Fernandes 2026](#fernandes-2026)
`q3 i2` Brier scores differed significantly across conditions, with Full-trace producing the worst (highest) scores (M = 0.342). [→ Fernandes 2026 (2)](#fernandes-2026-2)

## Evidence

### Fernandes 2026

Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R. (2026). Explaining Too Much? Understanding How Large Language Model Reasoning Traces Influence Performance and Metacognition. https://arxiv.org/abs/2605.25856 [doi:10.48550/arxiv.2605.25856](https://doi.org/10.48550/arxiv.2605.25856)

`q3 · i1` · `causal · r3`

Trial-level calibration index (mean confidence minus accuracy) differed across conditions with η² = .029; Tukey HSD showed Full-trace (M = 0.265) more overconfident than Answer-only (M = 0.189, p < .001), with Summary-trace between and not reliably different from either.

> "Calibration differed between conditions,𝐹( 2, 556)= 8.31,𝑝<. 001,𝜂2 =. 029."

### Fernandes 2026 (2)

Fernandes, D., Buschek, D., Tankelevitch, L., Kosch, T., & Welsch, R. (2026). Explaining Too Much? Understanding How Large Language Model Reasoning Traces Influence Performance and Metacognition. https://arxiv.org/abs/2605.25856. [doi:10.48550/arxiv.2605.25856](https://doi.org/10.48550/arxiv.2605.25856)

`q3 · i2` · `causal · r3`

Brier score ANOVA was significant with η² = .042; Full-trace (M = 0.342) was reliably worse than both Answer-only (M = 0.289) and Summary-trace (M = 0.296), which did not differ (p = .80).

> "Conditions differed reliably,𝐹( 2, 556)= 12.20,𝑝<. 001,𝜂2 =. 042."

## Discussion

## Learner Variables
- [Metacognition](../learner-variables/metacognition.md) — outcome: instruction changes it

## Related Claims

- [Access to AI advice roughly doubled reported confidence in answers in one experiment](ai-access-inflates-confidence.md) — the general claim this finding bears on, with the studies behind it
- [Full reasoning traces impaired task performance relative to both answer-only and summary-trace conditions in AI-assisted LSAT reasoning](full-traces-impair-ai-assisted-reasoning-performance.md) — related
- [Participants substantially overestimated their performance in all trace conditions, with the largest overestimation under full traces](overestimation-largest-under-full-traces.md) — related
- [No trace format supported calibrated self-evaluation: perceived-achieved correlations were low and non-significant in all conditions](no-trace-format-supported-calibrated-self-evaluation.md) — related
- [Summary traces preserved task performance at the answer-only baseline while elevating subjective appraisal](summary-traces-preserve-performance-baseline.md) — related
- [Learners are substantially overconfident when evaluating the quality of their self-generated examples](overconfidence-evaluating-self-generated-examples.md) — related
- [Practice with feedback, regardless of feedback type, improves metacognitive calibration relative to lecture, reducing overconfidence by about 13 percentage points](practice-feedback-improves-metacognitive-calibration.md) — related
- [Reasoning-trace exposure raised trust and hedonic appeal without performance benefits, shifting subjective appraisal of the interaction](trace-exposure-raises-trust-and-hedonic-appeal.md) — related
