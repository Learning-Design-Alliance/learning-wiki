---
type: product
id: trace-grade-prediction-training-code-and-anonymized-dataset-release
title: TRACE-grade-prediction training code and anonymized dataset release
description: "Paul Savala's TRACE release provides training code and an anonymized subset of enrollment records for retraining and replicating grade and course prediction models at other institutions."
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# TRACE-grade-prediction training code and anonymized dataset release

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Paul Savala's TRACE release provides training code and an anonymized subset of enrollment records for retraining and replicating grade and course prediction models at other institutions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **TRACE training code and anonymized dataset release on GitHub**: The author released training code and an anonymized subset of the data to support replication and adaptation by other institutions. The article states the architecture "requires no institution-specific feature engineering—course and major embeddings are learned from enrollment data alone, and the model can be retrained on any institution's historical records without structural modification." Code is available at https://github.com/paulsavala/TRACE-grade-prediction. (Paul Savala (2026))
- **Two-course Coursera clickstream dataset for grade prediction**: The dataset comprises clickstream logs from two Coursera courses run January through April 2013: an algebra course with 43,361 students used for training (first 80%) and validation (remaining 20%), and a pre-calculus course with 51,069 students used as testing data. For the classification task the article reports 5,577,375 training clicks, 1,311,938 validation clicks, and 6,531,139 test clicks, with 6,749 training, 1,688 validation, and 8,984 test instances. Three feature sets were derived: raw clicks (2,648 types, not generalizable), 46 course-consistent click categories, and 10 HMM/MMM session states that are almost course-independent. (Yohan Jo et al. (2018))

### Claims

- [Course prediction achieves modest classification metrics (F1 0.4432) yet the auxiliary task regularizes representations and improves grade prediction](../claims/course-prediction-metrics-auxiliary-task.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Paul Savala. (2026). Jointly Predicting Courses and Grades Using a Transformer-Based Model. arXiv. https://arxiv.org/abs/2608.13409
- Yohan Jo, Keith Maki, Gaurav Tomar. (2018). Time Series Analysis of Clickstream Logs from Online Courses. https://arxiv.org/abs/1809.04177
