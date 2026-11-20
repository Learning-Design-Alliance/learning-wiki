---
type: claim
title: LLaMA-2 70B performs best at adjusting readability while GPT-3.5 best preserves content and meaning
description: LLaMA-2 70B performs best at adjusting readability while GPT-3.5 best preserves content and meaning
id: llama2-readability-vs-gpt35-meaning-preservation
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

# LLaMA-2 70B performs best at adjusting readability while GPT-3.5 best preserves content and meaning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among the three tested LLMs, LLaMA-2 70B performs best in adjusting readability, whereas GPT-3.5 demonstrates superior performance in preserving content and meaning. [→ Chieh-Yang Huang 2024](#chieh-yang-huang-2024)

## Evidence

### Chieh-Yang Huang 2024

Chieh-Yang Huang, Jing Wei, and Ting-Hao Kenneth Huang. (2024). Generating Educational Materials with Different Levels of Readability using LLMs. In2Writing 2024. [doi:10.1145/3690712.3690718](https://doi.org/10.1145/3690712.3690718)

`q2 · i?` · `design · r2`

Benchmark comparison across GPT-3.5, LLaMA-2 70B, and Mixtral 8x7B on 100 test samples, where "LLaMA-2 70B performs best in adjusting readability" (lowest MAE = 172.9; highest match rate = 22.22%) while GPT-3.5 leads on BERTScore and semantic similarity.

> "When comparing different LLMs, we found that LLaMA-2 70B performs best in adjusting readability, whereas GPT-3.5 demonstrates superior performance in preserving content and meaning."

## Discussion


## Related Claims
- [Few-shot prompting significantly improves LLM performance in both readability manipulation and information preservation for leveled-text generation](few-shot-prompting-improves-leveled-text-generation.md) — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
- [GPT-4 improves gaze and question-answering simulation relative to GPT-3.5, while Gemini Pro and Llama 2 70B drop on those measures](foundation-model-comparison-student-simulation.md) — related
