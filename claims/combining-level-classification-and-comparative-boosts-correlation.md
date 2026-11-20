---
type: claim
title: "Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%"
description: "Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%"
id: combining-level-classification-and-comparative-boosts-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
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

# Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Averaging ranks of the level classification and zero-shot comparative systems yielded a Spearman correlation of 43.7±0.6, higher than either alone. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Combined-system result on CMCQRD (Table 3): rank averaging of the RACE++-trained level classifier and ChatGPT comparative approach reached 43.7±0.6 Spearman. The article describes "complementary behaviour in ranking the difficulty of MC questions".

> "We observe a significant performance jump to 43.7, suggesting the two approaches have complementary behaviour in ranking the difficulty of MC questions."

## Discussion


## Related Claims
- [Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%](zero-shot-comparative-difficulty-ranking-outperforms-absolute.md) — related
- [A RACE++-trained level classification system transfers to difficulty ranking better than a fine-tuned reading comprehension system (38.7% vs 30.8% Spearman)](level-classification-transfers-better-than-reading-comprehension.md) — related
- [Zero-shot difficulty-ranking performance plateaus with decreasing variance as the number of samples/comparisons K increases](zero-shot-performance-plateaus-with-k.md) — related
- [The open-source Mistral-7B model achieves much lower comparative difficulty-ranking correlation (17.5%) than ChatGPT](mistral-7b-weaker-comparative-ranking.md) — related
