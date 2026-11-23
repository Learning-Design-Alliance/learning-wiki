---
type: strategy
id: top-n-confidence-review-strategy
title: Teachers adaptively review the top-n students by model confidence instead of using fixed-threshold binary predictions
description: "The article recommends that teachers use the model's ROCAUC-based confidence scores to review students adaptively: \"by using ROCAUC, teachers can adaptively label the most talented n student whom the model gives the t..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: xinzhe-zheng-2025
    resource: "https://arxiv.org/abs/2509.00863"
    title: "Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. https://arxiv.org/abs/2509.00863"
    author: Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng
---

# Teachers adaptively review the top-n students by model confidence instead of using fixed-threshold binary predictions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends that teachers use the model's ROCAUC-based confidence scores to review students adaptively: "by using ROCAUC, teachers can adaptively label the most talented n student whom the model gives the top n confidence as a talented student". Because ROCAUC reflects ranking across all thresholds, teachers can choose how many students to examine each cycle rather than relying on binary predictions at a fixed threshold, which the article says prevents adaptive selection. This makes the model actionable for teachers who may be unfamiliar with the metric, since high ROCAUC means positive cases receive higher confidence than negative cases.

## Design Implications

### Context
#### Requirements
- A deployed model producing per-student confidence scores between 0 and 1 for each talent type.
- Teachers able to review and confirm model-suggested students.
#### Constraints
- The article notes a concern that not all teachers can understand the unpopular ROCAUC metric and may fail to utilize the model in practice.

### Target Learners
- secondary school students

### Target Learning Goals
- talent identification and follow-up nurturing by teachers

## Claims

- [TalentPredictor predicts seven talent types in secondary school students with a best test micro ROCAUC of 0.908 on a real-world dataset of 1,041 students](../claims/talentpredictor-0908-micro-rocauc-seven-talent-types.md) [+W]
- [The compact One Encoder gives a more balanced, stable and less overfitted predictor than the Raw Encoder, with higher average test ROCAUC (0.882 vs 0.860)](../claims/one-encoder-outperforms-raw-encoder-balance.md) [+W]

## Related Strategies

- [Pair talent identification with at-risk student detection to avoid unbalanced resource distribution](pair-talent-and-atrisk-detection-strategy.md)
- [Use fuzzy logic assessment on a spectrum rather than a binary scale to recognise student potential in teaching simulations](fuzzy-spectrum-assessment-teaching-simulations.md)
- [Use adaptive uncertainty thresholds instead of fixed domain-specific thresholds for advising decisions](adaptive-uncertainty-thresholds-advising-strategy.md)

## Examples
-

## Key Sources
- Xinzhe Zheng, Zhen-Qun Yang, Jiannong Cao, and Jiabei Cheng. (2025). Predicting Multi-Type Talented Students in Secondary School Using Semi-Supervised Machine Learning. arXiv. https://arxiv.org/abs/2509.00863
