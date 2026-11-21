---
type: claim
title: ANN prediction accuracy depends on hidden-node count, with 9 hidden nodes optimal and larger or smaller configurations showing overfitting or underfitting
description: ANN prediction accuracy depends on hidden-node count, with 9 hidden nodes optimal and larger or smaller configurations showing overfitting or underfitting
id: hidden-node-count-ann-overfitting-underfitting
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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
  - id: saralasrita-mohanty-2025-2
    resource: "https://doi.org/10.48550/arXiv.2503.23506"
    title: "Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2025). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. [doi:10.48550/arXiv.2503.23506](https://doi.org/10.48550/arXiv.2503.23506)"
    author: Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ANN prediction accuracy depends on hidden-node count, with 9 hidden nodes optimal and larger or smaller configurations showing overfitting or underfitting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among 1–30 hidden-node architectures tested, Node 9 yielded the lowest overall MAE (0.0005925) and MSE (0.00150054). [→ Saralasrita Mohanty 2025](#saralasrita-mohanty-2025)
`q2 i?` Configurations with nearly zero training errors but large validation/test errors (e.g., Nodes 12, 16, 20, 25, 29) indicate overfitting, while very few hidden nodes lead to underfitting. [→ Saralasrita Mohanty 2025 (2)](#saralasrita-mohanty-2025-2)

## Evidence

### Saralasrita Mohanty 2025

Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2025). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. [doi:10.48550/arXiv.2503.23506](https://doi.org/10.48550/arXiv.2503.23506)

`q2 · i?` · `design · r2`

Systematic trial-and-error comparison of hidden-node configurations from 1 to 30, each trained and evaluated with MSE and MAE across training, validation, and test datasets. Node 9 gave the "lowest overall MAE of 0.0005925".

> "Among all tested architectures, the best overall performance was obtained for Node 9, which yielded the lowest overall MAE of 0.0005925 and lowest overall MSE of 0.00150054, demonstrating the highest accuracy and best generalization performance."

### Saralasrita Mohanty 2025 (2)

Saralasrita Mohanty, Prabhu Prasad Tripathy, Raja Das, and Sudakshina Prusty. (2025). Integrating Artificial Neural Networks into Undergraduate Physics Laboratory: A Compound Pendulum Case Study. [doi:10.48550/arXiv.2503.23506](https://doi.org/10.48550/arXiv.2503.23506)

`q2 · i?` · `design · r2`

The same architecture comparison (Table 3) shows configurations with near-zero training error but much larger validation and test errors, which the authors read as "indicating overfitting"; very few hidden nodes may underfit.

> "Although some configurations such as Nodes 12, 16, 20, 25, and 29 show nearly zero training errors, their validation and test errors are significantly larger, indicating overfitting."

## Discussion


## Related Claims
- [Validation MSE reaches its minimum at epoch 127, and early stopping there prevents overfitting](early-stopping-validation-minimum-epoch-127.md) — related
- [The single-head base model (Model 1) outperformed the more complex Model 2, suggesting overfitting in the larger architecture](model1-outperforms-complex-model2.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [A MyGPT-generated tutorial for PHYSBO-based hyperparameter optimization of a Keras neural network was executable and converged to an accuracy of 0.9742](mygpt-generated-tutorial-executable-keras.md) — related
