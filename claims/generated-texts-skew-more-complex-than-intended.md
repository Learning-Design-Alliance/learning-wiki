---
type: claim
title: LLM-generated leveled texts skew more complex than the intended Lexile level regardless of model or prompting approach
description: LLM-generated leveled texts skew more complex than the intended Lexile level regardless of model or prompting approach
id: generated-texts-skew-more-complex-than-intended
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: chieh-yang-huang-2024
    resource: "https://doi.org/10.1145/3690712.3690718"
    title: "Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)"
    author: Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated leveled texts skew more complex than the intended Lexile level regardless of model or prompting approach

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all models and prompting settings, a higher proportion of generated texts fall above the intended Lexile score, indicating generated texts are generally more complex than intended. [→ Chieh-Yang Huang 2024](#chieh-yang-huang-2024)

## Evidence

### Chieh-Yang Huang 2024

Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)

`q2 · i?` · `design · r2`

Numerical result shown in scatter plots (Figures 2 and 3) comparing intended versus resulting Lexile scores and shifts for all six model-prompting settings; the red-shaded area marks the ±50-point match region, and points cluster above it.

> "we can clearly observe that a higher proportion of the data points are located above the red-shaded area, indicating that the generated texts are generally more complex than the intended level."

## Discussion


## Related Claims
- [Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels](iterative-prompting-improves-readability-alignment.md) — related
- [Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation](few-shot-prompting-improves-leveled-text-generation.md) — related
- [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy](llm-abstraction-bias-higher-order-overproduction.md) — related
- [Revising texts to improve readability-formula scores often produces nonexistent or insignificant comprehension gains](readability-revision-gains-nonexistent-insignificant.md) — related
- [In the district study, teachers assigned articles above students' STAR Lexile levels (about 375 points higher on average), and greater STAR growth related to completing more, harder, and more accurate ReadWorks assignments](readworks-assignment-difficulty-growth-association.md) — related
- [The tested LLMs tend to produce shorter texts than the originals regardless of whether the intent is to simplify or complexify](llm-length-bias-shorter-texts.md) — related
