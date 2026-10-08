---
type: claim
title: GPT-4 detected 45 PII words that human coders failed to redact across all nine courses
description: GPT-4 detected 45 PII words that human coders failed to redact across all nine courses
id: gpt4-detects-pii-missed-by-human-coders
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: s-singhal-2024
    resource: "https://doi.org/10.5281/zenodo.12729884"
    title: "S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884"
    author: S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 detected 45 PII words that human coders failed to redact across all nine courses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Analysis of disagreements between human and GPT-based de-identification revealed 45 PII words missed by human coders, including student names and personal webpage links. [→ S. Singhal 2024](#s-singhal-2024)

## Evidence

### S. Singhal 2024

S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884

`q2 · i?` · `design · r2`

Manual inspection of the 45 remaining human-GPT discrepancies in the 3,505-post dataset found "human coders failed to redact 45 words that involve PII", such as the name Laura in a Business Trends post and an unredacted personal webpage link.

> "we found that after the first iteration of human-based de-identification, human coders failed to redact 45 words that involve PII distributed across all the courses"

## Discussion


## Related Claims
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](gpt4-high-recall-low-precision-pii-redaction.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — related
- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](gpt4-redaction-performance-varies-by-course-content.md) — related
