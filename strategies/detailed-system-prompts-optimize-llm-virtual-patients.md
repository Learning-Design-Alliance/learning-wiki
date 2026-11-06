---
type: strategy
id: detailed-system-prompts-optimize-llm-virtual-patients
title: Use detailed, comprehensive system prompts and patient-like prompt language to optimize LLM virtual patient performance
description: "In the Future Directions section the author recommends refinements informed by the study's limitations: \"performance might be improved if the system prompt is more detailed and comprehensive, reducing the demand on in..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: bahammam-fahad-bds-2026
    resource: "https://doi.org/10.2196/91021"
    title: "BaHammam Fahad BDS, MClinDent, PhD. (2026). Feasibility of Large Language Model–Based Standardized Virtual Patients to Support Clinical Decision-Making Training in Operative Dentistry: Mixed Methods Study. JMIR Formative Research. https://doi.org/10.2196/91021"
    author: BaHammam Fahad BDS, MClinDent, PhD
---

# Use detailed, comprehensive system prompts and patient-like prompt language to optimize LLM virtual patient performance

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 design, 1 theoretical), `q1`–`q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
In the Future Directions section the author recommends refinements informed by the study's limitations: "performance might be improved if the system prompt is more detailed and comprehensive, reducing the demand on inferential reasoning", and prompts should "adopt language that matches how real patients communicate" to improve Humanlike ratings. For limitations not addressable through prompting, the author suggests a 2-stage cascaded architecture with a gatekeeper, fine-tuning on real doctor-patient interactions, and adding voice and visual capabilities.

## Design Implications

### Context
#### Requirements
- Detailed and comprehensive system prompts covering likely question topics
#### Constraints
- Some alignment-driven limitations may not be fully addressable through system prompting

### Target Learners
- undergraduate dental students

### Target Learning Goals
- clinical decision-making
- history-taking

## Claims

- [Iterative prompt refinement and expert pilot-testing may partly explain favorable LLM virtual patient output quality](../claims/iterative-prompt-refinement-expert-testing-improves-output.md) [+W]
- [Optimizing prompts can vastly improve the accuracy of LLM outputs, but critical evaluation of the resulting outputs still requires domain expertise.](../claims/prompt-optimization-improves-accuracy-expertise-still-needed.md) [+W]

## Related Strategies

- [Development strategies targeting AI virtual patient limitations: expert-reviewed content, iterative prompt engineering, behavioral rules, few-shot prompting, and conversational memory](ai-virtual-patient-mitigation-strategies.md)
- [Use detailed, structured prompts specifying question type, case details, distractors, explanation, source, and difficulty level](structured-nine-component-mcq-prompt.md)

## Examples
-

## Key Sources
- BaHammam Fahad BDS, MClinDent, PhD. (2026). Feasibility of Large Language Model–Based Standardized Virtual Patients to Support Clinical Decision-Making Training in Operative Dentistry: Mixed Methods Study. JMIR Formative Research. https://doi.org/10.2196/91021
