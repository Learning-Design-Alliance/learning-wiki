---
type: product
id: agenticmath
title: AgenticMath
description: A Liu et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# AgenticMath

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A Liu et al. automated multi-agent framework that filters seed problems, iteratively generates and reviews new problems, produces solutions, and ranks synthetic question-answer data for LLM supervised fine-tuning.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AgenticMath four-stage multi-agent data generation framework**: AgenticMath is an automated multi-agent framework enforcing quality control at every stage of mathematical data generation. It proceeds in four stages: seed problem filtering (LLM scoring on complexity, information value, and clarity with k-NN score curation), agentic problem generation (rephrase, review, and revise agents with an iterative loop), solution generation (one-shot chain-of-thought prompting), and synthetic-data evaluation with ranking-based selection. The article describes it as "an automated multi-agent framework that enforces quality control at every stage of mathematical data generation," following a "Less Is More" principle to yield a data-efficient, high-quality dataset. (Xianyang Liu et al. (2025))

### Claims
- [Each AgenticMath component contributes performance gains, with the review-revise loop playing a particularly important role](../claims/agenticmath-ablation-all-modules-contribute.md) [+M]
- [Higher seed-problem filtering thresholds yield better downstream reasoning performance, indicating problem quality directly impacts results](../claims/higher-seed-filtering-thresholds-improve-reasoning.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Xianyang Liu, Yilin Liu, Shuai Wang, Hao Cheng, Andrew Estornell, Yuzhi Zhao, Jun Shu, Jiaheng Wei. (2025). AgenticMath: Enhancing LLM Reasoning via Agentic-based Math Data Generation. arXiv preprint. https://arxiv.org/abs/2510.19361
