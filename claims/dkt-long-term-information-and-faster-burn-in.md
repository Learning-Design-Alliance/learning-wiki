---
type: claim
title: DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression
description: DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression
id: dkt-long-term-information-and-faster-burn-in
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
  - id: theophile-gervet-2020-2
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 1
---

# DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i1`–`i2`

## Subclaims
`q2 i?` On the spanish dataset DKT plateaus after 1000 student interactions while Best-LR keeps improving, evidence DKT cannot track long-term information. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` On the squirrel dataset DKT needs 6 times fewer interactions than Best-LR to reach close to peak performance on a new student. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Figure 6 analysis of AUC as a function of data available per student on the spanish dataset; a similar pattern was observed on bridge06. "DKT plateaus after 1000 student interactions", which the authors attribute to a well-documented recurrent network problem.

> "DKT plateaus after 1000 student interactions, whereas Best-LR keeps improving with more data."

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Figure 7 analysis on the squirrel dataset of AUC versus data available on a new student: "In only 10 interactions, DKT reaches close to peak performance", reducing the model's burn-in period.

> "In only 10 interactions, DKT reaches close to peak performance, whereas Best-LR needs 60."

## Discussion


## Related Claims
- [Dataset size moderates the LR-versus-DKT comparison: Best-LR dominates in low and medium data regimes and DKT takes over in the high data regime](dataset-size-moderates-lr-versus-dkt.md) — related
- [DKT makes better use of the temporal order of interactions than logistic regression, confirmed by KC-specific DKT models on sequential datasets](dkt-better-exploits-temporal-order.md) — related
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — related
