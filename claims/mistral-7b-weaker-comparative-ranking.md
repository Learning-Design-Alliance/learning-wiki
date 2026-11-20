---
type: claim
title: "The open-source Mistral-7B model achieves much lower comparative difficulty-ranking correlation (17.5%) than ChatGPT"
description: "The open-source Mistral-7B model achieves much lower comparative difficulty-ranking correlation (17.5%) than ChatGPT"
id: mistral-7b-weaker-comparative-ranking
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

# The open-source Mistral-7B model achieves much lower comparative difficulty-ranking correlation (17.5%) than ChatGPT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mistral-7B with 100 pairwise comparisons reached 17.5% Spearman correlation, lower than ChatGPT. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Appendix E reports Mistral-7B on the comparative approach with 100 pairwise comparisons on CMCQRD, reaching 17.5% Spearman's rank correlation. The authors state "the smaller model struggles to make sensible comparisons for a task with this challenge level".

> "Us- ing the smaller model, with 100 pairwise compar- isons, the Spearman’s rank correlation is 17.5%. The lower performance compared to ChatGPT sug- gests the smaller model struggles to make sensible comparisons for a task with this challenge level."

## Discussion


## Related Claims
- [Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%](zero-shot-comparative-difficulty-ranking-outperforms-absolute.md) — related
- [Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%](combining-level-classification-and-comparative-boosts-correlation.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
