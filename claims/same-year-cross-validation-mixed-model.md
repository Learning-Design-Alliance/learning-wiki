---
type: claim
title: "The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)"
description: "The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)"
id: same-year-cross-validation-mixed-model
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

# The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training the mixed model on a random half of 2004-05 data yielded r = .842 with 2005 MCAS scores, and it fit the held-out half at r = .837, MAD = 5.25. [→ Feng 2009](#feng-2009)

## Evidence

### Feng 2009

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf

`q2 · i?` · `associational · r2`

Same-year cross-validation on 2004-05 data: SPSS randomly selected 203 training cases; the held-out 188 testing cases fit at r = .837, MAD = 5.25, with the same variables and coefficient signs as the full-sample model. The reverse split gave a similar result.

> "We were glad to see that the mixed model correlated with the 2005 MCAS score with r equal to .842 (*p* < .01). The resulting model was very similar to the one shown in Table 3, where the same variables entered the model and the sign of all the coefficients were in the same direction as before"

## Discussion


## Related Claims
- [Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts](cross-year-model-generalization-mcas.md) — related
- [In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)](interaction-data-improves-mcas-prediction-0405.md) — related
- [The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model](interaction-data-improves-mcas-prediction-0506.md) — related
