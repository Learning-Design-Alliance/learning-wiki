---
type: claim
title: "BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13"
description: "BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13"
id: bert-cba-beats-svm-precision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BERT-CBA outperformed SVM by 44% to 73% in Precision@K for K of 1 through 5, and by 55% to 68% on Recall@K and 44% to 68% on F1@K. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

5×2 cross-validation comparison against the SVM baseline. The article reports "t(5) = 5.62, p = .002, d = 7.13" for the precision comparison and percentage ranges for recall and F1.

> "BERT-CBA outperformed SVM (t(5) = 5.62, p = .002, d = 7.13) by 44% to 73% in terms of Precision@K for K of 1 through 5 (see Table 8). BERT-CBA also had Recall@K values that were 55% to 68% higher (Tables 9) and F1@K values that were 44% to 68% higher than those achieved using SVM (Table 10)."

## Discussion


## Related Claims
- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](bert-cba-beats-bert-ffnn.md) — related
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](bert-cba-beats-mnb-40-73-percent.md) — related
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — a broader claim this one bears on
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](bert-cba-beats-lstm-gru.md) — related
- [The highway layer ablation showed no measurable performance difference between BERT-CBA variants](highway-layer-ablation-null-result.md) — related
