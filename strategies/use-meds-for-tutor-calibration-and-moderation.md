---
type: strategy
id: use-meds-for-tutor-calibration-and-moderation
title: Use MEDS as baseline data for fine-tuning and moderation of AI mathematics tutoring content
description: The article recommends concrete downstream uses of MEDS for safer AI mathematics tutors.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: esposito-2026
    resource: "https://arxiv.org/abs/2604.27618"
    title: "Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M. (2026). Math Education Digital Shadows for Investigating Learning with GenAI: Mathematics Performance, Anxiety, and Confidence in LLMs. arXiv preprint. https://arxiv.org/abs/2604.27618"
    author: "Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M"
---

# Use MEDS as baseline data for fine-tuning and moderation of AI mathematics tutoring content

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends concrete downstream uses of MEDS for safer AI mathematics tutors. It states that text from Tasks 1 and 4 "can serve as training data for classifiers that detect signals of mathematics anxiety in AI-generated educational content," and that the dataset "could also serve as baseline data for preference fine-tuning of LLMs towards mathematical explanations that express less anxiety and are better calibrated." Its psychometric distributions, semantic valences, and confidence–accuracy gaps can serve as baselines for other synthetic-participant datasets.

## Design Implications

### Context
#### Requirements
- Access to the publicly released JSON records on GitHub and comparable prompting conditions across models
#### Constraints
- The article notes MEDS is not a replacement for real data and is not statistically representative of any specific country

### Target Learners
- developers of AI tutoring platforms
- learning scientists

### Target Learning Goals
- detecting mathematics anxiety in AI-generated content
- improving confidence calibration of LLM tutors

### Affordances
- [Digital Shadowing Llm Behaviour Framework](../research-methods/digital-shadowing-as-a-framework-for-recording-llm-behaviour-under-controlled-conditions.md)

## Related Strategies

- [Use synthetic LLM-generated error datasets for AI tutors, teachable agents, and teacher professional development](synthetic-error-datasets-for-tutors-teachable-agents-teacher-pd.md)

## Examples
-

## Key Sources
- Esposito, N., Tricarico, A., Porzio, L., Aghazadeh Ardebili, A., & Stella, M. (2026). Math Education Digital Shadows for Investigating Learning with GenAI: Mathematics Performance, Anxiety, and Confidence in LLMs. arXiv preprint. https://arxiv.org/abs/2604.27618. [doi:10.48550/arxiv.2604.27618](https://doi.org/10.48550/arxiv.2604.27618)
