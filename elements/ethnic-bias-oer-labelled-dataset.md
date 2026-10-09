---
type: element
id: ethnic-bias-oer-labelled-dataset
title: Extended labelled dataset of 345 OER sentences with ethnic-bias annotations from 193 students
description: "A released dataset of \"345 contextualized sentences extracted from various OERs\" annotated by \"193 higher education students from the UK and US\" who self-identified as Asian, Black, mixed, or white."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: josmario-albuquerque-2026
    resource: "https://doi.org/10.18608/jla.2026.8905"
    title: "Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905"
    author: Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes
---

# Extended labelled dataset of 345 OER sentences with ethnic-bias annotations from 193 students

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
A released dataset of "345 contextualized sentences extracted from various OERs" annotated by "193 higher education students from the UK and US" who self-identified as Asian, Black, mixed, or white. Each sentence carries contextual attributes (OER title, type, subject, group reference) and counts of biased, not biased, and undecided marks, plus derived bias scores and binary labels. The article offers it "for promoting fairer artificial intelligence (AI) applications" and hosts code on GitHub for reproducibility.

## Design Implications

### Context
#### Requirements
- Access to the released dataset (figshare link printed in the article) and the companion code repository to reproduce the classification pipeline
#### Constraints
- Labels reflect perceived bias by higher education students in the UK and US; perceptions varied across individuals, reflecting the subjective nature of bias

### Target Learners
- Higher education students

### Target Learning Goals
- Detection and classification of ethnic bias in text-based learning materials
- Development of fairer AI and learning analytics tools

## Claims

- [Linguistic and psycholinguistic features such as verb ratio and aggressiveness are positively correlated with perceived ethnic bias](../claims/linguistic-features-correlate-ethnic-bias.md) [+W]
- [The naive Bayes model achieved the highest precision (0.75) for ethnic bias detection on the test set](../claims/naive-bayes-highest-precision-bias-detection.md) [+W]
- [Social sciences content is positively correlated with perceived ethnic bias in text-based learning materials](../claims/social-sciences-content-correlates-ethnic-bias.md) [+W]
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](../claims/stacking-ensemble-best-finetuning-f1.md) [+W]
- [SVM and random forest classifiers showed consistent performance in classifying ethnic bias, with F1-scores of 0.71 and 0.70 on the test set](../claims/svm-rf-consistent-bias-classification.md) [+W]

## Related Elements
- 

## Examples

- [Use interpretable feature-driven machine learning as a human-in-the-loop baseline for flagging ethnic bias in learning content](../strategies/feature-driven-ml-baseline-bias-flagging.md)

## Key Sources
- Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905
