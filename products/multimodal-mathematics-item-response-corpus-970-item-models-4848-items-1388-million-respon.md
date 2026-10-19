---
type: product
id: multimodal-mathematics-item-response-corpus-970-item-models-4848-items-1388-million-respon
title: "Multimodal mathematics item-response corpus: 970 item models, 4,848 items, 13.88 million responses"
description: A corpus of multimodal multiple-choice mathematics items and 13.88 million student responses created by Christopher Ormerod et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Multimodal mathematics item-response corpus: 970 item models, 4,848 items, 13.88 million responses

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
A corpus of multimodal multiple-choice mathematics items and 13.88 million student responses created by Christopher Ormerod et al. for item-parameter estimation and difficulty calibration in assessment development.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Multimodal mathematics item-response corpus: 970 item models, 4,848 items, 13.88 million responses**: The study's dataset consists of multiple-choice mathematics items, each with a stimulus and four options where stimulus and options may include image components combined into one image, generated from item models specifying structure, content and variable features. The article reports "There were a total of 970 item models and a total of 4,848 items" and "There are 13.88 million responses", split into train, development and test sets by item model to avoid conflation, with approximately 2860 responses per item on average. (Christopher Ormerod et al. (2026))

### Claims

- [A fine-tuned Qwen3.5-9B simulated-respondent model predicts item difficulty with Pearson correlation 0.85, exceeding MathBERT (0.68) and MetaMath (0.75) baselines](../claims/llm-simulated-respondents-predict-item-difficulty-above-regression-baselines.md) [+W]
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](../claims/simulated-respondents-recover-guessing-parameter-048.md) [+W]
- [Discrimination parameter recovery is weak (Pearson 0.31 for Qwen3.5-9B, below MathBERT's 0.35), with slope information partially lost through ability discretization](../claims/weak-discrimination-parameter-recovery.md) [-W]
- [Under a five-band discretization of difficulty, the simulated-respondent model reaches quadratic weighted kappa 0.835 versus 0.692 (MetaMath) and 0.625 (MathBERT)](../claims/qwk-discretized-difficulty-agreement-0835.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Christopher Ormerod and YoungKoung Kim. (2026). Multimodal Item Parameter Estimation using Simulated Response Probabilities. https://arxiv.org/abs/2608.10154v1
