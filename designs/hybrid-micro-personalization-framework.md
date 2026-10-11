---
type: design
id: hybrid-micro-personalization-framework
title: "Hybrid micro-level personalization framework combining learner-driven preferences with system-driven Bloom's Taxonomy cognitive assessment"
description: A framework for personalizing LLM/RAG teaching assistants at the level of individual student questions.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: saptarshi-basu-2026
    resource: "https://arxiv.org/abs/2609.03402"
    title: "Saptarshi Basu, Sandeep Kakar, Ashok Goel. (2026). A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant. https://arxiv.org/abs/2609.03402"
    author: Saptarshi Basu, Sandeep Kakar, Ashok Goel
---

# Hybrid micro-level personalization framework combining learner-driven preferences with system-driven Bloom's Taxonomy cognitive assessment

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A framework for personalizing LLM/RAG teaching assistants at the level of individual student questions. It represents learner characteristics through self-assessed metacognitive knowledge and question-level cognitive complexity via Bloom's Taxonomy, plus five Felder-Silverman-derived preferences (abstraction, verbosity, perception, processing, understanding). The article states "The combination of learner characteristics and preferences produces 96 distinct learner profiles" and that "This creates a hybrid framework combining learner-driven adaptability with system-driven adaptivity." It contrasts with prior adaptive systems that adapt content selection or sequencing by instead adapting response form.

## Design Implications

### Context
#### Requirements
- Learner preferences are explicitly selected by students while cognitive demand is inferred by the system via a fine-tuned BERT-based Bloom classifier (0.92 test accuracy)
- An engineered prompt encoding all learner attributes must condition the LLM within the existing RAG pipeline and course-specific knowledge base
#### Constraints
- Personalization modifies the form and presentation of responses while preserving grounding in retrieved instructional content
- Treated as user-selected preferences rather than fixed psychometric classifications

### Target Learners
- online and course-based higher-education students (e.g., KBAI graduate course)

### Learning Goals
- tailoring instructional explanations to learner preferences and question cognitive complexity

### Claims
- [Prompt Personalization Measurable Response Variation](../claims/prompt-personalization-measurable-response-variation.md) [+M]
- [Abstraction Processing Significant Self Assessment Not](../claims/abstraction-processing-significant-self-assessment-not.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Saptarshi Basu, Sandeep Kakar, Ashok Goel. (2026). A Prompt-Engineering Approach to Develop Scalable, Flexible, and Real-Time Hybrid Micro-Level Personalization in a General Purpose AI Teaching Assistant. https://arxiv.org/abs/2609.03402
