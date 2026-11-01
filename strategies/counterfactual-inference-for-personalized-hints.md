---
type: strategy
id: counterfactual-inference-for-personalized-hints
title: Use counterfactual inference models on online educational experiments to support personalized hint selection
description: The article recommends applying ITE estimation models to online educational experiments so that an intelligent tutoring system can choose the intervention leading to the best outcome for a specific student, such as de...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
sources:
  - id: siyuan-zhao-and-neil-heffernan-2016
    resource: "https://eric.ed.gov/?id=ED596589"
    title: "Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589"
    author: Siyuan Zhao and Neil Heffernan
---

# Use counterfactual inference models on online educational experiments to support personalized hint selection

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article recommends applying ITE estimation models to online educational experiments so that an intelligent tutoring system can choose the intervention leading to the best outcome for a specific student, such as deciding between a video hint and a text hint. Randomized assignment within the platform supplies the training data, and models like RCN estimate what each student's outcome would be under each intervention.

## Design Implications

### Context
#### Requirements
- Randomized (or otherwise analyzed) assignment data from online experiments, with covariates describing students before condition assignment
#### Constraints
- Running experiments is expensive and collecting enough data for reliable prediction is difficult, per the article's conclusion

### Target Learners
- individual students in intelligent tutoring systems

### Target Learning Goals
- selecting the most beneficial intervention (hint type) per student

### Affordances
- [Residual Counterfactual Networks](../research-methods/individualized-treatment-effects-ite-framework-for-student-success-analytics.md)

## Claims

- [Taking individual treatment effects into account yields better intervention choices than a single uniform assignment](../claims/individual-effect-better-intervention-choice.md) [+W]
- [Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable](../claims/policy-risk-evaluation-without-ground-truth-ite.md) [+W]
- [RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE](../claims/rcn-best-ihdp-ite-ate-pehe.md) [+W]
- [On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR](../claims/rcn-outperforms-ta-nt-cfr-assistments.md) [+W]
- [Individualised counterfactual inferences estimate whether a specific student would have performed differently under different help conditions](../claims/individual-counterfactuals-student-help-conditions.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589
