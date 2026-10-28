---
type: claim
title: STEM students show a higher mastery level and a higher learning gain in mathematics than non-STEM students.
description: STEM students show a higher mastery level and a higher learning gain in mathematics than non-STEM students.
id: stem-students-higher-mastery-and-learning-gain-in-mathematics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2018
sources:
  - id: yeung-2018
    resource: "https://arxiv.org/abs/1806.03256"
    title: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256"
    author: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y."
    q: 2
    i: 2
    kind: associational
    rigour: 1
  - id: yeung-2018-2
    resource: "https://arxiv.org/abs/1806.03256"
    title: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256"
    author: "Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# STEM students show a higher mastery level and a higher learning gain in mathematics than non-STEM students.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i2` medium
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i2` Independent t-tests on the student profile show the STEM class has higher mean values on AveCarelessness, AveKnow and AveCorrect, with Cohen's d of -0.47, -0.45 and -0.44 respectively. [→ Yeung 2018](#yeung-2018)
`q2 i?` A one-tailed hypothesis test on normalized learning gain computed from DKT+ knowledge states rejects the null hypothesis with a p-value of 0.0072, concluding STEM students have a higher knowledge gain in mathematics. [→ Yeung 2018 (2)](#yeung-2018-2)

## Evidence

### Yeung 2018

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i2` · `associational · r1`

Independent sample t-tests on student-profile attributes between STEM and non-STEM classes (Section 2.2, Table 1). The STEM class has higher means on AveKnow and AveCorrect; the printed Cohen's d values are -0.45 for AveKnow and -0.44 for AveCorrect, described as "a large magnitude in t-score and Cohen's d".

> "Furthermore, “AveKnow”, “AveCorrect” and “AveCareless-ness” seem to be potent predictors, as they have a large magnitude in t-score and Cohen’s d as well as a small p-value, indicating the STEM and the non-STEM classes have diﬀerent mean values in these attributes with a high conﬁdence level."

### Yeung 2018 (2)

Yeung, C.-K., Lin, Z., Yang, K., & Yeung, D.-Y. (2018). Incorporating Features Learned by an Enhanced Deep Knowledge Tracing Model for STEM/Non-STEM Job Prediction. arXiv preprint arXiv:1806.03256. https://arxiv.org/abs/1806.03256

`q2 · i?` · `associational · r1`

One-tailed hypothesis test on normalized learning gain adapted to DKT+ knowledge states (Section 5.2.3). The average NLG for STEM students is 0.065 (SD 0.172) and for non-STEM students 0.023 (SD 0.146); the null hypothesis is rejected "with a p-value of 0.0072".

> "As a result, the null hypothesis H0 is rejected with a p-value of 0.0072. It is concluded that STEM students have a higher knowledge gain in mathematics than non-STEM students after the use of the ASSISTments, indicating the STEM class has a higher ability in learning mathematics."

## Discussion


## Related Claims
- [Models trained with combined DKT/DKT+ knowledge-state and student-profile features generally outperform models trained with student profile alone on STEM/non-STEM job prediction.](combined-dkt-knowledge-state-features-improve-stem-job-prediction.md) — related
- [DKT+ knowledge states discriminate STEM from non-STEM students better than DKT knowledge states for the majority of mathematical skills.](dkt-plus-knowledge-state-better-discrimination-than-dkt.md) — related
