---
type: element
id: llmkt-llm-based-knowledge-tracing
title: "LLMKT: LLM-Based Knowledge Tracing for Dialogues"
description: "LLMKT is the article's knowledge tracing method: \"a novel LLM-based KT method, LLMKT, that leverages the textual content in dialogues, by fine-tuning the open-source Llama 3 LLM\" on the KT objective."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# LLMKT: LLM-Based Knowledge Tracing for Dialogues

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
LLMKT is the article's knowledge tracing method: "a novel LLM-based KT method, LLMKT, that leverages the textual content in dialogues, by fine-tuning the open-source Llama 3 LLM" on the KT objective. Given the dialogue up to the target turn and a prompt about one KC, it estimates mastery from the logits of the True and False tokens, averages KC masteries into a correctness prediction, and is trained with binary cross entropy. The article reports that "averaging over KC masteries performed better than taking a product over them", and the authors publicly release their code.

## Design Implications

### Context
#### Requirements
- Fine-tuning Llama-3.1-8B-Instruct (the article uses LoRA on NVIDIA RTX A6000 GPUs) on turn-level correctness labels.
- The dialogue text up to the current tutor turn and the text of each KC, packed into a single prompt with customized attention masks so KCs do not attend to each other.
#### Constraints
- KCs and correctness labels for previous turns are not explicitly provided due to memory constraints.
- The methods need to be tested on larger-scale data, since tutoring dialogue datasets are smaller than those typically used in standard KT works.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Goals
- Estimating student knowledge of math knowledge components (Common Core standards) and predicting student response correctness across dialogue turns

### Affordances
- [Dialogue Knowledge Tracing Framework](../theories/dialogue-knowledge-tracing-framework.md)

## Related Elements
- [Adaptive Learning](adaptive-learning.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
