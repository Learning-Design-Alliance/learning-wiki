---
type: strategy
id: curricular-chain-of-thought-prompting
title: "Curricular chain-of-thought prompting: extract key pedagogical elements before competency inference"
description: A reasoning-based prompting strategy in which the LLM first extracts key pedagogical components using guided questions grounded in curriculum design theory, then synthesizes them into a standardized structured summary...
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

# Curricular chain-of-thought prompting: extract key pedagogical elements before competency inference

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
A reasoning-based prompting strategy in which the LLM first extracts key pedagogical components using guided questions grounded in curriculum design theory, then synthesizes them into a standardized structured summary used for the final competency evaluation. The article states "The model follows a two-step reasoning process" of element extraction and standardized content representation, mitigating heterogeneous document granularity, inconsistent wording, and long or variable input length. Four variants (CQA, CQ, QA, A) vary what the model receives alongside the guided questions.

## Design Implications

### Context
#### Requirements
- Guided questions tailored to the curriculum document type (course description, learning objectives, or learning activities)
- Sufficient model capability: intermediate summaries from weaker models (e.g., GPT-3.5-turbo hallucinating unsupported elements) can degrade downstream performance
#### Constraints
- Gains are modest and more apparent in larger, more advanced models; summary quality varies across models and errors in summarization can degrade downstream performance

### Target Learners
- Postsecondary institutions using LLMs for curricular analytics

### Target Learning Goals
- Reliable inference of 21st-century competency coverage from curriculum documents

## Related Strategies

- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](structured-prompt-framework-inductive-coding.md)

## Examples
-

## Key Sources
- Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127
