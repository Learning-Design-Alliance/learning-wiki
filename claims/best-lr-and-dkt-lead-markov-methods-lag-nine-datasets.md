---
type: claim
title: Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind
description: Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind
id: best-lr-and-dkt-lead-markov-methods-lag-nine-datasets
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: theophile-gervet-2020
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 2
---

# Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i?` Best-LR outperforms deep learning methods and DAS3H on 4 of 9 datasets; DKT leads on the other 5. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` Markov process methods like BKT cannot compete on datasets of this scale. [→ Theophile Gervet 2020](#theophile-gervet-2020)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Extensive empirical comparison of three model families on nine real-world tutoring datasets with 5-fold learner-level cross-validation, reported in AUC and RMSE (Tables 3-11). The results section states Best-LR "outperforms all other approaches ... on 4 datasets out of 9" and DKT leads on the remaining 5.

> "The logistic regression model with the best feature vector (Best-LR) outperforms all other approaches – including deep learning methods (DKT and SAKT) and the best logistic regression model in prior literature (DAS3H) – on 4 datasets out of 9"

## Discussion


## Related Claims
-
