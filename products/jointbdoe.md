---
type: product
id: jointbdoe
title: JointBDOE
description: JointBDOE is a YOLOv11-based, end-to-end computer-vision model developed by Chen Yuqing et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
---

# JointBDOE

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
JointBDOE is a YOLOv11-based, end-to-end computer-vision model developed by Chen Yuqing et al. for jointly detecting human bodies and estimating their orientations in multi-person scenes, including classroom video.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **JointBDOE one-stage unified body detection and orientation estimation model**: JointBDOE is a single-stage, end-to-end trainable framework built on YOLOv11 that "integrates human bounding box prediction and body orientation into a unified embedding space, enabling the simultaneous and precise estimation of human positions and orientations in multi-person scenarios". It uses a CSPDarknet53 backbone, PANet neck, a decoupled three-branch head (classification, localization, orientation), a wrapped MSE loss for angle periodicity, and a probability-threshold filter for unreliable orientation estimates. (Chen Yuqing et al. (2025))

### Claims
- [The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset](../claims/jointbdoe-decoupled-yolov11x-mebow-performance.md) [+M]
- [A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones](../claims/decoupled-head-improves-orientation-estimation.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421
