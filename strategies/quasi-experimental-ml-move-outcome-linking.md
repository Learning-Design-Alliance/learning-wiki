---
type: strategy
id: quasi-experimental-ml-move-outcome-linking
title: Link tutor move patterns to learning outcomes with quasi-experimental machine learning such as leave-one-out potential outcomes and causal forests
description: "The National Tutoring Observatory plans to link tutor moves to learning outcomes using quasi-experimental machine learning — \"such as leave-one-out potential outcomes and causal forests\" — to estimate heterogeneous se..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zhuqian-zhou-2025
    resource: "https://arxiv.org/abs/2603.05778"
    title: "Zhuqian Zhou, Kirk Vanacore, Tamisha Thompson, Jennifer St John, René Kizilcec (2025). Tutor Move Taxonomy: A Theory-Aligned Framework for Analyzing Instructional Moves in Tutoring. National Tutoring Observatory, Cornell University. https://arxiv.org/abs/2603.05778"
    author: Zhuqian Zhou, Kirk Vanacore, Tamisha Thompson, Jennifer St John, René Kizilcec
---

# Link tutor move patterns to learning outcomes with quasi-experimental machine learning such as leave-one-out potential outcomes and causal forests

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The National Tutoring Observatory plans to link tutor moves to learning outcomes using quasi-experimental machine learning — "such as leave-one-out potential outcomes and causal forests" — to estimate heterogeneous session effectiveness and identify behaviors associated with stronger learning gains. The approach complements the observatory's inductive analysis rather than presuming what constitutes good tutoring.

## Design Implications

### Context
#### Requirements
- Session-level covariates and outcome data; the article notes that given a high-dimensional matrix of covariates, these methods can estimate near-individual-level treatment effects
#### Constraints
- The causal-forest study of human tutoring support in an intelligent tutoring intervention is ongoing with a preprint forthcoming; no results are reported in this article

### Target Learners
- Students receiving one-on-one or high-dosage tutoring through the observatory's provider partners

### Target Learning Goals
- Identifying which tutoring behaviors and interaction patterns are associated with stronger learning gains

### Affordances
- [Nto Tutor Move Taxonomy Four Categories](../research-methods/nto-tutor-move-taxonomy-four-support-categories-with-learning-support-moves-organized-alon.md)

## Claims

- [Combining tutor talk moves with student ITS metrics predicts math assessment scores better than either feature source alone (AUC 0.77 vs 0.63 and 0.66)](../claims/combined-talk-moves-its-predict-math-achievement.md) [+W]
- [The talk-move/ITS interaction pattern persists when predicting changes in assessment scores across rounds](../claims/talk-moves-its-robust-across-score-changes.md) [+W]

## Related Strategies

- [Scale tutor move annotation with large language models trained and validated on human annotations, enabling real-time analytics and feedback tools](llm-assisted-tutor-move-annotation.md)

## Examples
-

## Key Sources
- Zhuqian Zhou, Kirk Vanacore, Tamisha Thompson, Jennifer St John, René Kizilcec (2025). Tutor Move Taxonomy: A Theory-Aligned Framework for Analyzing Instructional Moves in Tutoring. National Tutoring Observatory, Cornell University. https://arxiv.org/abs/2603.05778
