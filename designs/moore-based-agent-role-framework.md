---
type: design
id: moore-based-agent-role-framework
title: "Role design framework instantiating Moore's three educational interaction types as agent roles (Tutee, Peer, Challenger) plus a learner-content Control"
description: "The article grounds its agent role design in Moore's framework of educational interaction, which \"identifies three fundamental types of interaction in learning: learner-instructor, learner-learner, and learner-content\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: zhengtao-xu-2026
    resource: "https://doi.org/10.1145/3772318.3790298"
    title: "Zhengtao Xu, Junti Zhang, Anthony Tang, and Yi-Chieh Lee. (2026). Who You Explain To Matters: Learning by Explaining to Conversational Agents with Different Pedagogical Roles. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790298"
    author: Zhengtao Xu, Junti Zhang, Anthony Tang, and Yi-Chieh Lee
---

# Role design framework instantiating Moore's three educational interaction types as agent roles (Tutee, Peer, Challenger) plus a learner-content Control

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
The article grounds its agent role design in Moore's framework of educational interaction, which "identifies three fundamental types of interaction in learning: learner-instructor, learner-learner, and learner-content". The Tutee agent instantiates a reversed learner-instructor dynamic drawing on the protégé effect; the Peer agent represents collaborative learner-learner interaction grounded in peer learning and socially shared metacognition; the Challenger agent embodies an expert instructor using Socratic questioning grounded in cognitive conflict and conceptual change; and the Control condition represents pure learner-content interaction. This mapping enables structured investigation of how pedagogical framings shape learning dynamics.

## Design Implications

### Context
#### Requirements
- Agents must be powered by a capable LLM (GPT-4o in the study) handling message analysis and response generation
- Role-consistent prompts and workflows must be designed so each agent enacts its pedagogical role
#### Constraints
- Roles were instantiated for one undergraduate economics concept (supply and demand) in short sessions, so generalization to other domains is not established by the study

### Target Learners
- undergraduate-level learners
- adult online learners

### Learning Goals
- conceptual understanding of economics concepts
- explanation and application of principles to scenarios

### Claims
- [Role Specific Interaction Patterns](../claims/role-specific-interaction-patterns.md) [+M]
- [Tutee And Control Induce High Pressure](../claims/tutee-and-control-induce-high-pressure.md) [+M]
- [Peer Role Fosters Absorption And Fluency](../claims/peer-role-fosters-absorption-and-fluency.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Zhengtao Xu, Junti Zhang, Anthony Tang, and Yi-Chieh Lee. (2026). Who You Explain To Matters: Learning by Explaining to Conversational Agents with Different Pedagogical Roles. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790298
