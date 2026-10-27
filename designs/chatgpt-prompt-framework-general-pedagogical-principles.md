---
type: design
id: chatgpt-prompt-framework-general-pedagogical-principles
title: A dual-focus framework for preparing ChatGPT prompts for training, distinguishing general LLM prompting principles from application-specific pedagogical principles
description: "The article introduces a framework for structuring ChatGPT prompts used as training tools, built on \"a dual focus, incorporating general LLM prompting principles, which apply universally across multiple contexts, and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: murtaza-2024
    resource: "https://doi.org/10.1007/s40593-024-00407-z"
    title: "Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J. (2024). Transforming Driver Education: A Comparative Analysis of LLM-Augmented Training and Conventional Instruction for Autonomous Vehicle Technologies. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00407-z"
    author: "Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J"
---

# A dual-focus framework for preparing ChatGPT prompts for training, distinguishing general LLM prompting principles from application-specific pedagogical principles

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article introduces a framework for structuring ChatGPT prompts used as training tools, built on "a dual focus, incorporating general LLM prompting principles, which apply universally across multiple contexts, and application-specific (pedagogical) principles tailored to particular training scenarios". The general principles cover goal and scene setting, structured instruction, and regular reiteration of objectives to counter token-limit context loss. The pedagogical principles cover personalised responses, proactive knowledge checking via follow-up questions, and phrasing of output format such as bullet points. The framework was demonstrated by equipping ChatGPT with an AV user manual for conversation-based driver training.

## Design Implications

### Context
#### Requirements
- ChatGPT must be instructed to base responses solely on the provided training material and not draw from external knowledge sources, to avoid inconsistent or invented information
#### Constraints
- The article notes the brief ~1100-word manual "does not adequately represent the complexities of processing larger documents", which could challenge ChatGPT's token capacity and increase the risk of inaccurate or invented information

### Target Learners
- adult licensed drivers learning ADAS and AV functions

### Learning Goals
- accurate operation of advanced driver assistance functions
- formation of accurate mental models of complex systems

### Claims
- [Chatgpt Training Higher Adas Accuracy Than Conventional](../claims/chatgpt-training-higher-adas-accuracy-than-conventional.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J. (2024). Transforming Driver Education: A Comparative Analysis of LLM-Augmented Training and Conventional Instruction for Autonomous Vehicle Technologies. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00407-z
