---
type: claim
title: "An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy"
description: "An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy"
id: rnn-stopping-reduces-aleks-assessment-length
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: matayoshi-2021
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: matayoshi-2021-2
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Combining an RNN with the ALEKS assessment reduces average assessment length by over 26% while maintaining a high degree of accuracy. [→ Matayoshi 2021](#matayoshi-2021)
`q2 i?` At accuracy of 0.99, the GRU model has an average assessment length of about 20.2 questions versus about 21.1 for logistic regression. [→ Matayoshi 2021 (2)](#matayoshi-2021-2)

## Evidence

### Matayoshi 2021

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Evaluation of the stopping algorithm on a held-out test set of 50,000 ALEKS PPL assessments, using the combined-features GRU model with threshold α = 0.99. The article reports the algorithm "reduce the average assessment length by over 26%" with accuracy of 0.9943 (Table 4).

> "We show that the combination of an RNN with the ALEKS assessment can reduce the average assessment length by over 26%, while a high degree of accuracy is maintained."

### Matayoshi 2021 (2)

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r3`

Results from Fig. 5 on held-out test data comparing accuracy versus average assessment length across probability thresholds. The GRU model outperforms logistic regression at high accuracy levels, with a minimum difference of 1.4 questions at accuracy ≥ 0.995.

> "at an accuracy of 0.99, the GRU model has an average assessment length of about 20.2 questions, while the logistic regression model has an average length of about 21.1 questions"

## Discussion


## Related Claims
- [Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points](rnn-boost-over-aleks-alone-early-stopping.md) — related
- [Combined assessment-centered and student-centered features yield the best classifier performance](combined-features-best-classifier-performance.md) — related
- [The stopping algorithm reduces average assessment duration by about 23.5 minutes](stopping-algorithm-reduces-assessment-duration.md) — possibly the same claim (merge candidate)
- [Stopping algorithm performance is weaker for middle placement categories (labels 4 and 5)](weaker-stopping-performance-middle-labels.md) — related
