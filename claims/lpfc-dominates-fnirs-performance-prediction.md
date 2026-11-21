---
type: claim
title: "Interpretability analysis indicates LPFC activity contributed significantly to the model's performance prediction"
description: "Interpretability analysis indicates LPFC activity contributed significantly to the model's performance prediction"
id: lpfc-dominates-fnirs-performance-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
sources:
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025
    title: Shayla Sharmin and Roghayeh Leila Barmaki 2025
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: shayla-sharmin-and-roghayeh-leila-barmaki-2025-2
    title: Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Interpretability analysis indicates LPFC activity contributed significantly to the model's performance prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 associational `r1`, 1 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` PCA component 2 showed a stronger total contribution from LPFC (6.99) than VMPFC (5.36), and GRU Feature 6 correlated most strongly with PC2 (r = 0.65). [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025](#shayla-sharmin-and-roghayeh-leila-barmaki-2025)
`q2 i?` SHAP analysis identified GRU Features 0 and 3 as most influential in final decision-making, both correlated with PC2. [→ Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)](#shayla-sharmin-and-roghayeh-leila-barmaki-2025-2)

## Evidence

### Shayla Sharmin and Roghayeh Leila Barmaki 2025

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `design · r2`

Multi-stage interpretability analysis combining PCA, GRU feature correlation, and SHAP on the trained model. The results section reports PC2's stronger LPFC contribution and, in the next stage, GRU Feature 6's correlation with PC2 (r = 0.65).

> "PC2 exhibited a stronger total contribution from LPFC (6.99) compared to VMPFC(5.36), which suggests that this component reflects distributed LPFC activity."

### Shayla Sharmin and Roghayeh Leila Barmaki 2025 (2)

Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals. Companion Proceedings of the 27th International Conference on Multimodal Interaction (ICMI Companion '25). https://doi.org/10.1145/3747327.3764901

`q2 · i?` · `associational · r1`

SHAP-based decision-stage analysis of the trained CNN-GRU model (Figure 4). The results section reports GRU Features 3 and 0 had the highest SHAP values with correlations to PC2 of r = -0.67 and r = 0.42.

> "As shown in Figure 4, GRU Features 3 and 0 had the highest SHAP values, indicating their strong impact in decision-making. Interestingly, these features also showed notable correlation with PC2—GRU3 negatively(𝑟=−0.67)and GRU0 positively(𝑟=0.42)."

## Discussion


## Related Claims
- [The lateral prefrontal cortex showed greater hemodynamic activity during learning, with game-condition ∆HbO 2.33 times higher than the video condition](lpfc-greater-hemodynamic-activity-gbl.md) — related
