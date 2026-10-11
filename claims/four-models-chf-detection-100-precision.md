---
type: claim
title: "Four supervised models (MLP, CNN, PCA-MLP, transformers) were effective for image-based critical heat flux detection with 100% precision, with PCA-MLP fastest at 1s/epoch and the transformer slowest at 212s/epoch"
description: "Four supervised models (MLP, CNN, PCA-MLP, transformers) were effective for image-based critical heat flux detection with 100% precision, with PCA-MLP fastest at 1s/epoch and the transformer slowest at 212s/epoch"
id: four-models-chf-detection-100-precision
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: changgen-li-2025
    resource: "https://github.com/hanhuark/machine-learning-for-engineers"
    title: "Changgen Li, Han Hu, Christy Dunlap, Nathaniel House, and Jonathan Wai. (2025). Giving Mechanical Engineers Intelligent Tools: A Project-Based AI Education Curriculum in Thermal Engineering. https://github.com/hanhuark/machine-learning-for-engineers"
    author: Changgen Li, Han Hu, Christy Dunlap, Nathaniel House, and Jonathan Wai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Four supervised models (MLP, CNN, PCA-MLP, transformers) were effective for image-based critical heat flux detection with 100% precision, with PCA-MLP fastest at 1s/epoch and the transformer slowest at 212s/epoch

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All four supervised models achieved effective image-based critical heat flux detection with 100% precision, differing in training efficiency. [→ Changgen Li 2025](#changgen-li-2025)

## Evidence

### Changgen Li 2025

Changgen Li, Han Hu, Christy Dunlap, Nathaniel House, and Jonathan Wai. (2025). Giving Mechanical Engineers Intelligent Tools: A Project-Based AI Education Curriculum in Thermal Engineering. https://github.com/hanhuark/machine-learning-for-engineers

`q2 · i?` · `design · r2`

A student project (Dunlap et al.) developed four supervised models on boiling images for critical heat flux assessment. The article reports "a precision of 100%" for all four models, with PCA-MLP at 1s/epoch and the transformer at 212s/epoch. No effect size is printed.

> "This work demonstrate d that all four state-of-the-art models were effective for image-based critical heat flux detection with a precision of 100%."

## Discussion


## Related Claims
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related
- [In a student project on laser-drilled hole diameter detection, GPR significantly outperformed MLP in detection accuracy and training speed](gpr-outperformed-mlp-hole-diameter-detection.md) — related
- [PCA models were useful for two-phase cooling system monitoring based on multi-modal input (acoustic signals, hydrophone signals, and boiling images)](pca-multimodal-cooling-monitoring.md) — related
