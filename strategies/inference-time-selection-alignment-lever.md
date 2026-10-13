---
type: strategy
id: inference-time-selection-alignment-lever
title: Use inference-time selection with a small interpretable index as a pedagogical alignment lever between full RL retraining and greedy decoding
description: "For practitioners, the article recommends keeping the model frozen and selecting among N stochastic candidate responses with an interpretable index rather than retraining: \"a useful pedagogical alignment lever sits be..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: shim-jaechang-and-unggi-lee
    resource: "https://arxiv.org/abs/2605.30666"
    title: "Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666"
---

# Use inference-time selection with a small interpretable index as a pedagogical alignment lever between full RL retraining and greedy decoding

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
For practitioners, the article recommends keeping the model frozen and selecting among N stochastic candidate responses with an interpretable index rather than retraining: "a useful pedagogical alignment lever sits between full RL retraining and unprincipled greedy decoding: inference-time selection with a tiny interpretable index retains the base model’s mathematical depth and exposes four interpretable weights for behavioural tuning". TEI@N generates N candidates, scores each with regex features plus a one-pass DTR forward hook, and returns the best-scoring response at cost linear in conversation length.

## Design Implications

### Context
#### Requirements
- A frozen reasoning LLM exposing explicit thinking traces; N stochastic candidate generations per turn
#### Constraints
- The selector helps most when the candidate pool is diverse and the base distribution is well-balanced; full RL alignment is described as a sharper but more dangerous instrument

### Target Learners
- students tutored by LLM math tutors

### Target Learning Goals
- improving learning outcomes of LLM tutoring without retraining the model

### Affordances
- Tutoring Effectiveness Index Tei

## Claims

- [TEI@4 selection shifts thinking-trace mass toward deeper deliberation, raising Schoenfeld Explore share by +10.8pp without changing the model](../claims/tei4-selects-deliberation-rich-candidates.md) [+M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666
