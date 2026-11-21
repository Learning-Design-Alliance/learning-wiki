---
type: strategy
id: anveshanai-dataset-augmentation-strategy
title: Augment question datasets via difficulty scaling and cross-mode adaptation with layered automated validation
description: "The paper recommends building practice datasets by augmenting a seed set of human-authored and curated tasks with two strategies: difficulty scaling, which introduces rephrased problems, domain-shift variants, and edg..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: rakesh-thakur-2025
    resource: "https://arxiv.org/abs/2509.23811"
    title: "Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari. (2025). ANVESHANAAI: A MULTIMODAL PLATFORM FOR ADAPTIVE AI/ML EDUCATION THROUGH AUTOMATED QUESTION GENERATION AND INTERACTIVE ASSESSMENT. arXiv preprint. https://arxiv.org/abs/2509.23811"
    author: Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari
---

# Augment question datasets via difficulty scaling and cross-mode adaptation with layered automated validation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The paper recommends building practice datasets by augmenting a seed set of human-authored and curated tasks with two strategies: difficulty scaling, which introduces rephrased problems, domain-shift variants, and edge cases, and cross-mode adaptation, which transforms base problems into coding, simulation, debugging, and viva-style formats. Quality is maintained through layered validation: LLM self-checks filter inconsistent problems, static validation ensures syntactic correctness, sandbox execution validates determinism of coding tasks, and rubric-based alignment ensures Bloom's taxonomy coverage.

## Design Implications

### Context
#### Requirements
- A structured schema with id, problem, answer, category, difficulty, tags, and bloom level fields; preprocessing via tokenization, chunking, and embedding for vectorized retrieval
#### Constraints
- Validation of executable coding tasks requires sandbox execution infrastructure; the reported pipeline was built for AI/ML subject matter

### Target Learners
- AI/ML learners from beginner to expert levels

### Target Learning Goals
- Balanced learning progression across difficulty levels and cognitive levels of Bloom's taxonomy

## Claims

- [Category and difficulty annotations are strongly correlated (Cramér's V = 0.596), while Bloom's level is only weakly associated with other dimensions (0.166–0.172)](../claims/anveshanai-cross-dimensional-correlations.md) [~W]
- [The AnveshanaAI dataset shows high annotation quality, including 97% effective utilization of Bloom's taxonomy levels](../claims/anveshanai-annotation-quality-metrics.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Rakesh Thakur, Diksha Khandelwal, Shreya Tiwari. (2025). ANVESHANAAI: A MULTIMODAL PLATFORM FOR ADAPTIVE AI/ML EDUCATION THROUGH AUTOMATED QUESTION GENERATION AND INTERACTIVE ASSESSMENT. arXiv preprint. https://arxiv.org/abs/2509.23811
