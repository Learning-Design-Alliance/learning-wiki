---
type: claim
title: A pre-trained essay argument mining system (wLDA) performs poorly when applied off-the-shelf to classroom discussions, performing comparably to a majority baseline
description: A pre-trained essay argument mining system (wLDA) performs poorly when applied off-the-shelf to classroom discussions, performing comparably to a majority baseline
id: pretrained-essay-argument-miner-poor-on-classroom-discussions
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

# A pre-trained essay argument mining system (wLDA) performs poorly when applied off-the-shelf to classroom discussions, performing comparably to a majority baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The pre-trained wLDA system achieves kappa 0.077 on classroom discussions, comparable to the majority baseline (kappa 0.068), showing claims and evidence in essays and classroom discussions have very little in common. [→ Luca Lugini and Diane Litman 2018](#luca-lugini-and-diane-litman-2018)

## Evidence

### Luca Lugini and Diane Litman 2018

Luca Lugini and Diane Litman. (2018). Argument Component Classification for Classroom Discussions. [doi:10.18653/v1/w18-5208](https://doi.org/10.18653/v1/w18-5208)

`q2 · i?` · `design · r2`

Leave-one-transcript-out cross-validation evaluation of the pre-trained wLDA system on the classroom discussion corpus (Table 3, row 2: kappa 0.077 vs majority baseline 0.068). The authors conclude essays and discussions have "very little in common".

> "we can see that it is comparable to a majority baseline which always predicts the majority class in each fold. This result shows that claims and evidence expressed in written essays and classroom discussions have very little in common."

## Discussion


## Related Claims
- [Retraining a logistic regression classifier on classroom discussions with wLDA features plus online dialogue features achieves the best kappa overall](wlda-plus-online-dialogue-features-best-kappa.md) — related
- [Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features](handcrafted-features-improve-neural-argument-classifiers.md) — related
