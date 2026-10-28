---
type: claim
title: Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics
description: Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics
id: aes-architecture-comparison-d7
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: kumar-2020
    resource: "https://doi.org/10.1007/s40593-020-00211-5"
    title: "Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5"
    author: "Kumar, V. S., & Boulanger, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Classification architectures had higher exact-match percentages, the article's stated most important metric, while regression ensembles reached the highest testing QWK on Ideas (0.770) and Conventions (0.726). [→ Kumar 2020](#kumar-2020)

## Evidence

### Kumar 2020

Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5

`q2 · i?` · `design · r2`

Comparison of six MLP architectures (classification, regression, multiple regression, each with bagging ensemble variants) trained, validated, and tested on ASAP D7 with 397 features; Table 9 reports QWK, exact, and adjacent (±1, ±2) percentages per rubric, e.g. Classification Ensemble Ideas testing QWK 0.751.

> "Given that on average classifiers have higher accuracy in terms of percentage of exact matches (the most important metric), their performance was investigated further."

## Discussion


## Related Claims
- [Regression-based XGBoost outperforms the classification formulation for automated speech scoring on the SOPI dataset](xgboost-regression-beats-classification-speech-scoring.md) — related
- [Feature-based MLP deep learning models predict ASAP D7 rubric scores with an average QWK of 0.72 against human raters' resolved scores, exceeding the 0.60 average agreement between the two human raters](aes-d7-rubric-qwk-072-exceeds-human-agreement.md) — a broader claim this one bears on
