---
type: claim
title: About 400 labeled proofs are sufficient for adequate autograding performance
description: About 400 labeled proofs are sufficient for adequate autograding performance
id: 400-proofs-sufficient-training
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: zhao-2025
    resource: "https://doi.org/10.1007/s40593-025-00498-2"
    title: "Zhao, C., Silva, M., & Poulsen, S. (2025). Autograding Mathematical Induction Proofs with Natural Language Processing. International Journal of Artificial Intelligence in Education, 35, 3202–3232. https://doi.org/10.1007/s40593-025-00498-2"
    author: "Zhao, C., Silva, M., & Poulsen, S."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# About 400 labeled proofs are sufficient for adequate autograding performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Model performance mostly saturates by a training set of about 400 proofs, with Llemma34b reaching 98.8% of its full-data accuracy at that size. [→ Zhao 2025](#zhao-2025)

## Evidence

### Zhao 2025

Zhao, C., Silva, M., & Poulsen, S. (2025). Autograding Mathematical Induction Proofs with Natural Language Processing. International Journal of Artificial Intelligence in Education, 35, 3202–3232. https://doi.org/10.1007/s40593-025-00498-2

`q2 · i?` · `design · r2`

Training-size sweep experiment varying training set sizes from 50 to the maximum available, with the same 30% test set held fixed. At 400 training proofs, Llemma34b achieved "98.8% of the full data size accuracy"; the article reports no standardized effect size.

> "For Llemma34b, the performance at 400 training data already achieves 98.8% of the full data size accuracy. Based on these results, we conclude that training a model with 400 proofs is suﬃcient for adequate results."

## Discussion


## Related Claims
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [An on-premises LLM autograder graded a 200-student course at 1–3 minutes wall-clock time per submission across a full term](lata-onprem-autograder-throughput.md) — related
- [Student perceptions of the autograder were mixed, with the LaTeX workflow rated more positively than the grader itself](mixed-student-perception-lata.md) — related
