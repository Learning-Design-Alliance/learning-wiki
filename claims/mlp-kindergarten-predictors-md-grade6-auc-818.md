---
type: claim
title: A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818
description: A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818
id: mlp-kindergarten-predictors-md-grade6-auc-818
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

# A multilayer perceptron trained on 49 kindergarten-age measures predicts Grade 6 math difficulties with an AUC of .818

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` A neural networks (MLP) model using 49 kindergarten-age variables classified Grade 6 MD with an AUC of .818, p < .001. [→ Psyridou 2024](#psyridou-2024)

## Evidence

### Psyridou 2024

Psyridou, M., Koponen, T., Tolvanen, A., Aunola, K., Lerkkanen, M.-K., Poikkeus, A.-M., & Torppa, M. (2024). Early prediction of math difficulties with the use of a neural networks model. Journal of Educational Psychology, 116(2), 212-232. https://doi.org/10.1037/edu0000835

`q3 · i?` · `associational · r2`

Testing-sample ROC analysis of the MLP trained on 49 kindergarten-age measures (training n = 1,272; testing n = 545) from the First Steps longitudinal study, with MD defined as the lowest 10% of the Grade 6 math distribution. The AUC was ".818". The study was not preregistered.

> "For the prediction of MD, the AUC was .818, (p < .001, 95% C.I. .769–.867). Thus, there is an 81.8% chance that the model will distinguish between those with and without MD."

## Discussion


## Related Claims
- [A reduced model using only the six top-ranked predictors maintains relatively similar MD prediction performance (AUC .776)](six-predictor-md-model-auc-776.md) — related
- [The most important kindergarten predictors of Grade 6 MD are RAN, spatial relations, arithmetic skills, number concepts, attention-orientation, and counting](top-predictors-md-ran-spatial-attention.md) — related
- [Training the MLP on an oversampled (balanced) MD dataset did not improve performance over training on the unbalanced data](oversampled-balanced-data-no-gain-md-model.md) — related
- [Kindergarten counting, arithmetic, and letter-knowledge measures correlate with Grade 6 arithmetic fluency (r up to .45)](kindergarten-measures-correlate-grade6-math.md) — related
