---
type: claim
title: "Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response"
description: "Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response"
id: llm-competency-error-patterns-four-types
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
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

# Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Over-interpretation occurred across all models and document types, e.g., defaulting to the assumption that exams are writing-based. [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` Failure to detect relevant information is common in lengthy learning activity content, and hallucination is more common in concise descriptions and instructional schedules. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Manual error analysis of cases where LLM predictions diverged from human annotations; the article identifies over-interpretation as occurring "across all models and all curriculum document types we evaluated".

> "In contrast, LLMs tend to default to the assumption that exams are writing based, leading them to confidently infer writing competencies, which reflects biased reasoning."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Manual error analysis found missed nuanced evidence mainly in long learning activity documents, while hallucination was "more common in concise course descriptions and instructional schedule data"; failure to respond occurred predominantly in smaller models such as Llama3-8B.

> "This error pattern is common in lengthy curriculum document types such as learning activity content, where dense information makes it difficult for LLMs to capture and interpret key details accurately."

## Discussion


## Related Claims
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- [LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers](llm-inductive-coding-risks-require-human-oversight.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — a narrower finding that bears on this claim
