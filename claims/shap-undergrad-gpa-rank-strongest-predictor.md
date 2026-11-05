---
type: claim
title: SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance
description: SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance
id: shap-undergrad-gpa-rank-strongest-predictor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: lai-wenyi-2026
    resource: "https://doi.org/10.1186/s12909-026-08741-7"
    title: "Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7"
    author: Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: lai-wenyi-2026-2
    resource: "https://doi.org/10.1186/s12909-026-08741-7"
    title: "Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7"
    author: Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the XGBoost model, undergraduate GPA rank exhibited the greatest influence on predictions, followed by gender, confidence, undergraduate score average, and CET-4 performance. [→ Lai Wenyi 2026](#lai-wenyi-2026)
`q2 i?` Self-reported confidence showed a positive association with higher predicted academic performance in the SHAP analysis. [→ Lai Wenyi 2026 (2)](#lai-wenyi-2026-2)

## Evidence

### Lai Wenyi 2026

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

SHAP interpretation of the XGBoost classifier on the testing dataset (Fig. 4); the article reports the importance ordering and that higher undergraduate GPA rank and score average were "generally associated with increased SHAP values".

> "Among these variables, undergraduate GPA rank exhibited the greatest influence on model predictions, followed by gender, confidence, undergraduate score average, and CET-4 performance."

### Lai Wenyi 2026 (2)

Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7

`q2 · i?` · `associational · r2`

SHAP summary-plot analysis of psychosocial predictors in the same model; the article reports confidence's positive association and that gender "exhibited a moderate but consistent effect on model output".

> "Confidence showed a positive association with higher predicted academic performance, suggesting that students reporting stronger self-confidence were more likely to be classified as high achievers."

## Discussion


## Learner Variables
- [Self-Efficacy](../learner-variables/self-efficacy.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Deletion tests show SHAP sentence rankings are more faithful than LLM-generated rationales for PLM scorers](shap-more-faithful-than-llm-rationales-deletion.md) — related
- [Feature importance analyses rank failed courses first for predicting academic performance, followed by institutional and academic background variables, with some regression-specific differences](feature-importance-failed-courses-institutional-background.md) — related
- [An XGBoost model predicted post-class test performance well, with knowledge mastery and learning interest the strongest SHAP contributors](xgboost-shap-knowledge-mastery-interest-predictors.md) — related
- [Biology and Introduction to Health Sciences midterm scores are the strongest predictors of at-risk classification, with SHAP analyses showing the largest case-level impact](biology-intro-midterms-strongest-predictors.md) — related
