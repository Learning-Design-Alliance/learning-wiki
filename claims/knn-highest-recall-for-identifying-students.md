---
type: claim
title: k-nearest neighbours achieves the highest recall of the tested models, making it better suited when identifying which students know a topic matters
description: k-nearest neighbours achieves the highest recall of the tested models, making it better suited when identifying which students know a topic matters
id: knn-highest-recall-for-identifying-students
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

# k-nearest neighbours achieves the highest recall of the tested models, making it better suited when identifying which students know a topic matters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` KNN scores highest for recall, capturing more students who get a question correct, and consequently has the highest F1 despite a higher log loss than BMM and multi-question logistic regression. [→ Benjamin Mawdsley 2026](#benjamin-mawdsley-2026)

## Evidence

### Benjamin Mawdsley 2026

Benjamin Mawdsley, Tom Quilter, Richard Turner, Sarah Jackson, and Paul Edwards. (2026). Archetypes or ability? Clustering for modelling student mathematical competence. https://arxiv.org/abs/2607.26063 [doi:10.48550/arxiv.2607.26063](https://doi.org/10.48550/arxiv.2607.26063)

`q2 · i?` · `associational · r2`

Model comparison in the predictive evaluation (Table 1: KNN recall 0.769±0.014 versus LogRegm 0.759±0.014 and BMM 0.754±0.015); the authors suggest KNN "may be the better suited model" when prioritising topics to revise.

> "Interestingly, the KNN approach scores highest for recall, meaning that it captures more of the students who get a question correct. In cases where capturing which students know a topic is important, such as when prioritising which topics to revise, it may be the better suited model."

## Discussion


## Related Claims
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
