---
type: claim
title: Machine-learning SHAP analysis identifies age and extraversion as the most important single predictors for students, and learning-based memory and motor response capabilities for physicians
description: Machine-learning SHAP analysis identifies age and extraversion as the most important single predictors for students, and learning-based memory and motor response capabilities for physicians
id: shap-single-variable-importance-students-physicians
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: ruchay-zino-2024
    resource: "https://doi.org/10.1097/JS9.0000000000001577"
    title: "Ruchay Zino, Julian Pape, Julia-Sophie Cordt, Carolina Kerres, Sebastian Siehl, Karina Jansone, Johannes Ackermann, Veronika Guenther, Liselotte Mettler, Leila Allahqoli, Nicolai Maass, Frauke Nees, Ibrahim Alkatout. (2024). Does an aptitude for surgery exist and can we predict it? An experimental study. International Journal of Surgery. https://doi.org/10.1097/JS9.0000000000001577"
    author: Ruchay Zino, Julian Pape, Julia-Sophie Cordt, Carolina Kerres, Sebastian Siehl, Karina Jansone, Johannes Ackermann, Veronika Guenther, Liselotte Mettler, Leila Allahqoli, Nicolai Maass, Frauke Nees, Ibrahim Alkatout
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Machine-learning SHAP analysis identifies age and extraversion as the most important single predictors for students, and learning-based memory and motor response capabilities for physicians

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the Random Forest Regressor with SHAP analysis, the most important features for students were age and extraversion, while the foremost features for physicians were learning-based memory and motor response capabilities. [→ Ruchay Zino 2024](#ruchay-zino-2024)

## Evidence

### Ruchay Zino 2024

Ruchay Zino, Julian Pape, Julia-Sophie Cordt, Carolina Kerres, Sebastian Siehl, Karina Jansone, Johannes Ackermann, Veronika Guenther, Liselotte Mettler, Leila Allahqoli, Nicolai Maass, Frauke Nees, Ibrahim Alkatout. (2024). Does an aptitude for surgery exist and can we predict it? An experimental study. International Journal of Surgery. https://doi.org/10.1097/JS9.0000000000001577

`q2 · i?` · `causal · r2`

Machine-learning importance analysis using a Random Forest Regressor (1000 decision trees, 70% training / 30% test split) with SHAP values; the model achieved an accuracy of 80.12% for students and 73.28% for physicians.

> "The most important features for students were age and the personality trait of extraversion (Fig. 6a), while the foremost features for physicians (Fig. 6b) were the psychomotor skills of learning-based memory and motor response capabilities."

## Discussion


## Learner Variables
- [Personality Traits](../learner-variables/personality-traits.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related
