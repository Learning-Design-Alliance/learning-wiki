---
type: research-method
id: history-conditioned-student-simulation-two-component-profile-generator-plus-simulator-fram
title: "History-conditioned student simulation: two-component profile-generator-plus-simulator framework"
description: "The article establishes the task of history-conditioned student simulation, where a model predicts a student's next tutoring-dialogue turn conditioned on their prior question-answering and dialogue history."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# History-conditioned student simulation: two-component profile-generator-plus-simulator framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article establishes the task of history-conditioned student simulation, where a model predicts a student's next tutoring-dialogue turn conditioned on their prior question-answering and dialogue history. "We propose a two-component framework in which a profile generator summarizes a student's history and a simulator predicts student turns conditioned on the resulting profile." Both components are trained with reinforcement learning so that profiles are optimized for faithful downstream simulation: the simulator is fine-tuned with SFT then DPO against counterfactual mismatched profiles, and the profile generator is distilled then refined with GRPO using ground-truth turn log-likelihood as reward.

## Accounts
<!-- How each source describes or uses the method -->
- **History-conditioned student simulation: two-component profile-generator-plus-simulator framework**: The article establishes the task of history-conditioned student simulation, where a model predicts a student's next tutoring-dialogue turn conditioned on their prior question-answering and dialogue history. "We propose a two-component framework in which a profile generator summarizes a student's history and a simulator predicts student turns conditioned on the resulting profile." Both components are trained with reinforcement learning so that profiles are optimized for faithful downstream simulation: the simulator is fine-tuned with SFT then DPO against counterfactual mismatched profiles, and the profile generator is distilled then refined with GRPO using ground-truth turn log-likelihood as reward. (Zhangqi Duan et al. (2026))

### Claims
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](../claims/rl-stages-needed-faithful-student-simulation.md) [+M]
- [Question-answering and dialogue histories are complementary views of the same student, with signals transferring across metric categories](../claims/qa-dialogue-histories-complementary-views.md) [+M]

## Related Research Methods
-

## Key Sources
- Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051
