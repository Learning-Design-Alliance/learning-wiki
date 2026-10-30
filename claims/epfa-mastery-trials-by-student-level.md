---
type: claim
title: EPFA estimates fewer trials to mastery for above-average students and more trials for below-average students relative to standard PFA
description: EPFA estimates fewer trials to mastery for above-average students and more trials for below-average students relative to standard PFA
id: epfa-mastery-trials-by-student-level
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
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

# EPFA estimates fewer trials to mastery for above-average students and more trials for below-average students relative to standard PFA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the KDD dataset, the average better-performing student was estimated to need 2.7 fewer trials to mastery per KC under EPFA, while the average lower-performing student was estimated to need 2.2 more trials. [→ Eglington 2022](#eglington-2022)

## Evidence

### Eglington 2022

Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0

`q2 · i?` · `design · r2`

Post-hoc analysis comparing PFA and EPFA estimated trials to mastery (correctness probability >= .95) per student per dataset, partitioning students above versus below average. Directional difference reported descriptively; no test statistic or effect size printed.

> "the average better-performing student in the KDD dataset was estimated to need 2.7 fewer trials to mastery per KC on average, and the average lower-performing student was estimated to need 2.2 more trials to achieve mastery per KC on average."

## Discussion


## Related Claims
- [Adding a Prior Error Valence (PEV) feature to a population-parameter model reduces systematic mastery-timing error in simulation](pev-reduces-simulation-mastery-error.md) — related
- [Learner models with population-level parameters systematically misestimate the trial of mastery for most students whose learning rates vary](population-parameters-systematic-mastery-error.md) — related
