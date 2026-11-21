---
type: claim
title: "False positives on human essays vary by length: short and long human essays were flagged more often than medium-length ones"
description: "False positives on human essays vary by length: short and long human essays were flagged more often than medium-length ones"
id: essay-length-moderates-gptzero-false-positives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
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

# False positives on human essays vary by length: short and long human essays were flagged more often than medium-length ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPTZero was more likely to wrongly identify human essays in the short (0-100 word) and long (350-800 word) categories, while medium-length human essays were identified most accurately. [→ Selin Dik 2025](#selin-dik-2025)

## Evidence

### Selin Dik 2025

Selin Dik, Osman Erdem, and Mehmet Dik. (2025). Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays. Originally published 2024. [doi:10.48550/arXiv.2506.23517](https://doi.org/10.48550/arXiv.2506.23517)

`q2 · i?` · `design · r2`

In the study's length-category comparison of 50 human essays, Table 1 reports average assessed AI likelihood of 35.56% for short, 10.29% for medium, and 14.75% for long human essays; the authors found GPTZero "more likely to wrongly identify" short and long human essays.

> "we found that GPTZero was more likely to wrongly identify human essays that were between zero and one-hundred words and human essays that were longer than three-hundred-fifty words."

## Discussion


## Related Claims
- [GPTZero's assessed AI likelihood for human essays fluctuates across length categories rather than approaching the ideal 0%](gptzero-human-essay-scores-fluctuate.md) — related
- [GPTZero misclassified 8 of 50 human-written essays as AI, a 16% false positive rate](gptzero-false-positives-human-essays-16-percent.md) — related
- [GPTZero correctly classifies AI-generated essays as AI at very high rates regardless of essay length](gptzero-high-accuracy-ai-generated-essays.md) — related
