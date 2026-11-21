---
type: design
id: learner-llm-co-decomposition
title: "Learner-LLM co-decomposition: learners lead problem decomposition while the LLM provides scaffolding only when needed"
description: "The article proposes learner-LLM co-decomposition as an approach to scaffolding algorithmic programming within the learner's Zone of Proximal Development."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: shuai-ma-2025
    resource: "https://doi.org/10.1145/3706598.3713748"
    title: "Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025. DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-Decomposition. In CHI Conference on Human Factors in Computing Systems (CHI '25). https://doi.org/10.1145/3706598.3713748"
    author: Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang
---

# Learner-LLM co-decomposition: learners lead problem decomposition while the LLM provides scaffolding only when needed

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes learner-LLM co-decomposition as an approach to scaffolding algorithmic programming within the learner's Zone of Proximal Development. Learners actively build a step tree capturing their thought process in code or natural language, while the LLM evaluates node statuses and provides only essential guidance. The authors state: "We term this approach 'learner-LLM co-decomposition', fundamentally distinct from the 'LLM-generate then user-verify' paradigm." Unlike tools that auto-generate decompositions for review, this design positions the learner as the lead decomposer and the LLM as a minimal, adaptive scaffold.

## Design Implications

### Context
#### Requirements
- Learners must be motivated, self-regulated, and actively engaging with the tool to improve their decomposition skills
#### Constraints
- The approach assumes students prefer independent problem-solving; the article notes less motivated students may bypass the tool to search for answers online

### Target Learners
- learners who understand basic algorithm concepts but struggle to apply them to practical problems
- university students in CS2-level algorithmic programming

### Learning Goals
- problem decomposition as a cornerstone of computational thinking
- independent problem-solving and algorithmic thinking

### Claims
- [Dbox Higher Test Correctness Than Baseline](../claims/dbox-higher-test-correctness-than-baseline.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025. DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-Decomposition. In CHI Conference on Human Factors in Computing Systems (CHI '25). https://doi.org/10.1145/3706598.3713748
