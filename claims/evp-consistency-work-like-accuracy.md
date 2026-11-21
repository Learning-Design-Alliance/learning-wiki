---
type: claim
title: Word-level analysis of high-frequency polysemous words suggests a strong degree of consistency in the CEFR classifications provided by the EVP
description: Word-level analysis of high-frequency polysemous words suggests a strong degree of consistency in the CEFR classifications provided by the EVP
id: evp-consistency-work-like-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: stefano-bannò-2025
    resource: "https://doi.org/10.18653/v1/2025.bea-1.45"
    title: "Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)"
    author: Stefano Bannò, Kate M. Knill, Mark J. F. Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Word-level analysis of high-frequency polysemous words suggests a strong degree of consistency in the CEFR classifications provided by the EVP

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Checking whether the words 'work' and 'like' appear in EFCAMDAT essays at their EVP-assigned level or above yields high accuracy (e.g. 96.8% for 'work' at ≥A2), suggesting strong EVP consistency. [→ Stefano Bannò 2025](#stefano-banno-2025)

## Evidence

### Stefano Bannò 2025

Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. [doi:10.18653/v1/2025.bea-1.45](https://doi.org/10.18653/v1/2025.bea-1.45)

`q2 · i?` · `design · r2`

Word-level analysis (Section 4.7, Table 5) reversing the prediction approach: the two most common polysemous words in EFCAMDAT, work and like, have their Qwen-predicted level distributions examined across essay levels, scoring accuracy for appearance at the assigned level or above (work: 88.6% ≥B2, 90.6% ≥B1, 96.8% ≥A2).

> "The results show high accuracy and suggest a strong degree of consistency in the CEFR classification provided by the EVP."

## Discussion


## Related Claims
- [LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases](llm-evp-sense-disambiguation-accuracy.md) — related
- [LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words](llms-beat-pos-baseline-word-level-cefr.md) — related
