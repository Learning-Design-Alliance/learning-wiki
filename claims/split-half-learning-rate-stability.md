---
type: claim
title: Split-half stability analysis shows fitted learning-rate parameters are meaningful, with Spearman correlations between 0.5 and 0.7 across independent data halves
description: Split-half stability analysis shows fitted learning-rate parameters are meaningful, with Spearman correlations between 0.5 and 0.7 across independent data halves
id: split-half-learning-rate-stability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2015
sources:
  - id: pelánek-2015
    resource: "https://doi.org/10.1007/s40593-015-0048-x"
    title: "Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x"
    author: "Pelánek, R., & Jarušek, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Split-half stability analysis shows fitted learning-rate parameters are meaningful, with Spearman correlations between 0.5 and 0.7 across independent data halves

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When data are split into two disjoint halves and one model is trained on each, student learning rate estimates correlate between 0.5 and 0.7, signaling the fitted parameters contain meaningful values. [→ Pelánek 2015](#pelanek-2015)

## Evidence

### Pelánek 2015

Pelánek, R., & Jarušek, P. (2015). Student Modeling Based on Problem Solving Times. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0048-x

`q2 · i?` · `design · r2`

Stability experiment on real tutor data: two models trained on disjoint halves, Spearman correlations between parameter values (Table 4). Difficulty correlated most highly; the learning rate "correlation coefficient between 0.5 and 0.7"; discrimination correlated weakest.

> "For students’ learning rate, the additional parameter of the extended model, we get the correlation coefficient between 0.5 and 0.7 – a significant correlation which signals that the fitted parameters contain meaningful values."

## Discussion


## Related Claims
- [Allowing ACT-R memory parameters to vary with the between-session interval produces a strong fit between model and recall data across timescales](time-variant-parameters-capture-retention-across-timescales.md) — related
- [In 5-fold cross-validation, multi-bin time-variant model fits outperform single-bin fits, with diminishing returns beyond a 5-bin split and further gains from differentiating by learner and amount of practice](cross-validation-favors-time-variant-fits.md) — related
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
