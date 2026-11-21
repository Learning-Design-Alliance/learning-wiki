---
type: claim
title: "Heart rate variance predicts agreeableness and conscientiousness levels, with Random Forest OOB errors of 27.59% and 24.14%"
description: "Heart rate variance predicts agreeableness and conscientiousness levels, with Random Forest OOB errors of 27.59% and 24.14%"
id: hr-variance-predicts-agreeableness-conscientiousness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: tseng-2023
    resource: "https://doi.org/10.1080/2331186x.2023.2245637"
    title: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)"
    author: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: tseng-2023-2
    resource: "https://doi.org/10.1080/2331186x.2023.2245637"
    title: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)"
    author: "Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Heart rate variance predicts agreeableness and conscientiousness levels, with Random Forest OOB errors of 27.59% and 24.14%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A Random Forest model predicting agreeableness class used Ex_class, Co_class, and hr2_var as important variables and reached an OOB error of 27.59%. [→ Tseng 2023](#tseng-2023)
`q2 i?` A Random Forest model predicting conscientiousness class used delta_gsr23, delta_hr13, and gsr2_var as important variables and reached an OOB error of 24.14%. [→ Tseng 2023 (2)](#tseng-2023-2)

## Evidence

### Tseng 2023

Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)

`q2 · i?` · `causal · r1`

In the same 30-participant signal-collection study, the agreeableness Random Forest used "Ex_class, Co_class, and hr2_var" as important variables; the printed OOB error was 27.59%.

> "To predict Ag_class, Boruta suggested that important variables were Ex_class, Co_class, and hr2_var, and the corresponding mean decrease accuracy was 23.55775, 37.66948, and 14.26147, respectively."

### Tseng 2023 (2)

Tseng, C.-H., Lin, H.-C. K., Huang, A. C.-W., & Lin, J.-R. (2023). Personalized Programming Education: Using Machine Learning to Boost Learning Performance Based on Students' Personality Traits. Originally published 2022. [doi:10.1080/2331186x.2023.2245637](https://doi.org/10.1080/2331186x.2023.2245637)

`q2 · i?` · `causal · r1`

In the same study, the conscientiousness Random Forest used "delta_gsr23, delta_hr13, and gsr2_var"; the printed OOB error was 24.14%.

> "To predict Co_class, Boruta suggested that important variables were delta_gsr23, delta_hr13, andgsr2_var,andthecorrespondingmeandecreaseaccuracywere12.84836,30.57563,and28.50746, respectively. The resulting OOB error was 24.14%"

## Discussion


## Related Claims
- [GSR and heart rate variance predict extraversion level in a Random Forest personality model built from physiological signals](physiological-gsr-hr-variance-predict-extraversion.md) — related
- [No effective prediction model was found for emotional stability or openness, though tendencies were observed](no-effective-model-emotional-stability-openness.md) — related
