---
type: claim
title: Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage
description: Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage
id: llm-accuracy-regression-overestimation-bias
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

# Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Instructional schedules show the largest accuracy decline relative to learning objectives, with reductions from 0.114 (five-class) to 0.216 (binary). [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` Zero-shot LLMs overestimate competency coverage, with positive and statistically significant intercepts across all granularities. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `design · r2`

Regression analyses at course-competency level with binary accuracy and score difference as dependent variables, controlling for word count, model, framework, and subject matter; learning objectives served as the reference category.

> "In contrast, instructional schedules are associated with the largest performance decline, with accuracy reductions ranging from 0.114 in the five-class setting to 0.216 in the binary classification task."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `design · r2`

Score-difference regressions (LLM-predicted minus human-annotated score) show LLMs "generally overestimate the extent to which a course covers a given competency", with the printed intercepts 0.128, 0.019, 0.051, and 0.147.

> "This upward bias is reflected in positive and statistically significant intercepts across all classification granularities (0.128 in the five-class task, 0.019 in the four-class task, 0.051 in the three-class task, and 0.147 in the binary task)."

## Discussion


## Related Claims
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Instructional schedules are the least informative curriculum document type for 21st-century competency analytics, while detailed learning activity content is the most informative](instructional-schedules-least-informative-competency-analytics.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- [ML-based scoring approaches more often overestimated expert-assigned scores, whereas LLM-based approaches more often underestimated them](ml-overestimates-llm-underestimates-pattern.md) — related
