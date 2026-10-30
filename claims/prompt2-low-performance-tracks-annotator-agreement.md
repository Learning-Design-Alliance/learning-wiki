---
type: claim
title: Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)
description: Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)
id: prompt2-low-performance-tracks-annotator-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
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

# Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All models, including the XGBoost regressor, perform worst on Prompt 2, which the authors attribute to poor inter-annotator QWK agreement of 0.560 versus an average of 0.758 on other prompts. [→ Pakhi Bamdev 2023](#pakhi-bamdev-2023)

## Evidence

### Pakhi Bamdev 2023

Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5

`q2 · i?` · `design · r2`

Observational analysis in the Results section linking per-prompt model performance to human inter-annotator agreement. Prompt 2 showed "poor inter-annotator QWK agreement of 0.560" against an average of 0.758 across other prompts; the authors label the reason probable.

> "The probable reason for that can be attributed to the poor inter-annotator QWK agreement of 0.560 compared to the average QWK of 0.758 across the other prompts."

## Discussion


## Related Claims

- [In classroom video labeling, high raw agreement (often exceeding 90%) co-occurred with low chance-corrected κ due to temporal misalignment](raw-agreement-kappa-paradox-classroom-video.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement](machine-machine-above-human-machine-below-human-human.md) — related
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — related
- [Regression-based XGBoost outperforms the classification formulation for automated speech scoring on the SOPI dataset](xgboost-regression-beats-classification-speech-scoring.md) — related
- [Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6](acoustic-features-least-impact-except-prompts-2-6.md)
