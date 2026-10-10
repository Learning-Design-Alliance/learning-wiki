---
type: product
id: agentschool
title: AgentSchool
description: AgentSchool is an LLM-powered multi-agent simulation system for modeling, inspecting, and comparing student–teacher interactions and learning trajectories in simulated educational settings.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# AgentSchool

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
AgentSchool is an LLM-powered multi-agent simulation system for modeling, inspecting, and comparing student–teacher interactions and learning trajectories in simulated educational settings.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Education modeled as a partially observable multi-agent state transition process**: AgentSchool's core explanatory framework treats an educational system as a dynamic state-transition process rather than static role-play. The paper states that "AgentSchool models an educational system as a partially observable, multi-agent state transition process," with system state comprising student and teacher internal states, scenery configuration, an interaction graph, and accumulated event history. Agents act on local observations, and a transition operator updates state, making trajectories generable, inspectable, and comparable rather than merely plausible dialogue. (AgentSchool: An LLM-Powered Multi-Agent Simulation for Education)
- **Cognitively growable student agents with weighted knowledge graphs, thinking-workflow pools, and explicit misconceptions**: Student agents are stateful learners rather than fixed personas. The paper states that "AgentSchool implements these components as a dialogue memory repository, a weighted subject knowledge graph, and a weighted thinking workflow pool," plus explicit misconception objects with persistence scores and stable learner attributes. Mastery updates follow a bounded transition formula combining instructional exposure quality, learner uptake, decay, and scaffolded support, so weakness can be localized to a node or subgraph and misconceptions persist until challenged. (AgentSchool: An LLM-Powered Multi-Agent Simulation for Education)

### Claims
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](../claims/structured-student-agents-differentiated-mastery-traces.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang. (2026). AgentSchool: An LLM-Powered Multi-Agent Simulation for Education. arXiv. https://arxiv.org/abs/2605.30144
