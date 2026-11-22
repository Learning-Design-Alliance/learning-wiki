---
type: product
id: ai-based-instrument-identification-system-for-surgical-skill-evaluation-from-video
title: AI-based instrument identification system for surgical skill evaluation from video
description: An Anaut Co., Ltd.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
---

# AI-based instrument identification system for surgical skill evaluation from video

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An Anaut Co., Ltd. software system that uses DeepLab v2 semantic segmentation and kinematic analysis of laparoscopic instrument video to evaluate surgical skill and support feedback for trainee surgeons.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AI-based instrument identification system for surgical skill evaluation from video (DeepLab v2-based semantic segmentation with fluctuation analysis)**: A video-based skill evaluation system in which a DeepLab v2-based AI algorithm developed by Anaut Co., Ltd. performs semantic segmentation of the HARMONIC ultrasonic coagulation shears, identifying the X and Y coordinates of the active blade tip. The system colors the blade and tip with an afterimage of the previous 10 frames and displays "The X and Y coordinates, velocity, acceleration, and jerk of the tip are displayed at the top left of the screen." Kinematic indices and the fluctuation index β are then computed from the coordinate time series. It was evaluated on 18 laparoscopic distal gastrectomy videos. (Matsumoto Shiro et al. (2024))

### Claims
- [The fluctuation index β was significantly higher in experts (1.45 vs 1.29), indicating more regular instrument movement, with a ROC cutoff of 1.4 giving 77.8% sensitivity and specificity](../claims/fluctuation-beta-higher-experts-cutoff-1-4.md) [+M]
- [An AI semantic segmentation algorithm identifies the HARMONIC shears active blade and tip from laparoscopic video with high accuracy (blade TPR 0.873, Dice 0.837; tip TPR 0.813, Dice 0.846)](../claims/ai-shears-tip-identification-accuracy-gastrectomy.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Matsumoto Shiro, Kawahira Hiroshi, Fukata Kyohei, Doi Yasunori, Kobayashi Nao, Hosoya Yoshinori, Sata Naohiro. (2024). Laparoscopic distal gastrectomy skill evaluation from video: a new artificial intelligence-based instrument identification system. Scientific Reports. https://doi.org/10.1038/s41598-024-63388-y
