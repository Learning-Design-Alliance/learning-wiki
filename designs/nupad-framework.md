---
type: design
id: nupad-framework
title: "NuPaD framework: three coupled components transforming GenAI into an inquiry-driven tutor"
description: "NuPaD (Nuclear & Particle Physics – Deep Learning Tutor) is a pedagogical framework for graduate subatomic physics that redefines the student–model interaction loop."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: chong-qi-2026
    resource: "https://arxiv.org/abs/2609.36930"
    title: "Chong Qi. (2026). NuPaD: A Generative AI Framework for Fostering Deep Learning in Subatomic Physics. arXiv. https://arxiv.org/abs/2609.36930"
    author: Chong Qi
---

# NuPaD framework: three coupled components transforming GenAI into an inquiry-driven tutor

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
NuPaD (Nuclear & Particle Physics – Deep Learning Tutor) is a pedagogical framework for graduate subatomic physics that redefines the student–model interaction loop. It couples a primary agent instruction file that "enforces a structured problem-based learning protocol", a Markdown textbook with Wiki RAG as an external knowledge base, and a condensed companion file grounding the model's factual baseline, plus nine modular sub-skills. The GenAI "is not considered the primary source of scientific truth" but a writing and reasoning assistant on an instructor-validated knowledge base.

## Design Implications

### Context
#### Requirements
- A structured, machine-readable knowledge base (Markdown textbook and companion file) from which the agent retrieves
- The skill file set as system prompt or loaded into an agentic environment to impose behavioral constraints
#### Constraints
- Designed for the graduate-level subatomic physics curriculum; the article states the framework aims to transform GenAI rather than reporting measured learning gains

### Target Learners
- graduate subatomic physics students (Explorer, Builder, Frontier levels)

### Learning Goals
- deep conceptual understanding and scientific reasoning in nuclear and particle physics

### Claims

- [Nupad Skill File Overrides Answer Tendency](../claims/nupad-skill-file-overrides-answer-tendency.md) [+W]
- Nupad Hierarchical Indexing Retrieval Balance [+W]
- [The article classifies unmediated GenAI's pedagogical risks in physics education as two illusions and two erosions](../claims/genai-illusions-erosions-physics-education.md) [+W]

## Related Designs

- [Markdown textbook with Wiki RAG and custom structural tags](nupad-markdown-textbook-wiki-rag.md)

## Examples
-

## Key Sources
- Chong Qi. (2026). NuPaD: A Generative AI Framework for Fostering Deep Learning in Subatomic Physics. arXiv. https://arxiv.org/abs/2609.36930
