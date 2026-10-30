---
type: claim
title: "LIME and SHAP analyses identified question words such as \"Angular\", \"VS Code\", \"ASP .NET\", and \"Core\" as features supporting correct tag predictions"
description: "LIME and SHAP analyses identified question words such as \"Angular\", \"VS Code\", \"ASP .NET\", and \"Core\" as features supporting correct tag predictions"
id: lime-shap-support-tag-predictions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: olatinwo-2025
    resource: "https://doi.org/10.1007/s40593-024-00441-x"
    title: "Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x"
    author: "Olatinwo, S. O., & Demmans Epp, C."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# LIME and SHAP analyses identified question words such as "Angular", "VS Code", "ASP .NET", and "Core" as features supporting correct tag predictions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In randomly sampled test posts, LIME and SHAP explanations overlapped and correctly identified the words driving correct tag predictions. [→ Olatinwo 2025](#olatinwo-2025)

## Evidence

### Olatinwo 2025

Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x

`q1 · i?` · `design · r2`

Interpretability analysis of four randomly sampled test posts using LIME and SHAP force plots. The article reports that "LIME and SHAP correctly identified "Angular" and "VS Code"" as important features, with overlapping explanations across methods.

> "The explanations in Fig.8 (i.e., "Angular" and "VS Code") overlap with what was identified in Figs. 10 and 11 which shows "Angular" and "VS Code" as important features for sample 1. These analyses suggest that LIME and SHAP correctly identified "Angular" and "VS Code"."

## Discussion


## Related Claims
- [Error analysis showed the model failed to predict the \"Java\" tag when question wording emphasized \"Android\" and \"React Native\"](error-analysis-java-tag-miss.md) — related
- [SHAP and LIME agree on which factors are influential in individual predictions and on their direction of effect.](shap-lime-agree-on-local-explanations.md) — a broader claim this one bears on
