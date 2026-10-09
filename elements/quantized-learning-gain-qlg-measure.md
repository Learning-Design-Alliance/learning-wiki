---
type: element
id: quantized-learning-gain-qlg-measure
title: "Quantized Learning Gain (QLG): a binary High/Low measure of whether a student benefited from a learning environment"
description: Quantized Learning Gain is a binary qualitative measurement introduced to avoid the asymmetry problems of Normalized Learning Gain for students with high pretest scores.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: ye-mao-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
---

# Quantized Learning Gain (QLG): a binary High/Low measure of whether a student benefited from a learning environment

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
Quantized Learning Gain is a binary qualitative measurement introduced to avoid the asymmetry problems of Normalized Learning Gain for students with high pretest scores. Per the article, "Our QLG is a binary qualitative measurement on students' learning gains from pretest to the posttest: High vs. Low." Students are split into low, medium and high performance groups by pre- and post-test percentiles (33rd and 66th); moving up or staying high yields High QLG, coded 1, while moving down or staying low/medium yields Low QLG, coded 0.

## Design Implications

### Context
#### Requirements
- Requires both pre-test and post-test scores, which the authors note are not always available in public educational datasets
#### Constraints
- The current QLG definition labels a student improving from 1% to 32% as Low QLG, the same category as a student declining from 32% to 30%

### Target Learners
- college students training on intelligent tutoring systems

### Target Learning Goals
- measuring whether students benefited from tutoring, as a prediction target for adaptive intervention

## Related Elements
- 

## Examples

- [Use early student-model predictions to identify at-risk students and adapt pedagogical strategy during tutoring](../strategies/early-prediction-adaptive-pedagogical-strategy.md)

## Key Sources
- Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318
