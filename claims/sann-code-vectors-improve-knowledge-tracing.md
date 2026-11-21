---
type: claim
title: "Concatenating SANN code vectors with DKT inputs improves next-attempt prediction by about 10% AUC over original DKT"
description: "Concatenating SANN code vectors with DKT inputs improves next-attempt prediction by about 10% AUC over original DKT"
id: sann-code-vectors-improve-knowledge-tracing
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

# Concatenating SANN code vectors with DKT inputs improves next-attempt prediction by about 10% AUC over original DKT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An LSTM-DKT model enriched with SANN code vectors achieved an overall AUC of 72.45% versus 65.87% for the original DKT, with per-assignment improvements marked significant at p < 0.05 or better. [→ Muntasir Hoq 2025](#muntasir-hoq-2025)

## Evidence

### Muntasir Hoq 2025

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Knowledge tracing experiment on student submissions for all 50 problems, student-level 80:10:10 split. Table 3 marks SANN-DKT improvements over DKT with significance stars (p < 0.05 to p < 0.001); the article notes the ~10% gain compares to Code-DKT's 3-4% improvement on CodeWorkout.

> "Our approach showed a higher AUC score of 72.45% than the original DKT model (65.87%)."

## Discussion


## Related Claims
- [SANN code vectors outperform explainable baseline code2vec in logical error identification](sann-beats-code2vec-error-identification.md) — related
- [LSTM model using SANN code embeddings predicts final exam grades better than baselines (R2 = 0.50, RMSE = 0.17)](sann-embeddings-predict-final-exam-grades.md) — related
- [Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive](code-embeddings-inconsistent-under-rectified-settings.md) — reports the opposite
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
