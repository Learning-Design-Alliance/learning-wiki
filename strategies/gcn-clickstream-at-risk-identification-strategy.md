---
type: strategy
id: gcn-clickstream-at-risk-identification-strategy
title: Use GCN on clickstream and assessment data for early identification of at-risk students in online courses
description: Apply a Graph Convolutional Network to a heterogeneous knowledge graph built from platform clickstream events (video interactions, assessment submissions) combined with assessment scores to predict whether individual...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: trask-2024
    resource: "https://arxiv.org/abs/2407.12153"
    title: "Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. https://arxiv.org/abs/2407.12153"
    author: "Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A"
---

# Use GCN on clickstream and assessment data for early identification of at-risk students in online courses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 against) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Apply a Graph Convolutional Network to a heterogeneous knowledge graph built from platform clickstream events (video interactions, assessment submissions) combined with assessment scores to predict whether individual students will pass upcoming problem sets. Students are labeled with interaction levels (high engagement, normal engagement, potential at-risk, at-risk) based on engagement calculations. This enables early intervention by identifying struggling learners before they fail graded assessments. The article demonstrates this approach achieves 70-90% prediction accuracy across course modalities.

## Design Implications

### Context
#### Requirements
- Access to platform clickstream data including video interactions and assessment submissions
- Assessment scores to serve as ground truth labels
- Sufficient user volume for reliable model training
#### Constraints
- Models are non-transferable between course instances without a translation layer
- Individual low-enrollment course instances show high per-run variance
- Only 30% of content could be linked via page properties

### Target Learners
- Online course learners
- At-risk students in self-paced or structured online courses

### Target Learning Goals
- Early identification of students likely to fail problem sets
- Enabling timely intervention

### Affordances
- [Hkg Gcn Student Performance Prediction Framework](../research-methods/heterogeneous-knowledge-graph-with-gcn-student-performance-prediction-method.md)

## Claims

- [A GCN trained on heterogeneous knowledge graph clickstream and assessment data predicts problem-set pass outcomes with 70-90% accuracy](../claims/gcn-hkg-predicts-problem-set-pass-70-90-accuracy.md) [+W]
- [GCN predictor performs better on aggregated yearly on-campus data than on individual course instances, with AUC rising to 90% for 2021 and 82% for 2022](../claims/gcn-aggregated-oncampus-data-higher-auc.md) [+W]
- [GCN models trained on one course instance are non-transferable to other course instances due to differences in data shape](../claims/gcn-models-non-transferable-across-instances.md) [-W]
- [Significant variance exists within and between GCN training runs for individual course instances, attributed to a floor effect from low user counts](../claims/gcn-variance-floor-effect-individual-instances.md) [-W]

## Related Strategies

- [Deploy ML-based early-warning prediction to shift retention support from reactive to proactive intervention](ml-early-warning-proactive-retention-support.md)

## Examples
-

## Key Sources
- Trask, T., Lytle, N., Boyle, M., Joyner, D., & Mubarak, A. (2024). A Comparative Analysis of Student Performance Predictions in Online Courses using Heterogeneous Knowledge Graphs. arXiv. https://arxiv.org/abs/2407.12153
