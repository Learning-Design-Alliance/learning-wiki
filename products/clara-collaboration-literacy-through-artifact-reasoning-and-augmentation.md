---
type: product
id: clara-collaboration-literacy-through-artifact-reasoning-and-augmentation
title: CLARA (Collaboration Literacy through Artifact Reasoning and Augmentation)
description: CLARA is an agentic analytics system developed by Dawei Xie and colleagues that transcribes discussions, generates and indexes collaboration artifacts, and provides artifact-grounded analyses for learners and educators.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CLARA (Collaboration Literacy through Artifact Reasoning and Augmentation)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
CLARA is an agentic analytics system developed by Dawei Xie and colleagues that transcribes discussions, generates and indexes collaboration artifacts, and provides artifact-grounded analyses for learners and educators.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CLARA agentic analytics system**: CLARA (Collaboration Literacy through Artifact Reasoning and Augmentation) is an agentic analytics system that transcribes discussions in real time, computes psycholinguistic metrics, and uses GPT-4.1 to generate concept maps and 7C collaboration assessments from transcripts. Artifacts are embedded with text-embedding-3-large and indexed into distinct ChromaDB collections, and a ReAct agent built with LangGraph and GPT-4.1-mini iteratively calls six tools (including search_sessions, get_concept_map, get_assessment, get_speaker_profile) to synthesize responses traceable to stored artifacts. Users can explore artifacts on a dashboard and constrain which artifact types the agent may consult. (Dawei Xie et al. (2026))

### Claims
- [LLM-generated 7C collaboration assessment scores fall within the range of human expert variability across ten discussions](../claims/llm-7c-scores-within-expert-variability.md) [+M]
- [Artifact-grounded agent responses are rated significantly higher than transcript-only responses on groundedness, analytical depth, helpfulness, relevance, and overall quality](../claims/artifact-grounded-responses-rated-higher.md) [+M]
- [Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations](../claims/artifact-indexing-improves-analytical-retrieval.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Dawei Xie, Khalil Anderson, Tochukwu Eze, Chenghong Lin, Bookyung Shin, and Marcelo Worsley. (2026). CLARA: An AI-Augmented Analytics Dashboard for Collaboration Literacy. https://arxiv.org/abs/2605.17259
