---
type: claim
title: Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation
description: Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation
id: few-shot-prompting-improves-leveled-text-generation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
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

# Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Providing a few in-context examples significantly improves both manipulating content readability and preserving the same information compared with zero-shot prompting. [→ Chieh-Yang Huang 2024](#chieh-yang-huang-2024)

## Evidence

### Chieh-Yang Huang 2024

Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)

`q2 · i?` · `design · r2`

Benchmark evaluation of 100 processed educational materials from the test set, comparing zero-shot and few-shot prompting of GPT-3.5, LLaMA-2 70B, and Mixtral 8x7B on Lexile accuracy and content-preservation metrics. The article reports that "few-shot learning outperforms zero-shot learning" with no printed effect size.

> "Our findings suggest that providing a few examples significantly improves performance, as few-shot learning outperforms zero-shot learning."

## Discussion


## Related Claims
- [The tested LLMs tend to produce shorter texts than the originals regardless of whether the intent is to simplify or complexify](llm-length-bias-shorter-texts.md) — related
- [LLaMA-2 70B performs best at adjusting readability while GPT-3.5 best preserves content and meaning](llama2-readability-vs-gpt35-meaning-preservation.md) — related
- [Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models](prompting-strategies-limited-alignment-gain.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [LLM-generated leveled texts skew more complex than the intended Lexile level regardless of model or prompting approach](generated-texts-skew-more-complex-than-intended.md) — related
