---
type: claim
title: Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies
description: Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies
id: hte-exists-but-cb-gains-limited
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

# Assistance actions exhibit heterogeneous treatment effects across students, but effect sizes are often too small for contextual bandit policies to significantly outperform well-optimized MAB policies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Causal analysis reveals effect heterogeneity for some actions on some questions, yet contextual policies frequently cannot provide significant improvements beyond MAB policies delivering the same action to all students. [→ Schmucker 2025](#schmucker-2025)

## Evidence

### Schmucker 2025

Schmucker, R., Pachapurkar, N., Bala, S., Shah, M., & Mitchell, T. (2025). Learning to Optimize Feedback for One Million Students: Insights from Multi-Armed and Contextual Bandits in Large-Scale Online Tutoring. [doi:10.48550/arXiv.2508.00270](https://doi.org/10.48550/arXiv.2508.00270)

`q2 · i?` · `causal · r2`

Causal machine learning analysis (linear regression interaction tests and causal random forests with calibration and RATE tests, FDR controlled at 0.2) using randomized-experiment log data; the analysis reveals that "some actions for some questions exhibit effect heterogeneity" yet contextual gains over MAB are often not significant.

> "While our analysis reveals that some actions for some questions exhibit effect heterogeneity, effect sizes may often be too small for CB policies to provide significant improvements beyond what well-optimized MAB policies that deliver the same action to all students already achieve."

## Discussion


## Related Claims
- [Bandit-optimized assistance policies significantly improve student outcomes over a randomized assistance policy in live use across 166,000 practice sessions](mab-assistance-policy-improves-outcomes-ab-test.md) — related
- [RITA can account for unobserved heterogeneity in treatment effects, while existing frequentist and bandit approaches can only address observed heterogeneity](rita-handles-unobserved-heterogeneity.md) — related
- [In a randomized controlled trial, students assigned exercises by the LinUCB bandit model had substantially higher completion rates and lower skip rates than students under an adaptive heuristic policy in both free-user and customer cohorts](linucb-rct-higher-completion-lower-skip.md) — related
- [No single assistance type is best: actions that help reattempting the current question are not always best for future-question performance](no-single-best-assistance-type-tradeoff.md) — related
- [MAB assignment overestimates effect sizes for normally distributed rewards, with greater overestimation for smaller true effects](mab-overestimates-effect-sizes.md) — related
