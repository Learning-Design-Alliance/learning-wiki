---
type: element
id: adaptive-g-ukt-benchmark-datasets
title: Four large-scale real-world sequential knowledge tracing benchmark datasets used to evaluate Adaptive G-UKT
description: "The evaluation corpus comprises four large-scale real-world sequential datasets: \"ASSISTments2009, Bridge2Algebra2006, Algebra2005, and NIPS34\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: jia-nan-2026
    resource: "https://doi.org/10.1038/s41598-026-50711-y"
    title: "Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue. (2026). Adaptive G-UKT: a unified probabilistic framework for knowledge tracing via adaptive graph topology learning and uncertainty-aware Gaussian embeddings. Scientific Reports. https://doi.org/10.1038/s41598-026-50711-y"
    author: Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue
---

# Four large-scale real-world sequential knowledge tracing benchmark datasets used to evaluate Adaptive G-UKT

> **Element** · [All elements](index.md)

## Description
The evaluation corpus comprises four large-scale real-world sequential datasets: "ASSISTments2009, Bridge2Algebra2006, Algebra2005, and NIPS34". These datasets supply the historical observation streams of exercise-response pairs over which the model predicts next-response probability and against which state-of-the-art baselines are compared, with the authors reporting particular advantages in sparse data regimes.

## Design Implications

### Context
#### Requirements
- Datasets must provide sequential exercise-response interaction streams with item-concept associations
#### Constraints
- 

### Target Learners
- students whose response logs populate the ASSISTments, Bridge to Algebra, Algebra, and NIPS34 datasets

### Target Learning Goals
- predicting correctness of future exercise responses from interaction history

## Related Elements
- 

## Examples
-

## Key Sources
- Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue. (2026). Adaptive G-UKT: a unified probabilistic framework for knowledge tracing via adaptive graph topology learning and uncertainty-aware Gaussian embeddings. Scientific Reports. https://doi.org/10.1038/s41598-026-50711-y
