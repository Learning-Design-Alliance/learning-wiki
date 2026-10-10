---
type: strategy
id: domain-adapted-rag-for-mathematical-education
title: Domain-adapt RAG pipelines for mathematical education via entity recognition, notation-aware retrieval, and pedagogical re-ranking
description: "The article recommends adapting RAG to formal domains with three optimizations: mathematical entity recognition that distinguishes O(n) as Big-O from the letter O and recognizes proof markers; notation-aware similarit..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: sushan-adhikari-2026
    resource: "https://arxiv.org/abs/2609.14572"
    title: "Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572"
    author: Sushan Adhikari
---

# Domain-adapt RAG pipelines for mathematical education via entity recognition, notation-aware retrieval, and pedagogical re-ranking

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends adapting RAG to formal domains with three optimizations: mathematical entity recognition that distinguishes O(n) as Big-O from the letter O and recognizes proof markers; notation-aware similarity treating log n and log2 n as contextually equivalent with a lightweight CS knowledge graph; and pedagogical ranking that scores retrieved material on readability, step granularity, worked examples, and query difficulty so introductory queries surface introductory material. These "reflect the lesson from domain-specific RAG research that technical vocabulary and notation require explicit domain adaptation".

## Design Implications

### Context
#### Requirements
- A specialized named-entity recognition model trained on CS and mathematical text, and topic/difficulty labels on knowledge-base items
#### Constraints
- The authors report these components only appear to contribute to consistency; the lowest-performing topic (recurrence relations) suggests additional proof templates would be needed

### Target Learners
- undergraduate and graduate students querying formal technical domains

### Target Learning Goals
- retrieving pedagogically appropriate, notation-consistent explanations for algorithm and complexity questions

## Related Strategies

- Algorag Five Stage Rag Pipeline
- [Support Decoding of Text, Mathematical Notation, and Symbols](support-decoding-of-text-mathematical-notation-and-symbols.md)

## Examples
-

## Key Sources
- Sushan Adhikari. (2026). AlgoRAG: Retrieval-Augmented Generation for Theoretical Computer Science Education — A Comprehensive Evaluation Framework for Algorithm Analysis and Complexity Theory. arXiv preprint. https://arxiv.org/abs/2609.14572
