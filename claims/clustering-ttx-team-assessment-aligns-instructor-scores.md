---
type: claim
title: Clustering of TTX activity logs aligns with instructor-assigned milestone scores and outperforms the random-grouping baseline in both exercises
description: Clustering of TTX activity logs aligns with instructor-assigned milestone scores and outperforms the random-grouping baseline in both exercises
id: clustering-ttx-team-assessment-aligns-instructor-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: v-švábenský-2026
    resource: "https://arxiv.org/abs/2607.19209"
    title: "V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209"
    author: V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Clustering of TTX activity logs aligns with instructor-assigned milestone scores and outperforms the random-grouping baseline in both exercises

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In both TTXs, cluster cohesion measured by RMSE against instructor milestone scores was much lower than the baseline average across all possible cluster groupings, so clustering sufficiently aligns with instructor scores and outperforms the baseline. [→ V. Švábenský 2026](#v-svabensky-2026)

## Evidence

### V. Švábenský 2026

V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209

`q2 · i?` · `design · r2`

Quantitative comparison (RQ1) of DBSCAN-based consensus clustering outputs against instructor milestone-score vectors for 13 EXF teams and 10 PHI teams, using pairwise RMSE with the average across all Bell-number groupings as baseline; clustering RMSE was lower than baseline in both exercises (e.g., EXF 0.45 vs 0.53 baseline).

> "Based on Table III, the baseline RMSE (average error across all these options) is much larger than for our clustering results. Therefore, our assessment has better internal cohesion of the clusters with respect to the manually assigned scores."

## Discussion


## Related Claims
- [Clustering yields a small number of behaviorally distinct team clusters that instructors can use for cluster-differentiated feedback](clustering-cluster-differentiated-feedback-ttx.md) — related
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Q-matrices clustered from DKT and skip-gram item embeddings do not outperform dAFM models but do outperform a randomly initialized Q-matrix](embedding-clustered-qmatrices-null-versus-dafm.md) — related
