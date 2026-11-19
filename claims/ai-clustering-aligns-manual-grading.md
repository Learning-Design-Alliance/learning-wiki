---
type: claim
title: Clustering solutions by AI grading scores and similarity-of-approach roughly aligns with manual grading clusters and total scores
description: Clustering solutions by AI grading scores and similarity-of-approach roughly aligns with manual grading clusters and total scores
id: ai-clustering-aligns-manual-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: gerd-kortemeyer-2023
    resource: "https://doi.org/10.48550/arXiv.2304.11221"
    title: "Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)"
    author: Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Clustering solutions by AI grading scores and similarity-of-approach roughly aligns with manual grading clusters and total scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Clusters based on manual grading, AI grading, and AI similarity-of-approach roughly align with low, medium, and high total scores, with all measures placing the almost entirely wrong solutions in the low cluster. [→ Gerd Kortemeyer 2023](#gerd-kortemeyer-2023)

## Evidence

### Gerd Kortemeyer 2023

Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)

`q2 · i?` · `design · r2`

Cluster analysis using dendrograms and heat maps (Fig. 12, Table IV) of 25 solutions based on manual grading, AI grading, and AI-reported similarity-of-approach, clustered with the gplots package in R. Clusters "roughly align with the total points".

> "it turns out that they roughly align with the total points in Fig. 11, with the low, medium, and highly scored problems forming the clusters."

## Discussion


## Related Claims
- [LLMs show discoverability bias: they accurately identify only high-quality open-ended biology responses and miss nuanced misconceptions](llm-discoverability-bias-open-ended-biology-assessment.md) — related
- [Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses](llm-embedding-clusters-low-alignment-kps.md) — related
- [Clustering of TTX activity logs aligns with instructor-assigned milestone scores and outperforms a baseline averaged over all possible groupings in both exercises](clustering-ttx-team-assessment-aligns-instructor-scores.md) — related
- [Cluster-based sampling of single answers from clusters (cluster centroid and random cluster instance) required the least manual grading and correcting work, outperforming full-cluster and random sampling strategies](cluster-instance-sampling-minimizes-grading-work.md) — related
