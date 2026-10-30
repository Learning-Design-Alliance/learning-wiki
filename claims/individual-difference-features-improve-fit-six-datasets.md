---
type: claim
title: Learner models with individual-difference features (PEV, student-level proportional correctness) improve cross-validated fit on six educational datasets
description: Learner models with individual-difference features (PEV, student-level proportional correctness) improve cross-validated fit on six educational datasets
id: individual-difference-features-improve-fit-six-datasets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: eglington-2022
    resource: "https://doi.org/10.1007/s40593-022-00296-0"
    title: "Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0"
    author: Eglington, L.G., Pavlik, P.I.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Learner models with individual-difference features (PEV, student-level proportional correctness) improve cross-validated fit on six educational datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across six datasets, models including features adjusting for individual differences achieved lower student-stratified cross-validated RMSE than PFAP or RKCPFA. [→ Eglington 2022](#eglington-2022)

## Evidence

### Eglington 2022

Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0

`q2 · i?` · `associational · r2`

Analysis of six datasets (Andes, Assistments, Cognitive Tutor/KDD, Chinese tones, McGraw Hill, statistics cloze) fit with five logistic-regression model variants using 10-fold student-stratified cross-validation. Improvement was found "in all tested datasets"; no effect size printed.

> "Overall, models that included features to adjust for individual differences improved fit relative to PFAP or RKCPFA in terms of student-stratified cross-validated RMSE (see Table 2). We also found a benefit of RKCPFA over PFAP in 4 of 6 datasets."

## Discussion


## Related Claims
- [The combined model with both PEV and student-level proportional decay typically fit better than either feature alone](combined-pev-student-proportion-best-fit.md) — a narrower finding that bears on this claim
- [Adding PEV or student-level proportional correctness significantly reduces the absolute value of student-level signed error in all six datasets](pev-student-proportion-reduce-signed-error.md) — a narrower finding that bears on this claim
- [Adding a Prior Error Valence (PEV) feature to a population-parameter model reduces systematic mastery-timing error in simulation](pev-reduces-simulation-mastery-error.md) — related
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — related
