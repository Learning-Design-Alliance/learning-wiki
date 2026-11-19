---
type: strategy
id: classifier-reranking-hedge-generation-strategy
title: Use the hedge classifier to re-rank generation outputs when generating hedges for tutor agents
description: The authors propose a forward-looking strategy in which the trained hedge classifier supports generation of hedged utterances by tutoring agents rather than only classification.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: yann-raphalen-2023
    resource: "https://arxiv.org/abs/2306.14911"
    title: "Yann Raphalen, Chloé Clavel, Justine Cassell. (2023). \"You might think about slightly revising the title\": Identifying Hedges in Peer-tutoring Interactions. https://arxiv.org/abs/2306.14911"
    author: Yann Raphalen, Chloé Clavel, Justine Cassell
---

# Use the hedge classifier to re-rank generation outputs when generating hedges for tutor agents

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors propose a forward-looking strategy in which the trained hedge classifier supports generation of hedged utterances by tutoring agents rather than only classification. They state: "we will explore using the classifier to re-rank generation outputs, taking advantage of the recurring syntactic patterns (see (ii) in Section 5.3) to improve the generation process of hedges, and regenerating clauses that don't contain one of these syntactic patterns." This builds on the SHAP finding that each hedge class shows recurring POS-tag n-gram patterns.

## Design Implications

### Context
#### Requirements
- A trained hedge classifier and the recurring syntactic patterns identified via SHAP for each hedge class
#### Constraints
- Generation of hedges is explicitly not part of the current work; the strategy is stated as future work

### Target Learners
- students interacting with tutoring agents

### Target Learning Goals
- rapport management and indirect instruction delivery in tutoring dialogue

## Claims

- [Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups](../claims/lightgbm-all-features-best-f1-79.md) [+W]
- [A LightGBM model with knowledge-driven rule-based features outperforms fine-tuned BERT and an Attention-CNN baseline for hedge detection in peer-tutoring conversation](../claims/lightgbm-knowledge-driven-features-beat-bert-hedge-detection.md) [+W]
- [Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not](../claims/ngrams-help-tutoring-moves-nonverbal-do-not.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Yann Raphalen, Chloé Clavel, Justine Cassell. (2023). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. https://arxiv.org/abs/2306.14911
