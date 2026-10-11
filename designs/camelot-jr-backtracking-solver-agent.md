---
type: design
id: camelot-jr-backtracking-solver-agent
title: Camelot Jr. recursive backtracking solver agent
description: A game-playing agent for Camelot Jr.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: abhishek-jaiswal-2026
    resource: "https://arxiv.org/abs/2609.20349"
    title: "Abhishek Jaiswal, Zoe Falomir. (2026). A Qualitative Model for Reasoning about Path and Support. arXiv preprint. https://arxiv.org/abs/2609.20349"
    author: Abhishek Jaiswal, Zoe Falomir
---

# Camelot Jr. recursive backtracking solver agent

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A game-playing agent for Camelot Jr. implemented as 'a recursive backtracking protocol' that searches the permutation space of the block inventory for arrangements satisfying two independent criteria: Static Stability and Path Connectivity. Mirroring a human player, it places blocks one after another, evaluates structural validity once the inventory is fully deployed, and then evaluates path connectivity. It also 'implements geometric pruning strategies to cut off impractical search branches that cannot connect the start and the end points with the remaining inventory'.

## Design Implications

### Context
#### Requirements
- A limited block inventory and grid layout defining the challenge
- Support-footprint validation before committing to each placement
- Backtracking with state reversion when stability or path criteria fail
#### Constraints
- Stability is checked only after all blocks are placed, since counterweights can stabilize an initially unstable arrangement

### Target Learners
- players of the Camelot Jr. puzzle game
- children training spatial skills

### Learning Goals
- block placement under stability constraints
- pathfinding from start to goal

### Claims
- [Camelot Jr Solver Solves Arbitrary Configurations](../claims/camelot-jr-solver-solves-arbitrary-configurations.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Abhishek Jaiswal, Zoe Falomir. (2026). A Qualitative Model for Reasoning about Path and Support. arXiv preprint. https://arxiv.org/abs/2609.20349
