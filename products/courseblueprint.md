---
type: product
id: courseblueprint
title: CourseBlueprint
description: CourseBlueprint is a retrieval-augmented course-blueprint and instructional-video generation pipeline developed by Md Zabirul Islam et al.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CourseBlueprint

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
CourseBlueprint is a retrieval-augmented course-blueprint and instructional-video generation pipeline developed by Md Zabirul Islam et al. that uses typed pedagogy representations to sequence prerequisites, adapt explanations, and generate engagement-oriented narration.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CourseBlueprint typed pedagogy pipeline with scaffolding, adaptive style, and engagement modules**: CourseBlueprint is a retrieval-augmented pipeline that converts a topic and learner persona into a course blueprint rendered as an instructional video. It "replaces prompt chaining with typed intermediate representations": a scaffolding module builds a stage-labeled prerequisite concept graph with deterministic cycle removal, an adaptive controller assigns per-concept style specifications across depth, vocabulary, example density, abstraction, and analogy use, and an engagement generator emits narration following a fixed hook-retrieval-core-analogy-forward template. Each module can be disabled via a Boolean flag, enabling ablations by replacing its typed output with a default object. (Md Zabirul Islam et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608
