---
type: claim
title: Random forest and support vector machine models also failed to beat chance when predicting laboratory performance, supporting the null result
description: Random forest and support vector machine models also failed to beat chance when predicting laboratory performance, supporting the null result
id: rf-svm-also-fail-beat-chance-lab-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: robert-solli-2019
    resource: "https://doi.org/10.1119/perc.2018.pr.solli"
    title: "Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)"
    author: Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: robert-solli-2019-2
    resource: "https://doi.org/10.1119/perc.2018.pr.solli"
    title: "Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)"
    author: Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Random forest and support vector machine models also failed to beat chance when predicting laboratory performance, supporting the null result

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Neither the Random Forest nor the Support Vector Machine model produced a classifier with a significant KS statistic versus the random guess classifier (Dn < 0.125, p > 0.28). [→ Robert Solli 2019](#robert-solli-2019)
`q2 i?` The Random Forest built on unscaled features indicates that breaking the normality assumption when z-scaling features had a negligible effect. [→ Robert Solli 2019 (2)](#robert-solli-2019-2)

## Evidence

### Robert Solli 2019

Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)

`q2 · i?` · `associational · r2`

Robustness check in the same study: Random Forest and Support Vector Machine models were trained on the same data and subjected to the same metrics; 'Neither model was able to produce a classiﬁer with a signiﬁcant KS statistic when compared to the random guess classiﬁer (Dn < 0.125 p > 0.28).'

> "Neither model was able to produce a classiﬁer with a signiﬁcant KS statistic when compared to the random guess classiﬁer (Dn < 0.125 p > 0.28)."

### Robert Solli 2019 (2)

Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)

`q2 · i?` · `associational · r2`

Same robustness check: the Random Forest 'was constructed using unscaled features', which the authors take as evidence that breaking the normality assumption when z-scaling features had a negligible effect on the null result.

> "The RF model was constructed using unscaled features and as such provides evidence that the eﬀect of breaking the assumption of normality when z scaling the features was negligible."

## Discussion


## Related Claims
- [Lr Clickstream Features Fail Predict Lab Performance](lr-clickstream-features-fail-predict-lab-performance.md)
- [The authors attribute their null result to the complexity of laboratory assessments and their distance in time from the videos, contrasting prior predictive results for end-of-video quizzes](assessment-complexity-explains-null-vs-quiz-prediction.md) — related
- [Keystroke-feature regression models fail to predict final writing grade at any point during the writing process](keystroke-regression-does-not-beat-grade-baseline.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [All three trained classifiers outperformed the zero-rule baseline (28.4% accuracy) for classifying cognitive engagement in discussion posts](classifiers-beat-zero-rule-baseline-engagement.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
- [Victory conditions compare AI and human prediction quality against each other and against random guessing, requiring both to significantly beat chance](victory-conditions-beat-random-guessing.md) — related
- [Student-built decision-tree classifiers typically do not significantly improve event classification over the sequential selection in this laboratory](student-ml-no-significant-improvement-over-sequential-selection.md) — related
