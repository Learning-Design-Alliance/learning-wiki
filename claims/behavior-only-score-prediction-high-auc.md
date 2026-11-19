---
type: claim
title: Without response status information, Process-BERT still predicts the NAEP score label well from behavior alone, though CKT slightly and non-significantly outperforms it
description: Without response status information, Process-BERT still predicts the NAEP score label well from behavior alone, though CKT slightly and non-significantly outperforms it
id: behavior-only-score-prediction-high-auc
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

# Without response status information, Process-BERT still predicts the NAEP score label well from behavior alone, though CKT slightly and non-significantly outperforms it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When response status is removed from input and pre-training, AUC drops but remains considerably high (0.792±0.004 for Process-BERT, 0.797±0.010 for CKT), with no statistically significant difference between the two models. [→ Alexander Scarlatos 2022](#alexander-scarlatos-2022)

## Evidence

### Alexander Scarlatos 2022

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Repeat of the score-label cross-validation experiment on the NAEP dataset with response status removed from the input and its pre-training objective skipped. Table 1 reports 0.792±0.004 for the proposed model and 0.797±0.010 for CKT without response status; the authors state the AUC "is still considerably high".

> "We see from the third column of Table 1 that the AUC drops, as expected, but is still considerably high, indicating that these models can associate student performance with their behavior. With the response status removed, CKT slightly outperforms our model, although the diﬀerence is not statistically signiﬁcant."

## Discussion


## Related Claims
- [Ablations show score-label prediction depends on the response status pre-training objective when correctness is available, while event type prediction and attention matter most for behavior-only prediction](ablation-response-status-objective-score-label.md) — related
- [On the finer-grained per-question label, Process-BERT slightly outperforms CKT with and without response status, with lower AUC than the score label](per-question-label-prediction.md) — related
- [On the NAEP score label, Process-BERT slightly outperforms the CKT autoencoder baseline and both neural models outperform feature engineering](process-bert-outperforms-baselines-score-label.md) — related
