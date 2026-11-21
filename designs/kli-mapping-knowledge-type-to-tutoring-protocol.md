---
type: design
id: kli-mapping-knowledge-type-to-tutoring-protocol
title: KLI-framework-based mapping of knowledge types to LLM tutoring protocols in pedagogical prompts
description: The article uses the Knowledge-Learning-Instruction framework to select tutoring protocols within pedagogical prompts, ensuring alignment between the knowledge type being acquired and the tutoring strategy.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: ruiwei-xiao-2025
    resource: "https://arxiv.org/abs/2506.19107"
    title: "Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper. (2025). Improving Student-AI Interaction Through Pedagogical Prompting: An Example in Computer Science Education. arXiv preprint. https://arxiv.org/abs/2506.19107"
    author: Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper
---

# KLI-framework-based mapping of knowledge types to LLM tutoring protocols in pedagogical prompts

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article uses the Knowledge-Learning-Instruction framework to select tutoring protocols within pedagogical prompts, ensuring alignment between the knowledge type being acquired and the tutoring strategy. The KLI framework categorizes three broad classes of learning events: memory and fluency, induction and refinement, and understanding and sense-making, each mapped to evidence-based instructional methods. Code writing is treated as a variable-variable KC best served by induction and refinement, where "One effective approach is the worked example method (Sweller and Cooper, 1985)"; debugging is treated as a principle-type KC best served by prompted self-explanation.

## Design Implications

### Context
#### Requirements
- The learner or designer must classify the target knowledge component type before selecting a tutoring protocol
#### Constraints
- The mapping is applied in this work only to code writing and debugging scenarios in early undergraduate CS

### Target Learners
- early undergraduate CS novices

### Learning Goals
- matching AI tutoring strategies (e.g., worked examples, prompted self-explanation) to the knowledge being learned

### Claims
- 

## Related Designs
- Pedagogical Prompt Framework

## Examples
-

## Key Sources
- Ruiwei Xiao, Xinying Hou, Runlong Ye, Majeed Kazemitabaar, Nicholas Diana, Michael Liut and John Stamper. (2025). Improving Student-AI Interaction Through Pedagogical Prompting: An Example in Computer Science Education. arXiv preprint. https://arxiv.org/abs/2506.19107
