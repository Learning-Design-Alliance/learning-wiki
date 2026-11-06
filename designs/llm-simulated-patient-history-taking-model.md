---
type: design
id: llm-simulated-patient-history-taking-model
title: LLM-configured simulated patient as a scalable, standardized practice environment for history taking
description: "The article configures a large language model (ChatGPT-5.2, temperature 0.7, top-p 0.9, not fine-tuned) with preloaded gynecological case scripts to \"behave as a real patient using predefined gynecological cases\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: gao-lingling-2026
    resource: "https://doi.org/10.1186/s12909-026-09219-2"
    title: "Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan. (2026). Utilizing generative artificial intelligence to create simulated patient for history taking in gynecology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09219-2"
    author: Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan
---

# LLM-configured simulated patient as a scalable, standardized practice environment for history taking

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article configures a large language model (ChatGPT-5.2, temperature 0.7, top-p 0.9, not fine-tuned) with preloaded gynecological case scripts to "behave as a real patient using predefined gynecological cases". Behavioral constraints restrict it from giving medical advice, require lay language, and withhold diagnostic clues unless elicited. Students interview it via text in 15–30 minute self-paced sessions without faculty supervision, positioning it as a scalable, 24/7-accessible adjunct to standardized patients.

## Design Implications

### Context
#### Requirements
- Preloaded standardized case scripts with chief complaint, history of present illness, past medical history, personal history, and family history
- Structured prompt controls and predefined technical parameters for reproducibility
#### Constraints
- Knowledge cutoff constraints and absence of non-verbal clinical cues
- AI output was not monitored in real time during student encounters

### Target Learners
- fourth-year medical students in a gynecology clerkship

### Learning Goals
- gynecological history-taking skills
- systematic clinical information gathering

### Claims
- [Ai Simulated Patient Checklist Completion Gynecology](../claims/ai-simulated-patient-checklist-completion-gynecology.md) [+M]
- [Ai Simulated Patient Osce Scores Gynecology](../claims/ai-simulated-patient-osce-scores-gynecology.md) [+M]

## Related Designs

- [Three-component prompt construction framework for LLM-driven virtual simulated patients](vsp-prompt-three-component-framework.md)

## Examples
-

## Key Sources
- Gao Lingling, Zhang Li, Zhang Yanxin, Wu Min, Xu Jianbo, Lu Dan. (2026). Utilizing generative artificial intelligence to create simulated patient for history taking in gynecology. BMC Medical Education. https://doi.org/10.1186/s12909-026-09219-2
