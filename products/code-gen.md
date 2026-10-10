---
type: product
id: code-gen
title: CODE-GEN
description: CODE-GEN is a retrieval-augmented, dual-agent educational AI system developed by Xiaojing Duan et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CODE-GEN

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CODE-GEN is a retrieval-augmented, dual-agent educational AI system developed by Xiaojing Duan et al. that generates course-grounded coding-comprehension questions and uses an independent Validator agent and execution tools to assess their pedagogical quality.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CODE-GEN dual-agent architecture separating generation from validation**: CODE-GEN is a human-in-the-loop agentic AI system integrating retrieval-augmented generation with a dual-agent architecture: a Generator agent produces multiple-choice coding comprehension questions grounded in retrieved course context, and a Validator agent independently assesses each question across seven pedagogical dimensions. Both agents are augmented with an Arithmetic Expression Evaluator and a Sandboxed Python Runner. The article states the separation "allows the system to decouple the creative task of question generation from the analytical task of quality evaluation" and treats automated validation as an empirical object of study rather than an assumed capability. (Xiaojing Duan et al. (2026))

### Claims
- [CODE-GEN achieves human-validated success rates of 79.9% to 98.6% across seven pedagogical evaluation dimensions](../claims/code-gen-success-rates-seven-dimensions.md) [+M]
- [Concept alignment achieves the highest success rate (98.6%) among the seven dimensions, attributed to the RAG-based design](../claims/code-gen-concept-alignment-highest-success.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Xiaojing Duan, Frederick Nwanganga, and Chaoli Wang. (2026). CODE-GEN: A Human-in-the-Loop RAG-Based Agentic AI System for Multiple-Choice Question Generation. https://arxiv.org/abs/2604.03926
