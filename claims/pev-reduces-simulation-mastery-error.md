---
type: claim
title: Adding a Prior Error Valence (PEV) feature to a population-parameter model reduces systematic mastery-timing error in simulation
description: Adding a Prior Error Valence (PEV) feature to a population-parameter model reduces systematic mastery-timing error in simulation
id: pev-reduces-simulation-mastery-error
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
    kind: design
    rigour: 2
---

# Adding a Prior Error Valence (PEV) feature to a population-parameter model reduces systematic mastery-timing error in simulation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the simulation, the error-sensitive model EPFA reduced systematic error toward zero, halving the median absolute difference in predicted mastery trial (9 to 4). [→ Eglington 2022](#eglington-2022)

## Evidence

### Eglington 2022

Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0

`q2 · i?` · `design · r2`

Numerical simulation comparing PFAP (population parameters) with EPFA (PFA plus PEV) on the same 1000 simulated students; the article reports EPFA "reduced systematic error towards zero as practice accumulated". No effect size printed.

> "In this simulation, the median absolute difference between predicted and actual trial of mastery (i.e., predicting when correctness probability >=.95) for the PFAP was 9 vs. 4 for EPFA."

## Discussion


## Related Claims
- [EPFA estimates fewer trials to mastery for above-average students and more trials for below-average students relative to standard PFA](epfa-mastery-trials-by-student-level.md) — related
- [Learner models with individual-difference features (PEV, student-level proportional correctness) improve cross-validated fit on six educational datasets](individual-difference-features-improve-fit-six-datasets.md) — related
- [Adding PEV or student-level proportional correctness significantly reduces the absolute value of student-level signed error in all six datasets](pev-student-proportion-reduce-signed-error.md) — related
- [Learner models with population-level parameters systematically misestimate the trial of mastery for most students whose learning rates vary](population-parameters-systematic-mastery-error.md) — related
