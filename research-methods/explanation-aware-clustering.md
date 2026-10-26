---
type: research-method
id: explanation-aware-clustering
title: Explanation-aware clustering
description: This framework pairs a model explainer with unsupervised learning to reveal heterogeneity hidden by binary classification.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
---

# Explanation-aware clustering

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This framework pairs a model explainer with unsupervised learning to reveal heterogeneity hidden by binary classification. LIME "perturbs the input data locally around a single instance and fits a simple interpretable model" to identify predictors contributing to class membership; clustering of these LIME profiles (via K-Means, cluster number selected by lowest Davies-Bouldin Index) then identifies subgroups within each class, addressing explainer models' "tendency to overstate class homogeneity due to such local approximations". The article uses it to uncover 2 responder and 4 non-responder subgroups with distinct longitudinal outcomes.

## Accounts
<!-- How each source describes or uses the method -->
- **Explanation-aware clustering: combining model explainers with unsupervised clustering to uncover heterogeneous subgroups within predicted classes**: This framework pairs a model explainer with unsupervised learning to reveal heterogeneity hidden by binary classification. LIME "perturbs the input data locally around a single instance and fits a simple interpretable model" to identify predictors contributing to class membership; clustering of these LIME profiles (via K-Means, cluster number selected by lowest Davies-Bouldin Index) then identifies subgroups within each class, addressing explainer models' "tendency to overstate class homogeneity due to such local approximations". The article uses it to uncover 2 responder and 4 non-responder subgroups with distinct longitudinal outcomes. (Tan et al. (2026))

### Claims
- [K-Means clustering of LIME feature-importance profiles identifies 2 responder and 4 non-responder subgroups within binary intervention-response classes](../claims/lime-clustering-dyslexia-subgroups.md) [+M]
- [Subgroup membership predicted distinct long-term literacy trajectories 68.2 months after intervention ended](../claims/subgroup-membership-predicts-long-term-literacy.md) [+M]

## Related Research Methods
-

## Key Sources
- Tan, A.S.-C., & Ali, F. (2026). Uncovering subgroup heterogeneity in dyslexia intervention outcomes using explainable machine learning. npj Science of Learning. https://doi.org/10.1038/s41539-026-00429-3
