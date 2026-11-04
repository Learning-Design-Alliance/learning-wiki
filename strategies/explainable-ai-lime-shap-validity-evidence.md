---
type: strategy
id: explainable-ai-lime-shap-validity-evidence
title: Use explainable AI methods (LIME, SHAP) to investigate the relation between individual features and model predictions
description: This strategy recommends using methods of interpretable machine learning and explainable AI, such as LIME and SHAP values, to investigate how changing individual features (e.g., tokens in NLP models) affects the model...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: debelak-rudolf-2026
    resource: "https://doi.org/10.1371/journal.pone.0354680"
    title: "Debelak Rudolf, Ziegler Matthias. (2026). Testing standards for AI-based scores in automated essay scoring. PLOS One. https://doi.org/10.1371/journal.pone.0354680"
    author: Debelak Rudolf, Ziegler Matthias
---

# Use explainable AI methods (LIME, SHAP) to investigate the relation between individual features and model predictions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (1 associational, 1 design), `q1`–`q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
This strategy recommends using methods of interpretable machine learning and explainable AI, such as LIME and SHAP values, to investigate how changing individual features (e.g., tokens in NLP models) affects the model's prediction. The article states these methods 'help to explain how changing individual features, such as tokens in the context of NLP models, affect the prediction of the model.'

## Design Implications

### Context
#### Requirements
- The relation between specific tokens and the overall rating must be interpretable for the scoring task at hand
#### Constraints
- The article does not illustrate this method in its empirical example because it is not clear how specific tokens relate to the overall rating of the text; content validity could be limited in some use cases

### Target Learners
- students whose essays are scored by AI systems

### Target Learning Goals
- valid automated scoring driven by construct-relevant features

## Claims

- [SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.](../claims/shap-lime-agree-on-local-explanations.md) [+W]
- [LIME and SHAP analyses identified question words such as \"Angular\", \"VS Code\", \"ASP .NET\", and \"Core\" as features supporting correct tag predictions](../claims/lime-shap-support-tag-predictions.md) [+W]
- [Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.](../claims/local-explanations-lack-directional-guidance.md) [~W]
- [Error analysis showed the model failed to predict the \"Java\" tag when question wording emphasized \"Android\" and \"React Native\"](../claims/error-analysis-java-tag-miss.md) [+W]

## Related Strategies

- [Use explainability tools (SHAP/LIME) and human monitoring for fair, transparent AI-driven personalized learning](explainability-tools-human-monitoring-personalized-learning.md)

## Examples
-

## Key Sources
- Debelak Rudolf, Ziegler Matthias. (2026). Testing standards for AI-based scores in automated essay scoring. PLOS One. https://doi.org/10.1371/journal.pone.0354680
