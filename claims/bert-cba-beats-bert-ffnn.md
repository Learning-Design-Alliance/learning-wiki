---
type: claim
title: "BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64"
description: "BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64"
id: bert-cba-beats-bert-ffnn
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

# BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` BERT-CBA outperformed BERT-FFNN in Precision@K for K of 1 through 5 by 6% to 15%, with similar advantages on Recall@K and F1@K. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q2 · i?` · `design · r2`

5×2 cross-validation comparison against the BERT-FFNN baseline. The article reports "t(5) = 6.56, p = .001, d = 4.64" and a 6–15% precision advantage.

> "BERT-CBA outperformed BERT-FFNN(t(5) = 6.56, p = .001, d = 4.64). As presented in Table 8, BERT-CBA outperformed BERT-FFNN in terms of Precision@K for K of 1 through 5 by 6% to 15%. BERT-CBA had similarly higher Recall@K and F1@K, as can be seen in Tables 9 and 10."

## Discussion


## Related Claims
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — a broader claim this one bears on
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](bert-cba-beats-lstm-gru.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13](bert-cba-beats-svm-precision.md) — related
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](bert-cba-beats-mnb-40-73-percent.md) — related
- [The highway layer ablation showed no measurable performance difference between BERT-CBA variants](highway-layer-ablation-null-result.md) — related
