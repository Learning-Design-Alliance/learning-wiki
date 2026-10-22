---
type: strategy
id: representation-analysis-ablation-trajectory-comparison
title: Use representation analysis, ablation, and trajectory-level comparison to enable causal inference about learning mechanisms within AI models
description: The review recommends a set of methodological tools for interrogating AI cognitive models so that mechanistic claims about learning can be causally tested rather than merely asserted.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
sources:
  - id: peng-wang-2026
    resource: "https://doi.org/10.1007/s10648-026-10202-y"
    title: "Peng Wang, Olga Viberg, Effie Lai-Chong Law, Samuel Greiff. (2026). When Can AI Models Explain Learning? Validity Criteria for AI as Cognitive Models in Education. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10202-y"
    author: Peng Wang, Olga Viberg, Effie Lai-Chong Law, Samuel Greiff
---

# Use representation analysis, ablation, and trajectory-level comparison to enable causal inference about learning mechanisms within AI models

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 3 studies (2 causal, 1 design), `q1`–`q2` · 0 of 3 report an effect size · 1 claim rests on one study

## Description
The review recommends a set of methodological tools for interrogating AI cognitive models so that mechanistic claims about learning can be causally tested rather than merely asserted. These include representation analysis, ablation of model components, and trajectory-level comparison against human learning data. The review argues these tools "enable causal inference about learning mechanisms within models", for example targeted ablation of an anxiety signal to show that a proposed mechanism, rather than a surface correlate, actually drives model behavior.

## Design Implications

### Context
#### Requirements
- Model-internal evidence obtained through representation analysis and targeted ablation is required to show that the proposed mechanism actually drives the behavior
#### Constraints
- Disconfirming evidence includes a model that reproduces the accuracy gap while relying on representations unrelated to the proposed mechanism, or that matches aggregate scores but not the human error trajectory

### Target Learners
- Researchers building and validating AI cognitive models of learners

### Target Learning Goals
- Establishing causal mechanistic explanations of learning processes such as anxiety effects on problem solving

## Claims

- [Ablation study shows metadata-enriched embeddings produce the largest accuracy drop, while attention masking, KV caching and dynamic batching primarily support inference efficiency](../claims/ablation-metadata-embeddings-largest-accuracy-drop.md) [+M]
- [Ablation baselines were configured to isolate the contribution of cross-modal attention, PPO clipping and Kalman filtering, but component-level results are not reported in the available text](../claims/ablation-baseline-configuration-component-isolation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Peng Wang, Olga Viberg, Effie Lai-Chong Law, Samuel Greiff. (2026). When Can AI Models Explain Learning? Validity Criteria for AI as Cognitive Models in Education. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10202-y
