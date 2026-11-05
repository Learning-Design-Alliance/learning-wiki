---
type: strategy
id: match-query-protocol-to-llm-use-purpose
title: "Match querying protocol to educational purpose: independent querying for raw knowledge checking, sequential querying for exam-like simulation"
description: The article distinguishes two utilization patterns of LLMs in dental education and links each to a querying protocol.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: erdal-selda-gökçe-2026
    resource: "https://doi.org/10.1186/s12909-026-08808-5"
    title: "Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5"
    author: Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül
---

# Match querying protocol to educational purpose: independent querying for raw knowledge checking, sequential querying for exam-like simulation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article distinguishes two utilization patterns of LLMs in dental education and links each to a querying protocol. Independent querying "measures raw knowledge accuracy in isolation", whereas sequential querying "evaluates the model's ability to maintain consistency throughout an extended session" in exam-like blocks of 10 items. Because sequential querying significantly lowered knowledge accuracy for the GPT models, educators should select the protocol—and the model—according to whether they want isolated knowledge practice or examination simulation.

## Design Implications

### Context
#### Requirements
- A standardized initial instruction prompt acknowledged by the model before questioning; fresh sessions to clear conversation history between phases.
#### Constraints
- Sequential querying significantly declined knowledge accuracy for GPT-5 and GPT-4o; effects were model-dependent and year-by-year differences were not significant.

### Target Learners
- Dental educators designing AI-supported practice and examination simulation

### Target Learning Goals
- Self-assessment of prosthodontics knowledge under realistic exam conditions

## Claims

- [Case-based question accuracy does not differ significantly across the four LLMs under either querying method](../claims/case-based-accuracy-no-model-difference.md) [+W]
- [The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance](../claims/llm-accuracy-differs-independent-query-dus-prosthodontics.md) [+W]
- [Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro](../claims/sequential-querying-degrades-gpt-knowledge-accuracy.md) [+W]
- [Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying](../claims/gemini-highest-case-accuracy-sequential.md) [~W]
- [The evaluated LLMs show higher accuracy on knowledge-based than case-based DUS questions, indicating a limitation in clinically oriented reasoning](../claims/llm-knowledge-beats-case-based-prosthodontics.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5
