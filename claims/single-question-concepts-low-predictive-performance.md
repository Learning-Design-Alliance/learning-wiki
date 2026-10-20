---
type: claim
title: Concepts associated with only a single post-test question yield markedly low predictive performance across all modeling approaches
description: Concepts associated with only a single post-test question yield markedly low predictive performance across all modeling approaches
id: single-question-concepts-low-predictive-performance
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

# Concepts associated with only a single post-test question yield markedly low predictive performance across all modeling approaches

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Single-question concepts produced an average R² of 0.046 across all models, attributed to reliability issues from dependence on a single binary response susceptible to guess-and-slip behavior. [→ Henderson 2020](#henderson-2020)

## Evidence

### Henderson 2020

Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/

`q2 · i?` · `associational · r2`

Analysis of predictive performance for concepts mapped to only one post-test item in the 316-student Geniventure dataset. These concepts "produced an average R2 value of 0.046 across all the models."

> "concepts that contained only a single question (i.e. 9, 11-12, 14) produced noticeably low R2 values. These single-question concepts produced an average R2 value of 0.046 across all the models."

## Discussion


## Related Claims

- [The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts](single-task-rf-best-average-not-universally-optimal.md)
- [Overlapping concepts (sharing post-test questions with other concepts) yield higher student scores and higher model R², and multi-task modeling across all concepts is detrimental for these concepts](overlapping-concepts-higher-performance-multi-task-detrimental.md) — related
- [Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions](sequential-models-outperform-static-multi-question-concepts.md) — related
- [A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies](hybrid-stealth-assessment-outperforms-single-model.md) — related
