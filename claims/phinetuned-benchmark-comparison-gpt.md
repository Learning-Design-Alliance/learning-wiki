---
type: claim
title: On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation
description: On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation
id: phinetuned-benchmark-comparison-gpt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: tozadore-2025
    resource: "https://doi.org/10.48550/arxiv.2508.16706"
    title: "Tozadore, D., Ertug, N., Chaker, Y., & Abderrahim, M. (2025). RoboBuddy in the Classroom: Exploring LLM-Powered Social Robots for Storytelling in Learning and Integration Activities. https://arxiv.org/abs/2508.16706 [doi:10.48550/arxiv.2508.16706](https://doi.org/10.48550/arxiv.2508.16706)"
    author: "Tozadore, D., Ertug, N., Chaker, Y., & Abderrahim, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On benchmarks, GPT-3.5-turbo outperformed the fine-tuned Phi model in knowledge and story completion, while PhinetunEd scored best in story generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The GPT model performed better in knowledge (MMLU 70% vs 62% base, 60% PhinetunEd) and story completion (Hellaswag 85.5% vs 59%/58%), whereas the fine-tuned model scored best in story generation (7.46 vs 7.05 and 6.87). [→ Tozadore 2025](#tozadore-2025)

## Evidence

### Tozadore 2025

Tozadore, D., Ertug, N., Chaker, Y., & Abderrahim, M. (2025). RoboBuddy in the Classroom: Exploring LLM-Powered Social Robots for Storytelling in Learning and Integration Activities. https://arxiv.org/abs/2508.16706 [doi:10.48550/arxiv.2508.16706](https://doi.org/10.48550/arxiv.2508.16706)

`q2 · i?` · `design · r2`

Model evaluation reported in Table I: MMLU, Hellaswag, and GPT-4-turbo-judged story generation on 200 WritingPrompts prompts rated 1–10. Printed scores: GPT-3.5-turbo 70%/85.5%/6.87; Phi-3 base 62%/59%/7.05; PhinetunEd 60%/58%/7.46. The comparison names GPT-3.5-turbo and PhinetunEd as the two sides.

> "The benchmark evaluation showed that the GPT model performs better in knowledge, reasoning, and story completion, whereas our finetuned models score best in story generation."

## Discussion


## Related Claims
- [A LoRA-adapted open-weight Gemma-3-27B model fine-tuned on 120 essays outperforms a fine-tuned GPT-3.5 baseline on TOEFL essay scoring across all reported metrics](gemma-27b-lora-beats-gpt35-essay-scoring.md) — related
- [The OpenAI gpt-4o reference model outperformed all quantised models on human-rated coherence, fluency, relevance and cultural appropriateness, serving as an upper benchmark](gpt-4o-reference-outperformed-quantised-models-human-ratings.md) — related
- On question answering and commonsense reasoning the model outperforms previous best results by up to 8.9% on Story Cloze and 5.7% overall on RACE — related
- [No significant differences emerged between GPT-3.5 Turbo and Claude 3 Opus on affective, collaborative, or performance measures](no-difference-gpt35-turbo-claude3-opus.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
