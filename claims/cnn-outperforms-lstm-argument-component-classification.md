---
type: claim
title: CNN models almost always outperform LSTM models for argument component classification in classroom discussions, with character-level LSTMs near random chance
description: CNN models almost always outperform LSTM models for argument component classification in classroom discussions, with character-level LSTMs near random chance
id: cnn-outperforms-lstm-argument-component-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: luca-lugini-and-diane-litman-2018
    resource: "https://doi.org/10.18653/v1/w18-5208"
    title: "Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)"
    author: Luca Lugini and Diane Litman
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CNN models almost always outperform LSTM models for argument component classification in classroom discussions, with character-level LSTMs near random chance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under the same conditions, CNN models almost always outperform LSTM models; character-level LSTMs show performance comparable to random chance, while word embeddings are essential for improving LSTM performance but not CNN performance. [→ Luca Lugini and Diane Litman 2018](#luca-lugini-and-diane-litman-2018)

## Evidence

### Luca Lugini and Diane Litman 2018

Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)

`q2 · i?` · `design · r2`

Comparison of CNN and LSTM models across character/word-level and single/multi-task conditions in Table 3. Character-level LSTM (row 5) has kappa -0.002, close to zero and below the majority baseline; the authors attribute this to LSTMs struggling with long sequences and limited training data.

> "Overall, under the same conditions CNN models almost always outperform LSTM models. One interesting difference between the two models is that the prior knowledge introduced by word embeddings in word-based models is essential for improving performance of LSTMs"

## Discussion


## Related Claims
- [Multi-task learning with specificity prediction as a secondary task almost always improves argument component classification, and yields the only model with warrant f-score above 0.3](multi-task-specificity-improves-argument-classification.md) — related
- [Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features](handcrafted-features-improve-neural-argument-classifiers.md) — related
