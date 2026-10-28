---
type: claim
title: The highway layer ablation showed no measurable performance difference between BERT-CBA variants
description: The highway layer ablation showed no measurable performance difference between BERT-CBA variants
id: highway-layer-ablation-null-result
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: olatinwo-2025
    resource: "https://doi.org/10.1007/s40593-024-00441-x"
    title: "Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x"
    author: "Olatinwo, S. O., & Demmans Epp, C."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The highway layer ablation showed no measurable performance difference between BERT-CBA variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A 5×2 cross-validation ablation found the two variants of BERT-CBA (with and without the highway layer) were not measurably different: t(5) = .74, p = .491, d = .03. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

Ablation study comparing BERT-CBA with and without the highway layer on the test set. The article reports "t(5) = .74, p = .491, d =.03" and concludes the variants are not measurably different.

> "Based on the 5×2 cross validation test (t(5) = .74, p = .491, d =.03), we noticed that the two variants of the proposed method are not measurably different. That is, BERT-CBA with Highway layer achieved competitive performance across all evaluation metrics."

## Discussion


## Related Claims
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — related
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](bert-cba-beats-lstm-gru.md) — related
- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](bert-cba-beats-bert-ffnn.md) — related
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](bert-cba-beats-mnb-40-73-percent.md) — related
- [BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13](bert-cba-beats-svm-precision.md) — related
