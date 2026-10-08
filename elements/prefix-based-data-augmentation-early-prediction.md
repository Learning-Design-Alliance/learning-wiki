---
type: element
id: prefix-based-data-augmentation-early-prediction
title: Prefix-based data augmentation for early prediction in educational sequences
description: "A data augmentation technique in which, instead of sliding windows or cropping, \"we generate all prefixes of each sequence (from length 1 to n), allowing the model to learn to make predictions at any point in a studen..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: alice-xu-2026
    resource: "https://doi.org/10.18608/jla.2026.9099"
    title: "Alice Xu, Icy (Yunyi) Zhang, Adam B. Blake and James W. Stigler. (2026). Modelability as a Strategy for Improving the Generalizability and Scalability of Predictive Models. Journal of Learning Analytics, 13(1). https://doi.org/10.18608/jla.2026.9099"
    author: Alice Xu, Icy (Yunyi) Zhang, Adam B. Blake and James W. Stigler
---

# Prefix-based data augmentation for early prediction in educational sequences

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 associational, 1 design), `q2` · 1 of 2 report an effect size · 3 claims rest on one study

## Description
A data augmentation technique in which, instead of sliding windows or cropping, "we generate all prefixes of each sequence (from length 1 to n), allowing the model to learn to make predictions at any point in a student's progression". Each student contributes twelve records, each masking all data after a given chapter, so models can be trained and evaluated on data available only through each chapter of the course.

## Design Implications

### Context
#### Requirements
- Augmentation must occur after the train/test split across cross-validation rounds to prevent data leakage from a student's augmented traces appearing in both sets.
#### Constraints
- Models trained on all 12 chapters may rely on later-chapter behaviors not yet available early in the course, limiting early prediction accuracy.

### Target Learners
- students in courses using instrumented online textbooks

### Target Learning Goals
- early identification of at-risk students before course completion

## Claims

- [Behavioral-only metrics from an instrumented online textbook support early prediction of final course grades in flipped statistics courses](../claims/behavioral-only-early-prediction-flipped-statistics.md) [+W]
- [Predictive models built in a modelable ecosystem generalize across institutions](../claims/cross-institutional-generalizability-coursekata-models.md) [+W]
- [A memory-augmented deep learning model improves hint-taking prediction by 12-15 AUC points over a fixed-length history baseline on two datasets](../claims/memory-augmented-model-improves-hint-prediction.md) [+W]

## Related Elements
- [Coursekata Instrumented Online Textbook](coursekata-instrumented-online-textbook.md)

## Examples
-

## Key Sources
- Alice Xu, Icy (Yunyi) Zhang, Adam B. Blake and James W. Stigler. (2026). Modelability as a Strategy for Improving the Generalizability and Scalability of Predictive Models. Journal of Learning Analytics, 13(1). https://doi.org/10.18608/jla.2026.9099
