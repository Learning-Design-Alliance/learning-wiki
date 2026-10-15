---
type: product
id: tue-cs-overlap-matrix-and-lu-erasmus-decision-set
title: TU/e CS overlap matrix and LU Erasmus+ decision set
description: A paired dataset comprising approved Computer Science course-overlap pairs from TU/e and anonymized Erasmus+ course-transfer decisions from Leiden University, assembled by Arthur Nijdam et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# TU/e CS overlap matrix and LU Erasmus+ decision set

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A paired dataset comprising approved Computer Science course-overlap pairs from TU/e and anonymized Erasmus+ course-transfer decisions from Leiden University, assembled by Arthur Nijdam et al. for automated curriculum-alignment research.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Two annotated datasets: the TU/e CS overlap matrix and the LU Erasmus+ decision set**: The evaluation rests on two datasets. The TU/e CS dataset derives from the university's examination-committee-approved 'overlap matrix' for the 180 ECTS Computer Science BSc program; "After processing, this resulted in 60 unique overlapping course pairs," augmented with 180 negative pairs for training. The LU Erasmus+ dataset contains approximately 25 exchange courses (24 decisions after cleaning) taken by C-program students between 2018 and 2020, approved or partially approved by the former program director, spread over 5 students' programs and 3 universities, released on an anonymized GitHub repository. (Arthur Nijdam et al. (2026))

### Claims

- [In a worked example from real Erasmus+ decisions, some of CourseGraph's nearest-neighbor course mappings matched the program director's and others did not, one plausibly because it ignores differences in learning methods](../claims/coursegraph-mappings-align-with-program-director.md) [+W]
- [Component-level embeddings make CourseGraph interpretable: learning outcomes contributed most to an example overlap decision](../claims/coursegraph-component-level-interpretability.md) [+W]
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](../claims/rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910
