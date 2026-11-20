---
type: claim
title: Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data
description: Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data
id: elo-logistic-regression-estimate-correlation
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
    i: 3
    kind: associational
    rigour: 2
---

# Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Question difficulty estimates from Elo and logistic regression correlate at r = 0.97, and user ability estimates at r = 0.86, on the 2020-2021 data. [→ Erva Nihan Kandemir 2024](#erva-nihan-kandemir-2024)

## Evidence

### Erva Nihan Kandemir 2024

Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858

`q2 · i3` · `associational · r2`

Correlational comparison of model estimates on the same 2020-2021 BNE data, plotted in Figure 4 with y = x reference lines. The article reports a "notable positive correlation" with r = 0.97 for question difficulty and r = 0.86 for user ability across 31 specialties.

> "Figure 4 illustrates a notable positive correlation between the estimates of question difficulty (𝑟 = 0.97) and user ability (𝑟 = 0.86) derived from the Elo rating and logistic regression models for the same-year data."

## Discussion


## Related Claims
- [Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)](difficulty-stable-ability-changes-across-years.md) — related
- [The multi-concept Elo rating system predicts mock final-exam performance with accuracy highly similar to logistic regression on the BNE medical training data](elo-comparable-logistic-regression-mock-exam-prediction.md) — related
- [Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days](historical-initialization-boosts-early-elo-accuracy.md) — related
