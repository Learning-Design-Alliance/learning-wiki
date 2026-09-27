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
> **Evidence** · 3 claims (3 for) · 1 study, `q1` · 0 of 1 report an effect size · 3 claims rest on one study

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

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](../claims/llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) [+W]
- [In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels.](../claims/llmkt-uses-dialogue-text-to-adjust-kc-mastery-estimates.md) [+W]
- [LLMKT's predicted knowledge change curves on CoMTA are mixed across the 15 most frequent KCs, though overall they mostly resemble the power law of practice when dialogues have sufficient turns.](../claims/llmkt-knowledge-change-curves-show-mixed-trends-resembling-power-law-of-practice.md) [+W]

## Related Elements
- [Adaptive Learning](adaptive-learning.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
