---
type: product
id: autograder
title: Autograder+
description: Autograder+ is a modular, multi-stage programming autograding and feedback platform developed by its authors, combining static and sandboxed dynamic code analysis with AI-generated feedback and instructor analytics.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Autograder+

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Autograder+ is a modular, multi-stage programming autograding and feedback platform developed by its authors, combining static and sandboxed dynamic code analysis with AI-generated feedback and instructor analytics.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Autograder+ modular multi-stage autograding pipeline**: Autograder+ is an end-to-end framework that evolves autograding from summative evaluation into a formative learning platform. As the article states, "Autograder+ is architected as a modular, multi-stage pipeline designed to systematically process student submissions, enriching them at each step with layers of analysis." Its stages are code ingestion, a static analysis engine (AST parsing, constraint checks), a Docker-sandboxed dynamic execution engine, a semantic core containing an embedding engine and a feedback engine with prompt pooling, and reporting/analytics engines producing per-student Markdown reports and interactive UMAP scatter plots for instructors. Code is available at the released GitHub repository. (Autograder+: A Multi-Faceted AI Framework for Rich Pedagogical Feedback in Programming Edu)

### Claims
- [Prompt pooling raises both lexical and semantic alignment of LLM feedback with TA-written gold-standard feedback across models](../claims/prompt-pooling-raises-feedback-alignment.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Vikrant Sahu, Dr. Gagan Raj Gupta, Raghav Borikar, and Nitin Mane. 2025. Autograder+: A Multi-Faceted AI Framework for Rich Pedagogical Feedback in Programming Education. CODS '25. https://arxiv.org/abs/2510.26402
