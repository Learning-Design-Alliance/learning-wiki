---
type: claim
title: "BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation"
description: "BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation"
id: bert-cba-outperforms-baselines-cross-validation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
source_checked: 2026-10-28
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

# BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · checked against its sources 2026-10-28 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` BERT-CBA achieved higher Precision@K, Recall@K, and F1@K than MNB, SVM, BERT-FFNN, BERT-LSTM, and BERT-GRU in 5×2 cross-validation. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

Cross-validation comparison of six tag recommendation models on the Stack Overflow dataset. BERT-CBA "achieved higher Precision@K (Table 8), Recall@K (Table 9), and F1@K (Table 10) scores compared to the existing, baseline methods." Differences were tested with the 5×2 CV test using precision.

> "The proposed method achieved higher Precision@K (Table 8), Recall@K (Table 9), and F1@K (Table 10) scores compared to the existing, baseline methods."

## Discussion


## Related Claims
- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](bert-cba-beats-bert-ffnn.md) — a narrower finding that bears on this claim
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](bert-cba-beats-lstm-gru.md) — a narrower finding that bears on this claim
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](bert-cba-beats-mnb-40-73-percent.md) — a narrower finding that bears on this claim
- [BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13](bert-cba-beats-svm-precision.md) — a narrower finding that bears on this claim
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [F1@K decreased as K increased for all methods](f1-decreases-with-k.md) — related
- [The highway layer ablation showed no measurable performance difference between BERT-CBA variants](highway-layer-ablation-null-result.md) — related
- [Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)](neural-models-outperform-baselines-review.md) — related
