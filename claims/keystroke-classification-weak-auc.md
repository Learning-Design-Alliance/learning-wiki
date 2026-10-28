---
type: claim
title: Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)
description: Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)
id: keystroke-classification-weak-auc
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
    rigour: 1
  - id: rianne-conijn-2022-2
    resource: "https://doi.org/10.1007/s40593-021-00268-w"
    title: "Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes. (2022). Early prediction of writing quality using keystroke logging. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00268-w"
    author: Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Binary classification of students who might need support from keystroke data only slightly exceeds the majority-class baseline (highest AUC 0.57)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Classification models predicting who might need support (final grade < 5.5) only occasionally beat the majority-class baseline; the best (SVM on keystroke-based segments) reached AUC 0.57. [→ Rianne Conijn 2022](#rianne-conijn-2022)
`q2 i?` The support vector machine outperformed the baseline and all other models at every keystroke-based timepoint, but performance did not improve as more keystrokes became available. [→ Rianne Conijn 2022 (2)](#rianne-conijn-2022-2)

## Evidence

### Rianne Conijn 2022

Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes. (2022). Early prediction of writing quality using keystroke logging. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00268-w

`q2 · i?` · `associational · r1`

Classification results on keystroke-based segments (Fig. 2) for 126 students, 48% below the 5.5 pass threshold. The SVM beat other models yet "with an AUC of 0.57, these models still do not perform well"; AUC is not an effect size, so no impact value is assigned.

> "The support vector machine outperforms the baseline and all other models at every timepoint within the writing process. Hence, the support vector machine appears to be the best model tested. However, with an AUC of 0.57, these models still do not perform well."

### Rianne Conijn 2022 (2)

Rianne Conijn, Christine Cook, Menno van Zaanen, Luuk Van Waes. (2022). Early prediction of writing quality using keystroke logging. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00268-w

`q2 · i?` · `associational · r1`

Same keystroke-based classification experiment: contrary to the expectation that error would decrease with more data, AUC rose around 15/30 and 20/30 of keystrokes then declined; for SVM and naive Bayes AUC was highest at only 5/30 of keystrokes.

> "Interestingly, the models also do not seem to improve over time. For the naive Bayes and random forest, there seems to be an increase at 15/30 th and 20/30 th of the total amount of keystrokes, but when more keystrokes are added, the performance decreases again."

## Discussion


## Related Claims
- [The relationship between keystroke data and writing quality may be less clear than previously posited](keystroke-quality-relationship-limited.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [Keystroke-feature regression models fail to predict final writing grade at any point during the writing process](keystroke-regression-does-not-beat-grade-baseline.md) — related
- [Over the full writing process, only one of 54 keystroke features (percentage of long pauses between words) correlates significantly with final writing grade in ESL academic summaries](only-one-keystroke-feature-correlates-with-writing-grade.md) — related
- [On real tutor log data, the models beat mean-time prediction but most of the gain is captured by a simple baseline, and the learning extension slightly overfits](real-data-prediction-baseline-captures-most-gain.md) — related
- [The proposed model's effectiveness was demonstrated by applying it to actual keystroke log datasets](tdlhmm-effectiveness-demonstrated-keystroke-datasets.md) — related
