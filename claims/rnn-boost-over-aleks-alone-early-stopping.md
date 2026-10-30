---
type: claim
title: Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points
description: Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points
id: rnn-boost-over-aleks-alone-early-stopping
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matayoshi-2021
    resource: "https://doi.org/10.1007/s40593-021-00240-8"
    title: "Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8"
    author: "Matayoshi, J., Cosyn, E., & Uzun, H."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After 20 questions, ALEKS PPL alone has accuracy of about 0.8, while the GRU model at average length 20 achieves roughly 0.99. [→ Matayoshi 2021](#matayoshi-2021)

## Evidence

### Matayoshi 2021

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Figure 6 comparison on held-out test data of ALEKS PPL placement accuracy when stopped after specific question numbers versus GRU model performance at various thresholds. The article describes "a very large boost in accuracy and efficiency when the information from the current state of the ALEKS assessment is fed to the RNN classifier."

> "after 20 questions we can see on the plot that ALEKS PPL has an accuracy of about 0.8; in comparison, when the average assessment length of the GRU model is 20, the corresponding accuracy is roughly 0.99"

## Discussion


## Related Claims
- [Misclassified assessments cluster near placement cut scores](misclassifications-cluster-near-cut-scores.md) — related
- [An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy](rnn-stopping-reduces-aleks-assessment-length.md) — related
- [Combined assessment-centered and student-centered features yield the best classifier performance](combined-features-best-classifier-performance.md) — related
- [Stopping algorithm performance is weaker for middle placement categories (labels 4 and 5)](weaker-stopping-performance-middle-labels.md) — related
