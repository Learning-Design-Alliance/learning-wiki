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
-
