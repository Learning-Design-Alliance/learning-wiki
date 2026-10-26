---
type: claim
title: First-attempt EEG features and initial performance score predict learning rate, with higher initial scores associated with lower learning rates
description: First-attempt EEG features and initial performance score predict learning rate, with higher initial scores associated with lower learning rates
id: first-attempt-features-predict-learning-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: shafiei-2024
    resource: "https://doi.org/10.1038/s41539-024-00216-y"
    title: "Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z. (2024). Development of performance and learning rate evaluation models in robot-assisted surgery using electroencephalography and eye-tracking. npj Science of Learning 9:3. https://doi.org/10.1038/s41539-024-00216-y"
    author: "Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: shafiei-2024-2
    resource: "https://doi.org/10.1038/s41539-024-00216-y"
    title: "Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z. (2024). Development of performance and learning rate evaluation models in robot-assisted surgery using electroencephalography and eye-tracking. npj Science of Learning 9:3. https://doi.org/10.1038/s41539-024-00216-y"
    author: "Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# First-attempt EEG features and initial performance score predict learning rate, with higher initial scores associated with lower learning rates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Each one-unit increase in first-attempt performance score was associated with a 0.35-point decrease in learning rate (p = 5 × 10−4), and greater temporal flexibility in BA 46 at alpha-band frequencies was associated with a 0.87-point decrease in learning rate (p = 7 × 10−4) in the Tubes task. [→ Shafiei 2024](#shafiei-2024)
`q2 i?` In Dots and Needles, greater search information in BA 45 (estimate 1.92, p = 0.0006) and BA 40 (estimate 1.45, p = 0.0009) at first attempt was associated with higher learning rates, as was temporal flexibility in BA 41 at theta band (estimate 0.41, p = 0.021). [→ Shafiei 2024 (2)](#shafiei-2024-2)

## Evidence

### Shafiei 2024

Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z. (2024). Development of performance and learning rate evaluation models in robot-assisted surgery using electroencephalography and eye-tracking. npj Science of Learning 9:3. https://doi.org/10.1038/s41539-024-00216-y

`q2 · i?` · `associational · r1`

Multivariate linear regression for Tubes learning rate, defined as the slope of performance scores across attempts, using first-attempt features (26 subjects; R2 = 0.64, MAE 4.89, RMSE 5.73). First-attempt score was included as a baseline to adjust for individual differences.

> "Furthermore, each one-unit increase in initial performance score was associated with a 0.35-point decrease in learning rate, implying that subjects with higher initial scores tend to exhibit lower learning rates."

### Shafiei 2024 (2)

Shafiei, S. B., Shadpour, S., Sasangohar, F., Mohler, J. L., Attwood, K. & Jing, Z. (2024). Development of performance and learning rate evaluation models in robot-assisted surgery using electroencephalography and eye-tracking. npj Science of Learning 9:3. https://doi.org/10.1038/s41539-024-00216-y

`q2 · i?` · `associational · r1`

Multivariate linear regression for Dots and Needles learning rate (26 subjects; R2 = 0.69, MAE 5.69, RMSE 7.15) with first-attempt EEG features. In Suture Sponge, search information in BA 19 at gamma band was associated with a 1.19-point increase in learning rate (p = 0.01), while BA 45 theta features were associated with decreases.

> "A one-standard deviation increase in the average search information in BA 45 at beta-band frequencies was associated with a 1.92-point increase in the learning rate value for this task."

## Discussion


## Related Claims
- [EEG-derived temporal flexibility and search information in specific Brodmann areas and frequency bands are associated with simulator task performance](eeg-flexibility-search-information-associated-performance.md) — related
- [In the Tubes task, larger average pupil diameter of the nondominant eye and higher rate of saccade are associated with lower RAS simulator performance](pupil-diameter-saccade-rate-lower-tubes-performance.md) — related
- [In the Dots and Needles task, higher entropy of the nondominant eye's pupil diameter is associated with lower performance](pupil-entropy-lower-dots-needles-performance.md) — related
- [A head-confined multimodal configuration (EEG, eye tracking, forehead EDA) predicts held-out learners' five-level engagement ratings at 75.0% balanced 1-off accuracy, 12.0 points above the mode baseline](e3sense-head-confined-engagement-prediction.md) — related
- [Subject-wise standardization of eye-tracking features marginally improved the fit of performance and learning rate models](subject-wise-standardization-improves-model-fit.md) — related
