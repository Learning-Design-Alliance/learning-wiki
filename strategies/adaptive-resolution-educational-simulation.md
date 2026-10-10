---
type: strategy
id: adaptive-resolution-educational-simulation
title: "Adaptive-resolution simulation: allocate more LLM calls to educationally consequential moments and compress routine transitions"
description: To manage the coupled trade-off among scale, duration, and granularity, the paper recommends making the simulation budget configurable and concentrating generative detail where it matters.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: yulei-ye-2026
    resource: "https://arxiv.org/abs/2605.30144"
    title: "Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang. (2026). AgentSchool: An LLM-Powered Multi-Agent Simulation for Education. arXiv. https://arxiv.org/abs/2605.30144"
    author: Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang
---

# Adaptive-resolution simulation: allocate more LLM calls to educationally consequential moments and compress routine transitions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To manage the coupled trade-off among scale, duration, and granularity, the paper recommends making the simulation budget configurable and concentrating generative detail where it matters. As printed: "Efficiency is achieved by adaptive resolution. The simulator can allocate more LLM calls to educationally consequential moments, such as misconception diagnosis, teacher reflection, conflict resolution, or high-stakes assessment, while compressing routine transitions into structured updates." Caching of stable agent profiles and memory retrieval further reduce runtime while preserving validation-relevant detail.

## Design Implications

### Context
#### Requirements
- Mixed granularity support so important lessons can be simulated turn by turn while routine practice is compressed into state updates with summary evidence
#### Constraints
- The simulation budget B ≈ N·H·(1/Δt)·c_step is finite, so every simulator implicitly decides which educational mechanisms remain visible

### Target Learners
- Researchers running multi-agent educational simulations across turn, lesson, and semester granularities

### Target Learning Goals
- Preserving visibility of misconception repair, scaffolding, and social dynamics within computational budgets

### Affordances
- [Education As Multi Agent State Transition](../products/agentschool.md)

## Related Strategies

- [Time Management In Instruction](time-management-in-instruction.md)
- [Team training with variable leadership roles and simulated communication delays](team-training-variable-leadership-communication-delays.md)

## Examples
-

## Key Sources
- Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang. (2026). AgentSchool: An LLM-Powered Multi-Agent Simulation for Education. arXiv. https://arxiv.org/abs/2605.30144
