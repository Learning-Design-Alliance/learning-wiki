---
type: claim
title: "Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category."
description: "Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category."
id: communication-strategy-most-impactful-ablation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In ablation analysis of the best classifier, removing the teacher's communication strategy feature yields the greatest accuracy reduction (3.25% on average per the discussion), while removing teaching objective has the smallest effect. [→ Vasileios Lampos 2021](#vasileios-lampos-2021)

## Evidence

### Vasileios Lampos 2021

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r1`

Ablation analysis of the GP-α (τ = 1) classifier on the 5460-observation dataset using a single covariance kernel, with Table 4 enumerating accuracy when each feature category is excluded. The article finds "omitting the communication strategy of the teacher yields the greatest negative impact to the classifier's accuracy". No effect size printed.

> "When we reverse this experiment, excluding one specific feature category at a time, we can see that omitting the communication strategy of the teacher yields the greatest negative impact to the classifier's accuracy."

## Discussion


## Related Claims
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](ablation-trust-module-largest-contribution.md) — related
- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](ablation-metadata-embeddings-largest-accuracy-drop.md) — related
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — related
- [In the classifier's expanded sample of over 2.6 million observations, negative student emotional state (r = −0.431) and physical prompt communication (r = 0.341) show the strongest correlations with full student response.](expanded-sample-correlations-emotion-physical-prompt.md) — related
- [Ablation testing shows simplification and ordering transformations contribute most to canonical reduction, while many domain-specific functions had no effect](ablation-simplification-ordering-transformations-most-effective.md) — related
