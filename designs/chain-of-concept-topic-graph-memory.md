---
type: design
id: chain-of-concept-topic-graph-memory
title: "Chain-of-Concept: topic-graph organisation of past assessments replacing similarity-based retrieval"
description: "Chain-of-Concept is the article's framework for curriculum-grounded retrieval."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: runcong-zhao-2025
    resource: "https://arxiv.org/abs/2507.04295"
    title: "Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He. (2025). LearnLens: LLM-Enabled Personalised, Curriculum-Grounded Feedback with Educators in the Loop. https://arxiv.org/abs/2507.04295"
    author: Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He
---

# Chain-of-Concept: topic-graph organisation of past assessments replacing similarity-based retrieval

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Chain-of-Concept is the article's framework for curriculum-grounded retrieval. Rather than storing past assessment records sequentially and relying on surface-level embedding similarity, it organises records as a topic graph in which questions are decomposed into sub-question nodes labelled with curriculum topics, and retrieval is confined to the topic subgraph matching the query's topics. The authors state that topic filtering removes cross-topic noise, yielding more coherent evidence, and that the module then analyses pupil errors and prior knowledge to choose the most effective feedback strategy.

## Design Implications

### Context
#### Requirements
- Questions must be decomposed into sub-question nodes and labelled with one or more curriculum topics
- A FAISS-based ranker is used for scoring within the filtered topic subgraph
#### Constraints
- Retrieval is confined to the topic subgraph matching the query's tagged topics, so records sharing no topic with the query are excluded

### Target Learners
- GCSE science students

### Learning Goals
- Personalised, curriculum-aligned feedback generation

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Runcong Zhao, Artem Bobrov, Jiazheng Li, Cesare Aloisi, Yulan He. (2025). LearnLens: LLM-Enabled Personalised, Curriculum-Grounded Feedback with Educators in the Loop. https://arxiv.org/abs/2507.04295
