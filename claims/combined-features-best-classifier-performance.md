---
type: claim
title: Combined assessment-centered and student-centered features yield the best classifier performance
description: Combined assessment-centered and student-centered features yield the best classifier performance
id: combined-features-best-classifier-performance
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
    rigour: 2
---

# Combined assessment-centered and student-centered features yield the best classifier performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The assessment-centered model performs better than the student-centered model in all cases, and the combined feature set yields the best results. [→ Matayoshi 2021](#matayoshi-2021)
`q2 i?` McNemar's test shows differences between RNN and logistic regression accuracy are statistically significant, but differences between GRU and LSTM are not. [→ Matayoshi 2021 (2)](#matayoshi-2021-2)

## Evidence

### Matayoshi 2021

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

Comparison of classifier models (LR, GRU, LSTM) across three feature sets on validation data (Table 2). Combined-features GRU achieves accuracy 0.830 after question 15 and 0.944 after question 25, the best among all models tested.

> "while the assessment-centered model performs better than the student-centered model in all cases, the best results are from the combined model"

### Matayoshi 2021 (2)

Matayoshi, J., Cosyn, E., & Uzun, H. (2021). Are We There Yet? Evaluating the Effectiveness of a Recurrent Neural Network-Based Stopping Algorithm for an Adaptive Assessment. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00240-8

`q2 · i?` · `design · r2`

McNemar's test with Benjamini-Yekutieli correction on validation set predictions (Table 3). LR vs GRU and LR vs LSTM comparisons show χ² values with p ≪ 0.001; GRU vs LSTM shows χ² = 0.02, p = 0.888 after question 15.

> "the differences in accuracy scores between the RNN and logistic regressions models are always statistically significant; however, the differences in the accuracy scores between the RNN models are not significant"

## Discussion


## Related Claims
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Reasoning-process features are particularly useful when difficulty depends on multi-step problem solving, and the representation also generalizes to text-based assessment items](process-features-strongest-for-multistep-items.md) — related
- [Feeding ALEKS assessment state to an RNN classifier yields a large boost in placement accuracy over the assessment alone at early stopping points](rnn-boost-over-aleks-alone-early-stopping.md) — related
- [An RNN-based stopping algorithm reduces ALEKS PPL assessment length by over 26% while maintaining high accuracy](rnn-stopping-reduces-aleks-assessment-length.md) — related
