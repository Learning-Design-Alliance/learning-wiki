---
type: claim
title: SAKT underperforms DKT on all nine datasets, contradicting previously reported results
description: SAKT underperforms DKT on all nine datasets, contradicting previously reported results
id: sakt-underperforms-dkt-all-datasets
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
---

# SAKT underperforms DKT on all nine datasets, contradicting previously reported results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i1` small

## Subclaims
`q2 i?` Self-attentive knowledge tracing underperforms DKT on every dataset tested, contradicting Pandey and Karypis (2019). [→ Theophile Gervet 2020](#theophile-gervet-2020)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Results section comparison across the nine benchmark datasets. The largest gap is on ASSISTment 2015, where the authors report "an AUC of 0.85, while we observed an AUC of 0.73 (no improvement over DKT)".

> "In our experiments, SAKT underperforms DKT on all datasets. This observation contradicts results from Pandey and Karypis (2019)."

## Discussion


## Related Claims
- [Adaptive G-UKT reportedly establishes competitive state-of-the-art knowledge tracing performance, particularly under sparse observation regimes](adaptive-g-ukt-competitive-performance-sparse-regimes.md) — related
- [BKTransformer rivals or surpasses deep KT baselines (DKT, SAKT) and BKT-EM in AUC, but DKT outperforms it on one dataset](bktransformer-rivals-deep-kt-auc.md) — related
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
- [Dataset size moderates the LR-versus-DKT comparison: Best-LR dominates in low and medium data regimes and DKT takes over in the high data regime](dataset-size-moderates-lr-versus-dkt.md) — related
