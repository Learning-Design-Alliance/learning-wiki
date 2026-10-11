---
type: strategy
id: teacher-in-the-loop-diagnostic-verification
title: Use teacher-in-the-loop verification targeted at each error stage rather than fully automated LLM diagnosis
description: "The article recommends moving \"beyond fully automated diagnosis toward transparency and selective human verification.\" Teachers intervene at specific pipeline stages: validating whether identified evidence is actually..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: yoonsu-kim-2026
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
---

# Use teacher-in-the-loop verification targeted at each error stage rather than fully automated LLM diagnosis

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends moving "beyond fully automated diagnosis toward transparency and selective human verification." Teachers intervene at specific pipeline stages: validating whether identified evidence is actually present, checking model interpretations against diagnostic criteria, scrutinizing whether inferred skills are supported by observable evidence, and overseeing coherence between intermediate reasoning and final judgments. This targets the five recurring error types the analysis identified.

## Design Implications

### Context
#### Requirements
- Teachers available to validate identified evidence, check rubric interpretation, scrutinize over-inference, and oversee consistency between reasoning and final verdicts
#### Constraints
- The article states current LLMs are not yet reliable for cognitive skill diagnosis without intermediate verification, as errors cascade throughout the diagnostic pipeline

### Target Learners
- middle school math students

### Target Learning Goals
- diagnosis of students' cognitive skills (knowing and applying) in mathematics from handwritten work

## Related Strategies
- 

## Examples
-

## Key Sources
- Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843
