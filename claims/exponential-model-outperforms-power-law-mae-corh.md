---
type: claim
title: The exponential forgetting curve model outperforms the power-law model on MAE and half-life correlation, while the power-law model performs slightly better on AUC
description: The exponential forgetting curve model outperforms the power-law model on MAE and half-life correlation, while the power-law model performs slightly better on AUC
id: exponential-model-outperforms-power-law-mae-corh
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: utkarsh-upadhyay-2021
    resource: "https://doi.org/10.1038/s41539-021-00105-8"
    title: "Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. Originally published 2020. [doi:10.1038/s41539-021-00105-8](https://doi.org/10.1038/s41539-021-00105-8)"
    author: Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The exponential forgetting curve model outperforms the power-law model on MAE and half-life correlation, while the power-law model performs slightly better on AUC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On held-out prediction of recall, the exponential model achieved lower MAE and higher half-life correlation than the power-law model, while the power-law model achieved a slightly higher AUC. [→ Utkarsh Upadhyay 2021](#utkarsh-upadhyay-2021)

## Evidence

### Utkarsh Upadhyay 2021

Utkarsh Upadhyay, Graham Lancashire, Christoph Moser, and Manuel Gomez-Rodriguez. (2021). Large-scale randomized experiment reveals machine learning helps people learn and remember more effectively. arXiv. Originally published 2020. [doi:10.1038/s41539-021-00105-8](https://doi.org/10.1038/s41539-021-00105-8)

`q2 · i?` · `causal · r2`

Benchmark evaluation of both fitted memory models on data from February 2019 to June 2019 (Table 2): exponential MAE 0.139 vs power-law 0.282; CORh 0.611 vs 0.571; AUC 0.887 vs 0.901. Based on these results the authors chose the exponential model for the trial.

> "In terms of mean average error (MAE) in predicting the recall of items and in terms of correlation between the predicted and empirically observed half-life for the items (COR h), the exponential model clearly outperforms the power-law model. However, in terms of Area Under the Curve (AUC), the power-law model performs slightly better than the exponential model."

## Discussion


## Related Claims
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related
- [In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.](exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) — related
- [Repeated retrieval practice alters the rate at which learned items are forgotten, according to learn-to-criterion studies and forgetting-curve analyses the chapter reviews](repeated-retrieval-alters-the-rate-of-forgetting.md) — related
