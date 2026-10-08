---
type: element
id: curriculum-competency-benchmark-7600-pairs
title: Benchmark dataset of 7,600 human-annotated curriculum-competency alignment scores
description: A benchmark dataset produced by two graduate annotators in education who scored 200 course documents sampled from five curriculum document types (concise course description, detailed course description, learning objec...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: zhen-xu-2026
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
---

# Benchmark dataset of 7,600 human-annotated curriculum-competency alignment scores

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A benchmark dataset produced by two graduate annotators in education who scored 200 course documents sampled from five curriculum document types (concise course description, detailed course description, learning objective, instructional schedule, learning activity content) against three competency frameworks (O*NET, EU Key Competences, ESDC). The article reports it "resulting in 7,600 pairs of curriculum-competency alignment scores" on a 0–3/NA rubric. Inter-rater reliability after guideline refinement reached κ = 0.94 (O*NET) and κ = 0.92 (ESDC).

## Design Implications

### Context
#### Requirements
- Trained annotators with curriculum and instructional design expertise
- A calibration round and refined coding guidelines distinguishing clearly irrelevant (0) from insufficient information (NA)
#### Constraints
- Reliability was initially low for the O*NET (κ = 0.288) and ESDC (κ = 0.168) frameworks before guideline refinement

### Target Learners
- Postsecondary education institutions and researchers conducting curricular analytics

### Target Learning Goals
- Assessing the integration of 21st-century competencies in course design

## Claims

- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](../claims/curricular-cot-improves-accuracy-larger-models.md) [+M]
- [Instructional schedules are the least informative curriculum document type for 21st-century competency analytics, while detailed learning activity content is the most informative](../claims/instructional-schedules-least-informative-competency-analytics.md) [+M]
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](../claims/llm-accuracy-regression-overestimation-bias.md) [+M]
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](../claims/llm-competency-error-patterns-four-types.md) [+M]
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](../claims/zero-shot-llm-granularity-competency-classification.md) [+M]

## Related Elements
- 

## Examples
-

## Key Sources
- Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127
