---
type: claim
title: "Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets"
description: "Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets"
id: time-window-features-null-for-lr-boost-nonlinear
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
  - id: theophile-gervet-2020-3
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 2
---

# Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · `q2` quasi-experiment · `i1`–`i2`

## Subclaims
`q2 i?` DAS3H time-window features add no predictive power to the best logistic regression model, suggesting DAS3H's boost over PFA comes from an IRT-inspired item difficulty parameter. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` Time-window features boost a feedforward network by +0.048 AUC on assistments17 and +0.014 on assistments12, suggesting a nonlinear relation between history and correctness log-odds. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)
`q2 i?` Total counts of prior correct answers and attempts substantially boost performance on all datasets. [→ Theophile Gervet 2020 (3)](#theophile-gervet-2020-3)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Ablation study (Table 13) of logistic regression and two-layer feedforward networks with different feature sets across the nine datasets. "do not add any predictive power to our best logistic regression model".

> "Surprisingly, the time-window features introduced in DAS3H (best paper at EDM 2019) do not add any predictive power to our best logistic regression model (see Best-LR vs. TW-LR in Table 13)."

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Same Table 13 ablation, comparing NoTW-FFW with Best-FFW: time-window features help only the nonlinear model on two datasets, consistent with DKT's advantage there.

> "time-window features boost the performance of a feedforward neural network on the assistments17 dataset by +0.048 AUC and on the assistments12 dataset by +0.014 AUC"

### Theophile Gervet 2020 (3)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Table 13 ablation introducing total count features; the authors report these "substantially boost performance on all datasets", underpinning new state-of-the-art results on 5 of 8 datasets.

> "We consider a set of features absent from prior work: the total number of prior correct answers and attempts (total counts). These features substantially boost performance on all datasets."

## Discussion


## Related Claims
- [The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets](expert-kc-model-adds-little-predictive-power.md) — related
- [The propdec adaptive student feature is highly colinear with a student intercept, capturing student individual differences without student parameters](propdec-colinear-with-student-intercept.md) — related
- [Models able to weight performance by recency fit better on the Assistments and KDD datasets, without explicit memory-decay terms being necessary](recency-weighting-models-better-assistments-kdd.md) — related
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — related
