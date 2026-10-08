---
type: claim
title: Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall
description: Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall
id: gpt4-redaction-compared-to-prior-methods
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: mixed
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

# Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-4's recall (0.958) exceeded Farrow et al.'s combined class-list and regular-expression approach (0.905) and Holmes et al.'s fine-tuned RoBERTa (0.84), but the best supervised machine learning approach (recall 0.970, precision 0.827) still outperformed GPT-4 (precision 0.526). [→ S. Singhal 2024](#s-singhal-2024)

## Evidence

### S. Singhal 2024

S. Singhal, A. F. Zambrano, M. Pankiewicz, X. Liu, C. Porter, and R. S. Baker. (2024). De-identifying student personally identifying information with gpt-4. Proceedings of the 17th International Conference on Educational Data Mining, pages 559-565, Atlanta, Georgia, USA. https://doi.org/10.5281/zenodo.12729884

`q2 · i?` · `design · r2`

Comparison against prior literature (Table 3) reported in the results section: GPT-4 recall of 0.958 beat Farrow et al.'s 0.905 and Holmes et al.'s 0.84, but "the current best approach using supervised machine learning algorithms" leads on both metrics.

> "the current best approach using supervised machine learning algorithms [1] still outperforms GPT-4 in this task, with a recall of 0.970 and a precision of 0.827."

## Discussion


## Related Claims
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](gpt4-high-recall-low-precision-pii-redaction.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — related
- [Fine-tuned GPT-4o-mini achieves the highest recall (0.9589) among tested PII detection models on the CRAPII dataset](fine-tuned-gpt4o-mini-highest-recall-crapii.md) — related
- [Verifier models raise PII detection precision above all other tested methods but reduce recall relative to fine-tuned GPT-4o-mini](verifier-models-raise-precision-reduce-recall.md) — related
- [GPT-4 de-identification performance varies by course, with lower agreement in courses with longer posts and more qualitative discussion](gpt4-redaction-performance-varies-by-course-content.md) — related
