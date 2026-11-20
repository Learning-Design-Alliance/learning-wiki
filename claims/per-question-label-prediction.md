---
type: claim
title: On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label
description: On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label
id: per-question-label-prediction
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
  - id: alexander-scarlatos-2022-2
    resource: "https://doi.org/10.48550/arXiv.2204.13607"
    title: "Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)"
    author: Alexander Scarlatos, Christopher Brinton, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predicting per-question correctness in block B yields lower AUC than the score label across all models, and AUC decreases when response status is not used. [→ Alexander Scarlatos 2022](#alexander-scarlatos-2022)
`q2 i?` For the per-question label, Process-BERT slightly outperforms CKT both with and without response status. [→ Alexander Scarlatos 2022 (2)](#alexander-scarlatos-2022-2)

## Evidence

### Alexander Scarlatos 2022

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Quantitative experiment on the NAEP dataset predicting a vector of binary correctness indicators for each block B question, with AUC taken as the macro average over questions. Table 2 reports 0.742±0.006 for the proposed model versus 0.725±0.005 for CKT, and 0.702±0.006 versus 0.674±0.006 without response status, showing "lower AUC numbers than the score label across all models".

> "For the per-question label, as seen in Table 2, we observe lower AUC numbers than the score label across all models and that AUC decreases when response status is not used."

### Alexander Scarlatos 2022 (2)

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Same per-question cross-validation experiment on the NAEP dataset; across the with- and without-response-status conditions in Table 2, "our model slightly outperforms CKT, both with and without response status".

> "The lower overall performance for this label is as expected since ﬁne-grained labels are generally harder to predict than ones at a higher level. For this label, our model slightly outperforms CKT, both with and without response status."

## Discussion


## Related Claims
- [Ablations show score-label prediction depends on the response status pre-training objective when correctness is available, while event type prediction and attention matter most for behavior-only prediction](ablation-response-status-objective-score-label.md) — related
- [Without response status information, Process-BERT still predicts the NAEP score label well from behavior alone, though CKT slightly and non-significantly outperforms it](behavior-only-score-prediction-high-auc.md) — related
- [Augmenting item response theory with a behavior term learned from process data improves question-level performance prediction over base IRT, though the gain shrinks when incomplete questions are excluded](behavior-enhanced-irt-improvement.md) — related
- [On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering](process-bert-outperforms-baselines-score-label.md) — related
- [Fine-grained per-question simulation of post-test performance outperforms whole-question-set simulation, with pre-test information and engagement improving realism](fine-grained-question-simulation-outperforms-coarse.md) — related
