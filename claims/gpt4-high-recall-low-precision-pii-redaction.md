---
type: claim
title: GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts
description: GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts
id: gpt4-high-recall-low-precision-pii-redaction
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

# GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across nine MOOCs, GPT-4 identified almost all PII (recall consistently over 0.85 per course, average 0.958) but frequently over-redacted non-PII names and locations (precision below 0.75 in all courses, average 0.526). [→ S. Singhal 2024](#s-singhal-2024)

## Evidence

### S. Singhal 2024

S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884

`q2 · i?` · `design · r2`

Evaluation of GPT-4 redaction against corrected human ground truth on 3,505 forum posts from nine MOOCs, averaged over three runs. The article reports "The recall rate was consistently over 0.85 for all courses examined" and precision below 0.75 in all cases; Table 2 gives averages of 0.958 recall and 0.526 precision.

> "The recall rate was consistently over 0.85 for all courses examined. However, precision was lower than 0.75 in all cases. These results show that GPT identified almost all PII."

## Discussion


## Related Claims
- [GPT-4 detected 45 PII words that human coders failed to redact across all nine courses](gpt4-detects-pii-missed-by-human-coders.md) — related
- [Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall](gpt4-redaction-compared-to-prior-methods.md) — related
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](fine-tuned-gpt4o-mini-highest-recall-crapii.md) — related
- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](gpt4-redaction-performance-varies-by-course-content.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — a narrower finding that bears on this claim
