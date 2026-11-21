---
type: strategy
id: concept-map-clustering-formative-assessment
title: Use clustering of learner concept-map graph metrics as formative assessment to detect experience outliers and reveal misconceptions
description: "Apply unsupervised and semi-supervised clustering of learner concept-map graph metrics as a formative assessment tool: the article states the approach 'can also be used to detect outliers overestimating their own expe..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: weihs-2025
    resource: "https://arxiv.org/abs/2508.03840"
    title: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. https://arxiv.org/abs/2508.03840"
    author: "Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H"
---

# Use clustering of learner concept-map graph metrics as formative assessment to detect experience outliers and reveal misconceptions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
Apply unsupervised and semi-supervised clustering of learner concept-map graph metrics as a formative assessment tool: the article states the approach 'can also be used to detect outliers overestimating their own experience in a field, and thus is a tool of formative assessment in both classroom and groups comprising learners of different disciplinary experience levels', with cluster insights serving 'to reveal misconceptions, and to structure a learning progression'.

## Design Implications

### Context
#### Requirements
- Participant concept maps converted into graph feature vectors with computed metrics
- For SSL refinement, a subset of experience labels confirmed by a disciplinary expert
#### Constraints
- Demonstrated on cloud-physics concept maps; the authors suggest the methodology could benefit educational research in any STEM discipline
- Best accuracies are close to 58% for SSL and 60% for the unsupervised method, so classification is not perfect

### Target Learners
- Classroom learners and mixed-experience groups
- University STEM learners

### Target Learning Goals
- Detecting learners who over- or under-estimate their own disciplinary experience
- Revealing misconceptions and structuring learning progressions

## Claims

- [Clustering favours merging Proficient and Expert learners into one Advanced level while Novice and Adept remain unseparated](../claims/clustering-favors-advanced-merge-novice-adept-unseparated.md) [+W]
- [Disciplinary experience is the learner characteristic that best explains variance in concept-map graph metrics](../claims/experience-best-explains-concept-map-graph-variance.md) [+W]
- [Node-level metrics are the most significant graph-derived metrics distinguishing learner experience groups](../claims/node-level-metrics-distinguish-experience-clusters.md) [+W]
- [Spectral clustering outperforms the other models in the low-variance threshold region](../claims/spectral-clustering-outperforms-low-variance-region.md) [+W]
- [Semi-supervised label propagation separates experience levels into distinct clusters with accuracy close to 58%](../claims/ssl-label-propagation-refines-experience-clusters.md) [+W]
- [The 3-clusters analysis yields better clustering performance than the 4-clusters analysis](../claims/three-experience-levels-clustering-outperforms-four.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Weihs, J.-P., Weihs, A., Gjerde, V., & Drange, H. (2025). Unsupervised and semi-supervised clustering methods to identify and refine participant experience levels in educational research. https://arxiv.org/abs/2508.03840. [doi:10.48550/arxiv.2508.03840](https://doi.org/10.48550/arxiv.2508.03840)
