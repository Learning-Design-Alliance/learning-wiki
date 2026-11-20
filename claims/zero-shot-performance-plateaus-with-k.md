---
type: claim
title: Zero-shot difficulty-ranking performance plateaus with decreasing variance as the number of samples/comparisons K increases
description: Zero-shot difficulty-ranking performance plateaus with decreasing variance as the number of samples/comparisons K increases
id: zero-shot-performance-plateaus-with-k
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: vatsal-raina-2024
    resource: "https://doi.org/10.48550/arXiv.2404.10704"
    title: "Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)"
    author: Vatsal Raina, Mark Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot difficulty-ranking performance plateaus with decreasing variance as the number of samples/comparisons K increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` As K increases, the performance of the absolute and comparative zero-shot systems plateaus with decreasing variance. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Numerical pattern shown in Figure 3 for the ChatGPT3.5 zero-shot systems on CMCQRD, with K samples for absolute and K comparisons for comparative. The article states that "as K increases, the performance plateaus with decreasing variance".

> "Figure 3 explores how the performance of the absolute and comparative systems vary with K. We observe that as K increases, the performance plateaus with decreasing variance."

## Discussion


## Related Claims
- [Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%](combining-level-classification-and-comparative-boosts-correlation.md) — related
- [Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%](zero-shot-comparative-difficulty-ranking-outperforms-absolute.md) — a narrower finding that bears on this claim
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
