---
type: strategy
id: hierarchical-rag-global-discourse-map-strategy
title: Use a hierarchical RAG approach combining local timestamped metadata with a global thematic discourse map for abstract topics
description: "The authors propose extending the platform's retrieval architecture for abstract concepts like pragmatics or discourse analysis, which \"require a 'global' understanding of context that spans the entire lecture rather..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: mohammed-abraar-raj-2026
    resource: "https://arxiv.org/abs/2604.15334"
    title: "Mohammed Abraar Raj, Abhijit Dandekar, Rajat Dandekar, Sreedath Panat. (2026). Beyond Passive Viewing: A Pilot Study of a Hybrid Learning Platform Augmenting Video Lectures with Conversational AI. https://arxiv.org/abs/2604.15334"
    author: Mohammed Abraar Raj, Abhijit Dandekar, Rajat Dandekar, Sreedath Panat
---

# Use a hierarchical RAG approach combining local timestamped metadata with a global thematic discourse map for abstract topics

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors propose extending the platform's retrieval architecture for abstract concepts like pragmatics or discourse analysis, which "require a 'global' understanding of context that spans the entire lecture rather than a single timestamped 'local' segment". A hierarchical RAG would combine local timestamped metadata with a global thematic discourse map, enabling the tutor to facilitate deeper theoretical debates without oversimplification as curriculum complexity increases.

## Design Implications

### Context
#### Requirements
- Requires combining local timestamped segment metadata with a global thematic discourse map of the lecture
#### Constraints
- The current timestamped local-segment architecture provides high-fidelity grounding for procedural or technical topics but not for topics needing lecture-wide context

### Target Learners
- Learners studying advanced NLP concepts

### Target Learning Goals
- Understanding abstract NLP concepts such as pragmatics, discourse analysis, and compositional vs. distributional semantics

## Claims

- [Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations](../claims/artifact-indexing-improves-analytical-retrieval.md) [+W]

## Related Strategies

- [Augment LLMs with retrieval-augmented generation using authoritative subspecialty resources to address remaining knowledge gaps on board-style examinations.](rag-subspecialty-resources-llm-knowledge-gaps.md)

## Examples
-

## Key Sources
- Mohammed Abraar Raj, Abhijit Dandekar, Rajat Dandekar, Sreedath Panat. (2026). Beyond Passive Viewing: A Pilot Study of a Hybrid Learning Platform Augmenting Video Lectures with Conversational AI. https://arxiv.org/abs/2604.15334
