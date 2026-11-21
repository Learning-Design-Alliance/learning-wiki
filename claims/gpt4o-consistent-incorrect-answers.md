---
type: claim
title: "GPT-4o's incorrect answers are far from random, gravitating toward specific incorrect answers"
description: "GPT-4o's incorrect answers are far from random, gravitating toward specific incorrect answers"
id: gpt4o-consistent-incorrect-answers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gerd-kortemeyer-2025
    resource: "https://doi.org/10.1103/98hg-rkrf"
    title: "Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic. (2025). Multilingual Performance of a Multimodal Artificial Intelligence System on Multisubject Physics Concept Inventories. [doi:10.1103/98hg-rkrf](https://doi.org/10.1103/98hg-rkrf)"
    author: Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o's incorrect answers are far from random, gravitating toward specific incorrect answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among items where all three answers were incorrect, 53% had three identical incorrect answers and only 8% had three different ones, against random expectations of 6.25% and 37.5% respectively; 66% of all items had the same two incorrect answers. [→ Gerd Kortemeyer 2025](#gerd-kortemeyer-2025)

## Evidence

### Gerd Kortemeyer 2025

Gerd Kortemeyer, Marina Babayeva, Giulia Polverini, Ralf Widenhorn, Bor Gregorcic. (2025). Multilingual Performance of a Multimodal Artificial Intelligence System on Multisubject Physics Concept Inventories. [doi:10.1103/98hg-rkrf](https://doi.org/10.1103/98hg-rkrf)

`q2 · i?` · `design · r2`

Analysis of repeated-response agreement on incorrect answers across the three submissions per item, benchmarked against the article's printed random-selection expectations; similar trends were observed for English and non-English items. No effect size is reported.

> "In reality, AI responses were far from random and gravitate toward specific incorrect answers: 53% of such items had three identical incorrect answers, while only 8% had three different ones."

## Discussion


## Related Claims
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [GPT-4o averages 71.1% on English physics concept inventories, with individual inventory scores ranging from 27% to 97%](gpt4o-english-inventory-average-71-percent.md) — related
- [Items difficult for GPT-4o in English tend to remain difficult in other languages, with correct-response rates rising from 18% to 82% as English agreement increases](item-difficulty-consistent-across-languages.md) — related
