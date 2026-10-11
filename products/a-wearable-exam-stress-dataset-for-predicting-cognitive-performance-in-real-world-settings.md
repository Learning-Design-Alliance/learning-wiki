---
type: product
id: a-wearable-exam-stress-dataset-for-predicting-cognitive-performance-in-real-world-settings
title: A Wearable Exam Stress Dataset for Predicting Cognitive Performance in Real-World Settings
description: An open-access PhysioNet dataset of Empatica E4 physiological signals collected from college students during exams, released for studying stress and predicting cognitive performance.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# A Wearable Exam Stress Dataset for Predicting Cognitive Performance in Real-World Settings

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An open-access PhysioNet dataset of Empatica E4 physiological signals collected from college students during exams, released for studying stress and predicting cognitive performance.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Wearable Exam Stress Dataset (PhysioNet) processed into a balanced 328,655-sample multivariate classification dataset**: The study uses the open-access "A Wearable Exam Stress Dataset for Predicting Cognitive Performance in Real-World Settings" from PhysioNet, collected from 10 college students wearing the Empatica E4 wristband during Midterm 1, Midterm 2, and a Final exam. After preprocessing (pivoting to wide format, removing rows with missing values, grade normalization and categorization into A–F, and undersampling to balance classes at 65,731 observations per grade category), "The final processed dataset contains 328,655 samples" with five physiological predictors (ACC, BVP, EDA, HR, TEMP), three exam-participation indicators, and the grade category as target. (Lala Yamazaki et al. (2026))

### Claims
- [Using all collected physiological features improves exam-grade prediction accuracy to 96% over the 80% achieved by prior EDA-only analyses](../claims/multivariate-features-improve-accuracy-over-eda-only-benchmark.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Lala Yamazaki and Ramchandra Rimal. (2026). Leveraging Physiological Signals to Predict Exam Outcomes with Machine Learning. https://arxiv.org/abs/2606.14960
