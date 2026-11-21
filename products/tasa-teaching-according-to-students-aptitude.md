---
type: product
id: tasa-teaching-according-to-students-aptitude
title: "TASA (Teaching According to Students' Aptitude)"
description: A persona-, memory-, and forgetting-aware LLM mathematics tutoring framework developed by Yang Wu et al.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# TASA (Teaching According to Students' Aptitude)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A persona-, memory-, and forgetting-aware LLM mathematics tutoring framework developed by Yang Wu et al. that uses knowledge tracing and interaction histories to generate personalized explanations and practice questions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **TASA: a persona-, memory-, and forgetting-aware LLM tutoring framework**: TASA (Teaching According to Students' Aptitude) is a framework in which "a personalized mathematics tutoring framework that integrates three synergistic components into a unified LLM tutor: persona modeling, event memory, and forgetting-aware dynamics." A persona generator and memory generator extract a structured proficiency profile and event-level records from a student's interaction history; a hybrid retriever selects top entries; a knowledge-tracing-based forgetting score decays retrieved descriptions via a tuning-free LLM rewriting step; and a generator produces explanatory feedback plus a difficulty-calibrated next question. It is grounded in exponential memory decay from cognitive psychology. (Yang Wu et al. (2025))

### Claims
- [TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks](../claims/tasa-outperforms-llm-tutor-baselines.md) [+M]
- [Removing any of TASA's three modules degrades performance, with the forgetting score contributing an average 6.8% drop in normalized learning gain when eliminated](../claims/tasa-ablation-module-importance.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. https://arxiv.org/abs/2511.15163
