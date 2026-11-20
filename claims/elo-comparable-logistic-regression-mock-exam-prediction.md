---
type: claim
title: The multi-concept Elo rating system predicts mock final-exam performance with accuracy highly similar to logistic regression on the BNE medical training data
description: The multi-concept Elo rating system predicts mock final-exam performance with accuracy highly similar to logistic regression on the BNE medical training data
id: elo-comparable-logistic-regression-mock-exam-prediction
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
---

# The multi-concept Elo rating system predicts mock final-exam performance with accuracy highly similar to logistic regression on the BNE medical training data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the mock ECN exam test set, Elo initialized at 0, Elo initialized with historical data, and logistic regression show highly similar prediction accuracy (AUC 0.812, 0.813, 0.811; ACC 0.737, 0.738, 0.736). [→ Erva Nihan Kandemir 2024](#erva-nihan-kandemir-2024)

## Evidence

### Erva Nihan Kandemir 2024

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i?` · `associational · r2`

Observational evaluation on the BNE platform: models trained on the 2020-2021 training period plus 60% of mock-exam users, tested on the remaining 40% of users (1,268,752 entries, 3,447 users, 372 questions). Table 2 prints Elo-at-0 RMSE 0.419, AUC 0.812, ACC 0.737; Elo-historical 0.418/0.813/0.738; logistic regression 0.419/0.811/0.736, showing "highly similar prediction accuracy".

> "These results reveal that the three models show highly similar prediction accuracy, with a slightly better performance on the Elo rating model initiated with historical data over other models."

## Discussion


## Related Claims
- [Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data](elo-logistic-regression-estimate-correlation.md) — related
- [Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days](historical-initialization-boosts-early-elo-accuracy.md) — related
