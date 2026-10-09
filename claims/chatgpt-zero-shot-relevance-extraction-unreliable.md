---
type: claim
title: ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality
description: ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality
id: chatgpt-zero-shot-relevance-extraction-unreliable
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: paiheng-xu-2024
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Preliminary analysis shows the relevant utterances retrieved by ChatGPT as a zero-shot summarization model are not helpful; it falsely identified leading questions as relevant to REMED regardless of whether they addressed student errors at a conceptual level. [→ Paiheng Xu 2024](#paiheng-xu-2024)

## Evidence

### Paiheng Xu 2024

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q1 · i?` · `design · r2`

Preliminary zero-shot analysis using ChatGPT as the first-stage summarization/relevance model. The authors report ChatGPT overestimated the mathematical instruction quality of utterances and failed to make inferences based on the level of pedagogical expertise required, consistent with Wang and Demszky (2023); poor results and high cost warranted no further large-scale experiments.

> "our preliminary analysis shows that the relevant utterances retrieved by ChatGPT are not helpful."

## Discussion


## Related Claims
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — a broader claim this one bears on
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences](two-stage-relevance-strategy-helps-multi-sentence-variables.md) — related
- [ChatGPT's exam scores were within 10% of human grades 70% of the time in a study of AI-based grading](chatgpt-grading-within-10-percent-human.md) — related
