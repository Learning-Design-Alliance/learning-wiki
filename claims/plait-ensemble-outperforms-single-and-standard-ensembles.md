---
type: claim
title: Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking
description: Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking
id: plait-ensemble-outperforms-single-and-standard-ensembles
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2016
source_checked: 2026-10-28
recheck_by: 2019
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

# Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · checked against its sources 2026-10-28 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The best performing plait on average is the KNN plait, except for class hard where the SVM plait performed best; DCT plait showed weaker performance. [→ Ruth Janning 2016](#ruth-janning-2016)

## Evidence

### Ruth Janning 2016

Ruth Janning, Carlotta Schatten, Lars Schmidt-Thieme. (2016). Perceived Task-Difficulty Recognition from Log-file Information for the Use in Adaptive Intelligent Tutoring Systems. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-016-0097-9

`q2 · i?` · `design · r2`

Per-student and per-class analysis of the same plait experiments (Fig. 2 and Fig. 3 plus Table 9). In Table 9 each plait has a lower average test error than the single classifier, majority and stacking ensemble of the same type (SVM 14.54% vs stacking 20.41%; KNN 12.84% vs 22.67%; DCT 20.57% vs 28.93%), though the DCT plait (20.57%) is slightly worse than the SVM stacking ensemble (20.41%). Per student (Fig. 2), the authors report the plait "outperformed the other models, except for SVM and DCT applied to the data of student 7", and that the DCT plait "seems not always to work well".

> "The best performing plait on average is the KNN plait, except for class hard where the SVM plait performed best. Overall, both SVM and KNN plait performed similarly good whereas DCT plait showed a weaker performance."

## Discussion


## Related Claims
- [Log-file features are suitable for recognising perceived task-difficulty per task, with SVM the best single classifier (25.24% average test error).](svm-best-single-classifier-task-difficulty.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — a broader claim this one bears on
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
- [Single log-file features per task show very small p-values but weak fit, with number of hints seen the strongest single predictor of perceived task-difficulty.](single-per-task-features-weak-fit.md) — related
- [The review reports that a log-file ensemble approach for perceived task-difficulty recognition outperforms classical ensemble methods](logfile-ensemble-outperforms-classical-ensembles.md) — possibly the same claim (merge candidate)
