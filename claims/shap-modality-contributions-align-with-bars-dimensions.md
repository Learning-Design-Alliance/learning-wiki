---
type: claim
title: "SHAP modality attributions aligned with each BARS dimension's behavioral focus, supporting interpretable feedback"
description: "SHAP modality attributions aligned with each BARS dimension's behavioral focus, supporting interpretable feedback"
id: shap-modality-contributions-align-with-bars-dimensions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: hung-yue-suen-and-kuo-en-hung-2026
    resource: "https://doi.org/10.1109/TLT.2026.3693864"
    title: "Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864"
    author: Hung-Yue Suen and Kuo-En Hung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SHAP modality attributions aligned with each BARS dimension's behavioral focus, supporting interpretable feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` SHAP analysis showed acoustic features dominated Voice & Talk (74.2% of predictive power) and Clarity, oculomotor features dominated Eye Contact, textual features dominated Topic and Content, and facial cues were primary for Nonverbal Expressiveness. [→ Hung-Yue Suen and Kuo-En Hung 2026](#hung-yue-suen-and-kuo-en-hung-2026)

## Evidence

### Hung-Yue Suen and Kuo-En Hung 2026

Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864

`q2 · i?` · `design · r2`

SHAP attributions aggregated to the modality level and normalized within each of the seven models (Table III); modality importance was not proportional to feature count despite the 3,780-dimensional facial feature set.

> "For Voice & Talk, the 203 acoustic features collectively contributed 74.2% of predictive power, indicating that fewer, highly informative features can outweigh larger but more redundant feature sets."

## Discussion


## Related Claims
- [Adult learners using the closed-loop ITS improved significantly across all seven BARS presentation dimensions over a 30-day practice window (Cohen's d = 0.39–0.90)](its-prepost-gains-all-seven-bars-dimensions.md) — related
- [Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance](multimodal-xgboost-expert-comparable-scoring.md) — related
