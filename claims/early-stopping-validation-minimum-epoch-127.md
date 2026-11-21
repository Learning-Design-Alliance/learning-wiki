---
type: claim
title: Validation MSE reaches its minimum at epoch 127, and early stopping there prevents overfitting
description: Validation MSE reaches its minimum at epoch 127, and early stopping there prevents overfitting
id: early-stopping-validation-minimum-epoch-127
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: saralasrita-mohanty-2025
    resource: "https://doi.org/10.48550/arXiv.2503.23506"
    title: "Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2025). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. [doi:10.48550/arXiv.2503.23506](https://doi.org/10.48550/arXiv.2503.23506)"
    author: Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Validation MSE reaches its minimum at epoch 127, and early stopping there prevents overfitting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Validation MSE reached its minimum (2.9853×10−6) at epoch 127; beyond that point validation error increased, indicating the onset of overfitting, and training was terminated accordingly. [→ Saralasrita Mohanty 2025](#saralasrita-mohanty-2025)

## Evidence

### Saralasrita Mohanty 2025

Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2025). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. [doi:10.48550/arXiv.2503.23506](https://doi.org/10.48550/arXiv.2503.23506)

`q2 · i?` · `design · r2`

Training-performance analysis (Figure 6) plotting MSE logarithmically against epochs for the trained pendulum ANN. The validation MSE minimum of 2.9853×10−6 occurred at epoch 127; parameters from that epoch were retained although training ran to 133 epochs.

> "Beyond epoch 127, the validation error begins to increase continuously for several successive epochs, which is a clear indication of the onset of overfitting. According to the early stopping criterion, training was therefore terminated at this stage to prevent deterioration of model performance on unseen data."

## Discussion


## Related Claims
- [ANN prediction accuracy depends on hidden-node count, with 9 hidden nodes optimal and larger or smaller configurations showing overfitting or underfitting](hidden-node-count-ann-overfitting-underfitting.md) — related
- [The CF–KG hybrid model achieves higher offline NDCG than all eight baselines on the MARS English subset, reaching about 0.625 at epoch 40](cfkg-outperforms-baselines-ndcg.md) — related
