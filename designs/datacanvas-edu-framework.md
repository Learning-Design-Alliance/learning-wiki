---
type: design
id: datacanvas-edu-framework
title: "DataCanvas-EDU: a four-phase agentic framework for instructor-guided synthetic data generation"
description: DataCanvas-EDU is an agentic framework in which the instructor specifies a teaching brief (business setting, learner level, permitted tools, assignment scope) and intended patterns through conversation, while an AI ag...
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: bang-an-2026
    resource: "https://arxiv.org/abs/2609.19617"
    title: "Bang An, Maria Hamdani, Joseph Fox. (2026). DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education. https://arxiv.org/abs/2609.19617"
    author: Bang An, Maria Hamdani, Joseph Fox
---

# DataCanvas-EDU: a four-phase agentic framework for instructor-guided synthetic data generation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
DataCanvas-EDU is an agentic framework in which the instructor specifies a teaching brief (business setting, learner level, permitted tools, assignment scope) and intended patterns through conversation, while an AI agent writes generation code, checks the exported data, and prepares reference analyses, assignments, and rubrics. As the paper states, "Four phases—Plan, Create, Verify / Test Analysis, and Evaluate—organize the process and support instructor review and revision." A shared case specification connects each intended pattern to its generation rule, comparison groups, measurement, and sample-size requirements, guiding checks and revision.

## Design Implications

### Context
#### Requirements
- Instructor approval of the complete design before the agent begins routine programming and numerical checks; changes to a substantive pattern or its intended difficulty require the instructor's review
#### Constraints
- The current workflow generates records from scratch and its numerical helper supports Python generation and a single CSV table; code execution is subject to the host environment's permissions

### Target Learners
- undergraduate business analytics students

### Learning Goals
- data investigation and visualization
- formulating analytical questions and justifying findings

### Claims
- [Agent Pattern Discovery Gap Windowdash Vs Olist](../claims/agent-pattern-discovery-gap-windowdash-vs-olist.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Bang An, Maria Hamdani, Joseph Fox. (2026). DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education. https://arxiv.org/abs/2609.19617
