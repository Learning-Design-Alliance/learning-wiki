---
type: strategy
id: human-ai-division-of-labor-mcq-generation
title: "Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment"
description: "The article's central design recommendation is a principled division of labor: agentic AI with retrieval grounding and computational tools can serve as scalable first-line quality control for dimensions grounded in ex..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: xiaojing-duan-2026
    resource: "https://arxiv.org/abs/2604.03926"
    title: "Xiaojing Duan, Frederick Nwanganga, and Chaoli Wang. (2026). CODE-GEN: A Human-in-the-Loop RAG-Based Agentic AI System for Multiple-Choice Question Generation. https://arxiv.org/abs/2604.03926"
    author: Xiaojing Duan, Frederick Nwanganga, and Chaoli Wang
---

# Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's central design recommendation is a principled division of labor: agentic AI with retrieval grounding and computational tools can serve as scalable first-line quality control for dimensions grounded in explicit criteria and verifiable correctness (clarity, code validity, concept alignment, correct answer validity), while human experts remain essential for pedagogical depth, meaningful misconception targeting in distractors, and pedagogically rich feedback. The article states these findings "inform the strategic allocation of human and AI effort in AI-assisted educational content generation."

## Design Implications

### Context
#### Requirements
- Systematic validation of automated evaluator performance against human expert judgment rather than assuming evaluator reliability
#### Constraints
- Automated validation was prone to approving items that were technically correct but instructionally shallow

### Target Learners
- introductory programming students

### Target Learning Goals
- code reasoning and comprehension
- high-quality assessment item generation

### Affordances
- [Code Gen Dual Agent Architecture](../products/code-gen.md)

## Related Strategies

- [Use accuracy-rejection curves with reliability analysis to select operating points for selective delegation in human-in-the-loop grading](arc-based-selective-delegation-grading.md)
- [Use automated collaboration assessments as scaffolds for reflection rather than ground truth](collaboration-assessments-as-reflection-scaffolds.md)
- [Use observable pedagogical variables as metadata to support teachers' explicit selection and integration of digital resources](metadata-variables-support-teacher-resource-selection.md)
- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)

## Examples
-

## Key Sources
- Xiaojing Duan, Frederick Nwanganga, and Chaoli Wang. (2026). CODE-GEN: A Human-in-the-Loop RAG-Based Agentic AI System for Multiple-Choice Question Generation. https://arxiv.org/abs/2604.03926
