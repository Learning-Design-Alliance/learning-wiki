---
type: claim
title: Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance
description: Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance
id: curricular-cot-improves-accuracy-larger-models
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: zhen-xu-2026
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zhen-xu-2026-2
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Curricular CoT improves prediction accuracy over the zero-shot baseline across all granularity levels, more apparently in GPT-4o and Llama3-70B. [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` The definition-based (DEF) strategy does not improve performance and can even reduce accuracy. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Experiment comparing five prompting strategies (DEF, CQA, CQ, QA, A) against the zero-shot baseline across four models and four granularity levels; the article describes the gains as modest but consistent, particularly in binary tasks.

> "Overall, we find that curricular CoT improves prediction accuracy over the zero-shot baseline across all levels of task granularity. However, these improvements are more apparent in larger and more advanced models, such as GPT-4o and Llama3-70B."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Same prompting-strategy comparison: providing competency definitions from human annotator notes failed to help and in some cells lowered accuracy relative to the zero-shot baseline.

> "In contrast, the definition-based (DEF) strategy, which provides the model with human-annotated notes for each competency, does not improve performance and can even reduce accuracy."

## Discussion


## Related Claims
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- [Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing](prompt-dimension-interaction-error-rates.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — related
- [Agentic frameworks built on GPT-3.5 and GPT-4 show significant performance gains on the HumanEval benchmark over zero-shot baselines](agentic-frameworks-humaneval-gains.md) — related
- [Chain-of-thought prompting improved LLM multistep reasoning, operationalized via decomposition and interleaved planning approaches](cot-planning-decomposition-interleaved.md) — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
