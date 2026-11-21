---
type: strategy
id: use-predictions-for-risk-factors-not-individual-ranking
title: Use ML-derived achievement predictions to identify general risk factors and support policy, not to rank individual students for high-stakes decisions
description: "The article recommends a bounded use of predictive models in education: because the models' R² ceilings leave most variance unexplained, \"they are best used to identify general risk factors or support policies, rather..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: liu-liu-2025
    resource: "https://www.google.com/search?q=%22Explainable+AI+for+Predicting+and+Understanding+Mathematics+Achievement%22+PISA+2018"
    title: "Liu Liu, Rui Dai. (2025). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. https://www.google.com/search?q=%22Explainable+AI+for+Predicting+and+Understanding+Mathematics+Achievement%22+PISA+2018"
    author: Liu Liu, Rui Dai
---

# Use ML-derived achievement predictions to identify general risk factors and support policy, not to rank individual students for high-stakes decisions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends a bounded use of predictive models in education: because the models' R² ceilings leave most variance unexplained, "they are best used to identify general risk factors or support policies, rather than precisely ranking individual students." The strategy directs practitioners and policymakers toward aggregate, equity-oriented uses — spotting risk scenarios such as low-SES, low-effort students and targeting interventions — rather than deterministic individual placement decisions.

## Design Implications

### Context
#### Requirements
- Predictive models with reported performance ceilings and explanation outputs (feature importance, SHAP) so users can see which factors drive predictions
#### Constraints
- Moderate R² ceilings (highest test R² = 0.38) mean predictions are far from deterministic for each student; the article warns against high-stakes individual use

### Target Learners
- 15-year-old students in large-scale assessment systems

### Target Learning Goals
- Equity-oriented educational policy and targeted intervention planning for mathematics achievement

## Claims

- [Non-linear ML models (RF, CatBoost, ANN) consistently outperform multiple linear regression in predicting PISA 2018 math scores across ten countries](../claims/nonlinear-ml-outperforms-mlr-pisa-math.md) [+W]
- [Socio-economic status (ESCS) is the most influential predictor of math performance in virtually all countries studied](../claims/escs-top-predictor-pisa-math-xai.md) [+W]
- [Surrogate decision-tree analysis of the Random Forest reveals conditional interactions, such as compounding negative effects of low SES combined with low study time](../claims/surrogate-tree-reveals-ses-effort-interaction.md) [+W]

## Related Strategies

- [Use early cheating-risk predictions only for low-stakes support with human review, never for disciplinary decisions](support-oriented-use-of-cheating-risk-predictions.md)
- [Decide whether to use demographic predictors case-by-case based on context: risk of discriminatory decision-making, who holds final choice, and stakes](contextual-decision-demographic-predictor-use.md)
- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)

## Examples
-

## Key Sources
- Liu Liu, Rui Dai. (2025). Explainable AI for Predicting and Understanding Mathematics Achievement: A Cross-National Analysis of PISA 2018. https://www.google.com/search?q=%22Explainable+AI+for+Predicting+and+Understanding+Mathematics+Achievement%22+PISA+2018
