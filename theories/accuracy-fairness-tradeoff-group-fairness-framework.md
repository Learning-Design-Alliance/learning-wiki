---
type: theory
title: Accuracy-fairness trade-off framework for educational predictive models using group fairness metrics
description: The article organizes the evaluation of student performance prediction around group fairness, operationalized through the Equal Opportunity Difference (EOD), which measures maximum disparity in true-positive rates acr...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: raymond-a-opoku-2025
    resource: "https://doi.org/10.18608/jla.2025.8543"
    title: "Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543"
    author: Raymond A. Opoku, Bo Pei and Wanli Xing
---

# Accuracy-fairness trade-off framework for educational predictive models using group fairness metrics

> **Theory** · [All theories](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 causal, 1 design), `q2` · 1 of 2 report an effect size · 5 claims rest on one study

## Description
The article organizes the evaluation of student performance prediction around group fairness, operationalized through the Equal Opportunity Difference (EOD), which measures maximum disparity in true-positive rates across subgroups, and the Average Odds Difference (AOD), which assesses the equalized odds criterion over both TPR and FPR. The authors prioritize the equal opportunity criterion because, in their words, "fairness should ensure that students at risk of failing are equally identified across groups so that they are fairly provided with the necessary support and accommodations." The framework frames model selection as navigating trade-offs between balanced accuracy and fairness disparities, with balanced accuracy prioritized at a fixed decision threshold for practical deployment.

## Design Implications

### Context
#### Requirements
- A defined key demographic attribute and subgroups for fairness evaluation
- Choice of a fairness criterion (equal opportunity or equalized odds) suited to the deployment context
- Balanced accuracy and AUC-ROC evaluation alongside fairness metrics
#### Constraints
- The article notes the accuracy-fairness trade-off is context-dependent and that perfect equality of rates across subgroups is challenging in real-world scenarios

### Target Learners
- adult learners in virtual learning environments
- students in online higher education courses

### Target Learning Objectives
- fair and accurate prediction of student pass/fail outcomes to target support

### Claims

- [Cpp Postprocessing Accuracy Fairness Tradeoff](../claims/cpp-postprocessing-accuracy-fairness-tradeoff.md) [+M]
- [Preprocessing Mitigation Reduces Disparities Oulad](../claims/preprocessing-mitigation-reduces-disparities-oulad.md) [+M]
- [Standard ML models predicting student pass/fail from VLE data exhibit biased true-positive rates across demographic subgroups](../claims/baseline-ml-models-biased-tpr-oulad.md) [+W]
- [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics while maintaining accuracy reasonably well, with a slight performance drop](../claims/thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) [+W]
- [Balancing the dataset significantly improved model predictive performance but increased bias under demographic parity](../claims/data-balancing-improves-accuracy-increases-bias.md) [+W]

## Related Theories

- [Three-stage fairness-aware analytical pipeline for early at-risk student identification](three-stage-fairness-aware-identification-pipeline.md)
- [FATE framework for MMLA: fairness, accountability, transparency, and ethics as student-centred evaluation dimensions](../research-methods/fate-framework.md)

## Examples

- [Regularly audit ML models for fairness and proactively apply bias mitigation during model training](../strategies/regular-fairness-audits-and-proactive-bias-mitigation.md)

## Key Sources
- Raymond A. Opoku, Bo Pei and Wanli Xing. (2025). Unveiling Accuracy-Fairness Trade-Offs: Investigating Machine Learning Models in Student Performance Prediction. Journal of Learning Analytics 12(2). https://doi.org/10.18608/jla.2025.8543
