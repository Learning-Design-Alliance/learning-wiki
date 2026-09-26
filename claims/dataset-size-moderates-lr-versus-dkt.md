---
type: claim
title: "Dataset size moderates the LR-versus-DKT comparison: Best-LR dominates in low and medium data regimes and DKT takes over in the high data regime"
description: "Dataset size moderates the LR-versus-DKT comparison: Best-LR dominates in low and medium data regimes and DKT takes over in the high data regime"
id: dataset-size-moderates-lr-versus-dkt
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

# Dataset size moderates the LR-versus-DKT comparison: Best-LR dominates in low and medium data regimes and DKT takes over in the high data regime

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i1`–`i2`

## Subclaims
`q2 i?` On the squirrel dataset, Best-LR dominates below one million training interactions and DKT takes over above that. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` Effective dataset size for generalization is better captured by learners per item and per KC than by total interactions. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Additional experiment on the squirrel dataset subsampling training data across 5 folds (Figure 5), comparing DKT and Best-LR AUC as a function of training amount; "Best-LR dominates in the low and medium data regimes".

> "Best-LR dominates in the low and medium data regimes (fewer than one million interactions), and DKT takes over in the high data regime."

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Authors' interpretation of the cross-dataset pattern: the statics dataset is smallest by total interactions (189,297) yet fits DKT without much overfitting because it has enough learners per item and KC, unlike bridge06.

> "for generalization purposes, the number of learners per item and per KC of a dataset better capture its size than the number of interactions it contains"

## Discussion


## Related Claims
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
- [DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression](dkt-long-term-information-and-faster-burn-in.md) — related
- [DKT makes better use of the temporal order of interactions than logistic regression, confirmed by KC-specific DKT models on sequential datasets](dkt-better-exploits-temporal-order.md) — related
- [DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets](dkt-input-output-representation-affects-performance.md) — related
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — related
- [SAKT underperforms DKT on all nine datasets, contradicting previously reported results](sakt-underperforms-dkt-all-datasets.md) — related
