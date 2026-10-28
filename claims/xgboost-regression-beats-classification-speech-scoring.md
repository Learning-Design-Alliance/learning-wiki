---
type: claim
title: Regression-based XGBoost outperforms the classification formulation for automated speech scoring on the SOPI dataset
description: Regression-based XGBoost outperforms the classification formulation for automated speech scoring on the SOPI dataset
id: xgboost-regression-beats-classification-speech-scoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: pakhi-bamdev-2023
    resource: "https://doi.org/10.1007/s40593-022-00291-5"
    title: "Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5"
    author: Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Regression-based XGBoost outperforms the classification formulation for automated speech scoring on the SOPI dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Regression-based XGBoost achieves higher average QWK (0.475) than classification XGBoost (0.458) for speech scoring on the SOPI dataset. [→ Pakhi Bamdev 2023](#pakhi-bamdev-2023)

## Evidence

### Pakhi Bamdev 2023

Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5

`q2 · i?` · `design · r2`

Model comparison on the SOPI test split across six prompts, reported in the Results section. Regression XGBoost achieved "an average QWK of 0.475, r of 0.493, and MSE of 0.299"; classification XGBoost averaged QWK 0.458, r 0.484, MSE 0.333.

> "On comparison, we notice that for regression analysis, XGBoost outperforms every other model by achieving an average QWK of 0.475, r of 0.493, and MSE of 0.299 across all the six prompts."

## Discussion


## Related Claims
- [In static concurrent prediction, TabPFN outperformed Random Forest, XGBoost and Linear Regression across the four emotional and proficiency targets](tabpfn-outperforms-baselines-static-concurrent-prediction.md) — related
- [Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)](prompt2-low-performance-tracks-annotator-agreement.md) — related
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
- [Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics](aes-architecture-comparison-d7.md) — related
