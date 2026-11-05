---
type: claim
title: A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set
description: A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set
id: lr-baseline-gpa-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: lai-wenyi-2026
    resource: "https://doi.org/10.1186/s12909-026-08741-7"
    title: "Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7"
    author: Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Logistic regression using five Boruta-confirmed features achieved AUC 0.659, accuracy 0.825, precision 0.835, recall 0.980, specificity 0.115, and F1-score 0.902 on the testing set. [→ Lai Wenyi 2026](#lai-wenyi-2026)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

Single-institution observational classification study of 1,091 medical postgraduate students, with a 60/40 train-test split; the held-out test set (n = 436) evaluation printed these metrics. The model used the five Boruta-confirmed features, with "a recall of 0.980" and "a specificity of 0.115".

> "On the testing set, the logistic regression model achieved an area under the receiver operating characteristic curve (AUC) of 0.659, an accuracy of 0.825, a precision of 0.835, a recall of 0.980, a specificity of 0.115, and an F1-score of 0.902 (Table 3)."

## Discussion


## Related Claims
- [Boruta feature selection confirmed five variables as robust predictors of GPA classification](boruta-five-confirmed-features.md) — related
- [An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set](xgboost-gpa-classification.md) — related
- [XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set](xgboost-comparable-to-logistic-regression.md) — a broader claim this one bears on
- [The XGBoost model's precision–recall curve yielded an area under the curve of 0.905 on the testing set](xgboost-pr-curve-discriminative-ability.md) — related
