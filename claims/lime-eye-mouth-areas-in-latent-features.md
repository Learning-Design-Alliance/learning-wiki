---
type: claim
title: LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face
description: LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face
id: lime-eye-mouth-areas-in-latent-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bühler-2025
    resource: "https://doi.org/10.1007/s40593-024-00412-2"
    title: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2"
    author: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Post-hoc explainability analysis indicates the CNN feature extractor mainly relies on eye and mouth areas, which are consequently encoded in the latent feature vectors. [→ Bühler 2025](#buhler-2025)

## Evidence

### Bühler 2025

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2

`q1 · i?` · `design · r2`

Explainability analysis applying LIME super-pixel highlighting to the pre-trained ResNet50 FER model fine-tuned for mind wandering detection (Figs. 7–8). The authors interpret the findings as validating that the learned information aligns with established theoretical frameworks and as consistent with prior work on facial textures and AUs.

> "We see that the CNN part of our classification model, employed for feature extraction, mainly relies on information from the eye and mouth areas of the participants, which are consequently inherently encoded in our feature vectors as well."

## Discussion


## Related Claims
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [K-Means clustering of LIME feature-importance profiles identifies 2 responder and 4 non-responder subgroups within binary intervention-response classes](lime-clustering-dyslexia-subgroups.md) — related
