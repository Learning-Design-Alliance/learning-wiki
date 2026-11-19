---
type: claim
title: Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data
description: Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data
id: synthetic-training-tree-embeddings-outperform-real-data
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

# Training on synthetically generated steps, tree embedding-based methods significantly outperform GRU and CNN encoders when tested on real student data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When trained on 7,000 synthetically generated steps and tested on real CogTutor subsets, TE+C significantly outperforms GRU+C and CNN+C on all data subsets. [→ Mengxue Zhang 2021](#mengxue-zhang-2021)

## Evidence

### Mengxue Zhang 2021

Mengxue Zhang, Zichao Wang, Richard Baraniuk, Andrew Lan. (2021). Math Operation Embeddings for Open-ended Solution Analysis and Feedback. [doi:10.48550/arXiv.2104.12047](https://doi.org/10.48550/arXiv.2104.12047)

`q2 · i?` · `design · r2`

Numerical experiment (Section 5.4.3, Table 4) training on 7,000 synthetic steps and testing on OK, ERROR, and BUG subsets of real CogTutor data; TE+C reaches 83.79±0.14 on OK versus 62.89±3.93 for GRU+C, and "TE+C signif- icantly outperforms GRU+C and CNN+C on all data sub- sets".

> "We see that TE+C signif- icantly outperforms GRU+C and CNN+C on all data sub- sets, which is in stark contrast to the previous experiment where the diﬀerence in performance across all methods is much smaller."

## Discussion


## Related Claims
- [Learned math operation representations identify the operation a student intended in incorrect solution steps with up to 95% accuracy despite training only on correct steps](operation-representations-generalize-incorrect-steps.md) — related
- [Pre-training on synthetic data before fine-tuning on limited real data improves math operation classification accuracy, with the largest gains when real data is extremely limited](synthetic-pretraining-finetuning-limited-real-data.md) — possibly the same claim (merge candidate)
- [Tree embedding-based encoding with a classifier achieves the highest math operation classification accuracy on the CogTutor OK subset and remains effective on incorrect steps](tree-embedding-classifier-best-operation-classification.md) — related
- [Tree embedding-based encoding outperforms GRU-based encoding when generalizing across question difficulty levels in equation solving](tree-embeddings-outperform-gru-across-difficulty-levels.md) — related
- [Tree embedding-based encoding with a classifier performs best at classifying feedback types for incorrect steps, reaching 78.71% accuracy across 24 feedback types](tree-embedding-best-feedback-type-classification.md) — related
