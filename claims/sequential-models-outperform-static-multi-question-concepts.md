---
type: claim
title: Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions
description: Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions
id: sequential-models-outperform-static-multi-question-concepts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
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

# Sequential deep learning models outperform static models for concepts mapped to multiple post-test questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For concepts mapped to multiple post-test questions, sequential deep learning models achieved higher average R² (0.224 single-task, 0.222 multi-task) than static models (0.214 single-task, 0.210 multi-task). [→ Henderson 2020](#henderson-2020)

## Evidence

### Henderson 2020

Henderson, N., Kumaran, V., Min, W., Mott, B., Wu, Z., Boulden, D., Lord, T., Reichsman, F., Dorsey, C., Wiebe, E., & Lester, J. (2020). Enhancing Student Competency Models for Game-Based Learning with a Hybrid Stealth Assessment Framework. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020), 92-103. https://educationaldatamining.org/EDM2020/proceedings/

`q2 · i?` · `associational · r2`

Subset analysis of concepts with multiple post-test questions from the same 316-student Geniventure dataset. Sequential models "produced a higher and more consistent performance" than static models on these concepts.

> "when considering only the concepts that mapped to multiple questions (i.e. 1-8, 13, 15-16), the deep-learning based sequential models produced a higher and more consistent performance (0.224 for single-task, 0.222 for multi-task) than the static models (0.214 for single-task, 0.210 for multi-task) on average."

## Discussion


## Related Claims
- [Overlapping concepts (sharing post-test questions with other concepts) yield higher student scores and higher model R², and multi-task modeling across all concepts is detrimental for these concepts](overlapping-concepts-higher-performance-multi-task-detrimental.md) — related
- [A hybrid stealth assessment framework selecting the optimal model per concept outperforms any single homogeneous modeling technique for predicting student competencies](hybrid-stealth-assessment-outperforms-single-model.md) — related
- [The single-task Random Forest achieves the best average predictive performance but is optimal for only 7 of 15 concepts](single-task-rf-best-average-not-universally-optimal.md) — related
- [Concepts associated with only a single post-test question yield markedly low predictive performance across all modeling approaches](single-question-concepts-low-predictive-performance.md) — related
