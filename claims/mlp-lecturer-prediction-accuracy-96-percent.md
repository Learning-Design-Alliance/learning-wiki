---
type: claim
title: "The trained MLP demonstrates an estimated accuracy rate of approximately 96% in predicting lecturer performance"
description: "The trained MLP demonstrates an estimated accuracy rate of approximately 96% in predicting lecturer performance"
id: mlp-lecturer-prediction-accuracy-96-percent
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

# The trained MLP demonstrates an estimated accuracy rate of approximately 96% in predicting lecturer performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The model demonstrated an estimated accuracy rate of approximately 96%, which the authors present as validating its effectiveness in predicting lecturer performance. [→ I. E. Ezeibe 2025](#i-e-ezeibe-2025)

## Evidence

### I. E. Ezeibe 2025

I. E. Ezeibe, S.O. Okide, D.C. Asogwa. (2025). Evaluating the Performance of Nigerian Lecturers using Multilayer Perceptron. International Journal of Research Publication and Reviews, Vol 6, Issue 4, pp 5359-5363. [doi:10.48550/arXiv.2505.17143](https://doi.org/10.48550/arXiv.2505.17143)

`q2 · i?` · `design · r2`

Numerical result reported in the Results section for the MLP trained on the 5000-row lecturer evaluation dataset. The quote prints the estimated accuracy of approximately 96%; the article describes it as an estimated rate validating prediction of lecturer performance.

> "The model also demonstrated an estimated accuracy rate of approximately 96%, validated its effectiveness in predicting lecturer performance."

## Discussion


## Related Claims
- [An MLP model trained on lecturer evaluation metrics achieves a test MAE of 13.76 and test MSE of 256.99 in predicting lecturer performance](mlp-lecturer-performance-test-mae-13-76-mse-256-99.md) — related
- [MLP training loss decreases significantly in the first epochs and then stabilizes, which the authors read as the model learning to generalize](mlp-training-loss-decreases-then-stabilizes.md) — related
- [The MLP starts with high loss (MAE about 74.92, MSE 5840.22) and gradually reduces error across epochs to the final test values](mlp-initial-high-loss-reduced-across-epochs.md) — related
