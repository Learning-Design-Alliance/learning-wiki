---
type: design
id: ai-kg-integrated-pathology-teaching-system
title: AI–knowledge graph integrated pathology teaching system (dual-core architecture with 89 knowledge points, 356 weighted relations, and three AI modules)
description: "A teaching system combining a pathology knowledge graph with an AI teaching assistant in a closed-loop architecture of \"knowledge guiding learning and learning feeding back to knowledge.\" The knowledge graph contains..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: yuanyuan-yu-2026
    resource: "https://doi.org/10.1186/s12909-026-09348-8"
    title: "Yuanyuan Yu, Ying Yuan. (2026). Application and effectiveness analysis of AI Intelligent tutoring system combined with knowledge graph in basic medical pathology teaching. BMC Medical Education. https://doi.org/10.1186/s12909-026-09348-8"
    author: Yuanyuan Yu, Ying Yuan
---

# AI–knowledge graph integrated pathology teaching system (dual-core architecture with 89 knowledge points, 356 weighted relations, and three AI modules)

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A teaching system combining a pathology knowledge graph with an AI teaching assistant in a closed-loop architecture of "knowledge guiding learning and learning feeding back to knowledge." The knowledge graph contains "89 core knowledge points, 356 weighted relations" built from a standard textbook and validated by five senior pathology professors. The AI assistant comprises a knowledge-aware recommendation module, a pathology-adapted BERT QA module, and a dynamic path planning module; the AI feeds students' high-frequency errors back to the graph to adjust relation weights.

## Design Implications

### Context
#### Requirements
- Reviewed and validated knowledge graph content by senior pathology professors
- Daily student use of weak-point diagnosis and associated exercises with a minimum effective usage duration to avoid formal login
#### Constraints
- All performance metrics are based on internal tests using a separate cohort; no independent external validation has been performed, and benchmarks remain internal, non-blinded, and without pre-registered thresholds

### Target Learners
- First-year nursing students in basic medical pathology courses

### Learning Goals
- Structured systematic construction of pathology knowledge
- Personalized learning and understanding of complex pathological mechanisms

### Claims
- Ai Kg Pathology Final Exam Improvement [+M]
- [Ai Kg Knowledge Mastery Rate](../claims/ai-kg-knowledge-mastery-rate.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Yuanyuan Yu, Ying Yuan. (2026). Application and effectiveness analysis of AI Intelligent tutoring system combined with knowledge graph in basic medical pathology teaching. BMC Medical Education. https://doi.org/10.1186/s12909-026-09348-8
