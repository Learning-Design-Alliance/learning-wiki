---
type: claim
title: GSR and heart rate variance predict extraversion level in a Random Forest personality model built from physiological signals
description: GSR and heart rate variance predict extraversion level in a Random Forest personality model built from physiological signals
id: physiological-gsr-hr-variance-predict-extraversion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: tseng-2023
    resource: "https://doi.org/10.1080/2331186x.2023.2245637"
    title: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)"
    author: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GSR and heart rate variance predict extraversion level in a Random Forest personality model built from physiological signals

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a 30-participant signal-collection study, a Random Forest model predicting extraversion class achieved an out-of-bag error of 10.34%, with delta_gsr12, delta_hr12, and gsr2_var confirmed as important variables. [→ Tseng 2023](#tseng-2023)

## Evidence

### Tseng 2023

Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)

`q2 · i?` · `causal · r1`

A modeling study with 30 Yuan Ze University electrical engineering students: sensors recorded GSR and heart rate while participants watched a JavaScript video; variance and delta features were used with Boruta variable selection to build a Random Forest model. The quote shows the confirmed variables "delta_gsr12, delta_hr12, gsr2_var" for Ex_class; the printed OOB error was 10.34%.

> "As suggested by Boruta, delta_gsr12, delta_hr12, gsr2_var were important variables to predict Ex_class."

## Discussion


## Related Claims
- [Heart rate variance predicts agreeableness and conscientiousness levels, with Random Forest OOB errors of 27.59% and 24.14%](hr-variance-predicts-agreeableness-conscientiousness.md) — related
- [No effective prediction model was found for emotional stability or openness, though tendencies were observed](no-effective-model-emotional-stability-openness.md) — related
