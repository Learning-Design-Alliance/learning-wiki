---
type: claim
title: Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.
description: Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.
id: single-per-task-features-weak-fit
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2016
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

# Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For per-task recognition, single features reach very small p-values (number of hints seen: p = 2.2e-16) but Adjusted R2 values far from 1 (0.2499 for number of hints seen). [→ Ruth Janning 2016](#ruth-janning-2016)

## Evidence

### Ruth Janning 2016

Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9

`q2 · i?` · `associational · r1`

Statistical analysis of per-task log-file features mapped to perceived task-difficulty labels (hard, appropriate, easy) on 234 non-skipped labelled tasks from the 7-student study. Table 6 reports number of hints seen with p-value 2.2e-16 and R2 0.2531 (Adjusted R2 0.2499); the authors state the single-feature "p-values are very small" but fit is weak. No standardised effect size is printed.

> "In the case of single features (Table 6) the p-values are very small but unfortunately the (Adjusted) R2 values are not very close to 1. The best feature combination (Table 7) delivers also a very small p-value and a much better result for (Adjusted) R2."

## Discussion


## Related Claims
- [A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session.](log-feature-combination-significant-accumulated-difficulty.md) — related
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](svm-best-single-classifier-task-difficulty.md) — related
- [The generalised plait ensemble outperforms single classifiers, majority-vote and stacking ensembles, substantially improving perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%).](plait-ensemble-outperforms-single-and-standard-ensembles.md) — related
