---
type: claim
title: The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets
description: The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets
id: expert-kc-model-adds-little-predictive-power
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
    i: 1
  - id: theophile-gervet-2020-2
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 1
---

# The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` On seven of nine datasets, KC features provide a boost of +0.01 AUC or less over a no-KC baseline. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` Only algebra05 and bridge06 show significant KC-model predictive power (+0.03 AUC), and 4 of 9 datasets fail a condition suggesting low-quality KC models. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Table 13 ablation comparing Best-LR with NoKC-LR across the nine datasets; the finding is "consistent with results from Lindsey et al. (2014)".

> "On seven out of nine datasets, our best logistic regression model using KC features (Best-LR) provides a boost of +0.01 AUC or less relative to a baseline not using KC features (NoKC-LR)."

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Same ablation: only the KDD Cup 2010 datasets show a +0.03 AUC KC benefit. Out of 9 datasets, 4 do not meet the condition that PFA-style KC-only models beat IRT item-difficulty baselines, suggesting low-quality KC models.

> "The only two datasets where the expert-designed KC model adds significant predictive power (+0.03 AUC) are the KDD Cup 2010 Challenge datasets (algebra05 and bridge06)."

## Discussion


## Related Claims
- [DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets](dkt-input-output-representation-affects-performance.md) — related
- [Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets](time-window-features-null-for-lr-boost-nonlinear.md) — related
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
