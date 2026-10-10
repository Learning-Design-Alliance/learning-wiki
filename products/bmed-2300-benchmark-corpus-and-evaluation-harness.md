---
type: product
id: bmed-2300-benchmark-corpus-and-evaluation-harness
title: BMED 2300 benchmark corpus and evaluation harness
description: A benchmark dataset and evaluation harness developed by Md Zabirul Islam et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# BMED 2300 benchmark corpus and evaluation harness

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
A benchmark dataset and evaluation harness developed by Md Zabirul Islam et al. containing course lectures, slides, aligned transcripts, and automated metrics for evaluating pedagogical video generation.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **BMED 2300 benchmark corpus and evaluation harness for course-grounded pedagogical video generation**: A reusable benchmark artifact built from the BMED 2300 Bio-Imaging course, packaged with "twenty-three lectures, 1,116 slides, aligned transcripts, a multi-repetition LLM-judge rubric, and regex-grounded objective metrics." Chunks are slide-granular, each embedding preserving a one-to-one link between a textual explanation and its slide image, stored in a flat inner-product FAISS index with 3,072-dimensional vectors. The harness pairs repeated LLM-judge rubric scoring (1-5 scale, n=3 reps) with deterministic metrics such as Flesch reading ease and regex counts of analogies and retrieval prompts. (Md Zabirul Islam et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608
