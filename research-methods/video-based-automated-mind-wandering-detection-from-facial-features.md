---
type: research-method
id: video-based-automated-mind-wandering-detection-from-facial-features
title: Video-based automated mind-wandering detection from facial features
description: A detection pipeline in which the article uses transfer learning, where the feature extraction part of a ResNet50 CNN pre-trained on the AffectNet facial expression recognition dataset is applied to webcam video.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Video-based automated mind-wandering detection from facial features

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A detection pipeline in which the article uses transfer learning, where the feature extraction part of a ResNet50 CNN pre-trained on the AffectNet facial expression recognition dataset is applied to webcam video. Faces are detected frame-wise with RetinaFace, aligned, cropped, and fed to the CNN without its classification layer, producing a 2048-digit latent feature vector passed to downstream classifiers including SVMs, XGBoost, DNNs, and LSTM/BiLSTM temporal models, with an optional fine-tuned end-to-end CNN-LSTM variant.

## Accounts
<!-- How each source describes or uses the method -->
- **Transfer-learning pipeline using AffectNet-pretrained ResNet50 latent features for video-based mind wandering detection**: A detection pipeline in which the article uses transfer learning, where the feature extraction part of a ResNet50 CNN pre-trained on the AffectNet facial expression recognition dataset is applied to webcam video. Faces are detected frame-wise with RetinaFace, aligned, cropped, and fed to the CNN without its classification layer, producing a 2048-digit latent feature vector passed to downstream classifiers including SVMs, XGBoost, DNNs, and LSTM/BiLSTM temporal models, with an optional fine-tuned end-to-end CNN-LSTM variant. (Bühler et al. (2025))

### Claims
- [Transfer-learned latent facial features support above-chance video-based mind wandering detection within a lab reading dataset, with LSTM reaching F1 = 0.459](../claims/latent-features-within-lab-mind-wandering-detection.md) [+M]
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](../claims/cross-dataset-generalization-mind-wandering-detection.md) [+M]

## Related Research Methods
-

## Key Sources
- Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2
