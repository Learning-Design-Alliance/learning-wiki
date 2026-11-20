---
type: claim
title: Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days
description: Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days
id: historical-initialization-boosts-early-elo-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: erva-nihan-kandemir-2024
    resource: "https://doi.org/10.1145/3636555.3636858"
    title: "Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858"
    author: Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: erva-nihan-kandemir-2024-2
    resource: "https://doi.org/10.1145/3636555.3636858"
    title: "Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858"
    author: Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` During the initial 30 training days, historical initialization gave an average accuracy boost of +0.016 AUC and an average error reduction of -0.008 RMSE. [→ Erva Nihan Kandemir 2024](#erva-nihan-kandemir-2024)
`q2 i?` The initial disparity between the two Elo versions diminishes rapidly, becoming less than 1 point within a few days and nearly negligible by the end of training (+0.002 AUC, -0.002 RMSE in the last 30 days). [→ Erva Nihan Kandemir 2024 (2)](#erva-nihan-kandemir-2024-2)

## Evidence

### Erva Nihan Kandemir 2024

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i?` · `associational · r2`

Observational analysis of daily AUC, ACC and RMSE over 180 consecutive training days (September 16, 2020 to March 14, 2021) comparing two Elo variants, shown in Figure 6. Historical initialization produced "an initial boost in average accuracy (+0.016 AUC)" in the first 30 days.

> "This advantage is reflected in an initial boost in average accuracy (+0.016 AUC) and a reduction in the average error (-0.008 RMSE) during the initial 30 days of training."

### Erva Nihan Kandemir 2024 (2)

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i?` · `associational · r2`

Same daily-metrics analysis (Figure 6): the gap between the two Elo variants "diminishes rapidly"; by the last 30 days the advantage is only +0.002 AUC and -0.002 RMSE, which the authors call nearly negligible.

> "However, it's worth noting that the initial disparity between the two model versions diminishes rapidly and becomes less than 1 point within a few days."

## Discussion


## Related Claims
- [Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data](elo-logistic-regression-estimate-correlation.md) — related
- [The multi-concept Elo rating system predicts mock final-exam performance with accuracy highly similar to logistic regression on the BNE medical training data](elo-comparable-logistic-regression-mock-exam-prediction.md) — related
