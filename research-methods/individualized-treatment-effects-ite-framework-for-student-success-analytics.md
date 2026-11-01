---
type: research-method
id: individualized-treatment-effects-ite-framework-for-student-success-analytics
title: Individualized treatment effects (ITE) framework for student success analytics
description: Individualized treatment effects, borrowed from the personalized medicine literature, quantify for each student the predicted difference in an outcome between experiencing an intervention and not, even though each student experiences only one modality.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Individualized treatment effects (ITE) framework for student success analytics

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
Individualized treatment effects, borrowed from the personalized medicine literature, quantify for each student the predicted difference in an outcome between experiencing an intervention and not, even though each student experiences only one modality. The article computes ITE by training separate ensemble learners on treatment and control groups and using each to predict the counterfactual outcome for the other group. It states the ensemble learner serves "as a best guess of the outcome for the treatment (control) group students if they had experienced the control (treatment)". ITE then support evaluating interventions, characterizing benefiting subgroups, and advising individual students.

## Accounts
<!-- How each source describes or uses the method -->
- **Individualized treatment effects (ITE) as a framework for student success analytics**: Individualized treatment effects, borrowed from the personalized medicine literature, quantify for each student the predicted difference in an outcome between experiencing an intervention and not, even though each student experiences only one modality. The article computes ITE by training separate ensemble learners on treatment and control groups and using each to predict the counterfactual outcome for the other group. It states the ensemble learner serves "as a best guess of the outcome for the treatment (control) group students if they had experienced the control (treatment)". ITE then support evaluating interventions, characterizing benefiting subgroups, and advising individual students. (Beemer et al. (2018))
- **Residual Counterfactual Networks (RCN)**: RCN is an end-to-end neural model for estimating individual treatment effects under the Rubin-Neyman causal model. It "first learns a balancing representation of deep features" by minimizing an Integral Probability Metric (MMD or Wasserstein distance) between control and treated distributions, then "learns a residual mapping" on that representation so the estimated treatment effect depends on the balanced features. It extends Balancing Neural Networks and Counterfactual Regression by adding a residual block for the treated population only. (Siyuan Zhao et al. (2016))

### Claims
- [Enrollment in the supplemental instruction section is associated with significantly positive average individualized treatment effects on final exam score and course grade](../claims/si-positive-average-ite-exam-grade.md) [+M]
- [Underrepresented minority students in the course showed significantly positive individualized treatment effects from supplemental instruction](../claims/si-urm-subgroup-positive-ite.md) [+M]
- [RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE](../claims/rcn-best-ihdp-ite-ate-pehe.md) [+M]
- [On the ASSISTments experiment, RCN outperforms the Treated-All and Not-Treated policies and CFR on policy risk and ATT error](../claims/rcn-outperforms-ta-nt-cfr-assistments.md) [+M]

## Related Research Methods
-

## Key Sources
- Beemer, J., Spoon, K., He, L., Fan, J., & Levine, R.A. (2018). Ensemble Learning for Estimating Individualized Treatment Effects in Student Success Studies. International Journal of Artificial Intelligence in Education, 28, 315–335. https://doi.org/10.1007/s40593-017-0148-x
- Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/
