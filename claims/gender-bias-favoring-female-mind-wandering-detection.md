---
type: claim
title: Mind wandering detection is more accurate for female than male learners, with the gender gap larger for temporal models
description: Mind wandering detection is more accurate for female than male learners, with the gender gap larger for temporal models
id: gender-bias-favoring-female-mind-wandering-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: bühler-2025
    resource: "https://doi.org/10.1007/s40593-024-00412-2"
    title: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2"
    author: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Mind wandering detection is more accurate for female than male learners, with the gender gap larger for temporal models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across both prediction scenarios and all latent-feature models, mind wandering instances are predicted more accurately for females than for males. [→ Bühler 2025](#buhler-2025)
`q2 i?` The gender difference becomes larger with temporal models, especially in within-dataset prediction, which the authors attribute to the increased parameter count requiring large training data. [→ Bühler 2025](#buhler-2025)

## Evidence

### Bühler 2025

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2

`q2 · i?` · `design · r2`

Gender comparison of all latent-feature models (Table 6) in within- and cross-dataset prediction; e.g., LSTM within-dataset AUC-PR 0.458 (female) vs 0.328 (male). The article attributes the gap to dataset imbalance in overall gender rates and gender-specific mind wandering rates, giving fewer male mind wandering instances in training.

> "In general, mind wandering instances are predicted more accurately for females than for males."

## Discussion


## Related Claims
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [Female children and adolescents recognize vocal emotions more accurately than males, with no interaction between sex and age](female-advantage-vocal-emotion-recognition-stable.md) — related
- [Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459](latent-features-within-lab-mind-wandering-detection.md) — related
