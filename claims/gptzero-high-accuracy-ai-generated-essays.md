---
type: claim
title: GPTZero correctly classifies AI-generated essays as AI at very high rates regardless of essay length
description: GPTZero correctly classifies AI-generated essays as AI at very high rates regardless of essay length
id: gptzero-high-accuracy-ai-generated-essays
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: selin-dik-2025
    resource: "https://doi.org/10.48550/arXiv.2506.23517"
    title: "Selin Dik, Osman Erdem, and Mehmet Dik. (2025). Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays. Originally published 2024. [doi:10.48550/arXiv.2506.23517](https://doi.org/10.48550/arXiv.2506.23517)"
    author: Selin Dik, Osman Erdem, and Mehmet Dik
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPTZero correctly classifies AI-generated essays as AI at very high rates regardless of essay length

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For all AI-generated essay length categories, GPTZero's average assessed likelihood that essays were AI-written never went below 98%. [→ Selin Dik 2025](#selin-dik-2025)

## Evidence

### Selin Dik 2025

Selin Dik, Osman Erdem, and Mehmet Dik. (2025). Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays. Originally published 2024. [doi:10.48550/arXiv.2506.23517](https://doi.org/10.48550/arXiv.2506.23517)

`q2 · i?` · `design · r2`

In this study's essay-submission experiment, 28 AI-generated essays across short, medium, and long categories were individually inputted into GPTZero. The authors report that "For all AI categories, this chance never went below 98%", and the confusion matrix shows all 28 AI essays predicted as AI.

> "For example, for short essays, on average, GPTZero said that the given essays were 99% likely to be written by AI. For all AI categories, this chance never went below 98%."

## Discussion


## Related Claims
- [GPTZero's assessed AI likelihood for human essays fluctuates across length categories rather than approaching the ideal 0%](gptzero-human-essay-scores-fluctuate.md) — related
- [False positives on human essays vary by length: short and long human essays were flagged more often than medium-length ones](essay-length-moderates-gptzero-false-positives.md) — related
