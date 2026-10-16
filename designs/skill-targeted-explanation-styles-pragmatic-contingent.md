---
type: design
id: skill-targeted-explanation-styles-pragmatic-contingent
title: "Skill-targeted explanation styles: pragmatic versus contingent LLM error-message rewrites"
description: The article defines two skill-targeted explanation styles for LLM rewrites of Python error messages, designed for different assessed proficiency levels.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: alexandru-radu-moraru-2026
    resource: "https://arxiv.org/abs/2608.20896"
    title: "Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896"
    author: Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju
---

# Skill-targeted explanation styles: pragmatic versus contingent LLM error-message rewrites

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article defines two skill-targeted explanation styles for LLM rewrites of Python error messages, designed for different assessed proficiency levels. As the article states, "Pragmatic messages are concise and task-oriented: they name the error, localize the likely cause, and provide a short hint toward repair", while contingent messages "provide more scaffolded guidance" including context about likely intent, possible misconception, and reasoning path. The styles are informed by actionable-feedback work, Bloom's taxonomy, claim-evidence-reasoning, and Toulmin's model, and were evaluated against standard interpreter messages in a controlled crowdsourced experiment.

## Design Implications

### Context
#### Requirements
- LLM-generated rewrites require the code snippet, the standard interpreter message, and line-numbered context in the prompt
#### Constraints
- The system does not dynamically adapt during interaction; the authors explicitly do not claim dynamic adaptation, only styles designed for different assessed proficiency levels

### Target Learners
- novice and more experienced Python programmers in crowdsourced debugging tasks

### Learning Goals
- interpreting programming error messages and repairing buggy code

### Claims
- [Llm Error Rewrites Subjective Not Objective Gains](../claims/llm-error-rewrites-subjective-not-objective-gains.md) [+M]
- [Llm Rewrites Lower Perceived Cognitive Load](../claims/llm-rewrites-lower-perceived-cognitive-load.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju. (2026). Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors. https://arxiv.org/abs/2608.20896
