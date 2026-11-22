---
type: design
id: mmla-closed-loop-eeg-engagement-pipeline
title: Closed-loop MMLA engagement-detection pipeline with dual-device EEG validation
description: "A pilot pipeline for classroom engagement monitoring that pairs two EEG systems: the consumer-grade Emotiv EpocX (14 channels, 128 Hz) and the research-grade OpenBCI Cyton+Daisy (16 wet active electrodes, 125 Hz)."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: adusumilli-2026
    resource: "https://arxiv.org/abs/2610.05178"
    title: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. https://arxiv.org/abs/2610.05178"
    author: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S"
---

# Closed-loop MMLA engagement-detection pipeline with dual-device EEG validation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A pilot pipeline for classroom engagement monitoring that pairs two EEG systems: the consumer-grade Emotiv EpocX (14 channels, 128 Hz) and the research-grade OpenBCI Cyton+Daisy (16 wet active electrodes, 125 Hz). Data are processed in EEGLAB (bandpass 0.5-50 Hz, 60 Hz notch, ICA artifact removal), segmented into 1-second epochs, and converted to band powers for PCA-reduced logistic-regression classification, "the pilot implementation of a closed-loop engagement detection pipeline" within an authentic graduate classroom.

## Design Implications

### Context
#### Requirements
- Two simultaneous EEG recordings per session are feasible; preprocessing via EEGLAB/MATLAB with ICA; PCA feature reduction to mitigate overfitting with small samples
#### Constraints
- Neurophysiological subsample of n=8 limits statistical power; results are proof-of-concept rather than population estimates; between-session design confounds time-of-day and session order; no concurrent eye-tracking or EDA for multimodal fusion validation

### Target Learners
- graduate students in live classroom environments

### Learning Goals
- objective, non-invasive monitoring of learner engagement during instruction

### Claims
- [Eeg Classification Preference Matching Openbci 83](../claims/eeg-classification-preference-matching-openbci-83.md) [+M]

## Related Designs

- [CytonRK: a custom head-mounted portable EEG recorder for classroom use](cytonrk-portable-eeg-headset.md)

## Examples
-

## Key Sources
- Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. https://arxiv.org/abs/2610.05178. [doi:10.1109/icalt68022.2026.00126](https://doi.org/10.1109/icalt68022.2026.00126)
