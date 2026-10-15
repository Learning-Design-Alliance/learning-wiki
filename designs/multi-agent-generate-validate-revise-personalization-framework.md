---
type: design
id: multi-agent-generate-validate-revise-personalization-framework
title: Multi-agent generate–validate–revise framework with four specialized validator agents for math problem personalization
description: The framework formalizes context personalization of math problems as an iterative generate–validate–revise loop.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: fareya-ikram-2026
    resource: "https://arxiv.org/abs/2604.05160"
    title: "Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160"
    author: Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan
---

# Multi-agent generate–validate–revise framework with four specialized validator agents for math problem personalization

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework formalizes context personalization of math problems as an iterative generate–validate–revise loop. A conversion agent generates an initial topic-aligned candidate problem, and "four independentvalidator agentsthat return a binary decision (pass/fail) and brief diagnostic feedback" check the candidate against solvability, realism, readability, and authenticity criteria; one or more refinement agents then revise the candidate using validator feedback until all validators pass or a maximum iteration count is reached. The framework is evaluated on 600 ASSISTments problems personalized to 20 student interest topics.

## Design Implications

### Context
#### Requirements
- A target topic reflecting a learner's interest, a target grade reading level computed with the Flesch–Kincaid metric, and validator feedback to drive refinement
#### Constraints
- Refinement iterates for at most k iterations (set to k=3 in the evaluation) and stops early only if the candidate passes all validator agent checks

### Target Learners
- middle school mathematics students

### Learning Goals
- math word problem solving with personally interesting contexts

### Claims
- [Single Refinement Iteration Reduces Personalization Failures](../claims/single-refinement-iteration-reduces-personalization-failures.md) [+M]
- [Validator Reliability Highest Realism Lowest Authenticity](../claims/validator-reliability-highest-realism-lowest-authenticity.md) [~M]

## Related Designs

- [Four specialized evaluation agents for LLM-generated problems](four-specialized-evaluation-agents-llm-problems.md)
- [Multi-agent teacher-in-the-loop architecture for context personalization](multi-agent-teacher-in-the-loop-architecture.md)

## Examples
-

## Key Sources
- Fareya Ikram, Nischal Ashok Kumar, Junyang Lu, Hunter McNichols, Candace Walkington, Neil Heffernan, and Andrew S. Lan. (2026). A Multi-Agent Approach to Validate and Refine LLM-Generated Personalized Math Problems. arXiv preprint. https://arxiv.org/abs/2604.05160
