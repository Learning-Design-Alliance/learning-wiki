---
type: claim
title: The MLP starts with high loss (MAE about 74.92, MSE 5840.22) and gradually reduces error across epochs to the final test values
description: The MLP starts with high loss (MAE about 74.92, MSE 5840.22) and gradually reduces error across epochs to the final test values
id: mlp-initial-high-loss-reduced-across-epochs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: i-e-ezeibe-2025
    resource: "https://doi.org/10.48550/arXiv.2505.17143"
    title: "I. E. Ezeibe, S.O. Okide, D.C. Asogwa. (2025). Evaluating the Performance of Nigerian Lecturers using Multilayer Perceptron. International Journal of Research Publication and Reviews, Vol 6, Issue 4, pp 5359-5363. [doi:10.48550/arXiv.2505.17143](https://doi.org/10.48550/arXiv.2505.17143)"
    author: I. E. Ezeibe, S.O. Okide, D.C. Asogwa
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The MLP starts with high loss (MAE about 74.92, MSE 5840.22) and gradually reduces error across epochs to the final test values

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` During the initial epochs the model exhibited high loss values, with a starting MAE of approximately 74.92 and MSE of 5840.22, which gradually minimized to the final test MAE of 13.76 and MSE of 256.99. [→ I. E. Ezeibe 2025](#i-e-ezeibe-2025)

## Evidence

### I. E. Ezeibe 2025

I. E. Ezeibe, S.O. Okide, D.C. Asogwa. (2025). Evaluating the Performance of Nigerian Lecturers using Multilayer Perceptron. International Journal of Research Publication and Reviews, Vol 6, Issue 4, pp 5359-5363. [doi:10.48550/arXiv.2505.17143](https://doi.org/10.48550/arXiv.2505.17143)

`q2 · i?` · `design · r2`

Numerical training result from the Results section of the MLP lecturer-performance experiment. The quote prints the starting error values; the article adds that as the model progressed through additional epochs it gradually minimized the errors, achieving a substantial reduction by the final epoch.

> "During the initial epochs, the model exhibited high loss values, with a starting MAE of approximately 74.92 and MSE of 5840.22."

## Discussion


## Related Claims
- [MLP training loss decreases significantly in the first epochs and then stabilizes, which the authors read as the model learning to generalize](mlp-training-loss-decreases-then-stabilizes.md) — related
- [An MLP model trained on lecturer evaluation metrics achieves a test MAE of 13.76 and test MSE of 256.99 in predicting lecturer performance](mlp-lecturer-performance-test-mae-13-76-mse-256-99.md) — related
- [The trained MLP demonstrates an estimated accuracy rate of approximately 96% in predicting lecturer performance](mlp-lecturer-prediction-accuracy-96-percent.md) — related
