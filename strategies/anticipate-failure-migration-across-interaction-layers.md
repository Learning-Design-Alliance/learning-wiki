---
type: strategy
id: anticipate-failure-migration-across-interaction-layers
title: Treat added output structure in AI problem solving systems as a tradeoff, anticipating failure migration across interaction layers
description: "For designers of AI-assisted problem solving systems, the article recommends that adding structure to model outputs, such as constrained executable reasoning, \"should be understood as a tradeoff rather than an unambig..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: sagnik-nath-2026
    resource: "https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
---

# Treat added output structure in AI problem solving systems as a tradeoff, anticipating failure migration across interaction layers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
For designers of AI-assisted problem solving systems, the article recommends that adding structure to model outputs, such as constrained executable reasoning, "should be understood as a tradeoff rather than an unambiguous improvement". Constraints can increase transparency and debuggability but introduce new points of breakdown at the protocol, execution, and mathematical layers. Designers should anticipate how failures migrate across representation layers rather than assuming they will disappear, treating LLMs as components within socio-technical systems.

## Design Implications

### Context
#### Requirements
- The system must log and categorize failure types (protocol violations, execution failures, math failures) separately so layer-specific breakdowns are visible.
#### Constraints
- The article states executable constraints can reduce per-success cost for some models despite increasing overall failure rates, so the tradeoff direction is model-specific.

### Target Learners
- designers of AI-assisted math problem solving systems
- system integrators deploying LLMs in interactive settings

### Target Learning Goals
- reliable operation of AI-assisted problem solving under executable output contracts

## Claims

- [Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations](../claims/executable-reasoning-failure-redistribution-layers.md) [+W]
- [Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier](../claims/code-augmented-latency-cost-increases.md) [+W]
- [Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance](../claims/representation-gaps-model-specific-code-amplification.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv
