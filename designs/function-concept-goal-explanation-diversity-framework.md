---
type: design
id: function-concept-goal-explanation-diversity-framework
title: Three-dimension semantic diversity framework for LLM code explanations (function, concept, goal)
description: "The article operationalizes explanation diversity as three distinct semantic dimensions drawn from prior work on code comprehension: function, concept, and goal."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: seth-bernstein-2026
    resource: "https://arxiv.org/abs/2606.28882"
    title: "Seth Bernstein, Paul Denny, Juho Leinonen, Kush Patel, Rayhona Nasimova, Matt Littlefield, and Stephen MacNeil. (2026). Exploring the Value of Diverse LLM Explanations in Introductory Programming. SIGCSE Virtual '26. https://arxiv.org/abs/2606.28882"
    author: Seth Bernstein, Paul Denny, Juho Leinonen, Kush Patel, Rayhona Nasimova, Matt Littlefield, and Stephen MacNeil
---

# Three-dimension semantic diversity framework for LLM code explanations (function, concept, goal)

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article operationalizes explanation diversity as three distinct semantic dimensions drawn from prior work on code comprehension: function, concept, and goal. In the Diverse condition, "we issued three distinct prompts targeting function, concept, and goal as the three dimensions, generating one explanation per dimension." These dimensions were chosen because prior work identifies them as distinct cognitive registers: "understanding what code does, why the underlying mechanism works, and what the program is trying to accomplish." Generic explanations, by contrast, were produced by issuing the identical prompt three times, covering the snippet in an all-purpose way. The framework is grounded in Variation Theory, which holds that learners grasp a concept when they see systematic variation exposing its critical features.

## Design Implications

### Context
#### Requirements
- GPT-4o (or similar LLM) used to generate one explanation per dimension with distinct prompts targeting function, concept, and goal
#### Constraints
- The authors note the sources of variation employed may not have been aligned with the dimensions students needed to discern, and the study did not compare outcomes across the three explanation dimensions individually

### Target Learners
- first-year computing students learning recursion in C

### Learning Goals
- code comprehension and understanding of recursion concepts

### Claims
- [Diverse Llm Explanations Higher Oe Accuracy Not Significant](../claims/diverse-llm-explanations-higher-oe-accuracy-not-significant.md) [~M]
- [No Significant Difference Perceived Helpfulness](../claims/no-significant-difference-perceived-helpfulness.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Seth Bernstein, Paul Denny, Juho Leinonen, Kush Patel, Rayhona Nasimova, Matt Littlefield, and Stephen MacNeil. (2026). Exploring the Value of Diverse LLM Explanations in Introductory Programming. SIGCSE Virtual '26. https://arxiv.org/abs/2606.28882
