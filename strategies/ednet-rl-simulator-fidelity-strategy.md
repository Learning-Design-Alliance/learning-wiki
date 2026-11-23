---
type: strategy
id: ednet-rl-simulator-fidelity-strategy
title: "Build student simulators of varying fidelity from EdNet's hierarchy for RL-based learning path recommendation"
description: "For RL-based learning path recommendation, where evaluating a tutoring strategy on real students is extremely costly, the authors propose training simulated students from different EdNet levels: a KT1-based simulator..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: choi-2020
    resource: "https://arxiv.org/abs/1912.03072"
    title: "Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. https://arxiv.org/abs/1912.03072"
    author: Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J
---

# Build student simulators of varying fidelity from EdNet's hierarchy for RL-based learning path recommendation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For RL-based learning path recommendation, where evaluating a tutoring strategy on real students is extremely costly, the authors propose training simulated students from different EdNet levels: a KT1-based simulator generates virtual responses to suggested questions, while KT4-based simulators can also generate lecture-watching, purchasing, and answer-elimination actions. Each option, they write, "trades off simplicity with fidelity," and "EdNet gives the researcher the opportunity to find the most appropriate simulator that suits the particular goal of the agent being trained."

## Design Implications

### Context
#### Requirements
- A trained model predicting student responses/actions from the chosen EdNet level's historical data
#### Constraints
- Simulator fidelity trades off against simplicity; most RL methods require simulated students because evaluating a tutoring strategy with real students is extremely costly

### Target Learners
- TOEIC self-study students served by RL-based tutoring policies

### Target Learning Goals
- individualized optimal learning path recommendation
- tutoring policy training

## Related Strategies
- 

## Examples
-

## Key Sources
- Choi, Y., Lee, Y., Shin, D., Cho, J., Park, S., Lee, S., Baek, J., Bae, C., Kim, B., Heo, J. (2020). EdNet: A Large-Scale Hierarchical Dataset in Education. https://arxiv.org/abs/1912.03072
