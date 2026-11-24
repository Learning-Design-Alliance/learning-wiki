---
type: claim
title: The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model
description: The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model
id: interaction-data-improves-mcas-prediction-0506
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-24
evidence_strength: moderate
newest_evidence: 2009
recheck_by: 2012
sources:
  - id: feng-2009
    resource: "http://www.doe.mass.edu/mcas/2002/results/summary.pdf"
    title: "Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf"
    author: "Feng, M., Heffernan, N.T., & Koedinger, K.R."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 2005-06 data (616 students), the mixed model correlated with 2006 MCAS scores at .853, reliably higher than the other models. [→ Feng 2009](#feng-2009)
`q2 i?` The difference between the help model and the assistance model was not reliable in 2005-06 (p = .693), unlike 2004-05. [→ Feng 2009](#feng-2009)

## Evidence

### Feng 2009

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf

`q2 · i?` · `associational · r2`

Replication of the four-model regression on 2005-06 logs from 616 Worcester 8th graders (mean 196 minutes, 88 items). The mixed model again fit best (MAD 4.89, R Square 0.728); assistance and mixed models remained reliably better than the lean model (p < .001).

> "The adjusted predicted score correlated with the 2006 MCAS test scores at .853, which is reliably higher than the correlation between the other models and the MCAS scores. The ranking of the other three models is the same as the ranking we got from using the 2004-2005 data except that the difference between the help model and the assistance model is no longer reliable (*p* = .693)."

## Discussion


## Related Claims
- [Most ASSISTment online metrics correlate significantly with MCAS scores; Attempt_Count and Avg_Question_Time do not](assistment-metrics-mcas-correlations.md) — related
- [Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts](cross-year-model-generalization-mcas.md) — related
- [In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)](interaction-data-improves-mcas-prediction-0405.md) — related
- [The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)](same-year-cross-validation-mixed-model.md) — related
