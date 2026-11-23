---
type: research-method
id: k-means-partitioned-transfer-learning-pipeline-for-student-performance-prediction
title: K-means-partitioned transfer learning pipeline for student performance prediction
description: "The article proposes a prediction method that first partitions a dataset with K-means clustering into subsets with distinct distribution patterns, trains an initial ANN on the subset with the largest data volume, then applies parameter-based fine-tuning: \"the weights of the several layers of the mod"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# K-means-partitioned transfer learning pipeline for student performance prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a prediction method that first partitions a dataset with K-means clustering into subsets with distinct distribution patterns, trains an initial ANN on the subset with the largest data volume, then applies parameter-based fine-tuning: "the weights of the several layers of the model were frozen, and only the remaining layers' weights were fine-tuned on another subset." The ANN has six layers (32, 16, 8, 4, 2, 1 neurons) with ReLU activations except the final layer, trained with MAE loss and the Adam optimizer. The method aims to improve applicability and accuracy across different data distributions.

## Accounts
<!-- How each source describes or uses the method -->
- **K-means-partitioned transfer learning pipeline for student performance prediction**: The article proposes a prediction method that first partitions a dataset with K-means clustering into subsets with distinct distribution patterns, trains an initial ANN on the subset with the largest data volume, then applies parameter-based fine-tuning: "the weights of the several layers of the model were frozen, and only the remaining layers' weights were fine-tuned on another subset." The ANN has six layers (32, 16, 8, 4, 2, 1 neurons) with ReLU activations except the final layer, trained with MAE loss and the Adam optimizer. The method aims to improve applicability and accuracy across different data distributions. (Yan Zhao et al. (2024))

### Claims
- [Transfer learning with progressive layer freezing reduces RMSE and MAE and increases R² in student performance prediction across both datasets](../claims/transfer-learning-freezing-improves-student-prediction.md) [+M]
- [The optimal number of frozen layers depends on data complexity and target-domain data volume: more frozen layers suit complex, small datasets; fewer suit simpler, larger ones](../claims/frozen-layer-count-depends-on-data-complexity-and-volume.md) [+M]

## Related Research Methods
-

## Key Sources
- Yan Zhao, Pengbo Wang, Hao Wang. (2024). Improvement of Applicability in Student Performance Prediction Based on Transfer Learning. https://www.kaggle.com/datasets/henryshan/student-performance-prediction
