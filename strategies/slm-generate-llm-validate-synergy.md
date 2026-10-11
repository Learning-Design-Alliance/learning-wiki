---
type: strategy
id: slm-generate-llm-validate-synergy
title: Use an SLM for rapid large-scale question generation with an LLM providing validation feedback
description: "The authors recommend exploiting an abundance mindset with small language models: generate many candidate questions cheaply and locally, then validate carefully afterwards, rather than expecting one-shot quality."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: yumou-wei-john-stamper-and
    resource: "https://doi.org/10.1145/3785022.3785100"
    title: "Yumou Wei, John Stamper, and Paulo F. Carvalho. 2026. Generate-Then-Validate: A Novel Question Generation Approach Using Small Language Models. In LAK26: 16th International Learning Analytics and Knowledge Conference (LAK 2026), Bergen, Norway. ACM, New York, NY, USA. https://doi.org/10.1145/3785022.3785100"
---

# Use an SLM for rapid large-scale question generation with an LLM providing validation feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors recommend exploiting an abundance mindset with small language models: generate many candidate questions cheaply and locally, then validate carefully afterwards, rather than expecting one-shot quality. They argue "It is unrealistic to expect an SLM to succeed in one shot, but the law of large numbers will guarantee that good outcomes will emerge from an abundance of trials". For future work they propose a division of labor in which "the SLM performs fast generation and the LLM provides accurate feedback". This strategy suits educational settings with resource, privacy, and cost constraints.

## Design Implications

### Context
#### Requirements
- A pipeline that pairs expansive generation with validation steps (syntactic filtering, answer confidence evaluation, LO alignment check) to prune low-quality candidates
#### Constraints
- The authors frame the SLM-plus-LLM synergy as future work to explore, not as an already-validated configuration

### Target Learners
- educational researchers and practitioners building question banks for mastery-based learning and testing

### Target Learning Goals
- generating high-quality assessment questions aligned to learning objectives at scale

## Related Strategies
- Generate Then Validate Pipeline

## Examples
-

## Key Sources
- Yumou Wei, John Stamper, and Paulo F. Carvalho. 2026. Generate-Then-Validate: A Novel Question Generation Approach Using Small Language Models. In LAK26: 16th International Learning Analytics and Knowledge Conference (LAK 2026), Bergen, Norway. ACM, New York, NY, USA. https://doi.org/10.1145/3785022.3785100
