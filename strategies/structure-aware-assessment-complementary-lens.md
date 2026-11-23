---
type: strategy
id: structure-aware-assessment-complementary-lens
title: Use structure-aware assessment as a complementary lens to accuracy-based LLM evaluation
description: The article recommends evaluating reasoning systems against the prerequisite structure of the knowledge domain rather than relying solely on accuracy or trace-level judgments.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: peng-cui-2026
    resource: "https://arxiv.org/abs/2609.05245"
    title: "Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. https://arxiv.org/abs/2609.05245"
    author: Peng Cui, Heejin Do, and Mrinmaya Sachan
---

# Use structure-aware assessment as a complementary lens to accuracy-based LLM evaluation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends evaluating reasoning systems against the prerequisite structure of the knowledge domain rather than relying solely on accuracy or trace-level judgments. Its stated conclusion is that the findings "motivate structure-aware assessment as a complementary lens for rigorous evaluation". In practice this means measuring whether correct answers to dependent questions are grounded in prerequisite mastery (via PSR), whether prerequisite context uniquely scaffolds (SG), and whether stronger systems subsume weaker ones (KOC), since high accuracy was shown to mask pervasive structural inconsistency.

## Design Implications

### Context
#### Requirements
- Access to an expert-defined concept dependency structure for the evaluated domain
- Response data from both a target system and a human reference group
#### Constraints
- The article limits its evidence to mathematics and states whether the same observations extend to science, programming, or general factual knowledge "remains an open question"

### Target Learners
- LLM developers and evaluators
- educational assessment researchers

### Target Learning Goals
- reliable evaluation of genuine mathematical reasoning

### Affordances

## Claims

- [Human learners' knowledge states subsume weaker learners' nearly perfectly, while LLMs show substantially lower and more fragmented subsumption](../claims/llms-lack-coherent-knowledge-subsumption.md) [+W]
- [LLMs satisfy mathematical prerequisite dependencies far less often than human learners despite matching or exceeding human accuracy](../claims/llms-violate-prerequisite-dependencies-despite-high-accuracy.md) [+W]
- [Structural knowledge deficits in LLMs remain invisible to accuracy-based and LLM-as-judge reasoning evaluations](../claims/psr-invisible-to-accuracy-and-llm-judge-evaluation.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Peng Cui, Heejin Do, and Mrinmaya Sachan. (2026). Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory. arXiv. https://arxiv.org/abs/2609.05245
