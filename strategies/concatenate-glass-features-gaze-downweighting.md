---
type: strategy
id: concatenate-glass-features-gaze-downweighting
title: Concatenate eyeglass-detection features with model outputs so the network can down-weight unreliable gaze features
description: "The strategy extracts features from a glass-detection network (ResNet18 fine-tuned on the MeGlass dataset) and concatenates them with bi-LSTM outputs, letting the network \"decide whether the reflection in the glasses..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: bodonhelyi-2026
    resource: "https://arxiv.org/abs/2602.09904"
    title: "Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. https://arxiv.org/abs/2602.09904"
    author: Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E
---

# Concatenate eyeglass-detection features with model outputs so the network can down-weight unreliable gaze features

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The strategy extracts features from a glass-detection network (ResNet18 fine-tuned on the MeGlass dataset) and concatenates them with bi-LSTM outputs, letting the network "decide whether the reflection in the glasses makes the gaze feature extraction irrelevant" instead of discarding gaze features for glasses wearers. Per-participant means and standard deviations of the glass features are added before the linear projection layer.

## Design Implications

### Context
#### Requirements
- A pre-trained glass-detection network fine-tuned on a glass-involved dataset (MeGlass), plus webcam video input from which OpenFace and EmoNet features are extracted.
#### Constraints
- The reported benefit was task-dependent: slight improvement on non-mind-wandering datasets but not on mind-wandering datasets, and the features "have yet to be thoroughly evaluated on more balanced datasets".

### Target Learners
- online learners, including the large share who wear eyeglasses

### Target Learning Goals
- accurate disengagement detection for learners wearing glasses

## Claims

- [Glasses reflections can render eyes unrecognizable in webcam frames while OpenFace confidence stays above 0.97](../claims/glasses-reflection-high-openface-confidence.md) [+W]
- [Eyeglass-detection (MeGlass) features slightly improved non-mind-wandering detection but not mind-wandering detection](../claims/meglass-features-mixed-benefit-learner-state.md) [+W]
- [LIME analysis shows the latent features mainly encode information from eye and mouth areas of the face](../claims/lime-eye-mouth-areas-in-latent-features.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. https://arxiv.org/abs/2602.09904
