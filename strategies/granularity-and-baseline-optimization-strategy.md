---
type: strategy
id: granularity-and-baseline-optimization-strategy
title: Develop a theoretically grounded data-granularity structure and stronger evaluation baselines, including meta-analysis-derived baselines
description: "The article recommends developing \"a theoretically grounded data structure for simulated data\" with standardized granularity levels (e.g., event-level, session-level, daily-level), since coarse simulations risk missin..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: jianxiao-jiang-2025
    resource: "https://arxiv.org/abs/2510.09183"
    title: "Jianxiao Jiang, Yu Zhang. (2025). Student Development Agent: Risk-free Simulation for Evaluating AIED Innovations. Preprint. https://arxiv.org/abs/2510.09183"
    author: Jianxiao Jiang, Yu Zhang
---

# Develop a theoretically grounded data-granularity structure and stronger evaluation baselines, including meta-analysis-derived baselines

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends developing "a theoretically grounded data structure for simulated data" with standardized granularity levels (e.g., event-level, session-level, daily-level), since coarse simulations risk missing subtle behaviors while fine-grained ones add noise and computational complexity. For evaluation, it proposes extending metrics beyond end-point outcomes to trajectories and key behaviors, embedding frequent consistency checks, and leveraging meta-analytic effect sizes to generate baselines when empirical data are sparse.

## Design Implications

### Context
#### Requirements
- Aligning simulation design with specific research questions and the theoretical constructs under investigation
#### Constraints
- The case study benefited from the MAIC platform's simplicity and narrow interaction scope; scaling to real classrooms requires handling more diverse and complex data types

### Target Learners
- students in classroom, school, and feature-rich online learning settings

### Target Learning Goals
- reproducing learning mechanisms and developmental trajectories, not merely end-point outcomes

### Affordances
- [Student Development Agent Framework](../research-methods/student-development-agents.md)

## Related Strategies

- [Validate the empirical-findings component and balance alignment against generalizability when injecting prior study results into agent prompts](validate-empirical-findings-component-balance.md)

## Examples
-

## Key Sources
- Jianxiao Jiang, Yu Zhang. (2025). Student Development Agent: Risk-free Simulation for Evaluating AIED Innovations. Preprint. https://arxiv.org/abs/2510.09183
