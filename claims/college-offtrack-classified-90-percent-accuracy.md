---
type: claim
title: Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors
description: Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors
id: college-offtrack-classified-90-percent-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: james-soland-2017
    resource: "https://www.nwea.org/research/publication/combining-academic-noncognitive-and-college-knowledge-measures-to-identify-students-not-on-track-for-college-a-data-driven-approach/"
    title: "James Soland. (2017). Combining Academic, Noncognitive, and College Knowledge Measures to Identify Students Not on Track For College: A Data-Driven Approach. Research & Practice in Assessment, Volume Twelve, Summer 2017. https://www.nwea.org/research/publication/combining-academic-noncognitive-and-college-knowledge-measures-to-identify-students-not-on-track-for-college-a-data-driven-approach/"
    author: James Soland
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Students not on track for college enrollment and persistence can be classified with about 90 percent accuracy using a small set of predictors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Random forest models classified 91 percent of training-set students and 88 percent of test-set students accurately on attending college and persisting for a semester. [→ James Soland 2017](#james-soland-2017)

## Evidence

### James Soland 2017

James Soland. (2017). Combining Academic, Noncognitive, and College Knowledge Measures to Identify Students Not on Track For College: A Data-Driven Approach. Research & Practice in Assessment, Volume Twelve, Summer 2017. https://www.nwea.org/research/publication/combining-academic-noncognitive-and-college-knowledge-measures-to-identify-students-not-on-track-for-college-a-data-driven-approach/

`q2 · i?` · `associational · r2`

Analysis of the nationally representative NELS sample of 12,144 baseline students, split roughly 70/30 into training and test sets; decision-tree-based data reduction models predicted attending college and persisting for a semester. The article reports "88 percent in the test set" accuracy, with similar lasso rates.

> "On average, random forest models accurately classified 91 percent of students in the training set and 88 percent in the test set—with far fewer false positives than in unweighted models. Classification rates were similar for the lasso models."

## Discussion


## Related Claims
- [The models' classification accuracy exceeds that of 97 percent of prior studies predicting high school completion](accuracy-exceeds-97-percent-of-prior-studies.md) — related
- [Gradient boosting and extreme gradient boosting are the highest-performing classifiers for predicting enrollment, with balanced accuracy 0.91, F-score 0.88 and AUC 0.96](gradient-boosting-best-enrollment-predictor-aid-optimization.md) — related
- [A few decision-tree splits identify very high-risk students, such as low-SES students who doubt they will reach college](few-splits-identify-high-risk-students.md) — a narrower finding that bears on this claim
