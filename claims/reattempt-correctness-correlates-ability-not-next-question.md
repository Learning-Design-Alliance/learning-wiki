---
type: claim
title: Reattempt correctness correlates with end-of-session student ability (r = 0.27) but is mostly uncorrelated with next-question correctness (r = 0.04)
description: Reattempt correctness correlates with end-of-session student ability (r = 0.27) but is mostly uncorrelated with next-question correctness (r = 0.04)
id: reattempt-correctness-correlates-ability-not-next-question
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: schmucker-2025
    resource: "https://doi.org/10.48550/arXiv.2508.00270"
    title: "Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)"
    author: "Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T."
    q: 2
    i: 2
    kind: causal
    rigour: 2
---

# Reattempt correctness correlates with end-of-session student ability (r = 0.27) but is mostly uncorrelated with next-question correctness (r = 0.04)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i2` medium
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i2` Within-question correlation analysis across 1,336 biology questions shows reattempt correctness is most correlated with IRT-based student ability (r = 0.27) and mostly uncorrelated with next-question correctness (r = 0.04). [→ Schmucker 2025](#schmucker-2025)

## Evidence

### Schmucker 2025

Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)

`q2 · i2` · `causal · r2`

Correlational analysis of average within-question correlations across 1,336 biology questions using randomized-policy log data, designed to be robust to question difficulty differences. Reattempt correctness was "most correlated with the IRT-based student ability estimates"; student ability also correlated with session success (r = 0.35), future correctness (r = 0.64) and next-question correctness (r = 0.36).

> "We find reattempt correctness rate to be most correlated with the IRT-based student ability estimates (r = 0.27) and mostly uncorrelated with next question correctness (r = 0.04)."

## Discussion


## Related Claims
- [No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance](no-single-best-assistance-type-tradeoff.md) — related
- [A per-question training-objective algorithm choosing between combined reward and low-variance reattempt correctness yields policies that improve both immediate and session-level outcomes](per-question-training-objective-algorithm.md) — related
