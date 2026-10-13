---
type: product
id: smarttutor
title: SmartTutor
description: A simulated Python tutoring environment developed by Oluseyi Olukolaa for testing pedagogical safety and adaptive tutoring policies in educational reinforcement-learning systems.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SmartTutor

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
A simulated Python tutoring environment developed by Oluseyi Olukolaa for testing pedagogical safety and adaptive tutoring policies in educational reinforcement-learning systems.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **SmartTutor simulated Python tutoring testbed for evaluating pedagogical safety in educational RL**: SmartTutor is a simulated Python tutoring environment comprising "a knowledge graph of 27 Python concepts (DAG, max depth 7", a student model with per-concept mastery tracking, a neural contextual bandit agent with UCB action selection over a 124-dimensional state representation, an action selection module enforcing C1 and C3 online, and a configurable reward system. Eight pedagogical actions span cognitive demand from d=0.0 (Encourage) to d=1.0 (Challenge), with Encourage producing zero mastery gain but the largest engagement boost (+0.8). Three learner profiles (Struggling, Average, Advanced) vary initial knowledge, gain multiplier, and confusion threshold. (Oluseyi Olukolaa (2026))

### Claims

- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](../claims/engagement-optimized-rl-tutor-reward-hacking.md) [+W]
- [A multi-objective reward weighting mastery at 50% does not prevent reward hacking: the MO agent selects the zero-learning Encourage action more often (32.6%) than the engagement-only agent (25.8%)](../claims/multi-objective-reward-insufficient-reward-hacking.md) [+W]
- [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](../claims/constrained-architecture-reduces-rhsi.md) [+W]
- [Removing the behavioral-safety constraint (C3) causes degenerate policy collapse to near-single-action policies, making C3 the most influential safeguard in the ablation study](../claims/c3-ablation-policy-collapse.md) [+W]
- [The RHSI condition ordering is robust across a 20-cell window-size and demand-floor grid, with EO strictly worst in all cells, though ST–MAS ordering reverses at demand floors ≥0.45](../claims/rhsi-ordering-parameter-robustness.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237
