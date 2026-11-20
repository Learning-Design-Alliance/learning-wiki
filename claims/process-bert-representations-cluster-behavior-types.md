---
type: claim
title: Latent representations cluster into interpretable behavior types at question level, with less distinguishable task-switching clusters at student level
description: Latent representations cluster into interpretable behavior types at question level, with less distinguishable task-switching clusters at student level
id: process-bert-representations-cluster-behavior-types
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
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

# Latent representations cluster into interpretable behavior types at question level, with less distinguishable task-switching clusters at student level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Question-level latent vectors from the behavior-enhanced IRT model yield distinct t-SNE clusters, each representing a distinct behavior type combining granular features such as helper tool use with high-level features such as sequence length and number of visits. [→ Alexander Scarlatos 2022](#alexander-scarlatos-2022)
`q2 i?` Student-level latent vectors show clusters that are less clearly distinguishable than question-level ones but still include clusters corresponding to clear task-switching behavior in the time-limited assessment. [→ Alexander Scarlatos 2022 (2)](#alexander-scarlatos-2022-2)

## Evidence

### Alexander Scarlatos 2022

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Qualitative t-SNE visualization of question-level behavior vectors extracted from the behavior-enhanced IRT model for an early multiple choice question in block A, where the authors identify 6 distinct clusters (calculator use, many visits, text-to-speech, high effort), each representing "a unique combination of granular features".

> "These clusters appear to represent distinct behavior types, with each one representing a unique combination of granular features, such as the use of speciﬁc helper tools, and high- level features, such as sequence length or number of visits."

### Alexander Scarlatos 2022 (2)

Alexander Scarlatos, Christopher Brinton, and Andrew Lan. (2022). Process-BERT: A Framework for Representation Learning on Educational Process Data. [doi:10.48550/arXiv.2204.13607](https://doi.org/10.48550/arXiv.2204.13607)

`q2 · i?` · `design · r2`

Qualitative t-SNE visualization of student-level vectors from a modified model with a question ID prediction objective and a GRU over visit-level vectors, colored by score label; the authors identify 4 clusters (rapid testing, checked their work, ran out of time) showing "clear task-switching behavior in online assessments".

> "While the clusters for the student-level vectors are not as clearly distinguishable as those for the question- level vectors, we can still identify some clusters that correspond to clear task-switching behavior in online assessments."

## Discussion


## Related Claims
- [Unsupervised hierarchical clustering of knowledge vectors recovers expert bundle structure without bundle labels](clustering-recovers-expert-bundles.md) — related
- [Clustering yields a small number of behaviorally distinct team clusters that instructors can use for cluster-differentiated feedback](clustering-cluster-differentiated-feedback-ttx.md) — related
- [Cluster analysis of student-AI dialogue identifies three distinct collaboration profiles: Delegated Reasoning, Concerted Interpretation, and Delegated Elaboration](three-human-ai-cps-profiles-dr-ci-de.md) — related
- [K-means clustering of K–8 students' platform trace data yields seven distinct engagement profiles](seven-engagement-profiles-k8-elearning.md) — related
- [Hierarchical clustering of CDM attainment probabilities identifies five learner groups with distinct patterns of professional standards attainment](five-learner-profiles-standards-attainment.md) — related
- [Time series clustering of screened mathematics achievement data groups students into the same four interpretable trend clusters in two independent cohorts](time-series-clustering-four-interpretable-math-trend-clusters.md) — related
- [Exploratory K-means clustering identifies four heterogeneous student AI-user profiles differing in experience, competence, usefulness, trust, and control, but the solution's optimality and stability are not established](exploratory-four-cluster-student-ai-profiles.md) — related
- [Clustering practice behavior in an open-ended task yields five behavior types that differ significantly in normalized learning gain](five-practice-behavior-clusters-differ-learning-gain.md) — related
