---
type: claim
title: Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352
description: Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352
id: cross-dataset-generalization-mind-wandering-detection
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
    i: "?"
    kind: design
    rigour: 2
---

# Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training on US lab reading data and predicting on Korean in-the-wild lecture data, BiLSTMs on latent features achieve F1 = 0.352 (AUC-PR = 0.26), comparable to the state-of-the-art despite cross-task, cross-cultural, in-the-wild evaluation. [→ Bühler 2025](#buhler-2025)

## Evidence

### Bühler 2025

Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2

`q2 · i?` · `design · r2`

Cross-dataset prediction (Table 3): models trained on the full lab reading dataset were applied to the in-the-wild lecture-viewing dataset (N = 15, probe-caught reports). Results outperform the random baseline (F1 = 0.25; AUC-PR = 0.17); BiLSTM on latent features reached F1 = 0.352, 11.00% above chance. Performance is described as very comparable, not superior.

> "We achieve a very comparable performance to the best performance of the state-of-the-art (Lee et al., 2022) despite cross-task evaluation, a culturally different target group, and an in-the-wild setting."

## Discussion


## Related Claims
- [Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459](latent-features-within-lab-mind-wandering-detection.md) — related
- [Latent transfer-learned features yield better overall mind wandering detection than explicit OpenFace features, and temporal models add a small improvement, especially cross-dataset](latent-features-beat-explicit-features-overall.md) — related
- [Mind wandering detection is more accurate for female than male learners, with the gender gap larger for temporal models](gender-bias-favoring-female-mind-wandering-detection.md) — related
- [LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face](lime-eye-mouth-areas-in-latent-features.md) — related
- [Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8](threshold-optimization-improves-cross-dataset-detection.md) — related
- [Questions interpolated between video lecture segments improve subsequent test performance and reduce mind wandering](interpolated-questions-improve-video-learning.md) — related
- [Carelessness detectors trained on Philippine students generalize to USA students without re-fitting](carelessness-detector-cross-country-generalizability.md) — related
- [SVM-based mind wandering detector achieved 69% precision and 67% recall generalizing to new learners](mind-wandering-detector-precision-recall.md) — related
- [Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)](neural-models-outperform-baselines-review.md) — related
