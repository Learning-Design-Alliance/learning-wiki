---
type: claim
title: "Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification"
description: "Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification"
id: zero-shot-llm-granularity-competency-classification
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
    kind: design
    rigour: 2
  - id: zhen-xu-2026-2
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In the five-class setting all zero-shot models perform only marginally above random, indicating shared difficulty with fine-grained competency distinctions. [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` On binary classification all four models achieve accuracies above 70%, with GPT-4o highest at 72.9%. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `design · r2`

Zero-shot benchmark evaluation of four LLMs (GPT-3.5-turbo, GPT-4o, Llama-3-70B, Llama-3-8B) on the 7,600-pair annotated benchmark; the article states models "perform only marginally above random" at five-class granularity.

> "Despite these differences, LLMs overall exhibit limited effectiveness in fine-grained competency analysis compared to humans. In the five-class setting, all models perform only marginally above random, suggesting a shared difficulty in distinguishing among different levels of competency coverage."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `design · r2`

Same zero-shot benchmark at binary granularity: the article prints accuracies of "GPT-3.5-turbo: 72.4%; GPT-4o: 72.9%; Llama3-70B: 71.5%; Llama3-8B: 72.4%".

> "When reduced to a binary classification task, as shown in Table 5, all models achieve accuracies above 70% (GPT-3.5-turbo: 72.4%; GPT-4o: 72.9%; Llama3-70B: 71.5%; Llama3-8B: 72.4%)."

## Discussion


## Related Claims
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
