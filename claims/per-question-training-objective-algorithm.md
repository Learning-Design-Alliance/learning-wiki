---
type: claim
title: A per-question training-objective algorithm choosing between combined reward and low-variance reattempt correctness yields policies that improve both immediate and session-level outcomes
description: A per-question training-objective algorithm choosing between combined reward and low-variance reattempt correctness yields policies that improve both immediate and session-level outcomes
id: per-question-training-objective-algorithm
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
    i: "?"
    kind: causal
    rigour: 2
---

# A per-question training-objective algorithm choosing between combined reward and low-variance reattempt correctness yields policies that improve both immediate and session-level outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The designed algorithm decides per question whether to optimize the combined reward directly or the lower-variance reattempt correctness measure, because optimizing high-variance measures directly was unreliable in preliminary experiments. [→ Schmucker 2025](#schmucker-2025)

## Evidence

### Schmucker 2025

Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)

`q2 · i?` · `causal · r2`

Preliminary offline experiments found that with "high variance as training objectives" the conventional approach "struggles to reliably identify actions" that perform well on separate test data; the final algorithm uses a one-sided Welch t-test to choose between the combined reward and the reattempt correctness objective per question.

> "In preliminary experiments, we found that when using measures with high variance as training objectives (i.e.,stu- dent abilityand session success), the conventional policy optimization approach (that for each question selects the assistance action estimated to be optimal)"

## Discussion


## Related Claims
- [No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance](no-single-best-assistance-type-tradeoff.md) — related
- [Reattempt correctness correlates with end-of-session student ability (r = 0.27) but is mostly uncorrelated with next-question correctness (r = 0.04)](reattempt-correctness-correlates-ability-not-next-question.md) — related
