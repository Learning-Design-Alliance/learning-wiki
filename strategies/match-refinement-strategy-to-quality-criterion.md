---
type: strategy
id: match-refinement-strategy-to-quality-criterion
title: "Match the refinement coordination strategy to the quality criterion: decentralized refinement for localized criteria, centralized planning for holistic ones"
description: The article recommends coordinating validator feedback differently depending on the criterion being refined.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: fareya-ikram-2026
    resource: "https://arxiv.org/abs/2604.05160"
    title: "Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160"
    author: Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan
---

# Match the refinement coordination strategy to the quality criterion: decentralized refinement for localized criteria, centralized planning for holistic ones

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends coordinating validator feedback differently depending on the criterion being refined. For criteria fixable with localized edits, such as realism and readability, the authors write that "we should not aggregate this feedback with other feedback before refinement," favoring Decentralized Refinement; for more global, coherence-dependent criteria such as authenticity, Centralized Refinement with Planning converges faster. The strategy therefore treats feedback coordination as a criterion-dependent design decision rather than a one-size-fits-all pipeline.

## Design Implications

### Context
#### Requirements
- Specialized validator agents for each quality criterion, and refinement agents that can be paired per criterion or coordinated through a planning agent
#### Constraints
- The article notes trade-offs: Centralized emphasizes mathematical preservation at the expense of contextual richness, Centralized with Planning may compromise pedagogical intent, and Decentralized increases sentence complexity

### Target Learners
- middle school mathematics students

### Target Learning Goals
- generating personalized math problems that are solvable, realistic, readable, and authentic

### Affordances
- [Multi Agent Generate Validate Revise Personalization Framework](../designs/multi-agent-generate-validate-revise-personalization-framework.md)

## Related Strategies

- [Combine holistic with analytic scores as a complementary approach to enhance rating validity](combine-holistic-analytic-complementary-scoring.md)

## Examples
-

## Key Sources
- Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160
