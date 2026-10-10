---
type: strategy
id: intended-impact-evaluation-strategy
title: Include an explicit intended-impact target in NLP evaluation and use noise-robust designs rather than only point estimates
description: "The article recommends that evaluators in domains with delayed, aggregated, or confounded outcomes adopt designs that stay robust under noise: \"multifacet decom- positions, decision studies, hierarchical rater models,..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.00883"
    title: "Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883"
    author: Michael Hardy, Yunsung Kim
---

# Include an explicit intended-impact target in NLP evaluation and use noise-robust designs rather than only point estimates

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that evaluators in domains with delayed, aggregated, or confounded outcomes adopt designs that stay robust under noise: "multifacet decom- positions, decision studies, hierarchical rater models, residualization and mediation analyses, and pre-registered stress tests." When consensus among models correlates poorly or negatively with intended impact, the authors advise reducing the shared misalignment component rather than chasing prompt-dependent gains on fixed transcript sets.

## Design Implications

### Context
#### Requirements
- requires access to an external intended-impact criterion, even a noisy one, and reporting of uncertainty and sensitivity rather than only point estimates
#### Constraints
- the article warns prompt changes can produce dramatic wins on a handful of cases while silently degrading performance elsewhere

### Target Learners
- schoolchildren affected by deployed educational AI systems

### Target Learning Goals
- validity of AI judgments relative to causal student learning outcomes

### Affordances
- [High Noise Alignment Measurement Framework](../research-methods/four-step-methodological-framework-for-measuring-llm-alignment-to-intended-impact-in-high.md)

## Related Strategies

- [Involve domain experts throughout the AI safety evaluation pipeline, especially for defining unsafe content](domain-experts-throughout-child-safety-evaluation.md)

## Examples
-

## Key Sources
- Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883
