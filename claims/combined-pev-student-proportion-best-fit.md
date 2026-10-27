---
type: claim
title: The combined model with both PEV and student-level proportional decay typically fit better than either feature alone
description: The combined model with both PEV and student-level proportional decay typically fit better than either feature alone
id: combined-pev-student-proportion-best-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2022
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

# The combined model with both PEV and student-level proportional decay typically fit better than either feature alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The RKC,SEPFA model including both features typically achieved the lowest cross-validated RMSE, implying the two features do not have identical effects. [→ Eglington 2022](#eglington-2022)

## Evidence

### Eglington 2022

Eglington, L.G., Pavlik, P.I. (2022). How to Optimize Student Learning Using Student Models That Adapt Rapidly to Individual Differences. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00296-0

`q2 · i?` · `design · r2`

Comparison of the five model variants' cross-validated RMSE across six datasets (Table 2); the rightmost column (RKC,SEPFA) shows the lowest RMSE in most datasets, e.g., .3954 (Andes), .4554 (Assistments), .4351 (MHE), .4006 (Cloze). No effect size printed.

> "The effect on RMSE was similar, although the model with both features included typically outperformed either separately (rightmost column, Table 2) which implies they do n ot have the same effects."

## Discussion


## Related Claims
- [Learner models with individual-difference features (PEV, student-level proportional correctness) improve cross-validated fit on six educational datasets](individual-difference-features-improve-fit-six-datasets.md) — a broader claim this one bears on
- [No single learner model was best across the six datasets, justifying a broad multi-model approach](no-single-learner-model-best-across-datasets.md) — related
- [Adding PEV or student-level proportional correctness significantly reduces the absolute value of student-level signed error in all six datasets](pev-student-proportion-reduce-signed-error.md) — related
