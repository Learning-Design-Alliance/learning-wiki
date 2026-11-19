---
type: claim
title: Augmenting item response theory with a behavior term learned from process data improves question-level performance prediction over base IRT, though the gain shrinks when incomplete questions are excluded
description: Augmenting item response theory with a behavior term learned from process data improves question-level performance prediction over base IRT, though the gain shrinks when incomplete questions are excluded
id: behavior-enhanced-irt-improvement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
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

# Augmenting item response theory with a behavior term learned from process data improves question-level performance prediction over base IRT, though the gain shrinks when incomplete questions are excluded

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Both Process-BERT and CKT, used to learn a behavior scalar added to the 1PL IRT probability, achieve a small improvement in test AUC over the base IRT model (0.836 vs 0.824 on all questions). [→ Alexander Scarlatos 2022](#alexander-scarlatos-2022)

## Evidence

### Alexander Scarlatos 2022

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

IRT experiment on all student activity sequences across blocks A and B of the NAEP dataset, with a 20% test split stratified on student ID and question ID and 5-fold cross-validation. Table 3 reports base IRT AUC 0.824±0.001, CKT 0.836±0.000, and the proposed model 0.836±0.002.

> "We see from Table 3 that the behavioral data leveraged by both our model and CKT result in a small improvement in test AUC over the base IRT model."

## Discussion


## Related Claims
- [In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.](item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) — related
- [On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label](per-question-label-prediction.md) — related
- [On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering](process-bert-outperforms-baselines-score-label.md) — related
