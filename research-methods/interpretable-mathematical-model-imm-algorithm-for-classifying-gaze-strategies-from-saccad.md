---
type: research-method
id: interpretable-mathematical-model-imm-algorithm-for-classifying-gaze-strategies-from-saccad
title: Interpretable mathematical model (IMM) algorithm for classifying gaze strategies from saccade properties
description: The IMM is an algorithm that transforms sequences of saccades on the graph area into classifications of horizontal or vertical scanning.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Interpretable mathematical model (IMM) algorithm for classifying gaze strategies from saccade properties

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The IMM is an algorithm that transforms sequences of saccades on the graph area into classifications of horizontal or vertical scanning. It maps saccades to values based on length (200-pixel cutoff) and slope (0.875 cutoff), removes short saccades, counts runs of consecutive long horizontal or vertical scans, and outputs a binary classification. The authors state "The best model we found relies on the following algorithm, which is based on saccade lengths and angles." Cut-off values were found empirically by testing values close to a slope of 1.

## Accounts
<!-- How each source describes or uses the method -->
- **Interpretable mathematical model (IMM) algorithm for classifying gaze strategies from saccade properties**: The IMM is an algorithm that transforms sequences of saccades on the graph area into classifications of horizontal or vertical scanning. It maps saccades to values based on length (200-pixel cutoff) and slope (0.875 cutoff), removes short saccades, counts runs of consecutive long horizontal or vertical scans, and outputs a binary classification. The authors state "The best model we found relies on the following algorithm, which is based on saccade lengths and angles." Cut-off values were found empirically by testing values close to a slope of 1. (Boels et al. (2024))

### Claims
- [An interpretable mathematical model based on saccade lengths and angles performs well, is transparent, and is theoretically meaningful for identifying students' histogram strategies](../claims/imm-transparent-performs-well.md) [+M]
- [The machine learning algorithm and the interpretable mathematical model identified the same task-solving strategies from students' gaze data](../claims/mla-imm-identify-same-strategies.md) [+M]

## Related Research Methods
-

## Key Sources
- Boels, L., Garcia Moreno-Esteva, E., Bakker, A., & Drijvers, P. (2024). Automated Gaze-Based Identification of Students' Strategies in Histogram Tasks through an Interpretable Mathematical Model and a Machine Learning Algorithm. International Journal of Artificial Intelligence in Education, 34, 931-973. https://doi.org/10.1007/s40593-023-00368-9
