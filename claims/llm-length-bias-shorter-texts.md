---
type: claim
title: The tested LLMs tend to produce shorter texts than the originals regardless of whether the intent is to simplify or complexify
description: The tested LLMs tend to produce shorter texts than the originals regardless of whether the intent is to simplify or complexify
id: llm-length-bias-shorter-texts
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

# The tested LLMs tend to produce shorter texts than the originals regardless of whether the intent is to simplify or complexify

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The three LLMs show a tendency to produce shorter texts than the originals, in both few-shot and zero-shot settings, regardless of the intended direction of readability change. [→ Chieh-Yang Huang 2024](#chieh-yang-huang-2024)

## Evidence

### Chieh-Yang Huang 2024

Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)

`q2 · i?` · `design · r2`

Manual inspection of generated articles identified a shortening bias: originals averaged 825 words while few-shot outputs were 350-500 words; a similar pattern appeared in zero-shot scenarios (500-600 words), suggesting a possible bias in off-the-shelf LLMs.

> "we found a tendency for the models to produce shorter texts than the originals (Original: 825 words, Few-Shot: 350-500 words), regardless of whether the intention was to simplify or complexify the texts."

## Discussion


## Related Claims
- [Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation](few-shot-prompting-improves-leveled-text-generation.md) — related
- [LLM-generated leveled texts skew more complex than the intended Lexile level regardless of model or prompting approach](generated-texts-skew-more-complex-than-intended.md) — related
