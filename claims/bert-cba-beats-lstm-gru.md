---
type: claim
title: "BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K"
description: "BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K"
id: bert-cba-beats-lstm-gru
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

# BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` BERT-CBA surpassed BERT-LSTM by 4% to 9% on Recall@K and F1@K (t(5) = 3.23, p = .023, d = 5.02) and outperformed BERT-GRU by 2% to 10% on Precision@K and F1@K (t(5) = 3.31, p = .021, d = 5.15). [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

5×2 cross-validation comparisons against the BERT-LSTM and BERT-GRU baselines. The article reports "t(5) = 3.23, p = .023, d = 5.02" for LSTM and "t(5) = 3.31, p = .021, d = 5.15" for GRU, with 2–10% advantages.

> "BERT-CBA outperformed BERT-LSTM ( t(5) = 3.23, p = .023, d = 5.02). As shown in Table 9, the performance of BERT-CBA surpassed BERT-LSTM in terms of Recall@K=1-5 by 4% to 9%, and it outperformed BERT-LSTM by 4% to 9% for F1@K=1-5 (Table 10)."

## Discussion


## Related Claims
- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](bert-cba-beats-bert-ffnn.md) — related
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — a broader claim this one bears on
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](bert-cba-beats-mnb-40-73-percent.md) — related
- [BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13](bert-cba-beats-svm-precision.md) — related
- [The highway layer ablation showed no measurable performance difference between BERT-CBA variants](highway-layer-ablation-null-result.md) — related
