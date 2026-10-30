---
type: claim
title: Machine learning models using whole-module fNIRS features predict transfer scores in all feedback groups, with the frontopolar area a predictor regardless of feedback type
description: Machine learning models using whole-module fNIRS features predict transfer scores in all feedback groups, with the frontopolar area a predictor regardless of feedback type
id: fnirs-extra-trees-predict-transfer-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yin-2025
    resource: "https://doi.org/10.1038/s41539-025-00311-8"
    title: "Yin, J., Xu, H., Pan, Y., & Hu, Y. (2025). Effects of different AI-driven Chatbot feedback on learning outcomes and brain activity. npj Science of Learning. https://doi.org/10.1038/s41539-025-00311-8"
    author: "Yin, J., Xu, H., Pan, Y., & Hu, Y."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Machine learning models using whole-module fNIRS features predict transfer scores in all feedback groups, with the frontopolar area a predictor regardless of feedback type

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Extra Trees model using brain activity from the entire learning module predicted transfer scores best across all groups, with mean R² of 0.88 (MF), 0.90 (AF), and 0.87 (NF), and identified key predictive regions including FP, SMG, DLPFC, and MTG. [→ Yin 2025](#yin-2025)

## Evidence

### Yin 2025

Yin, J., Xu, H., Pan, Y., & Hu, Y. (2025). Effects of different AI-driven Chatbot feedback on learning outcomes and brain activity. npj Science of Learning. https://doi.org/10.1038/s41539-025-00311-8

`q2 · i?` · `causal · r2`

Machine learning prediction analysis (Extra Trees ensemble with SHAP feature importance) in each feedback group; models using the whole learning module outperformed single-phase models. Key regions "that predicted transfer scores included the FP, SMG, DLPFC, and fusiform gyrus" in the MF group; SMG, DLPFC, MTG, FP in AF; SMG, MTG, FP, DLPFC in NF.

> "For the MF group, the results revealed that the mean R2 achieved 0.88, the mean MAE achieved 0.72, and the mean MSE achieved 0.93."

## Discussion


## Related Claims
- [Feedback types elicit distinct fNIRS activation patterns: frontopolar and middle temporal gyrus higher under metacognitive feedback, supramarginal gyrus under affective feedback, DLPFC under neutral feedback](chatbot-feedback-type-brain-activation-patterns.md) — related
- [In the metacognitive feedback group, frontopolar activation correlates with metacognitive sensitivity and middle temporal gyrus activation correlates with retention](frontopolar-activation-correlates-metacognitive-sensitivity-mf-group.md) — related
