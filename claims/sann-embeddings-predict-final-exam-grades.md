---
type: claim
title: LSTM model using SANN code embeddings predicts final exam grades better than baselines (R2 = 0.50, RMSE = 0.17)
description: LSTM model using SANN code embeddings predicts final exam grades better than baselines (R2 = 0.50, RMSE = 0.17)
id: sann-embeddings-predict-final-exam-grades
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: muntasir-hoq-2025
    resource: "https://doi.org/10.48550/arXiv.2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LSTM model using SANN code embeddings predicts final exam grades better than baselines (R2 = 0.50, RMSE = 0.17)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An LSTM-based model fed sequential SANN code vectors for 50 problems achieved the lowest RMSE of 0.17 and highest R2 of 0.50 among compared models including LSTM-code2vec, SVM, and regression baselines. [→ Muntasir Hoq 2025](#muntasir-hoq-2025)

## Evidence

### Muntasir Hoq 2025

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Long-term performance prediction using all code vectors per student-problem pair (truncated/padded to length 30) plus problem-solving behavior features. Baselines included no-skill, Linear, Lasso, SVM, GPR, and LSTM-code2vec (RMSE 0.23, R2 0.09).

> "Our LSTM model outperformed other models with the lowest RMSE of 0 .17 and the highest R 2 of 0.50, demonstrating its superior predictive capability for student final exam grades."

## Discussion


## Related Claims
- [SANN code vectors outperform explainable baseline code2vec in logical error identification](sann-beats-code2vec-error-identification.md) — related
- [Concatenating SANN code vectors with DKT inputs improves next-attempt prediction by about 10% AUC over original DKT](sann-code-vectors-improve-knowledge-tracing.md) — related
