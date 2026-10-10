---
type: product
id: open-university-learning-analytics-dataset-oulad
title: Open University Learning Analytics Dataset (OULAD)
description: OULAD is an open-source dataset maintained for learning-analytics research, containing demographic, virtual learning-environment activity, and performance data from adult learners at The Open University.
product_kind: dataset
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: raymond-a-opoku-2025
    resource: "https://doi.org/10.18608/jla.2025.8543"
    title: "Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543"
    author: Raymond A. Opoku, Bo Pei and Wanli Xing
---

# Open University Learning Analytics Dataset (OULAD)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 8 claims (8 for) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 8 claims rest on one study

## Description
OULAD is an open-source dataset maintained for learning-analytics research, containing demographic, virtual learning-environment activity, and performance data from adult learners at The Open University.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Open University Learning Analytics Dataset (OULAD) used for fairness-audited student performance prediction**: OULAD is an open-source benchmark dataset containing demographics, virtual learning activity, and performance outcomes for adult learners in online courses at The Open University. The article describes it as containing "demographics, virtual learning activity, and performance outcomes for over 35,000 adult learners," of which 25,690 students with nine features were used after aggregating Fail/Withdrawn into a Failed outcome and Distinction/Pass into a Passed outcome. The study used it to train and fairness-audit LR and XGBoost pass/fail predictors across gender, age band, disability, and IMD subgroups. (Raymond A. Opoku et al. (2025))

### Claims
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](../claims/baseline-ml-models-biased-tpr-oulad.md) [+W]
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](../claims/baseline-model-performance-oulad-lr-xgboost.md) [+W]
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](../claims/cpp-postprocessing-accuracy-fairness-tradeoff.md) [+W]
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](../claims/preprocessing-mitigation-reduces-disparities-oulad.md) [+W]
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](../claims/data-balancing-improves-accuracy-increases-bias.md) [+W]
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](../claims/stage1-optimal-early-at-risk-identification.md) [+W]
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](../claims/thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) [+W]
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](../claims/no-significant-performance-gain-later-stages.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543

<!-- merged 2026-10-10 from elements/oulad-dataset-fairness-audit-element ("Open University Learning Analytics Dataset (OULAD) used for fairness-audited student performance prediction"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Open University Learning Analytics Dataset (OULAD) used for fairness-audited student performance prediction

> **Element** · [All elements](index.md)
> **Evidence** · 8 claims (8 for) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 8 claims rest on one study

## Description
OULAD is an open-source benchmark dataset containing demographics, virtual learning activity, and performance outcomes for adult learners in online courses at The Open University. The article describes it as containing "demographics, virtual learning activity, and performance outcomes for over 35,000 adult learners," of which 25,690 students with nine features were used after aggregating Fail/Withdrawn into a Failed outcome and Distinction/Pass into a Passed outcome. The study used it to train and fairness-audit LR and XGBoost pass/fail predictors across gender, age band, disability, and IMD subgroups.

## Design Implications

### Context
#### Requirements
- Binary classification labels derived from final course grades
- Demographic attributes (gender, age band, disability, IMD) for subgroup fairness analysis
#### Constraints
- The authors state the aggregation of Fail and Withdrawn categories may obscure nuances and introduce or amplify biases, and that OULAD may not fully represent diverse VLEs or student populations

### Target Learners
- adult learners aged from their early 20s to over 60 in distance higher education

### Target Learning Goals
- predicting whether a student will successfully complete a course

## Claims

- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](../claims/baseline-ml-models-biased-tpr-oulad.md) [+W]
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](../claims/baseline-model-performance-oulad-lr-xgboost.md) [+W]
- [Calibrated Equalized Odds Post-processing shows significant accuracy drops and higher EOD compared to preprocessing techniques](../claims/cpp-postprocessing-accuracy-fairness-tradeoff.md) [+W]
- [Preprocessing bias mitigation (DIR, RW, SUP) reduces subgroup disparities in TPR while maintaining acceptable balanced accuracy](../claims/preprocessing-mitigation-reduces-disparities-oulad.md) [+W]
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](../claims/data-balancing-improves-accuracy-increases-bias.md) [+W]
- [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-risk students, balancing timeliness, accuracy, and fairness](../claims/stage1-optimal-early-at-risk-identification.md) [+W]
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](../claims/thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) [+W]
- [Adding more learning activity data beyond Stage 1 did not significantly improve predictive performance of at-risk identification models](../claims/no-significant-performance-gain-later-stages.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543
-->
