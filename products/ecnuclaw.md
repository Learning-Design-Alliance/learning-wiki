---
type: product
id: ecnuclaw
title: ECNUClaw
description: An open-source Python framework developed by Yizhou Zhou et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# ECNUClaw

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An open-source Python framework developed by Yizhou Zhou et al. for building learner-profiled intelligent study companions for K–12 subject learning and emotional and metacognitive support.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Five-dimension learner profile maintained across subject switches from dialogue signals**: ECNUClaw constructs and maintains a learner profile across five dimensions—cognitive, behavioral, emotional, metacognitive, and contextual—stored as per-dimension JSON fields in a SQLite table. Signals are extracted at every turn via keyword dictionaries and turn counting: Bloom's taxonomy level from question patterns, weak knowledge points from error markers, mood and self-efficacy from sentiment keywords, and reflection and strategy preference from metacognitive markers. All subject companions share a single memory store, so the profile persists across subject switches. (Yizhou Zhou et al. (2026))

### Claims

- [The system has no empirical evaluation yet: profile accuracy has not been assessed and learning outcomes remain an open question](../claims/ecnuclaw-no-empirical-evaluation-yet.md) [+W]
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](../claims/prompt-engineering-adaptation-transparency-tradeoff.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Yizhou Zhou, Jiayin Li, and Zhi Zhang. (2026). ECNUClaw: A Learner-Profiled Intelligent Study Companion Framework for K-12 Personalized Education. arXiv preprint. https://arxiv.org/abs/2605.08040
