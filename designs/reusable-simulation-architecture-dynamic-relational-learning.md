---
type: design
id: reusable-simulation-architecture-dynamic-relational-learning
title: Reusable simulation architecture for dynamic relational learning environments
description: "The article abstracts SupplyNet's pipeline into \"a reusable simulation architecture for dynamic relational learning environments.\" A graph represents domain entities, dependencies, and time-varying states; agents and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: yanjia-li-2026
    resource: "https://arxiv.org/abs/2606.24694"
    title: "Yanjia Li, Kelcy Kexin Han, Tianrui Hu, Yi-Fan Cao, Huamin Qu, Sicheng Song. (2026). SupplyNet: Supporting Visual Exploratory Learning in Supply Chain via Contextual Multi-Agent Simulation. https://arxiv.org/abs/2606.24694"
    author: Yanjia Li, Kelcy Kexin Han, Tianrui Hu, Yi-Fan Cao, Huamin Qu, Sicheng Song
---

# Reusable simulation architecture for dynamic relational learning environments

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article abstracts SupplyNet's pipeline into "a reusable simulation architecture for dynamic relational learning environments." A graph represents domain entities, dependencies, and time-varying states; agents and learners observe relevant subgraphs, take domain-specific actions, and trigger state transitions; a database stores temporal snapshots supporting replay, branching, and comparison. The reusable layer separates from a domain-specific layer so other subjects can reuse the architecture by replacing the domain schema, transition rules, agent heuristics, event types, and learning metrics.

## Design Implications

### Context
#### Requirements
- Subjects must be modelable as dynamic relational systems involving multiple connected entities, local decisions or disturbances, delayed propagation of effects, and trade-offs that learners need to diagnose over time.
#### Constraints
- The architecture was designed and evaluated only in the supply chain management context; cross-subject instantiations are discussed as future work.

### Target Learners
- university students in domains modelable as dynamic relational systems

### Learning Goals
- diagnosing delayed propagation of effects and trade-offs in interconnected systems

### Claims
- 

## Related Designs

- Supplynet Visual Simulation System
- [Behavior-based persona and course-grounded memory architecture for simulated students](educasim-agent-persona-memory-architecture.md)
- [CogEvolution framework: ICAP perception, IRT-based memory retrieval, and evolutionary cognitive state update](cogevolution-agent-framework.md)
- [Multi-agent AI tutoring architecture with an orchestrating Tutor Agent and specialist agents](multi-agent-ai-math-tutor-architecture.md)

## Examples
-

## Key Sources
- Yanjia Li, Kelcy Kexin Han, Tianrui Hu, Yi-Fan Cao, Huamin Qu, Sicheng Song. (2026). SupplyNet: Supporting Visual Exploratory Learning in Supply Chain via Contextual Multi-Agent Simulation. https://arxiv.org/abs/2606.24694
