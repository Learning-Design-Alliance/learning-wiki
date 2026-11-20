---
type: claim
title: "A RACE++-trained level classification system transfers to difficulty ranking better than a fine-tuned reading comprehension system (38.7% vs 30.8% Spearman)"
description: "A RACE++-trained level classification system transfers to difficulty ranking better than a fine-tuned reading comprehension system (38.7% vs 30.8% Spearman)"
id: level-classification-transfers-better-than-reading-comprehension
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

# A RACE++-trained level classification system transfers to difficulty ranking better than a fine-tuned reading comprehension system (38.7% vs 30.8% Spearman)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The level classification system transferred to difficulty ranking with 38.7% Spearman correlation, higher than the reading comprehension system's 30.8%. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Numerical results on CMCQRD (Table 3): level classification (ELECTRA-base ensemble trained on RACE++ levels, mapped to a continuous score via equation) reached 38.7% Spearman, while the Llama-2 reading comprehension system (difficulty = 1 minus true class probability) reached 30.8%. The article states "the level classification sys- tem hits 38.7%".

> "The task transfer ap- proaches show a positive correlation to rank MC questions. Particularly the level classification sys- tem hits 38.7%."

## Discussion


## Related Claims
- [Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%](combining-level-classification-and-comparative-boosts-correlation.md) — related
- [Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%](zero-shot-comparative-difficulty-ranking-outperforms-absolute.md) — related
