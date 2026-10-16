---
type: design
id: crewscaler-16-protocol-ai-tutor-library
title: CrewScaler 16-protocol AI-tutor coaching library
description: "The framework specifies the AI tutor's pedagogy in advance as a library of 16 named protocols drawn from the retrieval-practice, productive-failure, and affect literatures, rather than a single general-purpose prompt."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: tam-nguyen-2026
    resource: "https://arxiv.org/abs/2607.14044"
    title: "Tam Nguyen, Hung Nguyen, Robert Ogburn. (2026). AI-accelerated End-to-End Framework for Rapid Professional Upskilling. https://arxiv.org/abs/2607.14044"
    author: Tam Nguyen, Hung Nguyen, Robert Ogburn
---

# CrewScaler 16-protocol AI-tutor coaching library

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The framework specifies the AI tutor's pedagogy in advance as a library of 16 named protocols drawn from the retrieval-practice, productive-failure, and affect literatures, rather than a single general-purpose prompt. Protocols include direct explanation, Socratic questioning, worked examples, hint escalation, spaced retrieval, productive failure, and "affective support that prioritizes boredom over frustration". A selection layer picks the active protocol each turn by fixed priority: integrity risk first, then affective signals, then group context, then learner intent. Six cross-cutting principles constrain every protocol.

## Design Implications

### Context
#### Requirements
- A selection layer that prioritizes integrity risk, affective signals, group context, and learner intent
- Grounded RAG and academic-integrity guardrails as stated quality controls
#### Constraints
- The article cites evidence that current LLMs labeled incorrect learner actions no better than chance in a 223-domain testbed, motivating explicit protocol design

### Target Learners
- Adult professionals in frontier technical upskilling programs

### Learning Goals
- Reducing time-to-competency through protocolized one-to-one tutoring

### Claims

- [Prompt specificity changes AI tutor pedagogy: a no-direct-answer guardrail alone produces uniform questioning, while a detailed guided protocol produces varied, impasse-sensitive responses](../claims/prompt-specificity-shapes-tutor-pedagogy.md) [+W]

## Related Designs

- [Retrieval-augmented Conversational AI Tutor with modular GROW-aligned coaching routines](rag-conversational-ai-tutor-modular-coaching-routines.md)
- [CrewScaler: an end-to-end five-stage AI-accelerated upskilling pipeline](crewscaler-five-stage-ai-upskilling-pipeline.md)

## Examples
-

## Key Sources
- Tam Nguyen, Hung Nguyen, Robert Ogburn. (2026). AI-accelerated End-to-End Framework for Rapid Professional Upskilling. https://arxiv.org/abs/2607.14044
