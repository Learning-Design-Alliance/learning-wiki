---
type: claim
title: "Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts"
description: "Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts"
id: cross-year-model-generalization-mcas
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
  - id: feng-2009-2
    resource: "http://www.doe.mass.edu/mcas/2002/results/summary.pdf"
    title: "Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf"
    author: "Feng, M., Heffernan, N.T., & Koedinger, K.R."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cross-year testing showed the 04-05-trained mixed model correlated .827 with 2006 MCAS scores and the 05-06-trained model correlated .824 with 2005 scores, both significant at the .01 level. [→ Feng 2009](#feng-2009)
`q2 i?` The 2006 MCAS test was reliably easier than the 2005 test for Worcester students (46% vs 42% correct, p < .05), explaining under-/over-prediction; a 3-point correction lowered MADs by .7 points in both cases. [→ Feng 2009 (2)](#feng-2009-2)

## Evidence

### Feng 2009

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf

`q2 · i?` · `associational · r2`

Cross-year validation of the mixed models: each year's model was tested on the other year's data (Table 8), with MADs of 5.82 and 6.55 before correction. The article states the strong correlations protected against overfitting.

> "the predicted scores tested on the 2005-2006 data correlated with the 2006 MCAS with the correlation coefficient equal to .827 and the correlation is .824 for the model tested on 2004-2005 data. And both correlations are significant at the .01 level."

### Feng 2009 (2)

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf

`q2 · i?` · `associational · r1`

Secondary analysis comparing Worcester students' percent correct across the two years' MCAS tests via two-sample t-test; threshold raw scores also shifted 3 points higher in 2006. A simple 3-point correction lowered MAD from 5.89 to 5.16 and 6.49 to 5.80.

> "the students from Worcester got 42% correct on the 2005 MCAS test and 46% correct on the 2006 MCAS test which is statistically reliably higher than that of the 2005 test suggested by the two sample t-test of the two groups of students (*p* < .05)."

## Discussion


## Related Claims
- [The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)](same-year-cross-validation-mixed-model.md) — related
- [The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model](interaction-data-improves-mcas-prediction-0506.md) — related
- [In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)](interaction-data-improves-mcas-prediction-0405.md) — related
