---
type: research-method
id: spatially-explicit-markov-simulation-of-educational-network-growth
title: Spatially explicit Markov simulation of educational network growth
description: "A discrete-time stochastic model with annual transitions representing both school robotics-program development and each school's relationship to the ARC network."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Spatially explicit Markov simulation of educational network growth

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A discrete-time stochastic model with annual transitions representing both school robotics-program development and each school's relationship to the ARC network. Each K–12 school carries two state variables — a FIRST program state (no program, Early, Mature) and an ARC state (Unreachable, Reachable, Supported, secondary Hub) — with nine legal combinations, plus college hub states; geography enters through a fixed relation specifying which schools each hub can serve. The article states "Reachability alone does not alter a school's natural program-development probabilities" and that direct ARC support is what allows different maturation and persistence behavior. It was instantiated for Indiana with 1,925 public K–12 schools and 32 potential college hubs, simulated 40 years over 1,000 Monte Carlo runs across 12 optimism levels, with ablations isolating hub-growth mechanisms.

## Accounts
<!-- How each source describes or uses the method -->
- **Spatially-explicit Markov model of ARC regional growth**: A discrete-time stochastic model with annual transitions representing both school robotics-program development and each school's relationship to the ARC network. Each K–12 school carries two state variables — a FIRST program state (no program, Early, Mature) and an ARC state (Unreachable, Reachable, Supported, secondary Hub) — with nine legal combinations, plus college hub states; geography enters through a fixed relation specifying which schools each hub can serve. The article states "Reachability alone does not alter a school's natural program-development probabilities" and that direct ARC support is what allows different maturation and persistence behavior. It was instantiated for Indiana with 1,925 public K–12 schools and 32 potential college hubs, simulated 40 years over 1,000 Monte Carlo runs across 12 optimism levels, with ablations isolating hub-growth mechanisms. (Jacobson et al. (2026))

### Claims
- [Indiana Markov simulation projects ARC reaches 74% of public K–12 schools and produces 992 robotics programs after 40 years at moderate optimism, versus 161 under natural growth](../claims/arc-simulation-indiana-growth-projections.md) [+W]
- [Simulation ablations show ARC's projected growth requires both primary and secondary hub mechanisms together](../claims/arc-ablation-complementary-hub-mechanisms.md) [+W]

## Related Research Methods
-

## Key Sources
- Jacobson, M. J.; Rodriguez-Rivera, G.; Drineas, P.; and Xue, Y. (2026). Teaching AI, Robotics, & Community: A Hubs-Based K–12 Education Framework for Reaching Rural Schools. https://arxiv.org/abs/2609.18072
