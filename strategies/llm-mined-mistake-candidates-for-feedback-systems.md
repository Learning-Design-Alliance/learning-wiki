---
type: strategy
id: llm-mined-mistake-candidates-for-feedback-systems
title: Use validated LLM-generated mistake candidates as a preliminary step toward targeted feedback in interactive learning systems
description: The article recommends using transformation-based mistake candidates to scale discovery of common mistakes in education settings, and proposes integrating the resulting candidates into feedback systems of interactive...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: lilian-killich-2026
    resource: "https://arxiv.org/abs/2609.17111"
    title: "Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111"
    author: Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume
---

# Use validated LLM-generated mistake candidates as a preliminary step toward targeted feedback in interactive learning systems

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends using transformation-based mistake candidates to scale discovery of common mistakes in education settings, and proposes integrating the resulting candidates into feedback systems of interactive learning tools. Because candidates are validated algorithmically before entering the output set, the workflow addresses the reliability concerns the article raises about LLM-generated feedback content.

## Design Implications

### Context
#### Requirements
- Educational datasets of (incorrect, correct) formalization pairs from the target formalism
- Algorithmic validation of LLM-proposed transformations before use
#### Constraints
- Candidates are mistake candidates, not confirmed conceptual mistakes; researcher inspection of clusters is a necessary follow-up step

### Target Learners
- Students of computer science and other STEM disciplines learning to model with mathematical formalisms

### Target Learning Goals
- Providing targeted, high-quality feedback on modelling assignments in interactive learning systems

### Affordances
- [Bug Fixing Transformation Workflow Llm](../research-methods/tool-supported-workflow-for-identifying-clustering-and-visualizing-common-modelling-mistak.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Lilian Killich, Marko Schmellenkamp, Fabian Vehlken, Thomas Zeume. (2026). Finding Common Mistakes In Modelling With Mathematical Formalisms Using LLMs. https://arxiv.org/abs/2609.17111
