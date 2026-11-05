---
type: claim
title: "The XGBoost model's precision–recall curve yielded an area under the curve of 0.905 on the testing set"
description: "The XGBoost model's precision–recall curve yielded an area under the curve of 0.905 on the testing set"
id: xgboost-pr-curve-discriminative-ability
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
    rigour: 1
---

# The XGBoost model's precision–recall curve yielded an area under the curve of 0.905 on the testing set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` To account for class imbalance, precision–recall analysis produced an area under the curve of 0.905 on the testing set. [→ Lai Wenyi 2026](#lai-wenyi-2026)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r1`

Complementary validation on the testing dataset (Fig. 3c) of the same study; the article also reports decision curve analysis showing "a higher net benefit than the extreme strategies" across a range of threshold probabilities.

> "The precision–recall curve yielded an area under the curve of 0.905 on the testing set (Fig. 3c), indicating strong discriminative ability across varying recall levels."

## Discussion


## Related Claims
- [An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set](xgboost-gpa-classification.md) — related
- [A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set](lr-baseline-gpa-classification.md) — related
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
- [TRACE outperforms LSTM, GNN and XGBoost baselines on grade prediction](trace-outperforms-lstm-gnn-xgboost.md) — related
