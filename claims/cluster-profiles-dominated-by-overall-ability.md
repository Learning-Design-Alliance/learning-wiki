---
type: claim
title: Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance
description: Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance
id: cluster-profiles-dominated-by-overall-ability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: benjamin-mawdsley-2026
    resource: "https://doi.org/10.48550/arxiv.2607.26063"
    title: "Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)"
    author: Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: benjamin-mawdsley-2026-2
    resource: "https://arxiv.org/abs/2607.26063"
    title: "Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063"
    author: Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Most BMM clusters are strongly linearly correlated with each other and with average exam score, indicating overall ability rather than distinct skill profiles drives cluster shape. [→ Benjamin Mawdsley 2026](#benjamin-mawdsley-2026)
`q2 i?` A small number of cluster pairs show near zero or slightly negative correlation, suggesting small atypical subgroups that may benefit from increased personalisation. [→ Benjamin Mawdsley 2026 (2)](#benjamin-mawdsley-2026-2)

## Evidence

### Benjamin Mawdsley 2026

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)

`q2 · i?` · `associational · r2`

Analysis of Bernoulli Mixture Model clusters fitted to mock exam data from the platform. The authors use Pearson correlation between all pairs of clusters, finding most clusters have linear correlation above 0.6, showing "performance on each questions typically scales linearly with overall exam performance".

> "The dominant factor is ability and performance on each questions typically scales linearly with overall exam performance."

### Benjamin Mawdsley 2026 (2)

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063

`q2 · i?` · `associational · r2`

In the same cluster-correlation analysis of BMM outputs, the authors report that "a small number of cluster pairs have a near zero or slightly negative correlation", identifying rare atypical profiles; Appendix B gives an example of two differing high-performer populations.

> "A small number of cluster pairs have a near zero or slightly negative correlation, indicating that there may be small subsets of the population that have atypical behaviour and may benefit from increased personalisation."

## Discussion


## Learner Variables
- [General Cognitive Ability](../learner-variables/general-cognitive-ability.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Bernoulli Mixture Model fits select around 10-12 clusters per question, with no runs finding high cluster counts optimal, indicating specialised skill sets do not generally exist](bmm-selects-ten-to-twelve-clusters.md) — related
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model](small-gain-from-question-level-features.md) — related
