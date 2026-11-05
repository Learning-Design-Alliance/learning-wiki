---
type: claim
title: Boruta feature selection confirmed five variables as robust predictors of GPA classification
description: Boruta feature selection confirmed five variables as robust predictors of GPA classification
id: boruta-five-confirmed-features
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

# Boruta feature selection confirmed five variables as robust predictors of GPA classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Boruta algorithm, run on the training set, identified five confirmed important features with stable associations with GPA classification. [→ Lai Wenyi 2026](#lai-wenyi-2026)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

Feature-selection step on the training set (n = 655) of the same study; Boruta compares original variables with permuted shadow features, and "five variables were identified as confirmed important features" (Fig. 2).

> "In the final Boruta output, five variables were identified as confirmed important features (Fig. 2), indicating stable and robust associations with GPA classification."

## Discussion


## Related Claims
- [A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set](lr-baseline-gpa-classification.md) — related
- [An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set](xgboost-gpa-classification.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — reports the opposite
