---
type: design
id: heuristicedu-sft-grpo-pipeline
title: "HeuristicEdu: an SFT-then-GRPO alignment pipeline with a three-component heuristic reward for Socratic tutoring"
description: HeuristicEdu is a two-phase alignment pipeline that redirects an instruction-tuned LLM from direct answer delivery toward Socratic guided inquiry.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: xiaokun-wang-2026
    resource: "https://arxiv.org/abs/2607.22996"
    title: "Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996"
    author: Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou
---

# HeuristicEdu: an SFT-then-GRPO alignment pipeline with a three-component heuristic reward for Socratic tutoring

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
HeuristicEdu is a two-phase alignment pipeline that redirects an instruction-tuned LLM from direct answer delivery toward Socratic guided inquiry. Phase 1 is supervised fine-tuning on the SocraticEdu corpus; Phase 2 applies GRPO with the composite reward Rtotal = αRcog + βReng − γRdir, where Rcog measures normalized Bloom's-taxonomy cognitive lift between turns via an LLM judge, Reng scores engagement cues via an Engagement Proxy Model, and Rdir penalizes novel keyword leakage with a Kquery correction for student-introduced terms. The article states "Section 7 shows that γ= 0is optimal in practice", and the pipeline includes inference-time spell correction and intent filtering before evaluation with SE and CD metrics.

## Design Implications

### Context
#### Requirements
- A supervised warm-up corpus of Socratic trajectories (SocraticEdu, 797 trajectories)
- An LLM judge for Bloom's levels and an Engagement Proxy Model for reward scoring
- Curated keyword sets Ki per seed question for the directness term and leakage evaluation
#### Constraints
- The directness penalty Rdir is harmful as a GRPO reward (γ=0 optimal in practice), though explicit term constraints can reduce inference-time leakage
- Results are demonstrated on Qwen2.5-7B-Instruct with a 30-question held-out test set; margins below 0.10 are treated as indicative

### Target Learners
- Chinese primary-school students ages 8-12 in K-12 science platforms

### Learning Goals
- Guided discovery of core science concepts through progressive Socratic questioning rather than direct answer delivery

### Claims
- [Directness Penalty Harmful As Grpo Reward](../claims/directness-penalty-harmful-as-grpo-reward.md) [+M]
- [Grpo Without Directness Raises Socratic Scaffolding Effectiveness](../claims/grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) [+M]

## Related Designs

- [cc-self-train adaptive learning system: a three-layer hook-based engagement observation and scaffolding adjustment mechanism](cc-self-train-adaptive-learning-system.md)

## Examples
-

## Key Sources
- Xiaokun Wang, Siyu Song, Wentao Liu, Xiaodong Zou. (2026). Beyond Direct Answering: Aligning Educational LLMs as Socratic Guides via Heuristic Reinforcement Learning. arXiv preprint. https://arxiv.org/abs/2607.22996
