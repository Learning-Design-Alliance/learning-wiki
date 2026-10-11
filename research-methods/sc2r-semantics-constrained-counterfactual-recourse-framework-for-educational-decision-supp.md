---
type: research-method
id: sc2r-semantics-constrained-counterfactual-recourse-framework-for-educational-decision-supp
title: "SC2R: semantics-constrained counterfactual recourse framework for educational decision support"
description: "SC2R is a three-component pipeline for educational decision support: a predictive component estimating next-assessment success, an integer-programming recourse component generating candidate intervention plans over a discrete action space, and a semantic validation layer using SHACL."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SC2R: semantics-constrained counterfactual recourse framework for educational decision support

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
SC2R is a three-component pipeline for educational decision support: a predictive component estimating next-assessment success, an integer-programming recourse component generating candidate intervention plans over a discrete action space, and a semantic validation layer using SHACL. Plans are represented as RDF graphs and are "retained only if it satisfies the semantic feasibility condition" S(Gπ) = 1. The framework treats recourse as a constrained decision-support problem rather than geometric perturbation in feature space, turning counterfactual recourse into a machine-checkable process.

## Accounts
<!-- How each source describes or uses the method -->
- **SC2R: a semantics-constrained counterfactual recourse framework for educational decision support**: SC2R is a three-component pipeline for educational decision support: a predictive component estimating next-assessment success, an integer-programming recourse component generating candidate intervention plans over a discrete action space, and a semantic validation layer using SHACL. Plans are represented as RDF graphs and are "retained only if it satisfies the semantic feasibility condition" S(Gπ) = 1. The framework treats recourse as a constrained decision-support problem rather than geometric perturbation in feature space, turning counterfactual recourse into a machine-checkable process. (Ngoc Luyen Le et al. (2026))
- **Validate counterfactual recourse recommendations against explicit semantic feasibility constraints before use in educational decision support**: The article recommends that educational recourse outputs be treated as machine-checkable intervention plans subject to explicit semantic constraints rather than accepted on model validity alone. The semantic layer's contribution, as the authors put it, is "not to reduce optimization cost, but to distinguish between plans that are merely model-valid and plans that remain feasible" under explicit timing, budget, immutability, and availability constraints. This makes recommendations defensible and interpretable for instructors, advisors, and support services before any practical use. (Ngoc Luyen Le et al. (2026))

### Claims
- [A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons](../claims/oulad-calibrated-logistic-regression-strong-prediction.md) [+M]
- [Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD](../claims/ip-recourse-compact-plans-at-scale.md) [+M]
- [Activating availability constraints in the IP pipeline lowers SHACL conformance to 0.875 without reducing optimization cost, exposing infeasible plans](../claims/semantic-validation-exposes-infeasible-plans.md) [+M]

## Related Research Methods
-

## Key Sources
- Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618
