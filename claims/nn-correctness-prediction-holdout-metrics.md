---
type: claim
title: The neural network predicts student correctness on unseen questions with F1 of 0.8350 and AUC-ROC of 0.7789
description: The neural network predicts student correctness on unseen questions with F1 of 0.8350 and AUC-ROC of 0.7789
id: nn-correctness-prediction-holdout-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: matías-hoyl-2026
    resource: "https://doi.org/10.48550/arXiv.2602.00034"
    title: "Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)"
    author: Matías Hoyl
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The neural network predicts student correctness on unseen questions with F1 of 0.8350 and AUC-ROC of 0.7789

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Stage 1 network achieves holdout accuracy of 0.7529, AUC-ROC 0.7789, precision 0.8010, recall 0.8719, and F1 0.8350 when predicting correctness for unseen questions. [→ Matías Hoyl 2026](#matias-hoyl-2026)

## Evidence

### Matías Hoyl 2026

Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)

`q2 · i?` · `design · r2`

Classification performance of the Stage 1 neural network on the 470-question holdout test set, as printed in the results table: accuracy 0.7529, AUC-ROC 0.7789, precision 0.8010, recall 0.8719, F1 0.8350. No effect size is printed for this finding, so impact is coded i? (no magnitude reported; not a null effect).

> "The strong performance of our neural network model in predicting student correctness (test set F1 score of 0.8350, AUC of 0.7789) confirms that our feature engineering approach effectively captures many factors influencing student performance."

## Discussion


## Related Claims
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [XGBoost and Logistic Regression achieve the highest F1-scores (0.84) among five ML models predicting at-risk status from first-term midterm grades, with all models exceeding AUC 0.91](xgboost-logreg-highest-f1-midterm-risk-prediction.md) — related
