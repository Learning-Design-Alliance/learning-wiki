---
type: strategy
id: four-component-dialogue-analysis-method
title: "Four-component dialogue analysis method: data collection, dialogue act annotation, CM-SPAM pattern mining, and predictive model building"
description: "The proposed solution employs a dialogue analysis approach with four key components: dialogue data collection via an API-connected platform; dialogue act annotation using an adapted coding scheme based on SETT, SEDA a..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: liqun-he-2024
    resource: "https://arxiv.org/abs/2510.17698"
    title: "Liqun He, Manolis Mavrikis, Mutlu Cukurova. (2024). Towards Mining Effective Pedagogical Strategies from Learner–LLM Educational Dialogues. AIED Doctoral Consortium paper, University College London. https://arxiv.org/abs/2510.17698"
    author: Liqun He, Manolis Mavrikis, Mutlu Cukurova
---

# Four-component dialogue analysis method: data collection, dialogue act annotation, CM-SPAM pattern mining, and predictive model building

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The proposed solution employs a dialogue analysis approach with four key components: dialogue data collection via an API-connected platform; dialogue act annotation using an adapted coding scheme based on SETT, SEDA and T-SEDA; DA pattern mining with the CM-SPAM algorithm; and predictive model building. The authors plan decision tree classifiers following prior tutoring work, or Bayesian Networks, because "such models provide interpretable insights, enabling systematic assessment and targeted improvement of educational LLM systems".

## Design Implications

### Context
#### Requirements
- A coding scheme tailored to the learning context; annotated dialogue turns as input to sequential pattern mining; identified dialogue patterns as indicators of pedagogical strategies for model training
#### Constraints
- Currently in pilot phase with only three high-progress and three low-progress students; predictive model building is a planned next step, not yet completed

### Target Learners
- English language learners interacting with an LLM voice chatbot for speaking practice

### Target Learning Goals
- Identifying effective and less effective pedagogical strategies from learner–LLM dialogues

### Affordances
- [Speech Act Theory Dialogue Act Framework](../research-methods/dialogue-act-coding-dac-system.md)

## Claims

- [In the pilot data, high-progress and low-progress students had similar numbers of dialogue turns per session, but high-progress students produced longer utterances (15.3 vs 11.5 words per turn)](../claims/hp-longer-utterances-similar-turn-counts.md) [+W]

## Related Strategies

- [Three-stage hybrid workflow: API batch review, identification of doubtful cases, focused conversational teacher review](three-stage-hybrid-ai-assessment-workflow.md)

## Examples
-

## Key Sources
- Liqun He, Manolis Mavrikis, Mutlu Cukurova. (2024). Towards Mining Effective Pedagogical Strategies from Learner–LLM Educational Dialogues. AIED Doctoral Consortium paper, University College London. https://arxiv.org/abs/2510.17698
