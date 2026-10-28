---
type: strategy
id: overgenerate-and-rank-aqg
title: "Over-generate and rank: generate many questions then filter for quality"
description: "Several question generators employ an \"over-generate and rank\" approach in which a large number of questions are produced and then ranked or filtered in a subsequent phase, with the ranking goal of prioritising good q..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: ghader-kurdi-2020
    resource: "https://doi.org/10.1007/s40593-019-00186-y"
    title: "Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari. (2020). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-019-00186-y"
    author: Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari
---

# Over-generate and rank: generate many questions then filter for quality

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Several question generators employ an "over-generate and rank" approach in which a large number of questions are produced and then ranked or filtered in a subsequent phase, with the ranking goal of prioritising good quality questions. The review reports this as a post-processing strategy implemented with statistical models. It addresses the problem that not all automatically generated questions are of sufficient quality for use.

## Design Implications

### Context
#### Requirements
- A ranking or filtering mechanism, typically statistical models trained to score question quality
#### Constraints
- 

### Target Learners
- learners receiving automatically generated assessment or practice questions

### Target Learning Goals
- access to high-quality generated questions

## Claims

- [Raising the answer-confidence threshold reduces the number of retained MCQs but substantially improves their quality](../claims/answer-confidence-threshold-trades-quantity-for-quality.md) [+W]

## Related Strategies

- [Content selection: identify important sentences or concepts before generating questions](aqg-content-selection-strategy.md)
- [Use an SLM for rapid large-scale question generation with an LLM providing validation feedback](slm-generate-llm-validate-synergy.md)
- [Brainstorming](brainstorming.md)

## Examples
-

## Key Sources
- Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari. (2020). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-019-00186-y
