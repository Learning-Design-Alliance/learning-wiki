---
type: claim
title: "Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error)."
description: "Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error)."
id: svm-best-single-classifier-task-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2016
sources:
  - id: ruth-janning-2016
    resource: "https://doi.org/10.1007/s40593-016-0097-9"
    title: "Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9"
    author: Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Applied to per-task log-file features with leave-one-student-out cross-validation, SVM achieved 25.24% average classification test error, outperforming KNN (29.62%) and DCT (30.62%). [→ Ruth Janning 2016](#ruth-janning-2016)

## Evidence

### Ruth Janning 2016

Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9

`q2 · i?` · `design · r2`

Multi-class classification experiments (classes hard, appropriate, easy) on 234 labelled tasks from the 7-student study, using leave-one-student-out cross-validation with oversampling for balancing. SVM with RBF-kernel, DCT and KNN were compared; the authors conclude the features "are suitable for recognising the perceived task-difficulty per task". Only test error and F-measures are printed, no effect size.

> "These first experiments delivered an average classification test error of 25.24 % for the SVM, of 29.62 % for KNN and of 30.62 % for the DCT as well as F-measures for the 3 classes of 0.67, 0.68, 0.84 for the SVM, of 0.66, 0.67, 0.80 for KNN and of 0.60, 0.63, 0.83 for the DCT (see Table 9). These results show, that the features are suitable for recognising the perceived task-difficulty per task and that SVM performed best."

## Discussion


## Related Claims
- [The generalised plait ensemble outperforms single classifiers, majority-vote and stacking ensembles, substantially improving perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%).](plait-ensemble-outperforms-single-and-standard-ensembles.md) — related
- [Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.](single-per-task-features-weak-fit.md) — related
- [A two-feature combination of average time until skip and average time until first hint request statistically significantly describes students' accumulated perceived task-difficulty across a learning session.](log-feature-combination-significant-accumulated-difficulty.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [The review reports that a log-file ensemble approach for perceived task-difficulty recognition outperforms classical ensemble methods](logfile-ensemble-outperforms-classical-ensembles.md) — related
