---
type: design
id: three-stage-dataset-analysis-workflow
title: "Three-stage dataset analysis workflow: differential/enrichment, survival, then machine-learning modeling"
description: The system organizes practice into three sequential stages.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
sources:
  - id: qiu-kangli-2025
    resource: "https://doi.org/10.1186/s12909-025-07631-8"
    title: "Qiu Kangli, Zeng Tianshu, Xia Wenfang, Peng Miaomiao, Kong Wen. (2025). Interdisciplinary medical education practices: building a case-driven interdisciplinary simulation system based on public datasets. BMC Medical Education. https://doi.org/10.1186/s12909-025-07631-8"
    author: Qiu Kangli, Zeng Tianshu, Xia Wenfang, Peng Miaomiao, Kong Wen
---

# Three-stage dataset analysis workflow: differential/enrichment, survival, then machine-learning modeling

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system organizes practice into three sequential stages. As the article states, 'Stage I involves differential and enrichment analyses using the GEO datasets. Stage II conducts survival analysis utilizing the TCGA datasets. Stage III entails constructing and analyzing machine learning models for the diseases identified in the previous two stages.' Each stage is broken into numbered process steps with dynamically adjustable parameters (P-value, LogFC, enrichment thresholds), letting students compare algorithms such as DESeq2, edgeR, and limma.

## Design Implications

### Context
#### Requirements
- Datasets with grouping information, survival status data, and clinical biochemical indicators; R and Python toolkits
#### Constraints
- General screening criterion for differentially expressed genes is an absolute log2FC greater than 1

### Target Learners
- medical students learning bioinformatics analysis

### Learning Goals
- standard process of disease-based data analysis from model algorithms to result presentation

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Qiu Kangli, Zeng Tianshu, Xia Wenfang, Peng Miaomiao, Kong Wen. (2025). Interdisciplinary medical education practices: building a case-driven interdisciplinary simulation system based on public datasets. BMC Medical Education. https://doi.org/10.1186/s12909-025-07631-8
