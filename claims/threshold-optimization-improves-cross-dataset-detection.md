---
type: claim
title: Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8
description: Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8
id: threshold-optimization-improves-cross-dataset-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bühler-2025
    resource: "https://doi.org/10.1007/s40593-024-00412-2"
    title: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2"
    author: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E."
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Lowering the prediction threshold from 0.5 to 0.3 raised the person-level correlation between true and predicted mind wandering proportion in cross-dataset prediction from 0.48 (P = 0.07) to 0.8 (P < 0.001), a large correlation. [→ Bühler 2025](#buhler-2025)
`q2 i?` Optimal thresholds are smaller than 0.5 for most classifiers, and lower thresholds lead to notable improvements in F1 values. [→ Bühler 2025](#buhler-2025)

## Evidence

### Bühler 2025

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2

`q2 · i3` · `design · r2`

Person-level aggregation of instance-by-instance predictions on the in-the-wild dataset. The article reports r = 0.48 (P = 0.07) at the default threshold and r = 0.8 (P < 0.001) after adapting the threshold to 0.3, underscoring threshold fine-tuning for cross-dataset use. The printed r = 0.8 is a large correlation.

> "For cross-dataset predictions, we found a correlation of 0.48 (P = 0.07) on a person-level. However, when adapting the prediction threshold from 0.5 to 0.3 we achieve a correlation of 0.8 (P < 0.001)."

## Discussion


## Related Claims
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459](latent-features-within-lab-mind-wandering-detection.md) — related
