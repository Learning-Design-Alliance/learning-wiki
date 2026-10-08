---
type: claim
title: GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion
description: GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion
id: gpt4-redaction-performance-varies-by-course-content
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

# GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Cohen's Kappa between GPT-4 and human redactions ranged from 0.267 (Poetry) to 0.843 (Design), with lower performance in courses with longer average posts and frequent mentions of public figures or historical locations. [→ S. Singhal 2024](#s-singhal-2024)

## Evidence

### S. Singhal 2024

S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884

`q2 · i?` · `design · r2`

Course-level analysis of Kappa across the nine MOOCs: the article reports "The highest Kappas were observed for Design (Kappa=0.843), Accounting (Kappa=0.824)" and Poetry lowest at Kappa=0.267, linking lower performance to longer, more qualitative posts.

> "GPT's performance appears to be lower in courses characterized by longer average post lengths, all of them exceeding 65 words (Poetry has a much higher average of 241 words per post)."

## Discussion


## Related Claims
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](gpt4-high-recall-low-precision-pii-redaction.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — related
- [GPT-4 detected 45 PII words that human coders failed to redact across all nine courses](gpt4-detects-pii-missed-by-human-coders.md) — related
- [Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall](gpt4-redaction-compared-to-prior-methods.md) — related
