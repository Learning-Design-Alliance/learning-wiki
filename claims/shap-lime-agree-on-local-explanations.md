---
type: claim
title: SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.
description: SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.
id: shap-lime-agree-on-local-explanations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: nagy-2024
    resource: "https://doi.org/10.1007/s40593-023-00331-8"
    title: "Nagy, M., & Molontay, R. (2024). Interpretable Dropout Prediction: Towards XAI-Based Personalized Intervention. International Journal of Artificial Intelligence in Education, 34, 274–300. https://doi.org/10.1007/s40593-023-00331-8"
    author: "Nagy, M., & Molontay, R."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHAP and LIME produce consistent local explanations, identifying the same influential factors and agreeing on the direction of their effects. [→ Nagy 2024](#nagy-2024)

## Evidence

### Nagy 2024

Nagy, M., & Molontay, R. (2024). Interpretable Dropout Prediction: Towards XAI-Based Personalized Intervention. International Journal of Artificial Intelligence in Education, 34, 274–300. https://doi.org/10.1007/s40593-023-00331-8

`q2 · i?` · `associational · r2`

Comparison of SHAP force plots (Fig. 6) and LIME explanations (Fig. 7) for the same four students. The authors state that "both SHAP and LIME find the same factors influential and more importantly, they also agree on how these features affect the probability of graduation."

> "The two methods agree, i.e., both SHAP and LIME find the same factors influential and more importantly, they also agree on how these features affect the probability of graduation."

## Discussion


## Related Claims
- [LIME and SHAP analyses identified question words such as \"Angular\", \"VS Code\", \"ASP .NET\", and \"Core\" as features supporting correct tag predictions](lime-shap-support-tag-predictions.md) — a narrower finding that bears on this claim
- [Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.](local-explanations-lack-directional-guidance.md) — reports the opposite
