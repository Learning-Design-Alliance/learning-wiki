---
type: research-method
id: post-hoc-fairness-evaluation-testbed-for-vendor-controlled-early-warning-systems
title: Post-hoc fairness evaluation testbed for vendor-controlled early-warning systems
description: "The article built a comparative evaluation testbed simulating an institution's position under vendor procurement: a research replica EWS and six post-hoc fairness methods applied without accessing, modifying, or retraining the underlying model."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Post-hoc fairness evaluation testbed for vendor-controlled early-warning systems

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article built a comparative evaluation testbed simulating an institution's position under vendor procurement: a research replica EWS and six post-hoc fairness methods applied without accessing, modifying, or retraining the underlying model. The replica is "an XGBoost classifier of the same model class the AutoML platform had selected, trained on the same data with SMOTE-NC class balancing and post-hoc calibration." The modeling cohort contained 168,550 student records (97,599 Domestic, 70,951 International) drawn from 15 years of institutional data, with 46 predictive features and age, gender, and residency as fairness axes.

## Accounts
<!-- How each source describes or uses the method -->
- **Research EWS replica and six-method post-hoc fairness evaluation testbed**: The article built a comparative evaluation testbed simulating an institution's position under vendor procurement: a research replica EWS and six post-hoc fairness methods applied without accessing, modifying, or retraining the underlying model. The replica is "an XGBoost classifier of the same model class the AutoML platform had selected, trained on the same data with SMOTE-NC class balancing and post-hoc calibration." The modeling cohort contained 168,550 student records (97,599 Domestic, 70,951 International) drawn from 15 years of institutional data, with 46 predictive features and age, gender, and residency as fairness axes. (McConvey et al. (2026))

### Claims
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](../claims/six-posthoc-interventions-redistribute-disparities.md) [+M]

## Related Research Methods
-

## Key Sources
- McConvey, K., Zhai, A., Li, R., & Guha, S. (2026). Fairness Theatre: Evaluating Post-Hoc Fairness Interventions in Vendor-Controlled Early Warning Systems. arXiv. https://arxiv.org/abs/2609.38552
