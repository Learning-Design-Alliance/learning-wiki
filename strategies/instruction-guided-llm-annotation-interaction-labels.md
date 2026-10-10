---
type: strategy
id: instruction-guided-llm-annotation-interaction-labels
title: Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling
description: The article describes an annotation procedure using an instruction-guided LLM following a human-in-the-loop process to apply the taxonomy at scale.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: taelin-karidi-2026
    resource: "https://arxiv.org/abs/2606.29442"
    title: "Taelin Karidi, Ofra Amir, and Ido Roll. (2026). AI in the Wild: A Large Scale Analysis of Authentic Interactions of College Students with Generative AI. https://arxiv.org/abs/2606.29442"
    author: Taelin Karidi, Ofra Amir, and Ido Roll
---

# Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article describes an annotation procedure using an instruction-guided LLM following a human-in-the-loop process to apply the taxonomy at scale. The prompt was "iteratively developed by applying it to subsets of the data, inspecting outputs and refining label definitions and disambiguation rules until stable behavior was achieved", then applied uniformly to the full dataset using gpt-5-mini. The model was constrained to predefined label sets and output a confidence score per annotation.

## Design Implications

### Context
#### Requirements
- Iterative prompt refinement on data subsets until stable labeling behavior; full guidelines and prompt templates released in an online repository.
#### Constraints
- The study does not evaluate agreement between LLM-based and human annotations, relying instead on the prompt-based procedure; the authors suggest future work incorporate targeted human annotation.

### Target Learners
- researchers analyzing student–AI interaction data at scale

### Target Learning Goals
- characterizing cognitive intent and interaction context in student–AI conversations

## Related Strategies

- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](structured-prompts-clear-construct-definitions-llm-labeling.md)
- [Structured prompt framework for LLM-assisted inductive coding (role assignment, format specification, reasoning-based prompting)](structured-prompt-framework-inductive-coding.md)
- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)
- [Four guidelines for designing LLM-assisted qualitative coding pipelines](guidelines-llm-qualitative-coding-pipelines.md)

## Examples
-

## Key Sources
- Taelin Karidi, Ofra Amir, and Ido Roll. (2026). AI in the Wild: A Large Scale Analysis of Authentic Interactions of College Students with Generative AI. https://arxiv.org/abs/2606.29442
