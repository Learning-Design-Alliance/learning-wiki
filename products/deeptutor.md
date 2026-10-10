---
type: product
id: deeptutor
title: DeepTutor
description: DeepTutor is an AI-powered personalized tutoring platform developed by Zhao et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# DeepTutor

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
DeepTutor is an AI-powered personalized tutoring platform developed by Zhao et al. that combines course-content retrieval with evolving learner-memory profiles to diagnose gaps and adapt explanations and practice.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Hybrid Personalization Engine: closed-loop personalization coupling static knowledge grounding with dynamic learner memory**: The Hybrid Personalization Engine is DeepTutor's explanatory architecture for personalized tutoring: it "couples static knowledge grounding with dynamic learner memory", pairing Static Knowledge Grounding (dual-index retrieval over course content) with Dynamic Personal Memory that distills multi-turn interactions into an evolving learner profile D=(Ds,Dw,Dr). The closed loop operationalizes formative assessment: "weaknesses diagnosed during problem tutoring propagate to Dw and directly shape which questions are generated next", while practice outcomes refine future explanations. Each completed interaction appends a trace tree and updates the profile, so every interaction personalizes the next. (Bingxi Zhao et al. (2026))
- **Trace Forest: hierarchical three-level learner memory with programmatic toolkit**: The Trace Forest is DeepTutor's hierarchical memory in which each tree records one complete tutoring interaction as a multi-resolution, semantically searchable artifact. "Nodes are organized into three levels: Level 1 stores session-level input and a global summary; Level 2 captures intermediate planning units; and Level 3 preserves fine-grained execution records including tool outputs, evidence, and validation outcomes." Every node carries a dense embedding for similarity-based retrieval. A TraceToolkit exposes three operations — SearchTrace, ListTraces, and ReadNodes — letting every agent explore learner history at the resolution it needs. (Bingxi Zhao et al. (2026))

### Claims
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](../claims/skg-dpm-complementary-ablation-deeptutor.md) [+M]
- [DeepTutor improves overall first-person interactive tutoring quality by 10.76% over a Naive Tutor baseline on TutorBench](../claims/deeptutor-improves-interactive-tutoring-quality-10-76.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Bingxi Zhao, Jiahao Zhang, Xubin Ren, Zirui Guo, Tianzhe Chu, Yi Ma, Chao Huang. (2026). DeepTutor: Towards Agentic Personalized Tutoring. Technical Report, The University of Hong Kong. https://arxiv.org/abs/2604.26962
