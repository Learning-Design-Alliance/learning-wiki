---
type: strategy
id: predictive-model-as-screening-aid-not-deterministic-tool
title: Use the predictive model as a screening aid complementing existing academic monitoring, not as a deterministic evaluation tool
description: The article recommends deploying the GPA-classification model as a screening aid within existing academic monitoring systems so educators can allocate supportive resources more efficiently while maintaining transparen...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: lai-wenyi-2026
    resource: "https://doi.org/10.1186/s12909-026-08741-7"
    title: "Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7"
    author: Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying
---

# Use the predictive model as a screening aid complementing existing academic monitoring, not as a deterministic evaluation tool

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends deploying the GPA-classification model as a screening aid within existing academic monitoring systems so educators can allocate supportive resources more efficiently while maintaining transparency and fairness. It explicitly states the model should not serve as a deterministic evaluation tool, and that interpretability via SHAP may facilitate early identification of students who could benefit from targeted academic guidance or support.

## Design Implications

### Context
#### Requirements
- SHAP-based transparency; careful monitoring, periodic model updating, and fairness assessments across student subgroups before broader implementation
#### Constraints
- The article states deployment risk that the model could reflect or reinforce existing biases in training data; external validation across institutions is necessary first

### Target Learners
- medical postgraduate students

### Target Learning Goals
- early identification of students who could benefit from targeted academic guidance or support

## Claims

- [A baseline logistic regression model classifies outstanding postgraduate GPA with AUC 0.659 and accuracy 0.825 on a held-out test set](../claims/lr-baseline-gpa-classification.md) [+W]
- [An XGBoost classification model classifies outstanding postgraduate GPA with AUC 0.617 and accuracy 0.786 on the held-out test set](../claims/xgboost-gpa-classification.md) [+W]
- [Boruta feature selection confirmed five variables as robust predictors of GPA classification](../claims/boruta-five-confirmed-features.md) [+W]
- [SHAP analysis identifies undergraduate GPA rank as the most influential predictor, followed by gender, confidence, undergraduate score average, and CET-4 performance](../claims/shap-undergrad-gpa-rank-strongest-predictor.md) [+W]
- [XGBoost demonstrated comparable overall performance to the baseline logistic regression model on the testing set](../claims/xgboost-comparable-to-logistic-regression.md) [+W]

## Related Strategies

- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Use automatic reflection classification for preliminary feedback and workload support, with final assessment retained by educators](automated-reflection-preliminary-feedback-educator-final.md)
- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)

## Examples
-

## Key Sources
- Lai Wenyi, Lin Jinna, Shen Kailiang, Ling Zhihai, Guan Ying. (2026). Enhancing graduate education assessment: a machine learning-based classification of academic performance in medical students. BMC Medical Education. https://doi.org/10.1186/s12909-026-08741-7
