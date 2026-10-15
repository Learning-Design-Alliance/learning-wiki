---
type: research-method
id: neural-expected-increment-model-with-upper-bounded-softmax-for-next-skill-prediction
title: Neural expected-increment model with Upper Bounded Softmax for next-skill prediction
description: The article introduces a feed-forward neural model that maps a continuous mastery state to a distribution over the next skill using the Upper Bounded Softmax function, which assigns probability mass only to currently unmastered skills.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Neural expected-increment model with Upper Bounded Softmax for next-skill prediction

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The article introduces a feed-forward neural model that maps a continuous mastery state to a distribution over the next skill using the Upper Bounded Softmax function, which assigns probability mass only to currently unmastered skills. Parameters are trained by minimizing squared reconstruction error of observed mastery patterns with L1 regularization that "promotes sparse and interpretable dependencies among skills." Repeatedly accumulating expected increments approximates intermediate acquisition states.

## Accounts
<!-- How each source describes or uses the method -->
- **Neural expected-increment model with Upper Bounded Softmax for next-skill prediction**: The article introduces a feed-forward neural model that maps a continuous mastery state to a distribution over the next skill using the Upper Bounded Softmax function, which assigns probability mass only to currently unmastered skills. Parameters are trained by minimizing squared reconstruction error of observed mastery patterns with L1 regularization that "promotes sparse and interpretable dependencies among skills." Repeatedly accumulating expected increments approximates intermediate acquisition states. (Ryosuke Nagai et al. (2026))

### Claims

## Related Research Methods
-

## Key Sources
- Ryosuke Nagai, Kyohei Atarashi, Koh Takeuchi, Jill-Jênn Vie, and Hisashi Kashima. (2026). Estimating Learners' Skill Acquisition Without Temporal Information. https://arxiv.org/abs/2606.20611
