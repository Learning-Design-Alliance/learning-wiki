---
type: strategy
id: mid-quality-few-shot-examples-to-reduce-degradation
title: Reduce mid-range degradation by including more mid-quality examples in few-shot prompts and developing locally validated task-specific prompts
description: "The article's future-work agenda proposes testing \"whether including more mid-quality examples in few-shot prompts can reduce the observed degradation in scoring\", developing task-specific prompts as a human-in-the-lo..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: abigail-victoria-gurin-schleifer-2026
    resource: "https://arxiv.org/abs/2605.07647"
    title: "Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647"
    author: Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron
---

# Reduce mid-range degradation by including more mid-quality examples in few-shot prompts and developing locally validated task-specific prompts

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's future-work agenda proposes testing "whether including more mid-quality examples in few-shot prompts can reduce the observed degradation in scoring", developing task-specific prompts as a human-in-the-loop approach, and extending the research to additional instruments, domains, and the direction of misalignment. Prior work suggests LLMs may tend to over-score incorrect responses, motivating direction-of-error analysis.

## Design Implications

### Context
#### Requirements
- domain experts or teachers trained to develop and validate task-specific prompts within their local context
#### Constraints
- the study's prompts were originally designed and validated for GPT-4o, so model-tailored or alternative prompting strategies could yield different performance patterns

### Target Learners
- high-school biology students
- teachers and domain experts developing scoring prompts

### Target Learning Goals
- improved AI-human agreement on partially correct responses
- locally validated task-specific scoring prompts

## Related Strategies
- 

## Examples
-

## Key Sources
- Abigail Victoria Gurin Schleifer, Moriah Ariely, Beata Beigman Klebanov, Asaf Salman, Giora Alexandron. (2026). Quality-Conditioned Agreement in Automated Short Answer Scoring: Mid-Range Degradation and the Impact of Task-Specific Adaptation. arXiv. https://arxiv.org/abs/2605.07647
