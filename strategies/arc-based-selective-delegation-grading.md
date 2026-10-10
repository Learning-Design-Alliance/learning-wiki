---
type: strategy
id: arc-based-selective-delegation-grading
title: Use accuracy-rejection curves with reliability analysis to select operating points for selective delegation in human-in-the-loop grading
description: The article recommends that educators and system designers use accuracy-rejection curves together with reliability analysis as a principled basis for selective grading decisions, rather than thresholds chosen solely f...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: longwei-cong-2026
    resource: "https://arxiv.org/abs/2605.00200"
    title: "Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200"
    author: Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne
---

# Use accuracy-rejection curves with reliability analysis to select operating points for selective delegation in human-in-the-loop grading

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that educators and system designers use accuracy-rejection curves together with reliability analysis as a principled basis for selective grading decisions, rather than thresholds chosen solely from predefined error metrics. The ARC plots retained-prediction accuracy as a function of rejection rate, letting users pick an operating point that balances grading accuracy against the amount of manual review required. The article states that "an optimal trade-off point can be defined by jointly maximizing accuracy and human effort reduction", providing "a principled basis for selective grading decisions".

## Design Implications

### Context
#### Requirements
- Confidence scores for each automated grading decision, evaluated with ROC and ARC analyses and reliability metrics
#### Constraints
- The article demonstrates this on one dataset and one model; it recommends user studies with educators to understand how confidence estimates are interpreted and used in real workflows

### Target Learners
- students whose short constructed responses are graded in human-in-the-loop assessment workflows

### Target Learning Goals
- balancing automated grading accuracy against human review effort in assessment

### Affordances
- [Hybrid Confidence Framework Aleatoric Semantic Heterogeneity](../research-methods/hybrid-confidence-framework-integrating-model-based-confidence-with-dataset-derived-aleato.md)

## Related Strategies

- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)

## Examples
-

## Key Sources
- Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200
