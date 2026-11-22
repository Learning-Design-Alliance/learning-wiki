---
type: research-method
id: three-condition-pedagogical-reinforcement-learning-reward-framework
title: Three-condition pedagogical reinforcement-learning reward framework
description: "The article proposes that whether a learning-gain reward favors teaching over telling depends on how learning is measured, realized as \"amasked near-transfer post-test\" plus \"two binary reward gates\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Three-condition pedagogical reinforcement-learning reward framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 3 studies (3 causal), `q1`–`q2` · 0 of 3 report an effect size · 5 claims rest on one study

## Description
The article proposes that whether a learning-gain reward favors teaching over telling depends on how learning is measured, realized as "amasked near-transfer post-test" plus "two binary reward gates". Drawing on the Assistance Dilemma and ICAP, condition (1) tests the student on an unseen variant, condition (2) masks the tutor's utterances so reward flows only through student-authored turns, and condition (3) makes handover costly as a constraint rather than a traded-off penalty, allowing one fixed hyperparameter setting from 4B to 27B. This is the article's explanatory framework for pedagogical RL reward design.

## Accounts
<!-- How each source describes or uses the method -->
- **Three conditions on measuring learning for pedagogical RL: transfer, student-notes-only masking, and the cost of telling via binary reward gates**: The article proposes that whether a learning-gain reward favors teaching over telling depends on how learning is measured, realized as "amasked near-transfer post-test" plus "two binary reward gates". Drawing on the Assistance Dilemma and ICAP, condition (1) tests the student on an unseen variant, condition (2) masks the tutor's utterances so reward flows only through student-authored turns, and condition (3) makes handover costly as a constraint rather than a traded-off penalty, allowing one fixed hyperparameter setting from 4B to 27B. This is the article's explanatory framework for pedagogical RL reward design. (Jakub Macina et al. (2026))

### Claims

- [A learning-gain reward alone does not separate teaching from telling: a policy trained without the binary gates hands over the solution in 61% of dialogs at the same simulated gain](../claims/learning-gain-reward-alone-does-not-separate-teaching-from-telling.md) [+W]
- [The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches](../claims/gates-decide-whether-tutor-tells-transfer-shapes-how.md) [+W]
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](../claims/eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) [+W]
- [Adding gate-failure penalties based on predefined pedagogical criteria harms teaching performance and generalization, while training on student improvement alone allows broader capabilities to emerge](../claims/gate-penalties-harm-generalization-student-improvement-reward.md) [~W]
- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](../claims/engagement-optimized-rl-tutor-reward-hacking.md) [+W]

## Related Research Methods
-

## Key Sources
- Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. https://arxiv.org/abs/2610.06446
