---
type: design
id: five-dimension-curriculum-framework-llm
title: Metric-driven offline curriculum framework with five difficulty dimensions and two learning pathways
description: The article proposes a metric-driven offline curriculum framework that decomposes difficulty into five families—Problem Difficulty, Model Surprisal, Confidence Margin, Predictive Uncertainty, and Decision Variability—...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: yaning-jia-2025
    resource: "https://arxiv.org/abs/2510.19099"
    title: "Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. https://arxiv.org/abs/2510.19099"
    author: Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi
---

# Metric-driven offline curriculum framework with five difficulty dimensions and two learning pathways

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes a metric-driven offline curriculum framework that decomposes difficulty into five families—Problem Difficulty, Model Surprisal, Confidence Margin, Predictive Uncertainty, and Decision Variability—spanning problem-side and model-side perspectives, and constructs forward, reverse, single-tier, and group-based schedules under fixed training budgets. Its central explanatory account is that "internal-state metrics shape model properties such as confidence and uncertainty, while task-aligned metrics affect data fitting and generalization". The framework is used to attribute performance differences to data ordering alone, holding objectives, budgets, and optimization constant.

## Design Implications

### Context
#### Requirements
- An offline SFT setting where data are fixed but reordered, so that training objective, budget, and optimization procedure are held constant
#### Constraints
- The article states the offline design does not capture the adaptivity of online or self-paced curricula that evolve dynamically during training
- The analysis mainly examines solution accuracy and internal model states, not full reasoning trajectories or intermediate solution steps

### Target Learners
- Large language models undergoing supervised fine-tuning for mathematical reasoning

### Learning Goals
- Improved mathematical reasoning accuracy and generalization
- Calibration of internal confidence and uncertainty

### Claims
- [No Universal Curriculum Strategy Llm](../claims/no-universal-curriculum-strategy-llm.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yaning Jia, Chunhui Zhang, Xingjian Diao, Xiangchi Yuan, Zhongyu Ouyang, Chiyu Ma, and Soroush Vosoughi. (2025). What Makes a Good Curriculum? Disentangling the Effects of Data Ordering on LLM Mathematical Reasoning. https://arxiv.org/abs/2510.19099
