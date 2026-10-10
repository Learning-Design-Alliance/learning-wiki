---
type: strategy
id: adaptive-strategy-prompt-injection-rules
title: Profile-driven adaptive strategy rules composed dynamically and injected into the system prompt each turn
description: The adaptive strategy engine generates a natural-language instruction block appended to the system prompt, telling the LLM how to adjust pedagogical behavior based on the current profile.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: yizhou-zhou-2026
    resource: "https://arxiv.org/abs/2605.08040"
    title: "Yizhou Zhou, Jiayin Li, and Zhi Zhang. (2026). ECNUClaw: A Learner-Profiled Intelligent Study Companion Framework for K-12 Personalized Education. arXiv preprint. https://arxiv.org/abs/2605.08040"
    author: Yizhou Zhou, Jiayin Li, and Zhi Zhang
---

# Profile-driven adaptive strategy rules composed dynamically and injected into the system prompt each turn

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The adaptive strategy engine generates a natural-language instruction block appended to the system prompt, telling the LLM how to adjust pedagogical behavior based on the current profile. The strategy is composed dynamically from conditional rules that can fire simultaneously: low self-efficacy or high frustration increases encouragement and lowers difficulty; high motivation raises challenge; many weak topics trigger foundation building; Bloom's remember level scaffolds toward understand; and a guided strategy preference yields more Socratic questioning. Adaptation happens entirely through prompt engineering, with no model fine-tuning, making the strategy block interpretable and auditable by educators.

## Design Implications

### Context
#### Requirements
- The LLM must accept injected system-prompt instructions; adaptation is composed from Table 3's conditional rules mapping profile signals to strategy responses
#### Constraints
- The LLM may not always follow the injected instructions faithfully, especially under adversarial or unusual inputs; the heuristic rules use fixed increment/decrement steps that the authors describe as coarse

### Target Learners
- K-12 students

### Target Learning Goals
- Real-time adjustment of guidance intensity, encouragement frequency, and Bloom's taxonomy scaffolding

### Affordances
- [Human Ai Collaborative Iq](../theories/sociocultural-theory.md)

## Related Strategies

- [Use a natural-language strategy guideline in the generator prompt so tutoring strategy can be revised without code changes](collearn-natural-language-strategy-guideline.md)
- [Adaptive Learning](adaptive-learning.md)

## Examples
-

## Key Sources
- Yizhou Zhou, Jiayin Li, and Zhi Zhang. (2026). ECNUClaw: A Learner-Profiled Intelligent Study Companion Framework for K-12 Personalized Education. arXiv preprint. https://arxiv.org/abs/2605.08040
