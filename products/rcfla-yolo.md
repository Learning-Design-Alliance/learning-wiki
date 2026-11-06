---
type: product
id: rcfla-yolo
title: RCFLA-YOLO
description: "RCFLA-YOLO is the authors' YOLOv11-based software framework for automatically classifying root canal filling length as acceptable or unacceptable in periapical radiographs."
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
---

# RCFLA-YOLO

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
RCFLA-YOLO is the authors' YOLOv11-based software framework for automatically classifying root canal filling length as acceptable or unacceptable in periapical radiographs.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **RCFLA-YOLO seven-stage framework for automated acceptability evaluation of root canal filling length**: RCFLA-YOLO is a deep-learning framework that evaluates whether root canal filling length is acceptable in periapical radiographs, built on the YOLOv11 object detection architecture. The article describes that "the proposed method has been developed in seven stages", moving from data collection and expert labeling through preprocessing to 1280 × 640 pixels, training and testing of YOLOv11 variants, and confusion-matrix-based performance evaluation. The highest-performing variant (YOLOv11m) is incorporated into the proposed method, with output classes Length-Acceptable and Length-UnAcceptable. (Ayhan Muhammed et al. (2025))

### Claims
- [The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset](../claims/rcfla-yolo-yolov11m-performance-rcfl-dataset.md) [+M]
- [Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models](../claims/yolov11m-highest-map50-among-yolo-variants.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan. (2025). RCFLA-YOLO: a deep learning-driven framework for the automated assessment of root canal filling quality in periapical radiographs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07483-2
