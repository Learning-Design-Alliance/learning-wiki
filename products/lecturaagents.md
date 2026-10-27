---
type: product
id: lecturaagents
title: LecturaAgents
description: LecturaAgents is a hierarchical multi-agent AI framework developed by Jaward Sesay and colleagues for generating and delivering personalized lectures using learner profiles, specialized agents, and embodied presentation.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# LecturaAgents

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
LecturaAgents is a hierarchical multi-agent AI framework developed by Jaward Sesay and colleagues for generating and delivering personalized lectures using learner profiles, specialized agents, and embodied presentation.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **LecturaAgents hierarchical multi-agent framework for end-to-end personalized lecture generation and embodied delivery**: LecturaAgents is a hierarchical multi-agent framework in which a ProfessorAgent coordinates validator and executor agents across two sessions, Lecture Preparation and Lecture Delivery, supported by LLM, Agent, TASA, and Memory modules. The article states it "mirrors a professor–student relationship, where a ProfessorAgent coordinates specialized assistant agents (at different hierarchies) to plan, research, review, and create lecture contents tailored for the individual learner." Agents collaborate through a Swarm-of-Ranks group chat with nine message types, and personalization conditions all generated artifacts on the learner profile, preferences, and usage history. (Jaward Sesay et al. (2026))
- **Teaching Action-Speech Alignment (TASA) algorithm for generating coherent embodied teaching action sequences**: TASA is the module that aligns embodied teaching actions with lecture speech. Per the article, "TASA uses a combination of LLM-based salience heuristics analysis and temporal semantic segmentation to help guide theTasaAgent with prospective relevant teaching action sequences." It segments slide contents and speech into labeled segments (Pedagogical, Personalized, Salient, Adaptive, Assessment), assigns each segment a Rough Notation or Handwriting action with a natural-language rationale, and outputs ordered action-speech sequences with word-level timestamps for the ProfessorAgent to execute during delivery. (Jaward Sesay et al. (2026))

### Claims
- [LecturaAgents scores higher than Instructional Agents, GenMentor, and Learn Your Way on lecture content, personalization, and assessment quality](../claims/lecturaagents-outperforms-baselines-lcq-pq-aq.md) [+M]
- [Frontier-model choice affects LecturaAgents performance, with Gemini 3 Pro ranking first at 80.4% AAR](../claims/lecturaagents-frontier-model-evaluation-aar.md) [+M]
- [Embodied teaching actions are spatially accurate across models, but temporal action–speech alignment remains more variable](../claims/lecturaagents-taq-spatial-strong-temporal-variable.md) [+M]

## Related Products and Programmes

- [Goal Net and Multi-Agent Development Environment (MADE)](goal-net-and-multi-agent-development-environment-made.md)

## Key Sources
- Jaward Sesay, Yue Yu, Siwei Dong, Börje F. Karlsson. (2026). Lect¯uraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching. arXiv. https://arxiv.org/abs/2606.16428
