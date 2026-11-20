---
type: claim
title: "ChatGPT shows a 23.8% bias toward selecting the first item in pairwise difficulty comparisons"
description: "ChatGPT shows a 23.8% bias toward selecting the first item in pairwise difficulty comparisons"
id: chatgpt-first-item-bias-in-pairwise-comparison
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

# ChatGPT shows a 23.8% bias toward selecting the first item in pairwise difficulty comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In pairwise comparative prompting, ChatGPT selected the first item over the second 23.8% more often than the reverse. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Observation from the comparative zero-shot experiments with ChatGPT3.5 on CMCQRD: a position bias was observed in the pairwise prompt, reported as "a 23.8% bias to select the first item over the second in the prompt during comparison".

> "ChatGPT was observed to have a 23.8% bias to select the first item over the second in the prompt during comparison."

## Discussion


## Related Claims
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
