---
type: claim
title: Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps
description: Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps
id: tree-embedding-classifier-best-operation-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: mengxue-zhang-2021
    resource: "https://doi.org/10.48550/arXiv.2104.12047"
    title: "Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)"
    author: Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the OK subset, tree embedding-based encoding with a classifier reaches 99.82% accuracy and GRU-based encoding 99.18%, while CNN-based encoding performs worse and TransE/TransR frameworks perform lower on incorrect-step subsets. [→ Mengxue Zhang 2021](#mengxue-zhang-2021)

## Evidence

### Mengxue Zhang 2021

Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)

`q2 · i?` · `design · r2`

Numerical experiments on the CogTutor dataset (Table 2) training on the OK subset and testing on OK, ERROR, and BUG subsets; TE+C reaches 99.82±0.04 on OK, and "GRU-based encoding and tree embedding-based encoding in conjunction with a classiﬁer result in the best performance."

> "Accuracy is high across the board, while GRU-based encoding and tree embedding-based encoding in conjunction with a classiﬁer result in the best performance."

## Discussion


## Related Claims
- [Learned math operation representations identify the operation a student intended in incorrect solution steps with up to 95% accuracy despite training only on correct steps](operation-representations-generalize-incorrect-steps.md) — related
- [Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data](synthetic-training-tree-embeddings-outperform-real-data.md) — related
- [Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types](tree-embedding-best-feedback-type-classification.md) — related
- [Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving](tree-embeddings-outperform-gru-across-difficulty-levels.md) — related
