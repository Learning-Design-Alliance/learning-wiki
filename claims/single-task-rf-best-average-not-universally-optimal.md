---
type: claim
title: The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts
description: The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts
id: single-task-rf-best-average-not-universally-optimal
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: henderson-2020
    resource: "https://educationaldatamining.org/EDM2020/proceedings/"
    title: "Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/"
    author: "Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Single-task Random Forest achieved the highest average R² (0.206) across all concepts but was the optimal model for only 7 out of 15 concepts, demonstrating that average performance does not guarantee per-concept optimality. [→ Henderson 2020](#henderson-2020)

## Evidence

### Henderson 2020

Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/

`q2 · i?` · `associational · r2`

Held-out test set evaluation of multiple regression model types across 15 genetics concepts in Geniventure gameplay data from 316 students. The single-task Random Forest achieved the highest mean R² but was "only the optimal model for 7 out of the 15 total concepts."

> "The best performing model in terms of average R2 value across all concepts was the single-task Random Forest; however, it was only the optimal model for 7 out of the 15 total concepts."

## Discussion


## Related Claims

- [GRU is the lowest-performing model across both single-task and multi-task competency modeling, likely due to its two gating units versus LSTMs' three](gru-lowest-performing-competency-model.md)
- [Overlapping concepts (sharing post-test questions with other concepts) yield higher student scores and higher model R², and multi-task modeling across all concepts is detrimental for these concepts](overlapping-concepts-higher-performance-multi-task-detrimental.md)
- [Concepts associated with only a single post-test question yield markedly low predictive performance across all modeling approaches](single-question-concepts-low-predictive-performance.md)
- [Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions](sequential-models-outperform-static-multi-question-concepts.md) — related
- [A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies](hybrid-stealth-assessment-outperforms-single-model.md) — a broader claim this one bears on
