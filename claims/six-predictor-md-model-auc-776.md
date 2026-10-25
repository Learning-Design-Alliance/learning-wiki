---
type: claim
title: A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)
description: A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)
id: six-predictor-md-model-auc-776
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-25
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: psyridou-2024
    resource: "https://doi.org/10.1037/edu0000835"
    title: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835"
    author: "Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` An MLP using only RAN, spatial relations, kindergarten arithmetic, number concepts, counting (spring), and attention-orientation achieved an AUC of .776, close to the full model's performance. [→ Psyridou 2024](#psyridou-2024)

## Evidence

### Psyridou 2024

Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835

`q3 · i?` · `associational · r2`

Follow-up MLP analysis using an identical procedure but only the six top-ranked features (normalized importance > 50%). The reduced model achieved an AUC of ".776". The article states the full set of features accounts for a 3.60%–3.80% improvement in balanced accuracy.

> "The ROC analysis indicated that the AUC was .776, (p < .001, 95% C.I. .719–.834)."

## Discussion


## Related Claims
- [A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818](mlp-kindergarten-predictors-md-grade6-auc-818.md) — related
- [The most important kindergarten predictors of Grade 6 MD are RAN, spatial relations, arithmetic skills, number concepts, attention-orientation, and counting](top-predictors-md-ran-spatial-attention.md) — related
- [Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline](nonlinear-models-modest-auc-gains-over-logistic-baseline.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — related
