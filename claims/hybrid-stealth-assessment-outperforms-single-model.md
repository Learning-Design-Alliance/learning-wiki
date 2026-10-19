---
type: claim
title: A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies
description: A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies
id: hybrid-stealth-assessment-outperforms-single-model
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

# A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Selecting the optimal model for each individual concept yields a mean R² of 0.241, a 17.0% improvement over using the best single model (single-task Random Forest, mean R² 0.206) for all concepts. [→ Henderson 2020](#henderson-2020)
`q2 i?` Static, sequential, single-task, and multi-task models were each selected as optimal for at least one concept, explaining why the heterogeneous approach induces higher performance. [→ Henderson 2020](#henderson-2020)

## Evidence

### Henderson 2020

Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/

`q2 · i?` · `associational · r2`

Predictive modeling study of 316 students' gameplay logs in Geniventure, evaluating static and sequential single-task and multi-task regression models on held-out test sets. The hybrid framework achieved "a performance of 0.241" mean R² versus 0.206 for the best homogeneous baseline.

> "by using our proposed hybrid system approach and selecting the optimal model for each individual concept, we can obtain a performance of 0.241, which is a 17.0% improvement compared to a homogenous framework typically used within stealth assessment."

## Discussion


## Related Claims

- [Overlapping concepts (sharing post-test questions with other concepts) yield higher student scores and higher model R², and multi-task modeling across all concepts is detrimental for these concepts](overlapping-concepts-higher-performance-multi-task-detrimental.md)
