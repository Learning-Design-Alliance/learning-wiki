---
type: claim
title: On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering
description: On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering
id: process-bert-outperforms-baselines-score-label
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: alexander-scarlatos-2022
    resource: "https://doi.org/10.48550/arXiv.2204.13607"
    title: "Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)"
    author: Alexander Scarlatos, Christopher Brinton, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On predicting whether a student scores above or below average on block B from block A data, Process-BERT achieves test AUC 0.868±0.008, slightly above CKT (0.854±0.005) and above the feature engineering baseline (0.828). [→ Alexander Scarlatos 2022](#alexander-scarlatos-2022)

## Evidence

### Alexander Scarlatos 2022

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Quantitative experiment on the NAEP competition dataset using 5-fold stratified cross-validation with the competition's 30-minute validation partition as test set, evaluated by AUC. Table 1 reports test AUC of 0.868±0.008 for the proposed model, 0.854±0.005 for CKT, and 0.828 for FE, where "both CKT and our model outperformed the FE baseline".

> "For the score label, as shown in the second column of Table 1, both CKT and our model outperformed the FE baseline."

## Discussion


## Related Claims
- [Without response status information, Process-BERT still predicts the NAEP score label well from behavior alone, though CKT slightly and non-significantly outperforms it](behavior-only-score-prediction-high-auc.md) — related
- [On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label](per-question-label-prediction.md) — related
- [Augmenting item response theory with a behavior term learned from process data improves question-level performance prediction over base IRT, though the gain shrinks when incomplete questions are excluded](behavior-enhanced-irt-improvement.md) — related
