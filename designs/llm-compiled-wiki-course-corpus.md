---
type: design
id: llm-compiled-wiki-course-corpus
title: LLM-compiled wiki knowledge representation over an authentic course corpus
description: "An ingest-time knowledge representation in which a course corpus is compiled into a linked wiki: \"concept pages synthesized by an LLM, cross links between related pages, and citations from every page back to the raw s..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: brian-wright-2026
    resource: "https://arxiv.org/abs/2609.25303"
    title: "Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303"
    author: Brian Wright
---

# LLM-compiled wiki knowledge representation over an authentic course corpus

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An ingest-time knowledge representation in which a course corpus is compiled into a linked wiki: "concept pages synthesized by an LLM, cross links between related pages, and citations from every page back to the raw sourcematerials." At query time the LLM navigates and reads relevant pages rather than receiving similarity-ranked chunks. In this study it covered 12 pages (7 course concept pages such as K-Nearest Neighbors, Decision Trees, and ML Bias & Fairness, plus 5 navigational/meta pages) built from a frozen DS3001/DS3021 corpus snapshot, and served as Arm B in the head-to-head comparison against vector RAG.

## Design Implications

### Context
#### Requirements
- The corpus must be compiled at ingest into linked concept pages with explicit cross references and citations back to raw source materials, with the context budget matched across comparison arms.
#### Constraints
- Generalization is untested beyond a single course corpus (DS3001) and its topic mix; the evaluated wiki covered only the subset of DS 3021 compiled into 12 pages.

### Target Learners
- undergraduate machine learning students (DS3001/DS3021)

### Learning Goals
- answering course questions grounded in vetted course materials
- linking concepts across course units
- tracing claims back to source lectures and readings

### Claims
- Wiki Beats Vector Rag Course Qa Groundedness [+M]
- [Wiki Advantage Triples Cross Page Questions](../claims/wiki-advantage-triples-cross-page-questions.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303
