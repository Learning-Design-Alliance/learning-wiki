---
type: claim
title: Unsupervised clustering of grading data shows Classical Mechanics problems are graded differently from other physics topics
description: Unsupervised clustering of grading data shows Classical Mechanics problems are graded differently from other physics topics
id: clustering-classical-mechanics-graded-differently
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: mok-2025
    resource: "https://doi.org/10.1088/1361-6552/adb92b"
    title: "Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)"
    author: Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Unsupervised clustering of grading data shows Classical Mechanics problems are graded differently from other physics topics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When all LLMs are considered together, k-means clustering of t-SNE-reduced grading features places Classical Mechanics questions in one cluster (cluster 1, bottom right of Fig. 17). [→ Mok 2025](#mok-2025)

## Evidence

### Mok 2025

Mok, Akhtar, Clare, Li, Ida, Ross, and Campanelli. (2025). Using AI Large Language Models for Grading in Education: A Hands-On Test for Physics. arXiv. Originally published 2024. [doi:10.1088/1361-6552/adb92b](https://doi.org/10.1088/1361-6552/adb92b)

`q2 · i?` · `design · r2`

Unsupervised analysis: normalised grades, normalised standard deviations, and human-AI differences per grading type were t-SNE reduced and k-means clustered with K = 3 chosen via elbow plot; CM solutions usually clustered in the bottom-right cluster.

> "When all LLMs are considered together, questions pertaining to classical mechanics seem to cluster in one place. This is shown in Fig. 17."

## Discussion


## Related Claims
- [Latent representations cluster into interpretable behavior types at question level, with less distinguishable task-switching clusters at student level](process-bert-representations-cluster-behavior-types.md) — related
- [Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies](cluster-instance-sampling-minimizes-grading-work.md) — related
- [K-means clustering of K–8 students' platform trace data yields seven distinct engagement profiles](seven-engagement-profiles-k8-elearning.md) — related
