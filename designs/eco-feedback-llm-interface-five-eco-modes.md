---
type: design
id: eco-feedback-llm-interface-five-eco-modes
title: Eco-feedback LLM interface with five latency-based eco modes and four sustainability visualizations
description: "A live LLM chat interface in which \"Users can choose among multiple eco modes, each characterized by a distinct latency profile and corresponding carbon impact based on backend hardware configurations.\" Eco modes 1–5..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: hyeonwook-kim-2026
    resource: "https://arxiv.org/abs/2608.23968v1"
    title: "Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester. (2026). When LLMs Slow Down: How Environmental Impacts Mediate University Students' LLM Usage. https://arxiv.org/abs/2608.23968v1"
    author: Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester
---

# Eco-feedback LLM interface with five latency-based eco modes and four sustainability visualizations

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 qualitative), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A live LLM chat interface in which "Users can choose among multiple eco modes, each characterized by a distinct latency profile and corresponding carbon impact based on backend hardware configurations." Eco modes 1–5 trade response latency for lower emissions via tensor parallelism, batching, and renewable energy scheduling, within SLA constraints. The interface adds real-time latency and GHG metrics, cumulative carbon savings, annualized real-world impact equivalents, and a latency–emissions trade-off graph. It was deployed with 89 CS undergraduates in a computing ethics course.

## Design Implications

### Context
#### Requirements
- Operates under Service Level Agreement constraints, managing response latency to balance user experience and carbon emissions
- Requires backend configuration knobs (GPU count, batch size, renewable energy scheduling) to realize latency–emission trade-offs
#### Constraints
- The study assumed a fixed backend of four GPUs, batch size one, and no renewable energy scheduling, producing coarse-grained latency shifts that do not capture production systems' continuous behavior
- Carbon modeling involves uncertainty; the latency–GHG relationship illustrates general trends rather than precise real-world performance

### Target Learners
- undergraduate computer science students

### Learning Goals
- awareness of the environmental impacts of everyday LLM use
- understanding of latency–carbon trade-offs in AI systems

### Claims
- [Eco Mode Selection Declines With Latency](../claims/eco-mode-selection-declines-with-latency.md) [+M]
- [Eco Feedback Interface Supports Sustainability Learning](../claims/eco-feedback-interface-supports-sustainability-learning.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester. (2026). When LLMs Slow Down: How Environmental Impacts Mediate University Students' LLM Usage. https://arxiv.org/abs/2608.23968v1
