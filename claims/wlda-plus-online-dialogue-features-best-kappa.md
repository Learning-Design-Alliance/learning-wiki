---
type: claim
title: Retraining a logistic regression classifier on classroom discussions with wLDA features plus online dialogue features achieves the best kappa overall
description: Retraining a logistic regression classifier on classroom discussions with wLDA features plus online dialogue features achieves the best kappa overall
id: wlda-plus-online-dialogue-features-best-kappa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: luca-lugini-and-diane-litman-2018
    resource: "https://doi.org/10.18653/v1/w18-5208"
    title: "Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)"
    author: Luca Lugini and Diane Litman
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Retraining a logistic regression classifier on classroom discussions with wLDA features plus online dialogue features achieves the best kappa overall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding the online dialogue feature set to a logistic regression model trained with wLDA features on classroom discussions improves all results and obtains the best kappa overall (0.283). [→ Luca Lugini and Diane Litman 2018](#luca-lugini-and-diane-litman-2018)

## Evidence

### Luca Lugini and Diane Litman 2018

Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)

`q2 · i?` · `design · r2`

Cross-validation experiment (Table 3, row 4) training logistic regression on wLDA features plus online dialogue features; kappa 0.283, precision 0.508, recall 0.500, f-score 0.480. The authors state this "confirms our hypothesis" that online dialogue features are useful in classroom discussions.

> "if we add to this model the online dialogue feature set, the resulting model improves all results and obtains the best kappa overall (row 4)."

## Discussion


## Related Claims
- [Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features](handcrafted-features-improve-neural-argument-classifiers.md) — related
- [A pre-trained essay argument mining system (wLDA) performs poorly when applied off-the-shelf to classroom discussions, performing comparably to a majority baseline](pretrained-essay-argument-miner-poor-on-classroom-discussions.md) — related
- [Multi-task learning with specificity prediction as a secondary task almost always improves argument component classification, and yields the only model with warrant f-score above 0.3](multi-task-specificity-improves-argument-classification.md) — related
