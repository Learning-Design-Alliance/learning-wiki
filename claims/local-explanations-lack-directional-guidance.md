---
type: claim
title: Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.
description: Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.
id: local-explanations-lack-directional-guidance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Local explanations from SHAP and LIME communicate the contribution of each feature but do not reveal whether the value of a feature should be increased or decreased to push the prediction higher. [→ Nagy 2024](#nagy-2024)

## Evidence

### Nagy 2024

Nagy, M., & Molontay, R. (2024). Interpretable Dropout Prediction: Towards XAI-Based Personalized Intervention. International Journal of Artificial Intelligence in Education, 34, 274–300. https://doi.org/10.1007/s40593-023-00331-8

`q2 · i?` · `associational · r2`

The authors analyze the limitation of SHAP and LIME local explanations using the example of a student with 87 points in mathematics. They state that "these explanations only tell the contribution of a factor but do not reveal whether the value of a feature should be increased or decreased."

> "In general, these explanations only tell the contribution of a factor but do not reveal whether the value of a feature should be increased or decreased to push the model prediction higher."

## Discussion


## Related Claims
- [SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.](shap-lime-agree-on-local-explanations.md) — reports the opposite
