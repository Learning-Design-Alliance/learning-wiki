---
type: claim
title: "Machine learning on discussion-dialog indicators predicts group learning outcome as High, Mid, or Low with best accuracy of 78.9%"
description: "Machine learning on discussion-dialog indicators predicts group learning outcome as High, Mid, or Low with best accuracy of 78.9%"
id: ml-prediction-group-outcome-78-9-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: hang-su-2023
    resource: "https://doi.org/10.48550/arXiv.2301.12399"
    title: "Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng. (2023). Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom. [doi:10.48550/arXiv.2301.12399](https://doi.org/10.48550/arXiv.2301.12399)"
    author: Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Machine learning on discussion-dialog indicators predicts group learning outcome as High, Mid, or Low with best accuracy of 78.9%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The SVM model reaches the best prediction accuracy of 78.9% under five-fold cross-validation, vastly outperforming the random guess of 33.3%. [→ Hang Su 2023](#hang-su-2023)

## Evidence

### Hang Su 2023

Hang Su, Borislav Dzodzo, Changlun Li, Danyang Zhao, Hao Geng, Yunxiang Li, Sidharth Jaggi, and Helen Meng. (2023). Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom. [doi:10.48550/arXiv.2301.12399](https://doi.org/10.48550/arXiv.2301.12399)

`q2 · i?` · `associational · r1`

Prediction experiment on 90 labeled discussions (27 High, 36 Mid, 27 Low) using 62 statistically significant features reduced to 45 by random projection. Naive Bayes, Neural Network, KNN, Random Forest, LightGBM, XGBoost, and SVM were compared with five-fold cross-validation and Bayes-optimized hyperparameters; the confusion matrix shows only Low learning outcome reached marginally higher recall.

> "SVM model reaches the best prediction accuracy of 78.9%, which demonstrates the feasibility of achieving automatic group learning outcome prediction based on group discussion dialog in flipped classroom"

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Ensemble learning models (XGB, RF, Stacking) achieve higher cross-validated accuracy than individual learners (SVM, DT, LR, LDA) in predicting primary school students' academic achievement](ensemble-outperforms-individual-learners-training-accuracy.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — related
