---
type: product
id: cares
title: CARES
description: CARES is a multi-agent conversational AI system developed by Yang et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# CARES

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2`–`q3` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
CARES is a multi-agent conversational AI system developed by Yang et al. that supports construction-safety reporting by retrieving regulatory guidance, guiding users through dialogue, and generating structured daily reports.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Multi-agent conversational coordination with specialized agents sharing session state**: CARES replaces a single monolithic prompt with specialized agents that "share the same session state and coordinate with each other via structured message passing": a dialogue agent that guides the conversation toward unfilled report fields, a knowledge agent handling RAG queries, an extraction agent that re-derives a structured JSON snapshot after every turn, and a reporting agent that serializes the snapshot into a standardized PDF. (Yang et al. (2026))

### Claims

- [CARES achieved an overall majority-vote faithfulness score of 0.74, with most factual claims supported by retrieved regulatory context](../claims/cares-faithfulness-074.md) [+M]
- [CARES achieved an overall answer relevance score of 1.00, consistently addressing the user's immediately preceding message](../claims/cares-answer-relevance-100.md) [+M]
- [Initial retrieval ranking in CARES was weak, with a pooled Retrieval Precision Proxy@4 of 0.17](../claims/cares-retrieval-precision-proxy-017.md) [~M]
- [Multi-agent AI standardized patient training improved final OSCE-aligned examination scores compared with a structured non-LLM control condition](../claims/ma-scaffolding-improves-osce-exam-score.md) [+W]

## Related Products and Programmes

- [MeduAI-SP](meduai-sp.md)

## Key Sources
- Yang, F.; Wu, J.; Tian, Y.; and Zhang, J. (2026). CARES: A Conversational AI System for Regulation-Grounded Safety Reporting in Construction Education. [doi:10.48550/arxiv.2609.19429](https://doi.org/10.48550/arxiv.2609.19429)
