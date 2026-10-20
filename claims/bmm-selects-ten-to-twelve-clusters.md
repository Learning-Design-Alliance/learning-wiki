---
type: claim
title: Bernoulli Mixture Model fits select around 10-12 clusters per question, with no runs finding high cluster counts optimal, indicating specialised skill sets do not generally exist
description: Bernoulli Mixture Model fits select around 10-12 clusters per question, with no runs finding high cluster counts optimal, indicating specialised skill sets do not generally exist
id: bmm-selects-ten-to-twelve-clusters
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
---

# Bernoulli Mixture Model fits select around 10-12 clusters per question, with no runs finding high cluster counts optimal, indicating specialised skill sets do not generally exist

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` BIC-optimised BMM fits mostly choose 10-12 clusters despite a parameter space extending to 64, so different specialised skill sets at each ability level do not generally seem to exist at high numbers. [→ Benjamin Mawdsley 2026](#benjamin-mawdsley-2026)

## Evidence

### Benjamin Mawdsley 2026

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)

`q2 · i?` · `associational · r2`

BMM cluster-count selection via Bayesian Information Criterion across k training folds for each question (Figure 6); the authors allowed up to 64 clusters but "no runs of the fitting found these high values of clusters to be optimal".

> "Most questions select around 10-12 clusters, with a decaying frequency of optimisation runs finding more clusters."

## Discussion


## Related Claims
- [Cluster profiles of student mathematics performance are dominated by overall ability, with most clusters being linear rescalings of average exam performance](cluster-profiles-dominated-by-overall-ability.md) — related
- [Mean skill diversity rises from low to moderate specialisation before declining among the most specialised workers](diversity-specialisation-inverse-u-pattern.md) — related
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Using performance on each individual question as features yields only a small improvement over a single-ability logistic regression model](small-gain-from-question-level-features.md) — a narrower finding that bears on this claim
- [Gaussian Mixture Modeling identifies two latent clusters of delayed start behavior, outperforming three-cluster and unimodal models](gmm-two-clusters-delayed-start.md) — related
