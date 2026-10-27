---
type: claim
title: Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459
description: Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459
id: latent-features-within-lab-mind-wandering-detection
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

# Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Within the lab reading dataset, models trained on latent AffectNet features outperform the random baseline to a significant extent, with F1 scores up to 0.459 (LSTM) and about 14% above chance. [→ Bühler 2025](#buhler-2025)

## Evidence

### Bühler 2025

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2

`q2 · i?` · `design · r2`

Person-independent 4-fold cross-validated evaluation on the lab dataset (Bosch & D'Mello, 2021; N = 135 students, 10-second video clips). Models on latent features outperformed the random baseline "to a significant extent"; Table 2 shows LSTM F1 = 0.459 and DNN AUC-PR = 0.398. The article notes F1 scores are driven by high recall with low precision.

> "In the within-task prediction setting, models trained on latent features outperform the random baseline (i.e., F1 = 0.3 (Bosch & D'Mello, 2021) and AU C−PR = 0.3) to a significant extent."

## Discussion


## Related Claims
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Mind wandering detection is more accurate for female than male learners, with the gender gap larger for temporal models](gender-bias-favoring-female-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — a broader claim this one bears on
- [Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8](threshold-optimization-improves-cross-dataset-detection.md) — related
