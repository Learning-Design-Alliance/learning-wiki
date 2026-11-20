---
type: product
id: sensemo
title: SensEmo
description: SensEmo is a Markov-decision-process and reinforcement-learning classroom controller developed by Kushan Choksi et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# SensEmo

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
SensEmo is a Markov-decision-process and reinforcement-learning classroom controller developed by Kushan Choksi et al. that uses collective emotion, attention, and student-preference data to recommend instructional pacing and content adjustments.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **SensEmo's MDP-based affective learning controller adapts teaching content and pace from collective student emotion**: SensEmo's controller is a Markov Decision Process trained via reinforcement learning that takes the current collective emotional state and student preferences as input and selects actions (increase/decrease pace, simplify/no change in content) to keep students in a state of curiosity, "characterized by relaxed alertness". The collective emotion state is "defined as the weighted average of the individual emotions". Value iteration yields an optimal policy, with sub-optimal policies stored as fallbacks when optimal suggestions are infeasible. (Kushan Choksi et al. (2024))

### Claims
- [In an in-person classroom, a session with real-time SensEmo feedback showed more curiosity, less boredom, and higher quiz scores than a session without feedback, despite non-randomization](../claims/sensemoo-classroom-feedback-session-higher-quiz.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Kushan Choksi, Hongkai Chen, Karan Joshi, Sukrutha Jade, Shahriar Nirjon, and Shan Lin. (2024). SensEmo: Enabling Affective Learning through Real-time Emotion Recognition with Smartwatches. arXiv preprint. https://arxiv.org/abs/2407.09911
