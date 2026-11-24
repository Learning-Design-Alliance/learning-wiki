---
type: claim
title: In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)
description: In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)
id: interaction-data-improves-mcas-prediction-0405
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

# In the ASSISTment system, models using tutoring-interaction data predict end-of-year MCAS math scores better than a correctness-only IRT model (2004-05 data)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 2004-05 data (391 students), the mixed model combining IRT proficiency with assistance metrics correlated with MCAS scores at r = .841, reliably better than the lean model's .733. [→ Feng 2009](#feng-2009)
`q2 i?` The assistance model, using interaction information alone without original-question correctness, outperformed the lean model (r = .821 vs .733). [→ Feng 2009](#feng-2009)

## Evidence

### Feng 2009

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the Assessment Challenge with an Online System That Tutors as it Assesses. User Modeling and User-Adapted Interaction: The Journal of Personalization Research (UMUAI journal), 19(3), 243-266. http://www.doe.mass.edu/mcas/2002/results/summary.pdf

`q2 · i?` · `associational · r2`

Regression modeling on 2004-05 ASSISTment logs for 391 8th graders, comparing lean (IRT correctness-only), help, assistance and mixed models via MAD, BIC and correlation with 2005 MCAS raw scores; paired t-tests showed successive improvements were reliable (p = .031, .004, .001). The mixed model "correlates with MCAS scores fairly well (r = .841)".

> "As we can see in Table 2, the help model correlates reliably better with MCAS score than the lean model, suggesting that in ASSISTments, student help-seeking behavior is helpful in improving MCAS score prediction."

## Discussion


## Related Claims
- [Most ASSISTment online metrics correlate significantly with MCAS scores; Attempt_Count and Avg_Question_Time do not](assistment-metrics-mcas-correlations.md) — related
- [Mixed models trained on one school year generalize to another year's data (r = .827 and .824), with offsets explained by year-to-year MCAS difficulty shifts](cross-year-model-generalization-mcas.md) — related
- [The interaction-data advantage replicates on 2005-06 data (mixed model r = .853), though the help model no longer reliably beats the assistance model](interaction-data-improves-mcas-prediction-0506.md) — related
- [The mixed model validates within the same school year via 50% split cross-validation (r = .842 training, r = .837 testing)](same-year-cross-validation-mixed-model.md) — related
- [Among regular students, higher ASSISTments usage predicted higher 7th-grade MCAS performance](assistments-student-usage-predicts-mcas-regular.md) — related
- [Seventh graders using ASSISTments significantly outperformed comparison students on year-end MCAS scores after adjusting for prior-year scores](assistments-year-long-use-raises-mcas-scores.md) — related
