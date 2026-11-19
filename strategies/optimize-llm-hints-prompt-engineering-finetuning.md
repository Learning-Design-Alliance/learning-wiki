---
type: strategy
id: optimize-llm-hints-prompt-engineering-finetuning
title: Optimize LLM hint quality through prompt engineering, model fine-tuning, and correlation mining of hint properties
description: Because a share of students found the hints unhelpful, the authors recommend improving hint generation before wider deployment.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: maciej-pankiewicz-ryan-s-baker-2023
    resource: "https://arxiv.org/abs/2307.00150"
    title: "Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. https://arxiv.org/abs/2307.00150"
    author: "Maciej Pankiewicz & Ryan S. Baker"
---

# Optimize LLM hint quality through prompt engineering, model fine-tuning, and correlation mining of hint properties

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Because a share of students found the hints unhelpful, the authors recommend improving hint generation before wider deployment. They propose "more experimentation with prompt generation (prompt engineering), fine-tuning the GPT model (by providing examples on which the model can improve) or conducting correlation mining to identify the properties associated with less useful hints". The stated goal is to increase the proportion of useful hints and the degree to which each hint is useful, ultimately improving student performance.

## Design Implications

### Context
#### Requirements
- Access to hint-usefulness rating data to identify the properties of less useful hints
- Capacity to iterate on prompt generation or to fine-tune the GPT model with example data
#### Constraints
- The study's hints were generated only in Polish, and the authors call for experiments in other languages
- The study used a single programming language (C#) and a 9-week window within a 15-week term, which the authors flag as limits on generalizability

### Target Learners
- university students in introductory object-oriented programming courses

### Target Learning Goals
- improving the usefulness of automated feedback hints for programming assignments

## Claims

- [University students rated GPT-generated programming hints positively, though a minority found them not useful](../claims/gpt-hints-rated-useful-programming.md) [+W]

## Related Strategies

- [Achieve high-precision automated constructive assessment through prompt design alone—explicit role assignment plus human-scored hint examples—without fine-tuning](prompt-design-with-role-and-hints-for-llm-assessment.md)
- [Train medical educators in prompt engineering, using specific, contextualized prompts to improve LLM-generated MCQ quality](prompt-engineering-training-for-mcq-generation.md)
- [Apply error mitigation such as self-consistency before deploying LLM-generated help, and frame unmitigated LLM feedback as an imperfect source](mitigate-llm-hint-errors-before-deployment.md)
- [Use detailed, comprehensive system prompts and patient-like prompt language to optimize LLM virtual patient performance](detailed-system-prompts-optimize-llm-virtual-patients.md)

## Examples
-

## Key Sources
- Maciej Pankiewicz & Ryan S. Baker. (2023). Large Language Models (GPT) for automating feedback on programming assignments. Proceedings of the 31st International Conference on Computers in Education. https://arxiv.org/abs/2307.00150
