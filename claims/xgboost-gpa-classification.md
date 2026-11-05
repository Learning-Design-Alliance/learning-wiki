---
type: claim
title: An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set
description: An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set
id: xgboost-gpa-classification
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

# An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` XGBoost using the same five Boruta-confirmed features achieved AUC 0.617, accuracy 0.786, precision 0.835, recall 0.922, specificity 0.167, and F1-score 0.876 on the testing set. [→ Lai Wenyi 2026](#lai-wenyi-2026)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

Held-out test-set evaluation (n = 436) of the XGBoost classifier in the same 60/40 split study; the article reports these six printed metrics, including "an AUC of 0.617" and "an accuracy of 0.786".

> "The XGBoost model achieved an AUC of 0.617, an accuracy of 0.786, a precision of 0.835, a recall of 0.922, a specificity of 0.167, and an F1-score of 0.876 on the testing set (Table 3)."

## Discussion


## Related Claims
- [Boruta feature selection confirmed five variables as robust predictors of GPA classification](boruta-five-confirmed-features.md) — related
- [A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set](lr-baseline-gpa-classification.md) — related
- [XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set](xgboost-comparable-to-logistic-regression.md) — a broader claim this one bears on
- [The XGBoost model's precision–recall curve yielded an area under the curve of 0.905 on the testing set](xgboost-pr-curve-discriminative-ability.md) — related
