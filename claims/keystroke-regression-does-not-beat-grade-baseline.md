---
type: claim
title: Keystroke-feature regression models fail to predict final writing grade at any point during the writing process
description: Keystroke-feature regression models fail to predict final writing grade at any point during the writing process
id: keystroke-regression-does-not-beat-grade-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: rianne-conijn-2022
    resource: "https://doi.org/10.1007/s40593-021-00268-w"
    title: "Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes. (2022). Early prediction of writing quality using keystroke logging. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00268-w"
    author: Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Keystroke-feature regression models fail to predict final writing grade at any point during the writing process

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` None of the regression models (random forest, SVM, naive Bayes) at any time- or keystroke-based timepoint outperformed the mean final grade baseline for predicting final grade. [→ Rianne Conijn 2022](#rianne-conijn-2022)

## Evidence

### Rianne Conijn 2022

Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes. (2022). Early prediction of writing quality using keystroke logging. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00268-w

`q2 · i?` · `associational · r2`

Regression results (RQ2): random forest, support vector machine, and naive Bayes models trained on windowed and cumulative keystroke feature sets at twelve timepoints, evaluated with RMSE against the mean-grade baseline. No effect size printed; the null indicates no detected predictive gain, not equivalence.

> "None of the models outperformed the baseline (mean final grade) at any timepoint in the writing process. Thus, the keystroke features cannot be used for the early prediction of final grade, nor for the prediction of final grade once the writing process is finished."

## Discussion


## Related Claims
- [Which keystroke features correlate with writing grade changes across stages of the writing process: pause-variance and focus-shift features matter early, sentence-transition and event features later](keystroke-grade-correlations-vary-over-writing-stages.md) — reports the opposite
- [Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)](keystroke-classification-weak-auc.md) — related
- [Over the full writing process, only one of 54 keystroke features (percentage of long pauses between words) correlates significantly with final writing grade in ESL academic summaries](only-one-keystroke-feature-correlates-with-writing-grade.md) — reports the opposite
- [On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits](real-data-prediction-baseline-captures-most-gain.md) — related
