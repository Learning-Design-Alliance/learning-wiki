---
type: strategy
id: initialize-elo-with-historical-data-strategy
title: Initialize Elo rating estimates with prior-year model estimates to improve early-stage prediction in online assessment
description: "The article recommends addressing imprecise early-stage Elo estimations by using logistic regression outcomes from the previous year's data as informed initial values rather than starting from zero, giving the algorit..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: erva-nihan-kandemir-2024
    resource: "https://doi.org/10.1145/3636555.3636858"
    title: "Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858"
    author: Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus
---

# Initialize Elo rating estimates with prior-year model estimates to improve early-stage prediction in online assessment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends addressing imprecise early-stage Elo estimations by using logistic regression outcomes from the previous year's data as informed initial values rather than starting from zero, giving the algorithm a "head start" that conserves computational resources and leads to more precise estimates. Initialized values were given an initial attempt count of 50 so the uncertainty function could still update them without destabilizing estimations. This strategy is implementable on any platform with multi-year interaction logs.

## Design Implications

### Context
#### Requirements
- Historical data from preceding years must be available and processed with a comparable logistic regression encoding (one-hot vectors of user-specialty interaction, question, and specialty)
- Values absent from the historical data are initialized to zero, and the initial number of previous attempts must be set (the article used 50) to balance updateability against stability
#### Constraints
- The early advantage diminishes rapidly and becomes nearly negligible by the end of the training period, so the benefit is confined to the initial phases of student interactions

### Target Learners
- Students on digital learning platforms with multi-year interaction logs, here French medical students preparing for the ECN

### Target Learning Goals
- Accurate early-stage estimation of student ability and question difficulty for real-time or online adaptive applications

## Claims

- [Initializing Elo ratings with prior-year logistic regression estimates improves early-training prediction accuracy, with the advantage fading within days](../claims/historical-initialization-boosts-early-elo-accuracy.md) [+W]
- [Elo and logistic regression converge to strongly correlated estimates of question difficulty (r = 0.97) and user ability (r = 0.86) on the same-year data](../claims/elo-logistic-regression-estimate-correlation.md) [+W]
- [Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)](../claims/difficulty-stable-ability-changes-across-years.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Erva Nihan Kandemir, Jill-Jênn Vie, Adam Sanchez-Ayte, Olivier Palombi, and Franck Ramus. (2024). Adaptation of the Multi-Concept Multivariate Elo Rating System to Medical Students' Training Data. The 14th Learning Analytics and Knowledge Conference (LAK '24). https://doi.org/10.1145/3636555.3636858
