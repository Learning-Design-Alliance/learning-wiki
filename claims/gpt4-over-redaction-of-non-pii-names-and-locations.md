---
type: claim
title: GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions
description: GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions
id: gpt4-over-redaction-of-non-pii-names-and-locations
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

# GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-4 could not reliably distinguish names of artists, scientists, or political leaders from student names, redacted country and institution names needed for course discussions, and redacted mythological creature names like Cyclops. [→ S. Singhal 2024](#s-singhal-2024)

## Evidence

### S. Singhal 2024

S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884

`q2 · i?` · `design · r2`

Qualitative error analysis of GPT-4 outputs: in the Poetry course, names such as "John Latouche" and "Jackson Pollock" were inappropriately redacted; in Business Trends, countries like the UK were redacted; in Mythology, the word Cyclops was redacted.

> "GPT was not always able to successfully differentiate the names of artists, scientists, or political leaders from the names of students."

## Discussion


## Related Claims
- [GPT-4 detected 45 PII words that human coders failed to redact across all nine courses](gpt4-detects-pii-missed-by-human-coders.md) — related
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](gpt4-high-recall-low-precision-pii-redaction.md) — a broader claim this one bears on
- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](gpt4-redaction-performance-varies-by-course-content.md) — related
- [Low-precision PII detection disrupts the semantic integrity of educational data: Presidio and Azure AI Language false positives alter intended meaning while GPT-based models preserve it](low-precision-pii-detection-semantic-disruption.md) — reports the opposite
- [Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall](gpt4-redaction-compared-to-prior-methods.md) — related
