---
type: claim
title: The data-mined moment-by-moment learning model predicts P(J) with a correlation of .676 under six-fold student-level cross-validation
description: The data-mined moment-by-moment learning model predicts P(J) with a correlation of .676 under six-fold student-level cross-validation
id: moment-by-moment-model-crossvalidated-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: moderate
newest_evidence: 2013
recheck_by: 2016
sources:
  - id: baker-et-al-2013
    resource: "https://doi.org/10.1080/10508406.2013.836653"
    title: "Ryan S. Baker, Arnon Hershkovitz, Lisa M. Rossi, Adam B. Goldstein & Sujith M. Gowda (2013). Predicting Robust Learning With the Visual Form of the Moment-by-Moment Learning Curve. Journal of the Learning Sciences, 22:4, 639-666. https://doi.org/10.1080/10508406.2013.836653"
    author: "Ryan S. Baker, Arnon Hershkovitz, Lisa M. Rossi, Adam B. Goldstein & Sujith M. Gowda"
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# The data-mined moment-by-moment learning model predicts P(J) with a correlation of .676 under six-fold student-level cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2016**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A linear regression model with M5' feature selection, trained on Bayesian training labels of learning, achieved a Pearson correlation of .676 with training labels under six-fold student-level cross-validation. [→ Baker et al. 2013](#baker-et-al-2013)

## Evidence

### Baker et al. 2013

Ryan S. Baker, Arnon Hershkovitz, Lisa M. Rossi, Adam B. Goldstein & Sujith M. Gowda (2013). Predicting Robust Learning With the Visual Form of the Moment-by-Moment Learning Curve. Journal of the Learning Sciences, 22:4, 639-666. https://doi.org/10.1080/10508406.2013.836653

`q2 · i?` · `associational · r1`

Model-building result: training labels of the probability a knowledge component was just learned were generated from BKT plus future correctness via Bayes's theorem, then a data-mined model using only present-action features (no future data) was fit in RapidMiner. The correlation is a model fit metric, not an effect size.

> "The P(J) model achieved a solid correlation of .676 with the training labels under six-fold student-level cross-validation."

## Discussion


## Related Claims
- [Machine-learned P(J) models predict moment-of-learning training labels with cross-validated correlations around 0.40-0.45 in two intelligent tutoring systems.](pj-model-predicts-moment-of-learning-labels.md) — related
- [The two-fold training process suffers from overfitting due to the small labeled training set relative to feature dimensionality.](overfitting-from-small-labeled-set-and-high-dimensionality.md) — related
