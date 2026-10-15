---
type: design
id: rl-sft-rl-multi-stage-pipeline
title: "RL-SFT-RL: a multi-stage pipeline combining pedagogically aligned RL, difficulty-weighted SFT on RL-generated synthetic data, and an optional second RL round"
description: "The article proposes a three-phase training framework formalized in Algorithm 1: an initial RL stage (DAPO with asymmetric clipping) that identifies and trains on the base model's hard negatives; an SFT phase that use..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: singh-2026
    resource: "https://arxiv.org/abs/2604.06385"
    title: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385"
    author: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R"
---

# RL-SFT-RL: a multi-stage pipeline combining pedagogically aligned RL, difficulty-weighted SFT on RL-generated synthetic data, and an optional second RL round

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes a three-phase training framework formalized in Algorithm 1: an initial RL stage (DAPO with asymmetric clipping) that identifies and trains on the base model's hard negatives; an SFT phase that uses the RL-trained model to synthesize training data, filtered and weighted by difficulty; and an optional second RL round reusing the Phase 1 hard dataset. The authors describe "a virtuous cycle of improvement" in which each stage builds on the previous one, and state the pipeline "comprising the initial RL stage for hard-negative identification, the difficulty-weighted SFT phase for knowledge distillation, and the optional final RL refinement" is formalized in Algorithm 1.

## Design Implications

### Context
#### Requirements
- A base model with a benchmark (here CDPK) usable to identify failure modes via repeated attempts, plus a reward model trained to prioritize pedagogically sound responses that guide learners rather than simply providing answers
#### Constraints
- The third RL stage is optional; the article reports primary results only on teacher-exam-style multiple-choice questions from CDPK

### Target Learners
- developers of educational AI tutors for classroom and platform integration

### Learning Goals
- cross-domain pedagogical knowledge (strategic teaching capacity distinct from content knowledge)

### Claims
- Rl Sft Rl Stage Wise Gains Cdpk [+M]
- [Dapo Over Grpo Pedagogical Rl](../claims/dapo-over-grpo-pedagogical-rl.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385. [doi:10.48550/arxiv.2604.06385](https://doi.org/10.48550/arxiv.2604.06385)
