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
> **Evidence** · 5 claims (5 for) · 2 studies (1 causal, 1 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article establishes the task of history-conditioned student simulation, where a model predicts a student's next tutoring-dialogue turn conditioned on their prior question-answering and dialogue history. "We propose a two-component framework in which a profile generator summarizes a student's history and a simulator predicts student turns conditioned on the resulting profile." Both components are trained with reinforcement learning so that profiles are optimized for faithful downstream simulation: the simulator is fine-tuned with SFT then DPO against counterfactual mismatched profiles, and the profile generator is distilled then refined with GRPO using ground-truth turn log-likelihood as reward.

## Accounts
<!-- How each source describes or uses the method -->
- **History-conditioned student simulation: two-component profile-generator-plus-simulator framework**: The article establishes the task of history-conditioned student simulation, where a model predicts a student's next tutoring-dialogue turn conditioned on their prior question-answering and dialogue history. "We propose a two-component framework in which a profile generator summarizes a student's history and a simulator predicts student turns conditioned on the resulting profile." Both components are trained with reinforcement learning so that profiles are optimized for faithful downstream simulation: the simulator is fine-tuned with SFT then DPO against counterfactual mismatched profiles, and the profile generator is distilled then refined with GRPO using ground-truth turn log-likelihood as reward. (Zhangqi Duan et al. (2026))
- **INSIDE: internal dialogue as an intermediate cognitive layer preceding student actions in LLM student simulation**: INSIDE is a student-modeling framework that fine-tunes LLMs to generate a verbalized internal dialogue before producing the student's next code submission. A teacher LLM (GPT-5) performs retrospective inference over the interaction context and the observed next submission, first producing structured cognitive, affective, and action states inspired by Bloom's Taxonomy, then a first-person think trace used as fine-tuning supervision. The article states that "INSIDE introduces internal dialogue as an intermediate cognitive layer that precedes student actions during learning interactions, capturing the intent that leads to each attempt rather than only explaining mistakes after the fact." Unlike reconstructive post-hoc accounts of errors, the framework models reasoning that precedes each attempt, jointly modeling how and why students act. (Rose Niousha et al. (2026))

### Claims

- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](../claims/rl-stages-needed-faithful-student-simulation.md) [+M]
- [Question-answering and dialogue histories are complementary views of the same student, with signals transferring across metric categories](../claims/qa-dialogue-histories-complementary-views.md) [+M]
- [Fine-tuning with INSIDE internal dialogue achieves the lowest Wasserstein distances to real student code distributions on test_OP across all action-fidelity metrics](../claims/inside-lowest-wasserstein-action-fidelity-test-op.md) [+M]
- [INSIDE fine-tuning achieves the highest alignment between generated internal dialogue and ground-truth student code edits, up to 57.9%](../claims/inside-highest-reasoning-alignment-57-9.md) [+M]
- [GRPO training shifts profiles from broad summaries toward diagnostic, behaviorally grounded representations that better support simulation](../claims/grpo-refines-profiles-toward-diagnostic-representations.md) [+W]

## Related Research Methods

- [Multi-turn synthetic-dialogue evaluation protocol for AI tutors](multi-turn-synthetic-dialogue-evaluation-protocol-for-ai-tutors.md)

## Key Sources
- Zhangqi Duan, Shuyan Huang, Alexander Scarlatos, Jaewook Lee, Simon Woodhead, Andrew Lan. (2026). Who Am I? History-Aware Profiles for Student Simulation in Tutoring Dialogues. arXiv preprint. https://arxiv.org/abs/2605.30051
- Rose Niousha, Minwoo Kang, Narges Norouzi. (2026). INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2608.10492
