---
type: product
id: quantitative-suture-assessment-qsa
title: Quantitative Suture Assessment (QSA)
description: An image- and burst-pressure-based assessment pipeline developed by Spagnulo et al.
product_kind: assessment
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
---

# Quantitative Suture Assessment (QSA)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An image- and burst-pressure-based assessment pipeline developed by Spagnulo et al. for objectively measuring surgical suturing quality and technical skill in minimally invasive surgery training.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Quantitative Suture Assessment pipeline: image-derived spatial metrics with burst-pressure validation**: An ex vivo assessment pipeline in which standardized running sutures on porcine bowel are photographed under controlled conditions, annotated in MATLAB's ImageLabeler, and reduced to eighteen distance metrics (PM, PP, and combined max/mean/std/error variants) that are then correlated with intraluminal burst pressure measured via a CO2 pneumatic circuit. The article frames this as part of Quantitative Suture Assessment (QSA), "a framework for measuring variables such as stitch spacing, consistency of alignment, and mechanical strength". It was applied to compare three surgical platforms and three experience levels. (Spagnulo R et al. (2025))

### Claims
- [An XGBoost model on spatial metrics fails to predict burst pressure, indicating spatial metrics alone are insufficient standalone indicators of suture quality](../claims/xgboost-spatial-metrics-poor-burst-prediction.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Spagnulo R, Marzola F, Corso F, Distefano G, Pescio M, Hayashi K, Barontini F, Dagnino G, Althoefer K, Siciliano B, Ourselin S, Arezzo A. (2025). From precision to strength: computer vision for suture quality assessment—an ex vivo pilot study. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12441-6
