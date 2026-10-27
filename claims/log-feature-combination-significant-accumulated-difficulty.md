---
type: claim
title: "A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session."
description: "A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session."
id: log-feature-combination-significant-accumulated-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: ruth-janning-2016
    resource: "https://doi.org/10.1007/s40593-016-0097-9"
    title: "Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9"
    author: Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` A combination of average time until skip and average time until first hint request significantly predicts accumulated perceived task-difficulty (p = 0.00516, Adjusted R2 = 0.8923) in a study with 7 students. [→ Ruth Janning 2016](#ruth-janning-2016)

## Evidence

### Ruth Janning 2016

Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9

`q2 · i?` · `associational · r1`

Statistical analysis (multivariate linear regression mapping feature values to accumulated perceived task-difficulty labels) in the Recognising Accumulated Perceived Task-Difficulty section, on data from a study of 7 students solving 40 tasks. The authors report "p-value of 0.00516" and "(Adjusted) R2 value of 0.9282 (0.8923)" for the best 2-feature combination; no standardised effect size is printed.

> "The best feature combination consists of 2 features (average time until skip, average time until first hint request). The p-value of 0.00516 of this feature combination is small enough (compared to 0.05) and the (Adjusted) R2 value of 0.9282 (0.8923) of this feature combination is close enough to 1, to assume that this combination of features is statistically significant and hence is able to describe the behaviour of a student expressed as the accumulated perceived task-difficulty in our data."

## Discussion


## Learner Variables
- [Time and Continuity](../learner-variables/time-and-continuity.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.](single-per-task-features-weak-fit.md) — related
- [Not requesting any hints in at least one problem is related to greater wheel-spinning, consistent with help avoidance](hint-avoidance-related-greater-wheel-spinning.md) — related
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](svm-best-single-classifier-task-difficulty.md) — related
- [Students rarely request on-demand hints in this tutor, with no significant differences between conditions or proficiency groups](on-demand-hint-requests-rare-and-equivalent.md) — related
