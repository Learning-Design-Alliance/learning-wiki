---
type: strategy
id: dependency-taxonomy-curriculum-arrangement-strategy
title: Arrange SFT curriculum so preliminary categories (math and coding) dominate the early stage and subsequential categories the later stage
description: "A concrete curriculum recipe derived from the dependency taxonomy: in the first |D| instances, increase the proportion of preliminary category instructions by 50%; in the last |D| instances, decrease it by 50%, keepin..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: hanyu-zhao-2024
    resource: "https://arxiv.org/abs/2409.07045"
    title: "Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2024). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. https://arxiv.org/abs/2409.07045"
    author: Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan
---

# Arrange SFT curriculum so preliminary categories (math and coding) dominate the early stage and subsequential categories the later stage

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
A concrete curriculum recipe derived from the dependency taxonomy: in the first |D| instances, increase the proportion of preliminary category instructions by 50%; in the last |D| instances, decrease it by 50%, keeping the total number and constitution of the curriculum data identical. The article states this arranges instructions "to increase the proportion of preliminary category instructions in the early stage of SFT and increase the proportion of subsequential category instructions in the later stage of SFT". It is implementable with any tagged instruction set and induced taxonomy.

## Design Implications

### Context
#### Requirements
- Requires a dependency taxonomy over instruction categories and a base instruction set D partitioned into preliminary, intermediary, and subsequential category instructions.
#### Constraints
- The article's experiments used three epochs with the specified 50% shifts; performance beyond these settings is not reported.

### Target Learners
- Large language models undergoing supervised fine-tuning

### Target Learning Goals
- Acquiring complex task skills after preliminary knowledge is equipped

### Affordances
- Instruction Dependency Taxonomy

## Claims

- [DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA](../claims/dt-csft-curriculum-improves-sft.md) [+W]
- [Negative effect equivalence coefficients were observed between instruction categories; performance on one category fell from pre-test to post-test after another category was added, in one single-group pre-post study](../claims/antagonistic-instruction-category-effects.md) [+W]
- [Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning](../claims/mix-plus-uniform-addition-not-beneficial.md) [+W]
- [Hierarchical clustering of effect equivalence coefficients was reported to identify two meta-groups: a Symbolic Reasoning group and a Commonsense Memorization group](../claims/instruction-meta-groups-symbolic-commonsense.md) [+W]
- [EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone](../claims/ee-cpo-improves-over-deita.md) [+W]
- [Correlation patterns between categories of instructions are widespread across multiple instruction categories and different LLMs](../claims/widespread-instruction-category-correlation-patterns.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2024). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. https://arxiv.org/abs/2409.07045
