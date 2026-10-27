---
type: claim
title: Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance
description: Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance
id: multimodal-xgboost-expert-comparable-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hung-yue-suen-and-kuo-en-hung-2026
    resource: "https://doi.org/10.1109/TLT.2026.3693864"
    title: "Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864"
    author: Hung-Yue Suen and Kuo-En Hung
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: hung-yue-suen-and-kuo-en-hung-2026-2
    resource: "https://doi.org/10.1109/TLT.2026.3693864"
    title: "Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864"
    author: Hung-Yue Suen and Kuo-En Hung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multimodal XGBoost models achieved rubric-aligned scoring comparable to expert ratings, and no single modality approached multimodal performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Seven speaker-independent XGBoost regression models trained on 10,360 MOOC video segments reached R² = 0.48–0.61, Spearman's ρ = 0.69–0.78, and MAE = 0.43–0.57 against expert BARS ratings. [→ Hung-Yue Suen and Kuo-En Hung 2026](#hung-yue-suen-and-kuo-en-hung-2026)
`q2 i?` Unimodal baselines using only acoustic, facial, oculomotor, or textual features performed noticeably weaker (R² mostly 0.12–0.32; ρ around 0.34–0.56). [→ Hung-Yue Suen and Kuo-En Hung 2026 (2)](#hung-yue-suen-and-kuo-en-hung-2026-2)

## Evidence

### Hung-Yue Suen and Kuo-En Hung 2026

Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864

`q2 · i?` · `design · r2`

Speaker-independent evaluation on a held-out test set (15% partition) of seven XGBoost regression models trained on 4,374-dimensional early-fused multimodal features from 10,360 MOOC segments annotated by about 30 experts.

> "Across the dimensions, R² values ranged from 0.48 to 0.61, Spearman's ρ fell between 0.69 and 0.78, and MAE values were generally between 0.43 and 0.57."

### Hung-Yue Suen and Kuo-En Hung 2026 (2)

Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864

`q2 · i?` · `design · r2`

Unimodal baseline models trained with only acoustic, facial, oculomotor, or textual features; "None of the single-modality models approached the consistency observed in the multimodal setting," supporting early feature-level fusion.

> "unimodal R² values mostly fell between 0.12 and 0.32, with Spearman correlations around 0.34 to 0.56. None of the single-modality models approached the consistency observed in the multimodal setting."

## Discussion


## Related Claims

- [Adult learners using the closed-loop ITS improved significantly across all seven BARS presentation dimensions over a 30-day practice window (Cohen's d = 0.39–0.90)](its-prepost-gains-all-seven-bars-dimensions.md) — related
- [Domain-matched experts judged 87% of Bespoke-generated lecture videos at or above the rubric midpoint corresponding to a standard MOOC lecture's quality (mean G = 3.42 of 5)](bespoke-87-percent-mooc-comparable-quality.md) — related
- [Pedagogy and production dimensions associated most strongly with global quality (Spearman ρ = 0.68 and 0.66), while content was relatively independent (ρ = 0.46)](bespoke-pedagogy-production-correlate-with-global-quality.md) — related
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](ca-selective-best-average-agreement-drawings.md) — related
- [Across rubric dimensions, content scored highest (A = 4.03) while production scored lowest (D = 3.41), driven by synthetic voice quality (D1 = 3.16)](bespoke-content-strongest-production-weakest-voice.md) — related
- [SHAP modality attributions aligned with each BARS dimension's behavioral focus, supporting interpretable feedback](shap-modality-contributions-align-with-bars-dimensions.md) — related
- [Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6](acoustic-features-least-impact-except-prompts-2-6.md)
