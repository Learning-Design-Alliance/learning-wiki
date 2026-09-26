---
type: strategy
id: zpd-masked-rl-content-sequencing
title: "Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)"
description: The adaptive training component treats content sequencing as a sequential decision problem solved with Proximal Policy Optimization.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: chai-rui-2026
    resource: "https://doi.org/10.1038/s41598-026-51608-6"
    title: "Chai Rui. (2026). Deep learning-based intelligent diagnosis and adaptive training system for university english oral proficiency. Scientific Reports. https://doi.org/10.1038/s41598-026-51608-6"
    author: Chai Rui
---

# Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The adaptive training component treats content sequencing as a sequential decision problem solved with Proximal Policy Optimization. To formalize the zone of proximal development, content whose estimated success probability falls outside 0.4–0.8 is excluded: "Content falling outside this range is masked from the policy’s action space during training and inference, ensuring that the RL agent can only recommend activities within a pedagogically meaningful difficulty band." The reward combines diagnostic score improvement, task completion rate, and time-on-task efficiency.

## Design Implications

### Context
#### Requirements
- A trained diagnostic model supplying learner ability states, and empirically calibrated difficulty bounds (0.4 and 0.8) validated on a held-out set
#### Constraints
- Bounds were calibrated by maximizing normalized learning gain on a held-out validation set; sensitivity analysis showed stable performance only across moderate variations of about ±0.05

### Target Learners
- University English learners across proficiency levels

### Target Learning Goals
- Durable oral proficiency gains through appropriately challenged, individualized practice sequencing

## Related Strategies

- [Scaffolded Difficulty Progression](scaffolded-difficulty-progression.md)
- [Scaffolded Questioning](scaffolded-questioning.md)

## Examples
-

## Key Sources
- Chai Rui. (2026). Deep learning-based intelligent diagnosis and adaptive training system for university english oral proficiency. Scientific Reports. https://doi.org/10.1038/s41598-026-51608-6
