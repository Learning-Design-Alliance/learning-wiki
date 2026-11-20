---
type: claim
title: Manual inspection finds LLM-generated leveled texts risk introducing misinformation and show inconsistent edit distribution
description: Manual inspection finds LLM-generated leveled texts risk introducing misinformation and show inconsistent edit distribution
id: generated-leveled-texts-misinformation-and-uneven-edits
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

# Manual inspection finds LLM-generated leveled texts risk introducing misinformation and show inconsistent edit distribution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Manual quality inspection of generated texts revealed potential misinformation, particularly altered quotations and factual inaccuracies, and inconsistent distribution of edits leading to uneven readability across the article. [→ Chieh-Yang Huang 2024](#chieh-yang-huang-2024)

## Evidence

### Chieh-Yang Huang 2024

Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)

`q2 · i?` · `design · r2`

Manual quality inspection of 10 articles from the test set, reviewing generated texts for concerns if used as learning materials; the review of 30 generated articles noticed several modifications to quotations, which the authors call not ideal.

> "Our analysis revealed a few issues: (i) the potential for introducing misinformation, particularly in the form of altered quotations and factual inaccuracies, and (ii) the inconsistent distribution of edits within the text, leading to an uneven readability level throughout the article."

## Discussion


## Related Claims
- [Large language models can produce fluent but factually inaccurate or fabricated outputs (AI hallucination), posing risks for uncritical users in science education](llm-hallucination-risk-science-education.md) — a broader claim this one bears on
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — a broader claim this one bears on
- [AI-assisted scientific writing assignments risk fabricated references and altered chemical meaning](genai-writing-fabricated-references.md) — a broader claim this one bears on
